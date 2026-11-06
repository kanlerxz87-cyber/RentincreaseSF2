# Privacy and Anonymization Policy

**Status:** Binding on every session working in this repository.
**Reason:** This repository publishes to a **public** GitHub Pages site at
`https://kanlerxz87-cyber.github.io/RentincreaseSF2/`. Anything committed here is
publicly discoverable, indexed by search engines, and retained in Git history
permanently. A later deletion does **not** remove it from history.

---

## The rule

> **No personally identifiable information about any tenant, occupant, owner or
> property is committed to this repository. Not in a data file, not in a document,
> not in a commit message, not in a code comment.**

The details supplied by the owner are treated as **internal information only** and
are held **outside** this repository. They were never written to disk here and never
will be. There is no "internal copy" in the repo to leak.

What *is* preserved verbatim, because the owner asked for it and because it carries
no identity:

- **Dates** — lease commencement dates, anniversary dates, effective dates
- **Dollar amounts** — base rents, increase amounts, resulting rents
- **Unit labels** — `Unit 1`, `Unit 2` (sequential, not addresses)
- **Building facts already non-identifying** — year built (1940), unit count (2), ZIP (94122)

---

## Placeholder mapping

Names are replaced by role-based placeholders. The mapping below is deliberately
**reversible only by someone who already knows the real names**, so it leaks nothing.

| Placeholder | Role in the record | Real identity |
|---|---|---|
| **Tenant A** | Original occupant of Unit 1, **still in place** | held internally, not in repo |
| **Tenant B** | Original occupant of Unit 1, **departed** | held internally, not in repo |
| **Tenant C** | Original occupant of Unit 1, **departed** | held internally, not in repo |
| **Tenant D** | Occupant **added** to Unit 1 on 2026-04-01 | held internally, not in repo |
| **Tenant E** | Occupant of Unit 2, tenancy since 2019-06-01 | held internally, not in repo |
| **Tenant F** | Occupant of Unit 2, tenancy since 2019-06-01 | held internally, not in repo |
| **Owner** | Property owner / landlord | held internally, not in repo |

Two consequences matter for the legal analysis and are preserved precisely because
they are not identifying:

1. **Tenant A is an original occupant who remains.** That single fact is what
   defeats a market-rate rent reset under Rent Board Rules § 6.14 and under
   Costa-Hawkins. See `pages/calculations.html`.
2. **Tenant D was added, not substituted for the whole household.** Charging more
   because an occupant was added is an **unlawful rent increase** under SF Admin.
   Code § 37.3(a)(11)(A) — even if the lease says otherwise.

---

## Also withheld

| Item | Status | Why |
|---|---|---|
| Street address | **WITHHELD** | Directly identifies the property and its occupants |
| Assessor's Parcel Number | Not supplied | Would allow address recovery |
| Unit numbers as used on the building | Replaced by `Unit 1` / `Unit 2` | Sequential labels only |
| Owner name and business contact | **WITHHELD** | Note: the Rent Board Housing Inventory submission **is public** and does publish owner name and business contact information — see Flag F-22 |
| Tenant dates of birth, income, immigration status, criminal history | Never supplied, never collected | FEHA / Fair Chance protected characteristics |

---

## A note on the Housing Inventory

This is a real tension the owner should understand, and it is documented rather than
hidden. To obtain the **rent increase license** that SF Admin. Code § 37.15 requires
before *any* annual or banked increase can take effect, the owner must report into the
Rent Board Housing Inventory at `portal.sfrb.org`. SF.gov states plainly:

> "The information entered in the housing inventory submission is **public**. This may
> include information such as: name and business contact information, approximate square
> footage, number of bedrooms, number of bathrooms, history of vacancy or occupancy
> during the past 12 months."

It also requires the **amount of base rent** in $250 increments and the **date current
occupancy began**, submitted under penalty of perjury.

So: complying with the licensing precondition for a lawful rent increase necessarily
publishes some property-level data through a City system. That disclosure is made by
the owner, through the City's portal, under the City's own rules — **not** through this
repository. Tenants can search the portal to check a landlord's license status. Nothing
in this project adds to that disclosure.

Source: <https://www.sf.gov/rent-board-housing-inventory>

---

## Verification performed

| Check | Method | Result |
|---|---|---|
| No real names anywhere in tracked files | `git grep` across the whole tree for each supplied initial-pair pattern | Pass — zero matches |
| No address, APN or phone number of the property | `git grep` for street/number patterns | Pass — zero matches |
| Data files contain only placeholders | Manual review of `data/units.json` | Pass |
| Dates and dollar amounts preserved exactly | Compared against the owner-supplied facts | Pass — `$3,995.00`, `$3,150.00`, `2025-02-01`, `2026-04-01`, `2019-06-01` all verbatim |
| Nothing identifying in commit messages | Review of `git log` | Pass |

The `git grep` sweep is re-run automatically by `build.py` on every site build and the
build **fails** if any real identifier appears. See the `assert_no_pii()` function.

---

## If PII is ever committed by mistake

Do not just delete the file — Git retains history.

1. Note the exact commit and file.
2. Report it in `COORDINATION.md` under *Conflict / Handoff Log*.
3. Purge with `git filter-repo` or BFG, force-push, and ask GitHub Support to clear
   cached views and forks.
4. Assume the data was captured by crawlers and treat it as disclosed.

Prevention is the only reliable control, which is why the build-time sweep exists.
