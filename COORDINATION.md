# COORDINATION.md — Shared Task Board

**Repo:** `kanlerxz87-cyber/RentincreaseSF2`  
**Live site:** https://kanlerxz87-cyber.github.io/RentincreaseSF2/  
**Last updated:** 2026-11-07

## Sessions

| Session ID | Role | Status |
|---|---|---|
| `arena/3eac9d0e-rentincreasesf2` | Original build session | Completed tasks 1–8; merged PR #1; site deployed. Work preserved. |
| `session-arena-81e8c938` (this session) | Review, remediation, verification, and final integration | In progress. Reviewing the live site line by line, correcting legal accuracy, adding missing required pages, and re-verifying all sources. |
| `arena/fa7d2d77-rentincreasesf2` (this session) | Final integration: take over stale PR #5, port its verified findings, re-verify line by line, extend the live site, PR + merge + deploy | **IN PROGRESS** — claimed 2026-11-07. |

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
| 9 | Review and remediation of live site | done | session-arena-81e8c938 | all site files | Corrected legal accuracy, added missing required pages, replaced non-official source labels, and added unit-specific banked analysis. |
| 10 | Add GitHub Actions validation workflow and validation script | done | session-arena-81e8c938 | `.github/workflows/validate.yml`, `scripts/validate_site.py` | Validation checks internal links, external allowlist, table source links, and personal identifiers. GitHub Pages remains on the repository's existing legacy build from `main`; the workflow is a check, not a second deploy path. |
| 11 | Final verification, PR, and merge | done | session-arena-81e8c938 | all files | PR #2 merged; Pages build succeeded; live site re-verified. |
| 12 | Clarify individual-owner Housing Inventory/license and Rent Board notice timing | done | arena/795a54b7-rentincreasesf2 | index.html, executive-summary.html, process.html, practices.html, COORDINATION.md | Directly rechecked SF Rent Board Housing Inventory, rent increase, noncompliance, and counselor pages on 2026-11-07. All owners report; tenant-occupied units receive a license; current license is needed before effective date; license need not accompany tenant notice. Official guidance describes tenant notice and annual Housing Inventory, not a separate Rent Board filing for each increase. Safe sequencing advice is labeled as prudence, not a legal timing requirement. |
| 13 | Take over stale PR #5 (idle >30h) and audit it for privacy, accuracy and mergeability | in progress | arena/fa7d2d77-rentincreasesf2 | COORDINATION.md (audit record only; no PR #5 file is edited on its branch) | Handoff logged below. |
| 14 | Re-verify controlling sources line by line (rates, banking, license, notice, occupancy, retaliation, algorithmic pricing) | in progress | arena/fa7d2d77-rentincreasesf2 | COORDINATION.md verification log | Official sources fetched directly this session. |
| 15 | Add missing verified content: Unit 1 occupancy change, corporate algorithmic-pricing ban, license null-and-void rule, retaliation screen, action checklist | in progress | arena/fa7d2d77-rentincreasesf2 | NEW: occupancy.html, checklist.html, market.html | New files only — no other session owns them. |
| 16 | Reconcile unit calculations to an explicit effective-date scenario table (today = 2026-11-07) | in progress | arena/fa7d2d77-rentincreasesf2 | analysis.html, units.html, index.html, executive-summary.html | Supersedes ambiguous single-number maxima. |
| 17 | Integration: shared nav, sources register, flags, validator allowlist | in progress | arena/fa7d2d77-rentincreasesf2 | all *.html nav blocks, sources.html, flagged.html, scripts/validate_site.py, style.css, README.md | Integration-session prerogative; tasks 1–12 are all `done`. |
| 18 | Final verification, PR to main, merge, confirm Pages deploy | in progress | arena/fa7d2d77-rentincreasesf2 | COORDINATION.md | Pending tasks 13–17. |

## PR and deployment record

- **PR:** https://github.com/kanlerxz87-cyber/RentincreaseSF2/pull/2
- **Merge commit:** `153b260def7651b2860205bb8eaa646bd3a38227`
- **Merged at:** 2026-11-06T13:36:39Z
- **Merge method:** merge commit
- **Validation workflow:** `Validate site` passed on the PR (run 42226838919).
- **GitHub Pages build:** `pages build and deployment` run 42226890108 completed successfully; Pages status `built`.
- **Live site:** https://kanlerxz87-cyber.github.io/RentincreaseSF2/
- **Live pages verified:** `index.html`, `executive-summary.html`, `units.html`, `analysis.html`, `laws.html`, `process.html`, `tenant-protections.html`, `practices.html`, `flagged.html`, `sources.html`, and `style.css` all returned HTTP 200 locally and were re-fetched from the live site after deployment.

## Follow-up PR #6 — license and notice clarification

- **PR:** https://github.com/kanlerxz87-cyber/RentincreaseSF2/pull/6
- **Merge result:** merged to `main` at 2026-11-07T20:43:39Z; merge commit `ea942f3533f0ce181d50ade0a509d020c047415d`.
- **Validation:** PR `Validate site` passed (run 42412404807); post-merge `Validate site` passed (run 42412433323).
- **GitHub Pages:** deployment run 42412432988 completed successfully.
- **Live verification:** fetched the public dashboard and executive summary after deployment; both show the individual-owner answer, distinction between Rent Board reporting and tenant notice, and the effective-date license requirement.

## PR #3 review (session arena/77623c60-rentincreasesf2)

A parallel session opened PR #3, "Rental increase analysis — Outer Sunset SF, ZIP 94122 (verified sources + GitHub Pages site)," while this session was finishing PR #2. PR #3 proposes a 14-page static site with a different structure and a larger source register.

### Review findings

- **Privacy violation (blocking):** PR #3 publishes tenant initials (L O, V N, J P, M T, E R, I S) on the site, including in the privacy section and flagged-items page. The user explicitly required all personal information to be anonymized and said privacy is top priority. Initials are personal information and must not be published. This alone makes PR #3 unacceptable as submitted.
- **Unit 1 calculation conflict:** PR #3 presents $4,114.85 (3.0%) as a maximum for Unit 1 on the February 1, 2026 anniversary, and treats the 1.4% as banked. Under the Rent Board's 24-month banking rule, the 1.4% that became available on February 1, 2026 is not banked until February 1, 2027. For an April 1, 2026 effective date, the maximum is 1.6% ($4,058.92). PR #3's own flagged item F-07 acknowledges the 24-month rule but still presents 3.0% as a lawful outcome for Unit 1 without a clear date qualification. This conflicts with the more conservative analysis in PR #2.
- **Build artifacts:** PR #3 includes `tools/__pycache__/*.pyc` files. These should not be committed.
- **Duplicate/conflicting site:** PR #2 is already merged and live. Merging PR #3 would replace the live site with a different structure and would require a full line-by-line re-verification of all 14 pages.

### Decision

Do not merge PR #3. Close it with a comment explaining the privacy violation, the Unit 1 calculation conflict, and the duplicate-site issue. The work remains preserved on its branch. No files from PR #3 were edited by this session. PR #2 remains the live site.

### Coordination note

The parallel session should be notified that its PR was reviewed and closed. If it wants to contribute, it should open a new PR that removes all initials, uses placeholders only, corrects the Unit 1 analysis, and removes build artifacts. Any new PR must be reviewed against the same privacy and source-verification standard.

## Final verification summary

- `python3 scripts/validate_site.py` passes.
- All 10 HTML pages and `style.css` return HTTP 200 from a local static server.
- HTML tag-balance check passes for all 10 pages.
- Every table data row has at least one official source link.
- No tenant initials or personal identifiers are present in the published HTML.
- All external source links are on the verified official-source allowlist.
- Live site was re-fetched after deployment and shows the remediated content, including the Unit 2 banked calculation and the Flagged for Review page.

## Remaining items for the user to review

The Flagged for Review page lists the items that cannot be confirmed from official sources without additional records. The most important are:
- confirm the 1940 build year and rent-control coverage;
- confirm the lease dates, base rents, and occupancy;
- check the rent increase license in the Rent Board Portal;
- confirm Unit 1's last-increase date and whether the April 1, 2026 increase has been served;
- confirm Unit 1's tenancy status (continuing original tenant vs. new tenancy);
- confirm Unit 2's complete rent history before relying on the 13.1% banked calculation;
- confirm the notice service date for Unit 2's 90-day requirement;
- have a tenant lawyer review the final notice and documentation.

No further code changes are required for the site to be live. The remaining items are factual/legal confirmations that require records not available in the repository.

## Follow-up verification log (2026-11-07)

### Official sources rechecked directly for the license/notice clarification

- SF Rent Board, Housing Inventory — all residential property owners report; tenant-occupied units receive a Rent Increase License; current license must be on file before annual/banked increase takes effect; license need not be included with tenant notice; Housing Inventory data/public-reporting details — https://www.sf.gov/rent-board-housing-inventory
- SF Rent Board, Learn about rent increases — current 1.6% rate for 2026-27, annual allowable increase license requirement, written notice to tenant, notice periods/content — https://www.sf.gov/learn-about-rent-increases-san-francisco
- SF Rent Board, Notice of Owner Noncompliance — annual reporting applies to owners; license requirement applies to rent-controlled annual/banked increases; consequence for increase effective while unlicensed — https://www.sf.gov/notice-of-owner-noncompliance-with-housing-inventory
- SF Rent Board, Banked rent increases — license/effective-date requirement and tenant notice content — https://www.sf.gov/information--banked-rent-increases
- SF Rent Board, Speak with a Rent Board counselor — free counseling, not legal advice — https://www.sf.gov/speak-rent-board-counselor

The official sources do not expressly require a license to be active before the notice is served; they require it before the increase takes effect. Accordingly, the site states the formal effective-date requirement and separately labels checking the license before service as prudent sequencing. The sources describe written notice to tenants and Housing Inventory reporting but do not instruct an owner to separately file each individual increase notice with the Board. This is a statement about the cited official process, not an assertion that no other filing could ever apply to a different petition/passthrough situation.

### Validation performed

- `python3 scripts/validate_site.py` passes: all 10 pages, official links, per-table-row source links, privacy scan, and internal links.
- `git diff --check` passes.
- Changed only `index.html`, `executive-summary.html`, `process.html`, `practices.html`, and this coordination log.

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


---

## Session `arena/fa7d2d77-rentincreasesf2` — claim and handoff (2026-11-07)

### Claim

This session claims tasks 13–18 above and is acting as the **final integration session**. All
prior tasks (1–12) are recorded `done`, so no in-progress claim is being displaced. File scope
is listed per task on the board above.

### Branch-name deviation (platform constraint)

The task protocol asks for branches named `session-<id>/<task>`. This session runs on a
platform-managed branch, `arena/fa7d2d77-rentincreasesf2`, which is fixed and cannot be renamed
or switched. All work is committed to that branch and the pull request is opened from it. This
is the same convention already used by sessions `arena/3eac9d0e`, `arena/81e8c938` and
`arena/795a54b7`, so the board remains consistent.

### Handoff: PR #5 taken over under the 60-minute stale-claim rule

- **PR:** https://github.com/kanlerxz87-cyber/RentincreaseSF2/pull/5
- **Owning session:** `arena/48ffb5b4-rentincreasesf2`
- **Last activity:** 2026-11-06T14:09:21Z — more than 30 hours before this session started, with
  no commits in that window. The protocol permits any other session to take over a claim that
  is more than 60 minutes old with no commits. The takeover is recorded here.
- **Audit performed before takeover:**
  - **Privacy: PASS.** Swept all 34 files for the six supplied tenant initial pairs and for
    `JP`. No tenant initials, names, addresses or contact details are published. The branch
    uses `Tenant A`–`Tenant D` placeholders and preserves dates and dollar amounts.
  - **Build: PASS.** `python3 build.py` exits 0 in a clean extraction: 15 HTML documents,
    256 external links, 48 sources, 24 flags, 11 dollar checks and 8 deadline checks, Census
    reconciliation, PII guard clean.
  - **Mergeability: FAIL as a direct merge.** `git merge-base HEAD refs/pr/5` is empty and
    `git merge-tree` reports `refusing to merge unrelated histories`. PR #5 was authored on an
    orphan history that shares no ancestor with `main`. It also re-adds `index.html`,
    `README.md`, `COORDINATION.md` and `.nojekyll`, which already exist on `main` with three
    sessions of accumulated work.
- **Decision:** do **not** force an unrelated-history merge, because that would risk discarding
  the work of sessions `arena/3eac9d0e`, `arena/81e8c938` and `arena/795a54b7` and would publish
  two competing sites at overlapping URLs. Instead this session **ports PR #5's verified
  findings into the live site**, re-verifying each one against the official source first, and
  credits the originating session on the Sources page. PR #5's branch and commits are left
  untouched and preserved.
- **Findings adopted for re-verification (not accepted on trust):** Rent Ordinance § 37.10C
  algorithmic pricing ban; Rules § 13.14 licensing / null-and-void; Rules § 6.14 and
  Costa-Hawkins original-occupant limit; § 37.3 additional-occupant prohibition;
  Civ. Code § 1942.5 retaliation screen; Civ. Code § 1947.12 AB 1482 non-application.
- **Findings corrected on re-verification:** PR #5 states Unit 2's full 13.1% is first
  available on 2027-06-01 and that "nothing can lawfully be done today". Re-verification
  against the Rent Board's own off-anniversary worked examples shows the 13.1% is available
  on an earlier effective date, and that a notice can be served now. See the verification log
  below. PR #5's Flag F-03 (12 vs 24 months) is also resolved rather than left as a conflict.
