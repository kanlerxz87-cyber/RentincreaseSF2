# Internal — personal information handling

**This folder is published by GitHub Pages along with the rest of the repository.** Nothing in
this repository is private. Read that sentence twice before adding anything here.

## Why this file contains no personal data

The owner asked that personal information be kept **internal**, and that everything published on
the site be anonymised with placeholder names while dates and dollar amounts stay unchanged. A
GitHub Pages site serves the repository root, so a file placed here for "internal" use would
actually be public at `https://kanlerxz87-cyber.github.io/RentincreaseSF2/internal/README.md`.

Therefore:

- The tenant names and initials supplied in the intake **are not written anywhere in this
  repository** — not here, not in `COORDINATION.md`, not in `AUDIT.md`, not in any HTML page.
- The street address and Assessor's Parcel Number (APN) are **not written anywhere in this
  repository** either.
- The mapping between the real identity of each occupant and the placeholder used on the site
  (Tenant A … Tenant F, and "Unit 1" / "Unit 2") is held **offline by the owner**. It is
  deliberately not reproducible from anything committed here.

This is a departure from a literal reading of "store the identity mapping internally": the only
way to keep data internal in a public repository is to keep it out of the repository. The owner
should keep the mapping in their own records.

## What is published, and what is not

| Item | Published on the site? | Where it lives |
|---|---|---|
| Tenant names | No | Owner's records only |
| Tenant initials | No | Owner's records only |
| Street address | No | Owner's records only |
| APN / parcel number | No | Owner's records only |
| Contact details (phone, email), landlord or tenant | No | Owner's records only |
| Unit labels | Yes — "Unit 1", "Unit 2" | Site |
| Occupant placeholders | Yes — Tenant A … Tenant F | Site |
| Lease start dates | Yes, unchanged as supplied | Site (`units.html`) |
| Rents and every computed dollar amount | Yes, unchanged as supplied | Site (`units.html`, `analysis.html`, `answers.html`) |
| Build year, unit count, occupancy | Yes, labelled **owner-supplied; unverified** | Site (`units.html`) |

Dates and dollar amounts are published exactly as supplied, because the owner asked for that and
because they are the substance of the analysis. They are also the figures a reader needs in order
to check the arithmetic.

## Automated enforcement

`scripts/validate_site.py` runs a privacy sweep on every push and pull request. It scans every
HTML page **and** the public Markdown files (`README.md`, `COORDINATION.md`, `AUDIT.md`) for the
supplied tenant initial pairs and fails the build if any appear. The sweep is the reason the
initial-pair list below is written as a description rather than as the values themselves.

The sweep is a pattern check, not a guarantee. It cannot detect a *new* personal identifier that
nobody has told it about. If the intake is ever extended with a new name or identifier, add its
pattern to `PERSONAL_PATTERNS` in `scripts/validate_site.py` in the same commit.

## Known residual exposure (F-23)

Redaction only changes the **current** version of a file. This repository is public, and earlier
commits in its history contain tenant initials that one earlier session wrote into
`COORDINATION.md` while reviewing a different pull request. Those commits remain reachable through
the repository history.

Nothing on the site displays them and no current file contains them, but history is a separate
exposure. The options — and why none of them was applied automatically — are set out under F-23 on
the [Flagged for Review](../flagged.html) page:

1. Make the repository private. Check the effect on GitHub Pages first; access control depends on
   the plan.
2. Rewrite history and force-push. Destructive, and it would discard other sessions' commit
   identities, so it is the owner's decision, not an automated one.
3. Accept the exposure on the basis that initials alone are weak identifiers.

## Interaction with the Rent Board's own publication duty

Separate from anything on this site, the Rent Board states that information entered in the Housing
Inventory submission is **public**, including the owner's name and business contact information, and
that submissions are made under penalty of perjury. That disclosure is a legal filing obligation
and cannot be avoided by anonymising this site. It is tracked as F-21.

## If you are a future session reading this

- Do not add tenant names, initials, addresses or contact details to any file in this repository,
  including `COORDINATION.md` and `AUDIT.md`. Quote the intake by placeholder only.
- Do not "improve" this file by adding the identity mapping. That would convert the one internal
  dataset in this project into public data.
- Run `python3 scripts/validate_site.py` before any push. It checks the public Markdown too.
