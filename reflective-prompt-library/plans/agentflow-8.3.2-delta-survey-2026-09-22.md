# Agentflow 8.3.2 — Delta Survey — 2026-09-22

> **Status: decided — record-only; no installed change, no wording adopted.** A
> delta from the [8.3.0 survey](agentflow-8.3-delta-survey-2026-09-21.md) (itself a
> delta from [8.2.0](agentflow-8.2-delta-survey-2026-09-13.md) and the
> [2026-09-05 survey](agentflow-survey-2026-09-05.md)). The instruction is a **bare
> "survey"** → no adoption direction under DS-1. 8.3.0 → 8.3.2 is **4 commits, two
> patch releases (8.3.1 + 8.3.2), all host implementation**: one manual-compaction
> flag (`--include-answered true`) and two stream fixes (first-activation ownership
> claim; preserve-before-destroy cleanup recovery). **No schema change** (still 8),
> no new methodology, no new concept — every change refines an already-recorded
> host candidate (AF83-5 session ownership, AF83-8 compaction, AF83-10 cleanup
> safety), all `Record-only (host)` under the Standing Non-Goal. Method per the 8.2
> reflection: coordinator-owned top-level diff, no panel, no probing. Guard:
> `plans/tests/test_agentflow_v832_delta_record.py`.

## Research Question and Scope

User instruction: "Survey agfnow/agentflow 8.3.2" (checked 2026-09-22). Does anything
since the 8.3.0 pin alter the methodology or expose a **verified gap** on an installed
TeaPrompt surface, or is it host implementation? A bare survey carries no adoption
direction; the standing bar per candidate is a verified local gap, a named failure, a
smaller alternative rejected, and a guard. Scope: pin the current source; separate new
material from prior coverage; preserve every prior gate and adopted sentence; land
nothing.

## Direct Recommendation (as of 2026-09-22)

- **Study — minor.** The only mildly notable pattern is the 8.3.1 stream-cleanup fix:
  before Git removes a worktree it copies recognized local records / hook files /
  Finder metadata byte-for-byte into a **private recovery directory**, stops on unknown
  files / active ownership / changes during cleanup, and retains the recovery copy even
  if removal later fails. That is a clean **preserve-before-destroy / fail-closed
  reversibility** instance — the `reflective-risk` "rollback ≠ no-harm" and
  `governed-delivery` fail-closed disciplines, executed in host code.
- **Reproduce — not done.** Bare survey → nothing drafted → nothing probed; no CLI run.
  Every behavior is source-tier at the pin.
- **Adopt — nothing.** DS-1 record-only. Three delta items are all host runtime that
  refine already-recorded AF83-* host candidates (Standing Non-Goal); none is a
  methodology change and none exposes a local gap.
- **For citers:** GitHub tags/Releases still **empty** (`[]`); "8.3.2" is a file label,
  not a git tag; the release is a chain of squashed commits whose source builds
  (`f8f001f`, `d5190de`, …) are uninspected. **Config schema unchanged at 8.** License
  unchanged (Apache-2.0). Nothing executed.

## Version and Source Identity

Checked 2026-09-22:

| Identity | Observation | Tracking point |
| --- | --- | --- |
| Previous pin (8.3.0) | `0abf416ccfe10016f16893239bf6c9fd9d4d71e9` (2026-09-21) | 8.3.0 survey bound to this pin |
| Current `main` (8.3.2) | `6d699038ea14bf246c7bfaaef1ea4348a467d639`, tree `697b93dc832041fcf2a7b287ca0de69de551aded`, 2026-09-22T08:27:50Z ("docs: mark 8.3.2 changelog as released"); **ahead_by 4** of the 8.3.0 pin | Recheck `main` before any later reliance |
| Release span | 8.3.1 (Fixed) + 8.3.2 (Added) across 4 squashed commits | Two patch releases in one delta |
| Release label | `8.3.2` in `plugin.json`, `README`, `SKILL.md` | Label, not a git tag |
| Configuration schema | **8 — unchanged** (no schema bump in 8.3.1/8.3.2) | Separate from the release version |
| GitHub tags / Releases | Both **empty** (`[]`) at the pin | No independently published tag |
| License | Apache-2.0, unchanged | Concepts restated in original prose |
| Delta size | ~14 files, dominated by new host scripts (`stream-cleanup.js` +95, `terminal.test.js` +70, `notebook-owner-first-stream.test.js` +89) | Host implementation |

Primary sources (2026-09-22): [HEAD commit](https://api.github.com/repos/agfnow/agentflow/commits/main), [8.3.0→8.3.2 compare](https://api.github.com/repos/agfnow/agentflow/compare/0abf416ccfe10016f16893239bf6c9fd9d4d71e9...main), [tags](https://api.github.com/repos/agfnow/agentflow/tags), and `docs/CHANGELOG.md` + the `SKILL.md`/`references/streams.md` patches read in full.

## State Ledger and Changed Mechanisms

All entries are source-tier at the pin; the methodology-surface changes are in
`SKILL.md` (version label + a compaction-flag usage line + the first-activation
ownership sentence) and `references/streams.md` (the first-activation and cleanup
rules); everything else is host scripts and their tests.

| Change (8.3.1 / 8.3.2) | Evidence at the pin | Status / limit | TeaPrompt disposition |
| --- | --- | --- | --- |
| **`--include-answered true`** manual notebook compaction: archive completed rounds containing filled-in answers, byte-preserving; automatic compaction still retains answered rounds; the current open round stays live | CHANGELOG 8.3.2; `SKILL.md` compact usage; `notebook-compact.js` (+9/−6) | Verified source delta; host compaction flag | Refines **AF83-8** (compaction / evidence preservation, already `Record-only (host)`); no methodology change (AF832-1) |
| **Stream first-activation ownership claim**: explicit first activation may claim a newly-created stream after its first Ask is filled, using the **committed empty notebook as proof**, while preserving session-ownership protections; other unowned populated notebooks still require adoption | CHANGELOG 8.3.1; `SKILL.md` startup §; `streams.md` (+6); `notebook-owner.js` (+20/−2) | Verified source delta; runtime concurrency/ownership | Refines **AF83-5** (session-ownership lease model, already `Record-only (host)`) (AF832-2) |
| **Stream cleanup preserve-before-destroy**: copy recognized local records / hook files / Finder metadata byte-for-byte into a private `agentflow-cleanup/<taskkey>-<unique>/` recovery directory before removing the worktree; stop on unknown files, active ownership, or changes during cleanup; recovery copy retained even if removal fails, never overwritten | CHANGELOG 8.3.1; `streams.md`; new `stream-cleanup.js` (+95) | Verified source delta; host fail-closed cleanup | Refines **AF83-10** (cleanup fail-closed, already `Record-only (host)`); corroborates `reflective-risk` rollback≠no-harm (AF832-3) |

## Candidate Adoption Ledger

All rows decided under a **bare survey** (no adoption direction); none installed. IDs
continue the lineage as AF832-*.

| ID | Candidate | Status | Evidence | Reopen trigger |
| --- | --- | --- | --- | --- |
| AF832-1 | `--include-answered true` compaction flag | No change (host) | Refines AF83-8; TeaPrompt runs no compaction engine; no methodology change | A local dropped-evidence case, not an upstream flag |
| AF832-2 | Stream first-activation ownership claim (committed-empty-notebook proof) | No change (host) | Refines AF83-5 lease/ownership model; runtime concurrency is a Standing Non-Goal | A user directs lease/ownership scaffolding for a stateful agent (→ `agent-governance-scaffold` lease semantics, gated) |
| AF832-3 | Stream-cleanup preserve-before-destroy recovery | No change (host) | Refines AF83-10; corroborates `reflective-risk` rollback≠no-harm + `governed-delivery` fail-closed; host mechanics | A local irreversible-cleanup gap on an emitted governance scaffold |

Recurrence is `unknown`; two squashed patch releases are not local recurrence. Old
AF/EP/AF82/AF83 ledger rows, dates, pins, and adopted sentences are intentionally
unchanged; the 8.3.1/8.3.2 text contradicts none of them.

## Evidence vs Inference

- **Observed:** API identities (HEAD `6d699038`, tree, `ahead_by 4`, empty tags); the
  `docs/CHANGELOG.md` 8.3.1/8.3.2 sections and the `SKILL.md`/`streams.md` patches; the
  changed-file inventory and per-file line counts.
- **Author-claimed:** every runtime behavior (compaction flag, first-activation claim,
  cleanup recovery). Reading source or its tests does not verify them.
- **[INFERENCE]:** that the delta is "host-only" — from the changed-file families
  (scripts + one flag + two stream rules) and the absence of any new
  methodology/concept/schema text.
- **Unknown / not done:** recurrence; the private source builds; any CLI run; whether
  the shipped tests pass at this pin.

## Evidence Actually Checked

- GitHub API 2026-09-22: `commits/main`, `compare/0abf416...main` (4 commits), `tags`.
- Read in full: `docs/CHANGELOG.md` (8.3.1 + 8.3.2 sections) and the `SKILL.md` +
  `references/streams.md` patches; changed-file inventory enumerated.
- Installed-surface grep 2026-09-22: agentflow vocabulary absent from every skill and
  category surface (clean-room boundary holds).
- Not done: no CLI execution; the host script bodies beyond the two doc patches; the
  private build revisions.

## Falsifiability

- Wrong if the pin, `ahead_by 4`, empty-tags, or "schema unchanged at 8" facts are
  misread — all from the API/CHANGELOG at `6d699038`.
- Wrong if any 8.3.1/8.3.2 change is a methodology delta rather than a host refinement
  of AF83-5/8/10 — the two doc patches are quoted.
- A patch release is not local recurrence; only an explicit skill-update direction
  re-runs these rows at the "would the skill be better" bar, and even then only a
  verified local gap lands anything (none exists here).

## Completion Ledger

| Item | Status | Evidence |
| --- | --- | --- |
| Current pin, ahead_by, empty tags, schema-unchanged recorded | done | Version and Source Identity |
| 8.3.0→8.3.2 compare read; three host changes separated | done | State Ledger and Changed Mechanisms |
| Three delta items decided with evidence and triggers | done | Candidate Adoption Ledger |
| Bare-survey direction-scope rule applied: nothing installed | done | Status; Research Question |
| Clean-room boundary on installed surfaces | done | guard vocabulary test |
| Guard written | done | `plans/tests/test_agentflow_v832_delta_record.py` |
| Decision Index row (at head), case-studies row, `index.json` | done | `PROJECT_KNOWLEDGE.md`; `external-adoption-case-studies-2026-06-20.md` |
| Full repository gate | done | `make all` from the repository root |
