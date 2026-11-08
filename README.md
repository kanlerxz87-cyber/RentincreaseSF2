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
| `flagged.html` | Every unverified item and irregularity (F-01 … F-26) |
| `sources.html` | All official sources and the integration method |
| `banking-rule.html` | F-16 resolved: banking-interval decisive test, re-verification, closing service window |

## Key figures

Computed from the official percentages; **inputs are owner-supplied and unverified**.

- 2026–27 SF allowable annual increase: **1.6%** (3/1/2026–2/28/2027)
- **Unit 1** — effective 2027-02-01: 1.4% banked + 1.6% current = **3.0%** → **$119.85** → **$4,114.85**.
  Taking it earlier yields only 1.6% ($63.92 → $4,058.92) and the 1.4% is permanently lost.
  30-day notice; serve by 2027-01-02 (mailed 2026-12-28).
- **Unit 2** — effective 2027-02-15: 11.5% banked + 1.6% current = **13.1%** → **$412.65** → **$3,562.65**.
  90-day notice; serve by 2026-11-17 (mailed 2026-11-12). **Closing deadline: to use any effective
  date inside the published-rate window, serve by 2026-11-30 (personal) or 2026-11-25 (mail).**
  Assumes no increase was ever imposed.
  A phased 10.0% option ($315.00 → $3,465.00) needs only 30 days and leaves 3.1% banked.
- No market-rate reset on either unit; no surcharge for Unit 1's added occupant.

## Verification standard

Every legal and numerical claim links to an official government, legislative or City of San Francisco
source. Owner-supplied lease dates, rents, occupancy and build year are marked **unverified**. Values
that cannot be confirmed are left **blank** and flagged — including the not-yet-published 2027–28
percentage. Nothing is inferred.

Three checks run on every push and pull request:

```bash
python3 scripts/sync_nav.py            # one canonical navigation across all 13 pages
python3 scripts/validate_site.py       # links, official-source allowlist, per-row sources,
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
