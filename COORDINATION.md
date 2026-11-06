# COORDINATION.md — Shared Task Board & Verification Log

**Repository:** `kanlerxz87-cyber/RentincreaseSF2`  
**Privacy Policy:** Strict anonymization active. Zero personal names, initials, or street addresses may appear anywhere in this file, commits, pull requests, data files, or website pages. Placeholder identifiers (`Tenant 1A`–`Tenant 1D`, `Tenant 2A`–`Tenant 2B`) are used exclusively while preserving exact lease dates and dollar amounts.

---

## Shared Task Board

| Task ID | Task Description | Status | Owning Session ID | Claimed At (UTC) | File Scope |
|---|---|---|---|---|---|
| `T1` | Official Source Verification: SF Local Law (Admin Code Ch. 37, SF Rent Board Annual Rates 2019–2027, Banking Rules, Housing Inventory License, Co-Tenant/Subtenant Rules) | `done` | `arena/39ba7aa1-rentincreasesf2` | `2026-11-06T13:19:00Z` | `docs/research-local-sf.md` |
| `T2` | Official Source Verification: CA State Law (Costa-Hawkins, AB 1482, Civ. Code § 827, CCP §§ 1013/1162, FEHA, Unruh, Civ. Code § 1942.5), Federal Law (FHA, SCRA, CARES, DOJ), & ZIP 94122 Official Data | `done` | `arena/39ba7aa1-rentincreasesf2` | `2026-11-06T13:25:00Z` | `docs/research-state-federal-market.md` |
| `T3` | Corporate vs. Individual Landlord Practices, Proper Rent Increase Notice Protocol, SF Tenant Lawyer Scrutiny Standards, & Single-Unit vs. Both-Units Fair Housing Analysis | `in progress` | `arena/39ba7aa1-rentincreasesf2` | `2026-11-06T13:31:00Z` | `docs/analysis-practices-lawyer-audit.md` |
| `T4` | Anonymized Unit 1 & Unit 2 Rent Calculations, Executive Summary, & Irregularities / Unverified Items Audit | `unclaimed` | — | — | `docs/unit-calculations-and-flags.md`, `docs/executive-summary.md` |
| `T5` | Verified Structured Dataset & Line-by-Line Official Source Registry | `unclaimed` | — | — | `data/verified-data.json` |
| `T6` | GitHub Pages Clean Dashboard Website (Landing Page + Category Subpages + Flagged for Review Page) | `unclaimed` | — | — | `.nojekyll`, `index.html`, `executive-summary.html`, `legal-framework.html`, `unit-analysis.html`, `landlord-practices.html`, `notice-and-compliance.html`, `lawyer-scrutiny.html`, `flagged-for-review.html`, `assets/styles.css`, `assets/app.js`, `README.md` |
| `T7` | Final Integration, Line-by-Line Re-Verification, Broken-Link & PII Automated Checks, PR Creation, Merge to `main`, & GitHub Pages Deployment Confirmation | `unclaimed` | — | — | `scripts/verify_site.py`, `COORDINATION.md` |

---

## Verification & Irregularities Log

### `T1` — SF Local Rent Control & Municipal Law (`done`)
- **Session:** `arena/39ba7aa1-rentincreasesf2`
- **Verification Performed:** Verified line-by-line against official SF.gov Rent Board publications, Form 571 (2026–2027 edition), and American Legal Publishing SF Administrative Code Chapter 37 (`§§ 37.2, 37.3, 37.8, 37.9, 37.10B, 37.10C, 37.15`). Confirmed every annual allowable rate from `3/1/2019` (`2.6%`) through `3/1/2026–2/28/2027` (`1.6%`), Housing Inventory Rent Increase License mandate (`§ 37.15`), simple-addition banking rules (`Topic 503`), and co-tenant/original-occupant rules (`Rules § 6.14`).
- **Official Sources Linked:**
  - https://www.sf.gov/news--annual-rent-increase-3126-22827-announced
  - https://media.api.sf.gov/documents/571_Allowable_Annual_Increases_26-27_1.pdf
  - https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit
  - https://www.sf.gov/learn-about-rent-increases-san-francisco
  - https://www.sf.gov/information--banked-rent-increases
  - https://www.sf.gov/rent-board-housing-inventory
  - https://www.sf.gov/notice-of-owner-noncompliance-with-housing-inventory
  - https://www.sf.gov/information--rent-increases-under-section-614-and-costa-hawkins
  - https://www.sf.gov/rent-board-fee
  - https://www.sf.gov/landlord-petitions-and-passthroughs
  - https://www.sf.gov/news--new-law-prohibits-algorithmic-devices-used-set-rents-san-francisco
  - https://codelibrary.amlegal.com/codes/san_francisco/latest/sf_admin/0-0-0-70881
  - https://codelibrary.amlegal.com/codes/san_francisco/latest/sf_admin/0-0-0-16540
- **Flagged Irregularities (`needs review`):**
  1. **Future 3/1/2027–2/29/2028 SF Rent Board Rate Unannounced:** Left blank/unverified because SF Rent Board announces the March 1, 2027 rate in January 2027.
  2. **Unit 1 April 1, 2026 Lease/Addendum Structure (`Tenant 1A` + `Tenant 1D`):** Original occupant `Tenant 1A` remains in Unit 1 (blocking any Costa-Hawkins/§ 6.14 market reset), and if `Tenant 1D` signed a direct lease agreement on April 1, 2026, two critical items require owner document verification: (a) whether a new 12-month fixed-term lease was executed through March 31, 2027 (which bars unilateral rent increases mid-term), and (b) whether a timely written `§ 6.14` reservation notice was served within 60 days.
  3. **Housing Inventory Rent Increase License Status (`§ 37.15`):** Property-specific license status on `portal.sfrb.org` cannot be verified without the street address/APN (withheld for strict privacy) and is flagged for owner verification prior to serving any notice.

### `T2` — CA State Law, Federal Law, & ZIP Code 94122 Official Data (`done`)
- **Session:** `arena/39ba7aa1-rentincreasesf2`
- **Verification Performed:** Verified California statutory text on `leginfo.legislature.ca.gov` (`Civ. Code §§ 51, 827, 1942.5, 1947.12, 1954.52, 1954.53`; `CCP § 1013`; `Gov. Code § 12955`), California Attorney General 2026–2027 AB 1482 rent-cap table (`8.8%` SF County statewide cap superseded by stricter `1.6%` SF local cap), California Civil Rights Department housing guidance, U.S. HUD Fair Housing Act overview (`42 U.S.C. §§ 3601–3619`), U.S. DOJ Antitrust Division actions on corporate algorithmic rent-setting, and SF Rent Board FY 2024–2025 Annual Statistical Report ZIP `94122` tables (`42` tenant petitions, `15` capital improvement petitions, `14` wrongful eviction reports).
- **Official Sources Linked:**
  - https://oag.ca.gov/rentcaps
  - https://oag.ca.gov/tenants
  - https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=827.
  - https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1947.12.
  - https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1954.52
  - https://leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?chapter=2.7.&division=3.&lawCode=CIV&part=4.&title=5.
  - https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1013.&lawCode=CCP
  - https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1942.5.&lawCode=CIV
  - https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=GOV&sectionNum=12955.
  - https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=51.
  - https://calcivilrights.ca.gov/housing/
  - https://www.hud.gov/helping-americans/fair-housing-act-overview
  - https://www.govinfo.gov/content/pkg/USCODE-2024-title42/html/USCODE-2024-title42-chap45.htm
  - https://www.justice.gov/archives/opa/pr/justice-department-sues-six-large-landlords-algorithmic-pricing-scheme-harms-millions
  - https://www.justice.gov/opa/pr/justice-department-requires-realpage-end-sharing-competitively-sensitive-information-and
  - https://media.api.sf.gov/documents/Rent_Board_Annual_Statistical_Report_FY2024-2025.pdf
- **Flagged Irregularities (`needs review`):**
  1. **Unit Bedroom Counts & `94122` Private Market Comparables:** Unit 1 and Unit 2 bedroom/bathroom counts were not supplied in internal data, and official municipal/federal tables do not publish a 2026 private-listing median rent by bedroom for ZIP `94122`; left blank rather than estimated from third-party listing sites.
  2. **Repo Audit of `origin/main` (PR #1 from `arena/3eac9d0e-rentincreasesf2`):** Observed `origin/main` advanced to `1e6f88f`; audited line-by-line and noted (a) complete omission of Corporate vs. Individual landlord inquiry, (b) 10 table rows across `units.html` and `analysis.html` missing official source links, (c) placeholder mismatch (`Tenant A–E` vs `Tenant A–F`), and (d) redirection of legacy HUD link `hud.gov/program_offices/fair_housing_equal_opp` to `hud.gov/contactus/fairhousing` instead of `hud.gov/helping-americans/fair-housing-act-overview`. All items logged for non-destructive integration in `T6`/`T7`.

---

## Coordination & Merge Event Log

- `2026-11-06T13:19:00Z` — Session `arena/39ba7aa1-rentincreasesf2` initialized `COORDINATION.md` after checking repo root (`README.md` only on `main` at `3ed3b19`) and claimed `T1` (`docs/research-local-sf.md`).
- `2026-11-06T13:25:00Z` — Session `arena/39ba7aa1-rentincreasesf2` completed `T1` with full primary-source verification and claimed `T2` (`docs/research-state-federal-market.md`).
- `2026-11-06T13:31:00Z` — Session `arena/39ba7aa1-rentincreasesf2` completed `T2`, logged line-by-line audit of `origin/main` (`1e6f88f`), and claimed `T3` (`docs/analysis-practices-lawyer-audit.md`).
