# RentincreaseSF2

Verified rent-increase review for two rent-controlled units in a 1940 building in San Francisco's
Outer Sunset, ZIP 94122.

## Live site

https://kanlerxz87-cyber.github.io/RentincreaseSF2/

## The first question, answered

**An individual owner of a two-unit rent-controlled building does need a Rent Increase License.**
All owners of residential property must report into the Rent Board Housing Inventory; reporting a
tenant-occupied unit automatically generates the license. Buildings with fewer than ten units have
been in scope since **March 1, 2023**. The legal deadline is the **effective date** of the increase,
not the date the tenant notice is served, and an unlicensed annual or banked increase is **null and
void in its entirety**. There is no separate per-increase filing with the Rent Board for an ordinary
annual or banked increase.

Sources: [Housing Inventory](https://www.sf.gov/rent-board-housing-inventory) ·
[Rules § 13.14](https://sfrb.org/section-1314-licensing-%E2%80%93-notice-rent-increase) ·
[Notice of Owner Noncompliance](https://www.sf.gov/notice-of-owner-noncompliance-with-housing-inventory)

## Pages

| Page | Contents |
|---|---|
| `index.html` | Dashboard and key findings |
| `executive-summary.html` | Executive summary — the license question first, step by step |
| `units.html` | Anonymized unit facts and verification status |
| `analysis.html` | Effective-date scenarios and the banked ledger, line by line |
| `occupancy.html` | Unit 1's household change: Rules § 6.14, Costa-Hawkins, added occupants |
| `laws.html` | Local, state and federal rules with official source links |
| `process.html` | Notice process and permissible reasons |
| `tenant-protections.html` | Just cause, free legal help, discrimination, retaliation |
| `practices.html` | Corporate vs. individual owners, including the § 37.10C algorithm ban |
| `checklist.html` | Gate 0 prerequisites, computed service deadlines, notice content |
| `flagged.html` | Every unverified item and irregularity (F-01 … F-34) |
| `sources.html` | All official sources and the integration method |
| `banking-rule.html` | F-16 resolved: banking-interval decisive test, re-verification, closing service window |

## Key figures

Computed from the official percentages; **inputs are owner-supplied and unverified**. All
figures and deadlines below are re-derived from a base date of **2026-11-10** by
`scripts/verify_calculations.py`.

- 2026–27 SF allowable annual increase: **1.6%** (3/1/2026–2/28/2027) — citywide, not by ZIP code
- **Unit 1** — effective 2027-02-01: 1.4% banked + 1.6% current = **3.0%** → **$119.85** → **$4,114.85**.
  Taking it earlier yields only 1.6% ($63.92 → $4,058.92) and the 1.4% is permanently lost.
  30-day notice; serve by 2027-01-02 (mailed 2026-12-28).
- **Unit 2** — effective 2027-02-15: 11.5% banked + 1.6% current = **13.1%** → **$412.65** → **$3,562.65**.
  90-day notice; serve by 2026-11-17 (mailed 2026-11-12). **Closing deadline: to use any effective
  date inside the published-rate window, serve by 2026-11-30 (personal) or 2026-11-25 (mail).**
  Assumes no increase was ever imposed.
  A phased 10.0% option ($315.00 → $3,465.00) needs only 30 days and leaves 3.1% banked.
- No market-rate reset on either unit; no surcharge for Unit 1's added occupant.

## Watch item: File 261020 (F-27)

On 2026-11-09 the Rent Board posted a notice on its **Current Rates**, **Banked rent increases** and
**Learn about rent increases** pages: the Board of Supervisors is considering **File No. 261020**
(introduced 2026-09-15; Land Use and Transportation Committee; status **Pending Committee Action —
not enacted**). Proposed **§ 37.3(h)** in the legislative text (`Leg Ver1`) would bar banked
(§ 37.3(a)(2)) and/or capital-improvement (§ 37.3(a)(3)) increases *"that cause a tenant's rent to
increase by more than a total of 10% of the lowest base rent that was in effect at any time during
the 12 months immediately preceding the date the increase takes effect"* through **2029-12-31**
(excess deferred to **on or after 2030-01-01**), applying retroactively to banked notices provided
on or after **2026-09-15** and capital-improvement petitions filed on or after that date, and would
amend **§ 37.15(b)(2)(F)** to require Housing Inventory reporting of prior-12-month banked
increases. Under current law Unit 2's 13.1% is unaffected if the rent history is verified. If enacted
as drafted, the literal text of § 37.3(h) measures the *total rent increase* against 10% of the
lowest prior-12-month base rent, so only the phased **10.0% option ($315.00 → $3,465.00)** stays at
or below 10% total under every reading (a narrower title-only reading capping only the banked+CI
components yields theoretical bill-draft arithmetic of 10% banked + 1.6% annual = **11.6% ($365.40 →
$3,515.40)**, which is **not law and is uncertain under § 37.3(h)'s literal wording**). Re-check
Legistar status immediately before serving any Unit 2 notice.

Related flag: **F-28** — Unit 2's suggested effective date (2027-02-15) is not the June 1
anniversary. Rent Ordinance § 37.3(a)(2) ties a banked amount to anniversary dates while the Rent
Board's irregular-period guidance allows another date; the conservative alternative is 2027-06-01,
which needs the unpublished 2027–28 rate. Put the date to a counselor or counsel.

Sources: [Current Rates](https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit) ·
[Banked rent increases](https://www.sf.gov/information--banked-rent-increases) ·
[Legistar File 261020](https://sfgov.legistar.com/LegislationDetail.aspx?ID=8217304&GUID=7EDA4662-EBFB-4AF5-962F-C669B64AA770) ·
[Leg Ver1](https://sfgov.legistar.com/View.ashx?M=F&ID=15865646&GUID=0E2E6936-000B-4597-A4EE-FBB17C19636E) ·
[Leg Dig Ver1](https://sfgov.legistar.com/View.ashx?M=F&ID=15865647&GUID=CC09B796-4675-4A7D-9960-85FE239F7FBB)

## The other intake questions, answered on the site

| Question asked | Where it is answered | Bottom line |
|---|---|---|
| Does an individual owner need the Rent Board licence? | `executive-summary.html` § 1–3 | **Yes.** Buildings with 1–9 units have been in scope since **2023-03-01**. Reporting a tenant-occupied unit generates the licence; the test is the **effective date**, and an unlicensed annual/banked increase is **void in its entirety**. |
| What is reasonable/normal in ZIP 94122 under local, state and federal law? | `laws.html` (new "does the ZIP code change anything" table) | **1.6%** for 3/1/26–2/28/27 plus properly banked amounts. The limit is **citywide**; no official source publishes a ZIP-specific percentage. AB 1482 (8.8%) does **not** apply to locally controlled units. No federal rent ceiling. |
| How do corporations vs. individual owners handle increases? | `practices.html` (new corporate-practice section) | The rules are **identical**. No official source describes a distinct corporate method; the professional sequence is the same procedure available to an individual owner. |
| Which unit should be raised — one or both? | `process.html` (new "one unit or both, tested against the discrimination rules") | **Neither is required.** Discrimination is a decision made *because of* a protected characteristic; a difference explained by unit-specific banked allowances is a formula outcome. Document the ledger. |
| Would a tenant-side advocate accept the increase? | `tenant-protections.html` + `executive-summary.html` § 7a | The law grants the right (§ 37.3(a)(1)) and § 1942.5(f) preserves lawful increases — but **no official source can predict an advocate's conclusion**, and a petition is free. |

New flags from this pass: **F-31** (the live Form 538 still prints 2021/2022 licensing start dates while five other official sources give 2022/2023), **F-32** (dead O&M citation replaced), **F-33** (nothing in the limit is ZIP-dependent), **F-34** (no official source defines "reasonable" or predicts advocate approval).

## Verification standard

Every legal and numerical claim links to an official government, legislative or City of San Francisco
source. Owner-supplied lease dates, rents, occupancy and build year are marked **unverified**. Values
that cannot be confirmed are left **blank** and flagged — including the not-yet-published 2027–28
percentage. Nothing is inferred.

Three checks run on every push and pull request:

```bash
python3 scripts/sync_nav.py            # one canonical navigation across all 13 pages
python3 scripts/validate_site.py       # links, official-source allowlist synced to sources.html,
                                       # HTML tag balance & <head>/<meta> check, per-row sources,
                                       # table column integrity, privacy sweep
python3 scripts/verify_calculations.py # re-derive every dollar amount and deadline
```

## Privacy

No tenant or owner name, initial, address, contact detail or parcel number is published. Occupants
appear only as Tenant A–F placeholders. Dates and dollar amounts are preserved exactly as supplied.
Note that the Rent Board's Housing Inventory submission is itself public — that is a legal filing
obligation, and none of it is reproduced here.

## Not legal advice

This is a compliance review based on official sources. It is not legal advice. The SF Rent Board
expressly cannot give legal advice, and no one can guarantee that a tenant lawyer will approve an
increase. Consult a tenant lawyer or a Rent Board counselor before serving a notice.

## Coordination

Parallel sessions coordinate through [COORDINATION.md](COORDINATION.md), which records every claim,
handoff, verification log, flagged irregularity and deployment.

## Deployment

GitHub Pages serves the static files from the repository root on `main`. The
`Validate site` workflow is a check, not a second deploy path.
