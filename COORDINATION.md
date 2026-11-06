# COORDINATION.md — Shared Task Board & Multi-Session Verification Log

**Repo:** `kanlerxz87-cyber/RentincreaseSF2`  
**Live site:** https://kanlerxz87-cyber.github.io/RentincreaseSF2/  
**Last updated:** 2026-11-06  
**Privacy Policy:** Zero personal names, initials, contact details, or street addresses appear in any file, commit, or PR. Anonymized placeholders (`Tenant 1A`, `Tenant 1B`, `Tenant 1C`, `Tenant 1D`, `Tenant 2A`, `Tenant 2B`) are used while preserving exact dates and dollar amounts.

---

## Multi-Session Registry

| Session ID | Role | Status |
|---|---|---|
| `arena/3eac9d0e-rentincreasesf2` | Initial build session (PR #1 merged at `1e6f88f`) | Completed initial 7-page site & deployed. Full record preserved below. |
| `arena/81e8c938-rentincreasesf2` (`session-arena-81e8c938`) | First remediation & CI validation session (PR #2 merged at `153b260`) | Expanded to 10 pages, added banked math, `.github/workflows/validate.yml`, and `scripts/validate_site.py`. Full record preserved below. |
| `arena/39ba7aa1-rentincreasesf2` (active session) | Deep primary-source audit, municipal statistical verification, & final integration | `T1`–`T5` `done`; `T6` `in progress` (integrating deep primary-source research, correcting `April 1, 2026` intake semantics, restoring anonymized placeholder names, adding verified corporate/algorithmic/ZIP `94122` official data, and enforcing blank cells on unverified fields). |

---

## Shared Task Board — Session `arena/39ba7aa1-rentincreasesf2`

| Task ID | Task Description | Status | Owning Session ID | Claimed At (UTC) | File Scope |
|---|---|---|---|---|---|
| `T1` | Official Source Verification: SF Local Law (Admin Code Ch. 37, Form 571 Rates 2019–2027, Banking Rules, Housing Inventory License, Rules § 6.14, § 37.10C Algorithmic Ban) | `done` | `arena/39ba7aa1-rentincreasesf2` | `2026-11-06T13:19:00Z` | `docs/research-local-sf.md` |
| `T2` | Official Source Verification: CA State Law (Costa-Hawkins, AB 1482 SF County 8.8% Cap, Civ. Code § 827, CCP § 1013, FEHA, Unruh, § 1942.5), Federal Law (FHA, DOJ), & ZIP `94122` Data | `done` | `arena/39ba7aa1-rentincreasesf2` | `2026-11-06T13:25:00Z` | `docs/research-state-federal-market.md` |
| `T3` | Corporate vs. Individual Landlord Practices, Proper Rent Increase Notice Protocol, SF Tenant Lawyer Scrutiny Standards, & Single-Unit vs. Both-Units Fair Housing Analysis | `done` | `arena/39ba7aa1-rentincreasesf2` | `2026-11-06T13:31:00Z` | `docs/analysis-practices-lawyer-audit.md` |
| `T4` | Anonymized Unit 1 & Unit 2 Rent Calculations, Executive Summary, & Irregularities / Unverified Items Audit | `done` | `arena/39ba7aa1-rentincreasesf2` | `2026-11-06T13:35:00Z` | `docs/unit-calculations-and-flags.md`, `docs/executive-summary.md` |
| `T5` | Verified Structured Dataset & Line-by-Line Official Source Registry | `done` | `arena/39ba7aa1-rentincreasesf2` | `2026-11-06T13:38:00Z` | `data/verified-data.json` |
| `T6` | Final Integration Upgrade of GitHub Pages Site (10 HTML Pages + `style.css` + `scripts/validate_site.py`) | `in progress` | `arena/39ba7aa1-rentincreasesf2` | `2026-11-06T13:41:00Z` | `index.html`, `executive-summary.html`, `units.html`, `analysis.html`, `laws.html`, `process.html`, `tenant-protections.html`, `practices.html`, `flagged.html`, `sources.html`, `style.css`, `scripts/validate_site.py`, `README.md` |
| `T7` | Final Line-by-Line Re-Verification, Automated Validation, PR Creation, Merge to `main`, & GitHub Pages Deployment Confirmation | `unclaimed` | — | — | `COORDINATION.md` |

---

## Line-by-Line Review of `origin/main` (`153b260`) by `arena/39ba7aa1-rentincreasesf2`

Before modifying any shared site file, session `arena/39ba7aa1-rentincreasesf2` audited every HTML page, `style.css`, and `scripts/validate_site.py` from PR #1 (`3eac9d0e`) and PR #2 (`81e8c938`) line by line against primary government sources and user requirements:

1. **Correction of `April 1, 2026` Intake Semantics (`units.html`, `analysis.html`, `executive-summary.html`, `flagged.html`):** PR #2 treated `April 1, 2026` as a "proposed rent-increase effective date." In fact, today is `2026-11-06` (`November 6, 2026`), and `April 1, 2026 @ $3,995/month` was the historical continuing-tenancy / co-tenant change date (`Tenant 1A` continuing original tenant + `Tenant 1D`). Consequently: (a) under `Rules § 6.14` and `Civ. Code § 1954.53(d)`, original occupant `Tenant 1A` blocks any Costa-Hawkins market reset; (b) if `April 1, 2026` created a new 12-month fixed-term lease through `March 31, 2027`, `Civ. Code § 827(a)` bars any unilateral increase before `April 1, 2027` (flagged `needs review`); and (c) if month-to-month, any new `30/35-day` notice served on or after `2026-11-06` takes effect prospectively in `December 2026 / January 2027` (`1.6%` = `$63.92` → `$4,058.92`), or `February 1, 2027` (`24` months → `1.4% + 1.6% = 3.0%` = `$119.85` → `$4,114.85`).
2. **Restoration of Explicit Anonymized Placeholder Names:** The user explicitly requested placeholder names on the website while keeping dates and dollar amounts exact. PR #2 replaced placeholders with generic prose ("Three original tenants (names withheld)"). Integrated pages use explicit zero-PII placeholders: `Tenant 1A`, `Tenant 1B`, `Tenant 1C` (Unit 1 initial), `Tenant 1A` + `Tenant 1D` (Unit 1 current), and `Tenant 2A`, `Tenant 2B` (Unit 2).
3. **Verified Official Sources on Corporate vs. Individual Owner Practices (`practices.html`):** PR #2 stated that no official source documented corporate rent-setting distinctions. Session `39ba7aa1` verified primary municipal and federal enforcement records: (a) **SF Admin. Code § 37.10C (Ord. 207-24)** banning corporate algorithmic rent-setting software in San Francisco (`sf.gov` & `codelibrary.amlegal.com`), (b) **U.S. DOJ Antitrust Division** civil lawsuits and consent decrees against RealPage and six major corporate landlords (`justice.gov`), and (c) **SF Rent Board FY 2024–2025 Annual Statistical Report** & **Forms Center** (`Form 516D`, `Form 538`, `Form 542`, `1,261` capital improvement petition units across `209` petitions, `849` utility passthrough units, `99,800` Housing Inventory licenses). Meanwhile, exact CPI-imposition rates split by corporate vs. individual ownership are not tabulated by the Rent Board and remain explicitly blank/unverified.
4. **ZIP Code `94122` (Sunset) Official Municipal Data & Official SF County AB 1482 `8.8%` Cap:** Added official SF Rent Board FY 2024–2025 ZIP `94122` statistics (`42` tenant petitions — 6th highest of 24 SF ZIPs; `15` capital improvement petitions; `14` wrongful eviction reports) and the California Attorney General's official `8.8%` SF County AB 1482 cap (`8/1/2026–7/31/2027`, `oag.ca.gov/rentcaps`) superseded by SF's stricter `1.6%` cap.
5. **Unit 2 Anniversary-Date Forfeiture Trap (`March 1 – May 31, 2027`):** Highlighted the urgent `2026-11-06` calendar window: a `95-day` mailed notice from `2026-11-06` lands on `February 9, 2027` (`≤ 2/28/2027`), preserving `13.1%` (`$412.65`), whereas shifting the effective date into `March 1 – May 31, 2027` permanently forfeits Unit 2's `June 1, 2026` (`1.6%`) allowance under `Topic 503`.
6. **Strict Blank Cells for Unverified Official Values:** Added explicit blank (`—` / empty) official-record cells for every unconfirmed property/intake field while keeping supplied intake numbers clearly separated and flagged on `flagged.html`.

---

## Preserved Task Board & Logs from Prior Sessions (`arena/3eac9d0e-rentincreasesf2` & `arena/81e8c938-rentincreasesf2`)

### Preserved Task Board (`arena/3eac9d0e-rentincreasesf2` & `session-arena-81e8c938`)

| # | Task | Status | Owner session | File scope | Sources / verification notes |
|---|---|---|---|---|---|
| 1 | Research & verify SF/state/federal rent increase rules from official sources | `done` | `arena/3eac9d0e-rentincreasesf2` | `COORDINATION.md`, site pages | Preserved below. |
| 2 | Executive summary (anonymized) | `done` | `arena/3eac9d0e-rentincreasesf2` | `executive-summary.html` | Re-verified and expanded by `81e8c938` and `39ba7aa1`. |
| 3 | Unit data (anonymized, dates/amounts preserved) | `done` | `arena/3eac9d0e-rentincreasesf2` | `units.html` | Re-verified and expanded by `81e8c938` and `39ba7aa1`. |
| 4 | Laws & regulations reference with official source links | `done` | `arena/3eac9d0e-rentincreasesf2` | `laws.html` | Re-verified and expanded by `81e8c938` and `39ba7aa1`. |
| 5 | Notice process & fairness guidance | `done` | `arena/3eac9d0e-rentincreasesf2` | `process.html` | Corrected and expanded by `81e8c938` and `39ba7aa1`. |
| 6 | Increase calculations for both units | `done` | `arena/3eac9d0e-rentincreasesf2` | `analysis.html` | Banked calculation added by `81e8c938`; timing & forfeiture analysis added by `39ba7aa1`. |
| 7 | GitHub Pages site (dashboard UI) + Flagged for Review page | `done` | `arena/3eac9d0e-rentincreasesf2` | `index.html`, `*.html`, `style.css` | Expanded by `81e8c938` and `39ba7aa1`. |
| 8 | PR to main, merge, confirm Pages deploy | `done` | `arena/3eac9d0e-rentincreasesf2` | — | PR #1 merged (`1e6f88f`). |
| 9 | Review and remediation of live site | `done` | `session-arena-81e8c938` | all site files | Corrected legal accuracy, added missing required pages, replaced non-official source labels, and added unit-specific banked analysis. |
| 10 | Add GitHub Actions validation workflow and validation script | `done` | `session-arena-81e8c938` | `.github/workflows/validate.yml`, `scripts/validate_site.py` | Validation checks internal links, external allowlist, table source links, and personal identifiers. |
| 11 | Final verification, PR, and merge (`81e8c938`) | `done` | `session-arena-81e8c938` | all files | PR #2 merged (`153b260`); Pages build succeeded; live site re-verified. |

### Preserved PR #2 & PR #3 Review Record (`session-arena-81e8c938`)
- **PR #2:** https://github.com/kanlerxz87-cyber/RentincreaseSF2/pull/2 (`153b260def7651b2860205bb8eaa646bd3a38227`, merged `2026-11-06T13:36:39Z`; `Validate site` run `42226838919` passed; GitHub Pages run `42226890108` `built`).
- **PR #3 Review (`arena/77623c60-rentincreasesf2`):** Closed without merging by `81e8c938` because PR #3 published raw tenant initials on the public site (redacted here to preserve strict privacy), conflicted on Unit 1's 24-month banking date, included `.pyc` build artifacts, and proposed a duplicate 14-page structure. Work remains preserved on its branch.

### Preserved Verification Log (`arena/3eac9d0e-rentincreasesf2`)
- SF Rent Board current rates: `1.6%` (`3/1/2026–2/28/2027`), `1.4%` (`3/1/2025–2/28/2026`), `1.7%` (`3/1/2024–2/28/2025`) — https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit
- Rent increase rules (`12-month` rule, `30/90-day` notice, rent increase license, `60%` CPI formula) — https://www.sf.gov/learn-about-rent-increases-san-francisco
- Banked rent increases — https://www.sf.gov/information--banked-rent-increases
- CA Civil Code `§ 1947.12` (AB 1482) — https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1947.12.
- CA Civil Code `§ 827` (`30/90-day` notice) — https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=827.
- Federal Fair Housing Act, `42 U.S.C. § 3604` — https://www.hud.gov/reporthousingdiscrimination and https://www.govinfo.gov/content/pkg/USCODE-2024-title42/html/USCODE-2024-title42-chap45.htm

### Preserved Verification Log (`session-arena-81e8c938`)
- Checked 41 official URLs across `sf.gov`, `leginfo.legislature.ca.gov`, `calcivilrights.ca.gov`, `hud.gov`, `govinfo.gov`, `sfplanninggis.org`, `sfassessor.org`, and `portal.sfrb.org` (full list in `sources.html` and `scripts/validate_site.py`).
- Verified Unit 1 `$3,995 × 1.6% = $63.92 → $4,058.92` (`Feb 1, 2027`: `3.0% = $119.85 → $4,114.85`) and Unit 2 `11.5% + 1.6% = 13.1%` (`$3,150 × 13.1% = $412.65 → $3,562.65`).

### Additional Primary Official Sources Verified by `arena/39ba7aa1-rentincreasesf2` (`T1`–`T5`)
- SF Rent Board 2026–27 Announcement (`1.6%`) — https://www.sf.gov/news--annual-rent-increase-3126-22827-announced
- SF Rent Board Form 571 Direct PDF — https://media.api.sf.gov/documents/571_Allowable_Annual_Increases_26-27_1.pdf
- SF Rent Board FY 2024–2025 Annual Statistical Report (ZIP `94122` filings & citywide passthrough/petition volume) — https://media.api.sf.gov/documents/Rent_Board_Annual_Statistical_Report_FY2024-2025.pdf
- SF Rent Board Commission Minutes (`99,800` Housing Inventory licenses) — https://media.api.sf.gov/documents/minutes_040825.pdf
- SF Rent Board `Rules § 6.14` & Costa-Hawkins Co-Tenant Rules — https://www.sf.gov/information--rent-increases-under-section-614-and-costa-hawkins
- SF Rent Board Official Forms Center (`Forms 516D, 538, 542, 524a`) — https://www.sf.gov/rent-board-forms-forms-center
- SF Ordinance 207-24 (`SF Admin. Code § 37.10C`) Banning Algorithmic Rent-Setting — https://www.sf.gov/news--new-law-prohibits-algorithmic-devices-used-set-rents-san-francisco
- SF Administrative Code Chapter 37 Official Text — https://codelibrary.amlegal.com/codes/san_francisco/latest/sf_admin/0-0-0-70881
- California Attorney General Official 2026–2027 AB 1482 Rent Caps (`8.8%` SF County) — https://oag.ca.gov/rentcaps and https://oag.ca.gov/tenants
- California Code of Civil Procedure `§ 1013` (`+5` calendar days for mail service) — https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1013.&lawCode=CCP
- California Civil Code `§ 1942.5` (`180-day` anti-retaliation statute) — https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1942.5.&lawCode=CIV
- California Government Code `§ 12955` (FEHA housing discrimination) — https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=GOV&sectionNum=12955.
- California Civil Code `§ 51` (Unruh Civil Rights Act) — https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=51.
- California Civil Code `§ 1954.52` (Costa-Hawkins) — https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1954.52
- U.S. HUD Fair Housing Act Substantive Overview — https://www.hud.gov/helping-americans/fair-housing-act-overview
- U.S. DOJ Antitrust Suit Against Six Large Corporate Landlords — https://www.justice.gov/archives/opa/pr/justice-department-sues-six-large-landlords-algorithmic-pricing-scheme-harms-millions
- U.S. DOJ RealPage Algorithmic Pricing Consent Decree — https://www.justice.gov/opa/pr/justice-department-requires-realpage-end-sharing-competitively-sensitive-information-and

---

## Coordination & Merge Conflict Event Log

- `2026-11-06T13:19:00Z` — Session `arena/39ba7aa1-rentincreasesf2` initialized `COORDINATION.md` from `3ed3b19` and completed `T1`–`T5` (`docs/research-local-sf.md`, `docs/research-state-federal-market.md`, `docs/analysis-practices-lawyer-audit.md`, `docs/unit-calculations-and-flags.md`, `docs/executive-summary.md`, `data/verified-data.json`).
- `2026-11-06T13:19:14Z` — Session `arena/3eac9d0e-rentincreasesf2` merged PR #1 (`1e6f88f`) to `main`.
- `2026-11-06T13:36:15Z` — Session `arena/81e8c938-rentincreasesf2` merged PR #2 (`153b260`) to `main`.
- `2026-11-06T13:45:00Z` — **Merge Conflict Resolution Logged:** Session `arena/39ba7aa1-rentincreasesf2` merged `origin/main` (`153b260`) into `arena/39ba7aa1-rentincreasesf2`. Stopped at the `add/add` conflict in `COORDINATION.md`, resolved it without discarding any work from `arena/3eac9d0e-rentincreasesf2` or `arena/81e8c938-rentincreasesf2`, and preserved all prior task boards, source lists, and validation logs above. Proceeding with `T6` final integration upgrades across the 10-page site and `scripts/validate_site.py`.
