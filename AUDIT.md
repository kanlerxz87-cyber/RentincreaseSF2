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
