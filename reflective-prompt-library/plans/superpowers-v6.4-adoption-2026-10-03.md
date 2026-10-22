# Superpowers v6.4.2 Adoption Record — 2026-10-03

> **Status: implemented — verified within the recorded fixture scope.** User direction: "Survey https://github.com/obra/superpowers (updated recently)" (accessed 2026-10-03). Continuing the selective adoption pattern: two narrowed contracts land on existing core skills; no new skill, domain pack, helper, route, runtime, or install-time behavior. Supersedes the earlier high-level pass in `plans/skills-and-spec-systems-research-2026-06-25.md`, which covered Superpowers only at category level before the current release line.

> **Refresh 2026-10-22:** upstream moved v6.4.2 → v7.0.1; adopted SP-1/SP-2 surfaces verified byte-identical — see `## Latest-version refresh — 2026-10-22` below. Policy unchanged.

## Source Identity

- Upstream: `obra/superpowers`, MIT license, default branch `main`.
- Pinned ref: tag `v6.4.2` → commit `8ca22dba9a94f28898bce59f2537ff4d87c747d7` (`main` head at fetch time; `git ls-remote` tag peel `668b16d4d8d603f2fd25756478f4bbf4cfbcf22` — annotated tag object).
- Prior pin surveyed 2026-06-25: the category-level pass; no earlier per-skill pin exists, so this record is the baseline, not a delta.
- Checked at the pin: `README.md` head, `RELEASE-NOTES.md` head (v6.4.2 section), `skills/writing-plans/SKILL.md` in full, `skills/requesting-code-review/code-reviewer.md` in full, `skills/subagent-driven-development/` and `skills/executing-plans/` scripts listings. Clone is shallow (`--depth 1 --branch v6.4.2`); docs-to-agent fidelity and the remaining ~40 skills were not audited.

## Decision Question

Which v6.4.2 mechanisms, if any, close a verified gap in TeaPrompt's nine core skills or governance validators — given that routing, dispatch, worktrees, hook installation, and subagent orchestration are host-harness territory and permanently out of TeaPrompt scope?

## Verification Ladder

- Official repo pinned at tag `v6.4.2`; two source files read in full at the pin; release notes read at the pin.
- Fresh-consumer probes: each changed skill was run against a fixture request **before** the edit (unchanged baseline) and **after** (updated), by a clean subagent given only the SKILL.md text — proving the contract text itself induces the behavior, not this session's framing.
- Coverage boundary: probes show contract-induced output shape on synthetic fixtures only. They are not evidence of real-task efficacy.

## Candidate Adoption Ledger

| ID | Candidate | Status | Evidence | Next action or trigger |
| --- | --- | --- | --- | --- |
| SP-1 | Decision-only planning: a plan records decisions the executor cannot recover; code steps carry signature/file/pinned values, bodies only for undetermined algorithms; no code-transcript plans; bounded Review Focus list for spec-silent input classes; proportion over fixed budgets | Adopted in place 2026-10-03 — `reflective-spec-plan` §Planning Fidelity | `upstream/skills/writing-plans/SKILL.md` (lines 10, 77–88, 140–161, 173–175) read at pin; baseline probe already emitted decision gates + plan-size judgment (contract-adjacent), so adoption pins the explicit failure directions ("lines that decide nothing", transcript-shaped plans) and the spec-silence rule | Reopen if plans still arrive as code transcripts or if the Review Focus list is never exercised on real specs |
| SP-2 | Explicit review coverage/disposition: a named `Declined to Judge` section — every behavior set aside gets one line, a reason, and a ruling owner; spec silence is not permission to break; nothing declined is dropped silently | Adopted in place 2026-10-03 — `reflective-review` Output / Never / Review Flow step 8 / Output Shape | `upstream/skills/requesting-code-review/code-reviewer.md` (lines 33–48) read at pin; baseline probe already emitted a Claims Ledger with `unverifiable` statuses, so adoption adds the *named* declined-judgment surface and the no-silent-drop rule, not the ledger itself | Reopen if review outputs still let declined scope vanish, or the section duplicates Findings in practice |
| SP-3 | Subagent-driven development (`subagent-driven-development`, `executing-plans`, task-start/task-done scripts) | Rejected | Host orchestration territory: dispatching a fresh subagent per task is a runtime decision the host owns; TeaPrompt's standing non-goal excludes operating a multi-agent runner. Scripts are harness API calls, not prompt-layer contracts | Standing non-goal; would need an explicit rethink of the runtime boundary |
| SP-4 | Session bootstrap / plugin auto-injection (`using-superpowers`, SessionStart hooks, Muse plugin) | Rejected | Host-harness installation mechanics; TeaPrompt installs skills as files and relies on host rules and evals, not a separate invocation-enforcement protocol | Same non-goal boundary |
| SP-5 | Git worktree orchestration (`using-git-worktrees` skill chain) | Rejected | Host tooling; repo policy already covers isolated worktrees via harness `isolated` tasks | — |
| SP-6 | Whole-catalog skill import (brainstorming, TDD, debugging skills, ~40 skills) | Rejected | The useful prompt-layer mechanisms are already present across the nine skills (dispatch routing, spec planning, implementation gates, review gates, minimality); remainder is host territory or duplicates installed coverage | Local-gap question remains the standing test (see Handoff) |

## How Outputs Were Produced

1. Read upstream `RELEASE-NOTES.md` v6.4.2 section, README head, `writing-plans/SKILL.md`, and `code-reviewer.md` in full at the pinned tag.
2. Diffed candidate mechanisms against installed contract text — baseline probes run on the pre-edit SKILL.md text to separate "already induced" from "added by the edit".
3. Landed SP-1/SP-2 as contract paragraphs/sections only (no wording block imports); the record pins anchors in `plans/tests/test_superpowers_v642_adoption.py`.
4. Updated `PROJECT_KNOWLEDGE.md` Decision Index, this ledger, `external-adoption-case-studies-2026-06-20.md`, regenerated `index.json`, and ran the focused guard + full `make all` gate.

## Evidence Ledger

| Check | Result |
| --- | --- |
| Baseline spec-plan probe (pre-edit SKILL.md, fresh subagent, contract text only) | Already emitted Implementation Decision Gate + Plan-Size Judgment + a DoD "no implementation body leak" line — contract was adjacent; adoption adds explicit failure directions (transcript plans, lines that decide nothing) and the spec-silence Review Focus rule |
| Updated spec-plan probe (post-edit) | Added a bounded `## Review Focus` section (spec-silent input classes, each pinned to an owning task) and cited "Planning Fidelity & Proportion" explicitly; decision-gate shape retained |
| Baseline review probe (pre-edit) | Emitted a Claims Ledger with `unverifiable` rows but no named declined-judgment surface |
| Updated review probe (post-edit) | Emitted `## Declined to Judge` — two declined items with reasons and ruling owners, plus one checked-clean line; spec-silence reasoning cited inside a finding |
| `pytest plans/tests/test_superpowers_v642_adoption.py` | 7 passed — four SP anchors pinned at single surfaces, ledger dispositions, flow numbering, index links |
| `make all` | green — 1,365 tests passed; link/lint/governance/record-hygiene/index/benchmark/examples/route validators clean; ROUTE-001/002/003 evals passed |

## Mechanism-vs-Product Analysis

The adopted content is two reasoning contracts, not Superpowers' runtime machinery. Superpowers' actual product value — enforced skill invocation, subagent-per-task execution, worktree isolation — is host-side and stays host-side. What transfers is the *wording discipline*: plans-as-decisions and reviews-that-record-coverage are epistemic rules valid in any harness, which is why they land on core skills rather than a domain pack.

## Falsifiability

This record is wrong if (a) either adopted section silently duplicates an existing bullet without adding a checkable behavior — then merge it in place; (b) review outputs accumulate boilerplate `Declined to Judge: None` lines that carry no information — then scope the section to reviews that actually set something aside; (c) a real spec arrives where decision-only planning loses required detail — then define which classes of algorithm legitimately need bodies in the plan.

## Handoff

When future work asks whether to import more of Superpowers: start from the local-gap question — what failure in TeaPrompt is not already covered by the nine skills and governance validators — not from upstream's table of contents. SP-3–SP-6 rejections stand on the runtime non-goal, not on quality judgments about those skills.

## Latest-version refresh — 2026-10-22

- Prior baseline: tag `v6.4.2` → commit `8ca22dba9a94f28898bce59f2537ff4d87c747d7` (released 2026-09-25).
- Latest checked: `main` HEAD `2ce8aa15d05bd57213e6f746f953aafb7ded7a8b` (2026-10-21) = tag `v7.0.1` peel; intermediate release `v7.0.0` (`bb92a77741419a4ab5f06e711a283343f1ada0c3`, 2026-10-09). Branch, tag, and commit identities kept distinct; both releases are squash-merge commits on `main`.
- Range `8ca22dba..2ce8aa15`: 3 commits, 95 files (+2,381/−14,013). Most deletions are retired `docs/specs/` + `docs/plans/` design docs.
- Material upstream changes (release notes = author reports; range diff inspected):
  - v7.0.0: brainstorming rebuilt from scratch (playback with marked guesses, sized process, builder-check subagent replaces the spec-document reviewer); native Antigravity Marketplace manifest; hook hardening (broken-PATH SessionStart, Windows `run-hook.cmd` no longer executes cwd-planted `bash`/`where`, exit codes propagated); `task-done` records silent passes; `sdd-workspace` preserves repo `.gitignore` and uses repo-relative Windows paths; `requesting-code-review` BASE_SHA example `awk`→`cut` (Claude `$1` arg substitution); `systematic-debugging` secret-leak example fixed; Hermes skill descriptions.
  - v7.0.1: brainstorming retune (reads project context before asking, one open question at a time, skip-offer only when self-started, approaches + approved design doc before building); compaction survival (`subagent-driven-development`/`writing-skills` bodies moved to `references/`, new 20,000-byte `SKILL.md` size test); contribution templates require a human-written <200-word summary and decline agent-written PRs fixing others' issues unless requested.
- Adopted SP/FM policy: unchanged. Verified by diff: `skills/writing-plans/SKILL.md`, `skills/requesting-code-review/code-reviewer.md`, and `skills/using-superpowers/` are byte-identical across the range; the only requesting-code-review touch is the one-line BASE_SHA example fix. SP-1/SP-2 contracts stand; SP-3–SP-6 rejections (host-harness territory) unaffected. The brainstorming rebuild is prompt-layer but maps to `reflective-brief`, which already covers intent clarification; no local gap demonstrated, so reference-only, no new adoption.
- Observation: the annotated tag object for `v6.4.2` now hashes `668b16d4d8d4d603fd257567684fbbffccbf2022`, differing from the peel recorded 2026-10-03 — the tag object appears recreated; the commit identity `8ca22dba` is stable and is the authoritative pin.
- Inspected: `git ls-remote` HEAD + tags on `https://github.com/obra/superpowers`, `https://raw.githubusercontent.com/obra/superpowers/main/RELEASE-NOTES.md`, and the range diff above. No runtime verification; remaining-skills audit still not done.
