# AUDIT.md — Independent line-by-line repository audit

**Repository:** `kanlerxz87-cyber/RentincreaseSF2`
**Base commit audited:** `0f32ab2` (merge of PR #10, `main`)
**Audit date:** 2026-11-07
**Auditing session:** `arena/bf462feb-rentincreasesf2`
**Live site:** https://kanlerxz87-cyber.github.io/RentincreaseSF2/

This is an independent re-verification of the repository performed by a session that did not
write any of the material it audits. Every figure was re-derived from primary official sources
without reusing the site's own arithmetic. Nothing in this document is inferred: where a value
could not be confirmed from an official source it is recorded as blank and flagged.

**Privacy note.** This file is served publicly by GitHub Pages from the repository root, because
Pages is configured to publish `/` of `main` and `.nojekyll` disables Jekyll. It was confirmed
empirically during this audit that
`https://kanlerxz87-cyber.github.io/RentincreaseSF2/COORDINATION.md` returns raw file content.
Accordingly this document contains **no** tenant names, initials, addresses or contact details.
The site's own placeholders (`Tenant A`–`Tenant F`, see `occupancy.html`) are used instead.

---

## 1. Scope of the audit

| File | Lines | Audited | Result |
|---|---|---|---|
| `index.html` | 118 | yes | Pass — figures confirmed |
| `executive-summary.html` | 120 | yes | Pass — figures confirmed |
| `units.html` | 112 | yes | Pass — figures confirmed |
| `analysis.html` | 172 | yes | Pass — every scenario figure re-derived and confirmed |
| `occupancy.html` | — | yes | Pass — §6.14 / Costa-Hawkins reasoning consistent with cited sources |
| `laws.html` | 123 | yes | Pass |
| `process.html` | 111 | yes | Pass |
| `tenant-protections.html` | 126 | yes | Pass |
| `practices.html` | 107 | yes | Pass |
| `checklist.html` | — | yes | Pass — all service dates recomputed and confirmed |
| `flagged.html` | 95 | yes | Pass — 22 flags, all justified; F-16 can now be closed (A-01) |
| `sources.html` | 145 | yes | Pass |
| `scripts/validate_site.py` | — | yes | Pass — runs clean; see A-09 |
| `scripts/sync_nav.py` | — | yes | Pass |
| `scripts/verify_calculations.py` | — | yes | Pass |
| `.github/workflows/validate.yml` | 28 | yes | Pass |
| `README.md` | 47 | yes | Pass — no personal identifiers |
| `COORDINATION.md` | 447 | yes | Initials removed in PR #10; residual issues A-07, A-08 |
| `style.css` | 187 | yes | Pass |

**No fabricated or hallucinated value was found anywhere in the repository.** No figure was
identified that is contradicted by an official source.

---

## 2. Method

1. Read `COORDINATION.md` first, as the coordination instructions require, and enumerated every
   session claim on `main` and on all ten remote `arena/*` branches.
2. Fetched and read the **primary** official texts directly, in this order: Rent Board Rules and
   Regulations Part IV (§4.10, §4.12), Rent Ordinance §37.3, Rent Ordinance §37.10C, Form 571,
   the Current Rates page, the four worked examples on *Learn about rent increases*, *Banked rent
   increases*, *Increasing rents during irregular periods*, *Annual rent increase for multiple
   years*, *Housing Inventory*, *Tenant Petitions*, *Tenant and Landlord Resources*, the AB 1482
   report, Civil Code §827, and Rent Board Rules §13.14.
3. Re-derived every percentage and dollar figure independently, and recomputed every notice
   deadline by script from a base date of 2026-11-07.
4. Tested each candidate reading of the disputed banking interval against **both** official worked
   examples, rather than accepting either official page at face value.
5. Scanned all files for tenant initials and other personal identifiers.

Scripts and commands used are listed in section 7 so the audit is reproducible.

---

## 3. Independent re-verification — results

Every published figure was re-derived from primary sources. **All confirmed.** The full
claim-by-claim table, with verbatim source text, is section 6 of
[`banking-rule.html`](banking-rule.html). Summary:

| Claim | Re-derived | Verdict |
|---|---|---|
| Allowable annual increase 2026-03-01 to 2027-02-28 | 1.6% | Confirmed — Form 571 and Current Rates |
| Annual allowance is 60% of Bay Area CPI, capped at 7% | §37.3(a)(1) verbatim | Confirmed |
| Unit 1 below 2027-02-01: 1.6% → $63.92 → $4,058.92 | $3,995.00 × 0.016 = $63.92 | Confirmed |
| Unit 1 on 2027-02-01: 1.4% + 1.6% = 3.0% → $119.85 → $4,114.85 | $3,995.00 × 0.03 = $119.85 | Confirmed |
| Unit 2 banked: 1.8+0.7+2.3+3.6+1.7+1.4 = 11.5% | 11.5 | Confirmed |
| Unit 2 total 13.1% → $412.65 → $3,562.65 | $3,150.00 × 0.131 = $412.65 | Confirmed |
| Unit 2 phased 10.0% → $315.00 → $3,465.00, 3.1% remains banked | $3,150.00 × 0.10 = $315.00 | Confirmed |
| 2019-20 allowance (2.6%) not available on Unit 2 | first increase could only be imposed 2020-06-01 → 1.8% | Confirmed |
| Notice: 30 days at ≤10%, 90 days above 10%, +5 if mailed | Civ. Code §827(b)(1)–(3) | Confirmed |
| AB 1482's 8.8% cap does not apply | "does NOT apply for units under the… San Francisco Rent Ordinance" | Confirmed verbatim |
| 2027-28 percentage unpublished, left blank | Form 571 ends at 2027-02-28 | Confirmed — correctly blank |
| Added occupant cannot raise rent even if the lease allows it | sf.gov verbatim | Confirmed verbatim |
| Service dates in `checklist.html` (2026-11-17, 2026-11-12, 2027-01-02, 2026-12-28, 2027-03-03, 2027-02-26) | all recomputed | Confirmed |

**An error found and corrected in this audit's own draft:** an early version of
`banking-rule.html` asserted 14.7% for Unit 2 on 2027-06-01, treating the 2026-27 rate of 1.6% as
in effect on that date. It is not — 2027-06-01 falls in the 2027-28 period, which is unpublished.
The main site was right to leave that cell blank and the draft was corrected before publication.
Recorded here because it is exactly the class of error the verification standard exists to catch.

---

## 4. Irregularity register

Severities: **high** = affects a decision or a legal outcome; **medium** = materially improves
accuracy or timing; **low** = completeness.

| ID | Severity | Finding | Files affected | Official source for manual review |
|---|---|---|---|---|
| **A-01** | medium | **Flag F-16 is recorded as an open conflict, but it is resolvable on the evidence.** Rules §4.12(a) requires "a full 12 months… from the date that an annual rent increase… could have been imposed"; the summary page says "at least 24 full months pass without any rent increase." Of the three possible readings, only the per-allowance 12-month test reproduces **both** official worked examples (6.7% and 3.3%). A global-24 reading gives 4.7% where the Rent Board's own example says 3.3% and states the allowance is "permanently lost"; a per-allowance-24 reading gives 5.0% where the example says 6.7%. F-16 should be closed as resolved, with the test cited. | `flagged.html`, `analysis.html` | [Rules Part IV §4.12](https://www.sf.gov/reports--december-2022--rent-board-rules-and-regulations-part-iv-rent-increases-not-requiring) · [Banked increases](https://www.sf.gov/information--banked-rent-increases) · [Worked examples](https://www.sf.gov/learn-about-rent-increases-san-francisco) |
| **A-02** | **high** | **The Unit 2 service window is not stated as a closing deadline.** The site records the outer limit (effective on or before 2027-02-28) and the service dates for the suggested 2027-02-15 target, but not the last date on which *any* effective date inside the window can still be reached: **2026-11-30** by personal delivery, **2026-11-25** by mail — 23 and 18 days from the audit date. Nor is it stated that the mailed route to the earliest date (2027-02-05) closed on 2026-11-02. Because banked amounts may only be given at the time of an annual increase, and the 2027-28 percentage is unpublished, missing this window means Unit 2's 13.1% cannot be priced until the Rent Board announces the new rate. | `index.html`, `executive-summary.html`, `checklist.html` | [Form 571](https://www.sf.gov/documents/34344/571_Allowable_Annual_Increases_26-27_1.pdf) · [Civ. Code §827](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=827.&lawCode=CIV) · [Rule 4.12(a)](https://www.sf.gov/reports--december-2022--rent-board-rules-and-regulations-part-iv-rent-increases-not-requiring) |
| **A-03** | medium | The "take nothing yet" option in `checklist.html` says there is "no deadline to act, other than the rate-change effect above." That is accurate but incomplete: §4.12(a) provides the banked amount "may only be given at the time of an annual increase," so the 11.5% cannot be imposed on its own at a later date of the owner's choosing — it must ride with an annual allowance, and after 2027-02-28 that allowance is not yet known. | `checklist.html` | [Rules Part IV §4.12(a)](https://www.sf.gov/reports--december-2022--rent-board-rules-and-regulations-part-iv-rent-increases-not-requiring) · [Banked increases](https://www.sf.gov/information--banked-rent-increases) |
| **A-04** | low | **A favourable rule is missing.** Rules §13.14 ends: "Nothing in this Regulation shall affect a landlord's banking rights or the ability to accumulate otherwise lawful rent increases that were found to be null and void." This materially softens flag F-03: a notice that fails for want of a license voids *that increase*, not the accumulated 11.5%. Worth recording so the license risk is not over-weighted. | `checklist.html`, `flagged.html`, `laws.html` | [Rules §13.14 (Rent Board)](https://sfrb.org/section-1314-licensing-%E2%80%93-notice-rent-increase) · [Form 538 worksheet restating it](https://www.sf.gov/sites/default/files/2024-10/538%202024-25%20Bond%20Measure%20Worksheet%2010.24%20.pdf) |
| **A-05** | low | §13.14 also fixes the test to the **effective date, not the service date**: "the effective date of the rent increase, not the date of service, shall be used to determine whether or not the increase conforms." The site states the effective-date rule from the Housing Inventory page but not this express regulatory wording, which is the stronger citation. | `checklist.html`, `process.html` | [Rules §13.14](https://sfrb.org/section-1314-licensing-%E2%80%93-notice-rent-increase) |
| **A-06** | low | **New discrepancy between two official Rent Board documents.** The Housing Inventory page and *Learn about rent increases* give the license requirement's start as **1 July 2022** (buildings of 10+ units, other than condominiums) and **1 March 2023** (condominiums and buildings with fewer than 10 units). The Rent Board's own Form 538 worksheet states the requirement applies to increases effective on or after **1 July 2020** and **1 March 2021** respectively. Practical impact is nil — both dates are past and a current license is required now either way — but it is an inconsistency between official documents and belongs on the flagged page. For a two-unit building the applicable group is "fewer than 10 units" on either version. | `flagged.html`, `laws.html` | [Housing Inventory](https://www.sf.gov/rent-board-housing-inventory) · [Learn about rent increases](https://www.sf.gov/learn-about-rent-increases-san-francisco) · [Form 538 worksheet](https://www.sf.gov/sites/default/files/2024-10/538%202024-25%20Bond%20Measure%20Worksheet%2010.24%20.pdf) |
| **A-07** | **high** | **Coordination irregularity: duplicate task numbers and a stale base.** Session `arena/2b3012a0-rentincreasesf2` claimed tasks **13, 14, 15** on its branch; session `arena/fa7d2d77-rentincreasesf2` independently used **13–18** on `main`. Both sets are now in the record with different meanings. Separately, `arena/2b3012a0` branched from `62f6f59`, which predates PRs #6–#10, and its in-progress commit rewrites `executive-summary.html` and adds two pages against that stale base — merging it as-is would revert the PR #6/#7 license clarification and the PR #10 privacy redaction. It must rebase onto current `main` before opening a PR. | `COORDINATION.md` | Branch inspection: `git log origin/arena/2b3012a0-rentincreasesf2`; `git diff origin/main origin/arena/2b3012a0-rentincreasesf2` |
| **A-08** | **high** | **Markdown committed to the repository root is publicly served by GitHub Pages.** Confirmed empirically: `COORDINATION.md` was retrievable at the Pages URL during this audit. That is how tenant initials became public in the first place (remediated in PR #10, and the residual exposure in git history is already flagged there). The general rule is not yet written down anywhere, so a future session can repeat the mistake with `AUDIT.md` or any other root Markdown file. It should be recorded as a standing constraint, and `scripts/validate_site.py`'s privacy sweep should cover all root Markdown, not only the HTML page list. | `COORDINATION.md`, `scripts/validate_site.py`, `.github/workflows/validate.yml` | Pages configuration: `gh api repos/kanlerxz87-cyber/RentincreaseSF2/pages` → `source: {branch: main, path: /}`, `build_type: legacy`; `.nojekyll` present |
| **A-09** | low | `scripts/validate_site.py` enforces that every page links to every page in its `PAGES` list, and `scripts/sync_nav.py` renders one canonical nav. Both are sound. They do not yet know about `banking-rule.html` or `AUDIT.md`, so the new page is currently reachable only by direct URL and from this document. See change request CR-01. | `scripts/validate_site.py`, `scripts/sync_nav.py` | Local run: `python3 scripts/validate_site.py` |
| **A-10** | low | Stale open PR #5 (`arena/48ffb5b4-rentincreasesf2`) was closed by session `arena/fa7d2d77` during this audit, with its verified findings ported rather than merged. No action remains. Recorded for completeness because this session had claimed its disposition as task 19 before learning it was already handled. | GitHub only | [PR #5](https://github.com/kanlerxz87-cyber/RentincreaseSF2/pull/5) |

---

## 5. Confirmed-correct register

Recorded so that a later session does not re-litigate settled points. Each was checked against an
official source during this audit.

| Point | Confirmation | Official source |
|---|---|---|
| The Rent Ordinance itself sets **no waiting period** for banking | §37.3(a)(2) grants the right to accumulate and impose "on the tenant's subsequent rent increase anniversary dates", subject to §37.15, with no interval stated. The interval comes only from Rules §4.12. The site says exactly this. | [sf.gov — Sec. 37.3](https://www.sf.gov/information--sec-373-rent-limitations) |
| An individual owner is **not** exempt from the license | §37.3(a)(1) conditions the annual-increase right on having "reported the required information about their rental unit to the Rent Board as set forth in Section 37.15"; §13.14 grants the license to "a landlord who has substantially complied" with reporting. Neither turns on corporate form. | [sf.gov — Sec. 37.3](https://www.sf.gov/information--sec-373-rent-limitations) · [Rules §13.14](https://sfrb.org/section-1314-licensing-%E2%80%93-notice-rent-increase) |
| **No petition is filed** for an annual or banked increase | Form 571: "without filing a petition at the Rent Board". Banked increases "do not have to be approved by the Rent Board, but must be calculated correctly". Irregular-periods page: "Landlords are not required to file a petition with the City to impose these types of rent increases." | [Form 571](https://www.sf.gov/documents/34344/571_Allowable_Annual_Increases_26-27_1.pdf) · [Banked increases](https://www.sf.gov/information--banked-rent-increases) · [Irregular periods](https://www.sf.gov/information--increasing-rents-during-irregular-periods) |
| The license need **not** be attached to the tenant notice | "The rent increase license does not need to be included with your rent increase notice." | [sf.gov — Housing Inventory](https://www.sf.gov/rent-board-housing-inventory) |
| Housing Inventory submissions are **public** and made under penalty of perjury | "The information entered in the housing inventory submission is public," including owner name and business contact information, approximate square footage, bedrooms, bathrooms, occupancy start date, and base rent in $250 increments. | [sf.gov — Housing Inventory](https://www.sf.gov/rent-board-housing-inventory) |
| Housing Inventory reporting does **not** waive the Rent Board fee | "Reporting into the Rent Board Housing Inventory does not request an exemption of the Rent Board Fee." | [sf.gov — Housing Inventory](https://www.sf.gov/rent-board-housing-inventory) |
| Coverage turns on the build date | Units built on or before 13 June 1979 generally have both rent control and eviction protection; a 1940 building is inside that date if the year is confirmed. | [sf.gov — SF rental laws](https://www.sf.gov/learn-about-san-francisco-rental-laws) · [SF Planning PIM](https://sfplanninggis.org/pim/?pub=true) |
| Algorithmic rent-setting is banned | §37.10C, added by Ord. 224-24 effective 2024-10-14, amended by Ord. 169-25 effective 2025-10-06. Each separate month and each separate unit is a separate violation; penalties up to $1,000 each; the City Attorney, an individual tenant, and (since 2025-10-06) qualifying tenants' rights nonprofits may sue. | [sf.gov — Sec. 37.10C](https://www.sf.gov/information--sec-3710c-use-and-sale-algorithmic-devices-prohibited) · [sf.gov — update notice](https://www.sf.gov/news-update-to-algorithmic-devices-law) |
| A defective notice voids the **whole** increase, with a narrow tolerance | Rules §4.10(b): non-conforming increases are "null and void" unless the amount requested is no more than the allowable annual and banked increase, with a good-faith tolerance of one-half of one percent of the prior base rent — **$19.98** on Unit 1's $3,995.00 and **$15.75** on Unit 2's $3,150.00. Reinforced by Ordinance §37.3(b)(5). | [Rules Part IV §4.10](https://www.sf.gov/reports--december-2022--rent-board-rules-and-regulations-part-iv-rent-increases-not-requiring) · [sf.gov — Sec. 37.3(b)(5)](https://www.sf.gov/information--sec-373-rent-limitations) |
| §4.12(b) requires the banked **dates** in the notice | "which portion of the rent increase reflects banked amount, and (2) the dates upon which said banked amount is based". Omission does not void the increase, unlike §4.10. | [Rules Part IV §4.12(b)](https://www.sf.gov/reports--december-2022--rent-board-rules-and-regulations-part-iv-rent-increases-not-requiring) |
| Retaliation bars an increase | Civ. Code §1942.5(a) bars a rent increase within 180 days of a protected habitability or agency complaint where the tenant is not in default; §1942.5(d) separately bars retaliation for lawful organising; §1942.5(g) preserves a good-faith ground if stated. The site's gate 0.5 and flag F-18 are consistent with the statute it cites. | [Civ. Code §1942.5](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1942.5.&lawCode=CIV) |
| Tenants have free routes to challenge | Tenant petitions carry no filing charge and include an unlawful-rent-increase claim, a lawful-rent determination, and a summary petition based on receipt of an invalid notice. The Rent Board does not adjudicate discrimination, harassment or retaliation. | [sf.gov — Tenant petitions](https://www.sf.gov/tenant-petitions) · [sf.gov — Tenant summary petitions](https://www.sf.gov/information--tenant-summary-petitions) |
| "Reasonable" and "normal business practice" have no official definition | No official source defines either term beyond the Rent Board formula and petition process. The site correctly marks both unverified rather than inventing a benchmark. | [sf.gov — Rent increases](https://www.sf.gov/learn-about-rent-increases-san-francisco) · [sf.gov — About the Rent Board](https://www.sf.gov/departments--rent-board--about) |

---

## 6. Change requests to files owned by other sessions

Logged here rather than applied, per the coordination instructions. `scripts/validate_site.py`,
`scripts/sync_nav.py` and all twelve HTML pages fall within scopes claimed by
`arena/fa7d2d77-rentincreasesf2` (tasks 13–18, marked done) and `arena/2b3012a0-rentincreasesf2`
(tasks 13–15, in progress). This session edited none of them.

| ID | Request | Target file(s) | Exact change |
|---|---|---|---|
| **CR-01** | Add `banking-rule.html` to the shared navigation and to the validator's page list so the new page is not orphaned | `scripts/sync_nav.py`, `scripts/validate_site.py` | Add `("banking-rule.html", "Banking Interval (F-16)")` to the `NAV` list under a *Verification* group, run `python3 scripts/sync_nav.py`, and add `"banking-rule.html"` to `PAGES`. The page already links to all twelve existing pages and carries the standard footer, so it passes the validator as written. |
| **CR-02** | Allowlist the two official URLs this page cites that are not yet in `VERIFIED_URLS` | `scripts/validate_site.py` | `https://sfrb.org/section-1314-licensing-%E2%80%93-notice-rent-increase` and `https://www.sf.gov/sites/default/files/2024-10/538%202024-25%20Bond%20Measure%20Worksheet%2010.24%20.pdf`. Both are official Rent Board documents. |
| **CR-03** | Close flag **F-16** as resolved and cite the test | `flagged.html`, `analysis.html` | Replace the open-conflict wording with: only the per-allowance 12-month test in Rules §4.12(a) reproduces both official worked examples (6.7% and 3.3%); a global-24 reading gives 4.7% against an official 3.3%, and a per-allowance-24 reading gives 5.0% against an official 6.7%. Link `banking-rule.html`. |
| **CR-04** | Publish the closing service window as a deadline (A-02) | `index.html`, `executive-summary.html`, `checklist.html` | Unit 2's 13.1% requires an effective date on or before 2027-02-28, so a 90-day notice must be served by **2026-11-30** (personal delivery) or **2026-11-25** (mail). The mailed route to 2027-02-05 closed on 2026-11-02. Unit 1 needs no urgency: serve by 2027-01-02 for a 2027-02-01 effective date. |
| **CR-05** | Add Rules §13.14's two favourable provisions (A-04, A-05) | `checklist.html`, `laws.html`, `flagged.html` | The license test is applied to the effective date, not the service date; and a void increase does not affect banking rights or the ability to accumulate otherwise lawful increases. |
| **CR-06** | Add irregularity **A-06** to the flagged register | `flagged.html` | The license requirement's start dates differ between the Housing Inventory page (1 July 2022 / 1 March 2023) and Form 538 (1 July 2020 / 1 March 2021). No practical impact; recorded for completeness. |
| **CR-07** | Record the standing rule from A-08 and widen the privacy sweep | `COORDINATION.md`, `scripts/validate_site.py` | Any Markdown at the repository root is publicly served by GitHub Pages. The privacy sweep should scan all root `*.md`, not only the HTML `PAGES` list. |
| **CR-08** | Renumber or annotate the colliding task rows (A-07) | `COORDINATION.md` | Tasks 13–15 exist twice with different meanings and owners. Annotate which session each row belongs to. `arena/2b3012a0-rentincreasesf2` must rebase onto current `main` before opening a PR. |

---

## 7. Reproducibility

```bash
# Site validation (all twelve pages, allowlist, per-row sources, privacy sweep)
python3 scripts/validate_site.py

# Independent re-derivation of every figure and every notice deadline
python3 scripts/verify_calculations.py

# Public-file checks and merge-marker scan (no tenant-specific pattern is stored publicly)
python3 scripts/validate_site.py

# A reviewer may additionally supply private identifier regexes without committing them.
# Example shell syntax only; do not put actual identifiers in a public file or command log:
# PRIVATE_IDENTIFIER_PATTERNS="$private_patterns" python3 scripts/validate_site.py

# Arithmetic used for section 3 and A-02
python3 - <<'PY'
from datetime import date, timedelta
t = date(2026, 11, 7)
for eff, d in [(date(2027,2,5),90),(date(2027,2,15),90),(date(2027,2,28),90),
               (date(2027,2,15),30),(date(2027,2,1),30),(date(2027,6,1),90)]:
    print(eff, "serve by", eff-timedelta(days=d), "| mail by", eff-timedelta(days=d+5),
          "| days from today", (eff-timedelta(days=d)-t).days)
for base, pct in [(3995,1.6),(3995,3.0),(3150,13.1),(3150,10.0),(3150,1.6)]:
    inc = round(base*pct/100, 2); print(base, pct, inc, round(base+inc,2))
PY
```

---

## 8. Official sources read directly during this audit

Fetched and read on 2026-11-07, not quoted from memory or from another session's log.

- Rent Board Rules and Regulations Part IV — §4.10 Notice, §4.11, §4.12 Banking, §4.13 —
  https://www.sf.gov/reports--december-2022--rent-board-rules-and-regulations-part-iv-rent-increases-not-requiring
- Rent Ordinance §37.3 Rent Limitations — (a)(1) annual, (a)(2) banking, (b)(5) nonconforming —
  https://www.sf.gov/information--sec-373-rent-limitations
- Rent Ordinance §37.10C Use and Sale of Algorithmic Devices Prohibited —
  https://www.sf.gov/information--sec-3710c-use-and-sale-algorithmic-devices-prohibited
- Rent Board news — Update to Algorithmic Devices Law —
  https://www.sf.gov/news-update-to-algorithmic-devices-law
- Rent Board Rules §13.14 Licensing – Notice of Rent Increase —
  https://sfrb.org/section-1314-licensing-%E2%80%93-notice-rent-increase
- Form 571 Allowable Annual Increases 26-27 —
  https://www.sf.gov/documents/34344/571_Allowable_Annual_Increases_26-27_1.pdf
- Form 538 2024-25 Bond Measure Worksheet (restates §37.15 / §13.14) —
  https://www.sf.gov/sites/default/files/2024-10/538%202024-25%20Bond%20Measure%20Worksheet%2010.24%20.pdf
- Learn about rent increases in San Francisco (all four worked examples) —
  https://www.sf.gov/learn-about-rent-increases-san-francisco
- Banked rent increases (Topic 503) — https://www.sf.gov/information--banked-rent-increases
- Increasing rents during irregular periods —
  https://www.sf.gov/information--increasing-rents-during-irregular-periods
- Annual rent increase for multiple years —
  https://www.sf.gov/information--annual-rent-increase-multiple-years
- Current Rates, including Rent Increase, Relocation, Sec. Deposit —
  https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit
- The Rent Board Housing Inventory — https://www.sf.gov/rent-board-housing-inventory
- Learn about San Francisco rental laws — https://www.sf.gov/learn-about-san-francisco-rental-laws
- The California Tenant Protection Act of 2019 (AB 1482) —
  https://www.sf.gov/reports--california-tenant-protection-act-2019-ab-1482
- Tenant Petitions — https://www.sf.gov/tenant-petitions
- Tenant and Landlord Resources — https://www.sf.gov/tenant-and-landlord-resources
- Civil Code §827 — https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=827.&lawCode=CIV
- Rent Board Portal — https://portal.sfrb.org/

---

## 9. Audit conclusion

The repository is in good order. **No published figure is wrong, and no value was invented.**
Twelve pages, twenty-two flags and three verification scripts are internally consistent and each
legal and numerical claim traces to an official source.

Ten irregularities are recorded above. Three are **high**: A-02 (the Unit 2 service window closes
on 2026-11-30, and that deadline is not published as a deadline), A-07 (duplicate task numbering
and a stale-based branch that would revert merged work if merged as-is) and A-08 (root Markdown is
publicly served, which is how tenant initials were exposed before PR #10). The remainder are
medium or low and are covered by change requests CR-01 to CR-08.

The one substantive legal question the site left open — flag F-16, the 12-versus-24-month banking
interval — is resolved in section 2 of [`banking-rule.html`](banking-rule.html) by testing all
three readings against both official worked examples. Only Rules §4.12(a)'s per-allowance
12-month test reproduces both, and it confirms the figures the site already publishes: **1.6%**
and **3.0%** for Unit 1, **13.1%** for Unit 2.

**Not legal advice.** This is a documentary audit against official sources. A Rent Board counselor
cannot give legal advice, and no lawyer's approval can be guaranteed in advance.

---

## Addendum — 2026-11-08, corrections applied after PR #16 review

A parallel session (`arena/342c4cc9-rentincreasesf2`, PR #16, branch based on the pre-integration
commit `a747d82`) re-verified the site against primary sources and found four defects. Its branch
duplicates work already merged in PRs #14–#15 and is stale-based, so it was not merged; the
substantive corrections were re-verified here and applied surgically.

| # | Defect | Official source | Disposition |
|---|---|---|---|
| I-01 | This document and `banking-rule.html` quoted "Nonconforming Rent Increases … shall be null and void" as **§ 37.3(a)(5)**. That subsection is the water-charges-and-revenue-bond-passthrough provision. The quoted sentence is **§ 37.3(b)(5)**, inside "Notice of Rent Increase for Tenants in Occupancy". | [sf.gov — Sec. 37.3](https://www.sf.gov/information--sec-373-rent-limitations) (subsection (b)(5), read verbatim 2026-11-08) | Corrected in `banking-rule.html`, `AUDIT.md`, `COORDINATION.md`. Logged on the site as flag **F-25**. |
| I-02 | `units.html` carried pre-integration rows (past "proposed effective date" 2026-04-01, 24-month banking framing, a Unit 1 total of 1.6% contradicting the 3.0% scenario). | — | **Already resolved on `main`** — grep confirms no such rows remain; no change needed. |
| I-03 | `sources.html` was stamped "Verified 2026-11-06" against a later site stamp. | — | Corrected to 2026-11-08. |
| I-04 | `laws.html` said Costa-Hawkins "limits local rent control to units with a certificate of occupancy before 1979". Costa-Hawkins sets no such date; Civ. Code § 1954.52(a) exempts units with a certificate of occupancy issued after 1995-02-01, units already exempt under a local new-construction exemption on or before that date, and separately alienable units. The 1979-06-13 date comes from the Rent Ordinance / Rent Board guidance. | [Civ. Code § 1954.52](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1954.52.&lawCode=CIV) (read verbatim 2026-11-08) · [sf.gov — Rental laws](https://www.sf.gov/learn-about-san-francisco-rental-laws) | Rewritten in `laws.html`; logged as flag **F-26**. |

Two further consistency fixes were applied so every published date and stamp reads 2026-11-08:

- `scripts/verify_calculations.py` — `REVIEW_DATE` moved to 2026-11-08; assertions updated
  (Unit 2 earliest reachable effective date 2027-02-05 → 2027-02-06; days since added occupancy
  220 → 221) and assertions added for the published closing dates (2026-11-30 personal /
  2026-11-25 mailed) across the pages. **47 assertions pass.**
- `banking-rule.html` § 5 ("counted back from today") re-stamped to 2026-11-08 with every
  onward date and day-count recomputed (closing window 22/17 days; Unit 1 earliest reachable
  2026-12-08 personal / 2026-12-13 mailed); `flagged.html`, `occupancy.html`, `index.html`,
  `executive-summary.html`, `checklist.html`, `analysis.html` updated to match.

Full verification after the corrections: `scripts/validate_site.py` PASSED ·
`scripts/verify_calculations.py` PASSED (47 assertions) · tag-balance check OK on all 13 pages ·
zero personal-identifier hits in HTML and root Markdown.

## Addendum — 2026-11-10, residual integration pass (session `arena/d2474b1d-rentincreasesf2`)

This session began its own 2026-11-10 verification pass before knowing that two other sessions had
already published overlapping work. `main` moved twice while it read sources: **PR #22**
(`arena/9b0747eb`, which created flag F-27) and **PR #24** (`arena/d086cb8e`, which re-stamped every
page to 2026-11-10 and corrected its own F-27 citation note). Both are sound and were **not**
re-litigated. This branch was reset to `main` and only the residual differences below were applied.

### Sources fetched and read directly by this session (2026-11-10)

Learn about rent increases · Form 571 (26-27 PDF, full table) · Banked rent increases · Annual rent
increase for multiple years · Increasing rents during irregular periods · Rent Ordinance § 37.3 ·
Housing Inventory · Rules § 13.14 · Civ. Code § 827 · AB 1482 report · Rules 6.14 / Costa-Hawkins ·
Algorithmic devices § 37.10C · Legistar File No. 261020.

Confirmations relevant to the residual work:

- **Banked increases do not expire.** "Once an increase is properly banked, it does not expire. A
  landlord may impose it on a future anniversary date, or at another time when they are allowed to
  raise the rent (as long as at least 12 months have passed since the last increase)."
  ([sf.gov — Banked increases](https://www.sf.gov/information--banked-rent-increases))
- **The percentage is the one in effect on the effective date**, not on the service date.
  ([sf.gov — Learn about rent increases](https://www.sf.gov/learn-about-rent-increases-san-francisco))
- **§ 37.3(a)(2)** ties a banked amount to "the tenant's subsequent rent increase anniversary
  dates". ([sf.gov — § 37.3](https://www.sf.gov/information--sec-373-rent-limitations))
- **A non-anniversary increase is allowed** once 12+ months have passed since the last increase or
  move-in, with 12–24-month and 24-month-plus methods worked out.
  ([sf.gov — Irregular periods](https://www.sf.gov/information--increasing-rents-during-irregular-periods))
- **Legistar File No. 261020** — status **Pending Committee Action**; introduced 2026-09-15;
  Land Use and Transportation Committee; title limits *banked and capital-improvement* increases to
  a total of 10% per year for three years; no enactment date.

### Residual defects corrected on this branch

| # | Defect on `main` | Evidence | Disposition |
|---|---|---|---|
| C-01 | Three pages still said banked amounts "may only be given at the time of an annual increase" and that "the banked 11.5% cannot be imposed on its own later" (`checklist.html` ×2, `banking-rule.html`, `executive-summary.html`). This contradicts the Rent Board: banked increases do not expire during a tenancy and may be imposed on a future anniversary date or another permitted time. It is also the wrong reason for urgency — the owner could act on it and believe the bank itself is forfeited. | [sf.gov — Banked increases](https://www.sf.gov/information--banked-rent-increases) | Rewritten in all four places. What actually closes on 2027-02-28 is the **2026–27 annual component**, because the percentage charged is the one in effect on the effective date. The deadline, the dollar figures and the urgency are unchanged. A forbidden-phrase assertion in `scripts/verify_calculations.py` now fails CI if either sentence returns. |
| C-03 | `units.html` said Unit 1's 1.4% was not banked "because less than 24 full months have passed since the 1.4% … became available". Measured from 2026-02-01 that would put banking at 2028-02-01; the rule is 12 months from availability (Rules § 4.12(a)), which coincides with 24 months from the 2025-02-01 move-in. | [Rules § 4.12](https://www.sf.gov/reports--december-2022--rent-board-rules-and-regulations-part-iv-rent-increases-not-requiring) | Re-measured and restated in `units.html`. |
| C-04 | `units.html` labelled **April 1, 2026** a "Proposed effective date". That date is in the past, and the intake reports it as the continuing tenancy at the unchanged $3,995 — not a proposed increase. Unit 2's row also named the already-passed "June 1, 2026 anniversary". | Intake facts (unverified) | Relabelled "Intake date for the current rent … not a proposed effective date (see F-04)"; Unit 2 now reads "the next reachable anniversary is 2027-06-01". |
| C-06 / F-28 | Not on `main`: § 37.3(a)(2) ties a banked amount to anniversary dates, but the site's suggested Unit 2 effective date (2027-02-15) is not the June 1 anniversary, and the Rent Board's irregular-period guidance allows a non-anniversary date. | [§ 37.3](https://www.sf.gov/information--sec-373-rent-limitations); [Irregular periods](https://www.sf.gov/information--increasing-rents-during-irregular-periods) | New flag **F-28** with both texts, the conservative alternative (2027-06-01, needs the unpublished 2027–28 rate) and a clear-the-flag action row. Not resolved by this session. |
| C-05 | F-27 on `main` said that if the bill were enacted "the phased 10.0% option would be the lawful path", without stating the cap's components. The Legistar title caps **banked + capital-improvement** increases; the annual allowance is not in that list. | [Legistar 261020](https://sfgov.legistar.com/LegislationDetail.aspx?ID=8217304&GUID=7EDA4662-EBFB-4AF5-962F-C669B64AA770) | F-27's existing text is kept; one paragraph added giving the labelled conditional **10% banked + 1.6% annual = 11.6% → $365.40 → $3,515.40**, stated as arithmetic on a bill draft, not law, and asserted by script. The "check immediately before serving" instruction was tightened. |

### Verification

`scripts/validate_site.py` PASSED (13 pages, 49 allowlisted official URLs, per-row sources, column
integrity, privacy sweep over HTML and all root Markdown) · `scripts/verify_calculations.py` PASSED
(**105 assertions**, up from 61: the new conditional, the closing-window arithmetic, and 39
forbidden-phrase checks) · tag balance OK on all 13 pages · all 13 pages, `style.css` and the three
root Markdown files return HTTP 200 from a local static server · zero personal-identifier hits.

**Race record.** No work from PRs #22 or #24 was reverted or edited away; the only edits to
another session's text on this branch are the additive F-27 refinements above, made under the
integration-session prerogative after every other task reached `done`.

## Residual final-integration source check — session `arena/817d1de7-rentincreasesf2`, 2026-11-10

This session independently identified File 261020 and then aligned its branch to the newer integrated
`main` rather than merge duplicate text. The only residual site change is source hardening: the
[official draft ordinance, version 1](https://sfgov.legistar.com/View.ashx?M=F&ID=15865646&GUID=0E2E6936-000B-4597-A4EE-FBB17C19636E)
is now cited directly alongside the [legislation status record](https://sfgov.legistar.com/LegislationDetail.aspx?ID=8217304&GUID=7EDA4662-EBFB-4AF5-962F-C669B64AA770).
Proposed §37.3(h) was read directly. It states the 10% combined banked/capital-improvement limit,
the lowest-base-rent measurement, the 2026-09-15 notice cutoff, and the 2029-12-31 sunset unless
extended. The status remains Pending Committee Action; no enactment is inferred.

Final checks on the integrated tree: 13 pages; 50 allowlisted official URLs; every table row sourced;
column counts valid; no broken internal links or local fragments; balanced HTML; 17 public files
served locally with HTTP 200 and non-empty bodies; no personal identifiers in HTML or public
Markdown; all 105 calculation and forbidden-phrase assertions passed; `git diff --check` passed.

## Addendum — 2026-11-10, final audit and live-defect remediation (session `arena/c71c22cd-rentincreasesf2`)

Arriving on `main` at `9f0531d` and rebasing onto `22bf77d` (after PRs #22–#33), this session inspected every HTML page, CSS
rule, Python validator/calculator script, unmerged branch `arena/2b3012a0-rentincreasesf2`, and the
underlying primary legislative/agency sources directly on 2026-11-10.

### Additional primary official sources read verbatim this session

- [Rent Ordinance § 37.15 — Reporting Obligations; Licensing](https://www.sf.gov/information--sec-3715-reporting-obligations-licensing)
  and [The Rent Ordinance (last amended 11/2/26)](https://www.sf.gov/reports--rent-ordinance)
- [Form 538 — 2026–2027 Bond Measure Worksheet (10.26 PDF)](https://www.sf.gov/documents/64370/538_2026-2027_Bond_Measure_Worksheet_10.26.pdf)
- [The Rent Board Fee (2026–27)](https://www.sf.gov/rent-board-fee)
- File No. 261020 [Leg Ver1](https://sfgov.legistar.com/View.ashx?M=F&ID=15865646&GUID=0E2E6936-000B-4597-A4EE-FBB17C19636E)
  and [Leg Dig Ver1](https://sfgov.legistar.com/View.ashx?M=F&ID=15865647&GUID=CC09B796-4675-4A7D-9960-85FE239F7FBB)
- [Speak with a Rent Board counselor](https://www.sf.gov/speak-rent-board-counselor),
  [Tenant and Landlord Resources](https://www.sf.gov/tenant-and-landlord-resources),
  [Legal resources for housing discrimination](https://www.sf.gov/information/legal-resources-housing-discrimination),
  [Get help for discrimination in housing](https://www.sf.gov/information--get-help-discrimination-housing),
  [Landlord Petitions and Passthroughs](https://www.sf.gov/landlord-petitions-and-passthroughs),
  [Tenant Petitions](https://www.sf.gov/tenant-petitions),
  [Tenant Summary Petitions](https://www.sf.gov/information--tenant-summary-petitions),
  [About Rent Board](https://www.sf.gov/departments--rent-board--about)

### Live defects remediated on `9f0531d`

| # | Defect on `9f0531d` | Evidence / cause | Fix applied |
|---|---|---|---|
| D-01 | `<meta name="description">` missing `content="` attribute in `practices.html:7`, `flagged.html:7`, and `sources.html:7`, causing raw description text inside `<head>`. | Direct HTML parse | Fixed `<meta name="description" content="...">` in all 3 files and added strict `<head>`/`<meta>` & HTML tag-balance checking to `scripts/validate_site.py`. |
| D-02 | Broken Form 538 URL (`2024-10/538%202024-25%20Bond%20Measure%20Worksheet%2010.24%20.pdf`) returned HTTP 500; F-24 / A-06 still printed `2020 / 2021` from the dead PDF while the live Oct 2026 Form 538 prints `July 1, 2021` / `March 1, 2022` (vs. § 37.15(c) `July 1, 2022` / `March 1, 2023`). | Direct fetch (`538_2026-2027_Bond_Measure_Worksheet_10.26.pdf`, `§ 37.15`) | Replaced broken URL across `scripts/validate_site.py`, `flagged.html`, `laws.html`, `banking-rule.html`, `checklist.html`, `sources.html`; updated F-24 / A-06 text; added forbidden check in `verify_calculations.py`. (Historical 2026-11-07 `AUDIT.md` entries preserved with this addendum.) |
| D-03 | C-05 / F-27 in `flagged.html` & `README.md` relied on the Legistar bill title without reading `Leg Ver1` (`ID=15865646`) or `Leg Dig Ver1` (`ID=15865647`). Proposed **§ 37.3(h)** literally bars banked/CI increases *"that cause a tenant's rent to increase by more than a total of 10% of the lowest base rent ... during the 12 months immediately preceding"* through `2029-12-31` (deferred to `2030-01-01+`, retroactive to notices/petitions `>= 2026-09-15`) and adds `§ 37.15(b)(2)(F)` banked-increase Inventory reporting. | Verbatim text of `Leg Ver1` & `Leg Dig Ver1` | Updated F-27, `index.html`, `executive-summary.html`, `analysis.html`, `laws.html`, `checklist.html`, `README.md` to state the exact § 37.3(h) & § 37.15(b)(2)(F) terms, explain why literal § 37.3(h) puts even 11.6% (`10% banked + 1.6% annual`) at risk vs. phased **10.0% ($315.00 → $3,465.00)**, and add `Leg Ver1`/`Leg Dig Ver1` links. |
| D-04 | `units.html` (`Total allowable if banked` + `Calculation inputs and results` table) and `index.html` (`Unit 1 maximum at 1.6%` key-findings row) omitted Unit 1's `2027-02-01` `3.0%` (`$119.85 → $4,114.85`) option; `index.html` directory omitted `occupancy.html`, `checklist.html`, `banking-rule.html`; `index.html` Flags row said `F-01 to F-24` instead of `F-01 to F-28`. | Cross-page consistency audit | Reconciled both tables in `units.html` & `index.html`, completed the 13-page directory in `index.html`, updated Flags row to `F-01 to F-28`, and added `units.html` dollar assertions to `verify_calculations.py`. |
| D-05 | `tenant-protections.html` attributed `"proof of income may be required"` to Housing Rights Committee (absent from `sf.gov/tenant-and-landlord-resources`) and omitted Open Door Legal's published limited ZIP coverage (`94107, 94112, 94124, & 94134`, excluding 94122). | Verbatim SF.gov clinic pages | Corrected HRC, flagged Open Door Legal's ZIP-94122 exclusion, updated Bay Area Legal Aid / EDC / Rent Board hours, and added Legal Assistance to the Elderly and BASF LRIS / Conflict Intervention Service. |
| D-06 | `sources.html` omitted allowlisted URLs (`Civ. Code § 1954.52`, `departments--rent-board`, Form 538) and kept `2026-11-07` stamps on six sources re-fetched today; Rent Board Fee 2026–27 rate (`$59.00/unit`, `2026-12-14` exemption, `2027-03-01` due) was absent from F-13 / `laws.html` / `executive-summary.html`. | Allowlist diff & `sf.gov/rent-board-fee` | Synced `sources.html` with 100% of `VERIFIED_URLS` (enforced by `validate_site.py`), updated stamps for sources re-verified today to `2026-11-10`, added `§ 37.15`, and added verified 2026–27 Rent Board Fee details across F-13, `laws.html`, `executive-summary.html`, `sources.html`. |



---

---

## Verification record — session `arena/d2789389-rentincreasesf2` (2026-11-10, tasks 46–48)

Third independent pass on the same day. This session re-read the controlling sources **live**,
rather than adopting any earlier session's summary, and then checked every row of the published
site against the text it had just read.

### Sources read verbatim this session

| Source | What it was read to confirm |
|---|---|
| [Current Rates](https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit) | 1.6% for 3/1/2026–2/28/2027; 1.4% for 3/1/2025–2/28/2026; 1.7% for 3/1/2024–2/28/2025; the 2026-11-09 File 261020 notice reproduced on the page. |
| [Form 571 (26–27)](https://www.sf.gov/documents/34344/571_Allowable_Annual_Increases_26-27_1.pdf) | The full historical percentage table, row by row, from 4/1/82 to 3/1/26–2/28/27. **Confirms the table ends at 2/28/27** — the 2027–28 row does not exist, which is why F-17 stays blank. |
| [Banked rent increases](https://www.sf.gov/information--banked-rent-increases) | 24-month phrasing; "does not expire"; no limit; not compounded; no rounding up; does not carry over to a new tenant; the July 1, 2022 / March 1, 2023 licence dates; notice content; the "use the percentage in effect on the date of the increase" rule. |
| [Learn about rent increases](https://www.sf.gov/learn-about-rent-increases-san-francisco) | 1.6%; licence-before-imposing; 30/90-day notice; +5 if mailed; additional-occupant prohibition; **worked example 4** (the 1.7% banks, the 1.4% is "permanently lost due to the change in anniversary date") — the decisive test for F-16. |
| [Irregular periods](https://www.sf.gov/information--increasing-rents-during-irregular-periods) | 12–24 month and 24+ month options; "landlords must consider the trade-off"; anniversary dates are easiest. |
| [Annual rent increase for multiple years](https://www.sf.gov/information--annual-rent-increase-multiple-years) | Percentages are added, not compounded; no rounding up; no petition needed. |
| [Rules § 13.14](https://sfrb.org/section-1314-licensing-%E2%80%93-notice-rent-increase) | "the effective date of the rent increase, not the date of service"; null and void in its entirety; banking rights survive. |
| [Rent Ordinance § 37.15](https://www.sf.gov/information--sec-3715-reporting-obligations-licensing) | § 37.15(c) phase-in dates; § 37.15(e) substantial-compliance licence and suspension; 30-day contact updates. |
| [Rent Ordinance § 37.3](https://www.sf.gov/information--sec-373-rent-limitations) | § 37.3(a)(1) 60%-of-CPI / 7% cap; (a)(2) banking; (a)(8) petition above the allowance; (a)(11)(A) additional-occupant prohibition; **§ 37.3(b)** notice content; **(b)(5)** nonconforming increase null and void. |
| [Housing Inventory](https://www.sf.gov/rent-board-housing-inventory) | "All owners of residential property are required to report"; licence auto-generated; "does not need to be included with your rent increase notice"; information entered is public; penalty of perjury. |
| [Notice of Owner Noncompliance](https://www.sf.gov/notice-of-owner-noncompliance-with-housing-inventory) | "may apply for multiple years"; the Portal licence-status procedure; the tenant petition routes. |
| [Rules Part IV, §§ 4.10 & 4.12](https://www.sf.gov/reports--december-2022--rent-board-rules-and-regulations-part-iv-rent-increases-not-requiring) | § 4.10(a) notice breakdown and (b) the null-and-void rule with the half-percent good-faith allowance. |
| [Rent Board Fee](https://www.sf.gov/rent-board-fee) | $59.00 per dwelling unit for 2026–27; $29.50 recoverable once paid in full, tenants in occupancy on November 1; exemption deadline **2026-12-14**; due **2027-03-01**; exemption ≠ Inventory reporting. |
| [AB 1482 (sf.gov)](https://www.sf.gov/reports--california-tenant-protection-act-2019-ab-1482) | 8.8% for 8/1/2026–7/31/2027 **and** "This does NOT apply for units under the rent increase limitations of the San Francisco Rent Ordinance". |
| [Civ. Code § 1947.12](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1947.12.&lawCode=CIV) | 5% + CPI / 10% cap; (d)(3) local-rent-control exemption. |
| [Civ. Code § 827](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=827.&lawCode=CIV) | (b)(1) service methods; (b)(2) 30 days at ≤10%; (b)(3)(A) 90 days above 10%. |
| [Civ. Code § 1942.5](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1942.5.&lawCode=CIV) | The five 180-day triggers, the latest-date rule, once per 12 months, the organising bar, the immigration-report bar. |
| [Civ. Code § 1954.52](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1954.52.&lawCode=CIV) | (a)(1) post-1995-02-01 certificate of occupancy; (a)(3) separately alienable units. **Confirmed Costa-Hawkins does not contain the 1979 date** — the site's F-26 correction is right. |
| [Algorithmic devices § 37.10C](https://www.sf.gov/information--algorithmic-devices-set-rent-are-prohibited-san-francisco) | Effective 2024-10-14; each unit and each month a separate violation; tenant or tenants'-rights-organisation civil action; $1,000 per violation. |
| [Learn about SF rental laws](https://www.sf.gov/learn-about-san-francisco-rental-laws) | **"If your unit was built before June 14, 1979, and is not used as a single family dwelling, it may have both" rent control and eviction protection.** The two-limb coverage test — the basis of correction F-33. |
| [Costa-Hawkins partial exemption](https://www.sf.gov/information--partial-exemption-certain-single-family-homes-and-condominiums-under-costa-hawkins) | "A single-family dwelling with a legal in-law unit constitutes a two-unit building and is not exempt." |
| [Rules 6.14 and Costa-Hawkins](https://www.sf.gov/information--rent-increases-under-section-614-and-costa-hawkins) | Last-original-occupant test; 60 days generally reasonable; co-tenant never reached. |
| [Additional occupants prohibited](https://www.sf.gov/information--charging-additional-occupants-prohibited) | Unlawful even if the lease permits it; tenant may petition to void and recover. |
| [Landlord Petitions and Passthroughs](https://www.sf.gov/landlord-petitions-and-passthroughs) | Six petition types; **"landlords must file a petition at the Rent Board before serving the tenants with a notice"**; no charge. |
| [Tenant Petitions](https://www.sf.gov/tenant-petitions) / [Tenant Summary Petitions](https://www.sf.gov/information--tenant-summary-petitions) | No filing charge; the Board "do[es] not adjudicate issues that are not related to the amount of rent charged, such as harassment, discrimination and retaliation". |
| [Speak with a Rent Board counselor](https://www.sf.gov/speak-rent-board-counselor) | Free; English/Spanish/Cantonese/Mandarin plus interpretation; calls ~5 min, drop-in ~10 min; "We cannot give legal advice". |
| [Tenant and Landlord Resources](https://www.sf.gov/tenant-and-landlord-resources) / [Legal resources](https://www.sf.gov/information/legal-resources-housing-discrimination) | Every clinic detail the site publishes: EDC, Bay Area Legal Aid, Housing Rights Committee, Open Door Legal's four ZIPs, Tenderloin Housing Clinic, Legal Assistance to the Elderly, BASF LRIS and CIS. **All match.** |
| [Form 538 (2026–27)](https://www.sf.gov/documents/64370/538_2026-2027_Bond_Measure_Worksheet_10.26.pdf) | Live PDF; prints "July 1, 2021 for buildings with ten or more residential units" and "March 1, 2022" for condominiums and buildings with fewer than ten — the A-06 / F-24 inconsistency is real and is correctly described. |
| [File 261020 Legistar](https://sfgov.legistar.com/LegislationDetail.aspx?ID=8217304&GUID=7EDA4662-EBFB-4AF5-962F-C669B64AA770) | Status **Pending Committee Action** as at 2026-11-10; history is 4 records, latest 10/7/2026 Youth Commission response; no committee hearing, no enactment. |
| [File 261020 Leg Ver1](https://sfgov.legistar.com/View.ashx?M=F&ID=15865646&GUID=0E2E6936-000B-4597-A4EE-FBB17C19636E) | Proposed § 37.3(h) text read in full: 10% of "the lowest base rent that was in effect at any time during the 12 months immediately preceding", notices/petitions on or after 2026-09-15, to 2029-12-31 unless extended, excess recoverable on or after 2030-01-01. |

### Corrections made on the evidence (this session)

| # | What was wrong | What the source says | Fix |
|---|---|---|---|
| F-33 | `laws.html` and `units.html` said a 1940 building "would be covered if the build year is confirmed". That states one limb of a two-limb test, and leaves the site's own "two-unit buildings are not exempt" statement unattributed. | Rental laws: built before 1979-06-14 **and** not used as a single-family dwelling. Costa-Hawkins page: an in-law unit makes it a two-unit building, not exempt. | Both rows and the Executive Summary now state the two-limb test, attribute the second limb, and label the whole thing conditional on the unverified build year and unit count. |
| F-34 | The federal row asserted that no federal rent ceiling applies, with no source that says so. | No official page located states it. A negative that broad cannot be verified by citation. | The row now says explicitly that no federal statute or agency page **located in this review** sets a dollar ceiling, and identifies the verified federal limit (the anti-discrimination rule), with both links retained. |

### What was checked and found correct (no change)

- Every dollar figure: `$119.85 / $4,114.85 / $63.92 / $4,058.92 / $412.65 / $3,562.65 / $315.00 / $3,465.00` — re-derived independently from the 571 table, then confirmed against the published HTML by 176 script assertions.
- Every deadline: `2027-01-02`, `2026-12-28`, `2026-11-17`, `2026-11-12`, `2026-11-30`, `2026-11-25`, `2027-02-08`, `2027-02-13`, `2027-01-16`, `2027-03-03` — all consistent with § 827 and the +5-day mailed rule.
- The banked ledger: six components `1.8 + 0.7 + 2.3 + 3.6 + 1.7 + 1.4 = 11.5`, added not compounded, each matched to its 571 row.
- The F-16 resolution: both official worked examples reproduce under the per-allowance 12-month reading and under no other.
- The tenant-resource table: contact numbers, addresses, hours and ZIP scope all match the two cited SF.gov pages.

### New this session

- `answers.html` — every owner question answered in turn, one row each, with a status and an official source on every row, and an explicit "still open" table. Assertions added to `scripts/verify_calculations.py` so its figures cannot drift from the rest of the site.
- `internal/README.md` — how personal information is handled, and why the identity mapping is deliberately **not** in this repository (GitHub Pages publishes the repository root, so an "internal" file here would be public). No personal data in it.

## Addendum — independent verification pass on `cd005f7` (session `arena/22c8ef1e`, 2026-11-10)

Branch: `arena/22c8ef1e-rentincreasesf2`, branched from `main` at `cd005f7` (PR #36 merge).
Method: every source below was fetched and read **directly on 2026-11-10**. Nothing in this
addendum is inferred from an earlier session's notes; where a value could not be confirmed it is
left blank or flagged.

### Primary sources read live this session

| Source | What was confirmed verbatim |
|---|---|
| [sf.gov — Rent Board Housing Inventory](https://www.sf.gov/rent-board-housing-inventory) | "All owners of residential property are required to report." Reporting a tenant-occupied unit generates the licence; the licence is **automatically generated**; "A landlord must have a current rent increase license on file with the Rent Board before any annual or banked rent increase can go into effect. The rent increase license does not need to be included with your rent increase notice." Deadline **March 1 of every year**; late filing still produces a licence but "your rent increase notice will not be enforceable without having a rent increase license on the effective date of the notice." Tier dates: **2022-07-01** for units (other than condominiums) in buildings with **10+** units; **2023-03-01** for condominiums and buildings with **fewer than 10** units. Contact changes within 30 days. Submissions are public and under penalty of perjury. |
| [sf.gov — Learn about rent increases](https://www.sf.gov/learn-about-rent-increases-san-francisco) | Allowable increase **1.6%**, effective **2026-03-01 through 2027-02-28**, based on 60% of Bay Area CPI. 30-day notice; **90-day if the increase (by itself or combined with another increase in the same year) is more than 10%**; **+5 days if mailed**. Notice must state dollar amount, percentage and effective date. "The landlord should use the percentage that will be in effect on the date of the increase, not the percentage in effect on the date they serve the notice." No extra rent for an additional occupant. File 261020 notice **posted 2026-11-09**. |
| [sf.gov — Banked rent increases](https://sf.gov/information/banked-rent-increases) | "A skipped increase is only banked if **at least 24 full months pass** without any rent increase." "Once an increase is properly banked, it **does not expire**." Banked increases may be imposed "on a future anniversary date, **or at another time when they are allowed to raise the rent** (as long as at least 12 months have passed since the last increase)… This may create a new anniversary date." Banked amounts cannot be compounded or prorated; add the yearly percentages, then multiply by current base rent. Notice must also state **which part of the increase is banked**. |
| [Form 571 Allowable Annual Increases 26-27](https://www.sf.gov/documents/34344/571_Allowable_Annual_Increases_26-27_1.pdf) | Rate table read directly: 3/1/26–2/28/27 **1.6%**; 3/1/25–2/28/26 **1.4%**; 3/1/24–2/28/25 **1.7%**; 3/1/23–2/29/24 **3.6%**; 3/1/22–2/28/23 **2.3%**; 3/1/21–2/28/22 **0.7%**; 3/1/20–2/28/21 **1.8%**; 3/1/19–2/29/20 **2.6%**. |
| [Legistar — File No. 261020](https://sfgov.legistar.com/LegislationDetail.aspx?ID=8217304&GUID=7EDA4662-EBFB-4AF5-962F-C669B64AA770) | Re-checked 2026-11-10: Type **Ordinance**; Status **Pending Committee Action**; Introduced **9/15/2026**; In control: Land Use and Transportation Committee; **Enactment date blank; Enactment # blank**. Latest action **10/7/2026 Youth Commission RESPONSE RECEIVED**. Confirms the site's "not enacted" wording is still correct. |
| [Civ. Code § 827](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=827.&lawCode=CIV) | (b)(2) **30 days** where the increase is "10 percent or less … either in and of itself or when combined with any other rent increases for the 12 months before the effective date"; (b)(3)(A) **90 days** where it is "greater than 10 percent"; (b)(1)(B) service by mail under CCP § 1013. |
| [sf.gov — AB 1482](https://www.sf.gov/reports--california-tenant-protection-act-2019-ab-1482) | "The maximum rent increase for units under AB 1482 from **August 1, 2026 to July 31, 2027 is 8.8%** in San Francisco. **This does NOT apply for units under the rent increase limitations of the San Francisco Rent Ordinance.**" (5% + 3.8% CPI). |
| [sf.gov — Learn about San Francisco rental laws](https://www.sf.gov/learn-about-san-francisco-rental-laws) | Coverage threshold **1979-06-13**. Units with eviction protection but **no** rent control: built after 1979-06-13; most single-family homes and condos (occupancy on/after 1996-01-01); substantial rehabilitation; units regulated by another government agency. Eight categories fully exempt from the Rent Ordinance. |

### Independent re-derivation of every published figure (base date 2026-11-10)

**Unit 1** — base rent $3,995.00, tenancy began 2025-02-01.
- Anniversary 2026-02-01 fell in 3/1/25–2/28/26 → allowance **1.4%**; skipped.
- 2025-02-01 → 2027-02-01 is **24 full months**, so the skipped 1.4% is banked ("at least 24 full months pass without any rent increase"). ✔
- Current annual at 2027-02-01 = **1.6%**. Total **3.0%**.
- $3,995.00 × 0.030 = **$119.85** → new base rent **$4,114.85**. ✔ matches site.
- 3.0% ≤ 10% → 30 days (§ 827(b)(2)). 2027-02-01 − 30 d = **2027-01-02**; mailed +5 d = **2026-12-28**. ✔ matches site.

**Unit 2** — base rent $3,150.00, tenancy began 2019-06-01, no increase ever imposed (owner-supplied, F-06).
- Banked anniversaries 6/1/2020 … 6/1/2025: 1.8 + 0.7 + 2.3 + 3.6 + 1.7 + 1.4 = **11.5%**. ✔ (each of these has had ≥24 months pass)
- Current annual component = the percentage in effect on the effective date = **1.6%**.
- Total **13.1%**. $3,150.00 × 0.131 = **$412.65** → new base rent **$3,562.65**. ✔ matches site.
- 13.1% > 10% → **90 days** (§ 827(b)(3)(A)). 2027-02-15 − 90 d = **2026-11-17**; mailed +5 d = **2026-11-12**. ✔ matches site.
- Last day of the published 1.6% window is 2027-02-28; 2027-02-28 − 90 d = **2026-11-30** (personal) / **2026-11-25** (mail). ✔ matches site.
- Earliest reachable effective date from 2026-11-10: +90 d = **2027-02-08** (personal), +95 d = **2027-02-13** (mail). ✔ matches site.
- Phased option: $3,150.00 × 0.100 = **$315.00** → **$3,465.00**, 30-day notice (10.0% is not "greater than 10 percent"). ✔ matches site.

**Nothing was inferred.** Where the owner's intake is the only evidence (build year, unit count,
rent ledger, licence status, occupancy), the figure is flagged, not verified.

### Defects found and fixed this session

| # | Defect | Evidence / cause | Fix | Status after rebase |
|---|---|---|---|---|
| D-07 | `AUDIT.md` carried a stray, unresolved git merge marker (the `97aadef` conflict-resolution line). On `cd005f7` it was the last line of the file; by the time of this session's rebase a concurrent session had appended its own record after it, leaving raw conflict text **mid-file**, still published on the public site. | Direct read of `AUDIT.md` (line 395 on `cd005f7`; still present on `a791240`) | Marker line removed. Added a merge-marker guard to `scripts/validate_site.py` covering `*.html`, `*.md`, `*.css` and `scripts/*.py`, so this class of defect fails CI instead of shipping. Guard verified to fail on an injected `<<<<<<<` marker and to pass once removed. | **Fixed — still unique to this session.** No other session had removed it or guarded against it. |
| D-08 | `executive-summary.html` asserted as fact that "Your building is in scope" and "A two-unit building falls in that second group." The intake names two units, but no official source establishes the building's **total** residential unit count, which is what selects the 1-9 vs 10+ licensing tier, nor does it rule out a coverage exception. Raised as a review request by session `arena/0e02b0ec` (PR #36). | Housing Inventory tier dates; rental-laws coverage-exception list | **Superseded, not published.** Session `arena/f6a65204` reached the same finding independently and published it as **F-31** (PR #40, `d6d565e`). Their wording is preserved verbatim on `main`; this session dropped its duplicate F-31 row during the rebase rather than shipping two flags with one ID. | **Superseded by F-31 (PR #40).** |
| D-09 | The executive summary's "Lawful total on that date" row read as an unconditional entitlement. | Same review request | Partly superseded. `main` already labels the row `(conditional)` and lists conditions (1)-(4) plus F-27. This session kept `main`'s text and appended the two points it did not have: **F-28** (Unit 2's 2027-02-15 effective date is a non-anniversary date pending Rent Board counselor review) and an explicit statement that no official source guarantees a tenant lawyer, the Rent Board or a court would approve the notices. | **Merged additively - both sessions' text retained.** |
| D-10 | `index.html` and `README.md` described the flag range as F-01-F-30. | Cross-page consistency | Superseded: `main` now runs F-01-F-34 (F-33 coverage condition and F-34 federal label, both from `arena/d2789389`). | **Superseded.** |

### Concurrency note

This session began work on `cd005f7`. By the time it rebased, four other sessions had landed
PRs #37-#44 on `main`. The rebase produced conflicts in `COORDINATION.md`, `AUDIT.md`,
`executive-summary.html`, `flagged.html`, `index.html` and `README.md`. Every conflict was resolved
by keeping **main's** version where the two overlapped and adding only what was genuinely missing.
A line-by-line check confirmed that no line of `main`'s `AUDIT.md` was lost except the stray
conflict marker (D-07, intended) and the closing line, which was moved to the end of the file. No
other session's flag, page or wording was altered.

### Not changed

No percentage, dollar amount, statutory citation or deadline was altered. Every published figure
re-derived identically from the live sources above. File 261020 remains **not enacted** as of
2026-11-10.

**Not legal advice.** Documentary verification against official sources only.
## Addendum E — residual source and publication-integrity audit (2026-11-10)

This addendum covers the final residual review after PR #40 integrated F-31. Owner-supplied facts
remain unverified; no personal identifier is reproduced here. Historical entries above are retained
as historical records even where later corrections supersede their wording.

| # | Residual defect | Primary evidence | Correction / verification |
|---|---|---|---|
| E-01 | Public code and an audit example embedded tenant-specific matching patterns; the old privacy check covered HTML/Markdown and could echo a matched pattern. | Repository inspection; [Housing Inventory public-submission warning](https://www.sf.gov/rent-board-housing-inventory) | Removed the patterns without reproducing them. `validate_site.py` now accepts optional private patterns only through `PRIVATE_IDENTIFIER_PATTERNS`, never prints them, and recursively scans all public text files, including `internal/`, scripts and workflows. F-36 records that current-file removal does not erase Git history. |
| E-02 | `AUDIT.md` retained a merge marker; one dashboard table row had only internal links although its header promised an official source. | Repository parse and strengthened validator | Removed the marker, added the official banking source to the row, added public-text merge-marker checks, and required an external official link in every table data row. |
| E-03 | AB 1482 was called a statewide “floor”; algorithm wording could be read to prohibit ordinary management software; frequency was reduced to “on the anniversary.” | [Civ. Code § 1947.12(a), (d)(3)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1947.12.&lawCode=CIV), [SF AB 1482 guidance](https://www.sf.gov/reports--california-tenant-protection-act-2019-ab-1482), [SF algorithmic-device guidance](https://www.sf.gov/information--algorithmic-devices-set-rent-are-prohibited-san-francisco), [irregular-period guidance](https://www.sf.gov/information--increasing-rents-during-irregular-periods) | Published the state cap/local exemption relationship, the non-public competitor-data scope and ordinary-software exclusion, and the off-anniversary/new-anniversary rule. F-35 records the corrections. |
| E-04 | Some pages called Unit 2’s 13.1% “lawful” based principally on arithmetic, despite open coverage, license, ledger, conduct and F-28 questions. | [Banked-increase guidance](https://www.sf.gov/information--banked-rent-increases), [Rules § 13.14](https://sfrb.org/section-1314-licensing-%E2%80%93-notice-rent-increase), [Civ. Code § 1942.5](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1942.5.&lawCode=CIV) | Recast every such statement as conditional arithmetic. The current absence of the proposed 10% cap is not a legal clearance. Added Gate 0 checks for F-31 and F-28. |
| E-05 | F-28 cited the ordinance/guidance difference but omitted Rules § 4.12(a)’s express annual-increase timing sentence. | [Rules § 4.12(a)](https://www.sf.gov/reports--december-2022--rent-board-rules-and-regulations-part-iv-rent-increases-not-requiring), [banked-increase guidance](https://www.sf.gov/information--banked-rent-increases), [irregular-period guidance](https://www.sf.gov/information--increasing-rents-during-irregular-periods) | Published the exact sentence in `laws.html`, `flagged.html` and `banking-rule.html`; explained that 10.0%/13.1% scenarios pair banked amounts with current annual 1.6%; retained counselor/counsel review. Removed the regression rule that forbade quoting the regulation. |
| E-06 | The scenario set lacked the lowest-friction increase and sometimes attached F-28 even to an option using no banked amount. | Current 1.6% rate in [Form 571](https://www.sf.gov/documents/34344/571_Allowable_Annual_Increases_26-27_1.pdf); [partial-increase guidance](https://www.sf.gov/information--banked-rent-increases) | Added Unit 2 annual-only 1.6% = **$50.40 → $3,200.40**, leaving 11.5% banked. Clarified that F-28’s banked-timing issue does not arise for this option, while ordinary legal gates and the new-anniversary rule still apply. |
| E-07 | “Only by petition” and “all housing providers” were overbroad shorthand. | [Landlord petitions](https://www.sf.gov/landlord-petitions-and-passthroughs), [Rules 6.14 / Costa-Hawkins](https://www.sf.gov/information--rent-increases-under-section-614-and-costa-hawkins), [42 U.S.C. ch. 45](https://www.govinfo.gov/content/pkg/USCODE-2024-title42/html/USCODE-2024-title42-chap45.htm) | Distinguished petition/worksheet routes from the optional-petition Rules 6.14 route and noted that federal statutory exemptions are not established for this property. |
| E-08 | Concurrent PRs #44/#48 added `answers.html`, F-33/F-34 and `internal/README.md`; the new Q&A repeated unconditional legal wording, and the internal note instructed future editors to commit private patterns. Older rows also still treated build year as the only coverage condition. | Concurrent source diff plus the same primary sources above; [rental-laws coverage test](https://www.sf.gov/learn-about-san-francisco-rental-laws) | Preserved the new page and F-33/F-34. Applied the same conditional/scenario corrections to Q&A, renumbered this session’s new flags F-35/F-36, made privacy scanning recursive, removed the unsafe instruction, and propagated the two-limb coverage test into F-01/F-26, checklist, process, summary, laws and units. |

### Checks after Addendum E

- `python3 scripts/sync_nav.py`: 14 pages, 0 updates.
- `python3 scripts/validate_site.py`: 14 pages; 52 allowlisted official URLs; external official
  source on every table data row; valid structure, columns and internal links; public-text merge
  marker scan; optional private-pattern interface (no tenant-specific pattern stored).
- `python3 scripts/verify_calculations.py`: **315 assertions passed**, including the annual-only
  scenario, required Rules § 4.12 disclosure, corrected legal wording and forbidden overstatements.
- Negative validator test: generic probe in `internal/` detected without echoing the pattern;
  merge markers and an unresolved cross-page fragment also detected; probes removed.
- Local HTTP: 14 pages and 17 unique internal/public resources returned HTTP 200, including Q&A,
  `style.css`, `AUDIT.md` and `internal/README.md`; titles/H1/main landmarks and fragments checked.
- `git diff --check`: passed. PR, merge and deployment results are recorded in `COORDINATION.md`.

---

## Addendum F — re-verification pass on 2026-11-11 (session `arena/edd919ec-rentincreasesf2`)

**Method.** Every controlling source was fetched and read directly on 2026-11-11, not carried over from
the 2026-11-10 passes. The published site was then diffed against the fetched text, and every today-relative
figure was re-derived from a base date of 2026-11-11. The session record, the full source list and the
per-file change list are in `COORDINATION.md` (section "2026-11-11 independent re-verification pass").

### 1. Sources read directly (result: no substantive change)

| Source | Verdict on 2026-11-11 |
|---|---|
| Current Rates | 1.6% (2026-03-01–2027-02-28); 1.4%; 1.7%. Unchanged. File 261020 notice still posted 2026-11-09. |
| Form 571 (26-27 PDF) | Historical table unchanged; ends 2027-02-28; 2027-28 blank. |
| Learn about rent increases | 1.6%; 30/90 + 5; four worked examples unchanged, including the 3.3% new-anniversary example. |
| Banked rent increases | Mechanics unchanged; 24-month summary wording still present (F-16 as resolved). |
| Housing Inventory | "All owners of residential property"; tenant-occupied units receive the licence; licence current before the increase takes effect; not attached to the notice; 2023-03-01 for <10 units. |
| § 37.15 | (a), (c), (e) verbatim as published on the site. |
| Rules § 13.14 | Effective-date-not-service-date rule; entire increase void if unlicensed; banking rights survive. |
| Rules Part IV §§ 4.10, 4.12 | § 4.12(a) verbatim, including the 12-month sentence and the "only … at the time of an annual increase" sentence. |
| § 37.3 | 60% of CPI, 7% cap; (a)(2) banking on "subsequent rent increase anniversary dates". |
| Irregular periods | Non-anniversary increases permitted; "24 months or more" example applies three prior periods to a non-anniversary date. |
| Rental laws | Coverage requires built before 1979-06-14 **and** not used as a single-family dwelling. |
| Costa-Hawkins partial exemption | Legal or illegal in-law unit ⇒ two-unit building, not exempt (F-33). |
| Topic 153 (6.14 / Costa-Hawkins) | "within a reasonable time"; "generally, sixty days is considered reasonable". |
| Rent Board Fee | $59.00/unit 2026-27; 50% recoverable; exemption 2026-12-14; due 2027-03-01. |
| AB 1482 | 8.8% (2026-08-01–2027-07-31); "does NOT apply" to units under the SF rent-increase limitations. |
| Legistar File 261020 | Pending Committee Action; introduced 2026-09-15; 4 history records; not enacted. |

### 2. Arithmetic re-derived from 2026-11-11 (all confirmed)

| Figure | Derivation | Result |
|---|---|---|
| Unit 1, early | 3,995.00 × 1.6% | $63.92 → $4,058.92 |
| Unit 1, 2027-02-01 | (1.4 + 1.6) = 3.0%; 3,995.00 × 3.0% | $119.85 → $4,114.85 |
| Unit 2 banked | 1.8 + 0.7 + 2.3 + 3.6 + 1.7 + 1.4, added | 11.5% |
| Unit 2, 2027-02-15 | (11.5 + 1.6) = 13.1%; 3,150.00 × 13.1% | $412.65 → $3,562.65 |
| Unit 2, annual-only | 3,150.00 × 1.6% | $50.40 → $3,200.40 |
| Unit 2, phased | 3,150.00 × 10.0%; 13.1 − 10.0 left banked | $315.00 → $3,465.00; 3.1% banked |
| **Unit 2, banked-only on 2027-06-01 (new, F-38)** | 3,150.00 × 11.5% | **$362.25 → $3,512.25** |
| Notice period, banked-only | 11.5% > 10% ⇒ 90 days (+5 mailed) | serve by 2027-03-03 (mail 2027-02-26) |
| Earliest effective from 2026-11-11 | +90 d / +95 d | 2027-02-09 / 2027-02-14 |
| Unit 1 earliest from 2026-11-11 | +30 d / +35 d | 2026-12-11 / 2026-12-16 |
| Days since added occupancy | 2026-04-01 → 2026-11-11 | 224 days |

### 3. Defect found and fixed in the calculator

`scripts/verify_calculations.py` compared four computed dates and one computed day-count against
**hand-typed** values (`date(2027, 2, 8)`, `date(2027, 2, 13)`, `date(2026, 12, 10)`, `date(2026, 12, 15)`,
`223`). Those constants encode the 2026-11-10 base date, so on any later base date the script reports a
failure that describes the *test* rather than the site, and a careless session could "fix" it by editing the
site to match the stale constant. All five now compute from `REVIEW_DATE` and assert that the **printed
string** appears on every page that publishes it, so a base-date drift fails as drift. Assertions 315 → 334.

### 4. Additions, and why they are not conclusions

- **F-38** publishes a Unit 2 banked-only increase on the tenant's own anniversary. It exists because both
  published options that use the banked balance impose it off-anniversary (F-28), and the option that avoids
  F-28 entirely uses no banked amount at all. The new option is arithmetic on an unverified base rent and is
  labelled as such; it states that it would exceed the *proposed* 10% cap in File 261020 if enacted, and
  that ledger, coverage, licence, retaliation and discrimination reviews all still apply.
- **F-28** was corrected: its action line had said no dollar figure could be stated for the anniversary date,
  which the new option makes obsolete. Its record now also cites the Board's own non-anniversary example.

### 5. Standing irregularities (unchanged, published for review)

F-01 build year / coverage · F-02 lease facts · F-03 licence status · F-06 Unit 2 ledger · F-15 6.14 notice
timing · F-17 2027-28 rate unpublished · F-18 retaliation screen · F-27 pending File 261020 · F-28
off-anniversary timing · F-31 unit count · F-33 coverage second limb · F-34 federal "no ceiling" as an
absence of source · F-38 new option (F-37 on main is PR #53's notice/retaliation flag). None blocks publication. Six `sources.html` rows keep their
2026-11-10 badge because they were not re-read in this pass; that is recorded in `COORDINATION.md`.

### 6. Rebase onto PR #51 and cross-session re-check of its new content

Rebased onto `28e9a22` (PR #51, session `arena/e7ea8610`). Both conflicts — `COORDINATION.md` (append
boundary) and `sources.html` (three new source rows) — were resolved by keeping main's content and
re-applying this session's date stamps, and the resolution is recorded in `COORDINATION.md`. The new rows
introduced by PR #51 were then fetched and read verbatim in this pass:

| New source | Verdict |
|---|---|
| [§ 37.11A Civil Actions](https://www.sf.gov/information--sec-3711a-civil-actions) | Confirmed: tenant action for injunctive relief/damages over excess rent or retaliation; money awards for overpayments from a § 37.3(b)(5) void increase limited to the three-year period preceding the month of filing; prevailing party recovers fees and costs. |
| [§ 37.10B Tenant Harassment](https://www.sf.gov/information--sec-3710b-tenant-harassment) | Confirmed, with one qualifier: the rent-increase example in (a)(5) concerns a unit **exempt** from the increase limitations under § 37.3(d) or § 37.3(g). The `sources.html` row omitted that limitation; it was tightened to describe the rent-increase point as the subsection's example for exempt units. `process.html` already stated it correctly. |
| Rent Board Forms Center | Not re-fetched in this pass (listed in the six rows that keep a 2026-11-10 badge). |

Validator allowlist is now 55 official URLs; all checks pass on the rebased tree.
## Addendum F — independent final integration audit (2026-11-11)

Session `arena/04450261-rentincreasesf2` inspected all 14 HTML pages, the navigation and validation
scripts, the calculation suite, every table row and all 55 allowlisted official-source mappings.
Controlling sources were fetched again on 2026-11-11; the earlier sessions' direct-source records
above remain preserved as historical evidence, not silently rewritten.

| Check | Official evidence / result | Outcome |
|---|---|---|
| Individual-owner license and timing | [Housing Inventory](https://www.sf.gov/rent-board-housing-inventory) says all residential owners report, reporting tenant-occupied units generates the license, and the current license is required on the increase's effective date; [Rules § 13.14](https://sfrb.org/section-1314-licensing-%E2%80%93-notice-rent-increase) says an unlicensed annual/banked increase is entirely void and expressly uses the effective date, not service date. | Confirmed the executive summary's answer and recommended sequence. No separate ordinary annual/banked petition is required. |
| Rate ledger | [Form 571](https://www.sf.gov/documents/34344/571_Allowable_Annual_Increases_26-27_1.pdf) confirms 2019–20 2.6%; 2020–21 1.8%; 2021–22 0.7%; 2022–23 2.3%; 2023–24 3.6%; 2024–25 1.7%; 2025–26 1.4%; 2026–27 1.6%. | Unit 2 uses 1.8% + 0.7% + 2.3% + 3.6% + 1.7% + 1.4% = 11.5% banked, plus current 1.6% = 13.1%; Unit 1 uses 1.4% + 1.6% = 3.0%. Inputs remain owner-supplied and unverified. |
| Banking and dates | [Banked increases](https://www.sf.gov/information--banked-rent-increases), [irregular periods](https://www.sf.gov/information--increasing-rents-during-irregular-periods), [Rent Board Rules Part IV](https://www.sf.gov/reports--december-2022--rent-board-rules-and-regulations-part-iv-rent-increases-not-requiring) and [rent-increase guidance](https://www.sf.gov/learn-about-rent-increases-san-francisco). | Confirmed no compounding, no rounding up, base rent only, 12-month frequency, off-anniversary/new-anniversary consequences, and notice content. F-28 remains a counselor-review item. |
| Notice | [Civil Code § 827(b)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=827.&lawCode=CIV) confirms 30 days at 10% or less and 90 days above 10%, personal delivery or mail; Rent Board guidance adds five days for mail. | All serve-by dates and day counts re-derived. |
| Pending proposal | [Legistar File 261020](https://sfgov.legistar.com/LegislationDetail.aspx?ID=8217304&GUID=7EDA4662-EBFB-4AF5-962F-C669B64AA770) remained Version 1, **Pending Committee Action**, with no enactment date or number on 2026-11-11. The Rent Board notice remains posted on Current Rates and rent-increase pages. | Still not enacted. F-27 and the conditional 10.0%/13.1% wording remain correct. |
| State and federal framework | [Civil Code § 1947.12](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1947.12.&lawCode=CIV), [SF AB 1482 guidance](https://www.sf.gov/reports--california-tenant-protection-act-2019-ab-1482), [Civil Code § 1942.5](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1942.5.&lawCode=CIV), [California CRD](https://calcivilrights.ca.gov/housing/), [HUD](https://www.hud.gov/reporthousingdiscrimination), and [42 U.S.C. ch. 45](https://www.govinfo.gov/content/pkg/USCODE-2024-title42/html/USCODE-2024-title42-chap45.htm). | Confirmed local-cap exemption, notice/retaliation and protected-class analysis. The absence of a located federal rent ceiling remains explicitly qualified under F-34. |
| Occupancy and owner practices | [Rules 6.14 / Costa-Hawkins](https://www.sf.gov/information--rent-increases-under-section-614-and-costa-hawkins), [additional occupants](https://www.sf.gov/information--charging-additional-occupants-prohibited), [algorithmic devices](https://www.sf.gov/information--algorithmic-devices-set-rent-are-prohibited-san-francisco), and [landlord petitions](https://www.sf.gov/landlord-petitions-and-passthroughs). | No market reset while an original occupant remains; no added-occupant surcharge; same legal caps for individual and corporate owners; ordinary management software is not banned. |
| Fees, coverage and tenant help | [Rent Board Fee](https://www.sf.gov/rent-board-fee), [rental-law coverage](https://www.sf.gov/learn-about-san-francisco-rental-laws), [tenant petitions](https://www.sf.gov/tenant-petitions), [counselor](https://www.sf.gov/speak-rent-board-counselor), [tenant/landlord resources](https://www.sf.gov/tenant-and-landlord-resources), [legal resources](https://www.sf.gov/information/legal-resources-housing-discrimination), and [local discrimination help](https://www.sf.gov/information--get-help-discrimination-housing). | $59.00 dwelling-unit fee and 2026-12-14 exemption deadline confirmed; owner-supplied coverage facts and license status remain flagged; free help details and eligibility limits match the sources. |

### Corrections made

1. **Date-sensitive publication defect fixed.** The previous site used 2026-11-10 as “today.” The
   base date is now 2026-11-11 throughout the current pages and scripts. Unit 2's earliest effective
   dates are 2027-02-09 (personal service) and 2027-02-14 (mail); Unit 1's are 2026-12-11 and
   2026-12-16. All remaining day pairs and the occupancy interval (224 days) were recomputed.
   The fixed target serve-by dates and the outer 2026-11-30 / 2026-11-25 closing dates did not change.
2. **Overbroad shorthand corrected.** Tenant Protections now distinguishes annual/banked limits,
   petition routes, and the no-petition Rules 6.14 / Costa-Hawkins route rather than saying every
   nonstandard increase needs an approved petition.
3. **Privacy rechecked.** The recursive validator was run with six privately supplied identifier
   patterns; none occurs in current public files. No pattern was stored or printed. Historical Git
   exposure remains separately disclosed at F-23/F-36 and was not destructively rewritten.

**Not legal advice.** Documentary verification against official sources only.

## Addendum G — 2026-11-13 decision-support and date refresh

Session `arena/756ae8e9-rentincreasesf2` rechecked the controlling current sources and refreshed the published today-relative dates. This is an additive record; the 2026-11-10 and 2026-11-11 verification records above remain historical, and no owner-supplied property or tenancy fact has been treated as verified.

### Official sources fetched directly on 2026-11-13

| Official source | Direct check and result |
|---|---|
| [SF Rent Board Housing Inventory](https://www.sf.gov/rent-board-housing-inventory) | All residential property owners report; reporting is online and free; tenant-occupied units receive the license automatically; the license must be current before an annual or banked increase takes effect; it need not be attached to the tenant notice; annual March 1 reporting and 30-day owner-contact updates; Inventory contents are public. |
| [Rent Ordinance § 37.15](https://www.sf.gov/information--sec-3715-reporting-obligations-licensing) | Local San Francisco ordinance: § 37.15(a) reporting obligation; under-ten-unit non-condominium units and condominium units report beginning March 1, 2023, with annual updates. § 37.15(e) provides for a license after substantial compliance and temporary suspension during noncompliance. This is not a state statute passed in 2023; March 1, 2023 is the local phase-in date for the specified smaller buildings/condos. |
| [Rent Board Rules § 13.14](https://sfrb.org/section-1314-licensing-%E2%80%93-notice-rent-increase) | Direct text: an increase effective while unlicensed is null and void in its entirety; the effective date, not service date, controls; banking rights are unaffected. For condos and buildings with fewer than ten residential units the rule applies to increases effective on or after March 1, 2023. |
| [SF Rent Increases guidance](https://www.sf.gov/learn-about-rent-increases-san-francisco) and [Current Rates](https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit) | 1.6% remains in force March 1, 2026–February 28, 2027; 30/90-day written notice; 5 additional days when mailed; notice identifies dollar amount, percentage and effective date; use the rate in force on effective date; Housing Inventory/license is required. Rent Board notice for File 261020 still says proposed and not enacted. |
| [Banked rent increases](https://www.sf.gov/information--banked-rent-increases) | Current page still says banked increases do not expire, can be combined/partially imposed, and repeats its “24 full months” summary. The separate official Rules § 4.12(a) 12-month test and worked examples remain the basis of F-16; the inconsistency remains disclosed, not silently harmonized. |
| [California Civil Code § 827](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=827.&lawCode=CIV) | Current text confirms 30 days at 10% or less and 90 days above 10%, including increases in the preceding 12 months, with personal delivery or mail under the referenced service rules. Rent Board guidance adds five days for mail. |
| [Legistar File 261020](https://sfgov.legistar.com/LegislationDetail.aspx?ID=8217304&GUID=7EDA4662-EBFB-4AF5-962F-C669B64AA770) | Still Version 1; **Pending Committee Action**; Land Use and Transportation Committee; no final action, enactment date, or enactment number; latest listed action remains 2026-10-07. It is not law as of this direct check. The City’s current-rates notice remains posted. |

### Recomputed dates (base date 2026-11-13)

| Scenario / check | Re-derived result | Source / status |
|---|---|---|
| Earliest effective date from a 90-day notice served today | 2027-02-11 personal; 2027-02-16 mailed | Civil Code § 827 + Rent Board notice guidance. |
| Suggested Unit 2 effective date 2027-02-15 | Personal service deadline 2026-11-17; mailed deadline 2026-11-12 has passed | Same statutory notice periods. Unit 2's off-anniversary banked-increase timing remains F-28; no clearance implied. |
| Last service date for any effective date through the published-rate end date 2027-02-28 | 2026-11-30 personal / 2026-11-25 mailed; 17 / 12 calendar days from the review date | Form 571 ends 2027-02-28; Civ. Code § 827. The fixed dates did not change; only the remaining-day counts did. |
| Earliest Unit 1 dates from today | 2026-12-13 personal / 2026-12-18 mailed | 30-day notice, plus five days for mail. Fixed Unit 1 anniversary target remains 2027-02-01. |
| Time since reported Unit 1 occupancy change | 226 days from 2026-04-01 to 2026-11-13 | Arithmetic only on owner-supplied date; F-15 remains open. |
| Dollar scenarios | No change: Unit 1 3.0% = $119.85 → $4,114.85; Unit 2 annual-only 1.6% = $50.40 → $3,200.40; phased 10.0% = $315.00 → $3,465.00; conditional 13.1% = $412.65 → $3,562.65; banked-only 11.5% = $362.25 → $3,512.25 | Arithmetic only on owner-supplied rents and unverified histories. Unit 2 banked amounts remain contingent on complete records, coverage, license, applicable law and F-28. |

### Site and privacy changes

- Added `suggestions.html` as a dedicated, separately navigable decision-support page: evidence questions, instructions to discover missing facts, conditional scenario comparisons, fairness/review cautions, and a blank choice log. It selects no path and asserts no owner fact as verified. Every table row links to an official source.
- The Executive Summary now expressly answers that the license requirement is local San Francisco law, not a state law passed in 2023; 2023 is the under-ten-unit/condominium local phase-in date. The dashboard, checklist, summary and suggestions page explicitly state that the 2026-11-12 mail deadline for Unit 2's 2027-02-15 target has passed as of November 13.
- Date-sensitive page text and `scripts/verify_calculations.py` now use 2026-11-13; the calculations script asserts current strings rather than leaving day-counts to manual updating.
- Privacy scan of all public text files found none of the supplied tenant-initial patterns. No names, initials, street address, contact details or parcel identifiers were added. Only anonymized Tenant A–F references, the provided ZIP, dates and amounts remain.

### Verification performed

- `python3 scripts/sync_nav.py --check` — 15 pages, 0 changes.
- `python3 scripts/validate_site.py` — passed: all 15 pages structurally valid; all 55 allowlisted official URLs appear on Sources; every table data row has an official external source; all internal paths/fragments resolve; every table has consistent columns; no public merge markers; no private-initial matches.
- `python3 scripts/verify_calculations.py` — passed **349 assertions**, including all published dollar figures, service deadlines, current-date counts and expected HTML text.
- `python3 -m py_compile scripts/sync_nav.py scripts/validate_site.py scripts/verify_calculations.py` — passed. `git diff --check` — passed.
- The intake facts (1940 construction date, two-unit count, leases, rents, ledger, occupants, license status, and any discrimination/retaliation facts) remain unverified and are left flagged; they are not supplied or invented by this session.
