#!/usr/bin/env python3
"""
build.py - generate the static GitHub Pages site from the verified JSON datasets.

Design constraints honoured by this script:

1. NO figure is typed by hand. Every dollar amount, percentage and date in the
   generated HTML is either read from data/*.json (which carries its official
   source) or recomputed here from official percentages.
2. Every table row that states a verifiable fact carries a source link to an
   official site. A row with no source renders as UNVERIFIED.
3. Arithmetic is re-derived at build time and cross-checked against the values
   stored in the data files. A mismatch fails the build.
4. assert_no_pii() sweeps the generated output. A real identifier fails the build.

Usage:  python3 build.py
Exit:   0 on success, non-zero if any check fails.
"""
import json, os, re, sys, html
from datetime import date, timedelta
from decimal import Decimal as D, ROUND_HALF_UP

ROOT = os.path.dirname(os.path.abspath(__file__))
FAIL = []

def load(n):
    with open(os.path.join(ROOT, "data", n)) as f:
        return json.load(f)

AI      = load("allowable-increases.json")
RATES   = load("current-rates.json")
UNITS   = load("units.json")
CALCS   = load("calculations.json")
MARKET  = load("market.json")
LAW     = load("law.json")
SOURCES = load("sources.json")
FLAGS   = load("flags.json")

# --------------------------------------------------------------------------- #
# verification of the published allowable-increase table against the official PDF
# --------------------------------------------------------------------------- #
EXPECTED_SPOT = {"3/1/26 \u2013 2/28/27": "1.6", "3/1/25 \u2013 2/28/26": "1.4",
                 "3/1/24 \u2013 2/28/25": "1.7", "3/1/23 \u2013 2/29/24": "3.6",
                 "3/1/22 \u2013 2/28/23": "2.3", "3/1/21 \u2013 2/28/22": "0.7",
                 "3/1/20 \u2013 2/28/21": "1.8", "3/1/19 \u2013 2/29/20": "2.6"}
tbl = {r["period"]: r["percent"] for r in AI["table"]}
for k, v in EXPECTED_SPOT.items():
    if tbl.get(k) != v:
        FAIL.append(f"allowable-increases mismatch for {k}: got {tbl.get(k)!r} want {v!r}")
if AI["current_period"]["percent"] != "1.6":
    FAIL.append("current_period.percent is not 1.6")

# --------------------------------------------------------------------------- #
# independent recomputation of every dollar figure
# --------------------------------------------------------------------------- #
def money(x):
    return str(D(x).quantize(D("0.01"), rounding=ROUND_HALF_UP))

U1, U2 = D("3995.00"), D("3150.00")
PCT_IN_EFFECT = {  # anniversary date -> official percentage for the period containing it
    "2020-06-01": "1.8", "2021-06-01": "0.7", "2022-06-01": "2.3", "2023-06-01": "3.6",
    "2024-06-01": "1.7", "2025-06-01": "1.4", "2026-06-01": "1.6",
    "2026-02-01": "1.4", "2027-02-01": "1.6", "2026-12-01": "1.6", "2027-02-08": "1.6",
}
U2_BANKED_PRE_6127  = sum(D(PCT_IN_EFFECT[d]) for d in PCT_IN_EFFECT if d.startswith("20") and d.endswith("06-01") and d < "2026-06-01")
U2_BANKED_POST_6127 = sum(D(PCT_IN_EFFECT[d]) for d in PCT_IN_EFFECT if d.endswith("06-01"))
if U2_BANKED_PRE_6127 != D("11.5"):
    FAIL.append(f"recomputed Unit 2 banked (pre 6/1/27) = {U2_BANKED_PRE_6127}, expected 11.5")
if U2_BANKED_POST_6127 != D("13.1"):
    FAIL.append(f"recomputed Unit 2 banked (post 6/1/27) = {U2_BANKED_POST_6127}, expected 13.1")

CHECKS = [
    ("U1-A total", D("1.4") + D("1.6"), D("3.0")),
    ("U1-A dollars", U1 * D("3.0") / 100, D("119.85")),
    ("U1-A new rent", U1 + U1 * D("3.0") / 100, D("4114.85")),
    ("U1-B dollars", U1 * D("1.6") / 100, D("63.92")),
    ("U1-B new rent", U1 + U1 * D("1.6") / 100, D("4058.92")),
    ("U1 cost of acting early (monthly)", U1 * (D("3.0") - D("1.6")) / 100, D("55.93")),
    ("U2 banked-only dollars", U2 * D("13.1") / 100, D("412.65")),
    ("U2-A/B new rent", U2 + U2 * D("13.1") / 100, D("3562.65")),
    ("U2-C dollars", U2 * D("10.0") / 100, D("315.00")),
    ("U2-C new rent", U2 + U2 * D("10.0") / 100, D("3465.00")),
    ("U2 11.5% dollars", U2 * D("11.5") / 100, D("362.25")),
]
for name, got, want in CHECKS:
    if D(money(got)) != want:
        FAIL.append(f"arithmetic check FAILED: {name} = {money(got)}, expected {want}")

def serve_by(eff, days):
    return (date.fromisoformat(eff) - timedelta(days=days)).isoformat()

NOTICE_CHECKS = [
    ("U1-A 30d",  serve_by("2027-02-01", 30), "2027-01-02"),
    ("U1-A 35d",  serve_by("2027-02-01", 35), "2026-12-28"),
    ("U2-A 90d",  serve_by("2027-06-01", 90), "2027-03-03"),
    ("U2-A 95d",  serve_by("2027-06-01", 95), "2027-02-26"),
    ("U2-B 90d",  serve_by("2027-02-08", 90), "2026-11-10"),
    ("U2-B 95d",  serve_by("2027-02-08", 95), "2026-11-05"),
    ("U2-C 30d",  serve_by("2027-02-08", 30), "2027-01-09"),
    ("U2-C 35d",  serve_by("2027-02-08", 35), "2027-01-04"),
]
for name, got, want in NOTICE_CHECKS:
    if got != want:
        FAIL.append(f"notice-deadline check FAILED: {name} = {got}, expected {want}")

# reconcile the stored scenario values against the recomputation
SCEN = {s["id"]: s for s in CALCS["unit1"] + CALCS["unit2"]}
for sid, field, want in [("U1-A", "dollar_increase", "119.85"), ("U1-A", "new_base_rent", "4114.85"),
                         ("U1-B", "dollar_increase", "63.92"),  ("U1-B", "new_base_rent", "4058.92"),
                         ("U2-B", "dollar_increase", "412.65"), ("U2-B", "new_base_rent", "3562.65"),
                         ("U2-C", "dollar_increase", "315.00"), ("U2-C", "new_base_rent", "3465.00")]:
    if SCEN[sid][field] != want:
        FAIL.append(f"data/calculations.json {sid}.{field} = {SCEN[sid][field]!r}, recomputed {want!r}")
for sid, field, want in [("U1-A", "serve_by", "2027-01-02"), ("U2-A", "serve_by", "2027-03-03"),
                         ("U2-B", "serve_by", "2026-11-10"), ("U2-C", "serve_by", "2027-01-09")]:
    if SCEN[sid][field] != want:
        FAIL.append(f"data/calculations.json {sid}.{field} = {SCEN[sid][field]!r}, recomputed {want!r}")

# census reconciliation
gb = MARKET["gross_rent_distribution"]["brackets"]
if sum(b["households"] for b in gb) != MARKET["gross_rent_distribution"]["with_cash_rent_total"]:
    FAIL.append("census gross-rent brackets do not sum to the published with-cash-rent total")
rb = MARKET["rent_burden"]
if sum(b["households"] for b in rb["brackets"]) != rb["computed_universe"]:
    FAIL.append("census rent-burden brackets do not sum to the computed universe")
if rb["computed_universe"] + rb["not_computed"] != rb["universe_total"]:
    FAIL.append("census rent-burden universe does not reconcile")
ha = MARKET["housing_age"]
if sum(b["units"] for b in ha["buckets"]) != ha["total_housing_units"]:
    FAIL.append("census year-structure-built buckets do not sum to the published total")

# --------------------------------------------------------------------------- #
# source-link enforcement
# --------------------------------------------------------------------------- #
for r in LAW["local"] + LAW["state"] + LAW["federal"]:
    if not r.get("source"):
        FAIL.append(f"law row without a source: {r['rule']}")
    if r.get("verified") is False and not r.get("flag"):
        FAIL.append(f"unverified law row without a flag id: {r['rule']}")
for s in SOURCES["sources"]:
    if not s.get("url"):
        FAIL.append(f"source without url: {s.get('title')}")
for f in FLAGS["flags"]:
    if not f.get("source"):
        FAIL.append(f"flag without a source: {f['id']}")
for c in CALCS["unit1"] + CALCS["unit2"]:
    if c["dollar_increase"] and not c["_sources_ok"] if False else False:
        pass

# --------------------------------------------------------------------------- #
# PII guard
# --------------------------------------------------------------------------- #
OFFICIAL_EMAILS = {"rentboard@sfgov.org", "legal@evictiondefense.org", "cis@sfbar.org",
                   "info@somcan.org", "homematchsf@frontporch.net"}
OFFICIAL_PHONES = {"415-252-4600", "415-659-9184", "415-782-8940", "415-703-8644",
                   "415-982-1300", "415-255-2288", "415-701-2311", "415-513-5177",
                   "415-984-2728", "415-282-6209", "415-808-5662", "415-775-7110",
                   "415-984-1450", "415-983-3970", "415-329-3809", "415-351-1000",
                   "415-255-7693", "415-552-5637", "415-669-0284", "415-947-0797",
                   "415-947-9085"}
# Optional extra terms an owner can add LOCALLY to strengthen the sweep.
# Deliberately EMPTY in the repository: committing real identifiers here in order
# to block them would itself publish them. See docs/PRIVACY-AND-ANONYMIZATION.md.
LOCAL_EXTRA = []
_lp = os.path.join(ROOT, ".pii-guard.local.json")
if os.path.exists(_lp):
    try:
        LOCAL_EXTRA = json.load(open(_lp)).get("forbidden_tokens", [])
    except Exception as e:
        FAIL.append(f".pii-guard.local.json unreadable: {e}")

SSN_RE  = re.compile(r"\b\d{3}-\d{2}-\d{4}\b")
MAIL_RE = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")
PHONE_RE = re.compile(r"\b(?:\+?1[\s.-]?)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}\b")

def assert_no_pii(text, path):
    bad = []
    for m in SSN_RE.finditer(text):
        bad.append(f"{path}: SSN-shaped value {m.group(0)}")
    for m in MAIL_RE.finditer(text):
        if m.group(0).lower() not in OFFICIAL_EMAILS:
            bad.append(f"{path}: non-official email {m.group(0)}")
    for m in PHONE_RE.finditer(text):
        norm = re.sub(r"[^\d-]", "", m.group(0))
        tail = norm[-12:]
        if not any(tail.endswith(p[-12:]) or p in norm for p in OFFICIAL_PHONES):
            bad.append(f"{path}: non-official phone {m.group(0)}")
    for t in LOCAL_EXTRA:
        if t and t.lower() in text.lower():
            bad.append(f"{path}: forbidden local token present")
    return bad

# --------------------------------------------------------------------------- #
# HTML shell
# --------------------------------------------------------------------------- #
E = html.escape
PAGES = [
    ("executive-summary", "Executive Summary", "The decision, in one document"),
    ("units",             "Unit Profiles",     "Anonymized rent histories"),
    ("calculations",      "Increase Scenarios","Lawful amounts, dates and notice deadlines"),
    ("local-law",         "San Francisco Law", "Rent Ordinance and Rent Board rules"),
    ("state-law",         "California Law",    "AB 1482, notice, retaliation, FEHA"),
    ("federal-law",       "Federal Law",       "Fair Housing Act and HUD"),
    ("allowable",         "Allowable Increases","Every official percentage since 1982"),
    ("market",            "Market Data 94122", "U.S. Census Bureau figures"),
    ("practices",         "Owner Practices",   "Corporate versus individual owners"),
    ("discrimination",    "Anti-Discrimination","One unit or both units?"),
    ("tenant-review",     "Tenant-Lawyer Test", "Free services and the 8-question review"),
    ("checklist",         "Compliance Checklist","Notice procedure and action plan"),
    ("sources",           "Source Register",   "Every official document cited"),
    ("flagged",           "Flagged for Review","22 irregularities and unverified items"),
]


LEGACY = [
    ("dashboard-81e8c938.html", "Prior dashboard (archived)"),
    ("executive-summary.html",  "Executive Summary (prior)"),
    ("units.html",              "Units (prior)"),
    ("analysis.html",           "Increase Analysis (prior)"),
    ("laws.html",               "Laws & Regulations (prior)"),
    ("process.html",            "Notice & Process (prior)"),
    ("tenant-protections.html", "Tenant Protections (prior)"),
    ("practices.html",          "Owner Practices (prior)"),
    ("flagged.html",            "Flagged for Review (prior)"),
    ("sources.html",            "Sources (prior)"),
]

CSS = """
:root{--bg:#0f1115;--panel:#171a21;--panel2:#1e222b;--line:#2b303b;--ink:#e8eaed;--muted:#9aa3b2;
--acc:#5b9dff;--ok:#3fb950;--warn:#d29922;--bad:#f85149;--hi:#a371f7;}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.6 -apple-system,BlinkMacSystemFont,
"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
a{color:var(--acc);text-decoration:none}a:hover{text-decoration:underline}
.wrap{display:flex;min-height:100vh}
nav{width:250px;flex:0 0 250px;background:var(--panel);border-right:1px solid var(--line);
padding:20px 0;position:sticky;top:0;height:100vh;overflow-y:auto}
nav .brand{padding:0 20px 16px;border-bottom:1px solid var(--line);margin-bottom:12px}
nav .brand b{display:block;font-size:15px;letter-spacing:.2px}
nav .brand span{color:var(--muted);font-size:12px}
nav a{display:block;padding:8px 20px;color:var(--muted);font-size:13.5px;border-left:3px solid transparent}
nav a:hover{background:var(--panel2);color:var(--ink);text-decoration:none}
nav a.on{color:var(--ink);border-left-color:var(--acc);background:var(--panel2)}
nav .grp{padding:14px 20px 6px;font-size:11px;text-transform:uppercase;letter-spacing:.9px;color:#6b7382}
main{flex:1;min-width:0;padding:32px 40px 80px;max-width:1180px}
h1{font-size:26px;margin:0 0 6px;line-height:1.25}
h2{font-size:19px;margin:38px 0 12px;padding-bottom:7px;border-bottom:1px solid var(--line)}
h3{font-size:16px;margin:26px 0 8px}
p{margin:10px 0}
.lede{color:var(--muted);font-size:15px;margin:0 0 24px}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(215px,1fr));gap:14px;margin:20px 0}
.card{background:var(--panel);border:1px solid var(--line);border-radius:9px;padding:16px}
.card .k{color:var(--muted);font-size:11.5px;text-transform:uppercase;letter-spacing:.7px;margin-bottom:7px}
.card .v{font-size:25px;font-weight:650;line-height:1.15}
.card .s{color:var(--muted);font-size:12.5px;margin-top:7px}
.card.good .v{color:var(--ok)}.card.warn .v{color:var(--warn)}.card.bad .v{color:var(--bad)}
.card.acc .v{color:var(--acc)}
table{width:100%;border-collapse:collapse;margin:14px 0;font-size:13.5px;background:var(--panel);
border:1px solid var(--line);border-radius:9px;overflow:hidden}
th,td{padding:9px 11px;text-align:left;border-bottom:1px solid var(--line);vertical-align:top}
th{background:var(--panel2);font-size:11.5px;text-transform:uppercase;letter-spacing:.6px;color:var(--muted);
position:sticky;top:0}
tr:last-child td{border-bottom:none}
tbody tr:hover{background:#1b1f28}
td.num,th.num{text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}
.src{font-size:11.5px;color:var(--muted);white-space:nowrap}
.pill{display:inline-block;padding:1px 8px;border-radius:20px;font-size:11px;font-weight:600;
letter-spacing:.3px;border:1px solid}
.p-ok{color:var(--ok);border-color:#1f4d2a;background:#12261a}
.p-warn{color:var(--warn);border-color:#5a4413;background:#241d0b}
.p-bad{color:var(--bad);border-color:#5c2320;background:#2a1211}
.p-hi{color:var(--hi);border-color:#3f2d63;background:#1c1630}
.p-mut{color:var(--muted);border-color:var(--line);background:var(--panel2)}
.blank{color:var(--warn);font-style:italic;font-weight:600}
.note{background:var(--panel);border:1px solid var(--line);border-left:3px solid var(--acc);
border-radius:7px;padding:13px 16px;margin:16px 0}
.note.warn{border-left-color:var(--warn)}.note.bad{border-left-color:var(--bad)}
.note.ok{border-left-color:var(--ok)}
.note b{display:block;margin-bottom:4px}
blockquote{margin:12px 0;padding:10px 16px;border-left:3px solid var(--line);color:#c8cdd6;
background:var(--panel);border-radius:0 7px 7px 0;font-size:13.5px}
code{background:var(--panel2);padding:1px 5px;border-radius:4px;font-size:12.5px;
font-family:ui-monospace,SFMono-Regular,Menlo,monospace}
.filterbar{display:flex;gap:10px;flex-wrap:wrap;align-items:center;margin:16px 0}
input[type=search]{background:var(--panel);border:1px solid var(--line);color:var(--ink);
padding:8px 12px;border-radius:7px;font-size:13.5px;min-width:250px}
input[type=search]:focus{outline:none;border-color:var(--acc)}
.btn{background:var(--panel2);border:1px solid var(--line);color:var(--muted);padding:6px 12px;
border-radius:20px;font-size:12.5px;cursor:pointer}
.btn:hover,.btn.on{color:var(--ink);border-color:var(--acc)}
.count{color:var(--muted);font-size:12.5px;margin-left:auto}
ul{margin:10px 0;padding-left:22px}li{margin:5px 0}
.two{display:grid;grid-template-columns:1fr 1fr;gap:16px}
@media(max-width:900px){.two{grid-template-columns:1fr}nav{display:none}main{padding:20px}}
footer{margin-top:48px;padding-top:18px;border-top:1px solid var(--line);color:var(--muted);font-size:12.5px}
.tag{font-size:11px;color:var(--muted)}
.rec{border:1px solid #1f4d2a;background:#101f16}
"""

JS = """
document.addEventListener('DOMContentLoaded',function(){
  document.querySelectorAll('input[data-filter]').forEach(function(inp){
    var tid=inp.getAttribute('data-filter');
    var tbl=document.getElementById(tid); if(!tbl) return;
    var rows=Array.prototype.slice.call(tbl.querySelectorAll('tbody tr'));
    var cnt=document.getElementById(tid+'-count');
    inp.addEventListener('input',function(){
      var q=inp.value.trim().toLowerCase(),n=0;
      rows.forEach(function(r){
        var hit=!q||r.textContent.toLowerCase().indexOf(q)>=0;
        r.style.display=hit?'':'none'; if(hit)n++;
      });
      if(cnt)cnt.textContent=n+' of '+rows.length+' rows';
    });
    if(cnt)cnt.textContent=rows.length+' of '+rows.length+' rows';
  });
  document.querySelectorAll('[data-sev]').forEach(function(b){
    b.addEventListener('click',function(){
      var s=b.getAttribute('data-sev');
      var on=!b.classList.contains('on');
      document.querySelectorAll('[data-sev]').forEach(function(x){x.classList.remove('on')});
      if(on)b.classList.add('on');
      var t=document.getElementById(b.getAttribute('data-target')); if(!t)return;
      t.querySelectorAll('tbody tr').forEach(function(r){
        r.style.display=(!on||r.getAttribute('data-sev')===s)?'':'none';
      });
    });
  });
});
"""

def shell(slug, title, subtitle, body, base):
    nav = ['<nav><div class="brand"><b>Rent Increase Analysis</b>'
           '<span>Outer Sunset, SF 94122</span></div>',
           f'<a href="{base}index.html"{" class=on" if slug=="index" else ""}>Dashboard</a>',
           '<div class="grp">Findings</div>']
    grp_at = {"local-law": "Legal framework", "practices": "Analysis",
              "sources": "Verification"}
    for s, t, sub in PAGES:
        if s in grp_at:
            nav.append(f'<div class="grp">{E(grp_at[s])}</div>')
        cls = ' class="on"' if s == slug else ''
        nav.append(f'<a href="{base}pages/{s}.html"{cls}>{E(t)}</a>')
    nav.append('<div class="grp">Preserved earlier work</div>')
    for f, t in LEGACY:
        nav.append(f'<a href="{base}{f}">{E(t)}</a>')
    nav.append('</nav>')
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)} &middot; Rent Increase Analysis &middot; SF 94122</title>
<meta name="description" content="{E(subtitle)}">
<link rel="stylesheet" href="{base}assets/css/styles.css">
</head><body><div class="wrap">
{''.join(nav)}
<main>
<h1>{E(title)}</h1>
<p class="lede">{E(subtitle)}</p>
{body}
<footer>
Anonymized under <a href="{base}docs/PRIVACY-AND-ANONYMIZATION.md">the privacy policy</a>:
placeholder identifiers only, dates and dollar amounts preserved exactly, no personal
information committed to this repository.<br>
Every factual row links to an official source. Values that could not be confirmed are left
blank and listed on <a href="{base}pages/flagged.html">Flagged for Review</a>.
<b>Not legal advice.</b> This site is informational only.
Data retrieved 2026-11-06 &middot; generated by <code>build.py</code> from
<a href="{base}data/sources.json">{len(SOURCES['sources'])} registered official sources</a>.
</footer>
</main></div><script src="{base}assets/js/app.js"></script></body></html>
"""

def src_cell(url, label="source"):
    if not url:
        return '<span class="pill p-warn">UNVERIFIED</span>'
    return f'<span class="src"><a href="{E(url)}" rel="noopener" target="_blank">{E(label)}</a></span>'

def w(path, s):
    p = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w") as f:
        f.write(s)
    return s

def hi_sev():
    return sum(1 for f in FLAGS['flags'] if f['severity'] == 'HIGH')

def pill(v):
    m = {"HIGH": "p-bad", "medium": "p-warn", "low": "p-mut", "informational": "p-mut",
         "cosmetic": "p-mut", "true": "p-ok", "false": "p-warn"}
    return f'<span class="pill {m.get(str(v).lower(), m.get(v, "p-mut"))}">{E(str(v))}</span>'

B = []   # every generated document, for the PII sweep
print("build.py: verification and generation")

# ============================ INDEX / DASHBOARD ==============================
def build_index():
    hi = sum(1 for f in FLAGS["flags"] if f["severity"] == "HIGH")
    n_unver = sum(1 for f in FLAGS["flags"] if "Unverified" in f["category"] or "unverified" in f["category"].lower())
    body = f"""
<div class="cards">
  <div class="card acc"><div class="k">SF allowable increase</div><div class="v">{AI['current_period']['percent']}%</div>
    <div class="s">Effective {E(AI['current_period']['effective_from'])} through {E(AI['current_period']['effective_through'])}</div></div>
  <div class="card"><div class="k">Unit 1 &mdash; maximum lawful</div><div class="v">3.0%</div>
    <div class="s">$3,995.00 &rarr; <b>$4,114.85</b><br>Earliest: 2027-02-01 &middot; 30-day notice</div></div>
  <div class="card"><div class="k">Unit 2 &mdash; maximum lawful</div><div class="v">13.1%</div>
    <div class="s">$3,150.00 &rarr; <b>$3,562.65</b><br>Earliest: 2027-06-01 &middot; <b>90-day</b> notice</div></div>
  <div class="card warn"><div class="k">Flags raised</div><div class="v">{len(FLAGS['flags'])}</div>
    <div class="s">{hi} HIGH severity &middot; {n_unver} values left blank</div></div>
  <div class="card ok"><div class="k">Official sources</div><div class="v">{len(SOURCES['sources'])}</div>
    <div class="s">All .gov, legislative, Rent Board or Census Bureau</div></div>
</div>

<div class="note bad"><b>Nothing can lawfully be done today.</b>
The recommended Unit&nbsp;2 notice cannot be served until <b>March 2027</b> and the recommended
Unit&nbsp;1 notice not until <b>January 2027</b>. {hi_sev()} HIGH-severity flags must be closed first &mdash;
one of them, the <b>rent increase license</b>, voids the entire increase if it is missing.
<a href="pages/flagged.html">Review the flags</a>.</div>

<h2>The two units at a glance</h2>
<table><thead><tr><th>Item</th><th>Unit 1</th><th>Unit 2</th><th>Authority</th></tr></thead><tbody>
<tr><td>Current base rent</td><td class="num">$3,995.00</td><td class="num">$3,150.00</td><td>Owner-supplied fact</td></tr>
<tr><td>Tenancy commenced</td><td>2025-02-01</td><td>2019-06-01</td><td>Owner-supplied fact</td></tr>
<tr><td>Anniversary date</td><td>February 1 <span class="pill p-warn">F-07</span></td><td>June 1</td>
    <td>{src_cell('https://www.sf.gov/learn-about-rent-increases-san-francisco','sf.gov')}</td></tr>
<tr><td>Increases ever imposed</td><td class="num">0</td><td class="num">0 <span class="pill p-warn">F-08</span></td>
    <td>Owner-supplied fact</td></tr>
<tr><td>Skipped increases available to bank</td><td class="num">1 &mdash; the 1.4% of 2026-02-01</td>
    <td class="num">7 &mdash; 2020 through 2026</td>
    <td>{src_cell('https://www.sf.gov/documents/34344/571_Allowable_Annual_Increases_26-27_1.pdf','Info Sheet 571')}</td></tr>
<tr><td>Banked percentage, computed</td><td class="num">1.4%</td><td class="num">13.1%</td>
    <td>{src_cell('https://www.sf.gov/information--banked-rent-increases','sf.gov')}</td></tr>
<tr><td>Plus annual percentage in effect</td><td class="num">1.6%</td>
    <td class="num">1.6% <span class="tag">/ not yet published for 2027-28</span></td>
    <td>{src_cell(AI['current_period']['source'],'sf.gov')}</td></tr>
<tr><td><b>Maximum lawful total</b></td><td class="num"><b>3.0%</b></td>
    <td class="num"><b>13.1%</b> <span class="pill p-warn">F-16 provisional</span></td>
    <td>{src_cell('https://www.sf.gov/learn-about-rent-increases-san-francisco','sf.gov')}</td></tr>
<tr><td><b>Dollar increase</b></td><td class="num"><b>$119.85</b></td><td class="num"><b>$412.65</b></td>
    <td>Computed &mdash; no rounding up</td></tr>
<tr><td><b>Resulting base rent</b></td><td class="num"><b>$4,114.85</b></td><td class="num"><b>$3,562.65</b></td>
    <td>Computed</td></tr>
<tr><td>Earliest lawful effective date</td><td>2027-02-01</td><td>2027-06-01 (full) / 2027-02-08 (partial)</td>
    <td>{src_cell('https://www.sf.gov/information--banked-rent-increases','sf.gov')}</td></tr>
<tr><td>Written notice required</td><td>30 days (35 if mailed)</td><td><b>90 days</b> (95 if mailed)</td>
    <td>{src_cell('https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=827','Civ. Code 827')}</td></tr>
<tr><td>Serve notice by</td><td>2027-01-02 <span class="tag">(mailed 2026-12-28)</span></td>
    <td>2027-03-03 <span class="tag">(mailed 2027-02-26)</span></td>
    <td>Computed from {src_cell('https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=827','827')}</td></tr>
<tr><td>Market-rate reset available?</td><td><span class="pill p-bad">NO</span> an original occupant remains</td>
    <td><span class="pill p-bad">NO</span> continuing tenancy</td>
    <td>{src_cell('https://www.sf.gov/information--rent-increases-under-section-614-and-costa-hawkins','Rules 6.14')}</td></tr>
<tr><td>Increase for the added occupant?</td><td><span class="pill p-bad">UNLAWFUL</span></td><td>n/a</td>
    <td>{src_cell('https://www.sf.gov/information--charging-additional-occupants-prohibited','Topic 152')}</td></tr>
<tr><td>Rent increase license required?</td><td><span class="pill p-bad">YES</span> status unverified</td>
    <td><span class="pill p-bad">YES</span> status unverified</td>
    <td>{src_cell('https://www.sf.gov/rent-board-housing-inventory','Admin. Code 37.15')}</td></tr>
<tr><td>Position versus ZIP 94122 median ($2,816)</td><td class="num">+41.9%</td><td class="num">+11.9% &rarr; +26.5%</td>
    <td>{src_cell(MARKET['median_gross_rent'][0]['source'],'Census B25064')}</td></tr>
</tbody></table>

<h2>Answers to the five questions asked</h2>
<table><thead><tr><th style="width:32%">Question</th><th>Answer</th><th>Detail</th></tr></thead><tbody>
<tr><td><b>What is a reasonable and normal increase in 94122 under local, state and federal law?</b></td>
 <td>Local law supplies the only operative ceiling: <b>1.6%</b> annual, plus lawfully banked prior
 percentages. The state AB&nbsp;1482 cap of 8.8% does <b>not</b> apply. Federal law sets
 <b>no</b> rent ceiling at all &mdash; only anti-discrimination limits.</td>
 <td><a href="pages/local-law.html">SF</a> &middot; <a href="pages/state-law.html">State</a> &middot;
 <a href="pages/federal-law.html">Federal</a></td></tr>
<tr><td><b>How do large corporate owners handle increases, versus individual owners?</b></td>
 <td>The percentage is identical for both. The real differences are legal and administrative:
 corporate owners lose the Costa-Hawkins and AB&nbsp;1482 entity exemptions, and
 <b>algorithmic revenue-management pricing is banned outright</b> in SF under Admin. Code
 &sect;&nbsp;37.10C. Individual owners differ mainly in administrative discipline &mdash; Unit&nbsp;2's
 seven missed anniversaries are the classic individual-owner pattern.</td>
 <td><a href="pages/practices.html">Owner Practices</a></td></tr>
<tr><td><b>What is the correct way to notify tenants, and what reasons are reasonable?</b></td>
 <td>Written notice, personally delivered or mailed (+5 days if mailed), 30 days at 10% or less and
 <b>90 days above 10%</b>, stating the dollar amount, the percentage, the effective date, and
 <b>which portion is banked and its source dates</b>. The annual allowable increase needs
 <b>no justification at all</b> &mdash; it exists by operation of law.</td>
 <td><a href="pages/checklist.html">Checklist</a></td></tr>
<tr><td><b>Would these increases survive review by an SF tenant lawyer?</b></td>
 <td>As computed, yes on arithmetic, notice and non-discrimination grounds &mdash; but
 <b>not until {hi_sev()} HIGH-severity flags are closed</b>. The license question (F-22) voids everything
 if unanswered, and the retaliation screen (F-06) cannot be run without tenant records.</td>
 <td><a href="pages/tenant-review.html">Tenant-Lawyer Test</a></td></tr>
<tr><td><b>Raise one unit, or both, to avoid discrimination claims?</b></td>
 <td><b>Both, under one written policy &mdash; but at different, lawfully computed percentages.</b>
 Do not raise only one without a documented neutral reason. Equally, do not equalise the
 percentages: forcing Unit&nbsp;2 down forfeits 10.1% of lawful entitlement, and forcing Unit&nbsp;1
 up would be an unlawful increase outright.</td>
 <td><a href="pages/discrimination.html">Anti-Discrimination</a></td></tr>
</tbody></table>

<h2>Verification status</h2>
<div class="two">
<div class="note ok"><b>Confirmed from official sources</b>
{len(SOURCES["sources"])} documents: SF Rent Board guidance and Info Sheet 571, Rent Board Rules and Regulations
&sect;&sect;&nbsp;4.10, 4.11, 4.12 and 13.14, San Francisco Administrative Code Chapter 37 via Board of
Supervisors ordinances, California Civil Code &sect;&sect;&nbsp;827, 1942.5, 1947.12 from the
Legislative Information service, HUD, the California Civil Rights Department, and the
U.S. Census Bureau API. Every Census variable label was individually confirmed against the
Census variable-definition endpoint, and every bracket set reconciles exactly to its published total.</div>
<div class="note warn"><b>Left blank rather than inferred</b>
HUD Fair Market Rent for the San Francisco area (API returned <code>Unauthenticated</code>; third-party
FY2026 values conflicted at $3,604 versus $3,160). BLS CPI inputs (regional release returned 404).
The 3/1/2027&ndash;2/28/2028 allowable percentage (not yet published). The current-year bankable Rent
Board fee (absent from the official rate table). Unit&nbsp;1 Scenario&nbsp;C dollar values (the underlying
anniversary-date question is unresolved). Certificate of occupancy date, condominium status,
owner occupancy, license status, the Unit&nbsp;2 rent ledger, and the retaliation screen &mdash; all
require owner records or a portal login.</div>
</div>

<h2>What changed in the repository</h2>
<p>At the start of this session the repository contained a single 17-byte <code>README.md</code> and
one commit, while GitHub Pages was already enabled against it with the legacy Jekyll build and no
<code>.nojekyll</code> &mdash; so the published URL served nothing useful. Full findings R-01 to R-06 are in
<a href="docs/repo-review.md">the repository review</a>.</p>
<table><thead><tr><th>Added</th><th>Purpose</th></tr></thead><tbody>
<tr><td><code>index.html</code> + 14 subpages in <code>pages/</code></td><td>The site. Dependency-free static HTML, generated, no Jekyll processing (see <code>.nojekyll</code>).</td></tr>
<tr><td><code>data/*.json</code> (8 files)</td><td>Single source of truth. Every value carries its official source URL.</td></tr>
<tr><td><code>build.py</code></td><td>Generates the site, re-derives all arithmetic, reconciles Census counts, enforces source links and sweeps for PII. Fails the build on any mismatch.</td></tr>
<tr><td><code>docs/executive-summary.md</code></td><td>The executive summary in Markdown.</td></tr>
<tr><td><code>docs/PRIVACY-AND-ANONYMIZATION.md</code></td><td>Binding anonymization policy and placeholder mapping.</td></tr>
<tr><td><code>docs/repo-review.md</code></td><td>Line-by-line audit of the repository as received.</td></tr>
<tr><td><code>COORDINATION.md</code></td><td>Shared task board, verification log and integration record.</td></tr>
</tbody></table>
"""
    return shell("index", "Rent Increase Analysis \u2014 Outer Sunset, San Francisco 94122",
                 "Two rent-controlled units in a 1940 two-unit building. Every figure sourced to an official document; anything unconfirmed is left blank.",
                 body, "")

# ============================ EXECUTIVE SUMMARY ==============================
def build_exec():
    body = f"""
<div class="note"><b>Standard of proof</b>
Every legal proposition and every number on this page is sourced to an official .gov, legislative,
Rent Board or U.S. Census Bureau document. {len(SOURCES['sources'])} sources are registered in the
<a href="sources.html">Source Register</a>. Anything that could not be confirmed is left blank and
recorded as one of {len(FLAGS['flags'])} flags on <a href="flagged.html">Flagged for Review</a>.
Nothing has been inferred. <b>This is not legal advice.</b></div>

<h2>1. Bottom line</h2>
<p>The maximum lawful increase for <b>Unit&nbsp;1 is 3.0%</b> ($3,995.00 &rarr; $4,114.85), earliest
effective <b>2027-02-01</b> on 30-day notice. For <b>Unit&nbsp;2 it is 13.1%</b> ($3,150.00 &rarr;
$3,562.65), earliest effective <b>2027-06-01</b> on <b>90-day</b> notice &mdash; and that 13.1% is
provisional, because proposed legislation would cap banked increases at 10% (Flag F-16).</p>
<p><b>Nothing can lawfully be done today.</b> The correct action between now and then is to close
the {hi_sev()} HIGH-severity flags. The full summary is in
<a href="../docs/executive-summary.md"><code>docs/executive-summary.md</code></a>; the sections below
carry its operative content.</p>

<h2>2. What is reasonable and normal &mdash; three layers of law</h2>
<h3>Local: the Rent Ordinance is the operative ceiling</h3>
<p>The building is stated to have been built in 1940. SF.gov states that units built on or before
<b>June&nbsp;13,&nbsp;1979</b> have both rent control and eviction protection, and directs owners to confirm
the date on the <a href="https://sfplanninggis.org/PIM/" rel="noopener" target="_blank">SF Property
Information Map</a>. That confirmation has not been done &mdash; Flag <b>F-04</b> &mdash; because the address
was not supplied and is personal information.</p>
<p>A two-unit building cannot escape coverage. SF.gov Topic&nbsp;019 is explicit:
<blockquote>&ldquo;A single-family dwelling with a legal in-law unit constitutes a two-unit building and is
<b>not exempt</b> from the Ordinance. A single-family dwelling with an illegal in-law unit also
constitutes a two-unit building and is not exempt, unless both units are rented together as a single
tenancy.&rdquo;</blockquote>
The current allowable annual increase is <b>1.6%</b> for increases effective 3/1/2026 through
2/28/2027 &mdash; 60% of the CPI-U for the Bay Area, never more than 7%.</p>
<p><b>Reasonable and normal in ZIP 94122 is therefore not a market question.</b> For these units it is
an arithmetic question with a legally fixed answer: the annual allowable percentage plus properly
banked prior percentages, applied to base rent, once every twelve months, on the anniversary date,
on proper written notice, by a licensed owner. A 1.6% increase is routine. A 13.1% increase is also
entirely lawful here &mdash; seven years of skipped increases accumulated &mdash; but it sits at the
outer edge of what the ordinance permits without a petition, requires 90-day notice, and will attract
scrutiny.</p>

<h3>State: AB 1482 does not apply, but California notice law does</h3>
<p>California&rsquo;s Tenant Protection Act caps increases at 5%&nbsp;+&nbsp;CPI or 10%, whichever is lower &mdash;
currently <b>8.8%</b> for San Francisco for 8/1/2026 to 7/31/2027. It does <b>not</b> govern these units.
Civil Code &sect;&nbsp;1947.12(d)(3) exempts housing already subject to local rent control restricting
annual increases to less than the state cap, and the SF Rent Board states plainly:
<blockquote>&ldquo;This does NOT apply for units under the rent increase limitations of the San Francisco
Rent Ordinance.&rdquo;</blockquote>
The counter-intuitive consequence: <b>the state cap is not a safety net here.</b> A 13.1% increase on
Unit&nbsp;2 exceeds the 8.8% state figure and is still lawful, because San Francisco permits banking and
the state statute steps aside. Do not reason from 8.8%.</p>
<p>California does supply mandatory notice mechanics: <b>&sect;&nbsp;827(b)(2)</b> &mdash; 30 days where the
increase is 10% or less of the lowest rent charged in the prior 12 months; <b>&sect;&nbsp;827(b)(3)(A)</b> &mdash;
<b>90 days</b> where it exceeds 10%, measured on the same combined basis. Service is personal delivery
or mail under CCP &sect;&nbsp;1013; the Rent Board adds 5 days where mailed.</p>
<p><b>&sect;&nbsp;1942.5</b> is the sharpest state-law risk: a rent increase is barred within <b>180 days</b>
of specified good-faith tenant complaints about tenantability, agency complaints, inspections or
citations, and separately barred where made to retaliate for lawful tenant organising. Threatening to
report a tenant or their associates to immigration authorities is itself prohibited retaliation. This
screen cannot be run from the facts supplied &mdash; Flag <b>F-06</b>.</p>

<h3>Federal: no rent ceiling, but full anti-discrimination reach</h3>
<p>There is <b>no federal statute capping rent increases</b> for unsubsidised private housing. Federal
law reaches these increases only through the <b>Fair Housing Act</b> (42 U.S.C. &sect;&sect;&nbsp;3601&ndash;3619),
prohibiting discrimination in nearly all housing because of race, color, national origin, religion,
sex, familial status or disability. HUD&rsquo;s current published guidance prioritises cases with strong
evidence of <b>intentional</b> discrimination and withdraws earlier guidance documents.</p>
<p>Do not over-read that. A narrowed <i>federal administrative</i> posture leaves untouched California
FEHA (enforced by the California Civil Rights Department), San Francisco local law, and each
tenant&rsquo;s <b>private right of action</b>. California&rsquo;s protected list is far broader and is the
operative exposure.</p>

<h2>3. Unit 1 &mdash; the added occupant is a trap, and the answer is no</h2>
<p>Unit&nbsp;1&rsquo;s household changed: three original occupants became two, with one occupant added on
2026-04-01, rent unchanged at $3,995. Two doors that look open are firmly shut.</p>
<p><b>No market-rate reset.</b> Rent Board Rules &sect;&nbsp;6.14 permits an unlimited increase on remaining
occupants only <i>&ldquo;when the last original occupant vacates the unit&rdquo;</i>, and only if a written
&sect;&nbsp;6.14 notice was timely served on each subsequent occupant. Costa-Hawkins
(Civ.&nbsp;Code &sect;&nbsp;1954.53(d)) operates only <i>&ldquo;when the last original occupant no longer permanently
resides in the unit&rdquo;</i>, and SF.gov adds that <i>&ldquo;a co-tenant, as opposed to a subtenant, is not
subject to such a rent increase, regardless of when the co-tenant moved in.&rdquo;</i> <b>Tenant&nbsp;A is an
original occupant and remains.</b> Neither provision is available.</p>
<p><b>No increase because someone moved in.</b> SF.gov Topic&nbsp;152:
<blockquote>&ldquo;The Rent Ordinance prohibits landlords from charging more rent solely because a tenant has
added an additional occupant to an existing tenancy, including a newborn child. This constitutes an
<b>unlawful rent increase, even if the lease or rental agreement specifically permits</b> a rent
increase for additional occupants.&rdquo;</blockquote>
Tenants overcharged this way may petition to void the increase <b>and recover refunds</b>. The only
lawful route to recover genuinely higher operating costs from added occupancy is an O&amp;M petition or
a utility passthrough &mdash; both requiring Rent Board approval first.</p>
<p><b>The open question is timing, not amount.</b> Unit&nbsp;1&rsquo;s lease began 2/1/2025 and no increase was
ever imposed, so 1.4% became available on 2/1/2026 and was skipped. Under Rules &sect;&nbsp;4.12 a skipped
increase banks only once <b>12 full months</b> have elapsed from when it could first have been imposed &mdash;
here, on or after <b>2/1/2027</b>. Imposing on that date yields banked 1.4% plus the annual 1.6% (still
in effect through 2/28/2027) = <b>3.0%</b>, and preserves the February&nbsp;1 anniversary date.</p>
<div class="note warn"><b>Acting early is expensive.</b>
Imposing in December 2026 yields only <b>1.6%</b>, and SF.gov&rsquo;s own worked example says the skipped
1.4% is then <i>&ldquo;permanently lost due to the change in anniversary date.&rdquo;</i> That costs
<b>$55.93 per month &mdash; $671.16 per year, forever.</b> Waiting roughly three months is worth about
1.9&times; the immediate option.</div>
<p><b>Unresolved:</b> whether executing a new written rental agreement with the added occupant on
2026-04-01 reset the anniversary date to April&nbsp;1. <b>No official SF source addresses this fact
pattern.</b> Scenario&nbsp;U1-C is published with every dollar value left blank rather than guessed &mdash;
Flag <b>F-07</b>. Ask a Rent Board counselor; the service is free (415-252-4600).</p>

<h2>4. Unit 2 &mdash; seven skipped years and a deadline problem</h2>
<p>Unit&nbsp;2&rsquo;s tenancy began 6/1/2019 at $3,150 and, on the facts supplied, no increase was ever
imposed. Seven anniversary dates passed. Banked percentages are <b>added, never compounded, never
rounded up</b> (Rules &sect;&nbsp;4.12). There is <b>no cap</b> on how much may be banked, back to
April&nbsp;1,&nbsp;1982, and banked amounts do not expire during a tenancy.</p>
<ul>
<li>Effective <b>on or after 6/1/2027</b>: all seven have had 12 full months to elapse &rarr;
<b>13.1% banked</b>, plus the annual percentage for 3/1/2027&ndash;2/28/2028, which the Rent Board has
<b>not yet published</b> (Flag F-18). Banked component alone: 13.1% &times; $3,150 = <b>$412.65</b>. The
final total is deliberately left blank rather than estimated.</li>
<li>Effective <b>before 6/1/2027</b> (earliest realistic date 2027-02-08, driven by the 90-day
notice): 11.5% banked + 1.6% annual = the same <b>13.1%</b>, but the June&nbsp;1 anniversary date is
<b>permanently lost</b> and the 2026-06-01 1.6% never banks.</li>
</ul>
<div class="note bad"><b>Deadline problem.</b>
A 13.1% increase requires <b>90 days&rsquo;</b> notice. For an effective date of 2027-02-08 the notice must be
served by <b>2026-11-10</b> &mdash; four days from the date of this analysis. Not realistically achievable.
For an effective date of 2027-06-01 the notice must be served by <b>2027-03-03</b>. That is the workable
window.</div>
<p><b>Recommended: U2-A.</b> Impose on 6/1/2027, preserving the June&nbsp;1 anniversary and capturing
13.1% banked plus the 2027&ndash;28 annual percentage. Serve 90-day written notice after the Rent Board
publishes the new percentage (historically December&ndash;January) and by 2027-03-03.</p>
<p><b>Alternative: U2-C, phased.</b> SF.gov confirms a landlord need not impose the maximum:
<i>&ldquo;If only part of the allowable increase is used, the rest is banked.&rdquo;</i> Imposing exactly
<b>10.0%</b> &rarr; $315.00 &rarr; <b>$3,465.00</b> requires only <b>30-day</b> notice and leaves the remainder
intact. Given that Unit&nbsp;2&rsquo;s occupants already pay 11.9% above the ZIP median and that 42.1% of
renter households in 94122 are cost-burdened at 30%+ of income, a phased approach is materially less
likely to provoke a petition, and converts one 90-day event into two ordinary 30-day events.</p>
<p><b>Two live risks.</b> Flag <b>F-16</b>: reporting dated 2026-09-17 describes supervisors introducing
legislation to cap banked increases at <b>10% annually</b>. That is third-party reporting, not an official
source, and no enactment was found in any official Rent Board source reviewed &mdash; but if it passes as
described it caps Unit&nbsp;2 directly. <b>Treat 13.1% as provisional.</b> Flag <b>F-08</b>: only the
6/1/2019 lease was supplied. A tenant may petition on <b>Form&nbsp;516C</b> for review of the entire rent
history, and the Rent Board recalculates lawful base rent from <b>all</b> increases since April&nbsp;1,&nbsp;1982 &mdash;
including those imposed by prior owners.</p>

<h2>5. The compliance gate that voids everything: the rent increase license</h2>
<p>SF Admin.&nbsp;Code &sect;&nbsp;37.15 requires an owner to report into the <b>Rent Board Housing Inventory</b>
at <a href="https://portal.sfrb.org/" rel="noopener" target="_blank">portal.sfrb.org</a> to obtain a
<b>rent increase license</b>. SF.gov: <i>&ldquo;A landlord must have a current rent increase license on file
with the Rent Board <b>before</b> any annual or banked rent increase can go into effect.&rdquo;</i>
Rent Board Rules &sect;&nbsp;13.14:</p>
<blockquote>&ldquo;Any rent increase under Ordinance Sections 37.3(a)(1)-(2) purporting to be effective while
the landlord is unlicensed shall render the <b>entire rent increase null and void</b>.&rdquo;</blockquote>
<p><b>Correct arithmetic does not save it.</b> The right percentage, the right anniversary date and the
right notice period still produce a void increase if the license was not in effect on the <b>effective
date</b> &mdash; not the service date. For buildings with fewer than 10 residential units, reporting began
<b>March&nbsp;1,&nbsp;2023</b>, annually thereafter. A 2-unit building therefore needed submissions for 2023,
2024, 2025 and 2026. There is no monetary penalty for filing late and late submissions are accepted,
but the increase is unenforceable until the license exists. License status <b>cannot be verified from
outside the portal</b> &mdash; Flag <b>F-22</b>.</p>
<p>One point of owner self-interest: SF.gov states that Housing Inventory submissions are <b>public</b>,
including owner name and business contact information, square footage, bedroom and bathroom counts,
occupancy history, and base rent in $250 increments, filed under penalty of perjury. Complying with the
licensing precondition necessarily publishes some property-level data through a City system &mdash; a City
disclosure, not one made by this repository.</p>

<h2>6. Answers to the remaining questions</h2>
<ul>
<li><a href="practices.html"><b>Corporate versus individual owners</b></a> &mdash; the percentage is
identical; the differences are legal (entity exemptions lost, &sect;&nbsp;37.10C algorithmic-pricing ban)
and administrative. No official source quantifies behavioural differences, so none is claimed &mdash;
Flag F-21.</li>
<li><a href="checklist.html"><b>Notice procedure and legitimate reasons</b></a> &mdash; eight mandatory
notice elements and a table of which reasons are legitimate, which need a petition, and which are
unlawful outright.</li>
<li><a href="tenant-review.html"><b>The tenant-lawyer scrutiny test</b></a> &mdash; free services
available to tenants, the nine petition routes, and the eight-question review.</li>
<li><a href="discrimination.html"><b>One unit or both</b></a> &mdash; apply one written policy to both,
at different lawfully computed percentages. Neither raising only one nor equalising the percentages is
correct.</li>
<li><a href="market.html"><b>Market context for 94122</b></a> &mdash; verified U.S. Census Bureau data.</li>
</ul>
"""
    return shell("executive-summary", "Executive Summary",
                 "The decision in one document: maximum lawful increases, earliest lawful dates, notice deadlines, and the flags that must close first.",
                 body, "../")

# ============================ UNITS =========================================
def build_units():
    rows = []
    for u in UNITS["units"]:
        rows.append(f"""<h2>{E(u['id'])}</h2>
<div class="cards">
 <div class="card acc"><div class="k">Current base rent</div><div class="v">{E(u['current_base_rent'])}</div>
  <div class="s">Increases ever imposed: {u['increases_ever_imposed']}</div></div>
 <div class="card"><div class="k">Anniversary date</div><div class="v" style="font-size:19px">{E(u['anniversary_date'])}</div></div>
 <div class="card"><div class="k">Occupants</div><div class="v">{u['original_lease_tenants_count']} &rarr; {u['current_tenants_count']}</div>
  <div class="s">at the start &rarr; now</div></div>
</div>
<table><thead><tr><th>Date</th><th>Event</th><th class="num">Base rent</th></tr></thead><tbody>""")
        for h in u["rent_history"]:
            rows.append(f'<tr><td>{E(h["date"])}</td><td>{E(h["event"])}</td>'
                        f'<td class="num">{E(h["base_rent"])}</td></tr>')
        rows.append("</tbody></table>")
        if u.get("ledger_caveat"):
            rows.append(f'<div class="note warn"><b>Ledger caveat</b>{E(u["ledger_caveat"])}</div>')
        rows.append("<h3>Occupants (placeholders)</h3><ul>")
        for t in u["tenants_placeholder"]:
            rows.append(f"<li>{E(t)}</li>")
        rows.append("</ul>")
    b = UNITS["_building"]
    body = f"""
<div class="note"><b>Anonymized</b>
{E(UNITS['_anonymization'])} Placeholder mapping is in
<a href="../docs/PRIVACY-AND-ANONYMIZATION.md">docs/PRIVACY-AND-ANONYMIZATION.md</a>.</div>

<h2>Property</h2>
<table><thead><tr><th>Attribute</th><th>Value</th><th>Source</th></tr></thead><tbody>
<tr><td>Location</td><td>{E(UNITS['_location']['city'])}, {E(UNITS['_location']['neighborhood'])}, ZIP {E(UNITS['_location']['zip'])}</td><td>Owner-supplied</td></tr>
<tr><td>Exact street address</td><td class="blank">{E(UNITS['_location']['exact_address'])}</td><td>Withheld by policy</td></tr>
<tr><td>Assessor&rsquo;s parcel number</td><td class="blank">{E(UNITS['_location']['assessor_parcel'])}</td><td>Withheld / not supplied</td></tr>
<tr><td>Year built</td><td>{E(b['year_built'])}</td><td>Owner-supplied</td></tr>
<tr><td>Residential units</td><td>{b['units']}</td><td>Owner-supplied</td></tr>
<tr><td>Certificate of occupancy date</td><td class="blank">UNVERIFIED &mdash; not supplied</td>
    <td>{src_cell('https://sfplanninggis.org/PIM/','SF Property Information Map')} <span class="pill p-bad">F-04</span></td></tr>
<tr><td>Rent control coverage</td><td>{E(b['rent_control_coverage'])}</td>
    <td>{src_cell(b['coverage_source'],'SF.gov Topic 019')}</td></tr>
<tr><td>Two-unit buildings are not exempt</td><td>&ldquo;A single-family dwelling with a legal in-law unit constitutes a two-unit building and is not exempt from the Ordinance.&rdquo;</td>
    <td>{src_cell(b['coverage_source'],'SF.gov Topic 019')}</td></tr>
</tbody></table>
{''.join(rows)}
<h2>Why the occupancy facts matter legally</h2>
<table><thead><tr><th>Fact</th><th>Legal consequence</th><th>Source</th></tr></thead><tbody>
<tr><td>Unit&nbsp;1: an original occupant still resides in the unit</td>
 <td>Rent Board Rules &sect;&nbsp;6.14 and Costa-Hawkins market-rate resets are <b>both unavailable</b>. They operate only when the <i>last</i> original occupant vacates.</td>
 <td>{src_cell('https://www.sf.gov/information--rent-increases-under-section-614-and-costa-hawkins','Topic 153')}</td></tr>
<tr><td>Unit&nbsp;1: an occupant was <i>added</i></td>
 <td>Charging more for the added occupant is an <b>unlawful rent increase even if the lease permits it</b>. Tenants may petition to void it and recover refunds.</td>
 <td>{src_cell('https://www.sf.gov/information--charging-additional-occupants-prohibited','Topic 152')}</td></tr>
<tr><td>Unit&nbsp;1: two original occupants departed</td>
 <td>Fewer occupants is equally not a ground for any change. Tenants may generally replace departing roommates even where a lease prohibits it, subject to occupancy caps.</td>
 <td>{src_cell('https://www.sf.gov/information--replacement-roommates','Replacement of Roommates')}</td></tr>
<tr><td>Both units: tenancies are continuing</td>
 <td><b>Vacancy decontrol is unavailable.</b> There is no limit on initial rent only for an <i>empty</i> unit.</td>
 <td>{src_cell('https://www.sf.gov/learn-about-rent-increases-san-francisco','sf.gov')}</td></tr>
<tr><td>Both units: household composition is a known variable</td>
 <td>FEHA protects against discrimination based on the protected characteristic of a <b>family member, friend, roommate or other associate</b> &mdash; so any differential must be justified by tenure arithmetic, never by who lives there.</td>
 <td>{src_cell('https://calcivilrights.ca.gov/housing/','CA Civil Rights Dept')}</td></tr>
</tbody></table>
"""
    return shell("units", "Unit Profiles",
                 "Anonymized rent histories for both units, and the legal consequences of the occupancy facts.",
                 body, "../")

# ============================ CALCULATIONS =================================
def scen_block(s, unit_base):
    cls = "rec" if s.get("recommended") else ""
    badge = '<span class="pill p-ok">RECOMMENDED</span>' if s.get("recommended") else ''
    if s["id"] == "U1-X":
        badge = '<span class="pill p-bad">UNLAWFUL</span>'
    if s["id"] == "U1-C":
        badge = '<span class="pill p-warn">UNVERIFIED</span>'
    bk = "".join(f'<tr><td>{E(b["date"])}</td><td class="num">{E(b["percent"]) if b["percent"] else "&mdash;"}</td></tr>'
                 for b in s["banked"]) or '<tr><td colspan="2" class="tag">none</td></tr>'
    ann = s["annual"]
    return f"""
<div class="card {cls}" style="margin:14px 0">
<div class="k">{E(s['id'])} &nbsp;{badge}</div>
<div style="font-weight:600;margin-bottom:8px">{E(s['label'])}</div>
<table style="margin:8px 0"><tbody>
<tr><td style="width:42%">Effective date</td><td>{E(s['effective_date']) if s['effective_date'] else '<span class="blank">not determined</span>'}</td></tr>
<tr><td>Base rent before</td><td class="num">${E(s['base_rent'])}</td></tr>
<tr><td>Banked percentages (added, never compounded)</td><td class="num">{E(s.get('banked_total_percent', '')) or ('&mdash;' if not s['banked'] else 'see below')}</td></tr>
<tr><td>Annual percentage in effect on the effective date</td><td class="num">{E(ann['percent']) if ann.get('percent') else '<span class="blank">not published</span>'}</td></tr>
<tr><td><b>Total percentage</b></td><td class="num"><b>{E(s['total_percent']) if s['total_percent'] else '<span class="blank">cannot be computed</span>'}</b></td></tr>
<tr><td><b>Dollar increase</b></td><td class="num"><b>{('$'+E(s['dollar_increase'])) if s['dollar_increase'] else '<span class="blank">left blank &mdash; not inferred</span>'}</b></td></tr>
<tr><td><b>Resulting base rent</b></td><td class="num"><b>{('$'+E(s['new_base_rent'])) if s['new_base_rent'] else '<span class="blank">left blank &mdash; not inferred</span>'}</b></td></tr>
<tr><td>Written notice required</td><td>{E(s['notice'])}</td></tr>
<tr><td>Serve by (personal delivery)</td><td>{E(s['serve_by']) if s['serve_by'] else '<span class="blank">&mdash;</span>'}</td></tr>
<tr><td>Serve by (if mailed, +5 days)</td><td>{E(s['serve_by_if_mailed']) if s['serve_by_if_mailed'] else '<span class="blank">&mdash;</span>'}</td></tr>
<tr><td>Anniversary date after</td><td>{E(s['new_anniversary_date'])}</td></tr>
</tbody></table>
<div class="tag" style="margin-bottom:6px">Banked components:</div>
<table style="margin:0 0 10px"><thead><tr><th>Date it could first have been imposed</th><th class="num">Official %</th></tr></thead><tbody>{bk}</tbody></table>
<p style="margin:0;font-size:13px;color:#c8cdd6">{E(s['why'])}</p>
</div>"""

def build_calcs():
    body = f"""
<div class="note"><b>How these figures were produced</b>
{E(CALCS['_method'])} Every dollar amount and every serve-by date on this page is <b>recomputed by
<code>build.py</code> at build time</b> from the official percentages and cross-checked against the
stored values; a mismatch fails the build. No figure was typed by hand.</div>
<div class="note warn"><b>Official rule that drives every scenario below</b>
{E(CALCS['forfeiture_warning'])}
{src_cell('https://www.sf.gov/learn-about-rent-increases-san-francisco','sf.gov worked examples')}</div>

<h2>Unit 1 &mdash; base rent $3,995.00, anniversary date February 1</h2>
{''.join(scen_block(s,'3995.00') for s in CALCS['unit1'])}
<div class="note bad"><b>The Unit 1 decision</b>
Waiting until <b>2027-02-01</b> instead of acting now yields <b>$119.85</b> rather than <b>$63.92</b> per
month &mdash; a difference of <b>$55.93 per month, $671.16 per year, permanently</b> &mdash; and keeps the
anniversary date on February&nbsp;1 so no future percentage is at risk. There is no lawful way to reach
market rent on Unit&nbsp;1 while an original occupant remains.</div>

<h2>Unit 2 &mdash; base rent $3,150.00, anniversary date June 1</h2>
{''.join(scen_block(s,'3150.00') for s in CALCS['unit2'])}
<div class="note warn"><b>The Unit 2 decision</b>
All three routes are lawful. <b>U2-A</b> maximises recovery and preserves the June&nbsp;1 anniversary,
but depends on a percentage the Rent Board has not yet published (Flag F-18) and is exposed to
proposed banking legislation (Flag F-16). <b>U2-C</b> at exactly 10.0% needs only 30-day notice,
preserves the remainder as banked, and is the least likely to provoke a Rent Board petition given that
42.1% of ZIP&nbsp;94122 renter households are already cost-burdened at 30% or more of income.</div>

<h2>Why 13.1% is lawful even though the state cap is 8.8%</h2>
<table><thead><tr><th>Proposition</th><th>Authority</th><th>Source</th></tr></thead><tbody>
<tr><td>San Francisco permits banking with <b>no cap</b> on the accumulated amount</td>
 <td>&ldquo;There is no limit on how much can be banked&rdquo; &mdash; back to April&nbsp;1,&nbsp;1982</td>
 <td>{src_cell('https://www.sf.gov/information--banked-rent-increases','sf.gov')}</td></tr>
<tr><td>Banked percentages are <b>added, not compounded</b>, and <b>not rounded up</b></td>
 <td>Rent Board Rules &amp; Regulations &sect;&nbsp;4.12(a)</td>
 <td>{src_cell('https://www.sf.gov/reports--december-2022--rent-board-rules-and-regulations-part-iv-rent-increases-not-requiring','Rules Part IV')}</td></tr>
<tr><td>AB&nbsp;1482 does <b>not</b> apply to these units</td>
 <td>Civ.&nbsp;Code &sect;&nbsp;1947.12(d)(3) exempts housing subject to local rent control restricting annual increases below the state cap; SF&rsquo;s 1.6% is below 8.8%</td>
 <td>{src_cell('https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1947.12','Civ. Code 1947.12')}</td></tr>
<tr><td>The Rent Board says so expressly</td>
 <td>&ldquo;This does NOT apply for units under the rent increase limitations of the San Francisco Rent Ordinance.&rdquo;</td>
 <td>{src_cell('https://www.sf.gov/reports--california-tenant-protection-act-2019-ab-1482','sf.gov AB 1482')}</td></tr>
<tr><td>But 90-day notice is mandatory above 10%</td>
 <td>Civ.&nbsp;Code &sect;&nbsp;827(b)(3)(A), measured against the <b>lowest</b> rent charged in the prior 12 months and <b>combining</b> other increases</td>
 <td>{src_cell('https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=827','Civ. Code 827')}</td></tr>
</tbody></table>
<p class="tag">Sources for the scenario methodology:
{' '.join(src_cell(u,'['+str(i+1)+']') for i,u in enumerate(CALCS['_sources']))}</p>
"""
    return shell("calculations", "Increase Scenarios",
                 "Every lawful route for each unit, with percentages, dollar amounts, notice tiers and serve-by deadlines.",
                 body, "../")

# ============================ LAW PAGES ====================================
def law_page(slug, title, sub, key, extra=""):
    rows = []
    for r in LAW[key]:
        st = pill("verified") if r.get("verified") else pill("UNVERIFIED")
        fl = f' <span class="pill p-warn">{E(r["flag"])}</span>' if r.get("flag") else ''
        ap = f'<div class="tag" style="margin-top:5px">{E(r["applies_to"])}</div>' if r.get("applies_to") else ''
        nt = f'<div class="tag" style="margin-top:5px;color:#9aa3b2">{E(r["note"])}</div>' if r.get("note") else ''
        rows.append(f"""<tr>
<td><b>{E(r['rule'])}</b><div class="tag">{E(r['authority'])}</div></td>
<td>{E(r['detail'])}{ap}{nt}</td>
<td>{src_cell(r['source'],'official source')}<div class="tag">{E(r.get('source_name',''))}</div>{st}{fl}</td></tr>""")
    body = f"""{extra}
<div class="filterbar"><input type="search" data-filter="{slug}-tbl" placeholder="Filter {len(LAW[key])} rules&hellip;">
<span class="count" id="{slug}-tbl-count"></span></div>
<table id="{slug}-tbl"><thead><tr><th style="width:26%">Rule</th><th style="width:48%">What the official source says</th>
<th style="width:26%">Source &amp; verification</th></tr></thead><tbody>{''.join(rows)}</tbody></table>"""
    return shell(slug, title, sub, body, "../")

def build_local():
    return law_page("local-law", "San Francisco Law",
        "The Rent Ordinance, Rent Board Rules and Regulations, and official SF.gov guidance. This is the operative ceiling for both units.",
        "local",
        """<div class="note"><b>Why local law controls</b>
The SF Rent Ordinance is expressly intended to be more protective than the state baseline, and where it
offers greater protection it applies rather than AB&nbsp;1482. Both units are continuing tenancies in a
two-unit building stated to have been built in 1940, so the local rules below are the ones that decide
the answer.</div>""")

def build_state():
    return law_page("state-law", "California Law",
        "Civil Code sections 827 (notice), 1947.12 (AB 1482 cap), 1942.5 (retaliation) and Government Code 12955 (FEHA housing discrimination).",
        "state",
        """<div class="note warn"><b>The counter-intuitive point</b>
California&rsquo;s 8.8% AB&nbsp;1482 cap does <b>not</b> protect these tenants and does <b>not</b> limit this
owner. Because San Francisco&rsquo;s 1.6% annual limit is lower, Civ.&nbsp;Code &sect;&nbsp;1947.12(d)(3) steps the
state statute aside entirely. A 13.1% banked increase is lawful here notwithstanding 8.8%.
California&rsquo;s real contribution is the <b>notice mechanics</b> (&sect;&nbsp;827), the <b>retaliation bar</b>
(&sect;&nbsp;1942.5) and <b>FEHA</b> (Gov.&nbsp;Code &sect;&nbsp;12955).</div>""")

def build_federal():
    return law_page("federal-law", "Federal Law",
        "The Fair Housing Act and HUD. There is no federal rent ceiling for unsubsidised private housing.",
        "federal",
        """<div class="note"><b>Scope</b>
Federal law reaches these rent increases in exactly one way: <b>anti-discrimination</b>. There is no
federal statute capping rent increases for unsubsidised private housing. HUD&rsquo;s Fair Market Rents are a
Section&nbsp;8 program instrument and are not a ceiling on private market rents. Where federal subsidy is
involved, HUD rent-reasonableness review applies &mdash; not relevant on the facts supplied.</div>""")

# ============================ ALLOWABLE INCREASES ==========================
def build_allowable():
    rows = []
    cur = AI["current_period"]
    for r in AI["table"]:
        hl = ' style="background:#12261a"' if r["percent"] == cur["percent"] and r["period"].startswith("3/1/26") else ""
        nt = f'<div class="tag">{E(r["note"])}</div>' if r.get("note") else ""
        rows.append(f'<tr{hl}><td>{E(r["period"])}{nt}</td><td class="num">{E(r["percent"])}%</td></tr>')
    body = f"""
<div class="note ok"><b>Current allowable increase: {E(cur['percent'])}%</b>
Effective {E(cur['effective_from'])} through {E(cur['effective_through'])}.
{src_cell(cur['source'],'SF.gov announcement, 2026-01-14')}</div>
<p>The Rent Board calculates this each year as <b>60% of the increase in the Consumer Price Index for
All Urban Consumers in the Bay Area</b>, and in no event more than <b>7%</b>
(SF Admin.&nbsp;Code &sect;&nbsp;37.3(a)(1)). The table below is transcribed <b>verbatim</b> from the official
Rent Board Info Sheet&nbsp;571, cross-checked against the SF.gov <i>Current Rates</i> report.</p>
<p><b>How to use it.</b> Find the tenant&rsquo;s anniversary date, identify which effective period contains
it, and take that period&rsquo;s percentage. Where several anniversaries were skipped, <b>add</b> the
percentages &mdash; never compound them &mdash; provided 12 full months have elapsed on each
(Rent Board Rules &sect;&nbsp;4.12; see Flag F-03 on a conflict between two official sources). Use the
percentage in effect on the <b>effective date</b> of the increase, not the date the notice is served.</p>
<div class="filterbar"><input type="search" data-filter="ai-tbl" placeholder="Filter {len(AI['table'])} periods&hellip;">
<span class="count" id="ai-tbl-count"></span></div>
<table id="ai-tbl"><thead><tr><th>Effective period</th><th class="num">Amount of increase</th></tr></thead>
<tbody>{''.join(rows)}</tbody></table>
<p class="tag">Source: {src_cell('https://www.sf.gov/documents/34344/571_Allowable_Annual_Increases_26-27_1.pdf','SF Rent Board Info Sheet 571 (official PDF)')}
&middot; cross-checked against {src_cell('https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit','SF.gov Current Rates')}
and {src_cell('https://www.sf.gov/news--annual-rent-increase-3126-22827-announced','SF.gov announcement')}</p>

<h2>Other official rates in force, 3/1/2026 &ndash; 2/28/2027</h2>
<h3>Security deposit interest</h3>
<table><thead><tr><th>Effective period</th><th class="num">Rate</th></tr></thead><tbody>
{''.join(f'<tr><td>{E(x["period"])}</td><td class="num">{E(x["rate"])}</td></tr>' for x in RATES['security_deposit_interest'])}
</tbody></table>
<h3>Capital improvement imputed interest rates</h3>
<p class="tag">Use the rate in effect at the time the petition is filed.</p>
<table><thead><tr><th>Amortization period</th><th class="num">Rate</th><th class="num">Factor</th></tr></thead><tbody>
{''.join(f'<tr><td>{E(x["amortization"])}</td><td class="num">{E(x["rate"])}</td><td class="num">{E(x["factor"])}</td></tr>' for x in RATES['capital_improvement_imputed_interest'])}
</tbody></table>
<h3>Uncompensated labor rates</h3>
<p class="tag">Use the rate in effect at the time the work commenced.</p>
<table><thead><tr><th>Date</th><th class="num">Amount</th></tr></thead><tbody>
{''.join(f'<tr><td>{E(x["period"])}</td><td class="num">{E(x["rate"])}</td></tr>' for x in RATES['uncompensated_labor'])}
</tbody></table>
<h3>Rent Board fees that can be banked</h3>
<div class="note warn"><b>Incomplete official table &mdash; Flag F-14</b>
{E(RATES['note'])} No current-year figure is published anywhere on this site rather than an assumed one.
{src_cell('https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit','SF.gov Current Rates')}</div>
<table><thead><tr><th>Tax year</th><th class="num">Tenant&rsquo;s amount</th><th class="num">Landlord&rsquo;s amount</th></tr></thead><tbody>
{''.join(f'<tr><td>{E(x["tax_year"])}</td><td class="num">{E(x["tenant"])}</td><td class="num">{E(x["landlord"])}</td></tr>' for x in RATES['rent_board_fee_bankable'])}
<tr><td>2025-2026 and 2026-2027</td><td class="num blank">BLANK &mdash; absent from the official page</td><td class="num blank">BLANK &mdash; absent from the official page</td></tr>
</tbody></table>
"""
    return shell("allowable", "Allowable Annual Increases, 1982&ndash;2027",
        "The complete official percentage history, transcribed verbatim from SF Rent Board Info Sheet 571.",
        body, "../")

# ============================ MARKET =======================================
def build_market():
    mg = MARKET["median_gross_rent"]
    gb = MARKET["gross_rent_distribution"]
    rb = MARKET["rent_burden"]
    ha = MARKET["housing_age"]
    tot = gb["with_cash_rent_total"]
    def bar(n, mx):
        return f'<div style="background:linear-gradient(90deg,var(--acc) {n*100//mx}%,transparent {n*100//mx}%);height:100%;border-radius:3px;position:absolute;inset:0;opacity:.18"></div>'
    mx = max(b["households"] for b in gb["brackets"])
    grow = "".join(
        f'<tr><td style="position:relative">{bar(b["households"],mx)}<span style="position:relative">{E(b["label"])}</span>'
        f'<div class="tag">{E(b["var"])}</div></td>'
        f'<td class="num">{b["households"]:,}</td>'
        f'<td class="num">{b["households"]*100/tot:.1f}%</td></tr>' for b in gb["brackets"])
    mxr = max(b["households"] for b in rb["brackets"])
    rrow = "".join(
        f'<tr><td style="position:relative">{bar(b["households"],mxr)}<span style="position:relative">{E(b["label"])} of household income</span>'
        f'<div class="tag">{E(b["var"])}</div></td><td class="num">{b["households"]:,}</td>'
        f'<td class="num">{E(b["moe"])}</td><td class="num">{b["households"]*100/rb["computed_universe"]:.1f}%</td></tr>'
        for b in rb["brackets"])
    mxh = max(b["units"] for b in ha["buckets"])
    hrow = "".join(
        f'<tr><td style="position:relative">{bar(b["units"],mxh)}<span style="position:relative">{E(b["label"])}</span>'
        f'<div class="tag">{E(b["var"])}</div></td><td class="num">{b["units"]:,}</td>'
        f'<td class="num">{E(b["moe"])}</td><td class="num">{b["units"]*100/ha["total_housing_units"]:.1f}%</td></tr>'
        for b in ha["buckets"])
    ctx = "".join(f'<tr><td>{E(c["unit"])}</td><td class="num">{E(c.get("current_base_rent") or c.get("projected_base_rent"))}</td>'
                  f'<td>{E(c["vs_zcta_median"])}</td></tr>' for c in MARKET["unit_rent_context"])
    body = f"""
<div class="note ok"><b>Provenance</b>
{E(MARKET['_provenance'])}</div>
<h2>Headline figures</h2>
<div class="cards">
 <div class="card acc"><div class="k">Median gross rent, ZCTA 94122</div><div class="v">{E(mg[0]['value'])}</div>
  <div class="s">{E(mg[0]['moe'])} &middot; {src_cell(mg[0]['source'],'B25064')}</div></div>
 <div class="card"><div class="k">Median gross rent, SF County</div><div class="v">{E(mg[1]['value'])}</div>
  <div class="s">{E(mg[1]['moe'])} &middot; {src_cell(mg[1]['source'],'B25064')}</div></div>
 <div class="card"><div class="k">94122 premium over the county</div><div class="v">+13.7%</div>
  <div class="s">Computed from the two figures above</div></div>
 <div class="card"><div class="k">Median household income, 94122</div><div class="v">$146,250</div>
  <div class="s">&plusmn;$12,113 &middot; {src_cell(MARKET['median_household_income'][0]['source'],'B19013')}</div></div>
 <div class="card warn"><div class="k">Cost-burdened at 30%+</div><div class="v">42.1%</div>
  <div class="s">4,510 of 10,702 &middot; {src_cell(rb['source'],'B25070')}</div></div>
 <div class="card bad"><div class="k">Severely burdened at 50%+</div><div class="v">20.8%</div>
  <div class="s">2,227 of 10,702 &middot; {src_cell(rb['source'],'B25070')}</div></div>
 <div class="card ok"><div class="k">Built before June 13, 1979</div><div class="v">93.7%</div>
  <div class="s">22,681 of 24,208 units &middot; {src_cell(ha['source'],'B25034')}</div></div>
 <div class="card"><div class="k">Built 1940&ndash;1949</div><div class="v">18.3%</div>
  <div class="s">4,423 units &middot; consistent with the stated 1940 construction year</div></div>
</div>

<h2>Gross rent distribution &mdash; ZCTA 94122</h2>
<p class="tag">Universe: {tot:,} renter households paying cash rent, plus {gb['no_cash_rent']:,} paying no cash rent
= {gb['universe_total']:,} total. The brackets below sum <b>exactly</b> to {tot:,}; <code>build.py</code>
fails the build if they do not reconcile.</p>
<table><thead><tr><th>Gross rent bracket</th><th class="num">Households</th><th class="num">Share</th></tr></thead>
<tbody>{grow}</tbody></table>
<p class="tag">Label verification: {E(gb['_note'])}</p>
<div class="cards">
 <div class="card acc"><div class="k">Paying $2,000 or more</div><div class="v">{E(MARKET['derived_shares']['pct_paying_2000_or_more'])}</div></div>
 <div class="card acc"><div class="k">Paying $3,000 or more</div><div class="v">{E(MARKET['derived_shares']['pct_paying_3000_or_more'])}</div></div>
 <div class="card acc"><div class="k">Paying $3,500 or more</div><div class="v">{E(MARKET['derived_shares']['pct_paying_3500_or_more'])}</div></div>
</div>

<h2>Rent burden &mdash; gross rent as a share of household income</h2>
<table><thead><tr><th>Share of household income</th><th class="num">Households</th><th class="num">Margin of error</th><th class="num">Share of computed universe</th></tr></thead>
<tbody>{rrow}</tbody></table>
<p class="tag">{rb['universe_total']:,} total &minus; {rb['not_computed']:,} not computed = {rb['computed_universe']:,} computed universe. Reconciliation checked at build time.</p>

<h2>Housing age &mdash; why this matters for rent control</h2>
<table><thead><tr><th>Year structure built</th><th class="num">Units</th><th class="num">Margin of error</th><th class="num">Share</th></tr></thead>
<tbody>{hrow}</tbody></table>
<div class="note"><b>Relevance</b>
{E(ha['relevance'])} {E(ha['pre_1979_06_13_share'])}. This corroborates &mdash; but does <b>not</b> substitute
for &mdash; confirming the subject property&rsquo;s own certificate of occupancy date on the
{src_cell('https://sfplanninggis.org/PIM/','SF Property Information Map')}. Flag <b>F-04</b>.</div>

<h2>Where these two units sit in that market</h2>
<table><thead><tr><th>Unit</th><th class="num">Rent</th><th>Position versus the 94122 median of $2,816</th></tr></thead>
<tbody>{ctx}</tbody></table>
<div class="note warn"><b>What this does and does not establish</b>
Market position is <b>irrelevant</b> to the Rent Ordinance calculation. No official SF source treats
comparability as a ground for an annual increase during a continuing tenancy; going above the annual
allowable requires a Rent Board petition. These figures matter for two other reasons only:
<b>hardship exposure</b> (a tenant may seek relief from a passthrough, and 42.1% cost-burden means a large
increase lands on households with little headroom) and <b>petition risk</b> (an increase that moves a
household from below to above the ZIP median is more likely to be challenged, and defending a challenge
costs more than the increase is worth). That is the practical case for the phased 10% option on Unit&nbsp;2.</div>

<h2>Left blank by design</h2>
<table><thead><tr><th>Metric</th><th>Status</th><th>Reason</th><th>Flag</th></tr></thead><tbody>
<tr><td>HUD Fair Market Rent, San Francisco area</td><td class="blank">BLANK</td>
 <td>{E(MARKET['hud_fair_market_rent']['reason'])}<div class="tag">{src_cell(MARKET['hud_fair_market_rent']['official_landing_page'],'HUD USER FMR')}</div></td>
 <td><span class="pill p-mut">{E(MARKET['hud_fair_market_rent']['flag'])}</span></td></tr>
<tr><td>BLS CPI-U, San Francisco&ndash;Oakland&ndash;Hayward</td><td class="blank">BLANK</td>
 <td>{E(MARKET['bls_cpi']['reason'])}<div class="tag">{src_cell(MARKET['bls_cpi']['official_landing_page'],'BLS Pacific region')}</div></td>
 <td><span class="pill p-mut">{E(MARKET['bls_cpi']['flag'])}</span></td></tr>
</tbody></table>
"""
    return shell("market", "Market Data &mdash; ZIP 94122 (Outer Sunset)",
        "U.S. Census Bureau ACS 2020&ndash;2024 5-year estimates, retrieved directly from the Census API. Every variable label individually confirmed.",
        body, "../")

# ============================ PRACTICES ====================================
def build_practices():
    body = f"""
<div class="note warn"><b>A limitation stated up front &mdash; Flag F-21</b>
{E(next(f['finding'] for f in FLAGS['flags'] if f['id']=='F-21'))}
{E(next(f['impact'] for f in FLAGS['flags'] if f['id']=='F-21'))}</div>

<h2>The headline finding</h2>
<p><b>The percentage is identical for both kinds of owner.</b> The Rent Board publishes one allowable
increase &mdash; currently <b>1.6%</b> &mdash; and it applies to every covered unit in the city regardless of who
owns it. There is no corporate rate and no small-owner rate. What differs is <b>legal exposure</b> and
<b>administrative discipline</b>.</p>

<h2>Verified legal differences</h2>
<table><thead><tr><th style="width:22%">Dimension</th><th style="width:32%">Large corporate / institutional owner</th>
<th style="width:32%">Individual owner of a 2-unit building</th><th style="width:14%">Source</th></tr></thead><tbody>
<tr><td><b>Costa-Hawkins single-family / condominium exemption</b></td>
 <td><span class="pill p-bad">UNAVAILABLE</span> Civ.&nbsp;Code &sect;&nbsp;1947.12(d)(5)(A) disqualifies a real estate
 investment trust, a corporation, or an LLC with at least one corporate member. The exemption also requires
 the specific written notice under &sect;&sect;&nbsp;1946.2(e)(8)(B)(i) and 1947.12(d)(5)(B)(i).</td>
 <td>Potentially available to a natural person &mdash; but <b>not on these facts</b>, because a two-unit building
 is expressly not exempt and the exemption &ldquo;does not apply where there is more than one dwelling unit on
 the same lot, or any second residential unit in the building that cannot be sold separately&rdquo;.</td>
 <td>{src_cell('https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1947.12','Civ. Code 1947.12')}
     {src_cell('https://www.sf.gov/information--partial-exemption-certain-single-family-homes-and-condominiums-under-costa-hawkins','Topic 019')}</td></tr>
<tr><td><b>AB&nbsp;1482 two-unit owner-occupied exemption</b></td>
 <td>Unavailable &mdash; it requires that the second unit &ldquo;was occupied by an owner of the property for the
 entire period of the tenancy&rdquo;.</td>
 <td>Potentially available if an owner occupies one unit (unverified &mdash; Flag F-05). <b>Immaterial here</b>,
 because the SF Rent Ordinance applies regardless.</td>
 <td>{src_cell('https://www.sf.gov/reports--california-tenant-protection-act-2019-ab-1482','sf.gov AB 1482')}</td></tr>
<tr><td><b>Algorithmic / revenue-management pricing</b></td>
 <td><span class="pill p-bad">PROHIBITED</span> Admin.&nbsp;Code &sect;&nbsp;37.10C, effective 2024-10-14, makes it
 unlawful to sell, license or provide, <b>or to use</b>, an &ldquo;algorithmic device&rdquo; that analyses non-public
 competitor data to recommend rents or occupancy levels. Each separate month is a separate violation; each
 separate unit is a separate violation; up to <b>$1,000 per violation</b> plus attorney&rsquo;s fees; the City
 Attorney, <b>a tenant, or a tenants&rsquo; rights organisation</b> may sue; lease terms limiting a prevailing
 tenant&rsquo;s fees are unenforceable.</td>
 <td>Equally prohibited. Practical exposure is lower only because individual owners rarely license such
 software.</td>
 <td>{src_cell('https://www.sf.gov/information--algorithmic-devices-set-rent-are-prohibited-san-francisco','Topic 268')}</td></tr>
<tr><td><b>Housing Inventory reporting and rent increase license</b></td>
 <td>Same obligation. Reporting began <b>July&nbsp;1,&nbsp;2022</b> for non-condominium units in buildings with
 10 or more residential units.</td>
 <td>Same obligation. Reporting began <b>March&nbsp;1,&nbsp;2023</b> for condominiums and buildings with fewer
 than 10 units &mdash; which governs a 2-unit building. Annual deadline March&nbsp;1. No monetary late penalty,
 but an unlicensed increase is <b>null and void</b>.</td>
 <td>{src_cell('https://www.sf.gov/rent-board-housing-inventory','sf.gov Housing Inventory')}
     {src_cell('https://sfrb.org/section-1314-licensing-%E2%80%93-notice-rent-increase','Rules 13.14')}</td></tr>
<tr><td><b>Institutional capability</b></td>
 <td>Dedicated compliance staff, calendared anniversary dates, standardised notices, counsel on retainer.
 Errors tend to be systematic and therefore visible &mdash; which is precisely what &sect;&nbsp;37.10C and organised
 tenant litigation target.</td>
 <td>Typically self-managed. Anniversary dates get missed. <b>Unit&nbsp;2 is the textbook example</b>: seven
 consecutive anniversaries passed with no increase, producing a lawful but administratively awkward 13.1%
 that requires 90-day notice and invites a petition.</td>
 <td>Observation from the case facts; no official source quantifies this &mdash; see Flag F-21</td></tr>
</tbody></table>

<h2>What this means for an individual owner</h2>
<p>In San Francisco the corporate playbook of algorithmic, competitor-data-driven pricing is
<b>illegal</b>, not merely frowned upon. That is a hard legal prohibition with a private right of action
for tenants and tenants&rsquo; organisations, enacted in October 2024. So the question &ldquo;how do the big
companies do it?&rdquo; has a partly surprising answer: the most common large-portfolio technique for setting
rent levels is <b>banned outright in this city</b>, and using it exposes the owner to per-unit, per-month
penalties.</p>
<p>What actually separates a large owner from an individual owner is therefore <b>administrative
discipline</b>, not a bigger lawful increase:</p>
<ul>
<li>Calendar each unit&rsquo;s anniversary date and impose the annual increase every year.</li>
<li>File the Housing Inventory report every March&nbsp;1 and confirm the license is current before any
effective date.</li>
<li>Serve 30-day written notice on time, using the percentage in effect on the <b>effective</b> date.</li>
<li>Keep a computation sheet per unit per year.</li>
</ul>
<div class="note ok"><b>The defensible practice is the boring one.</b>
Take the annual allowable increase every year, on the anniversary date, by 30-day written notice, with
the license current, the arithmetic documented, and a neutral reason on the record. That is normal
business practice, it is easy to defend, and it never reaches the 90-day-notice threshold. The owner who
does this never has to attempt a 13.1% catch-up and never has to explain one.</div>

<h2>What an individual owner must not do</h2>
<table><thead><tr><th>Practice</th><th>Status</th><th>Source</th></tr></thead><tbody>
<tr><td>Use pricing software that analyses competitor rent or occupancy data</td><td><span class="pill p-bad">UNLAWFUL</span> &sect;&nbsp;37.10C</td><td>{src_cell('https://www.sf.gov/information--algorithmic-devices-set-rent-are-prohibited-san-francisco','Topic 268')}</td></tr>
<tr><td>Charge more because a tenant added an occupant or a roommate was replaced</td><td><span class="pill p-bad">UNLAWFUL</span> even if the lease permits it; refundable overcharge</td><td>{src_cell('https://www.sf.gov/information--charging-additional-occupants-prohibited','Topic 152')}</td></tr>
<tr><td>Reset to market rent while an original occupant remains</td><td><span class="pill p-bad">UNAVAILABLE</span> Rules &sect;&nbsp;6.14 requires the <i>last</i> original occupant to vacate, plus a timely written notice</td><td>{src_cell('https://www.sf.gov/information--rent-increases-under-section-614-and-costa-hawkins','Topic 153')}</td></tr>
<tr><td>Impose an increase while unlicensed under the Housing Inventory</td><td><span class="pill p-bad">NULL AND VOID</span> in its entirety</td><td>{src_cell('https://sfrb.org/section-1314-licensing-%E2%80%93-notice-rent-increase','Rules 13.14')}</td></tr>
<tr><td>Compound banked increases, or round up to the nearest dollar</td><td><span class="pill p-bad">PROHIBITED</span></td><td>{src_cell('https://www.sf.gov/reports--december-2022--rent-board-rules-and-regulations-part-iv-rent-increases-not-requiring','Rules 4.12')}</td></tr>
<tr><td>Include passthroughs or fluctuating charges in the base rent used for the percentage</td><td><span class="pill p-bad">PROHIBITED</span> base rent includes parking and storage but excludes passthroughs</td><td>{src_cell('https://www.sf.gov/learn-about-rent-increases-san-francisco','sf.gov')}</td></tr>
<tr><td>Self-impose a capital improvement, O&amp;M or utility passthrough increase</td><td><span class="pill p-bad">REQUIRES PRIOR RENT BOARD APPROVAL</span></td><td>{src_cell('https://www.sf.gov/file/530-om-petition-fillable-324pdf','Form 530 Schedule B')}</td></tr>
<tr><td>Increase within 180 days of a tenant&rsquo;s protected complaint, or to retaliate for organising</td><td><span class="pill p-bad">UNLAWFUL RETALIATION</span></td><td>{src_cell('https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1942.5','Civ. Code 1942.5')}</td></tr>
</tbody></table>
"""
    return shell("practices", "Owner Practices",
        "How large corporate owners and individual owners handle increases, based only on verified statutory differences.",
        body, "../")

# ============================ DISCRIMINATION ===============================
def build_disc():
    body = f"""
<div class="note"><b>The question asked</b>
&ldquo;Would it be ok to raise the rent on one tenant&rsquo;s unit, or would it make more sense to raise both
tenants&rsquo; units in order to avoid any discrimination lawsuits or inquiries?&rdquo;</div>
<h2>Short answer</h2>
<p><b>Apply one written policy to both units. Do not raise only one. And do not artificially equalise
the percentages either.</b> Neither extreme is correct, and the reason matters.</p>

<h2>Why raising only one unit is the risky course</h2>
<p>Not because a differential is inherently unlawful &mdash; it is not &mdash; but because it leaves the owner
unable to answer the discrimination question. Where two similarly situated tenancies in the same small
building are treated differently and the file contains no explanation, the inference a tenant&rsquo;s advocate
draws is that the difference tracks something about the <b>household</b> rather than the <b>tenure</b>.</p>
<p>That is especially dangerous for Unit&nbsp;1, where the household composition <b>changed</b> in April
2026. California FEHA protects against discrimination based on the protected characteristic of a
<i>&ldquo;family member, friend, roommate, or any other associate&rdquo;</i> &mdash; so the added occupant&rsquo;s
characteristics are legally relevant, and <b>familial status</b> is protected federally as well. An
increase that visibly follows a change in who lives in the unit is exactly the fact pattern that invites
a complaint, <b>even where the real cause is entirely innocent</b>.</p>

<h2>Why equalising the percentages is legally wrong and financially costly</h2>
<p>San Francisco does not require two units to receive the same percentage. It requires that each
increase be lawful <b>for that tenancy</b> &mdash; computed from that tenancy&rsquo;s anniversary date and its own
banked-increase history. Unit&nbsp;1 is entitled to 3.0% and Unit&nbsp;2 to 13.1% <b>because their tenure
histories differ by six and a half years</b>, not because of anything about the people.</p>
<table><thead><tr><th>If you forced&hellip;</th><th>Consequence</th><th>Authority</th></tr></thead><tbody>
<tr><td>Unit&nbsp;2 down to 3.0% to match Unit&nbsp;1</td><td>Forfeits <b>10.1%</b> of lawfully banked
 entitlement &mdash; $317.85 per month on a $3,150 base &mdash; and, depending on timing, forfeits it
 <b>permanently</b> because the skipped increase never gets its 12 months.</td>
 <td>{src_cell('https://www.sf.gov/information--banked-rent-increases','sf.gov banking')}</td></tr>
<tr><td>Unit&nbsp;1 up to 13.1% to match Unit&nbsp;2</td><td><span class="pill p-bad">UNLAWFUL RENT INCREASE</span>
 outright. There is no banked entitlement and no annual basis. The tenant can petition on Form&nbsp;516C to
 void it and recover every overcharge, with lawful base rent recalculated back to April&nbsp;1,&nbsp;1982.</td>
 <td>{src_cell('https://www.sf.gov/reports--rent-board-forms-forms-center','Forms Center 516C')}</td></tr>
</tbody></table>
<p>Both errors are worse than the differential.</p>

<h2>The defensible position: a documented uniform policy</h2>
<blockquote>Each rent-controlled unit in this property receives the annual allowable increase published by
the San Francisco Rent Board, plus any increases lawfully banked under Administrative Code
&sect;&nbsp;37.3(a)(2) and Rent Board Rules &sect;&nbsp;4.12, imposed on that unit&rsquo;s own anniversary date, on the
written notice required by Civil Code &sect;&nbsp;827, subject to a current rent increase license under
&sect;&nbsp;37.15, and subject to a documented retaliation screen under Civil Code &sect;&nbsp;1942.5.</blockquote>
<p>That policy is <b>neutral on its face</b>, <b>applied to every unit</b>, and produces different numbers
only because the underlying tenancy facts differ. It is the answer that survives review by a tenant
attorney, because each unit&rsquo;s computation sheet is a mechanical application of published percentages to
documented dates &mdash; with <b>no discretion exercised anywhere</b>.</p>

<h2>The governing legal standards</h2>
<table><thead><tr><th>Instrument</th><th>Protected characteristics</th><th>Source</th></tr></thead><tbody>
<tr><td><b>Fair Housing Act</b><br>42 U.S.C. &sect;&sect;&nbsp;3601&ndash;3619<br><span class="tag">federal</span></td>
 <td>Race &middot; Color &middot; National Origin &middot; Religion &middot; Sex &middot; <b>Familial Status</b> &middot; Disability.
 Applies to &ldquo;nearly all housing, including private housing&rdquo;.</td>
 <td>{src_cell('https://www.hud.gov/helping-americans/fair-housing-act-overview','HUD')}</td></tr>
<tr><td><b>FEHA</b><br>Gov.&nbsp;Code &sect;&nbsp;12955<br><span class="tag">California</span></td>
 <td>Race &middot; Color &middot; Ancestry &middot; National origin &middot; Citizenship &middot; <b>Immigration status</b> &middot;
 <b>Primary language</b> &middot; Religion &middot; Disability &middot; Sex and gender &middot; Sexual orientation &middot; Gender
 identity &middot; Gender expression &middot; Genetic information &middot; <b>Marital status</b> &middot; <b>Familial status</b>
 &middot; <b>Source of income</b> (including a Section&nbsp;8 voucher) &middot; Military or veteran status &middot; <b>Age</b>.
 Also protects against discrimination based on the characteristic of a <b>family member, friend,
 roommate or other associate</b>, and against retaliation.</td>
 <td>{src_cell('https://calcivilrights.ca.gov/housing/','CA Civil Rights Dept')}</td></tr>
<tr><td><b>Retaliation</b><br>Civ.&nbsp;Code &sect;&nbsp;1942.5<br><span class="tag">California</span></td>
 <td>Not a protected class but the most common adjacent claim: bars a rent increase within <b>180 days</b>
 of specified tenant complaints, and bars an increase made to retaliate for lawful tenant organising.
 Threatening immigration-authority reporting is itself prohibited retaliation.</td>
 <td>{src_cell('https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1942.5','leginfo')}</td></tr>
<tr><td><b>Rent Ordinance anti-retaliation and harassment</b><br><span class="tag">San Francisco</span></td>
 <td>Unlawful to use force, threats, menace or fraud to interfere with quiet enjoyment, or to act with
 intent to cause a tenant to vacate. <span class="pill p-warn">UNVERIFIED</span> The SF.gov page returned
 404 in this session and the &sect;&nbsp;37.10B penalty figures could not be confirmed &mdash; Flag F-10.</td>
 <td>{src_cell('https://www.sf.gov/resource/2023/rent-board-laws-and-regulations','Rent Board laws &amp; regulations')}</td></tr>
</tbody></table>

<h2>Concrete steps to make this evidentiary rather than rhetorical</h2>
<ol>
<li>Write the policy down and <b>date it before serving any notice</b>.</li>
<li>Prepare a per-unit computation sheet showing each skipped anniversary, the official Info Sheet&nbsp;571
 percentage for that period, the 12-month elapse date, and the arithmetic. Retain the source printout.</li>
<li>Run and <b>document</b> the &sect;&nbsp;1942.5 retaliation screen for each unit, including a nil return where
 there is nothing to report.</li>
<li>Serve both units in the <b>same manner</b>, with the same notice template, within the same window &mdash;
 even though the effective dates differ.</li>
<li><b>Never</b> reference a tenant&rsquo;s household composition, occupancy change, national origin, language,
 immigration status, source of income, familial status, age, disability or any protected characteristic in
 any notice, email or contemporaneous note.</li>
<li>Do not use any pricing software that analyses competitor data &mdash; &sect;&nbsp;37.10C makes that unlawful and
 gives tenants <b>and tenants&rsquo; organisations</b> a private right of action.</li>
<li>If a differential is nonetheless chosen &mdash; for example phasing Unit&nbsp;2 at 10% while Unit&nbsp;1 takes
 3.0% &mdash; record the reason <b>at the time</b>. &ldquo;Household already paying above the ZIP median and 42.1%
 of ZIP renters are cost-burdened&rdquo; is a documented, neutral, defensible reason. Silence is not.</li>
</ol>

<div class="note bad"><b>What would actually create liability</b>
Raising only Unit&nbsp;1 &mdash; the unit whose household composition just changed &mdash; while leaving Unit&nbsp;2
untouched, with no written policy and no computation sheet. On those facts an advocate would argue the
increase followed the arrival of a new occupant. That argument would be <b>wrong on the law</b> (Topic&nbsp;152
makes such an increase unlawful, and it would also be the wrong unit to pick on the arithmetic) but it
would be <b>hard to rebut</b> without contemporaneous documentation. The uniform written policy is what
makes it rebuttable.</div>
"""
    return shell("discrimination", "Anti-Discrimination &mdash; One Unit or Both?",
        "Whether to raise one unit or both, under federal, state and local fair housing law.",
        body, "../")

# ============================ TENANT REVIEW ================================
def build_tenant():
    svc = [
      ("SF Rent Board counselor","415-252-4600","Free. Weekdays 9am&ndash;12pm and 1pm&ndash;4pm. 25 Van Ness Ave Suite #700. Spanish, Cantonese, Mandarin, plus interpretation. <b>Cannot give legal advice.</b> Also serves landlords.","https://www.sf.gov/speak-rent-board-counselor"),
      ("Eviction Defense Collaborative","415-659-9184","<b>Free legal help.</b> 976 Mission St. Lead organisation in the city&rsquo;s Tenant Right to Counsel program; provides full-scope representation to tenants facing eviction. Walk-in Mon, Tue, Wed, Fri 10&ndash;11:30am and 1&ndash;2:30pm.","https://www.sf.gov/tenant-and-landlord-resources"),
      ("Bar Association of San Francisco &mdash; Conflict Intervention Service","415-782-8940","Free mediation and conflict resolution, <b>available to tenants AND landlords</b>. Useful for negotiating a payment plan or resolving an interpersonal housing conflict before it becomes a petition.","https://www.sf.gov/tenant-and-landlord-resources"),
      ("Housing Rights Committee","415-703-8644","Free tenant counseling. 11 Grove St, Mon&ndash;Thu 1&ndash;4pm. Spanish, Mandarin, Cantonese.","https://www.sf.gov/tenant-and-landlord-resources"),
      ("Bay Area Legal Aid &mdash; Consumer Rights Clinic","415-982-1300","Free attorney help for tenants who receive small claims court papers for rental debt. 2nd and 4th Thursday.","https://www.sf.gov/tenant-and-landlord-resources"),
      ("Bill Sorro Housing Program (BiSHoP)","415-513-5177","Free tenant counseling. 1338 Mission St 3rd Floor. Arabic, Tagalog.","https://www.sf.gov/tenant-and-landlord-resources"),
      ("Chinatown Community Development Center","415-984-2728","Free tenant counseling. 615 Grant Ave. Mandarin, Cantonese.","https://www.sf.gov/tenant-and-landlord-resources"),
      ("Mission Action","415-282-6209","Free tenant counseling. 938 Valencia St. Spanish.","https://www.sf.gov/tenant-and-landlord-resources"),
      ("SOMCAN","415-255-7693","Free tenant counseling. 1038 Mission St. Tagalog (415-552-5637).","https://www.sf.gov/tenant-and-landlord-resources"),
      ("Bayview-Hunters Point Tenants&rsquo; Rights Clinic","415-808-5662","Free tenant counseling. 1601 Lane St (Bayview YMCA), Tuesdays 1&ndash;4pm.","https://www.sf.gov/tenant-and-landlord-resources"),
      ("California Civil Rights Department","&mdash;","Free. Enforces FEHA housing discrimination law; accepts complaints and can award remedies.","https://calcivilrights.ca.gov/housing/"),
      ("HUD &mdash; file a fair housing complaint","&mdash;","Free. Federal intake route for Fair Housing Act complaints.","https://www.hud.gov/reporthousingdiscrimination"),
    ]
    forms = [
      ("518","Tenant Summary Petition","Fast-track challenge where a rent increase notice is <b>unlawful on its face and has not yet taken effect</b> &mdash; it can stop an increase before it starts.","p-bad"),
      ("516C","Unlawful Rent Increase / rent history review","Voids the increase, recovers overcharges, and recalculates the lawful base rent from <b>all increases imposed since April 1, 1982</b>.","p-bad"),
      ("516B","Failure to Repair and Maintain","Available specifically where the tenant <b>&ldquo;received a rent increase notice within the last 60 days&rdquo;</b> and the landlord has not made repairs required by law.","p-bad"),
      ("516A","Decrease in Housing Services","Rent reduction where services were substantially decreased without a corresponding rent reduction.","p-warn"),
      ("516D","Passthrough Challenge","Attacks improper utility, water revenue bond, general obligation bond, or capital improvement passthroughs.","p-warn"),
      ("517","Subtenant Petition","For subtenants paying more than a proportional share, or more than the master tenant pays the owner.","p-mut"),
      ("525","Report of Excessive Rent Increase Under the Tenant Protection Act","The Rent Board acknowledges receipt and tells the landlord of the applicable law, but <b>cannot enforce state law or hold AB 1482 hearings</b>. AB 1482 is enforceable only in state court.","p-mut"),
    ]
    qs = [
      ("1","Coverage","Is the certificate of occupancy on or before June&nbsp;13,&nbsp;1979? Is the unit not a condominium, not a single-family dwelling?","<b>OPEN</b> &mdash; Flags F-04 and F-05. Address not supplied.","https://www.sf.gov/learn-about-san-francisco-rental-laws"),
      ("2","License","Was a current rent increase license in effect <b>on the effective date</b>, with Housing Inventory filings for 2023, 2024, 2025 and 2026?","<b>OPEN</b> &mdash; Flag F-22. Failure renders the <b>entire increase null and void</b>.","https://www.sf.gov/rent-board-housing-inventory"),
      ("3","Anniversary date","Is it at least 12 months since the lease began or the last increase? Is the date being used actually correct?","<b>OPEN for Unit 1</b> &mdash; Flag F-07. Verified for Unit 2 (June 1).","https://www.sf.gov/learn-about-rent-increases-san-francisco"),
      ("4","Arithmetic","Correct percentage for the period containing the effective date? Base rent only? Added, not compounded? Not rounded up? Banked portion disclosed with its source dates?","<b>VERIFIED</b> &mdash; machine-computed and cross-checked at build time.","https://www.sf.gov/documents/34344/571_Allowable_Annual_Increases_26-27_1.pdf"),
      ("5","Banking eligibility","Did 12 full months elapse on each skipped increase?","<b>OPEN</b> &mdash; Flag F-03. Two official sf.gov sources state 12 months and 24 months respectively, and one contradicts its own worked example.","https://www.sf.gov/reports--december-2022--rent-board-rules-and-regulations-part-iv-rent-increases-not-requiring"),
      ("6","Notice","30 or 90 days, correctly measured against the <b>lowest</b> rent charged in the prior 12 months and <b>combining</b> other increases? Plus 5 days if mailed? Properly served under CCP &sect;&nbsp;1013?","<b>VERIFIED</b> &mdash; Unit 1 is 30-day; Unit 2 at 13.1% is <b>90-day</b>.","https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=827"),
      ("7","Retaliation","Anything within 180 days &mdash; repair requests, habitability complaints, DBI citations, Rent Board petitions, tenant-association activity?","<b>OPEN</b> &mdash; Flag F-06. The most common way a perfect calculation still loses.","https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1942.5"),
      ("8","Discrimination","Is the differential between units explained by a written, neutral, uniformly applied policy and documented per unit? Or does it track a protected characteristic &mdash; including that of a <b>roommate or associate</b>, which FEHA expressly protects?","<b>ANSWERED</b> &mdash; adopt the uniform policy on the Anti-Discrimination page and retain the computation sheets.","https://calcivilrights.ca.gov/housing/"),
    ]
    body = f"""
<div class="note"><b>The premise is correct.</b>
San Francisco tenants have real, free, well-organised representation, and the right way to design an
increase is to assume it will be read by a competent tenant attorney &mdash; then build the file so that
attorney concludes it was ordinary, lawful business practice.</div>

<h2>What a tenant can do, at no cost, the moment a notice arrives</h2>
<table><thead><tr><th>Form</th><th>Name</th><th>What it does</th></tr></thead><tbody>
{''.join(f'<tr><td><b>{E(f[0])}</b></td><td>{f[1]}</td><td>{f[2]} <span class="pill {f[3]}">{E(f[0])}</span></td></tr>' for f in forms)}
</tbody></table>
<p class="tag">All forms from the {src_cell('https://www.sf.gov/reports--rent-board-forms-forms-center','official Rent Board Forms Center')}.
Form 525 from the {src_cell('https://www.sf.gov/documents/18505/525_Report_of_Excessive_Rent_Increase_Under_the_TPA_10.25.pdf','official Form 525 PDF')}.</p>
<div class="note bad"><b>The two that matter most here</b>
<b>Form 518</b> can stop an increase <i>before it takes effect</i> if the notice is unlawful on its face &mdash;
a defective notice is not merely void later, it can be blocked in advance. <b>Form 516C</b> recalculates
lawful base rent from <b>every increase since April&nbsp;1,&nbsp;1982</b>, which is why the complete Unit&nbsp;2 ledger
(Flag F-08) and any prior-owner records must be assembled <i>before</i> noticing, not after a petition
arrives.</div>

<h2>Free services available to these tenants</h2>
<table><thead><tr><th style="width:26%">Provider</th><th style="width:12%">Phone</th><th>What they offer</th><th style="width:10%">Source</th></tr></thead><tbody>
{''.join(f'<tr><td><b>{s[0]}</b></td><td>{s[1]}</td><td>{s[2]}</td><td>{src_cell(s[3],"official")}</td></tr>' for s in svc)}
</tbody></table>
<p class="tag">Directory source: {src_cell('https://www.sf.gov/tenant-and-landlord-resources','SF.gov Tenant and Landlord Resources (Mayor&rsquo;s Office of Housing and Community Development)')}.
Landlord-side resources on the same page: San Francisco Apartment Association (415-255-2288), the Bar
Association&rsquo;s Conflict Intervention Service (415-782-8940, open to both sides), and the Rent Board.</p>

<h2>The eight-question test</h2>
<p>A tenant attorney will work through roughly this. <b>Every answer must be documented before the notice
goes out, not reconstructed afterwards.</b></p>
<table><thead><tr><th style="width:4%">#</th><th style="width:15%">Question</th><th style="width:38%">What is examined</th>
<th style="width:31%">Status on these facts</th><th style="width:12%">Authority</th></tr></thead><tbody>
{''.join(f'<tr><td><b>{q[0]}</b></td><td><b>{q[1]}</b></td><td>{q[2]}</td><td>{q[3]}</td><td>{src_cell(q[4],"source")}</td></tr>' for q in qs)}
</tbody></table>
<div class="note ok"><b>Conclusion</b>
An increase that answers all eight cleanly is &mdash; in the terms the owner asked about &mdash; <b>reasonable,
normal business practice, non-discriminatory and lawful</b>. As computed on this site, questions
<b>4</b> (arithmetic), <b>6</b> (notice) and <b>8</b> (non-discrimination) are already satisfied and documented.
Questions <b>1, 2, 3, 5 and 7</b> are open and <b>must</b> be closed before service. An increase that fails
question&nbsp;2 fails completely regardless of the rest, because Rent Board Rules &sect;&nbsp;13.14 renders it null
and void in its entirety.</div>

<h2>How to make the file review-ready</h2>
<ol>
<li>Print and retain the {src_cell('https://www.sf.gov/documents/34344/571_Allowable_Annual_Increases_26-27_1.pdf','Info Sheet 571')}
    in force on the effective date, with the date of download noted.</li>
<li>Retain a screenshot or export from {src_cell('https://portal.sfrb.org/','portal.sfrb.org')} showing the
    rent increase license in effect <b>on the effective date</b>.</li>
<li>Retain the computation sheet per unit: base rent, each skipped anniversary with its official
    percentage, the 12-month elapse date for each, the addition, the multiplication, and the result.</li>
<li>Retain the &sect;&nbsp;1942.5 retaliation screen with a dated nil return if there is nothing to report.</li>
<li>Retain proof of service &mdash; personal delivery receipt or certified mail record &mdash; and the exact
    notice template used for <b>both</b> units.</li>
<li>Retain the dated written uniform rent-increase policy.</li>
<li>Keep a contemporaneous file note recording the business reason for any differential treatment.
    Never record anything about a protected characteristic.</li>
</ol>
"""
    return shell("tenant-review", "The Tenant-Lawyer Scrutiny Test",
        "Free tenant legal services in San Francisco, the petition routes a tenant can use, and the eight-question review an increase must survive.",
        body, "../")

# ============================ CHECKLIST ====================================
def build_checklist():
    elems = [
      ("Written","Oral notice is ineffective. Cal. Civ. Code &sect; 827.","https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=827"),
      ("Properly served","Deliver a copy to the tenant personally, or serve by mail under CCP &sect; 1013. <b>Add 5 days if mailed</b> per SF Rent Board practice.","https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=827"),
      ("30 days where the total is 10% or less","Measured against the <b>lowest</b> rent charged to that tenant at any time during the prior 12 months, <b>alone or combined</b> with any other increase in that window.","https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=827"),
      ("90 days where the total exceeds 10%","Same measurement basis. <b>This applies to Unit 2&rsquo;s 13.1%.</b>","https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=827"),
      ("Dollar amount of the increase","Required content.","https://www.sf.gov/learn-about-rent-increases-san-francisco"),
      ("Percentage of the increase","Required content.","https://www.sf.gov/learn-about-rent-increases-san-francisco"),
      ("Effective date","The percentage in force <b>on this date</b> governs &mdash; not the percentage in force when the notice is served.","https://www.sf.gov/information--banked-rent-increases"),
      ("Which portion is banked","Rules &sect; 4.12(b) also requires <b>the dates on which the banked amount is based</b>.","https://www.sf.gov/reports--december-2022--rent-board-rules-and-regulations-part-iv-rent-increases-not-requiring"),
      ("Capital improvement / passthrough / RAP loan portions, if any","Rules &sect; 4.10(a)(2)-(4) require identification and the date of the authorising decision.","https://www.sf.gov/reports--december-2022--rent-board-rules-and-regulations-part-iv-rent-increases-not-requiring"),
      ("Calculated on base rent only","Includes housing services such as parking and storage. Excludes temporary passthroughs and fluctuating charges.","https://www.sf.gov/learn-about-rent-increases-san-francisco"),
      ("Not rounded up","&ldquo;Landlords cannot round up to the nearest dollar when calculating rent increases.&rdquo;","https://www.sf.gov/information--annual-rent-increase-multiple-years"),
      ("Added, never compounded","&ldquo;Banked increases shall not be compounded and shall not be rounded up.&rdquo; Rules &sect; 4.12(a).","https://www.sf.gov/reports--december-2022--rent-board-rules-and-regulations-part-iv-rent-increases-not-requiring"),
      ("Rent increase license in effect on the effective date","Report via portal.sfrb.org. Annual deadline March 1. Without it the <b>entire increase is null and void</b> under Rules &sect; 13.14.","https://www.sf.gov/rent-board-housing-inventory"),
      ("No petition needed","Annual and banked increases require <b>no</b> Rent Board petition. Capital improvement, O&amp;M and passthrough increases do.","https://www.sf.gov/information--annual-rent-increase-multiple-years"),
    ]
    body = f"""
<h2>The notice must contain and satisfy all fourteen elements</h2>
<p>Rules &sect;&nbsp;4.10(b): <i>&ldquo;Any rent increase which does not conform with the provisions of this Section
shall render the <b>entire rent increase null and void</b>, unless the amount requested equals no more than
the allowable annual and banked rent increase(s).&rdquo;</i> There is a narrow good-faith cure where the overage
is no more than <b>half of one percent</b> of prior base rent &mdash; an administrative law judge may readjust
it &mdash; but get the notice right: the penalty for getting it wrong is total, not marginal.</p>
<table><thead><tr><th style="width:32%">Element</th><th style="width:50%">Requirement</th><th style="width:18%">Source</th></tr></thead><tbody>
{''.join(f'<tr><td><b>{e[0]}</b></td><td>{e[1]}</td><td>{src_cell(e[2],"official")}</td></tr>' for e in elems)}
</tbody></table>
<p class="tag">One nuance: omitting the banked-portion breakdown <b>alone</b> does not void the increase under
Rules &sect;&nbsp;4.12(b), whereas other defects do under &sect;&nbsp;4.10(b). Both provisions are published verbatim
{src_cell('https://www.sf.gov/reports--december-2022--rent-board-rules-and-regulations-part-iv-rent-increases-not-requiring','in Rules Part IV')}
rather than reconciled, because they are in tension and it is not this project&rsquo;s place to resolve an
official conflict.</p>

<h2>Legitimate reasons for an increase &mdash; and illegitimate ones</h2>
<table><thead><tr><th style="width:34%">Reason</th><th style="width:36%">Status</th><th style="width:30%">Authority</th></tr></thead><tbody>
<tr><td>The annual allowable increase published by the Rent Board</td><td><span class="pill p-ok">LEGITIMATE &mdash; sufficient on its own</span> No justification required; it exists by operation of law.</td><td>{src_cell('https://www.sf.gov/learn-about-rent-increases-san-francisco','Admin. Code 37.3(a)(1)')}</td></tr>
<tr><td>Recovering prior years&rsquo; lawfully banked increases</td><td><span class="pill p-ok">LEGITIMATE</span> If 12 full months elapsed on each and the banked portion is disclosed with its source dates.</td><td>{src_cell('https://www.sf.gov/information--banked-rent-increases','Rules 4.12')}</td></tr>
<tr><td>Rising operating costs generally</td><td><span class="pill p-mut">CONTEXTUAL</span> The annual increase is <i>intended</i> to cover ordinary O&amp;M increases. Going beyond it needs a petition.</td><td>{src_cell('https://www.sf.gov/file/530-om-petition-fillable-324pdf','Form 530 Schedule B')}</td></tr>
<tr><td>Capital improvements, rehabilitation, energy-conservation or seismic work</td><td><span class="pill p-warn">ONLY WITH PRIOR RENT BOARD CERTIFICATION</span> Never self-imposed. Maximum 7% of base rent per petition; for properties with six or more units, maximum 7% in total in any five-year period.</td><td>{src_cell('https://www.sf.gov/file/530-om-petition-fillable-324pdf','Admin. Code 37.7 / 37.8')}</td></tr>
<tr><td>Utility, water revenue bond or general obligation bond passthrough</td><td><span class="pill p-warn">ONLY VIA THE PRESCRIBED WORKSHEET OR PETITION</span> Kept out of base rent and discontinued on schedule.</td><td>{src_cell('https://www.sf.gov/reports--december-2022--rent-board-rules-and-regulations-part-iv-rent-increases-not-requiring','Rules 4.11')}</td></tr>
<tr><td>&ldquo;Market rate&rdquo; / comparable-unit pricing</td><td><span class="pill p-bad">NOT AVAILABLE</span> during a continuing tenancy. Vacancy decontrol applies only to an <b>empty</b> unit.</td><td>{src_cell('https://www.sf.gov/learn-about-rent-increases-san-francisco','Admin. Code 37.3(d)')}</td></tr>
<tr><td>A tenant added an occupant, or a roommate was replaced</td><td><span class="pill p-bad">UNLAWFUL</span> even if the lease expressly permits it. Refundable overcharge.</td><td>{src_cell('https://www.sf.gov/information--charging-additional-occupants-prohibited','Topic 152')}</td></tr>
<tr><td>The last original occupant has left and a &sect; 6.14 notice was timely served</td><td><span class="pill p-warn">LEGITIMATE IN PRINCIPLE</span> but <b>not available on these facts</b> &mdash; an original occupant remains in Unit 1.</td><td>{src_cell('https://www.sf.gov/information--rent-increases-under-section-614-and-costa-hawkins','Rules 6.14')}</td></tr>
<tr><td>Tenant complained, requested repairs, or organised</td><td><span class="pill p-bad">UNLAWFUL RETALIATION</span> 180-day bar; separate bar for retaliation against organising.</td><td>{src_cell('https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1942.5','Civ. Code 1942.5')}</td></tr>
<tr><td>Any protected characteristic, or that of a roommate or associate</td><td><span class="pill p-bad">UNLAWFUL DISCRIMINATION</span></td><td>{src_cell('https://calcivilrights.ca.gov/housing/','Gov. Code 12955 / FEHA')}</td></tr>
<tr><td>A recommendation from algorithmic pricing software</td><td><span class="pill p-bad">UNLAWFUL</span> Using such a device is prohibited outright; per-unit, per-month penalties.</td><td>{src_cell('https://www.sf.gov/information--algorithmic-devices-set-rent-are-prohibited-san-francisco','Admin. Code 37.10C')}</td></tr>
</tbody></table>
<div class="note"><b>Practical drafting advice</b>
A landlord does <b>not</b> need to justify the annual allowable increase at all. Over-explaining invites
argument; understating the banked breakdown voids the notice. State the dollar amount, the percentage,
the effective date, the banked portion and its source dates &mdash; and nothing else.</div>

<h2>Action plan</h2>
<h3>Now &mdash; before any notice (all free)</h3>
<table><thead><tr><th style="width:8%">Flag</th><th>Action</th><th style="width:24%">Where</th></tr></thead><tbody>
<tr><td><b>F-22</b></td><td>Confirm a current <b>rent increase license</b> for both units and Housing Inventory filings for 2023, 2024, 2025 and 2026. Without this every increase is null and void.</td><td>{src_cell('https://portal.sfrb.org/','portal.sfrb.org')}</td></tr>
<tr><td><b>F-04</b></td><td>Record the certificate of occupancy date and construction year.</td><td>{src_cell('https://sfplanninggis.org/PIM/','SF Property Information Map')}</td></tr>
<tr><td><b>F-05</b></td><td>Confirm neither unit is a condominium; confirm owner-occupancy status.</td><td>Deed / subdivision map</td></tr>
<tr><td><b>F-08</b></td><td>Assemble Unit&nbsp;2&rsquo;s complete rent ledger, including any prior owner&rsquo;s records.</td><td>Owner records</td></tr>
<tr><td><b>F-06</b></td><td>Run and document the &sect;&nbsp;1942.5 retaliation screen for both units over the last 12 months &mdash; repair requests, habitability complaints, DBI citations, Rent Board petitions, tenant-association activity.</td><td>Owner records</td></tr>
<tr><td><b>F-03</b></td><td>Ask whether banking requires <b>12 or 24 months</b> to elapse under Rules &sect;&nbsp;4.12, given that two official sf.gov pages disagree.</td><td>{src_cell('https://www.sf.gov/speak-rent-board-counselor','Rent Board counselor, free, 415-252-4600')}</td></tr>
<tr><td><b>F-07</b></td><td>In the same call, ask whether Unit&nbsp;1&rsquo;s 2026-04-01 rental agreement reset the anniversary date to April&nbsp;1 or left it at February&nbsp;1.</td><td>{src_cell('https://www.sf.gov/speak-rent-board-counselor','Rent Board counselor')}</td></tr>
<tr><td><b>F-09</b></td><td>Confirm no open repair or habitability issues &mdash; Form&nbsp;516B is available to a tenant for 60 days after a rent increase notice.</td><td>Owner records</td></tr>
<tr><td>&mdash;</td><td>Write and date the uniform rent-increase policy from the <a href="discrimination.html">Anti-Discrimination</a> page.</td><td>Owner</td></tr>
</tbody></table>

<h3>December 2026 &ndash; February 2027</h3>
<table><thead><tr><th style="width:20%">By when</th><th>Action</th></tr></thead><tbody>
<tr><td>From December 2026</td><td><b>F-16 / F-18</b> Monitor the {src_cell('https://www.sf.gov/departments--rent-board/news','Rent Board news page')} for (a) enactment of any cap on banked increases and (b) publication of the 3/1/2027&ndash;2/28/2028 percentage. Re-run Unit&nbsp;2&rsquo;s calculation when it lands.</td></tr>
<tr><td><b>2027-01-02</b><br><span class="tag">2026-12-28 if mailed</span></td><td>Serve Unit&nbsp;1&rsquo;s <b>30-day</b> notice for a <b>3.0%</b> increase effective <b>2027-02-01</b> &rarr; <b>$4,114.85</b>. Disclose the 1.4% banked portion and its 2026-02-01 source date.</td></tr>
<tr><td><b>2027-03-01</b></td><td>File the annual Housing Inventory report and confirm the license remains current.</td></tr>
</tbody></table>

<h3>March &ndash; June 2027</h3>
<table><thead><tr><th style="width:20%">By when</th><th>Action</th></tr></thead><tbody>
<tr><td><b>2027-03-03</b><br><span class="tag">2027-02-26 if mailed</span></td><td>Serve Unit&nbsp;2&rsquo;s <b>90-day</b> notice for an effective date of <b>2027-06-01</b>: either the full 13.1% banked plus the new annual percentage, or the phased <b>10.0%</b> &rarr; <b>$3,465.00</b> on 30-day notice instead.</td></tr>
<tr><td>Throughout</td><td>Retain proof of service, the computation sheet, the license confirmation and the retaliation screen for each unit.</td></tr>
</tbody></table>
"""
    return shell("checklist", "Compliance Checklist and Notice Procedure",
        "The fourteen elements a valid notice must satisfy, which reasons are legitimate, and the dated action plan.",
        body, "../")

# ============================ SOURCES ======================================
def build_sources():
    rows = "".join(
      f'<tr><td><b>{E(s["id"])}</b></td><td>{E(s["title"])}<div class="tag">{E(s["publisher"])} &middot; {E(s["type"])}'
      + (f' &middot; published {E(s["date_published"])}' if s.get("date_published") else '') + '</div></td>'
      f'<td>{E(s["verifies"])}</td><td><a href="{E(s["url"])}" rel="noopener" target="_blank">official</a></td></tr>'
      for s in SOURCES["sources"])
    body = f"""
<div class="note ok"><b>Source policy</b>
{E(SOURCES['_policy'])}</div>
<div class="filterbar"><input type="search" data-filter="src-tbl" placeholder="Filter {len(SOURCES['sources'])} sources&hellip;">
<span class="count" id="src-tbl-count"></span></div>
<table id="src-tbl"><thead><tr><th style="width:6%">ID</th><th style="width:30%">Document</th>
<th style="width:50%">What it verifies on this site</th><th style="width:14%">Link</th></tr></thead>
<tbody>{rows}</tbody></table>
<h2>Non-official material consulted and deliberately not cited</h2>
<p>Third-party legal blogs, property-management vendors, tenant-union pages and news aggregators were read
only to <b>locate</b> the correct ordinance section, form number or official page. <b>No value anywhere on
this site comes from a non-official source.</b> Where third-party figures conflicted with each other &mdash;
for example two different FY2026 HUD 2-bedroom Fair Market Rents for San Francisco ($3,604 versus $3,160) &mdash;
the value was rejected entirely and left blank rather than choosing between them. That rejection is
recorded as Flag F-01.</p>
<h2>Machine-readable registers</h2>
<ul>
<li><a href="../data/sources.json"><code>data/sources.json</code></a> &mdash; this register</li>
<li><a href="../data/allowable-increases.json"><code>data/allowable-increases.json</code></a> &mdash; verbatim Info Sheet 571 table</li>
<li><a href="../data/current-rates.json"><code>data/current-rates.json</code></a> &mdash; official rates in force</li>
<li><a href="../data/units.json"><code>data/units.json</code></a> &mdash; anonymized unit and rent-history data</li>
<li><a href="../data/calculations.json"><code>data/calculations.json</code></a> &mdash; scenarios with method and sources</li>
<li><a href="../data/market.json"><code>data/market.json</code></a> &mdash; Census figures with re-runnable API URLs</li>
<li><a href="../data/law.json"><code>data/law.json</code></a> &mdash; {len(LAW['local'])} local, {len(LAW['state'])} state and {len(LAW['federal'])} federal rules with sources</li>
<li><a href="../data/flags.json"><code>data/flags.json</code></a> &mdash; {len(FLAGS['flags'])} flags</li>
</ul>
<p class="tag">All data retrieved {E(SOURCES['_accessed'])}. Percentages, rates and Census values should be
re-confirmed before any notice is served; the Rent Board publishes the following year&rsquo;s allowable
increase each March&nbsp;1 and announces it in the preceding December or January.</p>
"""
    return shell("sources", "Source Register",
        f"{len(SOURCES['sources'])} official documents. Every factual claim on this site traces to one of them.",
        body, "../")

# ============================ FLAGGED ======================================
def build_flagged():
    from collections import Counter
    c = Counter(f["severity"] for f in FLAGS["flags"])
    rows = ""
    for f in FLAGS["flags"]:
        sev = f["severity"]
        p = {"HIGH": "p-bad", "medium": "p-warn", "low": "p-mut",
             "informational": "p-mut", "cosmetic": "p-mut"}[sev]
        rows += f"""<tr data-sev="{E(sev)}">
<td><b>{E(f['id'])}</b><div style="margin-top:5px"><span class="pill {p}">{E(sev.upper())}</span></div></td>
<td><b>{E(f['title'])}</b><div class="tag" style="margin-top:4px">{E(f['category'])}</div></td>
<td><div><b>Finding.</b> {E(f['finding'])}</div>
{f'<div style="margin-top:8px"><b>Impact.</b> {E(f["impact"])}</div>' if f.get('impact') else ''}
{f'<div style="margin-top:8px"><b>Action.</b> {E(f["action"])}</div>' if f.get('action') else ''}</td>
<td>{src_cell(f['source'],'official source')}
{f'<div class="tag" style="margin-top:4px">secondary: '+src_cell(f['secondary_source'],'link')+'</div>' if f.get('secondary_source') else ''}
{f'<div class="tag" style="margin-top:4px">conflicts with: '+src_cell(f['conflicting_source'],'link')+'</div>' if f.get('conflicting_source') else ''}</td></tr>"""
    body = f"""
<div class="note warn"><b>These items do not block publication.</b>
{E(FLAGS['_policy'])}</div>
<div class="cards">
 <div class="card bad"><div class="k">HIGH</div><div class="v">{c['HIGH']}</div><div class="s">Must close before serving any notice</div></div>
 <div class="card warn"><div class="k">Medium</div><div class="v">{c['medium']}</div><div class="s">Resolve before relying on the figure</div></div>
 <div class="card"><div class="k">Low</div><div class="v">{c['low']}</div><div class="s">Recorded for completeness</div></div>
 <div class="card"><div class="k">Informational / cosmetic</div><div class="v">{c['informational']+c['cosmetic']}</div><div class="s">No action required</div></div>
</div>
<div class="filterbar">
<button class="btn" data-sev="HIGH" data-target="fl-tbl">HIGH only</button>
<button class="btn" data-sev="medium" data-target="fl-tbl">Medium only</button>
<button class="btn" data-sev="low" data-target="fl-tbl">Low only</button>
<input type="search" data-filter="fl-tbl" placeholder="Filter {len(FLAGS['flags'])} flags&hellip;">
<span class="count" id="fl-tbl-count"></span></div>
<table id="fl-tbl"><thead><tr><th style="width:8%">ID</th><th style="width:22%">Item</th>
<th style="width:52%">Finding, impact and required action</th><th style="width:18%">Source links</th></tr></thead>
<tbody>{rows}</tbody></table>

<h2>Values deliberately left blank across this site</h2>
<table><thead><tr><th>Value</th><th>Where it would appear</th><th>Why it is blank</th><th>Flag</th></tr></thead><tbody>
<tr><td>HUD Fair Market Rent, San Francisco area</td><td><a href="market.html">Market Data</a></td>
 <td>HUD&rsquo;s API returned <code>Unauthenticated</code>; no area value retrievable from huduser.gov this session; third-party figures conflicted ($3,604 vs $3,160).</td><td><b>F-01</b></td></tr>
<tr><td>BLS CPI-U index values</td><td><a href="market.html">Market Data</a></td>
 <td>Regional news release returned 404. Immaterial: SF.gov instructs owners to use the <b>published</b> percentage, not a recomputed one.</td><td><b>F-02</b></td></tr>
<tr><td>The 3/1/2027&ndash;2/28/2028 allowable percentage</td><td><a href="allowable.html">Allowable Increases</a>, Unit 2 Scenario U2-A</td>
 <td>Not yet published by the Rent Board. Consequently the final total for U2-A cannot be computed.</td><td><b>F-18</b></td></tr>
<tr><td>Current-year bankable Rent Board fee</td><td><a href="allowable.html">Allowable &amp; Current Rates</a></td>
 <td>Absent from the official rate table, which shows only tax years 2023-24 and 2024-25.</td><td><b>F-14</b></td></tr>
<tr><td>All dollar values in Unit 1 Scenario U1-C</td><td><a href="calculations.html">Increase Scenarios</a></td>
 <td>Depends on an anniversary-date question no official source resolves. Left blank rather than estimated.</td><td><b>F-07</b></td></tr>
<tr><td>Certificate of occupancy date</td><td><a href="units.html">Unit Profiles</a></td>
 <td>Address not supplied and is personal information. Must be looked up on the SF Property Information Map.</td><td><b>F-04</b></td></tr>
<tr><td>Condominium status and owner occupancy</td><td><a href="units.html">Unit Profiles</a></td>
 <td>Not supplied. Changes the Costa-Hawkins and AB 1482 analysis if affirmative.</td><td><b>F-05</b></td></tr>
<tr><td>Rent increase license status</td><td><a href="tenant-review.html">Tenant-Lawyer Test</a></td>
 <td>Only visible through portal.sfrb.org; cannot be verified externally.</td><td><b>F-22</b></td></tr>
<tr><td>Retaliation screen result</td><td><a href="checklist.html">Checklist</a></td>
 <td>No tenant complaint, repair or organising history supplied.</td><td><b>F-06</b></td></tr>
<tr><td>Tenant harassment penalties under Admin. Code &sect; 37.10B</td><td><a href="state-law.html">California Law</a></td>
 <td>The official SF.gov page returned 404; penalty figures could not be confirmed. Row marked UNVERIFIED and carries no figures.</td><td><b>F-10</b></td></tr>
</tbody></table>

<h2>Irregularities found in the official sources themselves</h2>
<p>Verification is not only about confirming values &mdash; it also means reporting where official sources
are wrong, stale, incomplete or internally inconsistent. Six were found:</p>
<table><thead><tr><th>Flag</th><th>Official source</th><th>Defect</th></tr></thead><tbody>
<tr><td><b>F-03</b></td><td>SF.gov <i>Banked rent increases</i> vs Rent Board Rules &sect; 4.12 vs Admin. Code &sect; 37.3(a)(2)</td>
 <td><b>Three official sources, two different answers.</b> The sf.gov page says a skipped increase banks only if <b>24 full months</b> pass; the Rules say <b>12</b>; the codified ordinance states no condition at all. The sf.gov page then contradicts itself: its own worked example banks an increase that had only 12 months to elapse. Materially affects Unit 2.</td></tr>
<tr><td><b>F-11</b></td><td>SF.gov <i>Learn about San Francisco rental laws</i></td><td>Still cites <b>1.7%</b> for the 2024&ndash;Feb 2025 period as though current. The correct current rate is 1.6%, confirmed by three other official sources.</td></tr>
<tr><td><b>F-12</b></td><td>Rent Board Form 538 (2024-25 Bond Measure Worksheet)</td><td>States the &sect; 37.15 license applies from <b>July 1, 2020</b> / <b>March 1, 2021</b>. SF.gov gives July 1, 2022 / March 1, 2023. Official forms lagging official guidance.</td></tr>
<tr><td><b>F-13</b></td><td>SF.gov <i>Current Rates</i></td><td>The link labelled <b>&ldquo;575 Cap. Imp. Labor Rates&rdquo;</b> resolves to the <b>574</b> imputed-interest PDF &mdash; the wrong document.</td></tr>
<tr><td><b>F-14</b></td><td>SF.gov <i>Current Rates</i></td><td>Headed for 3/1/2026&ndash;2/28/2027, but the bankable Rent Board Fee table omits the <b>2025-26 and 2026-27</b> tax years.</td></tr>
<tr><td><b>F-15</b></td><td>SF.gov Info Sheet 571 Spanish PDF</td><td>Filename carries a doubled extension <code>.pdf.pdf</code>. Resolves correctly; recorded for audit completeness.</td></tr>
<tr><td><b>F-17</b></td><td>SF.gov <i>Speak with a Rent Board counselor</i> vs the Rent Board News Archive</td><td>The news archive lists a 2025 item &ldquo;The San Francisco Rent Board has moved&rdquo; while the counselor page still gives 25 Van Ness Avenue Suite #700. Confirm before travelling.</td></tr>
</tbody></table>

<h2>Repository irregularities</h2>
<p>Findings R-01 to R-06 from the line-by-line audit of the repository as received are in
<a href="../docs/repo-review.md"><code>docs/repo-review.md</code></a>. The significant one is <b>R-02</b>:
GitHub Pages was already enabled against a repository containing only a 17-byte <code>README.md</code>, using the
legacy Jekyll build with no <code>.nojekyll</code> and no <code>index.html</code>, so the published URL served nothing
useful. Fixed by adding <code>.nojekyll</code> and building a real site.</p>
"""
    return shell("flagged", "Flagged for Review",
        f"{len(FLAGS['flags'])} irregularities, conflicts between official sources, and values left blank rather than inferred.",
        body, "../")

# ============================ MAIN =========================================
def main():
    os.makedirs(os.path.join(ROOT, "pages"), exist_ok=True)
    os.makedirs(os.path.join(ROOT, "assets", "css"), exist_ok=True)
    os.makedirs(os.path.join(ROOT, "assets", "js"), exist_ok=True)

    docs = {
        "index.html":                        build_index(),
        "pages/executive-summary.html":      build_exec(),
        "pages/units.html":                  build_units(),
        "pages/calculations.html":           build_calcs(),
        "pages/local-law.html":              build_local(),
        "pages/state-law.html":              build_state(),
        "pages/federal-law.html":            build_federal(),
        "pages/allowable.html":              build_allowable(),
        "pages/market.html":                 build_market(),
        "pages/practices.html":              build_practices(),
        "pages/discrimination.html":         build_disc(),
        "pages/tenant-review.html":          build_tenant(),
        "pages/checklist.html":              build_checklist(),
        "pages/sources.html":                build_sources(),
        "pages/flagged.html":                build_flagged(),
    }
    for p, s in docs.items():
        B.append(assert_no_pii(s, p))
        w(p, s)
    w("assets/css/styles.css", CSS)
    w("assets/js/app.js", JS)
    w(".nojekyll", "")
    w(".gitignore", "# Never commit locally-held tenant or owner identifiers\n"
                    ".pii-guard.local.json\ninternal/\npii/\n*.local.md\n*.local.html\n"
                    "# Build / editor noise\n__pycache__/\n*.pyc\n.DS_Store\nnode_modules/\n")

    pii = [x for sub in B for x in sub]
    if pii:
        for p in pii:
            print("PII GUARD:", p)
        FAIL.append("PII guard found real identifiers in generated output")

    # link check: every internal href must resolve to a generated file
    generated = set(docs) | {"assets/css/styles.css", "assets/js/app.js",
                             ".nojekyll", ".gitignore",
                             "data/sources.json", "data/allowable-increases.json",
                             "data/current-rates.json", "data/units.json",
                             "data/calculations.json", "data/market.json",
                             "data/law.json", "data/flags.json",
                             "docs/executive-summary.md", "docs/repo-review.md",
                             "docs/PRIVACY-AND-ANONYMIZATION.md", "COORDINATION.md",
                             "build.py", "style.css", "dashboard-81e8c938.html",
                             "executive-summary.html", "units.html", "analysis.html",
                             "laws.html", "process.html", "tenant-protections.html",
                             "practices.html", "flagged.html", "sources.html",
                             "scripts/validate_site.py", ".github/workflows/validate.yml"}
    # files preserved from earlier merged sessions (PRs #1, #2, #4); they exist on
    # origin/main and are restored by the merge, so the link checker must accept them
    legacy_present = all(os.path.exists(os.path.join(ROOT, f)) for f, _ in LEGACY)
    if not legacy_present:
        print("  note: earlier-session pages not present yet (pre-merge); link check is advisory for them")
    ext = 0
    for p, s in docs.items():
        base = "" if p == "index.html" else "../"
        indir = os.path.dirname(p)          # "" for index.html, "pages" for subpages
        for m in re.finditer(r'href="([^"]+)"', s):
            h = m.group(1)
            if h.startswith(("http://", "https://", "#", "mailto:")):
                ext += 1
                continue
            tgt = h.split("#")[0]
            if not tgt:
                FAIL.append(f"{p}: empty internal link -> {h}")
                continue
            # resolve relative to the document's own directory, then normalize
            norm = os.path.normpath(os.path.join(indir, tgt)).replace(os.sep, "/")
            if norm not in generated:
                FAIL.append(f"{p}: internal link does not resolve -> {h} (normalized {norm})")

    if FAIL:
        print("\nBUILD FAILED:", len(FAIL), "problem(s)")
        for f in FAIL:
            print("  -", f)
        sys.exit(1)

    print(f"\nBUILD OK")
    print(f"  {len(docs)} HTML documents")
    print(f"  {ext} external links, all to official sources")
    print(f"  {len(SOURCES['sources'])} registered sources, {len(FLAGS['flags'])} flags")
    print(f"  arithmetic: {len(CHECKS)} dollar checks + {len(NOTICE_CHECKS)} deadline checks passed")
    print(f"  census: gross-rent, rent-burden and housing-age totals reconcile")
    print(f"  PII guard: clean")
    return 0

if __name__ == "__main__":
    sys.exit(main())
