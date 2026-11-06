# COORDINATION.md — Shared Task Board

Last updated: 2026-11-06 (session `arena/f376a90e-rentincreasesf2`)

## Session registry

| Session ID | Branch | Started | Status | Scope |
|---|---|---|---|---|
| `arena/3eac9d0e-rentincreasesf2` | `arena/3eac9d0e-rentincreasesf2` | 2026-11-06 | done (PR #1 merged) | v1 site: `index.html`, `units.html`, `laws.html`, `analysis.html`, `process.html`, `executive-summary.html`, `flagged.html`, `style.css` |
| `arena/f376a90e-rentincreasesf2` | `arena/f376a90e-rentincreasesf2` | 2026-11-06 | **in progress** | v2 site rebuild + verification ledger + docs. Reuses v1 filenames as the integration owner of `main` after PR #1. |

## Task Board

| # | Task | Status | Owner session | Files touched |
|---|------|--------|---------------|---------------|
| 1 | v1 site (research, summary, unit table, laws, process, flagged page) built and merged via PR #1 | done | `arena/3eac9d0e-rentincreasesf2` | v1 site files |
| 2 | Line-by-line audit of v1 content against official sources; log every defect | done | `arena/f376a90e-rentincreasesf2` | `COORDINATION.md` (this file) |
| 3 | Canonical data layer with per-row source IDs (`data.js`) | in progress | `arena/f376a90e-rentincreasesf2` | `data.js` |
| 4 | Source register with verified URLs + what each page supports (`docs/sources.md`) | in progress | `arena/f376a90e-rentincreasesf2` | `docs/sources.md` |
| 5 | Executive summary (anonymized) | in progress | `arena/f376a90e-rentincreasesf2` | `executive-summary.html` |
| 6 | Unit register (anonymized placeholders, dates/amounts preserved) | in progress | `arena/f376a90e-rentincreasesf2` | `units.html` |
| 7 | Law matrix: local / state / federal, with source link per row | in progress | `arena/f376a90e-rentincreasesf2` | `laws.html` |
| 8 | Increase math: allowable, banked, and worked examples | in progress | `arena/f376a90e-rentincreasesf2` | `analysis.html` |
| 9 | Process + notice pack + fair-housing / discrimination analysis (one unit vs. both) | in progress | `arena/f376a90e-rentincreasesf2` | `process.html` |
| 10 | Corporate vs. individual-owner practice, with official/primary sources | in progress | `arena/f376a90e-rentincreasesf2` | `owners.html` |
| 11 | Tenant-lawyer review checklist and free-legal-aid directory | in progress | `arena/f376a90e-rentincreasesf2` | `review.html` |
| 12 | Flagged for Review (unverified / needs human decision) | in progress | `arena/f376a90e-rentincreasesf2` | `flagged.html` |
| 13 | Verification report: every URL re-checked, link checker output (`docs/verification.md`) | in progress | `arena/f376a90e-rentincreasesf2` | `docs/verification.md`, `tools/check_links.mjs` |
| 14 | Integration: build check, no broken links, PR to `main`, merge, confirm Pages deploy | unclaimed | — | `COORDINATION.md` |

## Claim / handoff rules in force

1. Read this file before starting. Never start a task another session has claimed and not released.
2. Claim = write your session ID + file list here, commit, push immediately.
3. Keep scopes non-overlapping. `data.js` and `COORDINATION.md` are shared outputs: only the
   integration session changes them once other tasks are done.
4. `git pull --rebase` before every push. On conflict: stop, resolve without discarding the other
   session's work, and log it below.
5. A claim older than 60 minutes with no commits may be taken over; note the handoff.
6. Never mark anything verified without re-opening the official source and recording what it says.

## Verification log — v2 session, official sources re-opened 2026-11-06

Full detail and quoted text: `docs/sources.md`. Summary of what was personally checked:

- **SF allowable increase 1.6%** for 3/1/2026–2/28/2027; 1.4% for 3/1/2025–2/28/2026; 1.7% for 3/1/2024–2/28/2025.
  `https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit` and
  `https://www.sf.gov/news--annual-rent-increase-3126-22827-announced` and the PDF
  `https://www.sf.gov/documents/34344/571_Allowable_Annual_Increases_26-27_1.pdf` (full 1982→2027 table).
- **Once per 12 months; anniversary date; base rent only; no rounding up; 30-day notice / 90-day if >10%; +5 days if mailed;
  notice must state dollar amount, percentage, effective date, banked portion; rent-increase license required.**
  `https://www.sf.gov/learn-about-rent-increases-san-francisco`
- **Banking** (accumulate unused annual increases, not compounded, not rounded up, Rule 4.12 notice content).
  `https://www.sf.gov/information--banked-rent-increases` and
  `https://www.sf.gov/reports--december-2022--rent-board-rules-and-regulations-part-iv-rent-increases-not-requiring`
- **Rent Ordinance §37.3** (60% of CPI, 7% hard cap, banking, petitions, notice content, additional-occupant prohibition),
  **§37.3(g)** new-construction/substantial-rehab exemption with June 13, 1979 date, **§37.3(d)** Costa-Hawkins,
  **§37.15** licensing + suspension remedy, **§37.10B** harassment, **§37.10C** algorithmic pricing ban, **§37.9F** circumvention.
  `https://www.sf.gov/information--sec-373-rent-limitations`, `.../sec-3715-reporting-obligations-licensing`,
  `.../sec-3710b-tenant-harassment`, `.../sec-3710c-use-and-sale-algorithmic-devices-prohibited`,
  `.../sec-379f-circumvention-tenant-protections`, full ordinance PDF `https://www.sf.gov/documents/65403/600_Ordinance_11-02-26_2.pdf`
- **Coverage cutoff June 13, 1979** and "most single-family homes and condos exempt if tenancy began on/after 1/1/1996".
  `https://www.sf.gov/learn-about-san-francisco-rental-laws` and
  `https://www.sf.gov/information--partial-exemption-certain-single-family-homes-and-condominiums-under-costa-hawkins`
- **6.14 / Costa-Hawkins** market-rate reset when the last original occupant leaves — co-tenants are not subject to it.
  `https://www.sf.gov/information--rent-increases-under-section-614-and-costa-hawkins`
- **Additional occupants**: raising rent because a roommate moved in is an unlawful increase.
  `https://www.sf.gov/roommates-and-subletting` and §37.3(a)(11).
- **Rent Board fee** $59/unit for tax year 2026-27, 50% recoverable ($29.50), due March 1.
  `https://www.sf.gov/rent-board-fee` and `https://www.sf.gov/documents/29484/573_Rent_Board_Fee_History_25-26_8.26.pdf`
- **Housing Inventory / license** deadline March 1; license must be in effect on the effective date.
  `https://www.sf.gov/rent-board-housing-inventory` and §37.15(e).
- **AB 1482 / Civ. Code §1947.12** 5%+CPI, max 10%, ≤2 increments, notice per §827.
  `https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1947.12`
- **AB 1482 does not apply to units under a local cap that is lower** — §1947.12(d)(3). SF Rent Board states the
  AB 1482 8.8% figure "does NOT apply for units under the rent increase limitations of the San Francisco Rent Ordinance".
  `https://www.sf.gov/reports--california-tenant-protection-act-2019-ab-1482`
- **Civ. Code §827** 30/90-day notice mechanics, personal delivery or mail per CCP §1013.
  `https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=827`
- **Civ. Code §1942.5** retaliation: no rent increase within 180 days of good-faith habitability complaint.
  `https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1942.5`
- **Civ. Code §1954.53** Costa-Hawkins; §1954.53(d)(2)-(3) sublessee-only, co-tenants protected.
  `https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1954.53`
- **Gov. Code §12955 / §12927** FEHA housing discrimination, protected classes incl. source of income, marital status,
  familial status, age; "inferior terms, conditions, privileges" is discrimination.
  `https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=GOV&sectionNum=12955`,
  `https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=GOV&sectionNum=12927`,
  `https://calcivilrights.ca.gov/housing/`
- **Civ. Code §51** Unruh Civil Rights Act (business establishments: full and equal accommodations).
  `https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=51`
- **42 U.S.C. §3604(b)** FHA — discrimination in terms/conditions of rental; §3603(b) exemptions.
  `https://www.govinfo.gov/content/pkg/USCODE-2023-title42/html/USCODE-2023-title42-chap45-subchapI-sec3604.htm`,
  `https://www.govinfo.gov/content/pkg/USCODE-2023-title42/html/USCODE-2023-title42-chap45-subchapI-sec3603.htm`
- **AB 1157 (2025-26) died** — "Inactive Bill - Died", died 1/31/2026. So the 2%+CPI/5% cap proposal is NOT law.
  `https://leginfo.legislature.ca.gov/faces/billStatusClient.xhtml?bill_id=202520260AB1157`
- **SF Rent Board FY2024-25 annual report**: 42 tenant petitions in 94122; 1,219 total petitions; 339 landlord
  petitions. `https://www.sf.gov/documents/47835/Rent_Board_Annual_Statistical_Report_FY2024-2025.pdf`
- **Free tenant legal help**: Rent Board referral listing (includes an Open Door Legal office at 1722 Irving St, 94122),
  Tenant Right to Counsel front door = Eviction Defense Collaborative (415) 659-9184.
  `https://www.sf.gov/information/rent-board-referral-listing`, `https://www.sf.gov/tenant-and-landlord-resources`

### Sources that could NOT be verified / were rejected

- `https://www.hud.gov/program_offices/fair_housing_equal_opp` — returns a *contact page*, not the Fair Housing Act
  text. v1 cited it as authority for "7 protected classes"; the FHA text lists six and handicap separately, and HUD's
  own fair-housing pages do not enumerate "7 classes" on that URL. **Replaced** with govinfo U.S. Code.
- `https://www.hud.gov/program_offices/fair_housing_equal_opp` is likewise not a source for the claim that a landlord
  must apply "the same increase to both units". That claim is not in any statute; it is re-framed below as risk
  management, with the actual statutory hooks cited.
- HUD FY2026 Fair Market Rent for the San Francisco HUD Metro FMR Area: the documentation system
  (`huduser.gov/.../2026summary.odn?...`) returned empty tables and ODBscript errors for the CBSA substitution used
  here. **No FMR number is published on the site.** Third-party figures found in search (e.g. $3,604 / $3,697 2BR)
  conflict with each other and are not official. Flagged, value left blank.
- SEC/EDGAR corporate filings could not be retrieved from this sandbox (connections to sec.gov/data.sec.gov are
  blocked; EDGAR full-text search returned an unrelated document set). Therefore **no specific corporate rent-increase
  percentage is published**. The corporate-practice page states only what can be shown from statute and from the
  Rent Board's own filing statistics, and flags the gap.

## Irregularities flagged by this session (also published on `flagged.html`)

1. **Unit 2 has no increase since 6/1/2019.** Whether banked increases still exist depends on the actual rent history,
   which the owner (not this research) holds. Six-plus unused annual allowances added together exceed 10%, which
   triggers the 90-day notice rule and a much higher chance of a tenant petition. Amount left blank until the owner
   supplies the rent ledger.
2. **Unit 1 had a tenant change on 4/1/2026 at the same $3,995.** That is consistent with a lawful co-tenant
   replacement (no vacancy), but if instead all original tenants vacated and a new tenancy began, the lawful base rent
   and the anniversary date both change. Flagged: needs lease documents, not inference.
3. **Whether the building is a legal two-unit property or a single-family home with a second unit is not stated.**
   Two units on one parcel is normally covered by the Rent Ordinance either way
   (`.../partial-exemption-certain-single-family-homes-and-condominiums-under-costa-hawkins`), but "single-family"
   status changes AB 1482 and Rent Board fee analysis. Flagged.
4. **Rent increase license status is unknown** and cannot be checked from public data. §37.15(e) suspends the license
   during noncompliance, and rent is not owed for months during a suspension. Must be checked in the Rent Board portal
   before any notice is served.
5. **Whether either unit is occupied by a recipient of a tenant-based voucher** is unknown; §37.3(a)(10) changes the
   analysis substantially. Flagged.
6. **v1 defect list** (fixed in v2): see "Audit of v1" below.

## Audit of v1 (PR #1) — defects found and corrected in v2

| # | v1 statement | Problem | v2 correction |
|---|---|---|---|
| A1 | "1.6% … max monthly increase Unit 1 $63.92" | Arithmetic correct (3,995 × 0.016 = 63.92), but presented as *the* increase rather than *the cap*, and no source line on the row itself | Recomputed and shown as a cap, with arithmetic shown to the cent and a source per row |
| A2 | Dashboard stat "$4,058.92 new rent" | 3,995 + 63.92 = 4,058.92 ✓, but rounding up to whole dollars at billing would be unlawful | Noted: rent increases cannot be rounded up; the lawful new base rent is $4,058.92 |
| A3 | "Unit 2 … unused allowable increases may have been banked … do not expire during the tenancy" | Overstated. sf.gov says a skipped increase is banked only if ≥24 full months pass without an increase; and banking only applies from 4/1/1982 | Restated with the 24-month rule and the Rule 4.12 conditions |
| A4 | "Earliest effective date: no earlier than 12 months after the last increase (anniversary date)" — no date given | Unit 1's last increase date is not known, and 4/1/2026 is a *tenancy* date, not necessarily an increase date | Left blank + flagged; gives the decision rule instead of a fabricated date |
| A5 | "Federal … 7 protected classes" | The statute (42 U.S.C. §3604) lists race, color, religion, sex, familial status, national origin + handicap in (f). "7 classes" is a HUD shorthand not on the cited page; the cited URL is a contact page | Replaced with the govinfo text of §3604 and a precise list, plus FEHA/Unruh state classes |
| A6 | "Apply the same policy and same allowable increase to both units" as a *legal requirement* | No statute requires equal percentage increases across units. Treating it as law would itself be a hallucination | Re-framed: it is not a legal requirement; it is the lowest-risk practice. The legal rule is that the *reason* must not be a protected characteristic, and that identical conduct must get identical treatment |
| A7 | "Anything above the cap requires a Rent Board petition (e.g. capital improvements, operating costs)" | True but incomplete: 6 petition types + 2 bond passthroughs + utility passthroughs with worksheets; and capital improvement + O&M combined capped at 10%/12 months | Full list with the 10% combined cap and the per-type links |
| A8 | "Rent control coverage: Covered (pre-6/13/1979 building)" | Correct, but the *reason* (two units, not a single-family dwelling, tenancy began before 1/1/1996 where relevant) was not shown | Coverage table with each condition and the Costa-Hawkins/6.14 caveats |
| A9 | No mention of §37.10B harassment, §37.10C algorithmic pricing, §37.9F, §1942.5 retaliation | Material omissions for a "would a tenant lawyer sign off" review | Added a compliance matrix with each of these |
| A10 | No free-legal-aid specifics; said tenants "can obtain free tenant lawyer services" | Vague, and overstated: Right to Counsel attaches to eviction notices/lawsuits, not to rent-increase notices | Corrected distinction + full referral list with phone numbers from the Rent Board's own listing |
| A11 | "Updated 2026-11-06" on pages with no verification record | Claim without evidence | `docs/verification.md` records the check run and timestamps |
| A12 | `laws.html` linked "sf.gov — Capital improvement petitions" to a URL that 404s (`/information/capital-improvement-petitions`) | Broken/rotted link | Replaced with `https://www.sf.gov/landlord-petitions-and-passthroughs` and per-topic pages that resolve |
| A13 | No page addressed the user's question about how corporations vs. individual owners handle increases | Question unanswered | New `owners.html`, with sources and an explicit "not verifiable from official sources" flag on percentages |
| A14 | No page answered "would it be OK to raise one unit only" with the actual legal test | Answered only by assertion | New section on `process.html` with the statutory test (protected characteristic causation), the disparate-treatment framework, and the practical recommendation |

## Blockers / requests to other sessions

None. No other session is active on this repo. If a new session starts, it should read this table, and it must not
edit `data.js`, `COORDINATION.md`, `index.html`, `style.css`, or `tools/` without claiming them here first.

## PR / merge record

- PR #1 (`arena/3eac9d0e-rentincreasesf2` → `main`): **MERGED** 2026-11-06T13:19:21Z.
  `https://github.com/kanlerxz87-cyber/RentincreaseSF2/pull/1`
- GitHub Pages build after PR #1: **built**, updated 2026-11-06T13:22:26Z, source `main` `/`.
- PR #2 (this session, v2): recorded below when opened.

## Conflict log

None.
