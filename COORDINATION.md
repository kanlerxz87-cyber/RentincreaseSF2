# COORDINATION.md — Shared Task Board

**Repo:** `kanlerxz87-cyber/RentincreaseSF2`  
**Live site:** https://kanlerxz87-cyber.github.io/RentincreaseSF2/  
**Last updated:** 2026-11-10

## Sessions

| Session ID | Role | Status |
|---|---|---|
| `arena/3eac9d0e-rentincreasesf2` | Original build session | Completed tasks 1–8; merged PR #1; site deployed. Work preserved. |
| `session-arena-81e8c938` (this session) | Review, remediation, verification, and final integration | In progress. Reviewing the live site line by line, correcting legal accuracy, adding missing required pages, and re-verifying all sources. |
| `arena/fa7d2d77-rentincreasesf2` | Final integration: took over stale PR #5, ported its verified findings, re-verified line by line, extended the live site to 12 pages, merged PR #8 and confirmed deployment | **DONE** — completed 2026-11-07. |
| `arena/2b3012a0-rentincreasesf2` | Rent Board license answer, Q&A page, line-by-line re-verification | In progress on its own branch. **Claimed tasks 13–15 there — those numbers collide with rows 13–18 below; see A-07.** Branched from `62f6f59`, which predates PRs #6–#10, so it must rebase before opening a PR. |
| `arena/bf462feb-rentincreasesf2` | Independent primary-source audit of the integrated site; resolution of flag F-16; new verification page | done — merged as PR #12. New files only: `AUDIT.md`, `banking-rule.html`. No file claimed by another session was edited. |
| `arena/f0449766-rentincreasesf2` (this session) | Final integration: apply audit change requests CR-01…CR-08, close F-16, publish the closing service deadline, re-verify, PR and merge | In progress — owns tasks 24–26. File scope: `scripts/sync_nav.py`, `scripts/validate_site.py`, all `*.html` nav blocks, `flagged.html`, `analysis.html`, `index.html`, `executive-summary.html`, `checklist.html`, `laws.html`, `process.html`, `COORDINATION.md`. Branched from `main` at `a747d82`. |
| `arena/9b0747eb-rentincreasesf2` (this session) | Line-by-line re-verification against official sources; new-development check (File 261020); close stale PRs #16/#20; final PR, merge and deploy confirmation | In progress — owns tasks 27–29. File scope: `scripts/validate_site.py` (allowlist only), `flagged.html`, `analysis.html`, `executive-summary.html`, `sources.html`, `README.md`, `COORDINATION.md`. Branched from `main` at `a91dc78` (PR #21 merge). |
| `arena/d2474b1d-rentincreasesf2` (this session, 2026-11-10) | Residual integration: re-read the controlling official sources live, then apply only what was still missing after PRs #22 and #24 — the banked-expiry wording (C-01), the `units.html` banking measurement and April-2026 label (C-03/C-04), and flag F-28 | **Done** — owns tasks 34–36. File scope: `flagged.html`, `checklist.html`, `banking-rule.html`, `executive-summary.html`, `units.html`, `scripts/verify_calculations.py`, `AUDIT.md`, `COORDINATION.md`. Branched from `main` at `a91dc78`, reset to `3701b1c` after the race described below. |
| `arena/585ad53b-rentincreasesf2` (this session) | Independent verification pass: Nov 3, 2026 election-results check (new diligence — no prior session checked the ballot), File 261020 re-verification, direct re-read of the core rate/banking/license sources, re-derivation of every published figure, validators re-run; final PR, merge and deploy confirmation | In progress — owns task 37 (claimed first as 30, renumbered after colliding with `arena/d086cb8e`'s task 30 and `arena/d2474b1d`'s task 34 — logged in the session record). File scope: `COORDINATION.md` only, additive edits; no site file will be touched while task 33's integration PR is open. |
| `arena/c71c22cd-rentincreasesf2` (this session, 2026-11-10) | Line-by-line audit, full primary-source re-verification (including File 261020 `Leg Ver1`/`Leg Dig Ver1`, Rent Ordinance `600_Ordinance_11-02-26_2.pdf`, § 37.15, Form 538 2026–27, 2026–27 Rent Board Fee `$59.00`, SF.gov legal clinics), and final defect remediation on `22bf77d` | **In progress (tasks 43–44 done; task 45 PR/deploy in progress)** — owns tasks 43–45 (renumbered from 37–39 after PRs #28–#33 used 37–42). File scope: `scripts/validate_site.py`, `scripts/verify_calculations.py`, `index.html`, `executive-summary.html`, `units.html`, `analysis.html`, `laws.html`, `checklist.html`, `tenant-protections.html`, `practices.html`, `flagged.html`, `sources.html`, `banking-rule.html`, `README.md`, `AUDIT.md`, `COORDINATION.md`. Branched/rebased onto `main` at `22bf77d` (PR #33 merge). |
| `arena/69f0c0e5-rentincreasesf2` (claimed 2026-11-10T05:45Z) | Independent line-by-line re-verification of every published row against the **live** official source, then integration of whatever is still wrong or missing: apply `arena/0e02b0ec`'s open change request (conditional wording on building scope and on "lawful total"), re-check every today-relative figure, triage stale open PRs #27 and #29, PR, merge, confirm Pages deploy | **In progress** — owns tasks `69f0-A`, `69f0-B`, `69f0-C` (session-prefixed IDs; see the claim note at the end of this file). File scope while in progress: `COORDINATION.md` (additive), then — as integration session, all earlier tasks being `done` or `needs review` — the 13 root `*.html` pages, `scripts/*.py`, `README.md`, `AUDIT.md`. Branched from `main` at `cd005f7` (PR #36 merge). |

## Coordination note / handoff

The original session (`arena/3eac9d0e-rentincreasesf2`) created the first site and merged PR #1. This session reviewed the live site and found several items that need remediation before the site can be treated as final:

- Unit 2 was analyzed only at the current 1.6% annual allowance; the banked-increase calculation (11.5% banked + 1.6% current = 13.1%) was flagged but not calculated.
- The site said to apply the "same allowable percentage" to both units. That is not correct: each unit has its own base rent and rent history, and Unit 2 may have banked increases. The lawful analysis is unit-specific.
- Some table rows used "Provided data" or "Calculation" instead of an official source link. These are being replaced with official verification-method links and explicit "unverified" labels.
- The site did not include a dedicated tenant-protections page, a corporate-vs-individual-owner practices page, a consolidated sources page, or a GitHub Actions deployment workflow.
- The site did not clearly state that a tenant lawyer's approval cannot be guaranteed and that "normal business practice" is not defined by official sources beyond the Rent Board formula.

This session is editing the existing files rather than creating a duplicate site. No work from the original session is discarded. The original session's verification log is preserved below.

## Task board

| # | Task | Status | Owner session | File scope | Sources / verification notes |
|---|---|---|---|---|---|
| 1 | Research & verify SF/state/federal rent increase rules from official sources | done | arena/3eac9d0e-rentincreasesf2 | COORDINATION.md, site pages | See original verification log below. |
| 2 | Executive summary (anonymized) | done | arena/3eac9d0e-rentincreasesf2 | executive-summary.html | Re-verified and expanded by this session. |
| 3 | Unit data (anonymized, dates/amounts preserved) | done | arena/3eac9d0e-rentincreasesf2 | units.html | Re-verified and expanded by this session. |
| 4 | Laws & regulations reference with official source links | done | arena/3eac9d0e-rentincreasesf2 | laws.html | Re-verified and expanded by this session. |
| 5 | Notice process & fairness guidance | done | arena/3eac9d0e-rentincreasesf2 | process.html | Corrected by this session; unit-specific analysis added. |
| 6 | Increase calculations for both units | done | arena/3eac9d0e-rentincreasesf2 | analysis.html | Re-verified and expanded by this session with banked calculation. |
| 7 | GitHub Pages site (dashboard UI) + Flagged for Review page | done | arena/3eac9d0e-rentincreasesf2 | index.html, *.html, style.css | Re-verified and expanded by this session. |
| 8 | PR to main, merge, confirm Pages deploy | done | arena/3eac9d0e-rentincreasesf2 | — | PR #1 merged; Pages build succeeded. |
| 9 | Review and remediation of live site | done | session-arena-81e8c938 | all site files | Corrected legal accuracy, added missing required pages, replaced non-official source labels, and added unit-specific banked analysis. |
| 10 | Add GitHub Actions validation workflow and validation script | done | session-arena-81e8c938 | `.github/workflows/validate.yml`, `scripts/validate_site.py` | Validation checks internal links, external allowlist, table source links, and personal identifiers. GitHub Pages remains on the repository's existing legacy build from `main`; the workflow is a check, not a second deploy path. |
| 11 | Final verification, PR, and merge | done | session-arena-81e8c938 | all files | PR #2 merged; Pages build succeeded; live site re-verified. |
| 12 | Clarify individual-owner Housing Inventory/license and Rent Board notice timing | done | arena/795a54b7-rentincreasesf2 | index.html, executive-summary.html, process.html, practices.html, COORDINATION.md | Directly rechecked SF Rent Board Housing Inventory, rent increase, noncompliance, and counselor pages on 2026-11-07. All owners report; tenant-occupied units receive a license; current license is needed before effective date; license need not accompany tenant notice. Official guidance describes tenant notice and annual Housing Inventory, not a separate Rent Board filing for each increase. Safe sequencing advice is labeled as prudence, not a legal timing requirement. |
| 13¹ | Take over stale PR #5 (idle >30h) and audit it for privacy, accuracy and mergeability | done | arena/fa7d2d77-rentincreasesf2 | COORDINATION.md (audit record only; no PR #5 file is edited on its branch) | Handoff logged below. Audit complete: privacy PASS, build PASS, direct merge FAIL (unrelated history). Ported instead. |
| 14¹ | Re-verify controlling sources line by line (rates, banking, license, notice, occupancy, retaliation, algorithmic pricing) | done | arena/fa7d2d77-rentincreasesf2 | COORDINATION.md verification log | Official sources fetched directly this session. 21 official sources fetched and read directly this session; see log below. |
| 15¹ | Add missing verified content: Unit 1 occupancy change, corporate algorithmic-pricing ban, license null-and-void rule, retaliation screen, action checklist | done | arena/fa7d2d77-rentincreasesf2 | NEW: occupancy.html, checklist.html, market.html | New files only — no other session owns them. occupancy.html and checklist.html added. market.html dropped from scope: no official source defines a market benchmark for covered units, so a market page would add unsourced inference. |
| 16 | Reconcile unit calculations to an explicit effective-date scenario table (today = 2026-11-07) | done | arena/fa7d2d77-rentincreasesf2 | analysis.html, units.html, index.html, executive-summary.html | Supersedes ambiguous single-number maxima. analysis.html rewritten as an effective-date scenario table; all figures re-derived by script. |
| 17 | Integration: shared nav, sources register, flags, validator allowlist | done | arena/fa7d2d77-rentincreasesf2 | all *.html nav blocks, sources.html, flagged.html, scripts/validate_site.py, style.css, README.md | Integration-session prerogative; tasks 1–12 are all `done`. 12 pages, 46 official URLs, per-row sources, column integrity and privacy sweep all pass. |
| 18 | Final verification, PR to main, merge, confirm Pages deploy | done | arena/fa7d2d77-rentincreasesf2 | COORDINATION.md | Pending tasks 13–17. PR #8 merged; Pages built on the merge commit; live site verified. |
| 19 | Independent primary-source audit of the integrated 12-page site: re-derive every published figure without reusing the site's arithmetic, recompute every notice deadline, scan for personal identifiers | done | arena/bf462feb-rentincreasesf2 | `AUDIT.md` (new) | **No published figure is wrong and no value was invented.** 13 figure classes re-derived and confirmed; 7 service deadlines recomputed and confirmed. Primary texts read directly: Rules Part IV §4.10/§4.12, Rent Ordinance §37.3, §37.10C, Rules §13.14, Form 571, Form 538, Current Rates, all four sf.gov worked examples, Banked increases, Irregular periods, Multiple years, Housing Inventory, AB 1482, Tenant Petitions, Civ. Code §827. Ten irregularities logged as A-01…A-10. |
| 20 | Resolve flag F-16 (the 12-vs-24-month banking interval conflict) on the evidence rather than leaving it open | done | arena/bf462feb-rentincreasesf2 | `banking-rule.html` (new) | Three candidate readings tested against **both** official Rent Board worked examples. Only Rules §4.12(a)'s per-allowance 12-month test reproduces both (6.7% and 3.3%). Global-24 gives 4.7% against an official 3.3%; per-allowance-24 gives 5.0% against an official 6.7%. The resolution **confirms** the site's published 11.5% / 13.1% / 1.6% / 3.0% figures. |
| 21 | Publish the closing service window as a deadline counted back from today (irregularity A-02) | done | arena/bf462feb-rentincreasesf2 | `banking-rule.html`, `AUDIT.md` | Unit 2's 13.1% needs an effective date on or before 2027-02-28 because Form 571 ends there and the 2027-28 percentage is unpublished; with a 90-day notice the last service date is **2026-11-30** personal / **2026-11-25** mailed. The mailed route to the earliest date closed 2026-11-02. Unit 1 is not urgent: serve by 2027-01-02 for 2027-02-01. |
| 22 | Log change requests for corrections that belong in files owned by other sessions, instead of editing them | done | arena/bf462feb-rentincreasesf2 | `AUDIT.md` section 6 | CR-01…CR-08. No page in `PAGES`, no script, and no nav block was modified by this session. |
| 23 | Validate, open PR to `main`, merge, confirm GitHub Pages deploy | done | arena/bf462feb-rentincreasesf2 | `COORDINATION.md` | **PR #11 merged** at 2026-11-07T21:32:15Z, merge commit `041632c`. `Validate site` passed on the PR and post-merge; `pages build and deployment` succeeded on `041632c`; Pages status `built`. Live URLs re-fetched after deployment and confirmed serving the new content. See *PR #11 — independent audit* below. |
| 24 | Final integration: apply audit change requests CR-01…CR-08 — add `banking-rule.html` to nav and validator, close flag F-16, publish the 2026-11-30/2026-11-25 closing service deadline, add Rules §13.14 provisions, log A-06 discrepancy, widen the privacy sweep to root Markdown, annotate the colliding task rows | done | arena/f0449766-rentincreasesf2 | `scripts/sync_nav.py`, `scripts/validate_site.py`, all `*.html` nav blocks, `flagged.html`, `analysis.html`, `index.html`, `executive-summary.html`, `checklist.html`, `laws.html`, `process.html`, `COORDINATION.md` | Official sources as cited per CR in `AUDIT.md` §6 and `banking-rule.html`; no figure re-derived by this session is presented without its official source link. |
| 25 | Full re-verification of the merged tree (validator, calculation script, privacy sweep) | done | arena/f0449766-rentincreasesf2 | scripts run only; no file scope | `python3 scripts/validate_site.py`; `python3 scripts/verify_calculations.py`; root-Markdown privacy sweep. |
| 26 | PR to `main`, merge, confirm GitHub Pages deploy, record result | done | arena/f0449766-rentincreasesf2 | `COORDINATION.md` | Flagged irregularities and unverified items do not block the merge; they are published on the Flagged for Review page. |
| 27 | Line-by-line re-verification of the live site against official sources (Housing Inventory, rent increases, banked increases, Form 571, Tenant Petitions, Legistar File 261020) | done | arena/9b0747eb-rentincreasesf2 | `COORDINATION.md` (verification record) | All key claims confirmed: license required on effective date for <10-unit buildings since 2023-03-01; 1.6% (2026–27); Unit 2 banked 11.5% = 1.8+0.7+2.3+3.6+1.7+1.4 (Form 571); 13.1% total; 30/90-day +5 mail; tenant petitions free, no discrimination adjudication. New development found: File 261020 proposed 10% cap (see task 28). |
| 28 | Publish new development as flag F-27: proposed 10% cap on banked increases (File 261020, Pending Committee Action, not enacted) | done | arena/9b0747eb-rentincreasesf2 | `flagged.html`, `analysis.html`, `executive-summary.html`, `sources.html`, `scripts/validate_site.py`, `README.md` | Legistar record read directly 2026-11-10: introduced 2026-09-15, Land Use and Transportation Committee, status Pending Committee Action. Rent Board notice posted 2026-11-09 on rent-increases and banked-increases pages. Under current law 13.1% remains lawful; phased 10.0% is the fallback if enacted. |
| 29 | Close stale PRs #16 and #20 (CONFLICTING, content already salvaged/merged), validate, PR to `main`, merge, confirm Pages deploy | in progress | arena/9b0747eb-rentincreasesf2 | `COORDINATION.md` | PR #16 duplicates PRs #14/#15/#17 (salvaged in #17); PR #20 is a PR #19 record whose text is not on `main` and whose branch conflicts after PRs #18/#21. Both closed unmerged with explanatory comments; PR #19 record summary preserved in this session's record below. |
| 30 | Re-stamp the whole site to the 2026-11-10 verification date and re-derive every today-relative figure (day counts, earliest reachable effective dates, days since the added occupancy) | done — PR #24 | arena/d086cb8e-rentincreasesf2 | `scripts/sync_nav.py`, `scripts/verify_calculations.py`, all 13 `*.html` pages | `REVIEW_DATE` and `LAST_VERIFIED` asserted against each other by `verify_calculations.py`; every printed `<personal> / <mailed>` day pair re-derived from the official 90/30-day notice periods. |
| 31 | Line-by-line re-verification of the merged tree against primary official sources, including the F-27 citation target | done — PR #24 | arena/d086cb8e-rentincreasesf2 | `flagged.html`, `analysis.html`, `executive-summary.html`, `sources.html` | Read directly this session: Form 571 table (1.6 / 1.4 / 1.7 / 3.6 / 2.3 / 0.7 / 1.8), Current Rates page, Rules §13.14, Housing Inventory, Civ. Code §827(b), AB 1482 page, Rent Ordinance §37.3(a)(1)–(2), Legistar File 261020. |
| 32 | Standardize the F-27 notice citation and correct this session's own initial misreading of it | done | arena/d086cb8e-rentincreasesf2 | `flagged.html`, `analysis.html`, `executive-summary.html`, `sources.html` | **Correction to this session's first claim.** This session initially wrote that PR #22 had cited the wrong page and that the 2026-11-09 notice appeared only on the Current Rates report. That was wrong: the notice is reproduced verbatim on **three** Rent Board pages (Current Rates, Banked rent increases, Learn about rent increases), so PR #22's citations were valid. Net change: `analysis.html` and `executive-summary.html` now cite the Current Rates report (where the notice was read this session) instead of the generic rent-increases page; F-27's source cell carries Legistar plus Current Rates. No claim of error against PR #22 is made. |
| 33 | Final integration: verify the combined data, confirm the site builds with no broken links, PR to `main`, merge, confirm GitHub Pages deploy, record the result | done — PR #24 merged, Pages built, live content read back | arena/d086cb8e-rentincreasesf2 | `COORDINATION.md`, `README.md` | Blocked only on rows 30–32. |
| 34 | Residual integration for session `arena/d2474b1d`: re-read every controlling official source live and diff the result against `main` rather than against this session's own draft | done | arena/d2474b1d-rentincreasesf2 | `COORDINATION.md`, `AUDIT.md` | 14 sources fetched 2026-11-10; confirmations and the exact list of what was *not* re-fetched are in the `AUDIT.md` addendum dated 2026-11-10. |
| 35 | Correct C-01 (banked increases do not expire — the wrong reason for the deadline), C-03 and C-04 (`units.html`), and add F-28 (non-anniversary effective date); add a CI guard so C-01 cannot return | done | arena/d2474b1d-rentincreasesf2 | `checklist.html`, `banking-rule.html`, `executive-summary.html`, `units.html`, `flagged.html`, `scripts/verify_calculations.py`, `AUDIT.md` | [Banked increases](https://www.sf.gov/information--banked-rent-increases) (“does not expire”); [§ 37.3](https://www.sf.gov/information--sec-373-rent-limitations) (a)(2) anniversary wording; [Irregular periods](https://www.sf.gov/information--increasing-rents-during-irregular-periods). 61 → 105 assertions. |
| 36 | Validate, PR to `main`, merge, confirm GitHub Pages deploy, record PR link and result | in progress | arena/d2474b1d-rentincreasesf2 | `COORDINATION.md` | Flagged items F-01…F-28 do not block the merge; they are published on the Flagged for Review page. |
| 40 | Add direct official draft § 37.3(h) citations alongside the File 261020 status record | done | arena/817d1de7-rentincreasesf2 | `flagged.html`, `sources.html`, `README.md`, `scripts/validate_site.py` | Draft read directly: proposed 10% banked/capital-improvement component cap, lowest base rent in prior 12 months, notices on/after 2026-09-15, 2029-12-31 sunset unless extended. No outcome inferred. |
| 41 | Final integrated build, source/table/privacy/link checks and all calculation assertions | done | arena/817d1de7-rentincreasesf2 | scripts run only; `AUDIT.md` verification record | 13 balanced pages, 50 official URLs, 17 public files HTTP 200, no broken internal links/fragments, privacy pass, 105 assertions, diff check pass; rerun after rebase. |
| 42 | PR to `main`, merge, Pages deployment verification and final record | done — PR #32 merged; Pages built and live-verified | arena/817d1de7-rentincreasesf2 | `COORDINATION.md` | Blocked on task 41. |
| 37 | Independent verification pass (new session, additive to `COORDINATION.md` only): re-read Form 571, Current Rates, rent-increases, banked-increases, Housing Inventory and Legistar File 261020 directly; verify the Nov 3, 2026 SF general election produced no rent-related change (new diligence — no prior session checked the ballot); confirm the re-stamped day counts re-derive from 2026-11-10; re-run all validators; PR to `main`, merge, confirm Pages deploy | done | arena/585ad53b-rentincreasesf2 | `COORDINATION.md` | Claimed 2026-11-10 ~00:50 UTC. Claimed as task 30 first; renumbered 34 after `arena/d086cb8e` claimed 30–33 concurrently (duplicate-number situation of the A-07 kind; no work duplicated — their rows were left verbatim). |
| 38 | Residual integration after concurrent PRs #22–#25; preserve all prior corrections | done | arena/9e245201-rentincreasesf2 | `*.html`, `scripts/verify_calculations.py`, `README.md` | PR #28 initially conflicted on this file. Rebased by resetting to `e538d59`, reviewing concurrent changes, and applying only residual deltas. No C-01 bank-expiry correction or F-28 non-anniversary warning discarded. |
| 39 | Correct residual internal contradiction and source-overstatement; extend pending-cap checks | done | arena/9e245201-rentincreasesf2 | `banking-rule.html`, `tenant-protections.html`, `laws.html`, `process.html`, `practices.html`, `checklist.html`, `units.html`, `flagged.html`, `index.html`, `README.md`, `scripts/verify_calculations.py` | F-29: current annual 1.6% is used, not also banked or forfeited. F-30: tenant resources narrowed to official wording. File 261020 warnings added to remaining process/checklist/law/practice/verification pages. Facts relabeled owner-supplied. |
| 40 | Final validation, PR #28 merge, Pages deployment and record | done | arena/9e245201-rentincreasesf2 | `COORDINATION.md` | PR #28 merged 2026-11-10T00:45:31Z as `3a284cd`; PR and post-merge validation passed; Pages run 42730738839 succeeded; Pages latest build `3a284cd`, status `built`. Live corrected pages fetched. |
| 43 | Live primary-source re-verification on `22bf77d` (Rent Ordinance `11-02-26` / §§ 37.3 & 37.15, Form 538 2026–27, 2026–27 Rent Board Fee `$59.00`, File 261020 `Leg Ver1`/`Leg Dig Ver1`, Rules §§ 4.10/4.12/13.14, Topics 152/153/254/268/301/322/323/325/331/351/361, Civ. Code §§ 827/1942.5/1947.12/1954.50/1954.52, SF.gov legal clinics & `arena/2b3012a0` comparison) | done | arena/c71c22cd-rentincreasesf2 | `COORDINATION.md`, `AUDIT.md` | Every official claim checked directly from live sources on 2026-11-10 (renumbered to 43–45 after PRs #28–#33 used 37–42). |
| 44 | Remediate residual live defects on `22bf77d` while preserving PR #28–#33 improvements (F-29, F-30, `"owner-supplied"`, `Leg Ver1`): fix malformed `<meta name="description">` on 3 pages, replace HTTP-500 Form 538 URL with live 2026–27 Form 538 & update F-24/A-06 (`2021-07-01`/`2022-03-01` vs § 37.15(c) `2022-07-01`/`2023-03-01`), sync `sources.html` with 100% of allowlisted URLs + verified 2026-11-10 timestamps + § 37.15/Leg Ver1/Leg Dig Ver1, fix `units.html` & `index.html` inconsistencies/directory omissions, update `tenant-protections.html` verified legal-clinic details (incl. Open Door Legal 94122 exclusion while retaining F-30 wording), tighten File 261020 wording against exact `Leg Ver1` text & add 2026–27 `$59.00` Rent Board Fee + F-28 cross-links, and harden `validate_site.py` (`<head>`/`<meta>`, tag balance, `sources.html` allowlist sync) | done | arena/c71c22cd-rentincreasesf2 | `scripts/validate_site.py`, `scripts/verify_calculations.py`, `index.html`, `executive-summary.html`, `units.html`, `analysis.html`, `laws.html`, `checklist.html`, `tenant-protections.html`, `practices.html`, `flagged.html`, `sources.html`, `banking-rule.html`, `README.md`, `AUDIT.md` | Zero values inferred; `validate_site.py` (52 URLs), `verify_calculations.py` (122 assertions), CSS check, HTTP 200 smoke test, and PII sweep all pass. |
| 45 | Run full checks (`sync_nav.py`, `validate_site.py`, `verify_calculations.py`, local HTTP 200 smoke test, PII sweep), open PR to `main`, merge, verify CI & GitHub Pages deployment, record result | in progress | arena/c71c22cd-rentincreasesf2 | `COORDINATION.md` | Runs after tasks 43–44. |
| 69f0-A | Independent line-by-line re-verification: fetch every official source cited on the site **live** and check each table row's claim against the fetched text; re-derive every dollar figure and deadline without reusing the site's arithmetic; record per-source results and every discrepancy | in progress | arena/69f0c0e5-rentincreasesf2 | `COORDINATION.md` (additive only) | Claimed 2026-11-10T05:45Z from `cd005f7`. Read-only on site files until 69f0-B. |
| 69f0-B | Integration of findings: apply `arena/0e02b0ec`'s logged request (make "your building is in scope" / "a two-unit building falls in that second group" / "lawful total" explicitly conditional on unverified unit count, coverage, tenancy, rent history, license status and pending legislation) and correct any defect found in 69f0-A. No value is filled by inference; anything unconfirmable stays blank and flagged | unclaimed until 69f0-A reports | arena/69f0c0e5-rentincreasesf2 | 13 root `*.html` pages, `scripts/*.py`, `README.md`, `AUDIT.md`, `COORDINATION.md` | Starts only after 69f0-A; exact files touched will be listed here before the first edit. |
| 69f0-C | Triage stale open PRs #27 and #29 (both idle since 2026-11-10T00:44Z, > 60 min); full checks (`sync_nav.py`, `validate_site.py`, `verify_calculations.py`, tag balance, local HTTP 200, privacy sweep); PR to `main`, merge, confirm GitHub Pages deploy and read the live pages back; record PR link and merge result | unclaimed until 69f0-B is done | arena/69f0c0e5-rentincreasesf2 | `COORDINATION.md` | Flagged and unverified items do not block the merge. |



¹ **Duplicate task numbers (A-07 / CR-08).** Rows 13–15 above belong to `arena/fa7d2d77-rentincreasesf2` on `main`. Session `arena/2b3012a0-rentincreasesf2` independently claimed rows numbered **13–15** on its own branch (`arena/2b3012a0-rentincreasesf2`) for different work (Rent Board license answer, Q&A page, line-by-line re-verification). That branch was cut from `62f6f59`, which predates PRs #6–#10, so merging it as-is would revert the PR #6/#7 license clarification and the PR #10 privacy redaction. **It must rebase onto current `main` before opening a pull request.** No session has merged it. Its claims remain pending and do not block the board.

## Standing rules

1. **Root Markdown is public (A-08).** GitHub Pages serves the repository root from `main` with `.nojekyll`, so **every `*.md` file at the repository root is publicly retrievable** at the site URL. Never write tenant names, initials, addresses, contact details, parcel numbers or other personal identifiers in any root Markdown file. `scripts/validate_site.py` now sweeps **all** root `*.md` (not only `README.md` and `COORDINATION.md`) for the personal-identifier patterns on every push and PR.
2. **No value without an official source.** If a value cannot be confirmed from an official government, legislative or City of San Francisco source, it is left blank and flagged — never filled by inference.
3. **Table rows need source links.** Every data row in every site table carries at least one official source link (enforced by the validator).
4. **File scope discipline.** Each session edits only the files in its claimed scope. Cross-cutting changes are logged as change requests (see `AUDIT.md` §6) and applied only by the integration session that owns the shared files.
5. **`banking-rule.html` is now in the shared navigation** (Verification group) and in the validator's page list, closing audit limitation / A-09 and change request CR-01.

## PR and deployment record

- **PR:** https://github.com/kanlerxz87-cyber/RentincreaseSF2/pull/2
- **Merge commit:** `153b260def7651b2860205bb8eaa646bd3a38227`
- **Merged at:** 2026-11-06T13:36:39Z
- **Merge method:** merge commit
- **Validation workflow:** `Validate site` passed on the PR (run 42226838919).
- **GitHub Pages build:** `pages build and deployment` run 42226890108 completed successfully; Pages status `built`.
- **Live site:** https://kanlerxz87-cyber.github.io/RentincreaseSF2/
- **Live pages verified:** `index.html`, `executive-summary.html`, `units.html`, `analysis.html`, `laws.html`, `process.html`, `tenant-protections.html`, `practices.html`, `flagged.html`, `sources.html`, and `style.css` all returned HTTP 200 locally and were re-fetched from the live site after deployment.

## Follow-up PR #6 — license and notice clarification

- **PR:** https://github.com/kanlerxz87-cyber/RentincreaseSF2/pull/6
- **Merge result:** merged to `main` at 2026-11-07T20:43:39Z; merge commit `ea942f3533f0ce181d50ade0a509d020c047415d`.
- **Validation:** PR `Validate site` passed (run 42412404807); post-merge `Validate site` passed (run 42412433323).
- **GitHub Pages:** deployment run 42412432988 completed successfully.
- **Live verification:** fetched the public dashboard and executive summary after deployment; both show the individual-owner answer, distinction between Rent Board reporting and tenant notice, and the effective-date license requirement.

## PR #3 review (session arena/77623c60-rentincreasesf2)

A parallel session opened PR #3, "Rental increase analysis — Outer Sunset SF, ZIP 94122 (verified sources + GitHub Pages site)," while this session was finishing PR #2. PR #3 proposes a 14-page static site with a different structure and a larger source register.

### Review findings

- **Privacy violation (blocking):** PR #3 published the six supplied tenant initial pairs on the site, including in the privacy section and flagged-items page. [Initials redacted from this log on 2026-11-07 — this file is served publicly by GitHub Pages, so reproducing them here was itself a leak.] The user explicitly required all personal information to be anonymized and said privacy is top priority. Initials are personal information and must not be published. This alone makes PR #3 unacceptable as submitted.
- **Unit 1 calculation conflict:** PR #3 presents $4,114.85 (3.0%) as a maximum for Unit 1 on the February 1, 2026 anniversary, and treats the 1.4% as banked. Under the Rent Board's 24-month banking rule, the 1.4% that became available on February 1, 2026 is not banked until February 1, 2027. For an April 1, 2026 effective date, the maximum is 1.6% ($4,058.92). PR #3's own flagged item F-07 acknowledges the 24-month rule but still presents 3.0% as a lawful outcome for Unit 1 without a clear date qualification. This conflicts with the more conservative analysis in PR #2.
- **Build artifacts:** PR #3 includes `tools/__pycache__/*.pyc` files. These should not be committed.
- **Duplicate/conflicting site:** PR #2 is already merged and live. Merging PR #3 would replace the live site with a different structure and would require a full line-by-line re-verification of all 14 pages.

### Decision

Do not merge PR #3. Close it with a comment explaining the privacy violation, the Unit 1 calculation conflict, and the duplicate-site issue. The work remains preserved on its branch. No files from PR #3 were edited by this session. PR #2 remains the live site.

### Coordination note

The parallel session should be notified that its PR was reviewed and closed. If it wants to contribute, it should open a new PR that removes all initials, uses placeholders only, corrects the Unit 1 analysis, and removes build artifacts. Any new PR must be reviewed against the same privacy and source-verification standard.

## Final verification summary

- `python3 scripts/validate_site.py` passes.
- All 10 HTML pages and `style.css` return HTTP 200 from a local static server.
- HTML tag-balance check passes for all 10 pages.
- Every table data row has at least one official source link.
- No tenant initials or personal identifiers are present in the published HTML.
- All external source links are on the verified official-source allowlist.
- Live site was re-fetched after deployment and shows the remediated content, including the Unit 2 banked calculation and the Flagged for Review page.

## Remaining items for the user to review

The Flagged for Review page lists the items that cannot be confirmed from official sources without additional records. The most important are:
- confirm the 1940 build year and rent-control coverage;
- confirm the lease dates, base rents, and occupancy;
- check the rent increase license in the Rent Board Portal;
- confirm Unit 1's last-increase date and whether the April 1, 2026 increase has been served;
- confirm Unit 1's tenancy status (continuing original tenant vs. new tenancy);
- confirm Unit 2's complete rent history before relying on the 13.1% banked calculation;
- confirm the notice service date for Unit 2's 90-day requirement;
- have a tenant lawyer review the final notice and documentation.

No further code changes are required for the site to be live. The remaining items are factual/legal confirmations that require records not available in the repository.

## Follow-up verification log (2026-11-07)

### Official sources rechecked directly for the license/notice clarification

- SF Rent Board, Housing Inventory — all residential property owners report; tenant-occupied units receive a Rent Increase License; current license must be on file before annual/banked increase takes effect; license need not be included with tenant notice; Housing Inventory data/public-reporting details — https://www.sf.gov/rent-board-housing-inventory
- SF Rent Board, Learn about rent increases — current 1.6% rate for 2026-27, annual allowable increase license requirement, written notice to tenant, notice periods/content — https://www.sf.gov/learn-about-rent-increases-san-francisco
- SF Rent Board, Notice of Owner Noncompliance — annual reporting applies to owners; license requirement applies to rent-controlled annual/banked increases; consequence for increase effective while unlicensed — https://www.sf.gov/notice-of-owner-noncompliance-with-housing-inventory
- SF Rent Board, Banked rent increases — license/effective-date requirement and tenant notice content — https://www.sf.gov/information--banked-rent-increases
- SF Rent Board, Speak with a Rent Board counselor — free counseling, not legal advice — https://www.sf.gov/speak-rent-board-counselor

The official sources do not expressly require a license to be active before the notice is served; they require it before the increase takes effect. Accordingly, the site states the formal effective-date requirement and separately labels checking the license before service as prudent sequencing. The sources describe written notice to tenants and Housing Inventory reporting but do not instruct an owner to separately file each individual increase notice with the Board. This is a statement about the cited official process, not an assertion that no other filing could ever apply to a different petition/passthrough situation.

### Validation performed

- `python3 scripts/validate_site.py` passes: all 10 pages, official links, per-table-row source links, privacy scan, and internal links.
- `git diff --check` passes.
- Changed only `index.html`, `executive-summary.html`, `process.html`, `practices.html`, and this coordination log.

## Original verification log (preserved from session arena/3eac9d0e-rentincreasesf2)

- SF Rent Board current rates: 1.6% allowable increase for 3/1/2026–2/28/2027 (1.4% for 3/1/2025–2/28/2026; 1.7% for 3/1/2024–2/28/2025) — https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit
- Rent increase rules (once per 12 months, 30-day notice / 90-day if >10%, rent increase license, 60% of Bay Area CPI formula) — https://www.sf.gov/learn-about-rent-increases-san-francisco
- Banked rent increases (no limit, do not expire during tenancy, notice must state banked portion) — https://www.sf.gov/information--banked-rent-increases
- CA Civil Code §1947.12 (AB 1482: 5% + regional CPI, max 10% in 12 months) — https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1947.12.
- CA Civil Code §827 (30/90-day notice) — https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=827.
- Federal Fair Housing Act, 42 U.S.C. §3604 (7 protected classes; terms/conditions discrimination prohibited) — https://www.hud.gov/reporthousingdiscrimination and https://www.govinfo.gov/content/pkg/USCODE-2024-title42/html/USCODE-2024-title42-chap45.htm

## This session's verification log (2026-11-06)

### Official sources checked directly

- SF Rent Board, "Learn about rent increases in San Francisco" — 1.6% for 3/1/2026–2/28/2027; 12-month rule; 30/90-day notice; license; base rent; additional occupants; anniversary date; use percentage in effect on date of increase — https://www.sf.gov/learn-about-rent-increases-san-francisco
- SF Rent Board, "Current Rates" — 1.6% for 3/1/2026–2/28/2027; 1.4% for 3/1/2025–2/28/2026; 1.7% for 3/1/2024–2/28/2025 — https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit
- SF Rent Board, "571 Allowable Annual Increases" PDF — full historical table: 2025–26 1.4%; 2024–25 1.7%; 2023–24 3.6%; 2022–23 2.3%; 2021–22 0.7%; 2020–21 1.8%; 2019–20 2.6% — https://www.sf.gov/documents/34344/571_Allowable_Annual_Increases_26-27_1.pdf
- SF Rent Board, "Banked rent increases" — skipped increase banked only if at least 24 full months pass; no limit; not compounded; not rounded up; do not carry over to a new tenant; license and notice requirements — https://www.sf.gov/information--banked-rent-increases
- SF Rent Board, "Increasing rents during irregular periods" — 12–24 months and 24+ months examples; option to impose current allowable or wait for anniversary to stack — https://www.sf.gov/information--increasing-rents-during-irregular-periods
- SF Rent Board, "Annual rent increase for multiple years" — add prior allowable percentages; no compounding; no rounding up — https://www.sf.gov/information--annual-rent-increase-multiple-years
- SF Rent Board, Rules and Regulations Part IV, §4.12 — banking rule text — https://www.sf.gov/reports--december-2022--rent-board-rules-and-regulations-part-iv-rent-increases-not-requiring
- SF Rent Board, Rent Ordinance §37.3 — annual increase, banking, capital improvements, utilities, notice — https://www.sf.gov/information--sec-373-rent-limitations
- SF Rent Board, "The Rent Ordinance" — official table of contents and complete ordinance PDF — https://www.sf.gov/reports--rent-ordinance
- SF Rent Board, "Housing Inventory" — license required; reporting deadline; portal — https://www.sf.gov/rent-board-housing-inventory
- SF Rent Board, "Notice of Owner Noncompliance" — unlicensed increase may be null and void; tenant refund — https://www.sf.gov/notice-of-owner-noncompliance-with-housing-inventory
- SF Rent Board, "Landlord Petitions and Passthroughs" — six petition types; above-cap process — https://www.sf.gov/landlord-petitions-and-passthroughs
- SF Rent Board, "Learn about San Francisco rental laws" — coverage; just cause; exemptions — https://www.sf.gov/learn-about-san-francisco-rental-laws
- SF Rent Board, "Partial Exemption for Newly Constructed Rental Units" — post-6/13/1979 exemption — https://www.sf.gov/information--partial-exemption-newly-constructed-rental-units
- SF Rent Board, "Partial Exemption for Certain Single-Family Homes and Condominiums Under Costa-Hawkins" — condo/SF exemption — https://www.sf.gov/information--partial-exemption-certain-single-family-homes-and-condominiums-under-costa-hawkins
- SF Rent Board, "Evictions in San Francisco" — just cause; eviction process; tenant help — https://www.sf.gov/evictions-san-francisco
- SF Rent Board, "Speak with a Rent Board counselor" — free counseling; no legal advice — https://www.sf.gov/speak-rent-board-counselor
- SF Rent Board, "Tenant and Landlord Resources" — free tenant counseling and legal help — https://www.sf.gov/tenant-and-landlord-resources
- SF Rent Board, "Tenant Petitions" — unlawful rent increase; lawful rent determination; no filing charge — https://www.sf.gov/tenant-petitions
- SF Rent Board, "Tenant Summary Petitions" — challenge pending increase — https://www.sf.gov/information--tenant-summary-petitions
- SF Rent Board, "About Rent Board" — cannot adjudicate discrimination/retaliation; contact SF Human Rights Commission — https://www.sf.gov/departments--rent-board--about
- SF Rent Board, "The California Tenant Protection Act of 2019 (AB 1482)" — state cap; interaction with local law — https://www.sf.gov/reports--california-tenant-protection-act-2019-ab-1482
- SF Rent Board, "Rent Board Fee" — fee and deadline — https://www.sf.gov/rent-board-fee
- SF Rent Board, "Capital Improvement Petitions" — above-cap reason; process — https://www.sf.gov/information--capital-improvement-petitions
- SF Rent Board, "Operating and Maintenance Expense Petitions" — above-cap reason; process — https://www.sf.gov/information/topic-no-322-operating-and-maintenance-expense-petitions
- SF Rent Board, "Special Circumstances Petitions" — above-cap reason; process — https://www.sf.gov/information--special-circumstances-petitions-based-rents-comparable-units
- SF Rent Board, "Utility Passthroughs" — above-cap reason; process — https://www.sf.gov/information--utility-passthroughs-gas-electricity-and-steam-heat
- SF Rent Board, "General Obligation Bond Passthrough Worksheets" — above-cap reason; process — https://www.sf.gov/information--general-obligation-bond-passthrough-worksheets
- SF Rent Board, "Water Revenue Bond Passthroughs" — above-cap reason; process — https://www.sf.gov/information--water-revenue-bond-passthroughs
- California Legislative Information, Civil Code §827 — 30/90-day notice; personal delivery or mail — https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=827.&lawCode=CIV
- California Legislative Information, Civil Code §1947.12 — AB 1482 cap; local law interaction — https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1947.12.&lawCode=CIV
- California Legislative Information, Civil Code §1954.50 — Costa-Hawkins — https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1954.50.&lawCode=CIV
- California Civil Rights Department, "Housing" — state fair housing protected characteristics; discrimination examples — https://calcivilrights.ca.gov/housing/
- HUD, "Report Housing Discrimination" — federal Fair Housing Act protected classes; complaint process; retaliation — https://www.hud.gov/reporthousingdiscrimination
- U.S. Government Publishing Office, 42 U.S.C. Chapter 45 — Fair Housing Act text — https://www.govinfo.gov/content/pkg/USCODE-2024-title42/html/USCODE-2024-title42-chap45.htm
- SF Human Rights Commission / SF.gov, "Get help for discrimination in housing" — local protected classes; complaint process — https://www.sf.gov/information--get-help-discrimination-housing
- SF Assessor / SF Planning, Property Information Map — official property/build-year verification tool — https://sfplanninggis.org/pim/?pub=true
- SF Rent Board Portal — license status and Housing Inventory — https://portal.sfrb.org/

### Validation performed

- `python3 scripts/validate_site.py` passes: 10 pages checked; 41 official source URLs on allowlist; every table data row has an official source link; no tenant initials or personal identifiers found; all internal links resolve.
- Local HTTP check: all 10 HTML pages and `style.css` return HTTP 200 from a local static server.
- HTML tag-balance check: all 10 pages parse with no unclosed or unmatched tags.
- External source links: each URL on the allowlist was checked against an official government or City of San Francisco page during this session.

### Calculations re-verified

- Unit 1: $3,995 × 1.6% = $63.92; new rent $4,058.92. This is the maximum on an April 1, 2026 effective date if the 1.6% rate is in effect. The 1.4% 2025–26 increase is not banked if the increase is imposed before 24 full months have passed; waiting until February 1, 2027 would allow 1.4% + 1.6% = 3.0%, or $119.85, new rent $4,114.85. Source: SF Rent Board irregular-periods page and banked-increases page.
- Unit 2: assumed June 1, 2026 anniversary and no prior increases. Banked: 1.8% (2020–21) + 0.7% (2021–22) + 2.3% (2022–23) + 3.6% (2023–24) + 1.7% (2024–25) + 1.4% (2025–26) = 11.5%. Current 2026–27: 1.6%. Total 13.1%. $3,150 × 13.1% = $412.65; new rent $3,562.65. This is a calculated maximum, not a verified current rent. Source: official 571 table and banked-increases rules.
- Unit 2 notice: 13.1% > 10%, so 90-day written notice is required (plus 5 days if mailed). Source: SF Rent Board and Civil Code §827.
- Unit 1 notice: 1.6% ≤ 10%, so 30-day written notice (plus 5 days if mailed). Source: SF Rent Board and Civil Code §827.

### Irregularities / items flagged for review

- Tenant-provided lease dates, rents, occupancy, and build year are not independently verified from official records. They are marked unverified on the site.
- Rent Board Housing Inventory / rent increase license status is not checked because no address/APN was provided. This is a blocking prerequisite for a lawful increase.
- Unit 2's 13.1% catch-up assumes no prior increases and the same tenants. Any prior increase changes the calculation.
- Unit 1's new occupant and continuing original tenant: banked increases do not carry over to a new tenant; confirm whether any banked amount exists and whether the tenancy is continuing.
- No official source defines "reasonable" or "normal business practice" beyond the Rent Board formula. A tenant lawyer's approval cannot be guaranteed.
- No official source documents a distinct corporate vs. individual owner practice. Both are subject to the same Rent Ordinance.
- No evidence of protected-class discrimination was found, but absence of evidence is not proof. Fair housing review is flagged.
- The site must not be treated as legal advice. The Rent Board counselor page expressly states that it cannot give legal advice.


---

## Session `arena/fa7d2d77-rentincreasesf2` — claim and handoff (2026-11-07)

### Claim

This session claims tasks 13–18 above and is acting as the **final integration session**. All
prior tasks (1–12) are recorded `done`, so no in-progress claim is being displaced. File scope
is listed per task on the board above.

### Branch-name deviation (platform constraint)

The task protocol asks for branches named `session-<id>/<task>`. This session runs on a
platform-managed branch, `arena/fa7d2d77-rentincreasesf2`, which is fixed and cannot be renamed
or switched. All work is committed to that branch and the pull request is opened from it. This
is the same convention already used by sessions `arena/3eac9d0e`, `arena/81e8c938` and
`arena/795a54b7`, so the board remains consistent.

### Handoff: PR #5 taken over under the 60-minute stale-claim rule

- **PR:** https://github.com/kanlerxz87-cyber/RentincreaseSF2/pull/5
- **Owning session:** `arena/48ffb5b4-rentincreasesf2`
- **Last activity:** 2026-11-06T14:09:21Z — more than 30 hours before this session started, with
  no commits in that window. The protocol permits any other session to take over a claim that
  is more than 60 minutes old with no commits. The takeover is recorded here.
- **Audit performed before takeover:**
  - **Privacy: PASS.** Swept all 34 files for the six supplied tenant initial pairs and for
    the two-letter initial pair. No tenant initials, names, addresses or contact details are published. The branch
    uses `Tenant A`–`Tenant D` placeholders and preserves dates and dollar amounts.
  - **Build: PASS.** `python3 build.py` exits 0 in a clean extraction: 15 HTML documents,
    256 external links, 48 sources, 24 flags, 11 dollar checks and 8 deadline checks, Census
    reconciliation, PII guard clean.
  - **Mergeability: FAIL as a direct merge.** `git merge-base HEAD refs/pr/5` is empty and
    `git merge-tree` reports `refusing to merge unrelated histories`. PR #5 was authored on an
    orphan history that shares no ancestor with `main`. It also re-adds `index.html`,
    `README.md`, `COORDINATION.md` and `.nojekyll`, which already exist on `main` with three
    sessions of accumulated work.
- **Decision:** do **not** force an unrelated-history merge, because that would risk discarding
  the work of sessions `arena/3eac9d0e`, `arena/81e8c938` and `arena/795a54b7` and would publish
  two competing sites at overlapping URLs. Instead this session **ports PR #5's verified
  findings into the live site**, re-verifying each one against the official source first, and
  credits the originating session on the Sources page. PR #5's branch and commits are left
  untouched and preserved.
- **Findings adopted for re-verification (not accepted on trust):** Rent Ordinance § 37.10C
  algorithmic pricing ban; Rules § 13.14 licensing / null-and-void; Rules § 6.14 and
  Costa-Hawkins original-occupant limit; § 37.3 additional-occupant prohibition;
  Civ. Code § 1942.5 retaliation screen; Civ. Code § 1947.12 AB 1482 non-application.
- **Findings corrected on re-verification:** PR #5 states Unit 2's full 13.1% is first
  available on 2027-06-01 and that "nothing can lawfully be done today". Re-verification
  against the Rent Board's own off-anniversary worked examples shows the 13.1% is available
  on an earlier effective date, and that a notice can be served now. See the verification log
  below. PR #5's Flag F-03 (12 vs 24 months) is also resolved rather than left as a conflict.


---

## Session `arena/fa7d2d77-rentincreasesf2` — verification log (2026-11-07)

### Official sources fetched and read directly this session

Every item below was retrieved and read during this session, not carried forward on trust.

| Source | What was confirmed |
|---|---|
| [Learn about rent increases in San Francisco](https://www.sf.gov/learn-about-rent-increases-san-francisco) | 1.6% for 3/1/2026–2/28/2027; 60% of Bay Area CPI; once per 12 months; anniversary mechanics; four worked examples including permanent loss of an unbanked allowance when the anniversary moves; 30/90-day notice +5 if mailed; notice content; base rent only; no rounding up; additional-occupant prohibition; license requirement |
| [Banked rent increases](https://www.sf.gov/information--banked-rent-increases) | 24-full-month wording; no limit; does not expire during a tenancy; new owners inherit; does not carry to a new tenant; partial increases bank the remainder; no compounding; notice must state the banked portion; license requirement |
| [Rules and Regulations Part IV](https://www.sf.gov/reports--december-2022--rent-board-rules-and-regulations-part-iv-rent-increases-not-requiring) | § 4.10(a) notice content and § 4.10(b) null-and-void consequence with the half-percent good-faith readjustment; § 4.12(a) "a full 12 months must have elapsed from the date that an annual rent increase … could have been imposed"; § 4.12(b) banked portion and its source dates |
| [Increasing rents during irregular periods](https://www.sf.gov/information--increasing-rents-during-irregular-periods) | Controlling definition of the anniversary date; off-anniversary increases at 12–24 and 24+ months; no petition needed; no compounding; no rounding up; base rent includes parking/storage |
| [571 Allowable Annual Increases 26-27 (PDF)](https://www.sf.gov/documents/34344/571_Allowable_Annual_Increases_26-27_1.pdf) | Full historical table read line by line: 2026–27 1.6%, 2025–26 1.4%, 2024–25 1.7%, 2023–24 3.6%, 2022–23 2.3%, 2021–22 0.7%, 2020–21 1.8%, 2019–20 2.6%. Table ends 2/28/2027 |
| [The Rent Board Housing Inventory](https://www.sf.gov/rent-board-housing-inventory) | All owners of residential property report; tenant-occupied units receive a license automatically; free; March 1 annual deadline; no monetary late penalty; license must be current on the effective date; license need not accompany the notice; 7/1/2022 and 3/1/2023 phase-in; submissions are public and under penalty of perjury; 30-day contact-update rule |
| [Rules § 13.14 Licensing](https://sfrb.org/section-1314-licensing-%E2%80%93-notice-rent-increase) | Unlicensed annual/banked increase is null and void in its entirety; **effective date, not service date** controls; banking rights survive a void increase; applies to increases effective on/after 3/1/2023 for condos and buildings under ten units |
| [Notice of Owner Noncompliance](https://www.sf.gov/notice-of-owner-noncompliance-with-housing-inventory) | Refund exposure across multiple years; how to check license status by address/APN; license **not** required for 6.14/Costa-Hawkins increases or passthroughs; paper filing route; tenant petition and summary petition routes |
| [Rent Ordinance § 37.3](https://www.sf.gov/information--sec-373-rent-limitations) | § 37.3(a)(1) 60% of CPI, 7% ceiling, license hook to § 37.15; § 37.3(a)(2) banking subject to § 37.15 with no waiting period stated in the ordinance itself |
| [Rent Increases Under Section 6.14 And Costa-Hawkins](https://www.sf.gov/information--rent-increases-under-section-614-and-costa-hawkins) | Unlimited increase only when the **last original occupant vacates**; timely written 6.14 notice on each subsequent occupant; generally 60 days reasonable; co-tenants never subject to the Costa-Hawkins reset; co-tenant status can arise from acceptance of rent; no petition required but tenant may challenge |
| [Charging for Additional Occupants Prohibited](https://www.sf.gov/information--charging-additional-occupants-prohibited) | Unlawful even if the lease permits it, including a newborn child; tenant may void and recover overcharges; O&M petition or utility passthrough is the only lawful cost-recovery route |
| [Algorithmic devices that set rent are prohibited](https://www.sf.gov/information--algorithmic-devices-set-rent-are-prohibited-san-francisco) | § 37.10C effective 10/14/2024; definition of algorithmic device and non-public competitor data; sale and use prohibitions; per-unit per-month violations; up to $1,000 per violation; tenant **and tenants' rights organization** right of action; fee-shifting |
| [The California Tenant Protection Act (AB 1482)](https://www.sf.gov/reports--california-tenant-protection-act-2019-ab-1482) | 8.8% for San Francisco 8/1/2026–7/31/2027; expressly "does NOT apply for units under the rent increase limitations of the San Francisco Rent Ordinance"; corporate/trust/LLC ownership defeats the single-family exemption; two-unit owner-occupied exemption |
| [Civil Code § 827](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=827.&lawCode=CIV) | (a)(1) mid-term proration at the prior rate; (b)(1) personal delivery or mail under CCP § 1013; (b)(2) 30 days at ≤10%; (b)(3)(A) 90 days above 10%, measured against rent charged at any time in the prior 12 months and combined with other increases |
| [Civil Code § 1942.5](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1942.5.&lawCode=CIV) | (a) 180-day bar and its five trigger events, latest-date rule; (b) once per 12 months; (c)/(e) immigration threats; (d) organising; (f) lawful cause preserved and waiver void; (g) good-faith statement of grounds in the notice; (h) $100–$2,000 punitive damages; (i) attorney's fees |
| [Learn about San Francisco rental laws](https://www.sf.gov/learn-about-san-francisco-rental-laws) | June 13, 1979 coverage cutoff; Property Information Map as the verification tool; just-cause examples; categories with eviction protection only; fully exempt unit types |
| [Costa-Hawkins partial exemption (Topic 019)](https://www.sf.gov/information--partial-exemption-certain-single-family-homes-and-condominiums-under-costa-hawkins) | A single-family dwelling with a legal **or** illegal in-law is a two-unit building and **not exempt**; exemption still leaves just cause and the Rent Board fee |
| [Tenant and Landlord Resources](https://www.sf.gov/tenant-and-landlord-resources) | Eviction Defense Collaborative free legal help; tenant counselling organisations; Rent Board address 25 Van Ness Ave Suite 700 and 415-252-4600; landlord-side resources |
| [Get help for discrimination in housing](https://www.sf.gov/information--get-help-discrimination-housing) | Full local protected-characteristic list including age, height, weight, source of income, pregnancy status; "change the terms of your housing" is expressly prohibited; HRC, CRD and HUD complaint routes |

### Resolution of the 12-month / 24-month conflict (PR #5 flag F-03)

Read together, the two official formulations are **consistent**, not contradictory:

- Rules § 4.12(a) measures **12 full months from the date the allowance could first have been imposed**.
- The sf.gov banked-increases page measures **24 full months from the last increase or move-in**.
- The allowance first becomes available exactly 12 months after the last increase or move-in, so the
  two starting points are 12 months apart and both land on the same date.
- Verified against Unit 1: tenancy 2025-02-01 → allowance available 2026-02-01 → banked 2027-02-01,
  which is simultaneously 12 months from availability and 24 months from move-in.

Published on `analysis.html` with all three sources and retained as flag **F-16** so the wording
difference stays visible. It changes no figure on the site.

### Corrections made to PR #5's conclusions on re-verification

1. **Unit 2 timing.** PR #5 stated the full 13.1% is first available on 2027-06-01. The Rent Board's
   off-anniversary worked examples show that banked percentages plus the current annual allowance can
   be imposed off-anniversary. The 11.5% is already banked and the 1.6% is the current allowance until
   2027-02-28, so **13.1% is available on an effective date in February 2027**. Sources:
   [irregular periods](https://www.sf.gov/information--increasing-rents-during-irregular-periods),
   [rent increases worked examples](https://www.sf.gov/learn-about-rent-increases-san-francisco).
2. **"Nothing can lawfully be done today."** Not correct. A notice may be served now for a future
   effective date; § 827 sets a minimum notice period, not a waiting period before service. The
   suggested Unit 2 date of 2027-02-15 requires service by **2026-11-17** (mailed 2026-11-12), which is
   still ahead. Source: [Civil Code § 827](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=827.&lawCode=CIV).
3. **Unit 1 April 1, 2026 framing** inherited from earlier sessions was stale. Replaced with explicit
   future effective-date scenarios.

### Verification performed

- `python3 scripts/sync_nav.py` — 12 pages, one canonical navigation, no drift.
- `python3 scripts/validate_site.py` — **PASSED**: 12 pages; 46 official source URLs on the allowlist;
  every table data row carries an official source link; every row matches its header column count;
  no tenant initials or personal identifiers; all internal links resolve.
- `python3 scripts/verify_calculations.py` — **PASSED**: 39 assertions re-deriving every dollar amount
  and every service deadline from the official 571 percentages and the § 827 notice periods, and
  confirming each computed value appears in the published HTML.
- HTML tag-balance parse of all 12 pages — **PASSED**, no unclosed or mismatched tags.
- Local HTTP check — all 12 pages and `style.css` returned **200**.
- Privacy sweep — no name, initial, address, contact detail or parcel number published; occupants
  appear only as Tenant A–F placeholders; dates and dollar amounts preserved exactly.

### Irregularities flagged (published on the Flagged for Review page)

F-01 build year and coverage · F-02 lease dates, rents and occupancy · F-03 license status unchecked ·
F-04 Unit 1 effective-date choice · F-05 Unit 1 tenancy status · F-06 Unit 2 banked balance ·
F-07 Unit 2 notice timing · F-08 corporate practice claims · F-09 "reasonable" undefined ·
F-10 no guaranteed lawyer approval · F-11 discrimination and retaliation review · F-12 free-lawyer
eligibility · F-13 Rent Board fee · F-14 passthrough petitions · **F-15 6.14 notice may be out of time ·
F-16 official banking wording differs · F-17 2027–28 rate unpublished · F-18 retaliation screen cannot
be run · F-19 Unit 2 service window is short · F-20 co-tenant vs subtenant status · F-21 Housing
Inventory submissions are public · F-22 no algorithmic pricing tool may be used.**

The eight bolded items are new this session. None blocks publication; all are listed with source links
for the owner to review.

### Scope note

Task 15 originally listed a `market.html` page. It was dropped: for units under the SF rent-increase
limitations the lawful amount is fixed by formula, and no official source publishes a market benchmark
that would govern these units. Adding one would have required inference, which the verification
standard forbids. The "reasonable and normal" question is answered on `analysis.html` and
`executive-summary.html` from the ordinance, the AB 1482 page and the fair-housing sources instead.


---

## PR #8 — final integration, merge and deployment record

- **PR:** https://github.com/kanlerxz87-cyber/RentincreaseSF2/pull/8
- **Title:** Final integration: verified SF rent-increase review, licence process first, 12-page site
- **Branch:** `arena/fa7d2d77-rentincreasesf2` → `main`
- **Merge result:** **MERGED** at 2026-11-07T21:02:32Z
- **Merge commit:** `9a306b1842e68322737883cafa69e6d03ba4157b`
- **Merge method:** merge commit
- **PR check:** `Validate site` passed (run 42413886322) — nav sync, site validation and calculation
  re-derivation all green before merge.
- **Post-merge check:** `Validate site` on `main` passed (run 42413929437).
- **GitHub Pages:** `pages build and deployment` run 42413928882 completed; Pages API status **built**;
  latest build commit `9a306b1842e68322737883cafa69e6d03ba4157b`, which matches `main` HEAD exactly.
- **Live site:** https://kanlerxz87-cyber.github.io/RentincreaseSF2/
- **Live verification:** the newly added `occupancy.html` was fetched from the public URL after
  deployment and renders the ported Rules § 6.14 analysis, the additional-occupant prohibition and
  the 220-day / 60-day notice-window table. All 12 pages and `style.css` are present on `main` at the
  deployed commit, and all returned HTTP 200 from the local static server before merge.

### Pages on the live site (12)

`index.html`, `executive-summary.html`, `units.html`, `analysis.html`, `occupancy.html`, `laws.html`,
`process.html`, `tenant-protections.html`, `practices.html`, `checklist.html`, `flagged.html`,
`sources.html`.

### PR #5 disposition

- **Closed** with a full explanatory comment: https://github.com/kanlerxz87-cyber/RentincreaseSF2/pull/5
- Reason: unrelated git history made a direct merge unsafe, not any defect in the work. Privacy and
  build audits both passed. Its verified findings were re-checked against primary sources and
  re-implemented in PR #8; three conclusions were corrected. The branch and its six commits are
  preserved untouched, and the originating session is credited on the Sources page.
- No file on the PR #5 branch was edited by this session.

### Handoff complete

Tasks 13–18 are all `done`. No claim is left in progress by this session, and no other session's
work was discarded. The eight new flagged items (F-15 … F-22) are published on the Flagged for Review
page with source links and do not block anything.


---

## Privacy remediation (2026-11-07, this session)

**Leak found and closed in the published files.** While doing the final privacy sweep, this session
found that the PR #3 review section of `COORDINATION.md` — written by an earlier session — quoted the
six supplied tenant initial pairs verbatim. GitHub Pages serves the repository root, so that Markdown
file was publicly retrievable at `https://kanlerxz87-cyber.github.io/RentincreaseSF2/COORDINATION.md`.
Ironically the passage was itself explaining why publishing initials is unacceptable.

Actions taken:

1. Redacted the initials from `COORDINATION.md`, leaving the review finding intact and noting the
   redaction. Also removed a stray two-letter initial from this session's own audit text.
2. Extended `scripts/validate_site.py` so the personal-identifier sweep covers `README.md` and
   `COORDINATION.md`, not just the HTML pages. CI now fails if any public document reintroduces them.
3. Published the issue as **F-23** on the Flagged for Review page.

**Still outstanding, and deliberately not automated:** the repository is public and the earlier
commits still contain the initials in history. Rewriting history is destructive and would discard
other sessions' commits, so it was not performed. The owner's options — make the repo private, rewrite
history, or accept the exposure — are set out on the Flagged for Review page.

## Session `arena/bf462feb-rentincreasesf2` — independent audit (2026-11-07)

This session arrived after PR #10 merged and audited the integrated site as an outside reviewer.
It wrote no part of the material it audits. Its deliverables are two new files and this record.

### Position and scope discipline

- **Branch:** platform-assigned `arena/bf462feb-rentincreasesf2`; the standing `session-<id>/<task>`
  naming is not available because the platform ties a session to one branch.
- **Rebased onto `origin/main` at `0f32ab2`** before starting, so the audit reads the integrated
  12-page site rather than a superseded revision.
- **Two sessions were still active** during this audit (`arena/fa7d2d77-rentincreasesf2`, last
  commit 21:06Z; `arena/2b3012a0-rentincreasesf2`, last commit 20:58Z), so all twelve HTML pages,
  `scripts/validate_site.py` and `scripts/sync_nav.py` were treated as owned and were **not**
  edited. Corrections belonging in those files are logged as change requests CR-01…CR-08 in
  `AUDIT.md` section 6 instead.
- **One page was dropped as duplicative.** A drafted `compliance-checklist.html` was deleted before
  publication when the audit found that `checklist.html` already covers every item in it. Shipping
  a near-duplicate would have created two checklists to keep in sync.
- **An error in this session's own draft was caught and corrected before publication.** It asserted
  14.7% for Unit 2 on 2027-06-01 by treating the 2026-27 rate as in effect on that date. It is not:
  2027-06-01 falls in the 2027-28 period, which is unpublished. The main site was already correct
  to leave that cell blank. Recorded in `AUDIT.md` section 3.

### Result

**No published figure is wrong and no value was invented.** Thirteen classes of figure were
re-derived from primary sources without reusing the site's arithmetic, and seven notice deadlines
were recomputed by script from a base date of 2026-11-07. All confirmed. The repository's own
`scripts/verify_calculations.py` was also run and passes 39 assertions.

Ten irregularities are logged as **A-01…A-10** in `AUDIT.md` section 4. Three are high:

- **A-02** — Unit 2's 13.1% requires an effective date on or before 2027-02-28, because Form 571
  ends there and the 2027-28 percentage is unpublished. With a 90-day notice the last service date
  is **2026-11-30** by personal delivery and **2026-11-25** by mail. The mailed route to the
  earliest reachable date (2027-02-05) closed on 2026-11-02. The site records the window's outer
  limit as a fact but not as a closing deadline, and banked amounts may only be given at the time of
  an annual increase, so the window cannot be reopened at will.
- **A-07** — task numbers 13–15 exist twice with different owners and meanings
  (`arena/2b3012a0-rentincreasesf2` on its branch, `arena/fa7d2d77-rentincreasesf2` on `main`).
  `arena/2b3012a0-rentincreasesf2` also branched from `62f6f59`, which predates PRs #6–#10, and its
  in-progress work rewrites `executive-summary.html`; merging it as-is would revert the license
  clarification and the privacy redaction. It must rebase onto current `main` first.
- **A-08** — any Markdown at the repository root is publicly served by GitHub Pages, because Pages
  publishes `/` of `main` with `.nojekyll`. Confirmed empirically during this audit: the
  `COORDINATION.md` Pages URL returned raw file content. That is the mechanism by which tenant
  initials were exposed before PR #10 remediated them. The standing rule is now written down here so
  a future session does not repeat it with `AUDIT.md` or any other root Markdown file.

**Flag F-16 is resolvable and has been resolved.** Two official Rent Board sources state different
banking intervals — Rules §4.12(a) says a full 12 months from when an allowance could have been
imposed; the *Banked rent increases* summary page says at least 24 full months without any increase.
Rather than accept either at face value, all three possible readings were tested against **both**
published Rent Board worked examples:

| Reading | Example A (official answer 6.7%) | Example B (official answer 3.3%) | Verdict |
|---|---|---|---|
| Per-allowance, 12 months — Rules §4.12(a) | 6.7% | 3.3% | **Matches both** |
| Global, 24 months | 6.7% | 4.7% | Fails B |
| Per-allowance, 24 months | 5.0% | 1.6% | Fails both |

Only Rules §4.12(a) reproduces both. The resolution **confirms** the figures the site already
publishes — Unit 1 at 1.6% ($4,058.92) before 2027-02-01 and 3.0% ($4,114.85) on it; Unit 2 at
11.5% banked plus 1.6% current = 13.1% ($3,562.65). CR-03 asks for F-16 to be closed on this basis.

Two further primary-source points were verified and are new to the repository: Rules §13.14 fixes
the license test to the **effective date, not the service date**, and expressly preserves banking
rights even where an increase is found null and void — which materially softens flag F-03. And
Rent Ordinance §37.3(b)(5) independently makes a nonconforming increase null and void at the
ordinance level, not only under Rules §4.10(b).

A new discrepancy between two official Rent Board documents was found and logged as **A-06**: the
license requirement's start dates are given as 1 July 2022 / 1 March 2023 on the Housing Inventory
and rent-increase pages, but as 1 July 2020 / 1 March 2021 on the Rent Board's own Form 538
worksheet. Practical impact is nil; both dates are past and a current license is required now either
way. For a two-unit building the applicable group is "fewer than 10 units" on either version.

### Validation performed

- `python3 scripts/validate_site.py` — PASSED (12 pages, 46 allowlisted URLs, per-row source links,
  column integrity, privacy sweep over HTML **and** public Markdown).
- `python3 scripts/verify_calculations.py` — PASSED (39 assertions).
- Personal-identifier sweep over all `*.html` and `*.md` — **0 hits**.
- `banking-rule.html` standalone check — tags balanced with no unclosed or stray elements; every
  table data row carries an official source link; 20 unique external URLs, all on official
  government or City domains (`sf.gov`, `sfrb.org`, `leginfo.legislature.ca.gov`, `portal.sfrb.org`,
  `sfplanninggis.org`); 14 internal links, none broken; navigation covers all twelve existing pages;
  the not-legal-advice footer is present.
- Every date in `banking-rule.html` section 5 recomputed by script from 2026-11-07.

### Known limitation

`banking-rule.html` is **not** linked from the shared navigation and is **not** in the validator's
`PAGES` list, because both live in files owned by other sessions. It is reachable by direct URL and
from `AUDIT.md`. CR-01 gives the exact two-line change to fix this: add the page to `NAV` in
`scripts/sync_nav.py`, run it, and add the filename to `PAGES`. The page is written to pass the
validator as-is once listed.

## PR #11 — independent audit, merge and deployment record

- **PR:** https://github.com/kanlerxz87-cyber/RentincreaseSF2/pull/11
- **Title:** "Independent audit: resolve flag F-16, publish Unit 2's closing service deadline, confirm every figure"
- **Merged to `main`:** 2026-11-07T21:32:15Z, merge commit `041632c1cd508ab4362e9e7ce55c3d2b23b81a23`
- **Merge method:** merge commit
- **Diff shape:** 3 files, 587 insertions, **0 deletions** — purely additive, so no other session's work could be reverted
- **Validation on the PR:** `Validate site` passed (`validate` job, 5s)
- **Validation post-merge:** `Validate site` **success** on `041632c`
- **GitHub Pages:** `pages build and deployment` **success** on `041632c`; Pages status `built`; build created 21:32:16Z, updated 21:32:35Z
- **Live URLs re-fetched after deployment:**
  - https://kanlerxz87-cyber.github.io/RentincreaseSF2/banking-rule.html — serving, renders the decisive F-16 test table
  - https://kanlerxz87-cyber.github.io/RentincreaseSF2/AUDIT.md — serving, renders the full irregularity register
- **Site integrity:** all twelve pre-existing pages untouched; `scripts/validate_site.py` and `scripts/verify_calculations.py` both still pass on the merged tree.

### Files added by this session

| File | Purpose |
|---|---|
| `AUDIT.md` | Line-by-line independent audit: scope table, method, re-verification results, irregularity register A-01…A-10, confirmed-correct register, change requests CR-01…CR-08, reproducibility commands, official sources read directly |
| `banking-rule.html` | Resolves flag F-16 by testing all three readings of the banking interval against both official Rent Board worked examples; independently re-verifies every published figure; states the Unit 2 service window as a closing deadline |

### Outstanding for a future integration session

`banking-rule.html` is live but is **not** in the shared navigation and **not** in the validator's
`PAGES` list, because both live in files owned by other sessions at the time of this audit. It is
reachable by direct URL and from `AUDIT.md`. **CR-01** in `AUDIT.md` §6 gives the exact change:
add `("banking-rule.html", "Banking Interval (F-16)")` to `NAV` in `scripts/sync_nav.py`, run
`python3 scripts/sync_nav.py`, and add `"banking-rule.html"` to `PAGES` in
`scripts/validate_site.py`. **CR-02** allowlists the two official URLs the new page cites that are
not yet in `VERIFIED_URLS`: Rent Board Rules §13.14 on `sfrb.org`, and Form 538 on `sf.gov`. The
page is written to pass the validator unchanged once listed — it was checked standalone for tag
balance, per-row source links, official-domain-only external links, internal link resolution, full
twelve-page navigation and the not-legal-advice footer.

CR-03 to CR-08 carry the remaining corrections into files owned by others, including closing F-16
on the evidence, publishing the 2026-11-30 service deadline, and adding Rules §13.14's two
favourable provisions.

## Session `arena/f0449766-rentincreasesf2` — final integration of audit change requests (2026-11-08)

**Branch:** `arena/f0449766-rentincreasesf2`, branched from `main` at `a747d82` (PR #12 merge). This session applied every change request logged in `AUDIT.md` §6 and closed the remaining audit findings. It is the integration session that `AUDIT.md` (CR-01…CR-08) was written for.

### What was applied

| ID | Change applied | Files |
|---|---|---|
| CR-01 | `banking-rule.html` added to the canonical navigation under a new **Verification** group; added to the validator's page list; `scripts/sync_nav.py` re-run (13 pages updated) | `scripts/sync_nav.py`, `scripts/validate_site.py`, all `*.html` nav blocks |
| CR-02 | Form 538 worksheet URL allowlisted (the §13.14 URL was already allowlisted); allowlist now 47 URLs | `scripts/validate_site.py` |
| CR-03 | Flag **F-16 closed as resolved** on the evidence (only the per-allowance 12-month test in Rules §4.12(a) reproduces both official worked examples, 6.7% and 3.3%; global-24 gives 4.7% vs official 3.3%; per-allowance-24 gives 5.0% vs official 6.7%). Linked `banking-rule.html`; the 24-month wording on `laws.html`, `process.html`, `practices.html`, `tenant-protections.html` annotated with the resolution | `flagged.html`, `analysis.html`, `laws.html`, `process.html`, `practices.html`, `tenant-protections.html` |
| CR-04 | Closing service window published as a deadline: Unit 2's 13.1% needs an effective date on or before **2027-02-28** → serve by **2026-11-30** (personal) / **2026-11-25** (mail); the mailed route to 2027-02-05 closed 2026-11-02; Unit 1 serve by 2027-01-02 | `index.html`, `executive-summary.html`, `checklist.html` (new row 2.8a) |
| CR-05 | Rules §13.14's two provisions added: the license test is keyed to the **effective date, not the service date** (express regulatory wording now quoted), and a void increase does **not** affect the owner's banking rights or the ability to accumulate otherwise lawful increases. F-03's "what to verify" softened accordingly; A-05 wording added to `process.html`; "Final review before service" gains a *Banking rights survive* row | `laws.html`, `checklist.html`, `flagged.html`, `process.html` |
| CR-06 | Official-documents discrepancy on the license requirement's start date (Housing Inventory / *Learn about rent increases*: 2022-07-01 for 10+ unit buildings vs 2023-03-01 for condominiums and buildings with fewer than 10 units; Form 538 worksheet: 2020-07-01 / 2021-03-01) logged as flag **F-24** and as a laws.html row. Practical impact nil — both dates are past; a two-unit building is "fewer than 10 units" on either version | `flagged.html`, `laws.html` |
| CR-07 | Standing rule recorded above (**Root Markdown is public**); validator privacy sweep widened from two named files to **all** root `*.md` | `COORDINATION.md`, `scripts/validate_site.py` |
| CR-08 | Colliding task rows 13–15 annotated (see footnote ¹ under the task board); the `arena/2b3012a0-rentincreasesf2` branch is documented as needing a rebase before any PR; it was **not** merged or modified | `COORDINATION.md` |
| A-03 | `checklist.html` "Take nothing yet" now states banked amounts may only be given at the time of an annual increase (Rules §4.12(a)) and that the window cannot be reopened at will | `checklist.html` |
| README | 13 pages listed; closing deadline stated; page count corrected | `README.md` |

### Sources (all official, read or re-checked by prior sessions and cited per row)

Rules §4.12(a)/§4.10/§4.12(b) and Rules §13.14 (sf.gov / sfrb.org) · Rent Ordinance §37.3(a)(2), §37.3(b)(5) (sf.gov) · Form 571 Allowable Annual Increases 26-27 (sf.gov PDF) · Form 538 2024-25 Bond Measure Worksheet (sf.gov PDF) · *Learn about rent increases*, *Banked rent increases*, *Increasing rents during irregular periods*, *Annual rent increase for multiple years*, *Housing Inventory*, *Current Rates*, *Notice of Owner Noncompliance* (sf.gov) · Civ. Code §827, §1942.5 (leginfo.legislature.ca.gov). Every added table row carries an official source link; `banking-rule.html` carries the decisive F-16 test with both official worked examples reproduced.

### Verification performed in this session (2026-11-08)

- `python3 scripts/sync_nav.py` — NAV OK, 13 pages.
- `python3 scripts/validate_site.py` — **PASSED**: 13 pages; 47 official URLs on allowlist; every table data row has an official source link; no personal identifiers in HTML or root Markdown; all internal links resolve; table column integrity; every page in nav.
- `python3 scripts/verify_calculations.py` — **PASSED**: 39 assertions; Unit 1 3.0% → $119.85 → $4,114.85; Unit 2 13.1% → $412.65 → $3,562.65.
- Personal-identifier sweep over all `*.html` and root `*.md` — **0 hits**.
- `git pull --rebase` before every push; branch pushed after each commit.

### Irregularities / flags

- **F-16 closed** on the evidence (see CR-03).
- **A-06** logged as **F-24** (official documents disagree on the license start date; practical impact nil).
- **A-02** addressed: the closing service window (2026-11-30 / 2026-11-25) is now published in `index.html`, `executive-summary.html` and `checklist.html` row 2.8a, in addition to `banking-rule.html`.
- **A-04 / A-05** addressed (Rules §13.14 provisions published; F-03 softened).
- **A-07** documented, not resolved: `arena/2b3012a0-rentincreasesf2` must rebase before any PR; left for that session.
- No new irregularity introduced. Values that remain unverifiable (2027–28 allowance; license status; rent ledger) remain blank and flagged.

### Publication

Work PR and deployment record follow in the *PR and deployment record* section and in the follow-up record commit.

## PR #14 — final integration, merge and deployment record

- **PR:** https://github.com/kanlerxz87-cyber/RentincreaseSF2/pull/14
- **Title:** "Final integration: apply audit change requests CR-01..CR-08, close F-16, publish closing service deadline"
- **Check on PR:** `validate` passed (6s); `mergeStateStatus` CLEAN, `mergeable` MERGEABLE
- **Merged to `main`:** 2026-11-08T22:48:36Z, merge commit `8017d7994a34b7d2d4cf3a09a2818306d5b60f18`
- **Merge method:** merge commit
- **Validation post-merge:** `Validate site` **success** on `8017d79` (2026-11-08T22:48:39Z)
- **GitHub Pages:** `pages build and deployment` **success** on `8017d79` (created 22:48:38Z, completed); Pages API reports latest build `8017d79`, status `built`, error `null` (updated 22:48:58Z). Live-URL fetch from the sandbox is not possible (outbound network is limited to github.com and package registries); deployment success is confirmed via the Actions and Pages APIs.
- **Task board:** tasks 24–26 marked done by this record. Flagged irregularities (F-24, and the standing F-01…F-23 owner actions) are published on the Flagged for Review page and do not block the merge.
- **Not merged / not modified:** branch `arena/2b3012a0-rentincreasesf2` (duplicate task numbers 13–15, stale base `62f6f59`; must rebase before any PR). Tracked as A-07.
- The follow-up record commit (this section) is merged to `main` via a separate record PR, the same pattern as PRs #9 and #12.

## Session `arena/e8ef4a1a-rentincreasesf2` — parallel-session race record (2026-11-08)

This session claimed tasks **24–25** at 2026-11-08T22:45:59Z (branch tip `299f8f7`, PR #13) to apply
`AUDIT.md` change requests CR-01…CR-08. Session `arena/f0449766-rentincreasesf2` had independently
claimed tasks **24–26** at 2026-11-08T22:45:43Z — sixteen seconds earlier — and opened PR #14 with an
equivalent implementation. Both branches were based on `a747d82`; neither session could see the
other's claim before branching.

**Resolution (coordination protocol, earlier claim wins):**

- Both branches were independently verified and found equivalent: `scripts/validate_site.py` PASSED
  (13 pages, 47 official-source URLs on allowlist, per-row source links, column integrity, privacy
  sweep over all root Markdown); `scripts/verify_calculations.py` PASSED (39 assertions); tag-balance
  check OK on all 13 pages; zero personal-identifier hits.
- This session additionally cross-verified PR #14 in a detached worktree before it merged:
  validator, calculation script, tag balance and privacy sweep all PASSED; PR `validate` check green;
  diff reviewed line by line (CR-01…CR-08 all applied, no unrelated changes, no deletions of other
  sessions' work).
- **PR #14 merged** at 2026-11-08T22:48:36Z, merge commit `8017d7994a34b7d2d4cf3a09a2818306d5b60f18`.
  Post-merge `Validate site` SUCCESS on `8017d79`; `pages build and deployment` SUCCESS; Pages later
  rebuilt for record merge `b3ed89f` (PR #15) and reports status **built**.
- **PR #13 closed unmerged** (superseded) with an explanatory comment:
  https://github.com/kanlerxz87-cyber/RentincreaseSF2/pull/13#issuecomment-… Its commits remain
  retrievable via the pull-request ref. This session's branch was reset to `origin/main` before this
  record commit; the earlier tip is preserved on closed PR #13. No material content differs between
  the two implementations; PR #14 was retained as canonical.
- No action taken against `arena/2b3012a0-rentincreasesf2` (A-07). Root Markdown remains public
  (A-08); personal identifiers must never be committed to root `*.md`.

**Sources of truth:** CR-01…CR-08 dispositions are recorded in the PR #14 record above; line-by-line
verification of every published figure is in the 2026-11-07 audit (`AUDIT.md`) and in
`banking-rule.html`. Official sources re-read live in this session: Housing Inventory
(https://www.sf.gov/rent-board-housing-inventory) and Form 571 Allowable Annual Increases 26-27
(https://www.sf.gov/documents/34344/571_Allowable_Annual_Increases_26-27_1.pdf) — both confirm the
site's license-requirement and 1.6% / 1.4% / 11.5% banked figures.

## Session `arena/e8ef4a1a-rentincreasesf2` — post-merge corrections salvaged from PR #16 (2026-11-08)

`arena/342c4cc9-rentincreasesf2` opened PR #16 ("Final integration: apply CR-01–CR-07, correct
four citation defects…"), based on the pre-integration commit `a747d82`. It duplicates work that
merged in PRs #14/#15 and would revert #14's F-03 softening if merged as-is, so it is not being
merged. Its four findings were independently re-verified against official sources and applied
surgically on this branch instead:

- **I-01** — "Nonconforming Rent Increases" sentence is Rent Ordinance **§ 37.3(b)(5)**, not
  § 37.3(a)(5) (verified verbatim at sf.gov/information--sec-373-rent-limitations). Fixed in
  `banking-rule.html`, `AUDIT.md`, `COORDINATION.md`; logged as site flag **F-25**.
- **I-02** — stale `units.html` rows: confirmed absent on `main`; no change required.
- **I-03** — `sources.html` verification stamp 2026-11-06 → 2026-11-08 (badge and footer).
- **I-04** — `laws.html` Costa-Hawkins row rewritten: § 1954.52(a) exempts units with a
  certificate of occupancy issued after **1995-02-01** (plus the local-exemption and
  separately-alienable grounds); the **1979-06-13** date comes from the Rent Ordinance / Rent
  Board rental-laws page. Logged as site flag **F-26**; Civ. Code § 1954.52 added to the
  validator allowlist.
- Re-stamp: every published "today"-relative date and count moved to **2026-11-08**
  (`verify_calculations.py` REVIEW_DATE + new closing-window assertions — **47 assertions
  pass**; `banking-rule.html` § 5, F-15/F-19 day counts, `occupancy.html`, `index.html`,
  `executive-summary.html`, `checklist.html`, `analysis.html`).
- README flag range F-01…F-24 → F-01…F-26.

All checks green after the corrections (validator, 47-assertion calculation script, tag balance,
privacy sweep over all root Markdown). `PR #16` should be rebased onto current `main` by its
session or closed; its unique verified content is now on `main`.

## PR #17 — post-merge corrections, merge and deployment record

- **PR:** https://github.com/kanlerxz87-cyber/RentincreaseSF2/pull/17
- **Title:** "Record race resolution + apply PR #16's verified citation corrections"
- **Merged to `main`:** 2026-11-08T22:54:22Z, merge commit `66ad077de9f0d9ca03ed1d197eaffeeff3ebdb4a`
- **Merge method:** merge commit
- **Validation on the PR:** `validate` passed (8s, run 42532483354); post-merge `Validate site` **success** on `66ad077`; `pages build and deployment` **success** on `66ad077` (22:54:44Z); Pages latest build `66ad077`, status **built** (updated 22:54:45Z).
- **Content:** race-resolution record; PR #16's four findings independently re-verified and applied surgically (§ 37.3(b)(5) citation fix `banking-rule.html`/`AUDIT.md`/`COORDINATION.md`; `sources.html` stamp → 2026-11-08; `laws.html` Costa-Hawkins row rewritten to Civ. Code § 1954.52(a)/1979-06-13 Rent Ordinance attribution; re-stamp of every today-relative date to 2026-11-08; `verify_calculations.py` REVIEW_DATE 2026-11-08 + closing-window assertions — **47 assertions pass**); site flags **F-25** (citation, corrected) and **F-26** (Costa-Hawkins attribution, corrected) added; Civ. Code § 1954.52 allowlisted; README flag range → F-01…F-26; AUDIT.md addendum appended.
- **Verification:** `validate_site.py` PASSED (13 pages; 48 allowlisted official URLs; per-row source links; column integrity; privacy sweep over all root Markdown); `verify_calculations.py` PASSED (47 assertions); tag balance OK; 0 personal-identifier hits.
- **Not merged:** PR #16 (stale base `a747d82`, duplicates merged work, would revert #14's F-03 softening). Comment posted on PR #16 explaining what was salvaged; its session can rebase or close.
- **Flagged items remain open for the owner** (see flagged.html): F-01…F-24 inputs and license status; F-25/F-26 recorded as corrected. None block publication.

## PR #18 — merge and deployment record (session `arena/b2b8a2de-rentincreasesf2`)

- **PR:** https://github.com/kanlerxz87-cyber/RentincreaseSF2/pull/18
- **Title:** "Fix the stale 'today' and mis-populated row in banking-rule.html; guard the printed day counts"
- **Merged to `main`:** 2026-11-08T22:58:25Z, merge commit `0ec790acaffd2ba38c529b629a88649857d81a2e`
- **Merge method:** merge commit (`gh pr merge 18 --merge`)
- **`mergeStateStatus` before merge:** `CLEAN` / `MERGEABLE`
- **Validation on the PR:** `validate` job **pass** (run 42532797769)
- **Validation post-merge:** `Validate site` **success** on `0ec790a`
- **GitHub Pages:** `pages build and deployment` **success** on `0ec790a`;
  `pages/builds/latest` → `{"commit":"0ec790a…","status":"built"}`, created 22:58:27Z, updated 22:58:47Z;
  `gh api …/pages` → `{"status":"built","build_type":"legacy"}`
- **Deployed-artifact verification.** The chunked live-page fetch failed at the proxy layer
  (`SignatureDoesNotMatch`, a fetcher artefact — not a site error), so the deployed file was read
  back directly at the built commit instead:
  `gh api repos/.../contents/banking-rule.html?ref=0ec790a…` → **0** occurrences of the stale
  "7 November 2026", **3** of "8 November 2026", **0** mis-populated `<td>30 / 35</td>` cells, the
  corrected Unit 1 row present, day counts `9 / 4`, `22 / 17`, `69 / 64`, `55 / 50`, `115 / 110`,
  and the closing-deadline row `2026-11-30 / 2026-11-25 / 22 / 17`.
- **Live fetch that did succeed:** https://kanlerxz87-cyber.github.io/RentincreaseSF2/banking-rule.html
  rendered "counted back from today, **8 November 2026**" and "Banked as of 2026-11-08?".

### Parallel-session races during this task (logged per the coordination rules)

`main` moved **five** times while this session worked: PR #14 → #15 → #17 → #19 → #18.
Two sessions (`arena/f0449766`, `arena/e8ef4a1a`) independently applied overlapping parts of the
same correction set, and PR #19 (`cf609b6`) explicitly salvaged this branch's base-date assertion
before this branch merged.

Resolution used throughout: **never force a divergent tree through.** Twice this branch was reset
to `origin/main` and re-inspected for what was *still* wrong, so only the residual difference was
committed. The final PR therefore touches **two files and one log** — `banking-rule.html`,
`scripts/verify_calculations.py`, `COORDINATION.md` — and reverts nothing. No other session's work
was discarded, and no session's claim was edited.

One rebase conflict occurred, in this file's task board: `arena/f0449766` had marked task 26 `done`
(PR #15) where this session's claim still carried the older `pending` row. Resolved by keeping
their `done` row and only the new rows 27–29.

### Net effect on the published site

Two reader-visible defects removed and one regression guard added:

1. The Banking Interval page no longer says "today is 7 November 2026" under a footer stamped
   2026-11-08.
2. The Unit 1 "any date before 2027-02-01" row no longer shows a **mailed** service deadline later
   than the **personal** one — an impossibility that a tenant's lawyer reviewing the arithmetic
   would have caught immediately.
3. `scripts/verify_calculations.py` now fails CI if any printed `<personal> / <mailed>` day count
   in that table disagrees with a date recomputed from `REVIEW_DATE`, and if the nav stamp
   disagrees with `REVIEW_DATE`. 48 → 61 assertions across the two additions.

**No legal conclusion, percentage or dollar figure changed.** The substantive analysis — 1.6%
current, Unit 1 at 3.0% → $4,114.85, Unit 2 at 13.1% → $3,562.65, and the 2026-11-30 closing
service deadline — was re-verified against primary official sources this session and confirmed
unchanged.

## Session `arena/9b0747eb-rentincreasesf2` — line-by-line re-verification and new-development check (2026-11-10)

This session arrived with `main` at `a91dc78` (PR #21 merge), all checks green (validator PASSED,
61 calculation assertions PASSED, Pages status `built`). Its job was to re-verify the live site
line by line against official sources, check for developments since the 2026-11-08 verification,
and close out the two stale open PRs.

### Official sources read directly this session

| Source | What was confirmed |
|---|---|
| [sf.gov — The Rent Board Housing Inventory](https://www.sf.gov/rent-board-housing-inventory) | All owners of residential property must report; tenant-occupied units receive a license; license must be current on the effective date; license need not be included with the notice; buildings with fewer than 10 units in scope since 2023-03-01; submissions are public and under penalty of perjury. Matches the site's license-first summary. |
| [sf.gov — Learn about rent increases](https://www.sf.gov/learn-about-rent-increases-san-francisco) | 1.6% effective 2026-03-01 through 2027-02-28; license required before imposing; 30-day / 90-day (>10%) notice +5 if mailed; base rent only; no rounding up; additional occupant may not be charged. Matches the site. **Also carries the 2026-11-09 File 261020 notice (see below).** |
| [sf.gov — Banked rent increases](https://www.sf.gov/information--banked-rent-increases) | Banking mechanics, partial increases, worked example 5.3% + 1.4% = 6.7% (Example A of the F-16 test). Summary-page 24-month language noted; the site's `banking-rule.html` resolution (Rules §4.12(a) per-allowance 12-month test) stands. **Also carries the File 261020 notice.** |
| [sf.gov — Form 571 Allowable Annual Increases 26-27 (PDF)](https://www.sf.gov/documents/34344/571_Allowable_Annual_Increases_26-27_1.pdf) | Full table read line by line. Unit 2 banked re-derived: 1.8% (2020–21) + 0.7% (2021–22) + 2.3% (2022–23) + 3.6% (2023–24) + 1.7% (2024–25) + 1.4% (2025–26) = **11.5%**; + 1.6% current = **13.1%**. Unit 1: 1.4% banked + 1.6% current = **3.0%**. All confirmed. |
| [sf.gov — Tenant Petitions](https://www.sf.gov/tenant-petitions) | No filing charge; unlawful-rent-increase claim and summary petition for invalid notice; Rent Board does not adjudicate harassment, discrimination or retaliation. Matches the site's tenant-protections page. |
| [Legistar — File 261020](https://sfgov.legistar.com/LegislationDetail.aspx?ID=8217304&GUID=7EDA4662-EBFB-4AF5-962F-C669B64AA770) | "Administrative Code — Cap On Rent Increases for Rent-Controlled Units"; introduced 2026-09-15; Land Use and Transportation Committee; status **Pending Committee Action**; no enactment date. **Not enacted.** |

### New development: File 261020 proposed 10% cap (flag F-27)

One day after the site's last full verification (2026-11-08), the Rent Board posted a notice
(2026-11-09) on both the rent-increases and banked-increases pages: Board of Supervisors
File No. 261020 would temporarily limit combined banked + capital improvement increases to
10% per year for three years, applying to banked increases noticed on or after 2026-09-15.
The site did not mention it (correctly — it did not exist at verification time). It is now
published as **flag F-27** on `flagged.html`, with notes on `analysis.html` and
`executive-summary.html`, a `sources.html` entry, and the Legistar URL added to the validator
allowlist. Under current law Unit 2's 13.1% remains lawful; if the ordinance were enacted as
proposed, the phased 10.0% option ($315.00 → $3,465.00) would be the lawful path. The global
"Last verified: 2026-11-08" stamps were deliberately left unchanged (the day-count assertions
are computed from `REVIEW_DATE` = 2026-11-08); F-27 is dated explicitly as verified 2026-11-10.

### Stale PRs closed

- **PR #16** (`arena/342c4cc9-rentincreasesf2`, base `a747d82`): CONFLICTING. Duplicates work
  merged in PRs #14/#15; its four verified findings were salvaged in PR #17 (see the
  post-merge corrections record above). Closed unmerged with an explanatory comment.
- **PR #20** (`arena/e8ef4a1a-rentincreasesf2`, "Record PR #19 merge and Pages deployment"):
  CONFLICTING after PRs #18/#21 merged. Its only content is a PR #19 deployment record whose
  text is not on `main`. Closed unmerged; the PR #19 record is summarised here instead:
  PR #19 merged 2026-11-08T22:56:33Z at `362b9e3`, `Validate site` success, Pages built on
  `362b9e3`; content was the PR #17 deployment record plus salvage of PR #18's unique items
  (47 → 56 assertions). No code was lost by closing either PR.

### Validation performed

- `python3 scripts/sync_nav.py` — NAV OK, 13 pages, 0 updated.
- `python3 scripts/validate_site.py` — PASSED (13 pages, 49 official-source URLs on allowlist
  including the Legistar URL, per-row source links, column integrity, privacy sweep over all
  root Markdown).
- `python3 scripts/verify_calculations.py` — PASSED (61 assertions; no figure changed).

**No legal conclusion, percentage or dollar figure changed.** The only site change is the
addition of flag F-27 and its cross-references. Flagged items F-01…F-27 remain for the owner
on the Flagged for Review page; none block publication.

**Not legal advice.** This is a documentary re-verification against official sources. A Rent
Board counselor cannot give legal advice, and no lawyer's approval can be guaranteed in advance.

## PR #22 — F-27 new-development flag, merge and deployment record

- **PR:** https://github.com/kanlerxz87-cyber/RentincreaseSF2/pull/22
- **Title:** "Add F-27: proposed 10% banked-increase cap (File 261020, pending); line-by-line re-verification"
- **Merged to `main`:** 2026-11-10T00:37:07Z, merge commit `d02bee89f1e737d57219316627f0f10e68bfcd5b`
- **Merge method:** merge commit (`gh pr merge 22 --merge`)
- **`mergeStateStatus` before merge:** `CLEAN` / `MERGEABLE`
- **Validation on the PR:** `validate` job **pass** (run 42729628081)
- **Validation post-merge:** `Validate site` **success** on `d02bee8` (run 42729675819)
- **GitHub Pages:** `pages build and deployment` **success** on `d02bee8` (run 42729674909);
  `pages/builds/latest` → status **built**, error `null`; `gh api …/pages` → status **built**.
- **Deployed-artifact verification:** `flagged.html` at `d02bee8` contains the F-27 row
  (grep count 1 for "F-27"). Live-URL fetch from the sandbox is not possible (outbound network
  is limited to github.com and package registries); deployment success is confirmed via the
  Actions and Pages APIs, the same method used in PRs #14/#17/#18.
- **Stale PRs closed by this session:** PR #16 and PR #20, both CONFLICTING and superseded,
  closed unmerged with explanatory comments (see session record above).
- **Task board:** tasks 27–29 done. Flagged items F-01…F-27 remain for the owner on the
  Flagged for Review page; none block publication.

## Session `arena/585ad53b-rentincreasesf2` — independent verification pass (2026-11-10)

**Position.** This session arrived as PR #24 merged (`3701b1c`) and PRs #22/#23 were already
recorded. While its reads were in progress, PR #25 (`arena/d2474b1d`, merge `e538d59`) also
landed on `main` — residual-integration wording corrections (banked-expiry wording, `units.html`
rows, new flag F-28, tightened F-27). This session's source reads and figure re-derivations are
unaffected by those wording changes (the controlling rates, percentages, deadlines and license
rules it re-derived are the same facts); its record below describes the tree as of `e538d59`.
It is an independent verification pass, not a content change: **file scope is
`COORDINATION.md` only, additive edits.** No site file was touched. This record is inserted
before `arena/d086cb8e`'s sections so the two sessions' appends do not overlap textually.

### Claim collision (logged per the standing conflict rule)

This session first wrote its claim as **task 30** at ~00:45 UTC and pushed it. The push's
`git pull --rebase` hit a conflict because `arena/d086cb8e` had claimed **tasks 30–33** at
00:38 UTC (PR #24, merged 00:39 UTC) — the A-07 kind of duplicate task number. Renumbering to
**task 34** and re-pushing hit a second conflict: `arena/d2474b1d` (PR #25, merged 00:41 UTC)
had by then claimed **tasks 34–36**. Resolution in both cases: their rows were kept
**verbatim**, this session's rows were renumbered to **task 37**, and no line of either
session's work was altered or discarded. The branch was force-pushed over this session's own
earlier pushes only.

### Official sources fetched and read directly (2026-11-10, ~00:38–00:50 UTC)

| Source | What it confirmed |
|---|---|
| [Legistar — File 261020](https://sfgov.legistar.com/LegislationDetail.aspx?ID=8217304&GUID=7EDA4662-EBFB-4AF5-962F-C669B64AA770) | Status **Pending Committee Action**; introduced 2026-09-15; Land Use and Transportation Committee; latest history entry 2026-10-07 (Youth Commission response received); **no enactment date, not enacted**. Matches flag F-27 exactly. |
| [sf.gov — Learn about rent increases](https://www.sf.gov/learn-about-rent-increases-san-francisco) | 1.6% effective 2026-03-01 through 2027-02-28; license required before imposing annual/banked increases (operative 2022-07-01, 2023-03-01 for condos and 1–9-unit buildings); 30-day / 90-day (>10%) written notice +5 days if mailed; calculate on base rent only; never round up; charging for an added roommate is an unlawful increase. Carries the 2026-11-09 File 261020 notice verbatim: if enacted as proposed it applies to banked increases **noticed on or after 2026-09-15**. |
| [sf.gov — Current Rates](https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit) | Allowable-increase table 1.6% (2026–27) / 1.4% (2025–26) / 1.7% (2024–25); the File 261020 notice; the 2027–28 percentage is still unpublished (nothing after 2027-02-28). |
| [sf.gov — Banked rent increases](https://www.sf.gov/information--banked-rent-increases) | 24-full-month banking sentence; banked percentages are added, **not compounded or prorated**; no cap on the banked amount; banked amounts do not carry to a new tenant; notice must state the banked portion; the 6.7% worked example; the File 261020 notice. |
| [Form 571 Allowable Annual Increases 26-27 (PDF)](https://www.sf.gov/documents/34344/571_Allowable_Annual_Increases_26-27_1.pdf) | Full historical table read line by line. Unit 2's banked component re-derived: 1.8 + 0.7 + 2.3 + 3.6 + 1.7 + 1.4 = **11.5%**; plus current 1.6% = **13.1%**. Unit 1: 1.4% banked (available 2027-02-01) + 1.6% = **3.0%**. |
| [sf.gov — Rent Board Housing Inventory](https://www.sf.gov/rent-board-housing-inventory) | All owners report; tenant-occupied units receive a rent increase license; license must be current **on the effective date**; March 1 annual deadline; no monetary penalty for late filing; submissions are public and under penalty of perjury. |
| [SF Dept. of Elections — Nov 3, 2026 Consolidated General Election results (official, preliminary)](https://www.sfelections.org/results/20261103/index.html) | **New diligence — no prior session checked the ballot.** Update of 2026-11-09 4:00 PM (≈1,800 ballots left; certification within 30 days). The complete San Francisco local measure list was read: **RTM** (regional transit sales tax), **A** (charter/departments), **B** (public bank), **C** (Housing Trust Fund), **D** (ballot-measure process), **E** (city administrator/contracting), **F** (executive-branch management), **G** (Upper Great Highway — failed), **H** (Muni parcel tax), **I** (transfer-tax dedication to affordable housing), **J** (removal of the foreclosure exemption from the transfer tax). **No measure concerns rent control, rent increases, or the Rent Ordinance.** The election therefore changes nothing in the legal framework this site analyzes; F-27's "monitor Legistar" guidance is unaffected by the ballot. |

### Figures re-derived independently (no site arithmetic reused)

- Unit 1: $3,995 × 1.6% = $63.92 → **$4,058.92**; on/after 2027-02-01: $3,995 × 3.0% = $119.85 → **$4,114.85**.
- Unit 2: $3,150 × 13.1% = $412.65 → **$3,562.65**; phased fallback under a hypothetical enacted cap: $3,150 × 10.0% = $315.00 → **$3,465.00**.
- Day counts re-derived from 2026-11-10: Unit 2's last service dates **2026-11-30** personal (20 days) and **2026-11-25** mailed (15 days). This independently confirms the re-stamp published by task 30 / PR #24 ("20 / 15" days, REVIEW_DATE = 2026-11-10).

### Validation performed on the post-PR-#24 tree

- `python3 scripts/sync_nav.py` — NAV OK, 13 pages, 0 updated.
- `python3 scripts/validate_site.py` — **PASSED** (13 pages, 49 official-source URLs, every table row sourced, column integrity, privacy sweep over HTML and all public Markdown).
- `python3 scripts/verify_calculations.py` — **PASSED** (61 assertions; REVIEW_DATE 2026-11-10 agrees with the `LAST_VERIFIED` stamp).

### Conclusion and noted items

- **No site change is required on this session's evidence.** Every published percentage, dollar figure, deadline and license rule re-derives from the official sources above; File 261020 remains unenacted; the Nov 3, 2026 ballot contained no rent measure.
- Noted (minor, left verbatim — not this session's scope): task 29's status cell still reads "in progress" although its owner's records show tasks 27–29 done (PRs #22/#23 merged, deployment confirmed). No published figure is affected.
- Flagged items F-01…F-27 remain for the owner on the Flagged for Review page; none block publication.
- **Not legal advice.** A Rent Board counselor cannot give legal advice, and no lawyer's approval can be guaranteed in advance.

## Session `arena/d086cb8e-rentincreasesf2` — claim (2026-11-10)

**Claimed at** 2026-11-10T00:38Z, immediately after PR #22 merged (`d02bee8`). **Tasks 30–33.**

**File scope (exclusive to this session until it closes):** `scripts/sync_nav.py`,
`scripts/verify_calculations.py`, `scripts/validate_site.py`, all 13 root `*.html` pages,
`COORDINATION.md`, `README.md`.

**Not in scope / not duplicated:** flag F-27 and the File 261020 analysis were published by
`arena/9b0747eb-rentincreasesf2` in PR #22 (merged `d02bee8`) minutes before this claim. This
session does **not** re-do that work; it integrates on top of it, corrects the citation target
(row 32) and performs the whole-site date re-stamp (row 30) that was outstanding on `main`
(every page still read "Last verified: 2026-11-08" and the arithmetic was anchored to that date).

**Why the re-stamp is not cosmetic:** the published site's most urgent number is a countdown.
`banking-rule.html` printed "22 / 17" days left to serve Unit 2's 13.1% notice; on 2026-11-10 the
correct counts are "20 / 15". A reader relying on a two-day-old countdown for a statutory
deadline would mis-plan the only irreversible step in this file. All such counts are recomputed
by `scripts/verify_calculations.py`, which fails if any printed cell disagrees with
`REVIEW_DATE`.

## Session `arena/d086cb8e-rentincreasesf2` — verification log (2026-11-10)

**Sequence.** PR #22 (session `arena/9b0747eb`) merged at 00:37:14Z as `d02bee8` while this session
was still reading sources. This session then rebased onto `d02bee8` and executed only the residual
work: tasks 30–33. Nothing in PR #22 was reverted, and this session did not re-do it.

### Primary official sources fetched and read directly this session

| Source | Read at | What it confirmed on the site |
|---|---|---|
| Form 571 Allowable Annual Increases 26-27 (PDF) | `sf.gov/documents/34344/571_...pdf` | Full historical rate table. **1.6 / 1.4 / 1.7 / 3.6 / 2.3 / 0.7 / 1.8 / 2.6** for 3/1/26 back to 3/1/19. The 0.7% for 3/1/21–2/28/22 is the row most often mis-stated; it confirms Unit 2's 11.5% (1.8+0.7+2.3+3.6+1.7+1.4). |
| Current Rates report | `sf.gov/reports--current-rates-...` | 1.6% current allowance; security deposit 4.2%; **the 2026-11-09 File 261020 notice**; the 2027-28 percentage is still unpublished (table ends 2027-02-28). |
| Rent Board Rules § 13.14 | `sfrb.org/section-1314-...` | Verbatim: unlicensed increase "null and void"; "effective date … not the date of service"; banking rights survive; <10-unit buildings from **2023-03-01**. |
| Housing Inventory | `sf.gov/rent-board-housing-inventory` | All owners must report; license auto-generated for tenant-occupied units; March 1 deadline; **no monetary penalty**; data is **public** and under **penalty of perjury**; $250 rent increments; 30-day contact updates; license need not accompany the notice. |
| Civ. Code § 827(b)(2),(b)(3)(A) | `leginfo.legislature.ca.gov` | 30 days ≤10%; 90 days >10%; personal delivery or CCP § 1013 mail. |
| AB 1482 report | `sf.gov/reports--california-tenant-protection-act-...` | 8.8% for SF 2026-08-01–2027-07-31 (5% + 3.8% CPI); states it "does NOT apply" to units under the SF Rent Ordinance. |
| Rent Ordinance § 37.3 | `sf.gov/information--sec-373-rent-limitations` | (a)(1) 60% of CPI, **7% cap**, license hook; (a)(2) banking on anniversary dates. |
| Banked rent increases | `sf.gov/information--banked-rent-increases` | The 24-full-month sentence the site quotes; "cannot be compounded or prorated"; no cap on banked amount; partial increases; the **6.7%** worked example. |
| Learn about rent increases (both chunks) | `sf.gov/learn-about-rent-increases-san-francisco` | 1.6%; 60% of Bay Area CPI; no rounding up; base rent only; additional-occupant charge unlawful; the **4.7%**, **8.2%** and **3.3%** worked examples — the 3.3% page text expressly says the 1.4% is "permanently lost", which is the R1 test the site relies on. |
| Annual rent increase for multiple years | `sf.gov/information--annual-rent-increase-multiple-years` | 8.2% example; no compounding; no rounding up; 30/35-day notice. |
| Increasing rents during irregular periods | `sf.gov/information--increasing-rents-during-irregular-periods` | 12–24-month and 24-month-plus methods; once every 12 months. |
| Algorithmic devices § 37.10C | `sf.gov/information--algorithmic-devices-...` | Effective **2024-10-14**; sale and use prohibited; per-unit and per-month violations; up to **$1,000** per violation; tenant and tenants'-organisation right of action. |
| Legistar File 261020 | `sfgov.legistar.com/LegislationDetail.aspx?ID=8217304` | **Pending Committee Action**; introduced 9/15/2026; Land Use and Transportation Committee; 10%/year for three years; no enactment date. |

### Result of this session's verification

**No published figure is wrong.** Every percentage, dollar amount and notice deadline on the site
was independently re-derived and matched the official source (see the table above; the arithmetic
is asserted by `scripts/verify_calculations.py`, 61 assertions).

Two defects found and fixed, both created by the calendar rather than by any earlier session:

1. **Every page was stamped 2026-11-08 and every countdown was anchored to that date.** On
   2026-11-10 the Unit 2 closing deadline is **20 days** away (15 by mail), not the 22/17 printed
   on `main`. All nine date-derived values were recomputed and the script's own expected literals
   updated so the two cannot drift apart again.
2. **`analysis.html` and `executive-summary.html` left a stale hand-typed sentence** — "the mailed
   route to the earliest reachable effective date (2027-02-06) closed on 2026-11-03". On 2026-11-10
   no route has closed yet; the sentence now states the earliest reachable date by each service
   method, which is true on any base date the reader picks up.

`index.html` gained the F-27 watch item (badge, callout, key-findings row) because the pending
10% cap is the one external event that could change the recommendation for Unit 2, and the landing
page is where the owner will look first.

### Checks run (all green)

- `python3 scripts/sync_nav.py` — NAV OK, 13 pages, 0 drift
- `python3 scripts/validate_site.py` — PASSED: 13 pages, 49 allowlisted official URLs, every table
  row carries a source link, column counts match headers, internal links resolve, privacy sweep over
  all root Markdown and HTML
- `python3 scripts/verify_calculations.py` — PASSED: 61 assertions, every computed value found in
  the published HTML
- Tag-balance parse of all 13 pages — OK
- Zero personal-identifier hits

**Not legal advice.** Documentary verification against official sources only. No lawyer's approval
can be guaranteed in advance, and the Rent Board cannot give legal advice.

## Session `arena/d2474b1d-rentincreasesf2` — race record and residual integration (2026-11-10)

**What happened.** This session claimed tasks 30–32 at 2026-11-10 and pushed the claim
(`1e88052`) before reading any source. It then did its own full live re-verification and drafted a
2026-11-10 re-stamp plus a new flag for the 2026-11-09 File 261020 notice. While it was doing that,
`main` moved twice:

| PR | Session | Landed | Overlap with this session's draft |
|---|---|---|---|
| [#22](https://github.com/kanlerxz87-cyber/RentincreaseSF2/pull/22) | `arena/9b0747eb` | `d02bee8` | Created flag **F-27** for File 261020 — the same finding this session had reached independently from the sf.gov notice and the Legistar record |
| [#24](https://github.com/kanlerxz87-cyber/RentincreaseSF2/pull/24) | `arena/d086cb8e` | `3701b1c` | Re-stamped all 13 pages from 2026-11-08 to **2026-11-10** and recomputed every countdown — the same correction this session had made in its own draft |

**Resolution (protocol: never force a divergent tree through).** The rebase conflicted in this file.
It was aborted, the branch was **reset to `3701b1c`**, and the merged tree was re-inspected for what
was *still* wrong. Only the residual differences were re-applied as new commits. Nothing from PRs
#22 or #24 was reverted; this session's duplicate re-stamp and duplicate F-27 draft were dropped, not
merged, because the merged versions already carry them. This session's earlier task numbering
(30–32) collided with the other sessions' rows; the residual work is therefore recorded as
**rows 34–36** above.

**Residual work that was still missing on `main` and is delivered here**

1. **C-01 — wrong reason for a right conclusion.** `checklist.html` (×2), `banking-rule.html` and
   `executive-summary.html` still asserted that banked amounts "may only be given at the time of an
   annual increase" and that "the banked 11.5% cannot be imposed on its own later". The Rent Board
   says the opposite: a properly banked increase "does not expire" and may be imposed on a future
   anniversary date or at another time when an increase is allowed. The real reason the window
   matters is that the **percentage charged is the one in effect on the effective date**, so the
   **13.1% total** cannot be reproduced after 2027-02-28 until the 2027–28 rate is announced.
   Rewritten in all four places; the deadline and every dollar figure are unchanged.
   A **forbidden-phrase assertion** in `scripts/verify_calculations.py` now fails the build if
   either sentence comes back.
2. **C-03 / C-04 — `units.html`.** The Unit 1 banking sentence is now measured correctly (12 months
   from availability under Rules § 4.12(a), which coincides with 24 months from the 2025-02-01
   move-in), and **April 1, 2026** is no longer described as a "proposed effective date" — it is the
   intake date for the unchanged $3,995 rent. Unit 2's row now names 2027-06-01 as the next
   reachable anniversary.
3. **F-28 — non-anniversary effective date.** § 37.3(a)(2) ties a banked amount to "the tenant's
   subsequent rent increase anniversary dates", while the suggested Unit 2 date (2027-02-15) is not
   the June 1 anniversary and the Rent Board's irregular-period guidance permits a non-anniversary
   date. Not resolved by this session: published as **F-28** with both texts, the conservative
   alternative and a clear-the-flag row.
4. **F-27 precision (additive only).** The cap in the Legistar title covers **banked +
   capital-improvement** increases; the annual allowance is not in that list. One paragraph was added
   stating the conditional **10% + 1.6% = 11.6% → $365.40 → $3,515.40** as arithmetic on a bill
   draft, not law, and asserting it by script. Nothing already published was removed.

**Verification (all green, run on the final tree)**

```
python3 scripts/sync_nav.py             # NAV OK — 13 pages, 0 drift
python3 scripts/validate_site.py        # PASSED — 13 pages, 49 allowlisted URLs,
                                        # per-row sources, column integrity, privacy sweep
python3 scripts/verify_calculations.py  # PASSED — 105 assertions (61 + 5 new + 39 guards)
```

Tag balance OK on all 13 pages; all 13 HTML pages, `style.css`, `README.md`, `AUDIT.md` and
`COORDINATION.md` return HTTP 200 from a local static server; zero personal-identifier hits in HTML
and in every root Markdown file. No tenant name, initial, address, contact detail or parcel number
is published anywhere; dates and dollar amounts are unchanged as supplied.

**Not claimed.** This session did not re-fetch Civ. Code §§ 1942.5, 1947.12, 1954.50, 1954.52,
HUD / 42 U.S.C. ch. 45, CRD, Rules § 4.10 / § 4.12, Form 538, the noncompliance page or the petition
pages; those keep their earlier verification dates on `sources.html`. The 14 sources it did read
live on 2026-11-10, and what each confirmed, are listed in the `AUDIT.md` addendum dated 2026-11-10.

## PR #24 — 2026-11-10 re-stamp, merge and deployment record (session `arena/d086cb8e-rentincreasesf2`)

- **PR:** https://github.com/kanlerxz87-cyber/RentincreaseSF2/pull/24
- **Title:** "Re-stamp the site to 2026-11-10 and re-derive every countdown; add the F-27 watch item to the dashboard"
- **Merged to `main`:** 2026-11-10T00:41Z, merge commit `3701b1c8a08405bb3b68a99e4bb38d869e9f0d7f`
- **Merge method:** merge commit (`gh pr merge 24 --merge`)
- **`mergeStateStatus` before merge:** `CLEAN` / `MERGEABLE`, `validate` job **SUCCESS**
- **Validation post-merge:** `Validate site` **success** on `3701b1c`;
  `pages build and deployment` **success** on `3701b1c`;
  `pages/builds/latest` → commit `3701b1c`, status **built**
- **Deployed-artifact check:** `index.html` read back from the deployed ref via the Contents API
  contains 3 occurrences of `261020` and the corrected 2027-02-08 sentence.
- **Live-page check (this session read the live site, not just the API):**
  `banking-rule.html` rendered "Today is **10 November 2026**", the day pairs `7 / 2`, `20 / 15`,
  `67 / 62`, `53 / 48`, `113 / 108`, and the row "**2027-02-08** — the earliest date a 90-day
  notice served today can reach"; `index.html` rendered the `Pending legislation (F-27)` badge,
  the File 261020 watch-item callout and its key-findings row.
  **Correction to the PR #22 record above:** that record says a live-URL fetch "is not possible"
  from this environment. It is not possible from the **shell** (outbound is restricted to
  github.com and package registries), but the agent's **web-fetch tool reaches both sf.gov and
  github.io**, so deployed pages can be, and now have been, read back directly. Future sessions
  should verify the deploy this way rather than relying on the Actions API alone.
- **CDN note:** the first live fetch of `index.html` after the build returned the *previous*
  deployment's HTML even though the deployed artifact was already correct. A cache-busted re-fetch
  (`index.html?v=3701b1c`) returned the new content. Treat a single stale live fetch immediately
  after a build as a caching artefact; re-check with a query string before treating it as a defect.

### Parallel-session race during this task (logged per the coordination rules)

`main` moved three times between this session's claim and its final merge: PR #22 (F-27, `d02bee8`)
merged at 00:37:07Z while this session was reading sources; its record commit PR #23 (`0f6347d`)
merged before this session could push; and PR #25 (`e538d59`, session `arena/d2474b1d`) merged
while this record's own pull request was waiting on CI, conflicting in this file a second time.
**Consequence for this record:** PR #25 corrected the reason given for the Unit 2 deadline (C-01)
and added F-28. Where this record and PR #25 describe the deadline, **PR #25's wording is the
current one** — the banked 11.5% does not expire, and the binding reason for the 2026-11-30 service
date is that the 13.1% total is priced at the rate in effect on the effective date. The deadline and
every dollar figure are the same under either explanation. `git pull --rebase` then hit a conflict **in this file only** —
both sides appended a section at the end of `COORDINATION.md`. Resolution: kept **both** sections
(PR #22's record first, this session's claim second); nothing from the other session was discarded
and no row it owned was edited. Each rebased branch was force-pushed with `--force-with-lease` to
the session's own branch only, re-validated, and merged; the second rebase (onto `e538d59`) kept
both sides of the conflict again, so no session's record was lost. GitHub reported `CONFLICTING`/`DIRTY` for
about 30 seconds after the force-push; a local `git merge-tree` against `origin/main` reported a
clean merge, and the PR status settled to `MERGEABLE` without any further action.

### Net effect on the published site

- Every page now stamped **2026-11-10**, and every countdown re-derived from that date.
- Unit 2's remaining service window is published as **20 days** (personal) / **15 days** (mailed).
- The landing dashboard carries the F-27 pending-legislation watch item with its Legistar source.
- No percentage, dollar figure or legal conclusion changed. F-01…F-27 stay open for the owner on
  the Flagged for Review page and none of them blocks publication.

**Not legal advice.** Documentary verification against official sources only.

## PR #30 — independent verification pass, merge and deployment record (session `arena/585ad53b`)

- **PR:** https://github.com/kanlerxz87-cyber/RentincreaseSF2/pull/30
- **Title:** "Independent verification pass (2026-11-10): election check, File 261020 re-verified, every figure re-derived — documentation only"
- **Content:** documentation only — this session's verification record (election check, File 261020 re-check, Form 571 / Current Rates / banked-increases / Housing Inventory re-reads, independent figure re-derivation, validator runs, dual claim-collision log). **No site file changed.**
- **Merged to `main`:** 2026-11-10, merge commit `8571294d51d5a1d30e2ef14b43d99538667ae572`
- **Merge method:** merge commit (`gh pr merge 30 --merge`)
- **Check on the PR:** `Validate site` **passed** (run 42730463669)
- **GitHub Pages:** `pages build and deployment` completed; `pages/builds/latest` → status **built** on `8571294`
- **Live verification:** `https://kanlerxz87-cyber.github.io/RentincreaseSF2/index.html` fetched after deployment — dashboard serving with the license-first answer, the Unit 2 service-window deadline (2026-11-30 personal / 2026-11-25 mailed), sourced key-findings table, and privacy notices intact.
- **Task 37:** done. Flagged items F-01…F-28 remain for the owner on the Flagged for Review page; none block publication.
- **Standing observation for future sessions:** task numbers 30 and 34 were each claimed by two sessions within minutes on 2026-11-10 (both resolved without loss; this session renumbered to 37). Consider claiming by appending a row and pushing **before** starting any reads, and re-checking `origin/main` immediately before writing the row.

**Not legal advice.** Documentary verification against official sources only.
## Session `arena/817d1de7-rentincreasesf2` — residual final integration (2026-11-10)

This session independently found File 261020 and the date-sensitive changes, then discovered that
PRs #22–#26 had integrated equivalent and more precise work concurrently. Its duplicate working
changes were not merged. The branch was aligned to the integrated `main` without reverting any
other session's work. PR #25's 105 assertions and PR #26's validation/deployment record were
independently reviewed before their already-completed merges were observed.

**Residual tasks 40–42** (renumbered after another session used 37): add the direct official File 261020 draft text as a primary citation;
run the complete integrated validation; open/merge the PR and verify Pages. No legal conclusion,
rate, dollar amount or deadline is changed by this residual source-hardening work.


## PR #28 — residual final integration and deployment (2026-11-10)

- **PR:** https://github.com/kanlerxz87-cyber/RentincreaseSF2/pull/28
- **Merged:** 2026-11-10T00:45:31Z; merge commit `3a284cd9987b2ecc5391c3c73d52351acc36e880`.
- **Parallel-session resolution:** the first branch conflicted after concurrent PRs #22–#25. This session preserved all concurrent work, including C-01 bank-expiry corrections and F-28 non-anniversary review, and applied only residual verified changes. Task rows were renumbered 38–40 to avoid another collision.
- **Checks:** PR `Validate site` run 42730684702 passed; post-merge run 42730739904 passed on `3a284cd`. Site validator: 13 pages, 49 official URLs, per-row source links, columns, internal links and privacy. Calculation/regression suite: **109 assertions passed**. HTML tag balance, local HTTP 200 and `git diff --check` passed before merge.
- **Pages:** run 42730738839 succeeded; Pages API latest build `3a284cd`, status `built`, error `null`, completed 2026-11-10T00:46:01Z.
- **Live verification:** executive summary, banking-rule and tenant-protections fetched from the public Pages URL. Cache-busted banking-rule fetch confirms “current annual 1.6% component,” “not separately banked,” and File 261020 pending warning. Tenant resources now match official SF.gov wording.
- **Flags:** F-29 and F-30 corrected and published; F-27 pending legislation and F-28 non-anniversary counselor review remain visible. Other unverified owner inputs do not block deployment.
## PR #32 — residual final integration, merge and deployment record

- **PR:** https://github.com/kanlerxz87-cyber/RentincreaseSF2/pull/32
- **Title:** "Final integration: cite official pending ordinance text"
- **Merged to `main`:** 2026-11-10T00:46:58Z; merge commit `b654142ef8d37ddd45fb1f771b98bef93013716b`.
- **PR validation:** `Validate site` passed, run 42730877094.
- **Post-merge validation:** `Validate site` passed on `b654142`, run 42730922803.
- **GitHub Pages:** `pages-build-deployment` succeeded on `b654142`, run 42730921592; `pages/builds/latest` reports **built**, commit `b654142`, error `null`.
- **Live verification:** `sources.html` fetched from the public GitHub Pages URL and confirmed to show the new direct **File No. 261020 — official draft ordinance, version 1** row and the proposed § 37.3(h) details. `executive-summary.html` and `flagged.html` were also fetched successfully; the license-first process, current-date flags, and anonymized content remain live.
- **Content:** direct primary-source draft citation in `flagged.html`, `sources.html`, and `README.md`; official-source allowlist expanded to 50 URLs; verification record. No legal conclusion, rate, dollar amount or deadline changed.
- **Parallel-session resolution:** duplicate F-27/date work was aligned to `main` rather than merged. Two append-only `COORDINATION.md` rebase conflicts were resolved by preserving both sessions' sections and renumbering residual tasks to 40–42. No other session's work was discarded.
- **Task 42:** done. F-01…F-28 remain published for review; none blocks deployment.

## Session `arena/0e02b0ec-rentincreasesf2` — independent deployment and core-rule check

- Status: **in progress**. Scope: additive `COORDINATION.md` entries only. This session will check the existing integrated site, core official rules, automated tests, and current deployment; it will not edit files claimed by another session. Any needed site changes will be logged as requests. Branch name is fixed by the session environment.

### Review result and request — 2026-11-10

- **Status: needs review.** Core-source spot check only, not an independent line-by-line re-verification: the [Housing Inventory](https://www.sf.gov/rent-board-housing-inventory) confirms all residential owners report, the automatically generated license must be current when an annual or banked increase takes effect, and the annual March 1 deadline. The [Rent Board increase guidance](https://www.sf.gov/learn-about-rent-increases-san-francisco) confirms 1.6% through February 2027, the written notice periods, and pending File 261020. The published executive summary contains the license-first answer.
- Site validator passed 13 pages, local links and privacy checks; calculation suite passed 122 assertions; navigation was in sync. These tests do not independently prove that every external link is reachable or every legal conclusion is correct.
- Latest Pages build at the time of checking was **built** on `d17a5a0834f57deeb5c53c3515c026b533e7de27`; the public executive summary was fetched successfully.
- **Request to site owner:** the executive summary says “Your building is in scope” and “A two-unit building falls in that second group.” The intake identifies two units but does not independently establish the total number of residential units in the building or all coverage exceptions. Please qualify these as conditional and flag the building unit count and coverage for verification. In the summary table, “Lawful total on that date” should likewise be explicitly conditional on unverified tenancy, rent history, license status and future legislation. Do not treat a source about a calculation method as verification of owner-provided facts. Relevant sources: [Housing Inventory](https://www.sf.gov/rent-board-housing-inventory), [Rent Board increase guidance](https://www.sf.gov/learn-about-rent-increases-san-francisco).
- Existing uncertainty remains on the [Flagged for Review page](https://kanlerxz87-cyber.github.io/RentincreaseSF2/flagged.html); this review does not guarantee attorney approval or immunity from challenge.

## Session `arena/69f0c0e5-rentincreasesf2` — claim (2026-11-10T05:45Z)

- **Status: in progress.** Tasks `69f0-A` (verification, read-only on site files), `69f0-B` (integration of findings) and `69f0-C` (stale-PR triage, PR, merge, deploy check). Rows are on the task board above.
- **Why session-prefixed task IDs.** Plain numbers have been claimed twice by simultaneous sessions at least six times on this board (13–15, 24, 30, 34, 37 and 40 — the A-07 pattern). A session-prefixed ID cannot collide, so no renumbering or force-push is needed when two sessions claim in the same minute. Suggested convention for later sessions: `<first four characters of the session id>-<letter>`.
- **Branch name.** The protocol asks for `session-<id>/<task>`. This session's branch, `arena/69f0c0e5-rentincreasesf2`, is assigned by the platform and cannot be renamed or switched — the same constraint every earlier session recorded. All work is committed to that one branch and the pull request is opened from it.
- **Not displaced.** No task on the board is `in progress` under a live claim: rows 29, 36 and 45 still read *in progress*, but their pull requests (#22/#23, #25, #35) are merged and their branches have had no commit since 2026-11-10T00:51Z. `arena/0e02b0ec` finished at 05:42Z with status *needs review* and an explicit request to the site owner; that request is what task `69f0-B` picks up. Those rows are left verbatim.
- **Privacy rule acknowledged.** This file is served publicly by GitHub Pages. Nothing but placeholders (Tenant A–F), dates and dollar amounts will be written here or on any page.
