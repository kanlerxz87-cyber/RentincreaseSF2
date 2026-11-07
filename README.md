# RentincreaseSF2

Verified rent-increase review for two rent-controlled units in a 1940 building in San Francisco's Outer Sunset, ZIP 94122.

## Live site

https://kanlerxz87-cyber.github.io/RentincreaseSF2/

## Pages

- `index.html` — dashboard and key findings
- `executive-summary.html` — executive summary, leading with the Rent Board license question
- `units.html` — anonymized unit facts, verification status, and calculations
- `analysis.html` — Unit 1 and Unit 2 calculations, including banked increases
- `laws.html` — local, state, and federal rules with official source links
- `rent-board-process.html` — the step-by-step Rent Board process and the individual-owner license answer
- `process.html` — notice process and permissible reasons for an increase
- `tenant-protections.html` — just cause, free legal help, discrimination, and lawyer-review checklist
- `practices.html` — corporate vs. individual owner practices
- `questions.html` — every question in the brief, answered with official source links
- `flagged.html` — every unverified item and irregularity
- `sources.html` — all official sources

## Verification standard

Every legal and numerical claim is linked to an official government or City of San Francisco source. Tenant-provided lease dates, rents, occupancy, and build year are marked **unverified** until confirmed against official records. The rent increase license status is unchecked because no address/APN was provided. No value is inferred or filled in without an official source.

Sources were re-checked line by line against the live official pages on 2026-11-07. All arithmetic on the site was independently recomputed and matches.

## Key figures

- 2026–27 SF allowable annual increase: **1.6%** (3/1/2026–2/28/2027)
- Unit 1: $3,995 × 1.6% = **$63.92**; new rent **$4,058.92** (calculated from unverified base rent)
- Unit 2: 11.5% banked + 1.6% current = **13.1%**; $3,150 × 13.1% = **$412.65**; new rent **$3,562.65** (calculated; verify rent history)
- Notice: 30 days for ≤10%; 90 days for >10%; +5 days if mailed
- Rent Board Fee 2026–27: **$59.00** per dwelling unit, due March 1; 50% ($29.50) recoverable from tenants in occupancy as of November 1
- AB 1482 San Francisco maximum (units not under the local rent increase limitations): **8.8%** for August 1, 2026 – July 31, 2027

## The headline answer

**Do individual (non-corporate) owners need the Rent Board license? Yes.** Reporting into the Rent Board Housing Inventory and holding a current rent increase license on the effective date are prerequisites for any annual allowable or banked increase on a rent-controlled unit. The requirement is in Rent Ordinance §37.15(e) and §37.3(a)(1) and applies to all owners. Full step-by-step detail and official links: `rent-board-process.html` and section 1 of `executive-summary.html`.

## Privacy

Tenant names and personal identifiers are withheld. The site uses placeholders only. Dates and dollar amounts are preserved as provided.

## Not legal advice

This site is a compliance review based on official sources. It is not legal advice. The SF Rent Board cannot give legal advice. Consult a tenant lawyer or the Rent Board before serving a notice.

## Deployment

GitHub Pages serves the static files from the repository root using the repository's existing Pages configuration. A GitHub Actions workflow validates the site on every push to `main`. See `.github/workflows/validate.yml`.

## Validation

Run `python3 scripts/validate_site.py` to check internal links, external source links, table source links, and personal-identifier leakage.
