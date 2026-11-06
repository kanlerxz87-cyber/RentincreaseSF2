# COORDINATION.md — Shared Task Board

**Repo:** `kanlerxz87-cyber/RentincreaseSF2`  
**Live site:** https://kanlerxz87-cyber.github.io/RentincreaseSF2/  
**Last updated:** 2026-11-06

## Sessions

| Session ID | Role | Status |
|---|---|---|
| `arena/3eac9d0e-rentincreasesf2` | Original build session | Completed tasks 1–8; merged PR #1; site deployed. Work preserved. |
| `session-arena-81e8c938` (this session) | Review, remediation, verification, and final integration | In progress. Reviewing the live site line by line, correcting legal accuracy, adding missing required pages, and re-verifying all sources. |

## Coordination note / handoff

The original session (`arena/3eac9d0e-rentincreasesf2`) created the first site and merged PR #1. This session reviewed the live site and found several items that need remediation before the site can be treated as final:

- Unit 2 was analyzed only at the current 1.6% annual allowance; the banked-increase calculation (11.5% banked + 1.6% current = 13.1%) was flagged but not calculated.
- The site said to apply the "same allowable percentage" to both units. That is not correct: each unit has its own base rent and rent history, and Unit 2 may have banked increases. The lawful analysis is unit-specific.
- Some table rows used "Provided data" or "Calculation" instead of an official source link. These are being replaced with official verification-method links and explicit "unverified" labels.
- The site did not include a dedicated tenant-protections page, a corporate-vs-individual-owner practices page, a consolidated sources page, or a GitHub Actions deployment workflow.
- The site did not clearly state that a tenant lawyer's approval cannot be guaranteed and that "normal business practice" is not defined by official sources beyond the Rent Board formula.

This session is editing the existing files rather than creating a duplicate site. No work from the original session is discarded. The original session's verification log is preserved below.

## Task board

| # | Task | Status | Owner session | File scope | Sources / verification notes |
|---|---|---|---|---|---|
| 1 | Research & verify SF/state/federal rent increase rules from official sources | done | arena/3eac9d0e-rentincreasesf2 | COORDINATION.md, site pages | See original verification log below. |
| 2 | Executive summary (anonymized) | done | arena/3eac9d0e-rentincreasesf2 | executive-summary.html | Re-verified and expanded by this session. |
| 3 | Unit data (anonymized, dates/amounts preserved) | done | arena/3eac9d0e-rentincreasesf2 | units.html | Re-verified and expanded by this session. |
| 4 | Laws & regulations reference with official source links | done | arena/3eac9d0e-rentincreasesf2 | laws.html | Re-verified and expanded by this session. |
| 5 | Notice process & fairness guidance | done | arena/3eac9d0e-rentincreasesf2 | process.html | Corrected by this session; unit-specific analysis added. |
| 6 | Increase calculations for both units | done | arena/3eac9d0e-rentincreasesf2 | analysis.html | Re-verified and expanded by this session with banked calculation. |
| 7 | GitHub Pages site (dashboard UI) + Flagged for Review page | done | arena/3eac9d0e-rentincreasesf2 | index.html, *.html, style.css | Re-verified and expanded by this session. |
| 8 | PR to main, merge, confirm Pages deploy | done | arena/3eac9d0e-rentincreasesf2 | — | PR #1 merged; Pages build succeeded. |
| 9 | Review and remediation of live site | in progress | session-arena-81e8c938 | all site files | Correct legal accuracy, add missing required pages, replace non-official source labels. |
| 10 | Add GitHub Actions validation workflow and validation script | done | session-arena-81e8c938 | `.github/workflows/validate.yml`, `scripts/validate_site.py` | Validation checks internal links, external allowlist, table source links, and personal identifiers. GitHub Pages remains on the repository's existing legacy build from `main`; the workflow is a check, not a second deploy path. |
| 11 | Final verification, PR, and merge | pending | session-arena-81e8c938 | all files | Re-verify combined data, check links, confirm Pages deploy, create and merge PR. |

## Original verification log (preserved from session arena/3eac9d0e-rentincreasesf2)

- SF Rent Board current rates: 1.6% allowable increase for 3/1/2026–2/28/2027 (1.4% for 3/1/2025–2/28/2026; 1.7% for 3/1/2024–2/28/2025) — https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit
- Rent increase rules (once per 12 months, 30-day notice / 90-day if >10%, rent increase license, 60% of Bay Area CPI formula) — https://www.sf.gov/learn-about-rent-increases-san-francisco
- Banked rent increases (no limit, do not expire during tenancy, notice must state banked portion) — https://www.sf.gov/information--banked-rent-increases
- CA Civil Code §1947.12 (AB 1482: 5% + regional CPI, max 10% in 12 months) — https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1947.12.
- CA Civil Code §827 (30/90-day notice) — https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=827.
- Federal Fair Housing Act, 42 U.S.C. §3604 (7 protected classes; terms/conditions discrimination prohibited) — https://www.hud.gov/reporthousingdiscrimination and https://www.govinfo.gov/content/pkg/USCODE-2024-title42/html/USCODE-2024-title42-chap45.htm

## This session's verification log (2026-11-06)

### Official sources checked directly

- SF Rent Board, "Learn about rent increases in San Francisco" — 1.6% for 3/1/2026–2/28/2027; 12-month rule; 30/90-day notice; license; base rent; additional occupants; anniversary date; use percentage in effect on date of increase — https://www.sf.gov/learn-about-rent-increases-san-francisco
- SF Rent Board, "Current Rates" — 1.6% for 3/1/2026–2/28/2027; 1.4% for 3/1/2025–2/28/2026; 1.7% for 3/1/2024–2/28/2025 — https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit
- SF Rent Board, "571 Allowable Annual Increases" PDF — full historical table: 2025–26 1.4%; 2024–25 1.7%; 2023–24 3.6%; 2022–23 2.3%; 2021–22 0.7%; 2020–21 1.8%; 2019–20 2.6% — https://www.sf.gov/documents/34344/571_Allowable_Annual_Increases_26-27_1.pdf
- SF Rent Board, "Banked rent increases" — skipped increase banked only if at least 24 full months pass; no limit; not compounded; not rounded up; do not carry over to a new tenant; license and notice requirements — https://www.sf.gov/information--banked-rent-increases
- SF Rent Board, "Increasing rents during irregular periods" — 12–24 months and 24+ months examples; option to impose current allowable or wait for anniversary to stack — https://www.sf.gov/information--increasing-rents-during-irregular-periods
- SF Rent Board, "Annual rent increase for multiple years" — add prior allowable percentages; no compounding; no rounding up — https://www.sf.gov/information--annual-rent-increase-multiple-years
- SF Rent Board, Rules and Regulations Part IV, §4.12 — banking rule text — https://www.sf.gov/reports--december-2022--rent-board-rules-and-regulations-part-iv-rent-increases-not-requiring
- SF Rent Board, Rent Ordinance §37.3 — annual increase, banking, capital improvements, utilities, notice — https://www.sf.gov/information--sec-373-rent-limitations
- SF Rent Board, "The Rent Ordinance" — official table of contents and complete ordinance PDF — https://www.sf.gov/reports--rent-ordinance
- SF Rent Board, "Housing Inventory" — license required; reporting deadline; portal — https://www.sf.gov/rent-board-housing-inventory
- SF Rent Board, "Notice of Owner Noncompliance" — unlicensed increase may be null and void; tenant refund — https://www.sf.gov/notice-of-owner-noncompliance-with-housing-inventory
- SF Rent Board, "Landlord Petitions and Passthroughs" — six petition types; above-cap process — https://www.sf.gov/landlord-petitions-and-passthroughs
- SF Rent Board, "Learn about San Francisco rental laws" — coverage; just cause; exemptions — https://www.sf.gov/learn-about-san-francisco-rental-laws
- SF Rent Board, "Partial Exemption for Newly Constructed Rental Units" — post-6/13/1979 exemption — https://www.sf.gov/information--partial-exemption-newly-constructed-rental-units
- SF Rent Board, "Partial Exemption for Certain Single-Family Homes and Condominiums Under Costa-Hawkins" — condo/SF exemption — https://www.sf.gov/information--partial-exemption-certain-single-family-homes-and-condominiums-under-costa-hawkins
- SF Rent Board, "Evictions in San Francisco" — just cause; eviction process; tenant help — https://www.sf.gov/evictions-san-francisco
- SF Rent Board, "Speak with a Rent Board counselor" — free counseling; no legal advice — https://www.sf.gov/speak-rent-board-counselor
- SF Rent Board, "Tenant and Landlord Resources" — free tenant counseling and legal help — https://www.sf.gov/tenant-and-landlord-resources
- SF Rent Board, "Tenant Petitions" — unlawful rent increase; lawful rent determination; no filing charge — https://www.sf.gov/tenant-petitions
- SF Rent Board, "Tenant Summary Petitions" — challenge pending increase — https://www.sf.gov/information--tenant-summary-petitions
- SF Rent Board, "About Rent Board" — cannot adjudicate discrimination/retaliation; contact SF Human Rights Commission — https://www.sf.gov/departments--rent-board--about
- SF Rent Board, "The California Tenant Protection Act of 2019 (AB 1482)" — state cap; interaction with local law — https://www.sf.gov/reports--california-tenant-protection-act-2019-ab-1482
- SF Rent Board, "Rent Board Fee" — fee and deadline — https://www.sf.gov/rent-board-fee
- SF Rent Board, "Capital Improvement Petitions" — above-cap reason; process — https://www.sf.gov/information--capital-improvement-petitions
- SF Rent Board, "Operating and Maintenance Expense Petitions" — above-cap reason; process — https://www.sf.gov/information/topic-no-322-operating-and-maintenance-expense-petitions
- SF Rent Board, "Special Circumstances Petitions" — above-cap reason; process — https://www.sf.gov/information--special-circumstances-petitions-based-rents-comparable-units
- SF Rent Board, "Utility Passthroughs" — above-cap reason; process — https://www.sf.gov/information--utility-passthroughs-gas-electricity-and-steam-heat
- SF Rent Board, "General Obligation Bond Passthrough Worksheets" — above-cap reason; process — https://www.sf.gov/information--general-obligation-bond-passthrough-worksheets
- SF Rent Board, "Water Revenue Bond Passthroughs" — above-cap reason; process — https://www.sf.gov/information--water-revenue-bond-passthroughs
- California Legislative Information, Civil Code §827 — 30/90-day notice; personal delivery or mail — https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=827.&lawCode=CIV
- California Legislative Information, Civil Code §1947.12 — AB 1482 cap; local law interaction — https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1947.12.&lawCode=CIV
- California Legislative Information, Civil Code §1954.50 — Costa-Hawkins — https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1954.50.&lawCode=CIV
- California Civil Rights Department, "Housing" — state fair housing protected characteristics; discrimination examples — https://calcivilrights.ca.gov/housing/
- HUD, "Report Housing Discrimination" — federal Fair Housing Act protected classes; complaint process; retaliation — https://www.hud.gov/reporthousingdiscrimination
- U.S. Government Publishing Office, 42 U.S.C. Chapter 45 — Fair Housing Act text — https://www.govinfo.gov/content/pkg/USCODE-2024-title42/html/USCODE-2024-title42-chap45.htm
- SF Human Rights Commission / SF.gov, "Get help for discrimination in housing" — local protected classes; complaint process — https://www.sf.gov/information--get-help-discrimination-housing
- SF Assessor / SF Planning, Property Information Map — official property/build-year verification tool — https://sfplanninggis.org/pim/?pub=true
- SF Rent Board Portal — license status and Housing Inventory — https://portal.sfrb.org/

### Validation performed

- `python3 scripts/validate_site.py` passes: 10 pages checked; 41 official source URLs on allowlist; every table data row has an official source link; no tenant initials or personal identifiers found; all internal links resolve.
- Local HTTP check: all 10 HTML pages and `style.css` return HTTP 200 from a local static server.
- HTML tag-balance check: all 10 pages parse with no unclosed or unmatched tags.
- External source links: each URL on the allowlist was checked against an official government or City of San Francisco page during this session.

### Calculations re-verified

- Unit 1: $3,995 × 1.6% = $63.92; new rent $4,058.92. This is the maximum on an April 1, 2026 effective date if the 1.6% rate is in effect. The 1.4% 2025–26 increase is not banked if the increase is imposed before 24 full months have passed; waiting until February 1, 2027 would allow 1.4% + 1.6% = 3.0%, or $119.85, new rent $4,114.85. Source: SF Rent Board irregular-periods page and banked-increases page.
- Unit 2: assumed June 1, 2026 anniversary and no prior increases. Banked: 1.8% (2020–21) + 0.7% (2021–22) + 2.3% (2022–23) + 3.6% (2023–24) + 1.7% (2024–25) + 1.4% (2025–26) = 11.5%. Current 2026–27: 1.6%. Total 13.1%. $3,150 × 13.1% = $412.65; new rent $3,562.65. This is a calculated maximum, not a verified current rent. Source: official 571 table and banked-increases rules.
- Unit 2 notice: 13.1% > 10%, so 90-day written notice is required (plus 5 days if mailed). Source: SF Rent Board and Civil Code §827.
- Unit 1 notice: 1.6% ≤ 10%, so 30-day written notice (plus 5 days if mailed). Source: SF Rent Board and Civil Code §827.

### Irregularities / items flagged for review

- Tenant-provided lease dates, rents, occupancy, and build year are not independently verified from official records. They are marked unverified on the site.
- Rent Board Housing Inventory / rent increase license status is not checked because no address/APN was provided. This is a blocking prerequisite for a lawful increase.
- Unit 2's 13.1% catch-up assumes no prior increases and the same tenants. Any prior increase changes the calculation.
- Unit 1's new occupant and continuing original tenant: banked increases do not carry over to a new tenant; confirm whether any banked amount exists and whether the tenancy is continuing.
- No official source defines "reasonable" or "normal business practice" beyond the Rent Board formula. A tenant lawyer's approval cannot be guaranteed.
- No official source documents a distinct corporate vs. individual owner practice. Both are subject to the same Rent Ordinance.
- No evidence of protected-class discrimination was found, but absence of evidence is not proof. Fair housing review is flagged.
- The site must not be treated as legal advice. The Rent Board counselor page expressly states that it cannot give legal advice.
