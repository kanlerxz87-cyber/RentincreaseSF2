# Repository Review

**Repository:** `kanlerxz87-cyber/RentincreaseSF2`
**Reviewed by:** session `arena-48ffb5b4`
**Reviewed:** 2026-11-06
**Base commit:** `3ed3b190ac09077c13588b9ce6771f7c877c7df2` ("Initial commit")

---

## 1. What the repository contained

A line-by-line audit of the working tree at the base commit.

```
$ find . -type f -not -path './.git/*'
./README.md

$ find . -type f -not -path './.git/*' | wc -l
1
```

| Path | Size | Content | Assessment |
|---|---|---|---|
| `README.md` | 17 bytes | `# RentincreaseSF2` — one line, **no trailing newline** | Placeholder. No project description, no data, no findings, no licence, no contact. |

That is the entire repository. **There was no prior data, no prior analysis, no prior
site and no prior `COORDINATION.md`.**

### Git history

```
$ git log --oneline
3ed3b19 Initial commit
```

One commit, no branches other than `main`, no tags, no releases, no open issues or pull
requests.

### Irregularity R-01 — missing trailing newline

`README.md` did not end in a newline, so `cat README.md && echo` concatenated into
`# RentincreaseSF2---REMOTE---`. Cosmetic, but it is the kind of thing that silently
corrupts shell pipelines and diffs. Fixed in this work.

---

## 2. Repository configuration

| Setting | Observed value | Source |
|---|---|---|
| Default branch | `main` | `gh repo view --json defaultBranchRef` |
| Visibility | **public** | `gh repo view --json isPrivate` → `false` |
| Is empty | `false` | `gh repo view --json isEmpty` |
| Fork | no | `gh repo view --json isFork` |
| GitHub Pages | **already enabled**, `build_type: legacy`, `source: {branch: main, path: /}` | `gh api repos/…/pages` |
| Pages URL | `https://kanlerxz87-cyber.github.io/RentincreaseSF2/` | same |
| HTTPS enforced | `true` | same |
| CNAME | none | same |
| Custom 404 | `false` | same |
| Git identity | `kanlerxz87-cyber <312694378+kanlerxz87-cyber@users.noreply.github.com>` | `.git/config` |
| Auth | `gh` authenticated as `kanlerxz87-cyber` via `GH_TOKEN`, HTTPS | `gh auth status` |

### Irregularity R-02 — HIGH: Pages was enabled against an empty repository

GitHub Pages was configured to publish the **root of `main`** with the **legacy Jekyll
build**, but `main` contained only a 17-byte `README.md`. There was no `index.html` and
no Jekyll front matter anywhere.

Consequences:

- The published URL served no usable content before this work.
- With `build_type: legacy` and no `.nojekyll`, Jekyll would process every committed
  Markdown file into HTML and apply its default layout, which is not what a hand-built
  dashboard site wants, and Jekyll also **excludes** a list of filenames and any file
  beginning with `_` from the published output.

**Resolution applied:** a `.nojekyll` file was added at the repository root so Pages
serves the static site verbatim, and a real `index.html` plus category subpages were
built. Pages remains on `main` / root, which is correct.

### Irregularity R-03 — no `.gitignore`

Nothing excluded `node_modules`, build output, editor files or OS cruft. Since this
site is dependency-free static HTML/CSS/JS with no build step requiring packages, the
risk is low, but a `.gitignore` was added to prevent accidental commits of local
scratch files — including any file an owner might create holding real tenant names.
`*.local.md`, `internal/`, `pii/` and `.pii-guard.local.json` are excluded for exactly
that reason.

### Irregularity R-04 — no LICENSE

The repository is public with no licence. Legally that means **all rights reserved**:
nobody may copy or redistribute the content. If open reuse is intended, a licence must
be added. Recorded, not silently fixed — choosing a licence is the owner's decision.

### Irregularity R-05 — public repository holding a rent-increase workpaper

Worth stating plainly rather than burying. This repository is **public** and its subject
matter is a specific two-unit rent-controlled building. Even fully anonymized, a
sufficiently determined reader could combine the ZIP code, the 1940 construction year,
the two-unit size and the exact base rents ($3,995 and $3,150) with other public
records to try to identify the property.

The base rents are **not** withheld because the owner expressly required dates and
amounts to be preserved, and because they are the entire basis of the analysis. But the
owner should understand the residual re-identification risk of a public site. Two
mitigations are available and were **not** applied unilaterally:

1. Make the repository private and use a private Pages deployment (requires GitHub Pro).
2. Round the rents to the nearest $50 on the public site while keeping exact figures in
   the internal working copy.

See Flag **F-23** on the Flagged for Review page.

### Observation R-06 — the remote fetch refspec is narrowed

`.git/config` contains two fetch refspecs, one for `main` and one restricted to
`arena/48ffb5b4-rentincreasesf2*`. This is normal for a platform-managed working
branch, but it means a bare `git fetch` will not surface *other* sessions' branches.
Any session checking for a competing claim must run
`git fetch origin '+refs/heads/*:refs/remotes/origin/*'` explicitly. Recorded so a
future session does not wrongly conclude it is alone.

---

## 3. Coordination check performed before claiming work

Per the parallel-session protocol, the repository was checked for an existing board and
for competing claims **before** any file was created.

| Check | Command | Result |
|---|---|---|
| Does `COORDINATION.md` exist? | `find . -type f -not -path './.git/*'` | **No** — only `README.md` present |
| Any remote branches claimed by others? | `git branch -a` | Only `main` and this session's branch |
| Any commits by another session? | `git log --oneline` | Single "Initial commit" |
| Any open PRs? | `gh pr list` | None |

**Conclusion:** no other session had claimed any task. `COORDINATION.md` was created,
all 19 tasks were claimed by session `arena-48ffb5b4`, and the claim was committed and
pushed immediately (`9c6813b`) before any substantive work began. This session is
therefore also the **final integration session**.

The first push produced:

```
fatal: couldn't find remote ref arena/48ffb5b4-rentincreasesf2
```

That is `git pull --rebase` failing because the branch did not yet exist on the remote.
The push itself succeeded. Informational only — recorded as Flag **F-20** context and in
the `COORDINATION.md` conflict log so a later session does not mistake it for a problem.

---

## 4. Verification method used for all new content

Because there was no prior content to audit, "verify line by line" was applied to the
**newly sourced material**. The method:

1. **Official sources only.** `.gov` domains, the California Legislative Information
   service (`leginfo.legislature.ca.gov`), the SF Rent Board (`sfrb.org`), the SF Board
   of Supervisors (`sfbos.org`) and the U.S. Census Bureau API. 40 sources are
   registered in `data/sources.json`.
2. **Third-party material used only to *locate* official documents.** Legal blogs,
   property-management vendors and news aggregators were read to find the right
   ordinance section or form number, then the official document was fetched and cited.
   No value anywhere on this site comes from a non-official source.
3. **Every table row carries a source link.** Enforced by construction: the site is
   generated by `build.py` directly from the JSON data files, and the generator emits a
   source cell for each row. A row without a source is rendered as `UNVERIFIED`.
4. **Blank rather than inferred.** Where a value could not be confirmed, it is left
   empty and recorded in `data/flags.json` — 22 flags, 7 of them HIGH severity.
5. **Primary text over summaries.** Statutory rules are taken from the section text on
   `leginfo`, not from a description of the section. Where only a description was
   available (the § 37.10B harassment penalties), the row is marked `verified: false`.
6. **Machine-computed arithmetic.** Every dollar figure and every notice deadline is
   computed by `build.py` from the official percentages, never typed by hand. The
   Census bracket counts are sum-checked against the published totals and the build
   fails if they do not reconcile.
7. **Internal cross-checking of official sources.** Comparing SF.gov pages against each
   other, against the Rent Board Rules, and against the codified ordinance is what
   surfaced the three genuine conflicts recorded as Flags F-03, F-11, F-12 and the two
   official-page defects F-13 and F-14.

---

## 5. Summary of irregularities

| ID | Severity | Finding | Where recorded |
|---|---|---|---|
| R-01 | cosmetic | `README.md` had no trailing newline | This document; fixed |
| R-02 | **HIGH** | GitHub Pages enabled against an empty repo with legacy Jekyll build and no `.nojekyll` | This document; fixed |
| R-03 | low | No `.gitignore` | This document; fixed |
| R-04 | medium | No LICENSE on a public repository | Owner decision required |
| R-05 | medium | Public repo + exact rents = residual re-identification risk | Flag F-23 |
| R-06 | informational | Narrowed fetch refspec hides other sessions' branches | This document |

Separately, 22 irregularities found **in the official sources themselves** are recorded
in `data/flags.json` and published on the Flagged for Review page. The most significant
is **F-03**: two official sf.gov pages state different minimum periods before a skipped
increase banks (24 months versus 12 months), and one of them contradicts its own worked
example. That conflict materially affects Unit 2 and must be resolved with a Rent Board
counselor before any notice is served.
