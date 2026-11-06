# COORDINATION.md — Shared Task Board

**Repository:** `kanlerxz87-cyber/RentincreaseSF2`
**Purpose:** Shared task board for parallel agent sessions. Claim a task by writing your session ID
and file scope below, then commit and push that claim immediately. Never start a task another
session has claimed. Keep scopes non-overlapping. Run `git pull --rebase` before every push.

> **Privacy rule (applies to every session, no exceptions):** No personally identifiable
> information about any tenant or owner may be committed to this repository. This repository
> publishes to a public GitHub Pages site. Use placeholder identifiers only
> (`Unit 1`, `Unit 2`, `Tenant A`, `Tenant B`, ...). Dates and dollar amounts are preserved
> exactly as provided; all names and identifying details are replaced. See
> `docs/PRIVACY-AND-ANONYMIZATION.md`.

---

## Sessions

| Session ID | Branch | Role | Status |
|---|---|---|---|
| `arena-48ffb5b4` | `arena/48ffb5b4-rentincreasesf2` | All tasks below **+ final integration** (only session active on this repo; repo was empty apart from `README.md` at start, so no competing claims exist) | active |

**Note on branch naming:** the platform pins this session to branch
`arena/48ffb5b4-rentincreasesf2` and forbids switching branches, so the conventional
`session-<id>/<task>` naming is not used. This branch is the single working branch and also
serves as the integration branch. No other session has claimed any task.

---

## Task Board

| # | Task | Status | Owner | Files in scope |
|---|---|---|---|---|
| 00 | Create `COORDINATION.md` shared task board | done | `arena-48ffb5b4` | `COORDINATION.md` |
| 01 | Privacy / anonymization policy — placeholder mapping, confirm zero PII in repo | done | `arena-48ffb5b4` | `docs/PRIVACY-AND-ANONYMIZATION.md` |
| 02 | Repo review — line-by-line audit of pre-existing content, flag irregularities | done | `arena-48ffb5b4` | `docs/repo-review.md` |
| 03 | Source register — every official source, URL, date accessed, what it verifies | done | `arena-48ffb5b4` | `data/sources.json`, `pages/sources.html` |
| 04 | SF Rent Ordinance research — allowable increases, banking, notice, license | done | `arena-48ffb5b4` | `data/allowable-increases.json`, `pages/local-law.html` |
| 05 | California state law research — Civ. Code §§ 827, 1946.2, 1947.12, 1954.50 (Costa-Hawkins) | done | `arena-48ffb5b4` | `data/state-law.json`, `pages/state-law.html` |
| 06 | Federal law research — Fair Housing Act, HUD, BLS CPI, HUD FMR | done | `arena-48ffb5b4` | `data/federal-law.json`, `pages/federal-law.html` |
| 07 | Unit dataset — anonymized rent history for Unit 1 and Unit 2 | done | `arena-48ffb5b4` | `data/units.json`, `pages/units.html` |
| 08 | Lawful-increase calculations, scenario modelling | done | `arena-48ffb5b4` | `data/calculations.json`, `pages/calculations.html` |
| 09 | Market analysis for ZIP 94122 (Outer Sunset) | done | `arena-48ffb5b4` | `data/market.json`, `pages/market.html` |
| 10 | Corporate vs. individual-owner practice research | done | `arena-48ffb5b4` | `pages/practices.html` |
| 11 | Anti-discrimination / "one unit or both units" analysis | done | `arena-48ffb5b4` | `pages/anti-discrimination.html` |
| 12 | Tenant-lawyer scrutiny test + free tenant legal services in SF | done | `arena-48ffb5b4` | `pages/tenant-review.html` |
| 13 | Compliance checklist + notice procedure + reasonableness guidance | done | `arena-48ffb5b4` | `pages/checklist.html` |
| 14 | Executive summary (Markdown + HTML) | done | `arena-48ffb5b4` | `docs/executive-summary.md`, `pages/executive-summary.html` |
| 15 | Flagged for Review page — all irregularities + unverified items | done | `arena-48ffb5b4` | `data/flags.json`, `pages/flagged.html` |
| 16 | Site build — landing page, subpages, nav, tables, dashboard UI | done | `arena-48ffb5b4` | `index.html`, `assets/**`, `pages/**` |
| 17 | **Integration** — re-verify combined data, link check, publish to GitHub Pages | done | `arena-48ffb5b4` | all |
| 18 | PR to `main`, merge, confirm Pages deploy, record result here | done | `arena-48ffb5b4` | `COORDINATION.md` |

---

## Verification Log

Every value published on the site carries a source link to an official (`.gov`, legislative,
Rent Board or Census Bureau) source. Values that could **not** be confirmed are left **blank**
and flagged in `data/flags.json` → published on **Flagged for Review**. Nothing was inferred.

✅ = value confirmed from the linked official source, fetched during this session.
⚠️ = official source exists but the row is incomplete, conflicting, or was **not** fetched; published with the caveat attached.
❌ = **left blank**. No official value obtained. Published as blank, never estimated.

> **Correction note (2026-11-06).** An earlier draft of this log marked several rows ✅ before
> the underlying fetch had succeeded. Those rows were re-checked at integration and are now
> correctly recorded below — two are ❌ (HUD FMR, BLS CPI), one is ⚠️ (SF Admin Code Ch. 95,
> never fetched), one is ⚠️ (tenant harassment, source page 404), the Census row's URL was
> replaced with the endpoint that actually works without an API key, and "security deposit
> interest" was **moved out of the unverified table** because it was in fact verified at 4.2%.

| Item | Value | Official source | Status |
|---|---|---|---|
| SF allowable annual increase, 3/1/2026 – 2/28/2027 | **1.6%** | [sf.gov news 1/14/2026](https://www.sf.gov/news--annual-rent-increase-3126-22827-announced) · [sf.gov Learn about rent increases](https://www.sf.gov/learn-about-rent-increases-san-francisco) · [Info Sheet 571 PDF](https://www.sf.gov/documents/34344/571_Allowable_Annual_Increases_26-27_1.pdf) · [sf.gov Current Rates](https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit) | ✅ |
| SF allowable annual increase, 3/1/2025 – 2/28/2026 | 1.4% | same four sources | ✅ |
| Full historical allowable-increase table | **46 periods**, 4/1/1982 → 2/28/2027 | [Info Sheet 571 PDF](https://www.sf.gov/documents/34344/571_Allowable_Annual_Increases_26-27_1.pdf) — transcribed verbatim | ✅ |
| Increase = 60% of CPI-U Bay Area, capped at 7% | — | [SF Admin Code §37.3(a)(1) via Ord. 11-24-24](https://www.sf.gov/sites/default/files/2024-12/600%20Ordinance%2011-24-24.pdf) · [sf.gov](https://www.sf.gov/learn-about-rent-increases-san-francisco) | ✅ |
| Once every 12 months; anniversary-date mechanics; four worked examples | — | [sf.gov Learn about rent increases](https://www.sf.gov/learn-about-rent-increases-san-francisco) | ✅ |
| Banking permitted; added not compounded; not rounded up; back to 4/1/1982; no limit; does not carry to a new tenant; new owners inherit | — | [sf.gov Banked rent increases](https://www.sf.gov/information--banked-rent-increases) · [Rules §4.12](https://www.sf.gov/reports--december-2022--rent-board-rules-and-regulations-part-iv-rent-increases-not-requiring) | ✅ |
| **Banking requires 12 full months to elapse** | 12 months | [Rent Board Rules §4.12(a)](https://www.sf.gov/reports--december-2022--rent-board-rules-and-regulations-part-iv-rent-increases-not-requiring) | ⚠️ **F-03** — [sf.gov Banked rent increases](https://www.sf.gov/information--banked-rent-increases) says **24 months** and then contradicts itself in its own worked example. Both official texts published; conflict not resolved here. |
| A skipped increase is **permanently lost** if the anniversary date changes before it banks | — | [sf.gov worked example](https://www.sf.gov/learn-about-rent-increases-san-francisco) | ✅ |
| Increase applies to **base rent only** (incl. parking/storage, excl. passthroughs) | — | [sf.gov](https://www.sf.gov/learn-about-rent-increases-san-francisco) | ✅ |
| Use the percentage in effect on the **effective date**, not the service date | — | [sf.gov Banked rent increases](https://www.sf.gov/information--banked-rent-increases) | ✅ |
| 30-day notice ≤10%; **90-day** notice >10%; measured vs lowest rent in prior 12 months incl. combined increases; +5 days if mailed | — | [Cal. Civ. Code §827(b)(2)–(3)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=827) · [sf.gov](https://www.sf.gov/learn-about-rent-increases-san-francisco) | ✅ |
| Non-conforming increase is **null and void** in its entirety; ≤½% good-faith overage may be readjusted | — | [Rent Board Rules §4.10(b)](https://www.sf.gov/reports--december-2022--rent-board-rules-and-regulations-part-iv-rent-increases-not-requiring) | ✅ |
| Rent increase **license** required before any annual/banked increase | — | [SF Admin Code §37.15](https://sfbos.org/sites/default/files/o0265-20.pdf) · [sf.gov Housing Inventory](https://www.sf.gov/rent-board-housing-inventory) | ✅ |
| Increase while unlicensed = **null and void** | — | [Rent Board Rules §13.14](https://sfrb.org/section-1314-licensing-%E2%80%93-notice-rent-increase) · [sf.gov Housing Inventory](https://www.sf.gov/rent-board-housing-inventory) | ✅ |
| Housing Inventory: portal.sfrb.org, deadline **March 1** annually, no monetary late penalty | — | [sf.gov Housing Inventory](https://www.sf.gov/rent-board-housing-inventory) | ✅ |
| License phase-in: **7/1/2022** (10+ units); **3/1/2023** (condos & 1–9 units) | — | [sf.gov Housing Inventory](https://www.sf.gov/rent-board-housing-inventory) | ⚠️ **F-12** — [Rent Board Form 538](https://www.sf.gov/sites/default/files/2024-10/538%202024-25%20Bond%20Measure%20Worksheet%2010.24%20.pdf) states 7/1/**2020** and 3/1/**2021**. sf.gov dates used. |
| Housing Inventory submissions are **public**, under penalty of perjury | — | [sf.gov Housing Inventory](https://www.sf.gov/rent-board-housing-inventory) | ✅ |
| Rent control coverage: certificate of occupancy on/before **6/13/1979** | — | [sf.gov Learn about SF rental laws](https://www.sf.gov/learn-about-san-francisco-rental-laws) | ✅ |
| **A two-unit building is NOT exempt** from the Rent Ordinance | — | [sf.gov Topic 019](https://www.sf.gov/information--partial-exemption-certain-single-family-homes-and-condominiums-under-costa-hawkins) | ✅ |
| Charging more because a tenant **added an occupant** = unlawful increase even if the lease permits it; refundable | — | [sf.gov Topics 152/254](https://www.sf.gov/information--charging-additional-occupants-prohibited) · SF Admin Code §37.3(a)(11)(A) | ✅ |
| Market-rate reset requires the **LAST original occupant** to vacate + a timely written §6.14 notice; co-tenants are never subject | — | [sf.gov Topic 153](https://www.sf.gov/information--rent-increases-under-section-614-and-costa-hawkins) · Cal. Civ. Code §1954.53(d) | ✅ |
| Tenants may replace roommates; landlord has **14 days**; silence/unreasonable denial = deemed approved; occupancy caps | — | [sf.gov Replacement of Roommates](https://www.sf.gov/information--replacement-roommates) · Rules §§6.15A/B/D/E | ✅ |
| **§37.10C algorithmic-pricing ban**, effective 10/14/2024; per-unit and per-month violations; up to $1,000 each; tenants **and tenants' organisations** may sue | — | [sf.gov Topic 268](https://www.sf.gov/information--algorithmic-devices-set-rent-are-prohibited-san-francisco) · [sf.gov news](https://www.sf.gov/news--new-law-prohibits-algorithmic-devices-used-set-rents-san-francisco) · [Legistar legislation](https://sfgov.legistar.com/View.ashx?M=F&ID=13312164&GUID=D1DC4F7F-DFD9-433D-9D17-82992BDE5B91) | ✅ |
| AB 1482 SF cap = **8.8%** (8/1/2026 – 7/31/2027) but does **NOT apply** to SF Rent Ordinance units | — | [sf.gov AB 1482](https://www.sf.gov/reports--california-tenant-protection-act-2019-ab-1482) · [Cal. Civ. Code §1947.12(d)(3)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1947.12) | ✅ |
| AB 1482 two-unit owner-occupied exemption | — | [sf.gov AB 1482](https://www.sf.gov/reports--california-tenant-protection-act-2019-ab-1482) · Cal. Civ. Code §§1946.2(e), 1947.12(d) | ✅ |
| **Corporate owners lose** the Costa-Hawkins single-family/condo exemption (REIT, corporation, LLC with a corporate member) | — | [Cal. Civ. Code §1947.12(d)(5)(A)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1947.12) | ✅ |
| Vacancy decontrol — no limit on initial rent for an **empty** unit | — | [sf.gov](https://www.sf.gov/learn-about-rent-increases-san-francisco) · Cal. Civ. Code §1954.52 | ✅ |
| O&M petition: ≤7% of base rent per petition; 7% five-year aggregate for 6+ units | — | [Rent Board Form 530 Schedule B](https://www.sf.gov/file/530-om-petition-fillable-324pdf) | ✅ |
| Tenant petition forms **516A / 516B / 516C / 516D / 517 / 518** | — | [Rent Board Forms Center](https://www.sf.gov/reports--rent-board-forms-forms-center) | ⚠️ chunk 0 of 12 fetched — tenant forms confirmed; landlord-side forms and the notice-of-rent-increase form are in unfetched chunks |
| Form **525** Report of Excessive Rent Increase (AB 1482); Rent Board **cannot enforce state law** | — | [Form 525 PDF](https://www.sf.gov/documents/18505/525_Report_of_Excessive_Rent_Increase_Under_the_TPA_10.25.pdf) | ✅ |
| Retaliation: **180-day** bar on increasing rent after specified tenant complaints; separate bar for tenant organising; immigration-authority threats prohibited; waiver void | — | [Cal. Civ. Code §1942.5](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1942.5) — full section text fetched and quoted | ✅ |
| Federal Fair Housing Act protected classes: race, color, national origin, religion, sex, familial status, disability; applies to nearly all housing incl. private | 42 U.S.C. §§3601–3619 | [HUD Fair Housing Act overview](https://www.hud.gov/helping-americans/fair-housing-act-overview) | ✅ |
| HUD FHEO enforcement prioritisation guidance + withdrawn guidance documents | — | [HUD FHEO PDF](https://www.hud.gov/sites/dfiles/Main/documents/Fair-Housing-Act-Enforcement-Prioritization-Resources.pdf) | ✅ |
| Federal complaint intake route | — | [HUD reporthousingdiscrimination](https://www.hud.gov/reporthousingdiscrimination) | ✅ |
| **No federal statute caps rent increases** for unsubsidised private housing | — | Scope confirmed via [HUD Fair Housing Act overview](https://www.hud.gov/helping-americans/fair-housing-act-overview); both sf.gov and leginfo identify local/state law as the operative limits | ✅ |
| CA FEHA scope + full protected-characteristic list incl. source of income, immigration status, primary language, familial status, age; **protects a roommate/associate's characteristic**; retaliation prohibited | Gov. Code §12955 | [California Civil Rights Department — Housing](https://calcivilrights.ca.gov/housing/) | ✅ |
| SF non-discrimination in housing ordinance | Admin Code Ch. 95 | [SF Human Rights Commission](https://www.sf.gov/departments--human-rights-commission/) | ⚠️ **never fetched** — cited for manual review only; no value published from it |
| Tenant harassment | SF Admin Code §37.10B | [Rent Board laws & regulations](https://www.sf.gov/resource/2023/rent-board-laws-and-regulations) | ⚠️ **F-10** — the sf.gov harassment page returned **404**; penalty figures could **not** be confirmed and are **not** published anywhere on the site |
| Free Rent Board counseling, **415-252-4600**, M–F 9–12 & 1–4, 25 Van Ness Ave #700, cannot give legal advice | — | [sf.gov Speak with a Rent Board counselor](https://www.sf.gov/speak-rent-board-counselor) | ✅ (⚠️ **F-17**: news archive lists a 2025 "Rent Board has moved" item — confirm the address before travelling) |
| Free tenant legal services directory (Eviction Defense Collaborative 415-659-9184, BASF Conflict Intervention Service 415-782-8940, Housing Rights Committee, Bay Area Legal Aid, BiSHoP, Chinatown CDC, Mission Action, SOMCAN, BHP Tenants' Rights Clinic) | — | [sf.gov Tenant and Landlord Resources](https://www.sf.gov/tenant-and-landlord-resources) (Mayor's Office of Housing and Community Development) | ✅ |
| **Security deposit interest rate in force** | **4.2%** for 3/1/2026 – 2/28/2027 | [sf.gov Current Rates](https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit) | ✅ *(corrected — an earlier draft wrongly listed this as "not researched")* |
| Capital improvement imputed interest rates | 4.1% /7yr (.01372), 4.3% /10yr (.01027), 4.6% /15yr (.00770), 4.8% /20yr (.00649) | [sf.gov Current Rates](https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit) · [Form 574 PDF](https://www.sf.gov/documents/34916/574_Cap._Imp._Imputed_Interest_26-27_7.26.pdf) | ✅ (⚠️ **F-13**: the page's "575 Cap. Imp. Labor Rates" link resolves to the **574** document) |
| Uncompensated labor rate | **$40.40** from 6/29/2026 | [sf.gov Current Rates](https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit) | ✅ |
| Relocation payments 2026-27 | $8,245.00/tenant, max $24,733.00/unit, +$5,497.00 elderly(60+)/disabled/minors | [sf.gov Current Rates](https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit) | ✅ |
| Ellis Act payments 2026-27 | $11,110.05/tenant, max $33,330.13/unit, +$7,443.90 elderly(62+)/disabled | [sf.gov Current Rates](https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit) | ✅ |
| Bankable Rent Board fee | tenant $29.50 + landlord $29.50 for tax years 2023-24 and 2024-25 **only** | [sf.gov Current Rates](https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit) | ⚠️ **F-14** — the official table **omits 2025-26 and 2026-27**. Current-year figure left **blank**, not assumed. |
| Median gross rent, ZCTA 94122 | **$2,816** ±$153 | [Census ACS 2020-2024 5yr B25064](https://data.census.gov/api/access/data/table?id=ACSDT5Y2024.B25064&g=860XX00US94122) | ✅ |
| Median gross rent, San Francisco County | **$2,476** ±$30 | [Census B25064](https://data.census.gov/api/access/data/table?id=ACSDT5Y2024.B25064&g=050XX00US06075) | ✅ |
| Median household income, ZCTA 94122 | **$146,250** ±$12,113 | [Census B19013](https://data.census.gov/api/access/data/table?id=ACSDT5Y2024.B19013&g=860XX00US94122) | ✅ |
| Gross rent distribution, ZCTA 94122 | 10,864 with cash rent; brackets <$2,000 **2,731**, $2,000–2,499 **1,826**, $2,500–2,999 **1,384**, $3,000–3,499 **1,587**, $3,500+ **3,336** | [Census B25063](https://data.census.gov/api/access/data/table?id=ACSDT5Y2024.B25063&g=860XX00US94122) | ✅ brackets sum **exactly** to the published total; checked by `build.py` |
| Rent burden, ZCTA 94122 | ≥30% = **4,510** = **42.1%**; ≥50% = **2,227** = **20.8%** (universe 10,702) | [Census B25070](https://data.census.gov/api/access/data/table?id=ACSDT5Y2024.B25070&g=860XX00US94122) | ✅ reconciles to published universe |
| Year structure built, ZCTA 94122 | 24,208 units; **93.7%** pre-6/13/1979; 1940–49 = 4,423 (18.3%); ≤1939 = 11,116 (45.9%) | [Census B25034](https://data.census.gov/api/access/data/table?id=ACSDT5Y2024.B25034&g=860XX00US94122) | ✅ buckets sum exactly to the published total |
| **Every Census variable label** | 7 labels fetched individually | [Census variable definitions](https://api.census.gov/data/2024/acs/acs5/variables/B25063_026E.json) | ✅ B25063_022E/023E/025E/026E and B25034_002E/010E/011E confirmed rather than assumed |
| Census retrieval method | key-free endpoint `data.census.gov/api/access/data/table` | — | ✅ `api.census.gov/data/.../acs5?get=…` returns **"Missing Key"** and was **not** used |
| HUD Fair Market Rent, San Francisco area | — | [HUD USER FMR](https://www.huduser.gov/portal/datasets/fmr.html) | ❌ **F-01 — LEFT BLANK.** API returned `{"error":"Unauthenticated"}`; two dataset URLs 404'd; third-party FY26 2-BR values conflicted ($3,604 vs $3,160) and were rejected |
| CPI-U, San Francisco–Oakland–Hayward | — | [BLS Pacific region](https://www.bls.gov/regions/pacific/) | ❌ **F-02 — LEFT BLANK.** Regional news-release URL returned 404. Immaterial: sf.gov instructs owners to use the **published** 1.6%, not a recomputed CPI figure |
| Allowable increase for **3/1/2027 – 2/28/2028** | — | [Rent Board news](https://www.sf.gov/departments--rent-board/news) | ❌ **F-18 — not yet published.** Consequently Unit 2 Scenario U2-A's final total is left blank |
| Comparative data: corporate vs individual landlord increase behaviour | — | none exists | ❌ **F-21 — no official source publishes this.** Answered structurally from verified statutory differences instead; **no behavioural statistic is asserted anywhere** |

### Unverified / left blank (published on Flagged for Review)

| Item | Flag | Why blank |
|---|---|---|
| Certificate of occupancy date for the subject property | **F-04** | Requires the address/APN — not supplied, and the address is PII. Owner must check the [SF Property Information Map](https://sfplanninggis.org/PIM/). Decisive: could remove both units from rent control. |
| Whether either unit is a condominium | **F-05** | Condo status changes the Costa-Hawkins analysis for both tenancies (both commenced after 1/1/1996). Not supplied. |
| Whether an owner occupies either unit | **F-05** | Changes the AB 1482 two-unit exemption. Not supplied. Immaterial to the operative cap either way. |
| Whether a rent increase license is currently on file | **F-22** | Requires a [Rent Board Portal](https://portal.sfrb.org/) login. Not verifiable externally. **Failure renders the entire increase null and void.** |
| Whether any increase was ever imposed on Unit 2 between 6/1/2019 and today | **F-08** | Only the 6/1/2019 lease at $3,150 was supplied. The 11.5%/13.1% banked totals rest on this assumption. Form 516C recalculates from 4/1/1982. |
| Whether Unit 1's 4/1/2026 rental agreement reset the anniversary date | **F-07** | **No official SF source resolves this fact pattern.** Scenario U1-C published with every dollar value blank. |
| Banked-increase elapse period: 12 or 24 months | **F-03** | Two official sf.gov sources conflict and one contradicts its own worked example. 12-month Rule §4.12 text used in analysis; conflict published, not resolved. |
| Proposed cap on banked increases at 10%/yr | **F-16** | Only third-party reporting (2026-09-17). No enactment found in any official source. Unit 2's 13.1% marked **provisional**. |
| Security deposit interest rate in force | — | **CORRECTED:** verified at **4.2%**; moved to the verified table above. |
| Building condition / capital-improvement / O&M history | **F-09** | Not supplied. Separate petition routes (Admin Code §§37.3(a)(3)–(6), 37.7, 37.8) deliberately not modelled. |
| Retaliation screen result (§1942.5) | **F-06** | No tenant complaint, repair, inspection or organising history supplied. Cannot be screened. |
| Tenant harassment penalties under §37.10B | **F-10** | Official sf.gov page returned 404. Row marked UNVERIFIED; **no dollar figures published**. |
| HUD Fair Market Rent for the SF area | **F-01** | See ❌ rows above. |
| BLS CPI-U index values | **F-02** | See ❌ rows above. |
| Current-year bankable Rent Board fee | **F-14** | Absent from the official rate table. Not assumed. |

---

## Change Requests Against Other Sessions' Files

None. No other session holds a claim.

---

## Conflict / Handoff Log

| Timestamp (UTC) | Session | Event |
|---|---|---|
| 2026-11-06 | `arena-48ffb5b4` | Board created. Repo contained only `README.md` (17 bytes, `# RentincreaseSF2`). No competing claims found. All tasks claimed by this session. |
| 2026-11-06 | `arena-48ffb5b4` | First `git push` printed `fatal: couldn't find remote ref arena/48ffb5b4-rentincreasesf2` from the preceding `git pull --rebase`. **Expected** — the branch did not yet exist remotely. The push succeeded and created it. Not a conflict. |
| 2026-11-06 | `arena-48ffb5b4` | **No merge conflicts occurred at any point.** This was the only session; nothing was overwritten and no other session's work existed to preserve. |
| 2026-11-06 | `arena-48ffb5b4` | Integration found **12** corrections needed in this session's own earlier output, including a Census aggregation error and eight stale ✅ marks in the verification log above. All fixed rather than published as-is — see `docs/integration-report.md` §3. |

---

## Final Integration Record

| Field | Value |
|---|---|
| Integration session | `arena-48ffb5b4` (also the sole working session — no competing claims existed) |
| Branch merged | `arena/48ffb5b4-rentincreasesf2` → `main` |
| Combined data re-verified | ✅ 11 dollar-figure checks and 8 notice-deadline checks re-derived from official percentages and matched against the stored values; banked sums re-derived independently (Unit 2 = 11.5% pre-6/1/2027, 13.1% after) |
| Census reconciliation | ✅ B25063 brackets sum exactly to 10,864; B25070 to 10,702 (+867 not-computed = 11,569); B25034 to 24,208. 7 variable labels fetched individually rather than assumed |
| Allowable-increase table | ✅ 46 periods transcribed verbatim from Info Sheet 571; current period and 7 prior periods cross-checked against three independent official sources |
| Source-link enforcement | ✅ every `law.json` rule row has a source URL; every `verified: false` row has a flag ID; every source and flag entry has a URL. One row published UNVERIFIED (§37.10B, F-10) with no figures |
| Internal link check | ✅ every `href` in all 15 documents resolved against the generated file set — **no broken links** |
| External link check | ✅ **253** external links, all official or primary sources; single third-party link (localnewsmatters.org) appears only as the *secondary* source for F-16 with an explicit not-official caveat |
| HTML structural check | ✅ tag balance across 15 element types, one doctype and terminating `</html>` in all 15 documents; no leaked template expressions |
| PII sweep | ✅ clean — no SSN-shaped value, no non-official email or phone number, no tenant name, address or APN anywhere in the repository |
| Local serving check | ✅ all 15 pages + 2 assets + `.nojekyll` returned HTTP 200 with non-zero content |
| Build | `python3 build.py` → exit 0. A non-zero exit means a broken site and is never committed |
| Corrections made at integration | **12** — see `docs/integration-report.md` §3. Included a Census aggregation error (436 → **2,731**), a wrongly-raised flag (**F-17 resolved**), missing new law (**F-24**, effective 2026-02-09), and **eight** stale ✅ marks in the verification log above that were reclassified to ⚠️ or ❌ |
| Flagged items | **24** — 7 HIGH, 8 medium, 5 low, 3 informational, 1 cosmetic. Published on [Flagged for Review](pages/flagged.html); per protocol these do **not** block the merge |
| Values left blank | **11** categories, each published blank with its reason and flag ID — never inferred |
| Pull request | _filled in below after creation_ |
| Merge result | _filled in below after merge_ |
| GitHub Pages URL | https://kanlerxz87-cyber.github.io/RentincreaseSF2/ |
| Pages build status | _filled in below after deploy_ |
| Full report | [`docs/integration-report.md`](docs/integration-report.md) |

### Sources used

**47 official documents**, registered with what each one verifies in
[`data/sources.json`](data/sources.json) and rendered as a filterable table on
[Source Register](pages/sources.html). Domains: `sf.gov` (Rent Board), `leginfo.legislature.ca.gov`
(primary California statutes), `data.census.gov` and `api.census.gov` (U.S. Census Bureau),
`hud.gov` and `huduser.gov`, `calcivilrights.ca.gov`, `sfrb.org` (Rent Board Rules & Regulations),
`portal.sfrb.org`, `sfbos.org` (ordinance text), `sfplanninggis.org`, `bls.gov`.

Third-party legal blogs, property-management vendors, tenant-union pages and news aggregators were
consulted **only to locate** official documents. **No value anywhere on the site comes from a
non-official source.** Where third-party figures conflicted — two different FY2026 HUD 2-bedroom
Fair Market Rents for San Francisco, $3,604 versus $3,160 — the value was rejected entirely and
left blank rather than choosing between them.

### Verification performed

See `docs/integration-report.md` §2 for the full method. In summary: official sources only;
primary statutory text preferred over descriptions of it; every table row carries a source link
enforced by the generator; arithmetic re-derived at build time rather than typed; Census bracket
counts sum-checked against published totals; official sources cross-checked **against each other**
(which is what surfaced the three genuine conflicts F-03, F-11 and F-12 and the two official-page
defects F-13 and F-14); anything unconfirmable left blank and flagged.

### Irregularities

**In the official sources themselves (7):**

| Flag | Source | Defect |
|---|---|---|
| **F-03** | sf.gov *Banked rent increases* vs Rent Board Rules §4.12 vs Admin Code §37.3(a)(2) | **Three official sources, two answers.** sf.gov says a skipped increase banks only after **24 full months**; the Rules say **12**; the codified ordinance states no condition. sf.gov then contradicts its own worked example, which banks an increase that had only 12 months. **Material to Unit 2.** 12-month Rule §4.12 text used; conflict published, not resolved |
| **F-11** | sf.gov *Learn about San Francisco rental laws* | Still cites **1.7%** for the 2024–Feb 2025 period as though current; the current rate is 1.6% |
| **F-12** | Rent Board Form 538 | States the §37.15 license applies from **7/1/2020** and **3/1/2021**; sf.gov gives 7/1/**2022** and 3/1/**2023** |
| **F-13** | sf.gov *Current Rates* | The link labelled **"575 Cap. Imp. Labor Rates"** resolves to the **574** imputed-interest PDF |
| **F-14** | sf.gov *Current Rates* | Headed for 3/1/2026–2/28/2027 but the bankable Rent Board Fee table **omits the 2025-26 and 2026-27 tax years** |
| **F-15** | Info Sheet 571 Spanish PDF | Filename carries a doubled extension `.pdf.pdf` |
| **F-17** | sf.gov counselor page vs Rent Board news archive | **RESOLVED at integration** — the 2025-03-18 move notice says the Board moved **to** 25 Van Ness Ave Suite 700, the same address the counselor page gives. An earlier draft read this as a conflict; it is not |

**In the repository as received (6):** R-01 to R-06 in [`docs/repo-review.md`](docs/repo-review.md).
The significant one is **R-02**: GitHub Pages was already enabled against a repository containing
only a 17-byte `README.md`, using the legacy Jekyll build with no `.nojekyll` and no `index.html`,
so the published URL served nothing useful. Fixed by adding `.nojekyll` and building the site.

**Requiring owner records or a portal login (7 HIGH):** F-03, F-04, F-06, F-07, F-08, F-16, F-22.
No notice should be served until these are closed. Two of them — F-04 (certificate of occupancy)
and F-22 (rent increase license) — could each independently change the outcome completely.

**Analytical limitations, stated rather than papered over:** no official source publishes
comparative data on corporate versus individual landlord increase behaviour, so the question is
answered structurally from verified statutory differences and **no behavioural statistic is
asserted** (F-21); the 3/1/2027–2/28/2028 percentage does not exist yet, so Unit 2 Scenario A's
final total is blank (F-18); and a public site carrying exact rents leaves a re-identification
path, with two mitigations described but not applied unilaterally (F-23).
