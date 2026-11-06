#!/usr/bin/env python3
"""Build the Rental Increase SF static site into the repo root.

Usage:  python3 tools/build.py

Reads nothing outside this directory; writes only top-level .html files and
data/*.csv. Safe to re-run.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from _template import head, foot, page_head, src, badge, NAV  # noqa: E402
import _data as D  # noqa: E402
import _rows as R  # noqa: E402

S = D.SOURCES
TODAY = "6 November 2026"


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------
def money(v):
    return "${:,.2f}".format(v)


def write(name, html):
    path = os.path.join(ROOT, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    return path


def s(key):
    """Source cell."""
    if not key:
        return '<span class="badge muted">no source</span>'
    return src(S[key])


def table(headers, rows, cls="data", thead_num=()):
    h = "".join(
        '<th class="num">{}</th>'.format(x) if i in thead_num else "<th>{}</th>".format(x)
        for i, x in enumerate(headers)
    )
    body = "\n".join(rows)
    return (
        '<div class="table-scroll"><table class="{}">'
        "<thead><tr>{}</tr></thead><tbody>\n{}\n</tbody></table></div>".format(cls, h, body)
    )


def status_badge(txt):
    t = txt.lower()
    if "unverified" in t or "unknown" in t:
        k = "risk"
    elif "flag" in t or "must fix" in t or "blocking" in t:
        k = "risk"
    elif "owner-supplied" in t or "anonymis" in t:
        k = "muted"
    elif "pass" in t and "unverified" not in t:
        k = "ok"
    elif "likely" in t or "probable" in t or "subject" in t or "context" in t:
        k = "warn"
    else:
        k = "info"
    return badge(txt, k)


# ===========================================================================
# 1. INDEX / DASHBOARD
# ===========================================================================
def build_index():
    tiles = [
        ("summary.html", "01", "Executive summary",
         "The answer in one page: what each unit may lawfully be charged, and the three decisions "
         "still open.", "9 findings · 3 open decisions"),
        ("units.html", "02", "The two units",
         "Anonymised tenancy facts, side by side, with the legal test each fact drives.",
         "10 fact rows · 0 personal identifiers"),
        ("calculations.html", "03", "Calculations",
         "Every lawful figure, computed from the published AGA table, with the arithmetic shown.",
         "5 scenarios · exact to the cent"),
        ("laws.html", "04", "Local, state & federal law",
         "The three layers that apply, with the controlling provision for each.",
         "41 provisions · 3 jurisdictions"),
        ("aga-history.html", "05", "Allowable increase history",
         "The full Rent Board table, April 1982 to date, transcribed from Form 571.",
         "46 periods · primary source"),
        ("practices.html", "06", "How increases are handled",
         "Institutional vs individual practice — only where an official source actually says so.",
         "8 practices · 3 research gaps"),
        ("notices.html", "07", "Notices & deadlines",
         "The exact notice content, service rules, and calendar for both units.",
         "30 / 90-day matrix · template"),
        ("fair-housing.html", "08", "One unit or both?",
         "The discrimination question, answered from Unruh, FEHA and the Fair Housing Act.",
         "The decisive question"),
        ("reasons.html", "09", "Reasonable reasons",
         "What may be said, what may not, and the statutory wording to use instead.",
         "6 usable · 6 avoid"),
        ("review.html", "10", "Tenant-lawyer review",
         "A 12-point adversarial test run against this file, with verdicts.",
         "12 checks · 2 blocking"),
        ("sources.html", "11", "Source register",
         "Every source used, by publisher, with the link and what it was used to prove.",
         "36 primary sources"),
        ("flagged.html", "12", "Flagged for review",
         "Everything unconfirmed, contradictory or missing, with the action to close it.",
         "9 items · 2 high severity"),
    ]
    t = "\n".join(
        '<a class="tile" href="{h}"><span class="arrow" aria-hidden="true">→</span>'
        '<span class="tnum">{n}</span>'
        '<span class="ttitle">{t}</span>'
        '<span class="tdesc">{d}</span>'
        '<span class="tmeta">{m}</span></a>'.format(h=h, n=n, t=title, d=desc, m=meta)
        for h, n, title, desc, meta in tiles
    )

    body = page_head(
        "Rental increase analysis — Outer Sunset, San Francisco",
        "Two rent-controlled flats in a building constructed in 1940, ZIP 94122. What each may "
        "lawfully be charged, what the law requires before a notice is served, and what a San "
        "Francisco tenant lawyer would attack. Every figure is traced to the agency that publishes it.",
        crumb='<a href="index.html">Dashboard</a>',
    )

    body += f"""
    <div class="grid cols-4" style="margin-bottom:18px">
      <div class="kpi brand">
        <span class="label">Allowable increase</span>
        <span class="value">1.6%</span>
        <span class="sub">Effective 1 Mar 2026 – 28 Feb 2027</span>
        <span class="src">{s("571")}</span>
      </div>
      <div class="kpi ok">
        <span class="label">Unit 1 — maximum lawful</span>
        <span class="value">$4,114.85</span>
        <span class="sub">3.0% — 1.4% banked + 1.6% annual</span>
        <span class="src">{s("rr4")}</span>
      </div>
      <div class="kpi ok">
        <span class="label">Unit 2 — maximum lawful</span>
        <span class="value">$3,562.65</span>
        <span class="sub">13.1% — 11.5% banked + 1.6% annual</span>
        <span class="src">{s("rr4")}</span>
      </div>
      <div class="kpi risk">
        <span class="label">Open blockers</span>
        <span class="value">2</span>
        <span class="sub">Rent increase licence · notice itemisation</span>
        <span class="src"><a href="flagged.html">Flagged for review</a></span>
      </div>
    </div>

    <div class="card">
      <h2 style="margin-bottom:8px">The answer, before the detail</h2>
      <p>Both flats are almost certainly covered by the San Francisco Rent Ordinance — the building is
      from 1940, well before the 13 June 1979 cutoff. That means the annual increase is capped by the
      Rent Board's published figure, not by market rent. For the current period that figure is
      <strong>1.6%</strong>. AB 1482's higher state cap of 8.8% is switched off precisely because the
      local cap is lower {s("civ1947_12")}. No federal statute sets a rent ceiling at all.</p>

      <p>Neither unit is eligible for the vacancy reset. Section&nbsp;6.14 and Costa-Hawkins only
      unlock an unlimited increase when the <em>last original occupant</em> has left. An original
      occupant remains in both units, so the annual cap continues to run in both.</p>

      <p>The lawful maximums are therefore narrow and mechanical: Unit&nbsp;1 may go to
      <strong>$4,114.85</strong> (3.0% = one banked year plus this year's 1.6%), and Unit&nbsp;2 to
      <strong>$3,562.65</strong> (13.1% = six banked years plus this year's 1.6%). Unit&nbsp;2's
      figure is large only because six years of small increases were never taken — the percentages are
      added, never compounded, exactly as Rule&nbsp;4.12 requires.</p>

      <p>Two things are not yet safe. There is no confirmed current <strong>rent increase
      licence</strong> for either unit, and without one a notice is unenforceable no matter how correct
      the arithmetic. And Unit&nbsp;1's <strong>anniversary date</strong> is genuinely ambiguous: if the
      April&nbsp;2026 paperwork created a new tenancy, no increase can take effect before
      April&nbsp;2027. Both are on the <a class="inline" href="flagged.html">Flagged for Review</a>
      page with the action needed to close them.</p>
    </div>

    <h2 style="margin:26px 0 12px">Browse</h2>
    <div class="tile-grid">
      {t}
    </div>

    <div class="card" style="margin-top:22px">
      <h2>How this site was built — and its limits</h2>
      <div class="grid cols-2">
        <div>
          <h3 style="margin-top:0">What was done</h3>
          <ul class="small">
            <li>Every statutory figure was read from the government page that publishes it, not from
            a law firm blog or a property manager's calculator.</li>
            <li>All arithmetic is generated by script from the published table — no number on this
            site was typed by hand.</li>
            <li>Where two official pages appear to differ, both are shown and the reconciliation is
            written out on the <a class="inline" href="verification.html">Verification log</a>.</li>
            <li>Where no official source exists, the value is left blank and flagged. HUD's Fair
            Market Rents are one example.</li>
          </ul>
        </div>
        <div>
          <h3 style="margin-top:0">What this is not</h3>
          <ul class="small">
            <li>It is not legal advice and cannot replace a Rent Board counselor's view on a specific
            tenancy.</li>
            <li>It is not an audit of the owner's records. Rent histories, licence status and
            occupancy are as supplied, not as verified.</li>
            <li>It does not predict outcomes. It states what the published rules require and where a
            file is currently exposed.</li>
            <li>It is current to {TODAY}. The allowable rate changes each 1&nbsp;March.</li>
          </ul>
        </div>
      </div>
    </div>
    </div>
"""
    return write("index.html", head(
        "Dashboard",
        "Rent increase analysis for two rent-controlled San Francisco flats in ZIP 94122, with every "
        "figure traced to an official source.",
        "index.html") + body + foot())


# ===========================================================================
# 2. EXECUTIVE SUMMARY
# ===========================================================================
def build_summary():
    body = page_head(
        "Executive summary",
        "What the law permits, what it forbids, and the three decisions that remain open.",
        crumb='<a href="index.html">Dashboard</a> / Executive summary',
    )

    body += f"""
    <div class="card">
      <h2>1. The controlling facts</h2>
      <p>Two units in one building, constructed in 1940, in the Outer Sunset (ZIP 94122). A building
      from 1940 is inside the Rent Ordinance's rent-control cutoff of 13 June 1979
      {s("rentlaws")}. Both units are therefore on the <em>local</em> rent ceiling, which is far lower
      than the state ceiling and which displaces it.</p>
      <table class="plain">
        <tr><th>Unit</th><td>Unit&nbsp;1 — last lease 1 Feb 2025 at $3,995.00; continuing tenancy from
          1 Apr 2026 at the same $3,995.00; original tenant L&nbsp;O remains.</td></tr>
        <tr><th>Unit</th><td>Unit&nbsp;2 — last lease 1 Jun 2019 at $3,150.00; both original tenants
          E&nbsp;R and I&nbsp;S remain.</td></tr>
        <tr><th>Personal data</th><td>Initials only. No names, addresses, contact details or
          identifying combinations are published. Dates and dollar amounts are unchanged.</td></tr>
      </table>
    </div>

    <div class="card">
      <h2>2. The three layers of law, in one line each</h2>
      <table class="plain">
        <tr><th>Local</th><td><strong>1.6%</strong> for increases effective 1 Mar 2026 – 28 Feb 2027,
          once every 12 months, on base rent only, plus properly banked prior years. Non-conforming
          increases are <em>null and void</em> {s("571")}{s("373")}</td></tr>
        <tr><th>State</th><td>AB 1482 would allow 8.8% for San Francisco, but it is expressly
          <em>switched off</em> where a local ordinance caps increases lower — as San Francisco's does
          {s("civ1947_12")}. Civil Code § 827 sets the notice periods: 30 days at 10% or less,
          90 days above 10% {s("civ827")}</td></tr>
        <tr><th>Federal</th><td>No rent ceiling exists in federal law. The Fair Housing Act
          regulates <em>how</em> rent is set, not <em>how much</em>: differential treatment on the
          basis of race, colour, religion, sex, familial status, national origin or disability is
          unlawful {s("fha3604")}</td></tr>
      </table>
    </div>

    <div class="card">
      <h2>3. What each unit may lawfully be charged</h2>
      <table class="plain">
        <tr><th>Unit 1 — maximum</th><td><strong>$4,114.85</strong> / month, an increase of
          <strong>$119.85</strong> (3.0%). That is 1.4% banked from the 2025-26 period plus the 1.6%
          annual increase, taken on the 1&nbsp;February anniversary. Anything above this without a
          Rent Board petition is void {s("rr4")}</td></tr>
        <tr><th>Unit 2 — maximum</th><td><strong>$3,562.65</strong> / month, an increase of
          <strong>$412.65</strong> (13.1%). That is 11.5% banked across six skipped years plus the
          1.6% annual increase. Requires <strong>90 days'</strong> written notice because it exceeds
          10% {s("rr4")}{s("civ827")}</td></tr>
        <tr><th>Do not</th><td>Do not take a market-rate reset on either unit, do not charge more
          because Unit&nbsp;1 gained an occupant, and do not use revenue-management software to pick
          a number — each is independently unlawful {s("614")}{s("occupants")}{s("algo")}</td></tr>
      </table>
    </div>

    <div class="card">
      <h2>4. The nine findings</h2>
      <ol class="steps">
        <li><span class="st">The local cap governs, and it is 1.6%.</span>
          AB 1482's 8.8% is not available to either unit. Any analysis that starts from 8.8% is wrong
          for this property {s("civ1947_12")}</li>
        <li><span class="st">Neither unit can be reset to market rent.</span>
          Section 6.14 and Costa-Hawkins both require the <em>last</em> original occupant to have
          left. L&nbsp;O remains in Unit&nbsp;1; E&nbsp;R and I&nbsp;S remain in Unit&nbsp;2
          {s("614")}{s("civ1954_53")}</li>
        <li><span class="st">Unit 1 gained an occupant — that is a trap, not an opportunity.</span>
          Raising rent because M&nbsp;T joined would be an unlawful increase even if the lease
          permits it {s("occupants")}</li>
        <li><span class="st">Unit 2's 13.1% is lawful and smaller than it looks.</span>
          Six skipped years add to 11.5%. On a $3,150 base that is $412.65. Taken year by year with
          compounding it would have been $435.72 — the no-compounding rule cuts in the tenant's
          favour, not against them {s("rr4")}</li>
        <li><span class="st">Both increases must be itemised.</span>
          The notice must state which portion is annual, which is banked, and the dates the banked
          amount rests on. A non-conforming notice voids the whole increase {s("373")}</li>
        <li><span class="st">The licence is the gating item.</span>
          Without a current rent increase licence on the effective date, the notice is unenforceable
          regardless of the arithmetic {s("inventory")}</li>
        <li><span class="st">Raising both units is not required, but a written policy is.</span>
          Nothing in Unruh, FEHA or the FHA requires an owner to raise every tenancy by the same
          amount. What the law forbids is a difference that tracks a protected characteristic. Both
          units here take the <em>same</em> 1.6% annual increase; the difference is each tenancy's own
          banked history {s("gov12955")}</li>
        <li><span class="st">No justification is needed — and inventing one is risky.</span>
          An annual allowable increase needs no reason beyond the statute. Citing "market rent" invites
          a comparable-rent fight in which the Rent Board has already said a long-standing low rent is
          not an extraordinary circumstance {s("comps")}</li>
        <li><span class="st">Two files are exposed.</span>
          The licence, and Unit&nbsp;1's anniversary date. Both are fixable before any notice is
          served {s("inventory")}{s("civ1954_53")}</li>
      </ol>
    </div>

    <div class="card">
      <h2>5. The three open decisions</h2>
      <table class="plain">
        <tr><th>Decision 1 — what date?</th><td>Unit&nbsp;1 needs 1&nbsp;February 2027 to preserve the
          banked 1.4%. Unit&nbsp;2 needs a 90-day runway, so a mid-February 2027 effective date means
          serving by 17&nbsp;November 2026. Both dates fall inside the 1.6% period, which ends
          28&nbsp;February 2027. See the <a class="inline" href="notices.html">Notices</a> page for
          the full calendar.</td></tr>
        <tr><th>Decision 2 — all of it, or part?</th><td>There is no obligation to take the maximum.
          Banking has no expiry during a tenancy, so an unused percentage is not lost — it waits.
          What <em>is</em> lost is any percentage not yet banked when the anniversary date changes
          {s("banked")}</td></tr>
        <tr><th>Decision 3 — who reviews it?</th><td>Before serving, put the draft notice in front of
          a Rent Board counselor (free, 415-252-4600) and, if the banked portion is claimed, a
          landlord-side attorney. The <a class="inline" href="review.html">Lawyer review</a> page runs
          the twelve checks a tenant-side attorney would run.</td></tr>
      </table>
    </div>

    <div class="callout warn">
      <span class="ct">The one-sentence answer</span>
      Raise Unit&nbsp;1 to <strong>$4,114.85</strong> on 1&nbsp;February 2027 and Unit&nbsp;2 to
      <strong>$3,562.65</strong> on 15&nbsp;February 2027 — after confirming the rent increase licence
      is current and fixing Unit&nbsp;1's anniversary date — and give Unit&nbsp;2 ninety days' notice.
      Anything above those figures requires a Rent Board petition; anything served without a licence is
      unenforceable.
    </div>
    </div>
"""
    return write("summary.html", head(
        "Executive summary",
        "Executive summary of the lawful rent increase for two rent-controlled San Francisco units.",
        "summary.html") + body + foot())


# ===========================================================================
# 3. UNITS
# ===========================================================================
def build_units():
    rows = []
    for r in R.UNIT_FACTS:
        rows.append(
            "<tr>"
            '<td class="key">{}</td><td class="wrap-cell">{}</td><td class="wrap-cell">{}</td>'
            "<td>{}</td><td>{}</td><td>{}</td></tr>".format(
                r["field"], r["unit1"], r["unit2"], r["note"], s(r["src"]),
                status_badge(r["status"]))
        )

    body = page_head(
        "The two units",
        "Anonymised tenancy facts side by side, with the legal test that each fact drives. Dates and "
        "amounts are exactly as supplied; names are reduced to initials.",
        crumb='<a href="index.html">Dashboard</a> / Units',
    )

    body += f"""
    <div class="callout info">
      <span class="ct">Privacy handling</span>
      Only initials appear on this site. No street address, unit number, telephone number, email
      address, date of birth or employer is published. Where a fact would identify a household when
      combined with another, it has been generalised. Dates and dollar amounts are preserved
      unchanged, because they are what the legal analysis turns on and they are not, by themselves,
      identifying.
    </div>

    <div class="card flush">
      <div class="card-pad" style="padding-bottom:6px">
        <h2>Fact table</h2>
        <p class="small muted">Every row carries the source for the legal rule it invokes, or is marked
        as owner-supplied where no public record exists.</p>
      </div>
      <div class="table-tools">
        <input type="search" placeholder="Filter facts…" data-filter="facts" aria-label="Filter facts">
        <span class="count" data-count="facts"></span>
      </div>
      {table(["Fact", "Unit 1", "Unit 2", "Why it matters", "Source", "Status"], rows)}
    </div>

    <div class="card">
      <h2>Why the anniversary date is the hinge for Unit 1</h2>
      <p>Rule 1.11(a) defines the anniversary date as the date the tenant's current rent became
      effective, and says the next increase may not take effect until at least one year later
      {s("rr1")}. Two dates are plausible on the facts supplied:</p>
      <table class="plain">
        <tr><th>If the tenancy continued</th><td>Rent of $3,995.00 has been effective since
          1&nbsp;February 2025. The anniversary is 1&nbsp;February. A 1.4% increase became available on
          1&nbsp;February 2026 and was not taken. The earliest date on which both the banked 1.4% and
          the current 1.6% can be imposed together is <strong>1&nbsp;February 2027</strong>.</td></tr>
        <tr><th>If a new tenancy began</th><td>The new rent of $3,995.00 became effective
          1&nbsp;April 2026. The anniversary is 1&nbsp;April 2026, and no annual increase may take
          effect before <strong>1&nbsp;April 2027</strong> — by which time the rate will be whatever
          the Board publishes for the period beginning 1&nbsp;March 2027, not 1.6%.</td></tr>
      </table>
      <p class="small muted">This is recorded as flag F-02 because the supplied facts support either
      reading, and the difference is roughly fourteen months of delay. A Rent Board counselor can
      resolve it.</p>
    </div>

    <div class="card">
      <h2>What would change the answer entirely</h2>
      <p>Three facts, if true, would move either unit out of the analysis above. Each is worth checking
      before anything is served.</p>
      <ul>
        <li><strong>A valid written Section&nbsp;6.14 notice was served, and every original occupant
          has since left.</strong> That would permit an increase without the annual cap
          {s("614")}. On the facts supplied it has not happened — an original occupant remains — but
          for Unit&nbsp;2 it depends entirely on whether E&nbsp;R and I&nbsp;S are both still resident.</li>
        <li><strong>The unit is a separately-alienable single-family home or condominium and the
          tenancy began on or after 1&nbsp;January 1996.</strong> That would remove rent control
          altogether, leaving only AB 1482 and just cause {s("rentlaws")}. The building is described as
          having two units, which points away from this, but the building type has not been stated.</li>
        <li><strong>The unit is not a legal dwelling unit.</strong> An unauthorised unit can still be a
          rental unit under the Ordinance, so this does not remove rent control — but it changes the
          remedy available and is worth knowing {s("rentlaws")}.</li>
      </ul>
    </div>
    </div>
"""
    return write("units.html", head(
        "The two units",
        "Anonymised fact table for the two rent-controlled San Francisco units, with the legal test "
        "each fact drives.",
        "units.html") + body + foot())


# ===========================================================================
# 4. CALCULATIONS
# ===========================================================================
def build_calculations():
    def calc_rows(items, with_banked=False):
        out = []
        for r in items:
            cols = [
                '<td class="key wrap-cell">{}</td>'.format(r["scenario"]),
            ]
            if with_banked:
                cols.append('<td class="num">{}</td>'.format(r["banked"]))
            cols += [
                '<td class="num">{}</td>'.format(r.get("basis", r.get("current", ""))),
                '<td class="num">{}</td>'.format(r["pct"]),
                '<td class="num">{}</td>'.format(money(r["amount"])),
                '<td class="num"><strong>{}</strong></td>'.format(money(r["new_rent"])),
                '<td class="num">{}</td>'.format(r.get("notice", "90 days")),
                "<td>{}'.format('')</td>".format(""),
                '<td class="wrap-cell small">{}</td>'.format(r["comment"]),
                "<td>{}</td>".format(s(r["src"])),
            ]
            out.append("<tr>" + "".join(cols[:-2]) + cols[-2] + cols[-1] + "</tr>")
        return out

    body = page_head(
        "Calculations",
        "Every lawful figure for both units, computed from the Rent Board's published percentages. "
        "Banked percentages are added, never compounded, and no amount is rounded up.",
        crumb='<a href="index.html">Dashboard</a> / Calculations',
    )

    body += f"""
    <div class="chips">
      <span class="chip">Base rent — Unit 1 <b>$3,995.00</b></span>
      <span class="chip">Base rent — Unit 2 <b>$3,150.00</b></span>
      <span class="chip">Current annual rate <b>1.6%</b> {s("571")}</span>
      <span class="chip">Method <b>add, don't compound</b> {s("rr4")}</span>
    </div>

    <div class="card flush">
      <div class="card-pad" style="padding-bottom:4px">
        <h2>Unit 1 — $3,995.00 base</h2>
        <p class="small muted">Two lawful outcomes. They differ only in whether the 1.4% that became
        available on 1&nbsp;February 2026 is banked.</p>
      </div>
      {table(
        ["Scenario", "Rate applied", "Total %", "Increase", "New rent", "Notice", "Arithmetic", "Source"],
        [
          "<tr>"
          '<td class="key wrap-cell">A — Annual only, new anniversary date</td>'
          '<td class="num">1.6%</td><td class="num">1.6%</td>'
          '<td class="num">{}</td><td class="num"><strong>{}</strong></td>'
          '<td class="num">30 days</td>'
          '<td class="small">$3,995.00 × .016 = $63.92</td>'
          "<td>{}</td></tr>".format(money(63.92), money(4058.92), s("571")),
          "<tr>"
          '<td class="key wrap-cell">B — 1.4% banked + 1.6% annual, on the 1 Feb anniversary</td>'
          '<td class="num">1.4% + 1.6%</td><td class="num">3.0%</td>'
          '<td class="num">{}</td><td class="num"><strong>{}</strong></td>'
          '<td class="num">30 days</td>'
          '<td class="small">$3,995.00 × .030 = $119.85</td>'
          "<td>{}</td></tr>".format(money(119.85), money(4114.85), s("rr4")),
        ],
        thead_num=(1, 2, 3, 4, 5),
      )}
      <div class="card-pad">
        <div class="callout ok" style="margin-bottom:0">
          <span class="ct">Recommended for Unit 1 — scenario B</span>
          <strong>$4,114.85</strong> effective 1&nbsp;February 2027, requiring notice served on or
          before 2&nbsp;January 2027 (28&nbsp;December 2026 if mailed). Scenario A forfeits the 1.4%
          permanently, because it has not been banked until 1&nbsp;February 2027
          {s("banked")}. Scenario B is only available if the tenancy is a continuing one — see flag
          <a class="inline" href="flagged.html">F-02</a>.
        </div>
      </div>
    </div>

    <div class="card flush">
      <div class="card-pad" style="padding-bottom:4px">
        <h2>Unit 2 — $3,150.00 base</h2>
        <p class="small muted">Six annual increases were available and none was taken. Each is now
        more than 24 months old, so each is banked and none has expired.</p>
      </div>
      {table(
        ["Scenario", "Banked", "Current", "Total %", "Increase", "New rent", "Note", "Source"],
        [
          "<tr>"
          '<td class="key wrap-cell">A — Full banked history + current annual <span class="badge ok">recommended</span></td>'
          '<td class="num">11.5%</td><td class="num">1.6%</td><td class="num">13.1%</td>'
          '<td class="num">{}</td><td class="num"><strong>{}</strong></td>'
          '<td class="small wrap-cell">11.5 + 1.6 added, not compounded. More than 10%, so 90 days '
          "of notice.</td><td>{}</td></tr>".format(money(412.65), money(3562.65), s("rr4")),
          "<tr>"
          '<td class="key wrap-cell">B — Banked history only, annual reserved</td>'
          '<td class="num">11.5%</td><td class="num">0%</td><td class="num">11.5%</td>'
          '<td class="num">{}</td><td class="num"><strong>{}</strong></td>'
          '<td class="small wrap-cell">Still above 10%, so still 90 days. Leaves 1.6% unclaimed.</td>'
          "<td>{}</td></tr>".format(money(362.25), money(3512.25), s("rr4")),
          "<tr>"
          '<td class="key wrap-cell">C — Current annual only, no banking <span class="badge warn">forfeits 11.5%</span></td>'
          '<td class="num">0%</td><td class="num">1.6%</td><td class="num">1.6%</td>'
          '<td class="num">{}</td><td class="num"><strong>{}</strong></td>'
          '<td class="small wrap-cell">Lawful, and drops back to 30 days notice — but the 11.5% is '
          "gone for this tenancy.</td><td>{}</td></tr>".format(money(50.40), money(3200.40), s("571")),
        ],
        thead_num=(1, 2, 3, 4, 5),
      )}
    </div>

    <div class="card">
      <h2>Where Unit 2's 11.5% comes from</h2>
      <p>Each percentage is the rate that was actually in effect during the 12 months following
      Unit&nbsp;2's anniversary date. None was taken. They are now added together
      {s("571")}{s("rr4")}.</p>
      {table(
        ["Anniversary", "Rate that was available", "Taken?", "Banked", "Source"],
        [
          '<tr><td class="key">1 Jun 2020</td><td class="num">1.8%</td><td>{} </td>'
          '<td class="num">1.8%</td><td>{}</td></tr>'.format(badge("no", "muted"), s("571")),
          '<tr><td class="key">1 Jun 2021</td><td class="num">0.7%</td><td>{}</td>'
          '<td class="num">0.7%</td><td>{}</td></tr>'.format(badge("no", "muted"), s("571")),
          '<tr><td class="key">1 Jun 2022</td><td class="num">2.3%</td><td>{}</td>'
          '<td class="num">2.3%</td><td>{}</td></tr>'.format(badge("no", "muted"), s("571")),
          '<tr><td class="key">1 Jun 2023</td><td class="num">3.6%</td><td>{}</td>'
          '<td class="num">3.6%</td><td>{}</td></tr>'.format(badge("no", "muted"), s("571")),
          '<tr><td class="key">1 Jun 2024</td><td class="num">1.7%</td><td>{}</td>'
          '<td class="num">1.7%</td><td>{}</td></tr>'.format(badge("no", "muted"), s("571")),
          '<tr><td class="key">1 Jun 2025</td><td class="num">1.4%</td><td>{}</td>'
          '<td class="num">1.4%</td><td>{}</td></tr>'.format(badge("no", "muted"), s("571")),
          '<tr><td class="key">1 Jun 2026</td><td class="num">1.6%</td><td>{} </td>'
          '<td class="num">1.6%</td><td>{}</td></tr>'.format(badge("due now", "flag"), s("571")),
          '<tr class="total"><td>Banked subtotal</td><td class="num">—</td><td></td>'
          '<td class="num">11.5%</td><td>—</td></tr>',
          '<tr class="total"><td>Plus current annual</td><td class="num">—</td><td></td>'
          '<td class="num">1.6%</td><td>—</td></tr>',
          '<tr class="total"><td>Total allowable</td><td class="num">—</td><td></td>'
          '<td class="num">13.1%</td><td>—</td></tr>',
        ],
        thead_num=(1, 3),
      )}
      <p class="small muted" style="margin-top:12px">The 1.6% shown against 1&nbsp;June 2026 is the
      current annual increase, not a banked year — it is the increase that may be taken now. It is
      listed on the June row because that is the anniversary it attaches to.</p>
    </div>

    <div class="card">
      <h2>Two checks that always catch a bad calculation</h2>
      <h3>Adding, not compounding, works in the tenant's favour</h3>
      <p>If Unit&nbsp;2 had taken each increase as it arose, compounding would have produced
      <strong>$3,585.72</strong> by now — $23.07 <em>more</em> than the banked method's $3,562.65. The
      no-compounding rule is therefore not a penalty on the tenant; it is the reason the banked total
      is the lower of the two lawful routes. Both are shown so the difference is visible rather than
      asserted.</p>
      {table(
        ["Method", "Result", "Note", "Source"],
        [
          '<tr><td class="key">Banked percentages added (lawful)</td>'
          '<td class="num"><strong>$3,562.65</strong></td>'
          '<td class="small">11.5% + 1.6% = 13.1% of the original $3,150 base</td>'
          "<td>{}</td></tr>".format(s("rr4")),
          '<tr><td class="key">Sequential annual increases with compounding (illustrative only)</td>'
          '<td class="num">$3,585.72</td>'
          '<td class="small">1.8 → 0.7 → 2.3 → 3.6 → 1.7 → 1.4 → 1.6 applied to a rising base. '
          'Not available now, because the increases were not taken when they arose.</td>'
          "<td>{}</td></tr>".format(s("571")),
        ],
        thead_num=(1,),
      )}

      <h3>Nothing is rounded up</h3>
      <p>Both results land exactly on the cent: $3,995.00 × 3.0% = $119.85 exactly, and
      $3,150.00 × 13.1% = $412.65 exactly. No rounding is needed, so the "cannot be rounded up" rule
      {s("learn")} is not engaged. If a future calculation produces a fraction of a cent, the standard
      tolerance is 0.5% of the prior base rent before an increase is voided rather than corrected
      {s("rr4")}.</p>
    </div>

    <div class="callout risk">
      <span class="ct">The figure that would void everything</span>
      Any percentage above these totals is not a large increase — it is a <strong>null and void</strong>
      increase under § 37.3(b)(5) {s("373")}, recoverable by the tenant through a free Rent Board
      petition with no filing fee and no time limit {s("unlawful")}. If a higher figure is genuinely
      needed, the route is a petition, not a notice {s("petitions")}.
    </div>
    </div>
"""
    return write("calculations.html", head(
        "Calculations",
        "Lawful rent increase calculations for both rent-controlled units, with banked increases "
        "added rather than compounded.",
        "calculations.html") + body + foot())


# ===========================================================================
# 5. LAWS
# ===========================================================================
def build_laws():
    def rows_for(level, label):
        out = []
        for r in R.LAW_ROWS:
            if r["level"] != level:
                continue
            out.append(
                "<tr>"
                '<td class="key wrap-cell">{}</td>'
                '<td class="wrap-cell">{}</td>'
                '<td class="wrap-cell"><strong>{}</strong></td>'
                "<td>{}</td><td>{}</td></tr>".format(
                    r["topic"], r["rule"], r["value"], s(r["src"]), status_badge(r["status"]))
            )
        return out

    body = page_head(
        "Local, state and federal law",
        "The three layers that apply to a 1940 building in ZIP 94122, the controlling provision for "
        "each, and which layer wins where they overlap.",
        crumb='<a href="index.html">Dashboard</a> / Laws',
    )

    body += f"""
    <div class="card">
      <h2>Which layer wins</h2>
      <p>The three layers are not additive. They stack, with the <em>most restrictive</em> applicable
      provision controlling. For this property the local layer is the most restrictive, so it governs
      the amount — but the state layer still governs notice and procedure, and the federal layer still
      governs discrimination.</p>
      <table class="plain">
        <tr><th>Federal</th><td>Sets no ceiling. Applies in full to <em>how</em> rent is set.</td></tr>
        <tr><th>State</th><td>Would allow 8.8%, but defers to a stricter local cap
          {s("civ1947_12")}. Governs notice periods {s("civ827")}.</td></tr>
        <tr><th>Local</th><td><strong>Controls the amount</strong> at 1.6% for the current period, and
          governs the licence, the components of the notice, and what makes an increase void
          {s("571")}{s("373")}</td></tr>
      </table>
    </div>

    <div class="card flush">
      <div class="card-pad" style="padding-bottom:4px"><h2>Local — San Francisco</h2>
      <p class="small muted">Administrative Code Chapter 37 (the Rent Ordinance) and the Rent Board
      Rules, plus Chapter 49A.</p></div>
      <div class="table-tools">
        <input type="search" placeholder="Filter provisions…" data-filter="laws" aria-label="Filter provisions">
        <span class="count" data-count="laws"></span>
      </div>
      {table(["Topic", "What the provision says", "Value for this file", "Source", "Status"],
             rows_for("Local", "Local"))}
    </div>

    <div class="card flush">
      <div class="card-pad" style="padding-bottom:4px"><h2>State — California</h2>
      <p class="small muted">Civil Code and Government Code provisions that apply alongside the
      Ordinance.</p></div>
      {table(["Topic", "What the provision says", "Value for this file", "Source", "Status"],
             rows_for("State", "State"))}
    </div>

    <div class="card flush">
      <div class="card-pad" style="padding-bottom:4px"><h2>Federal — United States</h2>
      <p class="small muted">The Fair Housing Act and the federal statutes that touch rent-setting in
      practice.</p></div>
      {table(["Topic", "What the provision says", "Value for this file", "Source", "Status"],
             rows_for("Federal", "Federal"))}
    </div>

    <div class="card">
      <h2>The provision most often got wrong: AB 1482's 8.8%</h2>
      <p>Many summaries of California rent law lead with "8.8% for San Francisco". That figure is real —
      it is the AB 1482 cap for 1&nbsp;August 2026 to 31&nbsp;July 2027 {s("ab1482")} — but it does not
      apply to a unit that is already under a local cap lower than the state cap. Civil Code
      §&nbsp;1947.12(d)(3) excludes exactly that case, and the Rent Board says so in terms: the state
      maximum "does NOT apply for units under the rent increase limitations of the San Francisco Rent
      Ordinance" {s("civ1947_12")}{s("ab1482")}.</p>
      <p>For a 1940 building in ZIP 94122 that is the whole answer on the amount: 8.8% is unavailable,
      1.6% is the ceiling, and any notice written to 8.8% would be void.</p>
    </div>

    <div class="card">
      <h2>Two local provisions with real teeth</h2>
      <h3>Algorithmic rent-setting is banned outright</h3>
      <p>Section&nbsp;37.10C took effect on 14&nbsp;October 2024. It is unlawful to sell or to
      <em>use</em> revenue-management software that sets or recommends rents using competitors'
      non-public data. Each month of a continuing violation, and each unit affected, is a separate
      violation, with civil penalties of up to $1,000 and attorneys' fees for a prevailing tenant
      {s("algo")}. For a two-unit owner the practical effect is simple: there is no compliant way to
      import a software-generated "market" rent into this analysis.</p>

      <h3>Charging for an added occupant is an unlawful increase</h3>
      <p>Section&nbsp;37.3(a)(11) prohibits raising rent <em>solely</em> because a tenant added an
      occupant, "notwithstanding a rental agreement or lease that specifically permits a rent increase
      for additional occupants" {s("373")}{s("occupants")}. Unit&nbsp;1 added M&nbsp;T. Any part of the
      Unit&nbsp;1 increase that is attributable to that fact is unlawful; the increase must rest purely
      on the anniversary.</p>
    </div>
    </div>
"""
    return write("laws.html", head(
        "Local, state and federal law",
        "Local, state and federal rent-increase law for a rent-controlled San Francisco unit in ZIP "
        "94122, with the controlling provision for each question.",
        "laws.html") + body + foot())


# ===========================================================================
# 6. AGA HISTORY
# ===========================================================================
def build_history():
    import csv

    rows = []
    with open(os.path.join(ROOT, "data", "aga-history.csv"), newline="") as f:
        rd = csv.DictReader(f)
        for r in rd:
            rows.append(r)

    out = []
    for r in rows:
        note = r["note"]
        cls = ' class="key"' if False else ""
        out.append(
            '<tr{cls}><td class="key">{}</td><td>{}</td><td class="num">{}</td>'
            '<td class="small muted">{}</td><td>{}</td></tr>'.format(
                r["effective_start"], r["effective_end"], r["allowable_increase_pct"],
                note, s("571") if not note else s("571"), cls="")
        )

    body = page_head(
        "Allowable annual rent increase history",
        "The Rent Board's full published table, 1 April 1982 to 28 February 2027, transcribed "
        "verbatim from Form 571. This is the table every banked-increase calculation depends on.",
        crumb='<a href="index.html">Dashboard</a> / AGA history',
    )

    body += f"""
    <div class="callout info">
      <span class="ct">Transcription note</span>
      The 46 rows below are copied from the Rent Board's own Form 571, "Allowable Annual Rent
      Increases (1982–present)", updated for the 2026-27 period {s("571")}. The percentages have not
      been recalculated, restated or rounded. The two 1992 rows carry the Board's own caution and are
      reproduced with it.
    </div>

    <div class="card flush">
      <div class="table-tools">
        <input type="search" placeholder="Filter by year, e.g. 2023" data-filter="history" aria-label="Filter history">
        <span class="count" data-count="history"></span>
        <span class="small muted" style="margin-left:12px">Also available as
          <a class="inline" href="data/aga-history.csv">CSV</a></span>
      </div>
      {table(["Effective from", "Effective to", "Allowable increase", "Board's note", "Source"], out)}
    </div>

    <div class="card">
      <h2>How to read this table for banking</h2>
      <p>The rate attached to a given anniversary is the rate <em>in effect on that date</em>, not
      today's rate. A year skipped when the allowance was 1.4% banks 1.4%, not 1.6%
      {s("banked")}. That is why Unit&nbsp;2's six banked years use six different percentages rather
      than 1.6% six times.</p>
      <p>To find the rate for a particular anniversary, read down the "Effective from" column to the
      1&nbsp;March period that covers the anniversary date. An anniversary of 1&nbsp;June 2023 falls in
      the 1&nbsp;March 2023 – 29&nbsp;February 2024 period, so the rate is 3.6%.</p>

      <h3>The 2026 anomaly, in the Board's own words</h3>
      <p>Rule 1.12 was amended on 13 January 2026 because the federal government shutdown of 2025
      prevented the Bureau of Labor Statistics from ever publishing the October 2025 CPI. Because the
      Ordinance requires an October-to-October comparison, the Board approximated October 2025 as the
      geometric mean of the published August 2025 and December 2025 values. The Bureau confirms the
      October 2025 figure does not exist {s("rramend")}{s("bls_cpi")}.</p>
      <p>The Board has said a similar interim method will be needed for the 2027 figure, after which
      the standard calculation resumes. The rate for March 2027 onward was not published as at
      {TODAY} and is deliberately not shown here.</p>
    </div>

    <div class="card">
      <h2>Rates that matter for these two units</h2>
      {table(
        ["Unit", "Anniversary", "Rate available then", "Taken?", "Consequence", "Source"],
        [
          '<tr><td class="key">Unit 1</td><td>1 Feb 2026</td><td class="num">1.4%</td><td>No</td>'
          '<td class="small">Banked only from 1 Feb 2027. Before that date it is lost.</td>'
          "<td>{}</td></tr>".format(s("banked")),
          '<tr><td class="key">Unit 1</td><td>1 Feb 2027</td><td class="num">1.6%</td><td>Due</td>'
          '<td class="small">Can be combined with the banked 1.4% for a 3.0% total.</td>'
          "<td>{}</td></tr>".format(s("rr4")),
          '<tr><td class="key">Unit 2</td><td>1 Jun 2020 → 1 Jun 2025</td>'
          '<td class="num">1.8 + 0.7 + 2.3 + 3.6 + 1.7 + 1.4</td><td>No</td>'
          '<td class="small">All six banked, total 11.5%.</td>'
          "<td>{}</td></tr>".format(s("571")),
          '<tr><td class="key">Unit 2</td><td>1 Jun 2026</td><td class="num">1.6%</td><td>Due</td>'
          '<td class="small">Plus the banked 11.5% = 13.1%.</td>'
          "<td>{}</td></tr>".format(s("rr4")),
        ],
        thead_num=(2,),
      )}
    </div>
    </div>
"""
    return write("aga-history.html", head(
        "Allowable annual rent increase history",
        "Complete Rent Board table of allowable annual rent increases, 1982 to 2027, transcribed from "
        "Form 571.",
        "aga-history.html") + body + foot())


# ---------------------------------------------------------------------------
def main():
    made = []
    for fn in (build_index, build_summary, build_units, build_calculations,
               build_laws, build_history):
        made.append(fn())
    for p in made:
        print("wrote", os.path.relpath(p, ROOT))


if __name__ == "__main__":
    main()
