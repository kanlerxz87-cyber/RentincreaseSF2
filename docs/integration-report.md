# Integration Report

**Integration session:** `arena-48ffb5b4`
**Branch:** `arena/48ffb5b4-rentincreasesf2` → `main`
**Date:** 2026-11-06

This session was also the **sole working session**. A coordination check performed before any
file was created found no `COORDINATION.md`, no competing branch, no other session's commits
and no open pull requests — so there was no other session's output to integrate against.
This report therefore covers (a) re-verification of this session's own combined data,
(b) the link check, and (c) the publication result.

---

## 1. What was integrated

| Layer | Files | Status |
|---|---|---|
| Data | `data/allowable-increases.json`, `current-rates.json`, `units.json`, `calculations.json`, `market.json`, `law.json`, `sources.json`, `flags.json` | 8 files, all parse as JSON |
| Documents | `docs/executive-summary.md`, `docs/repo-review.md`, `docs/PRIVACY-AND-ANONYMIZATION.md` | 3 files |
| Site | `index.html` + 14 subpages in `pages/`, `assets/css/styles.css`, `assets/js/app.js` | 15 HTML documents |
| Coordination | `COORDINATION.md` | task board, verification log, integration record |
| Repo hygiene | `.nojekyll`, `.gitignore`, rewritten `README.md` | added |
| Generator | `build.py` | verification harness + generator |

Nothing is hand-written twice: the HTML is **generated from the JSON**, so a table on the site
cannot drift from the data file behind it.

---

## 2. Verification performed at integration

`build.py` runs every check below and **exits non-zero** on any failure. Nothing was committed
from a failed build.

### 2.1 Arithmetic re-derivation — 11 dollar checks, all pass

Every dollar figure published on the site is recomputed at build time from the official
percentages and compared against the value stored in `data/calculations.json`. A mismatch fails
the build.

| Check | Recomputed | Stored | Result |
|---|---|---|---|
| Unit 1 Scenario A total percentage | 1.4 + 1.6 = 3.0 | 3.0% | ✅ |
| Unit 1 Scenario A dollar increase | $3,995.00 × 3.0% = $119.85 | $119.85 | ✅ |
| Unit 1 Scenario A resulting rent | $4,114.85 | $4,114.85 | ✅ |
| Unit 1 Scenario B dollar increase | $3,995.00 × 1.6% = $63.92 | $63.92 | ✅ |
| Unit 1 Scenario B resulting rent | $4,058.92 | $4,058.92 | ✅ |
| Cost of acting early on Unit 1 | $55.93/month | $55.93 | ✅ |
| Unit 2 banked-only dollar amount | $3,150.00 × 13.1% = $412.65 | $412.65 | ✅ |
| Unit 2 Scenario A/B resulting rent | $3,562.65 | $3,562.65 | ✅ |
| Unit 2 Scenario C dollar increase | $3,150.00 × 10.0% = $315.00 | $315.00 | ✅ |
| Unit 2 Scenario C resulting rent | $3,465.00 | $3,465.00 | ✅ |
| Unit 2 11.5% component | $362.25 | $362.25 | ✅ |

Banked percentage sums were also re-derived independently from the per-anniversary official
percentages: Unit 2 pre-6/1/2027 = **11.5%** and post-6/1/2027 = **13.1%**, both matching.

### 2.2 Notice-deadline re-derivation — 8 deadline checks, all pass

Serve-by dates are computed as *effective date minus the statutory notice period*, then compared
against the stored values.

| Scenario | Notice period | Effective | Serve by | Mailed (+5 days) |
|---|---|---|---|---|
| Unit 1 A | 30 days | 2027-02-01 | **2027-01-02** | 2026-12-28 |
| Unit 1 A | 35 days | 2027-02-01 | — | **2026-12-28** |
| Unit 2 A | 90 days | 2027-06-01 | **2027-03-03** | 2027-02-26 |
| Unit 2 A | 95 days | 2027-06-01 | — | **2027-02-26** |
| Unit 2 B | 90 days | 2027-02-08 | **2026-11-10** | 2026-11-05 |
| Unit 2 B | 95 days | 2027-02-08 | — | **2026-11-05** |
| Unit 2 C | 30 days | 2027-02-08 | **2027-01-09** | 2027-01-04 |
| Unit 2 C | 35 days | 2027-02-08 | — | **2027-01-04** |

### 2.3 Allowable-increase table spot-check

The current period and the seven most recent prior periods in `data/allowable-increases.json`
were compared against the values independently confirmed from three official sources
(the 2026-01-14 announcement, Info Sheet 571, and the Current Rates report). All match:
**1.6 / 1.4 / 1.7 / 3.6 / 2.3 / 0.7 / 1.8 / 2.6%**. The full table contains **46 periods**.

### 2.4 U.S. Census Bureau reconciliation — 3 sets, all reconcile exactly

| Table | Check | Result |
|---|---|---|
| B25063 gross rent | 2,731 + 1,826 + 1,384 + 1,587 + 3,336 = **10,864** = published with-cash-rent total | ✅ |
| B25070 rent burden | brackets sum to **10,702** computed universe; 10,702 + 867 not-computed = **11,569** universe | ✅ |
| B25034 year built | buckets sum to **24,208** total housing units | ✅ |

An aggregation error **was caught and fixed** during this reconciliation: the "<$2,000" row had
been written as 436 (the sum of the nine sub-$1,000 brackets only) instead of **2,731** (all
brackets below $2,000). The derived share of 74.9% paying $2,000+ was already correct, which is
what exposed the inconsistency. The row now carries its sub-bracket breakdown and the verified
label for B25063_022E.

Seven Census variable labels were fetched **individually** from the Census variable-definition
endpoint rather than assumed: `B25063_022E`, `B25063_023E`, `B25063_025E`, `B25063_026E`,
`B25034_002E`, `B25034_010E`, `B25034_011E`.

### 2.5 Source-link enforcement

Every rule row in `data/law.json` was checked for a non-empty `source` URL, and every row with
`verified: false` was checked for an associated flag ID. Every source register entry was checked
for a URL. Every flag was checked for a source. **All pass.** Exactly one law row is published as
`UNVERIFIED` — SF Admin. Code § 37.10B tenant harassment — and it carries no dollar figures
(Flag F-10).

### 2.6 PII sweep

Every generated document was swept for SSN-shaped values, email addresses and phone numbers.
Non-official matches fail the build. Allowlists cover only the official Rent Board, city
agency and free-legal-service contacts published by sf.gov. **Result: clean.** No tenant name,
address, APN or other identifier appears anywhere in the repository.

### 2.7 Link check — internal

Every `href` in all 15 documents was resolved relative to its own directory and checked against
the set of generated files plus the linked `data/`, `docs/` and root files. **No broken internal
links.** An earlier draft of the checker produced 18 false positives by failing to normalise
sibling links inside `pages/`; the checker was fixed to resolve via `os.path.normpath` relative
to each document's directory, after which all links resolve.

### 2.8 Link check — external

**253 external links**, all to official or primary sources. Domain breakdown of the generated
site:

| Domain | Links | Kind |
|---|---|---|
| `www.sf.gov` | 163 | City & County of San Francisco / Rent Board |
| `leginfo.legislature.ca.gov` | 27 | California Legislative Information (primary statutes) |
| `data.census.gov` | 13 | U.S. Census Bureau data API |
| `www.hud.gov` | 9 | U.S. Department of Housing and Urban Development |
| `sfplanninggis.org` | 8 | SF Planning official GIS tool (cited by sf.gov) |
| `calcivilrights.ca.gov` | 8 | California Civil Rights Department |
| `sfrb.org` | 5 | SF Rent Board (Rules & Regulations) |
| `portal.sfrb.org` | 5 | SF Rent Board Housing Inventory portal |
| `www.huduser.gov` | 4 | HUD Office of Policy Development and Research |
| `api.census.gov` | 2 | Census variable-definition endpoint |
| `sfbos.org` | 1 | SF Board of Supervisors (ordinance text) |
| `www.bls.gov` | 1 | Bureau of Labor Statistics (cited as the failed lookup for F-02) |
| `github.com` / `kanlerxz87-cyber.github.io` | 3 | This repository and its Pages URL |
| `localnewsmatters.org` | 1 | **Third-party** — cited only as the secondary source for Flag F-16, with an explicit caveat that it is not official and that no enactment was found |

Every sf.gov, leginfo, sfrb.org, sfbos.org, calcivilrights.ca.gov, hud.gov, huduser.gov and
Census URL in the register **was fetched during this project**. Two were fetched again at
integration to confirm they resolve and to capture newer official content (see § 3).

### 2.9 HTML structural check

All 15 documents were parsed for tag balance across `table`, `thead`, `tbody`, `tr`, `td`, `th`,
`div`, `ul`, `ol`, `li`, `p`, `main`, `nav`, `h2`, `h3`; each was checked for exactly one
`<!DOCTYPE html>` and a terminating `</html>`. **Zero structural issues.** A scan for leaked
template expressions, `None`, `NaN`, `undefined` and placeholder text found none — the apparent
`null` hits are the legal phrase "null and void" and the apparent `None` hits are prose in flag
impact fields.

### 2.10 Local serving check

All 15 pages plus both asset files and `.nojekyll` were served over HTTP and returned **200** with
non-zero content. Rendered spot-checks confirmed the headline figures ($4,114.85, $3,562.65,
13.1%, 3.0%, 1.6%) appear in the generated HTML.

---

## 3. Corrections made during integration

Integration is supposed to catch things, and it caught several. Each was fixed rather than
published as-is.

| # | What was wrong | Correction |
|---|---|---|
| 1 | `data/market.json` "<$2,000" gross-rent row held **436** instead of **2,731** | Recomputed from the sub-bracket breakdown; sum now reconciles exactly to 10,864; label for B25063_022E fetched and recorded |
| 2 | **Flag F-17 was wrong.** It read the March 2025 "Rent Board has moved" news item as evidence the counselor page address was stale | Fetched the announcement: the Board moved **to** 25 Van Ness Avenue Suite 700 on 2025-03-18 — the same address the counselor page gives. F-17 reclassified **RESOLVED**, severity lowered to informational, finding text rewritten to state the earlier reading was wrong |
| 3 | The § 37.10C algorithmic-pricing row did not reflect the **October 6, 2025** expansion of enforcement to tenants' rights organisations | Row updated with the date, the change and File No. 240796; primary source switched to the official announcement |
| 4 | **New law was missing entirely**: demolition and major-renovation tenant protections effective **February 9, 2026** | Added as a new rule row and as **Flag F-24**. Materially relevant to Flag F-09 (capital-improvement displacement now carries up to 39 months of additional relocation for lower-income tenants) and to Flag F-10 (now the authoritative official description of Rent Board harassment hearings) |
| 5 | `COORDINATION.md`'s verification log marked **HUD FMR** and **BLS CPI** ✅ even though both values are blank | Both reclassified ❌ with the reason and flag ID; a correction note added at the top of the log explaining the change |
| 6 | The log's Census row cited `api.census.gov/data/2024/acs/acs5?get=…`, which returns **"Missing Key"** | Replaced with the key-free `data.census.gov/api/access/data/table` endpoint that was actually used; the failure mode is recorded so nobody repeats it |
| 7 | The log listed "**Security deposit interest rate in force — not part of the request; not researched**" as unverified | It *was* researched and verified at **4.2%** for 3/1/2026 – 2/28/2027, independently confirmed by the 2026-01-09 announcement. Moved into the verified table |
| 8 | The log marked **SF Admin Code Ch. 95** and **tenant harassment § 37.10B** ✅ though neither page was successfully fetched | Ch. 95 reclassified ⚠️ "never fetched — cited for manual review only; no value published from it". § 37.10B reclassified ⚠️ F-10 with the 404 recorded and the row marked UNVERIFIED with no figures |
| 9 | The log marked the Rent Board **Forms Center** ✅ though only chunk 0 of 12 was fetched | Reclassified ⚠️ with an explicit note that tenant forms are confirmed and landlord-side forms are in unfetched chunks |
| 10 | The log cited the HUD Fair Housing Act overview at a `program_offices/…` path | Replaced with the `helping-americans/fair-housing-act-overview` URL that actually resolves |
| 11 | Residual re-identification risk of a public site was mentioned in the repo review but referenced a flag that did not exist | Added as **Flag F-23** with both mitigations described and an explicit note that neither was applied unilaterally |
| 12 | Hardcoded source and flag counts in the generator and docs drifted as the registers grew | All counts made dynamic; `README.md` and both docs synced to **47 sources / 24 flags / 7 HIGH** |

The log now uses a three-state marker — ✅ verified, ⚠️ incomplete or conflicting, ❌ left blank —
instead of a bare ✅, so a reader can see at a glance which rows are not fully closed.

---

## 4. Flagged and unverified items published

**24 flags: 7 HIGH, 8 medium, 5 low, 3 informational and 1 cosmetic.** One of the informational
items, **F-17**, is a *resolved* flag retained on the page for the audit trail — it records that an
earlier reading of the Rent Board's move notice was wrong and shows the correction.

Per the task protocol, flagged items **do not block the merge**. They are published on a clearly
labelled **[Flagged for Review](../pages/flagged.html)** page, each with its source link, its
impact and the action required to close it. That page also carries a dedicated table of every
value **deliberately left blank** across the site, and a separate table of the **seven defects
found in official sources themselves** — including the material conflict where two sf.gov pages
state different banking periods (12 months vs 24 months) and one contradicts its own worked
example.

The seven HIGH-severity flags that must be closed before any notice is served:

| Flag | Item |
|---|---|
| F-03 | Official sources conflict on whether banking requires 12 or 24 months to elapse |
| F-04 | Certificate of occupancy date not established |
| F-06 | Retaliation screen cannot be run — no tenant complaint history supplied |
| F-07 | No official source resolves whether Unit 1's 2026-04-01 agreement reset the anniversary date |
| F-08 | Unit 2's rent ledger assumed, not verified |
| F-16 | Pending legislation would cap banked increases at 10% — Unit 2's 13.1% marked provisional |
| F-22 | Rent increase license status unverifiable externally; absence voids the entire increase |

---

## 5. Site structure

A landing dashboard plus 14 category subpages. Sidebar navigation groups them into Findings,
Legal framework, Analysis and Verification. No external dependencies of any kind — no CDN, no
webfont, no framework — so the site renders identically offline, in the sandbox preview and on
GitHub Pages.

| Page | Content |
|---|---|
| `index.html` | Dashboard: KPI cards, the two-unit comparison table, answers to the five questions asked, verification status, what changed in the repo |
| `pages/executive-summary.html` | The full executive summary |
| `pages/units.html` | Anonymized unit profiles, rent ledgers, legal consequences of the occupancy facts |
| `pages/calculations.html` | All seven scenarios with percentages, dollar amounts, notice tiers, serve-by dates and the reasoning |
| `pages/local-law.html` | 25 San Francisco rules, each with authority, official source and verification state |
| `pages/state-law.html` | 11 California rules |
| `pages/federal-law.html` | 5 federal rules |
| `pages/allowable.html` | All 46 official percentages 1982–2027, plus current rates in force |
| `pages/market.html` | Census figures with inline distribution bars, derived shares and the two blank metrics |
| `pages/practices.html` | Corporate vs individual owners, from verified statutory differences only |
| `pages/discrimination.html` | One unit or both — the full analysis and the uniform policy text |
| `pages/tenant-review.html` | Free tenant services, seven petition routes, the eight-question test |
| `pages/checklist.html` | Fourteen notice elements, legitimate vs illegitimate reasons, dated action plan |
| `pages/sources.html` | The 47-entry source register with a filter box |
| `pages/flagged.html` | All 24 flags with severity filter, blank-values table, official-source defects |

Tables are filterable client-side (vanilla JS, ~1.3 KB). The flags table has severity buttons.

---

## 6. Publication

| Field | Value |
|---|---|
| Pages configuration | `build_type: legacy`, source `main`, path `/`, HTTPS enforced — already enabled before this work |
| `.nojekyll` | **Added**, so Pages serves the static site verbatim instead of running Jekyll (which would also exclude `_`-prefixed and certain other filenames) |
| Pull request | [**#5**](https://github.com/kanlerxz87-cyber/RentincreaseSF2/pull/5) |
| Build | `python3 build.py` — exits 0 |
| URL | https://kanlerxz87-cyber.github.io/RentincreaseSF2/ |

---

## 7. Residual limitations, stated plainly

1. **This is not legal advice.** The Rent Board's own counselors "cannot give legal advice"; a
   research project certainly cannot.
2. **Seven HIGH-severity flags are open.** No notice should be served until they are closed. Two
   of them (F-04 certificate of occupancy, F-22 license status) could each independently change
   the outcome completely.
3. **Unit 2's 13.1% is provisional** pending Flag F-16 (proposed banking cap) and cannot be
   finalised until the 3/1/2027 – 2/28/2028 percentage is published (Flag F-18).
4. **No behavioural claim is made** about how corporate landlords actually set rents, because no
   official source publishes such data (Flag F-21). The corporate-vs-individual comparison is
   structural, not empirical.
5. **Two official sources genuinely conflict** on the banking elapse period (Flag F-03). Both are
   published with their URLs. This project deliberately does **not** pick a winner beyond noting
   which text is the regulation and which is a guidance page — that is a question for a Rent Board
   counselor.
6. **A public site carrying exact rents leaves a re-identification path** (Flag F-23). Two
   mitigations are described; neither was applied without the owner's decision.
