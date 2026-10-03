# Superpowers v6.4.2 Adoption Record — 2026-10-03

> **Status: implemented — verified within the recorded fixture scope.** User direction: "Survey https://github.com/obra/superpowers (updated recently)" (accessed 2026-10-03). Continuing the selective adoption pattern: two narrowed contracts land on existing core skills; no new skill, domain pack, helper, route, runtime, or install-time behavior. Supersedes the earlier high-level pass in `plans/skills-and-spec-systems-research-2026-06-25.md`, which covered Superpowers only at category level before the current release line.

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
