# Internal — personal information handling

**This folder is published by GitHub Pages along with the rest of the repository.** Nothing in
this repository is private. Read that sentence twice before adding anything here.

## Why this file contains no personal data

The owner asked that personal information be kept **internal**, and that everything published on
the site be anonymised with placeholder names while dates and dollar amounts stay unchanged. A
GitHub Pages site serves the repository root, so a file placed here for "internal" use would
actually be public at `https://kanlerxz87-cyber.github.io/RentincreaseSF2/internal/README.md`.

Therefore:

- Current public pages use anonymized labels. Earlier commits contain tenant initials; see F-23.
  A scan without privately supplied patterns cannot guarantee every current file is free of identifiers.
- Do not add the street address or Assessor's Parcel Number (APN) to any public file.
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

`scripts/validate_site.py` runs on every push and pull request. It recursively scans all public
text files, including this folder, for merge markers. A reviewer may also supply private identifier
regexes through the `PRIVATE_IDENTIFIER_PATTERNS` environment variable, one per line. The validator
reports only that a privately supplied pattern matched; it never prints the pattern.

**Do not commit identifier patterns to this repository.** The former `PERSONAL_PATTERNS` list was
removed because public code is not a safe place for tenant-specific matching rules. Supply any new
private patterns only through a local environment variable or another private secret channel, and
check that logs do not echo them. The pattern check is not a guarantee that an unknown identifier
will be detected.

## Known residual exposure (F-23)

Redaction only changes the **current** version of a file. This repository is public, and earlier
commits in its history contain tenant initials that one earlier session wrote into
`COORDINATION.md` while reviewing a different pull request. Those commits remain reachable through
the repository history.

Current pages use anonymized labels, but optional private-pattern checks are not a guarantee that
unknown identifiers are absent. History remains a separate exposure, and published dates and
amounts may also contribute to re-identification. The options — and why none of them was applied automatically — are set out under F-23 on
the [Flagged for Review](../flagged.html#F-23) page:

1. Make the repository private. Check the effect on GitHub Pages first; access control depends on
   the plan.
2. Rewrite history and force-push. Destructive, and it would discard other sessions' commit
   identities, so it is the owner's decision, not an automated one.
3. Document and accept the residual exposure only after assessing the privacy risk.

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
- Run `python3 scripts/validate_site.py` before any push. It checks public text files recursively; private patterns belong only in the environment.
