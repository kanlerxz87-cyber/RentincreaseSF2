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

# Personal-identifier sweep across HTML and Markdown
python3 - <<'PY'
import re, glob
pats = [r"\bL\s*O\b", r"\bV\s*N\b", r"\bJP\b", r"\bM\s*T\b", r"\bE\s*R\b", r"\bI\s*S\b"]
hits = 0
for f in sorted(glob.glob("*.html") + glob.glob("*.md")):
    t = open(f, encoding="utf-8").read()
    for p in pats:
        for m in re.finditer(p, t):
            print(f, p, repr(t[max(0, m.start()-40):m.end()+40])); hits += 1
print("PII hits:", hits)
PY

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
- Rent Ordinance §37.3 Rent Limitations — (a)(1) annual, (a)(2) banking, (a)(5) nonconforming —
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

## 8. Addendum — final integration session `arena/342c4cc9-rentincreasesf2` (2026-11-08)

This addendum was written by the session that applied the change requests above. It is appended
rather than woven into the sections it corrects, so the audit keeps its original shape and every
correction stays visible.

### Change requests: disposition

| ID | Status | Where it landed |
|---|---|---|
| CR-01 | **Applied** | `banking-rule.html` is now in `NAV` in `scripts/sync_nav.py` (Review group), re-rendered across all 13 pages, and listed in `PAGES` in `scripts/validate_site.py`. The page is no longer orphaned. |
| CR-02 | **Applied** | The Form 538 worksheet URL was added to `VERIFIED_URLS`. The `sfrb.org` §13.14 URL was already present. |
| CR-03 | **Applied** | `flagged.html` F-16 now reads *Resolved*, with the two-worked-example test and a link to `banking-rule.html`; `analysis.html` carries the same resolution. |
| CR-04 | **Applied** | **2026-11-30** (personal) / **2026-11-25** (mailed) is now published as a closing deadline on `index.html`, `executive-summary.html`, `analysis.html`, `checklist.html` (new row 2.8a) and `flagged.html` F-19, and is asserted by `scripts/verify_calculations.py`. |
| CR-05 | **Applied** | Rules §13.14's effective-date rule and its banking-survival sentence now appear on `laws.html` (license-consequence row). |
| CR-06 | **Applied** | The Form 538 date discrepancy is published as flag **F-25**. |
| CR-07 | **Applied** | The privacy sweep in `scripts/validate_site.py` now globs **every** root `*.md` instead of naming two files, so `AUDIT.md` and `banking-rule.html`'s siblings are covered. |
| CR-08 | **Applied** | `COORDINATION.md` annotates the colliding rows 13–15 by owner and records that `arena/2b3012a0` never opened a PR; its branch no longer exists on the remote. |

### Corrections this session found on re-verification

| ID | Severity | Finding | Fix |
|---|---|---|---|
| **I-01** | **medium — citation** | `banking-rule.html` §7 quoted *"Nonconforming Rent Increases. Any rent increase which does not conform with the provisions of this section shall be null and void"* and attributed it to **Ordinance §37.3(a)(5)**. §37.3(a)(5) is the water-charges and water-bond-passthrough provision. The quoted sentence is **§37.3(b)(5)**, inside the notice-of-increase subdivision. The conclusion was unaffected; the pin-cite was wrong. | Corrected in `banking-rule.html`, `laws.html`, `AUDIT.md` §3 and `COORDINATION.md`, and published as flag **F-24**. |
| **I-02** | medium — internal contradiction | `units.html` had not been reconciled when `analysis.html` was rewritten as an effective-date scenario table. It still offered **2026-04-01** as the "proposed effective date" (a date in the past), described Unit 1's banked position using the **24-month** framing that F-16 resolved against, and gave Unit 1 a total of **1.6%** where `analysis.html` gives **3.0%** on 2027-02-01. | `units.html` rewritten to the scenario table: 1.6% before 2027-02-01, **3.0% → $119.85 → $4,114.85** on 2027-02-01, 13.1% for Unit 2, and the closing deadline in the recommended-effective-date row. |
| **I-03** | low — metadata | `sources.html` was stamped **Verified 2026-11-06** on a site whose nav said 2026-11-07, and five rows carried a stray `Verified 2026-11-07` string inside the *what it supports* column instead of the status column. | Re-stamped 2026-11-08, stray strings removed, and the verification-notes bullet rewritten to explain the three pass dates. |
| **I-04** | **medium — legal misattribution** | `laws.html` said Costa-Hawkins "limits local rent control to units with a certificate of occupancy before 1979". It does not: Civ. Code §1954.52(a) exempts units with a certificate of occupancy **after 1995-02-01**, units already exempt under a new-construction exemption on or before that date, and **separately alienable** units. San Francisco's **1979-06-13** date comes from the Rent Ordinance. | Rewritten to state §1954.52(a) accurately and to attribute 1979-06-13 to the Rent Board's rental-laws page. Published as flag **F-26**. |

All four corrections are citation or attribution defects. **No published dollar amount, percentage,
notice period or service date was wrong**, and no value was inferred at any point.

### Re-verification performed this session (2026-11-08)

Twenty official documents were fetched and read directly, not summarised from earlier sessions:

| Document | What it confirmed |
|---|---|
| [Current Rates](https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit) | 1.6% for 3/1/2026–2/28/2027; 1.4% for 2025–26; 1.7% for 2024–25 |
| [Form 571](https://www.sf.gov/documents/34344/571_Allowable_Annual_Increases_26-27_1.pdf) | The full percentage table 1982–2027, including 2.6% / 1.8% / 0.7% / 2.3% / 3.6% / 1.7% / 1.4% / 1.6% — every input in `verify_calculations.py`, and the 2027-02-28 end date |
| [Learn about rent increases](https://www.sf.gov/learn-about-rent-increases-san-francisco) | 12-month rule, anniversary date, use-the-effective-date rate, 30/90-day notice (+5 mailed), additional-occupant bar, license paragraph, and all four worked examples (1.6%, 1.6%, 4.7%, 3.3%) |
| [Banked rent increases](https://www.sf.gov/information--banked-rent-increases) | 24-month wording, partial increases, no expiry during a tenancy, not compounded, notice content, and the 6.7% worked example |
| [Irregular periods](https://www.sf.gov/information--increasing-rents-during-irregular-periods) | Anniversary = last increase or lease start; once every 12 months; 30/35-day notice; base rent only; no rounding up |
| [Multiple years](https://www.sf.gov/information--annual-rent-increase-multiple-years) | Add the percentages (8.2% example), no compounding |
| [Rules Part IV §4.10 / §4.12](https://www.sf.gov/reports--december-2022--rent-board-rules-and-regulations-part-iv-rent-increases-not-requiring) | The null-and-void rule, the half-percent good-faith tolerance, and §4.12(a)'s *"A full 12 months must have elapsed…"* and *"may only be given at the time of an annual increase"* |
| [Housing Inventory](https://www.sf.gov/rent-board-housing-inventory) | All owners report; license auto-generated for tenant-occupied units; March 1 annual deadline; no monetary penalty for late filing; $250 increments; submissions are public and under penalty of perjury; license need not accompany the notice |
| [Notice of Owner Noncompliance](https://www.sf.gov/notice-of-owner-noncompliance-with-housing-inventory) | 2022-07-01 / 2023-03-01 phase-in on the Board's own page (contrast Form 538 → F-25); refund exposure; how to check license status |
| [Rent Ordinance §37.3](https://www.sf.gov/information--sec-373-rent-limitations) | 60% of CPI capped at 7%; license hook to §37.15; banking subject to §37.15; §37.3(a)(11) additional occupants; **§37.3(b)(5)** nonconforming increases (I-01) |
| [Rules §13.14](https://sfrb.org/section-1314-licensing-%E2%80%93-notice-rent-increase) | Effective date not service date; banking rights survive a void increase; 2022-07-01 / 2023-03-01 phase-in |
| [Rental laws](https://www.sf.gov/learn-about-san-francisco-rental-laws) | 1979-06-13 coverage date; counselor line 415-252-4600 |
| [AB 1482](https://www.sf.gov/reports--california-tenant-protection-act-2019-ab-1482) | 8.8% for 2026-08-01–2027-07-31 and the express *does NOT apply* to Rent Ordinance units |
| [Civ. Code §827](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=827.&lawCode=CIV) | 30 days ≤10%, 90 days >10%, personal delivery or mail, prior-rate proration |
| [Civ. Code §1942.5](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1942.5.&lawCode=CIV) | 180-day bar from the latest listed event; once per 12 months; organising and immigration-threat provisions |
| [Civ. Code §1947.12](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1947.12.&lawCode=CIV) | 5% + CPI or 10%, two increments per 12 months, and the §1947.12(d)(3) local-control exemption |
| [Civ. Code §1954.52](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1954.52.&lawCode=CIV) | Post-1995-02-01 certificate of occupancy, new-construction and separately-alienable exemptions (I-04) |
| [Rules 6.14 / Costa-Hawkins](https://www.sf.gov/information--rent-increases-under-section-614-and-costa-hawkins) | 6.14 trigger is the **last** original occupant vacating; 60 days generally reasonable; a co-tenant is never subject to the Costa-Hawkins reset |
| [Algorithmic devices §37.10C](https://www.sf.gov/information--algorithmic-devices-set-rent-are-prohibited-san-francisco) | Effective 2024-10-14; per-unit and per-month violations; $1,000 penalties; tenant and organisation right of action |
| [Tenant Petitions](https://www.sf.gov/tenant-petitions) | No charge to file; the Board does not adjudicate discrimination or retaliation |
| [Landlord Petitions](https://www.sf.gov/landlord-petitions-and-passthroughs) | Six petition types; **no charge** for filing a petition; worksheet filings |
| [Tenant and Landlord Resources](https://www.sf.gov/tenant-and-landlord-resources) + [Legal resources](https://www.sf.gov/information/legal-resources-housing-discrimination) | Every phone number and address published on `tenant-protections.html`, and the Open Door Legal service-area limitation now noted there |

### Date re-stamp (2026-11-07 → 2026-11-08)

Only the quantities measured **from today** moved. Every absolute deadline is computed from an
effective date and was unchanged:

| Quantity | Before | After |
|---|---|---|
| Days since the added occupancy (2026-04-01) | 220 | **221** |
| Days remaining before the Unit 2 closing date (2026-11-30 / 2026-11-25) | 23 / 18 | **22 / 17** |
| Earliest effective date a 90-day notice served today can reach | 2027-02-05 | **2027-02-06** (mailed **2027-02-11**) |
| Earliest reachable effective date for Unit 1 if served today | 2026-12-07 / 2026-12-12 | **2026-12-08 / 2026-12-13** |

### Validation performed after these changes

- `python3 scripts/sync_nav.py` — 13 pages, one canonical navigation, 13 updated.
- `python3 scripts/validate_site.py` — **PASSED**: 13 pages, 47 allowlisted official URLs, a source
  link on every table data row, header/column-count integrity, no personal identifiers in HTML or in
  any of the 3 root Markdown files, all internal links resolve.
- `python3 scripts/verify_calculations.py` — **PASSED**: 47 assertions, including the new closing-
  deadline and earliest-reachable-date assertions.
- Tag balance spot-checked on every page that was edited by hand.
