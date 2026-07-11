# Whole-Project Roadmap — TeaPrompt (2026-07-11)

> **Status: active planning artifact (non-authoritative).** Scheduling companion to
> [whole-project-plan-2026-07-11.md](whole-project-plan-2026-07-11.md). This roadmap
> aggregates when things happen; the owning decisions stay in the cited records and
> in [`PROJECT_KNOWLEDGE.md`](../PROJECT_KNOWLEDGE.md). It grants no authority and
> adds no new gates: every row restates an existing gate with a pointer. If a row
> and its source record disagree, the record wins.

## Horizon model

TeaPrompt does not schedule by calendar quarters; it schedules by **gates**. Four
horizon classes, ordered by certainty:

1. **Standing cadence** — always-on maintenance duties tied to change events.
2. **Date-gated** — a named calendar checkpoint exists (currently one: 2026-10-11).
3. **Trigger-gated** — fires when a named, observable event occurs; until then the
   item is deliberately dormant (missing usage evidence is `unknown`, not zero).
4. **Direction-gated (never-unless)** — Standing Non-Goals; only an explicit human
   direction change reopens them.

This mirrors how the project actually decides (recurrence gates, holdout-before-tune,
demotion triggers) — a quarter-based roadmap would fabricate certainty the evidence
does not support.

## Horizon 1 — Standing cadence (always on)

| Duty | When it fires | Gate / check | Source |
| --- | --- | --- | --- |
| `make all` from the repository root | Every governance or routing change | Full pytest + validators + ROUTE-001/002/003 | [Playbook item 1](../GLOSSARY.md#governance-maintenance-playbook--治理維護手冊) |
| Holdout-before-tune | Before any router keyword/rule change | Fresh ROUTE-002/003 phrases added first; `validate_route_fixture.py` blocks shrinkage | [ROUTING_CONTRACT R8](ROUTING_CONTRACT.md) |
| Decision Index entry | Governance-surface change lands | `validate_project_knowledge.py` undocumented-decision warning stays clean | Playbook operational test |
| Undocumented-decision warning watch | Each validator run | Non-blocking warnings triaged, not ignored | [QUALITY_GATES_SUMMARY.md](QUALITY_GATES_SUMMARY.md) |
| Regenerate committed `index.json` | Docs, skills, or plans change | `python3 reflective-prompt-library/plans/generate_index.py` | QUALITY_GATES Validation Commands |
| Adoption Guard Closure audit | Any Candidate Adoption Ledger row flips state | Phrase pins retire or become structural | [GLOSSARY §Adoption Guard Closure](../GLOSSARY.md#adoption-guard-closure) |
| Evidence-tier labels on new records | Every new panel/research record | Packet contract fields present; same-host caveat stated | [Necessity record N13](governance-necessity-panel-record-2026-07-11.md) |
| Cheatsheet / cross-link / HR parity mechanics | When the named surfaces change | Playbook items 6–33 name the exact test per surface | [GLOSSARY playbook](../GLOSSARY.md#governance-maintenance-playbook--治理維護手冊) |
| Optional manual benchmark run | Operator discretion (never CI) | `benchmark_tasks.py` baseline-vs-skill comparison | [June backlog](multi-agent-panel-consensus-2026-06-25.md#recurrence-gated-backlog-not-panel-blockers) |

Near-term actionable tasks T1 (P15 parity review), T2 (zh-TW pack-appendix parity),
T3 (manual pack-usage evidence convention), and T4 (loop-pack demotion-trigger
evaluation, added 2026-07-11 after the
[skills/flow-control survey](../../surveys/agent-skills-flow-control-survey-2026-07-11.md))
are defined with acceptance criteria in the
[plan's open-work register](whole-project-plan-2026-07-11.md#consolidated-open-work-register);
T3 must land before the Horizon 2 checkpoint to make P6 evidential, and T4's
seed analysis lives in the [flow-control roadmap](flow-control-roadmap-2026-07-11.md).

## Horizon 2 — Date-gated checkpoint: 2026-10-11

The only calendar commitment currently on record. Agenda:

| Item | Question to answer | Evidence needed | Source |
| --- | --- | --- | --- |
| P6 / N11 — pack merge re-litigation | Did either `flow-control-generator` or `flow-loop-harness` see zero solo invocations? If yes, re-open merge-to-one-skill (Minimality dissent preserved) | Manual usage log (task T3); `unknown` must be recorded as `unknown` | [Pack record §Required Changes 6](flow-control-pack-panel-record-2026-07-11.md), [Necessity N11](governance-necessity-panel-record-2026-07-11.md) |
| Pack utility claims re-verification | Utility claims above template correctness were labeled `[INFERENCE]` until this review | Same usage log | [Pack record §Disagreements](flow-control-pack-panel-record-2026-07-11.md) |
| T2 stability check | EN pack appendix unedited since 2026-07-11? Then zh-TW parity qualifies as due | Git history of the EN cheatsheet | [Pack record §Required Changes 6](flow-control-pack-panel-record-2026-07-11.md) |
| T4 / F1 — loop-pack demotion evaluation | **Answered 2026-07-11: not fired** (model-judge stop; unpackaged Stop-hook primitives). Checkpoint duty reduces to re-checking the F4 watch table | [Evaluation record](flow-pack-demotion-evaluation-2026-07-11.md); [usage log](flow-pack-usage-log.md) | [Pack record §Demotion Triggers](flow-control-pack-panel-record-2026-07-11.md) |
| Roadmap self-review | Any trigger below fired unnoticed? Any staleness falsifier hit? | This file vs Decision Index diff | [Plan §Falsifiability](whole-project-plan-2026-07-11.md#falsifiability-staleness-triggers-for-this-plan) |

Event-gated sibling (no fixed date): **M5 managed-skill re-audit** fires at the next
governance panel, whenever that occurs ([managed-skill record](managed-skill-promotion-panel-record-2026-07-11.md)).

## Horizon 3 — Trigger-gated queue (dormant until the named event)

| Item | Wakes when | Destination surface | Source |
| --- | --- | --- | --- |
| P7 / N12 — pack trigger phrases in core router + quick cues | New ROUTE-002/003 holdout groups covering pack/core collisions exist first (holdout-before-tune); then decide whether dispatch should route to packs at all. Candidate groups + pre-tune procedure: [routing-holdout plan](routing-holdout-plan-2026-07-11.md) | Route fixtures, router, cheatsheets | [Pack record §Required Changes 6](flow-control-pack-panel-record-2026-07-11.md), [Necessity N12](governance-necessity-panel-record-2026-07-11.md) |
| P12 — Conductor-style DAG executor template | First local task needing dependency-gated fan-out that pipeline/parallel/orchestrator templates cannot express | `flow-control-generator` | [Flow-coverage §Deferred](flow-coverage-panel-record-2026-07-11.md) |
| P13 — dedicated multi-wave ReMoM template | Recurrence of real multi-wave runs (composition note already adopted) | `flow-loop-harness` | [Flow-coverage §Deferred](flow-coverage-panel-record-2026-07-11.md) |
| M4 — ephemeral-source internalization deltas | Third documented local occurrence (count today: 1) | [`04-agent/workflow-acquisition.md`](../04-agent/workflow-acquisition.md) | [Managed-skill M4](managed-skill-promotion-panel-record-2026-07-11.md) |
| M6 — README `## Orientation` section | Newcomer-orientation gap recurs in future session records | Root README | [Managed-skill M6](managed-skill-promotion-panel-record-2026-07-11.md) |
| M7 — redaction methodology | First TeaPrompt-local sensitive-evidence external review | [`04-agent/external-adoption-review.md`](../04-agent/external-adoption-review.md) | [Managed-skill M7](managed-skill-promotion-panel-record-2026-07-11.md) |
| E2 — archive restructuring (panel-transcript demotion, `00-core`/`03-context` merges) | Second independent archive-weight complaint, or a maintainer hits real navigation failure attributable to these surfaces | `plans/`, prompt categories | [Rethink Adoption Update 2](governance-rules-rethink-review-2026-07-11.md) |
| D4 — record-hygiene lint | A new record ships without evidence separation or fact-check dating | New validator | [Rethink Adoption Update 2](governance-rules-rethink-review-2026-07-11.md) |
| `reflective-implement` default-invokes `reflective-minimality` | Three cross-session recurrences (signal scan suffices today) | `reflective-implement` skill | [June backlog](multi-agent-panel-consensus-2026-06-25.md#recurrence-gated-backlog-not-panel-blockers) |
| Localized trigger cues beyond cheatsheet/glossary | Adoption signal from zh-TW users | zh-TW navigation surfaces | [June backlog](multi-agent-panel-consensus-2026-06-25.md#recurrence-gated-backlog-not-panel-blockers) |
| Writer-critic deterministic companion check | User demand for a non-model gate beside the advisory-tier critic (open design question) | `flow-loop-harness` guidance | [Flow-coverage §Disagreements](flow-coverage-panel-record-2026-07-11.md) |

Queue discipline: when a trigger fires, the item gets its own review/panel record
with a Candidate Adoption Ledger — a fired trigger authorizes *re-litigation*, not
silent adoption.

## Horizon 4 — Direction-gated (never-unless)

Standing Non-Goals; reopened only by an explicit human direction change recorded in
[PROJECT_KNOWLEDGE.md](../PROJECT_KNOWLEDGE.md#standing-non-goals):

- Operating any TeaPrompt-owned runtime: multi-agent runtime, swarm, async peer
  messaging, recorder, replay engine, side-effect enforcer.
- A tenth core workflow skill (three-recurrence promotion gate + explicit human
  approval; a user-directed pack exception never waives this).
- Full `SKILL.md` localization (navigation/cheatsheet/glossary parity only).
- LLM benchmark comparisons in CI (fixture gate only; manual runs allowed).
- Enforcing runtime guarantees that skills merely declare (host runtime is the
  authority; missing enforcement evidence is `unknown` / no-go).

## Rejected — do not re-litigate without new evidence

Recorded no-change/reject outcomes, kept visible so they are not silently re-argued:
M8 blanket other-project skill promotion ([managed-skill record](managed-skill-promotion-panel-record-2026-07-11.md));
N8 meta:product ratio unless a stable guarded formula is defined first
([necessity record](governance-necessity-panel-record-2026-07-11.md)); STORM fan-out
as a generator topology, per-script provenance ledger headers, semantic ledger
columns in loop state, memory backends for loop state, retry-with-backoff and other
serving-layer features ([flow-coverage §Rejected](flow-coverage-panel-record-2026-07-11.md));
`skills/packs/` nesting and repo-root pack placement ([pack record](flow-control-pack-panel-record-2026-07-11.md)).

## Falsifiability

This roadmap is wrong or stale if: a cited trigger fires and the item is acted on
without a record (queue discipline violated); the 2026-10-11 checkpoint passes
undocumented; a Standing Non-Goal is reopened without a PK direction change; or a
new deferred item appears in a panel record but not here at the next checkpoint.

## Verification

- Every row above was traced to its source record this session; no new gate was
  invented.
- Mechanical check after both files were added (2026-07-11, repository root):
  `generate_index.py` → 104 files indexed (93 prompts, 11 skills); `make all` →
  782 pytest tests passed; links/lint/governance/PK/benchmark/skill-example/route
  fixture validators all passed (lint: 0 errors, 7 pre-existing length warnings on
  large records, none on these files); ROUTE-001 128, ROUTE-002 114, ROUTE-003 66
  phrases — each at 100% seeded-fixture consistency (regression-guard tier, not
  semantic proof).
