# Rental Increase SF

A researched, source-verified analysis of what a lawful rent increase looks like for two
rent-controlled flats in San Francisco's Outer Sunset (ZIP 94122), in a building constructed in 1940.

**Live site:** https://kanlerxz87-cyber.github.io/RentincreaseSF2/

---

## What this is

A static research site plus the data and build scripts behind it. It answers four questions:

1. What is a reasonable and normal rent increase here under local, state and federal law?
2. How do large institutional owners and individual owners handle increases?
3. How should a tenant be informed, and what reasons are defensible?
4. Would the proposed increases survive review by a San Francisco tenant-side attorney?

## The answer, briefly

| | Unit 1 | Unit 2 |
| --- | --- | --- |
| Current base rent | $3,995.00 | $3,150.00 |
| Allowable annual increase | 1.6% | 1.6% |
| Banked prior increases | 1.4% (one year) | 11.5% (six years) |
| **Maximum lawful new rent** | **$4,114.85** (3.0%) | **$3,562.65** (13.1%) |
| Notice required | 30 days | 90 days |

Two items must be closed before any notice is served: the **rent increase licence** for each unit,
and **Unit 1's anniversary date** (see `flagged.html`).

## Source policy

Every figure is linked to the government agency that publishes it — the SF Rent Board, the
California Legislature, HUD, the Department of Justice, or the Bureau of Labor Statistics. No
law-firm blog or property-manager calculator was relied on for any number. Where a value could not
be confirmed from an official source it is **left blank and flagged**, never estimated.

The allowable-increase table (`data/aga-history.csv`) is a verbatim transcription of SF Rent Board
Form 571.

## Repository layout

```
index.html … verification.html   Built pages (committed — GitHub Pages serves them directly)
assets/style.css                 Stylesheet, no dependencies
assets/app.js                    Table filter/sort, progressive enhancement only
data/aga-history.csv             Form 571 transcribed, 1982–2027
tools/_template.py               Shared page chrome
tools/_data.py                   Source register (URLs and labels)
tools/_rows.py                   All table row data
tools/build.py                   Builds pages 01–06
tools/build2.py                  Builds pages 07–13
tools/check.py                   Link, host, privacy and table integrity checker
COORDINATION.md                  Shared task board for parallel agent sessions
```

## Rebuild

There is no toolchain and no `package.json` by design — GitHub Pages serves `main` at `/` with the
legacy build type, so a broken build is not possible at deploy time. To regenerate after editing the
data files:

```bash
python3 tools/build.py
python3 tools/build2.py
python3 tools/check.py      # must print CLEAN
```

To preview locally:

```bash
python3 -m http.server 8080
```

## Privacy

Placeholder initials only. No names, street address, unit numbers, phone numbers or email addresses
are published. Dates and dollar amounts are preserved unchanged because they are what the legal
analysis turns on. See the "Privacy handling" section on `flagged.html`.

## Not legal advice

This is a research aid. Rent Ordinance questions should go to a San Francisco Rent Board counselor
(415-252-4600), and tenancy-specific questions to a licensed attorney.
