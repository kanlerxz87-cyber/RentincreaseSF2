# COORDINATION — shared task board

Multiple agent sessions may work on this repo. Read this file before starting work.
Claim a task by writing your session ID and file scope, then commit and push the claim immediately.
Never start a task another session has claimed. Keep scopes non-overlapping.

Session naming convention: `session-<id>` working on branch `session-<id>/<task>`.
This session (the integration session for this run) works on branch
`arena/77623c60-rentincreasesf2` because that branch is fixed by the harness.

---

## Sessions

| Session ID | Branch | Started (UTC) | Status |
| --- | --- | --- | --- |
| `session-77623c60` | `arena/77623c60-rentincreasesf2` | 2026-11-06 | active |

---

## Task board

Legend: `unclaimed` · `in progress` · `done` · `needs review`

| ID | Task | Status | Owner | File scope |
| --- | --- | --- | --- | --- |
| T1 | Local law research: SF Rent Ordinance Ch. 37, Rent Board Rules, AGA history | done | session-77623c60 | research only (recorded in `sources.html`, `data/aga-history.csv`) |
| T2 | California law research: AB 1482, Civ. Code 827 / 1942.5 / 1954.53 / 51, Gov. Code 12955 | done | session-77623c60 | research only (`laws.html`) |
| T3 | Federal law research: Fair Housing Act 42 U.S.C. 3604, HUD | done | session-77623c60 | research only (`laws.html`) |
| T4 | Unit-by-unit entitlement analysis and rent-increase arithmetic | in progress | session-77623c60 | `units.html`, `calculations.html`, `data/unit-analysis.csv` |
| T5 | Fair-housing / uniform-policy analysis ("raise one unit or both") | in progress | session-77623c60 | `fair-housing.html` |
| T6 | Institutional vs. individual owner practices (official sources only) | in progress | session-77623c60 | `practices.html` |
| T7 | Notice requirements, draft notice language, defensible reasons | in progress | session-77623c60 | `notices.html` |
| T8 | Tenant-lawyer review simulation and risk register | in progress | session-77623c60 | `review.html` |
| T9 | Static site build (landing dashboard + subpages + data files) | in progress | session-77623c60 | `index.html`, `assets/*`, `data/*`, `_config`-free static output |
| T10 | Line-by-line verification pass; every row must carry an official source link | unclaimed | — | read-only + `flagged.html` |
| T11 | Integration: re-verify combined data, check for broken links, merge, publish | unclaimed | — | `main` branch, `flagged.html`, `sources.html` |
| T12 | Pull request to `main`, merge, confirm GitHub Pages deploy | unclaimed | — | repo settings + `COORDINATION.md` |

---

## Claim log

| UTC timestamp | Session | Action |
| --- | --- | --- |
| 2026-11-06 | session-77623c60 | Board created. Claimed T1–T9 (single-session run, no competing claims found). T10–T12 left `unclaimed` for the closing verification pass of the same session so the record shows the hand-off. |
| 2026-11-06 | session-77623c60 | T1, T2, T3 closed as `done`. Sources recorded in `sources.html`; AGA history transcribed verbatim from SF Rent Board Form 571 (26-27). |

---

## Handoff / takeover rule

If a session crashes or its claim is more than 60 minutes old with no commits, any other
session may take over the task and must note the handoff in the claim log above.

---

## Notes for the next session

- Do **not** edit `data/aga-history.csv` values. They are a verbatim transcription of
  SF Rent Board Form 571 (`571_Allowable_Annual_Increases_26-27_1.pdf`). Re-verify, do not rewrite.
- The repo has **no build step** by design. GitHub Pages serves `main` / root (`build_type: legacy`).
  Keep it static HTML/CSS so deploys cannot break.
- Personal information policy: placeholder names only. Dates and dollar amounts are preserved
  exactly as supplied. See `flagged.html` → "Privacy handling".
