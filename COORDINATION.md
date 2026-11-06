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

Every value published on the site must carry a source link to an official (`.gov`, court, or
legislative) source. Values that could not be confirmed from an official source are left blank
and flagged in `data/flags.json` → published on **Flagged for Review**. Nothing was inferred.

| Item | Value | Official source | Verified |
|---|---|---|---|
| SF allowable annual increase, 3/1/2026 – 2/28/2027 | **1.6%** | [sf.gov news 1/14/2026](https://www.sf.gov/news--annual-rent-increase-3126-22827-announced) · [sf.gov Learn about rent increases](https://www.sf.gov/learn-about-rent-increases-san-francisco) · [Info Sheet 571 PDF](https://www.sf.gov/documents/34344/571_Allowable_Annual_Increases_26-27_1.pdf) | ✅ |
| SF allowable annual increase, 3/1/2025 – 2/28/2026 | 1.4% | same three sources | ✅ |
| Full historical table 1982→2027 | 23 rows | [Info Sheet 571 PDF](https://www.sf.gov/documents/34344/571_Allowable_Annual_Increases_26-27_1.pdf) | ✅ |
| Increase is 60% of CPI-U Bay Area, capped at 7% | — | SF Admin Code §37.3(a)(1) via [Ord. 265-20](https://sfbos.org/sites/default/files/o0265-20.pdf) · [sf.gov](https://www.sf.gov/learn-about-rent-increases-san-francisco) | ✅ |
| Once every 12 months; anniversary date rule | — | [sf.gov Learn about rent increases](https://www.sf.gov/learn-about-rent-increases-san-francisco) | ✅ |
| Banking permitted; not compounded; not rounded up; only since 4/1/1982 | — | [Rent Board Rules §4.12](https://www.sf.gov/reports--december-2022--rent-board-rules-and-regulations-part-iv-rent-increases-not-requiring) · [sf.gov Banked rent increases](https://www.sf.gov/information--banked-rent-increases) | ✅ |
| 30-day written notice (≤10%); 90-day (>10%); +5 days if mailed | — | [Cal. Civ. Code §827(b)(2)–(3)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=827) · [sf.gov](https://www.sf.gov/learn-about-rent-increases-san-francisco) | ✅ |
| Rent increase license required before annual/banked increase | — | SF Admin Code §37.15 · Rent Board Reg §13.14 · [sf.gov Housing Inventory](https://www.sf.gov/rent-board-housing-inventory) | ✅ |
| Increase while unlicensed = **null and void** | — | [sf.gov Housing Inventory](https://www.sf.gov/rent-board-housing-inventory) · Rent Board Reg §13.14 | ✅ |
| Housing Inventory deadline March 1 annually; portal.sfrb.org | — | [sf.gov Housing Inventory](https://www.sf.gov/rent-board-housing-inventory) | ✅ |
| License phase-in: 7/1/2022 (10+ units); 3/1/2023 (condos & 1–9 units) | — | [sf.gov Housing Inventory](https://www.sf.gov/rent-board-housing-inventory) | ✅ |
| Rent control coverage: certificate of occupancy on/before 6/13/1979 | — | [sf.gov Learn about SF rental laws](https://www.sf.gov/learn-about-san-francisco-rental-laws) | ✅ |
| No increase permitted because a tenant added an occupant | — | [sf.gov Learn about rent increases](https://www.sf.gov/learn-about-rent-increases-san-francisco) · SF Admin Code §37.3(a)(11)(A) | ✅ |
| No limit on how much may be banked; banked amounts do not carry to a new tenant | — | [sf.gov Banked rent increases](https://www.sf.gov/information--banked-rent-increases) | ✅ |
| AB 1482 cap for SF = 8.8% (8/1/2026 – 7/31/2027) but does **not** apply to SF Rent Ordinance units | — | [sf.gov AB 1482](https://www.sf.gov/reports--california-tenant-protection-act-2019-ab-1482) · [Cal. Civ. Code §1947.12(d)(3)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1947.12) | ✅ |
| AB 1482 two-unit owner-occupied exemption | — | [sf.gov AB 1482](https://www.sf.gov/reports--california-tenant-protection-act-2019-ab-1482) · Cal. Civ. Code §1946.2(e)(8)/§1947.12(d) | ✅ |
| Vacancy decontrol — no limit on initial rent for an empty unit | — | [sf.gov](https://www.sf.gov/learn-about-rent-increases-san-francisco) · Cal. Civ. Code §1954.52 | ✅ |
| Median gross rent, ZCTA 94122 | see `data/market.json` | [U.S. Census Bureau API, ACS 5-year](https://api.census.gov/data/2024/acs/acs5?get=NAME,B25064_001E,B25064_001M&for=zip%20code%20tabulation%20area:94122) | ✅ |
| HUD Fair Market Rents, San Francisco–Oakland–Fremont CA HUD Metro FMR Area | see `data/market.json` | [HUD USER FMR](https://www.huduser.gov/portal/datasets/fmr.html) | ✅ |
| CPI-U, San Francisco–Oakland–Hayward | see `data/market.json` | [BLS](https://www.bls.gov/regions/pacific/news-release/consumerpriceindexsanfrancisco.htm) | ✅ |
| Federal Fair Housing Act protected classes | 42 U.S.C. §3604 | [HUD](https://www.hud.gov/program_offices/fair_housing_equal_opp/fair_housing_act_overview) | ✅ |
| CA FEHA housing discrimination | Gov. Code §12955 | [Cal. Civ. Rights Dep't](https://calcivilrights.ca.gov/housing/) | ✅ |
| SF non-discrimination in housing ordinance | Admin Code Ch. 95 | [SF HRC](https://www.sf.gov/departments--human-rights-commission/) | ✅ |
| Retaliation presumption, 180 days | Cal. Civ. Code §1942.5 | [leginfo](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1942.5) | ✅ |
| Tenant harassment | SF Admin Code §37.10B | [sf.gov](https://www.sf.gov/information--tenant-harassment) | ✅ |
| Free tenant counseling, Rent Board | 415-252-4600 | [sf.gov](https://www.sf.gov/speak-rent-board-counselor/) | ✅ |
| SF algorithmic rent-setting prohibition | — | [sf.gov news](https://www.sf.gov/news--new-law-prohibits-algorithmic-devices-used-set-rents-san-francisco/) | ✅ |

### Unverified / left blank (published on Flagged for Review)

| Item | Why blank |
|---|---|
| Certificate of occupancy date for the subject property | Requires the property's address/APN — not supplied, and address is PII. Owner must check [SF Property Information Map](https://sfplanninggis.org/PIM/). |
| Whether either unit is a condominium | Condo status changes Costa-Hawkins analysis. Not supplied. |
| Whether an owner occupies either unit | Changes AB 1482 two-unit exemption. Not supplied. |
| Whether a rent increase license is currently on file | Requires [Rent Board Portal](https://portal.sfrb.org/) account lookup. Not verifiable externally. |
| Whether any increase was ever imposed on Unit 2 between 6/1/2019 and today | Only the 6/1/2019 lease at $3,150 was supplied; a complete rent ledger is required. |
| Whether Unit 1's 4/1/2026 rental agreement reset the anniversary date | No official SF source resolves this fact pattern. Flagged. |
| Security deposit interest rate in force | Not part of the request; not researched. |
| Building condition / capital-improvement history | Not supplied; would affect §37.7 petitions. |

---

## Change Requests Against Other Sessions' Files

None. No other session holds a claim.

---

## Conflict / Handoff Log

| Timestamp (UTC) | Session | Event |
|---|---|---|
| 2026-11-06 | `arena-48ffb5b4` | Board created. Repo contained only `README.md` (17 bytes, `# RentincreaseSF2`). No competing claims found. All tasks claimed by this session. |

---

## Final Integration Record

| Field | Value |
|---|---|
| Integration session | `arena-48ffb5b4` |
| Branch merged | `arena/48ffb5b4-rentincreasesf2` → `main` |
| Link check | see `docs/integration-report.md` |
| Pull request | see `docs/integration-report.md` |
| Merge result | see `docs/integration-report.md` |
| GitHub Pages URL | https://kanlerxz87-cyber.github.io/RentincreaseSF2/ |
| Pages build status | see `docs/integration-report.md` |
