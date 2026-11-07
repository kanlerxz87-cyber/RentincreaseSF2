# RentincreaseSF2

Verified rent-increase review for two rent-controlled units in a 1940 building in San Francisco's Outer Sunset, ZIP 94122.

## Live site

https://kanlerxz87-cyber.github.io/RentincreaseSF2/

## Pages

- `index.html` — dashboard and key findings
- `executive-summary.html` — executive summary
- `units.html` — anonymized unit facts, verification status, and calculations
- `analysis.html` — Unit 1 and Unit 2 calculations, including banked increases
- `laws.html` — local, state, and federal rules with official source links
- `process.html` — notice process and permissible reasons for an increase
- `tenant-protections.html` — just cause, free legal help, discrimination, and lawyer-review checklist
- `practices.html` — corporate vs. individual owner practices
- `flagged.html` — every unverified item and irregularity
- `sources.html` — all official sources

## Verification standard

Every legal and numerical claim is linked to an official government or City of San Francisco source. Tenant-provided lease dates, rents, occupancy, and build year are marked **unverified** until confirmed against official records. The rent increase license status is unchecked because no address/APN was provided. No value is inferred or filled in without an official source.

## Key figures

All dollar amounts are re-derived from the official percentages by
`scripts/validate_site.py` on every run, so a mistyped figure fails the build.

- 2026–27 SF allowable annual increase: **1.6%** (3/1/2026–2/28/2027)
- Unit 1: $3,995 × 1.6% = **$63.92**; new rent **$4,058.92**. A 4/1/2026 date is
  *not* an anniversary date, so it forfeits the 1.4%; waiting for the 2/1/2027
  anniversary allows 1.4% + 1.6% = 3.0% = **$119.85**, new rent **$4,114.85**
- Unit 2: the total depends on a genuine conflict between official sources over
  the banking interval — **13.1%** (11.5% + 1.6%) under the 12-month reading,
  new rent **$3,562.65**; **11.7%** (10.1% + 1.6%) under the 24-month reading,
  new rent **$3,518.55**. Both are shown; neither is asserted as settled.
- Notice: 30 days for ≤10%; 90 days for >10%; +5 days if mailed

## Known official-source conflict

The sf.gov "Banked rent increases" page says a skipped increase banks only after
**24 full months**, while Rent Board Rules §4.12 says **12 months**, the Ordinance
§37.3(a)(2) states no waiting period, and the Board's own worked examples apply
12 months. Both readings are published (Flagged item 15) rather than one being
silently chosen.

## Privacy

Tenant names and personal identifiers are withheld. The site uses placeholders only. Dates and dollar amounts are preserved as provided.

## Not legal advice

This site is a compliance review based on official sources. It is not legal advice. The SF Rent Board cannot give legal advice. Consult a tenant lawyer or the Rent Board before serving a notice.

## Deployment

GitHub Pages serves the static files from the repository root using the repository's existing Pages configuration. A GitHub Actions workflow validates the site on every push to `main`. See `.github/workflows/validate.yml`.

## Validation

Run `python3 scripts/validate_site.py` to check internal links, external source links, table source links, and personal-identifier leakage.
