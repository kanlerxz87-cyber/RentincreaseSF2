# Rent Increase Analysis — Outer Sunset, San Francisco (ZIP 94122)

A requirements, verification and analysis project for a **two-unit rent-controlled building
built in 1940** in the Outer Sunset district of San Francisco.

**Live site:** <https://kanlerxz87-cyber.github.io/RentincreaseSF2/>

---

## What this answers

| Question | Where |
|---|---|
| What is a reasonable and normal rental increase here under **local, state and federal** law? | [Executive Summary](pages/executive-summary.html) · [SF Law](pages/local-law.html) · [CA Law](pages/state-law.html) · [Federal Law](pages/federal-law.html) |
| How do **large corporate owners** handle increases versus **individual owners**? | [Owner Practices](pages/practices.html) |
| What is the **correct way to notify** tenants, and which reasons are **legitimate**? | [Checklist & Notice Procedure](pages/checklist.html) |
| Would these increases survive review by an **SF tenant lawyer**? | [Tenant-Lawyer Test](pages/tenant-review.html) |
| Raise **one unit or both**, to avoid discrimination claims? | [Anti-Discrimination](pages/discrimination.html) |
| Lawful **amounts, dates and notice deadlines** for each unit | [Increase Scenarios](pages/calculations.html) |
| Every **official percentage** published since 1982 | [Allowable Increases](pages/allowable.html) |
| **Market data** for ZIP 94122 | [Market Data](pages/market.html) |
| Where each figure came from | [Source Register](pages/sources.html) |
| What could **not** be verified | [Flagged for Review](pages/flagged.html) |

---

## Verification standard

- **Official sources only.** `.gov` domains, the California Legislative Information service,
  the SF Rent Board, the SF Board of Supervisors and the U.S. Census Bureau API.
  47 documents registered in [`data/sources.json`](data/sources.json).
- **Every table row carries a source link.** Enforced by the generator, not by discipline.
- **Blank rather than inferred.** Any value that could not be confirmed from an official
  source is left empty and recorded in [`data/flags.json`](data/flags.json) — 24 flags,
  7 of them HIGH severity.
- **No figure is typed by hand.** Every dollar amount and every notice deadline is recomputed
  from official percentages at build time and cross-checked against the stored values; a
  mismatch fails the build. Census bracket counts are sum-checked against published totals.
- **No hallucinated URLs.** Every link in the source register was fetched during this project.

## Privacy

All tenant and owner identities are **withheld** and replaced with placeholders
(`Unit 1` / `Unit 2`, `Tenant A`–`F`). Dates and dollar amounts are preserved exactly.
Nothing personally identifying is committed to this repository — see
[`docs/PRIVACY-AND-ANONYMIZATION.md`](docs/PRIVACY-AND-ANONYMIZATION.md).

`build.py` runs a PII sweep over every generated document and **fails the build** if a
non-official email address, phone number or SSN-shaped value appears. An owner can strengthen
the sweep locally via a gitignored `.pii-guard.local.json` — deliberately not committed,
because listing real identifiers in the repo in order to block them would publish them.

---

## Repository layout

```
index.html                  Landing dashboard
pages/                      14 category subpages
assets/css/styles.css       Site styling (no external dependencies, no CDN)
assets/js/app.js            Table filtering only (no external dependencies)
data/*.json                 Single source of truth — every value carries its source URL
build.py                    Generator + verification harness
docs/executive-summary.md   The executive summary
docs/repo-review.md         Line-by-line audit of the repository as received
docs/PRIVACY-AND-ANONYMIZATION.md   Binding anonymization policy
COORDINATION.md             Shared task board, verification log, integration record
.nojekyll                   Stops GitHub Pages running Jekyll over the static site
```

## Rebuilding

```bash
python3 build.py
```

Exit code is non-zero if any arithmetic check, Census reconciliation, source-link check,
internal-link check or PII sweep fails. No packages required — Python 3 standard library only.

## Not legal advice

This is a research and verification project. Seven HIGH-severity flags must be closed before
any notice is served, including confirmation of a current **rent increase license** under
SF Administrative Code § 37.15 — without which an increase is null and void in its entirety
regardless of correct arithmetic. Free Rent Board counseling is available at 415-252-4600.
