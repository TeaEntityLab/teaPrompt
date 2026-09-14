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
| Durable-runtime reference revalidation | Before a future implementation or deployment claim relies on Temporal, LangGraph, DBOS, Restate, Orleans, OTP, or another live runtime source | Pin the exact host/version; keep source-read, executed, process-kill, real-sink, failover, and power-loss evidence tiers separate | [Harness lineage addendum AH-9/AH-18](agent-harness-convergence-survey-2026-08-25.md#2026-08-25-technical-lineage-addendum) |
| Pack template dry-run before commit | Any edit to a fenced executable template in a registered domain pack | A stub dry-run covers each gate path the template implements; the regression test is updated, never deleted | [Intent-drift rethink L-1](harness-intent-drift-rethink-2026-09-06.md), [installed-skills GL-6](installed-skills-general-lessons-2026-09-05.md) |
| Same-day adoption collision check | Two records adopt onto the same skill in one session | Before the second lands, diff the skill for a sentence already holding the shared clause; land one merged sentence and point both guards at it | [September review](september-skills-review-2026-09-14.md) |
| Flow-pack size budget | Any adoption touching `flow-control-generator` or `flow-loop-harness` | Zero-sum text (an offsetting deletion) until the checkpoint decides a pack lint tier; body stays ≤ 20,000 chars | [September review](september-skills-review-2026-09-14.md), [skill-verification panel](skill-verification-panel-2026-09-05.md) |
| Next survey of the 2026-09-05 agentflow source | The source publishes past `fcb6878` | Delta-only in a separate record; the coordinator owns the top-level contract diff; probe only if a sentence is drafted; no new panel | [8.2 delta record](agentflow-8.2-delta-survey-2026-09-13.md) |

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
| `governed-delivery` recurrence checkpoint | Any host-supplied evidence of a `governed-delivery` invocation? None → recurrence stays `unknown` and the pack is demoted by policy: fold into its adoption record, unwind `DOMAIN_PACK_SKILLS` 4→3 and every admission surface | Host-supplied invocation evidence only; a skipped checkpoint demotes | [GD adoption §Demotion Triggers](governed-delivery-adoption-2026-09-03.md), [GD review R5/R6](governed-delivery-review-2026-09-13.md) |
| GD↔AGS redundancy-in-use | Has `governed-delivery` ever run independently of `agent-governance-scaffold`; has the shared host-precondition / `artifact-complete` / constitutional-path machinery diverged? | Same evidence; a diff of the two packs' shared blocks | [GD review R6](governed-delivery-review-2026-09-13.md) |
| Flow-pack lint tier decision | Both flow packs sit under 1k chars below the 20k lint warning; decide a pack lint tier (25k, matching AS8) or template factoring | Current char counts; agenda item 6 (AS8/R10) | [September review](september-skills-review-2026-09-14.md) |
| A1/E1 anchor tightening | Keep the two decorative-leaning GD anchors (`reflective-brief` A1, `reflective-research` E1) at full length, or reduce each to its novel clause? | Any local case where the owner tag or attester field carried weight | [GD review §Shared Findings](governed-delivery-review-2026-09-13.md) |

Event-gated sibling (no fixed date): **M5 managed-skill re-audit** fires at the next
governance panel ([managed-skill record](managed-skill-promotion-panel-record-2026-07-11.md)) —
**fired 2026-09-13** at the GD-18 panel (four TeaPrompt managed skills audited, one
corrected host-side; [record](governed-delivery-review-2026-09-13.md)); it fires again
at the checkpoint if that session convenes a panel.

## Horizon 3 — Trigger-gated queue (dormant until the named event)

### Adopted 2026-07-12 (user-directed; recurrence `unknown`)

Closed out of the queue under an explicit user instruction; recurrence stays
`unknown`, guards migrated from absence to activation → [adoption record](dormant-items-user-directed-adoption-2026-07-12.md).

| Item | Surface | Guard |
| --- | --- | --- |
| P12 — DAG executor template | `flow-control-generator` | `test_dormant_item_watch.py`, `test_dormant_conditional_contracts.py` |
| P13 — multi-wave template | `flow-loop-harness` | same |
| M4 — ephemeral-source internalization | [`04-agent/workflow-acquisition.md`](../04-agent/workflow-acquisition.md) | `test_dormant_conditional_contracts.py` |
| M6 — README `## Orientation` | Root README (EN + zh-TW) | `test_dormant_conditional_contracts.py` |
| M7 — sensitive-evidence packet handling | [`04-agent/external-adoption-review.md`](../04-agent/external-adoption-review.md) | `test_dormant_conditional_contracts.py` |
| D4 — record-hygiene validator | [`validate_record_hygiene.py`](validate_record_hygiene.py) + Makefile | `test_validate_record_hygiene.py` |
| Writer-critic deterministic companion | `flow-loop-harness` guidance | template-set pin |

### Adopted 2026-08-25 (user-directed; recurrence `unknown`)

Explicit user direction promoted only the risk-scaled, prompt-level recovery
contract; host enforcement and the deferred Effect Contract/benchmark remain
unfired.

| Item | Surface | Guard |
| --- | --- | --- |
| AH-19 — external-effect recovery skill repair | `04-agent/runtime-trust-boundary.md`; `reflective-risk`; `reflective-spec-plan`; `reflective-implement`; `reflective-review`; `reflective-handoff-retro` | `test_agent_harness_convergence_survey_record.py` + affected prompt/skill eval harnesses |

### Adopted 2026-09-03 → 2026-09-14 (user-directed and consensus; recurrence `unknown`)

Thirteen records in eleven days; every adoption is guarded at its surface and
indexed in the Decision Index. Listed here so the queue reflects what landed
outside it (the plan's "adopted without appearing here" falsifier fired and is
reconciled by this section).

| Item | Surface | Guard |
| --- | --- | --- |
| GA-1..GA-9 — governable-autonomy sentences | `reflective-implement`, `-review`, `-research`, `-brief`, `-risk`, `-handoff-retro`; `04-agent/*`; `06-repo/AGENTS.md` | `test_governable_autonomy_survey_record.py` |
| GD-1..GD-18 — `governed-delivery` pack (4th registered pack) + eight core anchors; independent review 2026-09-13 | pack; eight core skills; registry, examples, skill-map, cheatsheets, install guides | `test_governed_delivery_adoption_state.py` |
| AF-2/19/20, EP-1/6, CX-1..6, TK-10 — agentflow | implement, handoff-retro, minimality, dispatch, brief, spec-plan, review; `runtime-trust-boundary.md`; PK Lesson | `test_agentflow_survey_record.py` |
| GL-1..10, JL-2a/3, skill-verification fixes | six core skills; both flow packs; `agent-governance-scaffold` | `test_installed_skills_general_lessons_record.py`, `test_llm_judge_lifecycle_survey_record.py`, `test_skill_verification_panel_record.py` |
| G-1/2, L-1/2, A-7a, OG-1..4, AF82-1/2/9/14 | GLOSSARY; implement; minimality; spec-plan; research; dispatch | the respective record guards |
| September review merges (GA-4+C2, GA-5+D1, GA-6+E1), three intra-skill trims, GLOSSARY `stale` / `unknown` | implement, review, research, dispatch, minimality, handoff-retro; GLOSSARY | `test_september_skills_review_record.py` |

### Still trigger-gated

| Item | Wakes when | Destination surface | Source |
| --- | --- | --- | --- |
| E2 — archive restructuring (panel-transcript demotion, `00-core`/`03-context` merges) | Second independent archive-weight complaint, or a maintainer hits real navigation failure attributable to these surfaces | `plans/`, prompt categories | [Rethink Adoption Update 2](governance-rules-rethink-review-2026-07-11.md) |
| `reflective-implement` default-invokes `reflective-minimality` | Three cross-session recurrences (signal scan suffices today) | `reflective-implement` skill | [June backlog](multi-agent-panel-consensus-2026-06-25.md#recurrence-gated-backlog-not-panel-blockers) |
| Localized trigger cues beyond cheatsheet/glossary | Adoption signal from zh-TW users | zh-TW navigation surfaces | [June backlog](multi-agent-panel-consensus-2026-06-25.md#recurrence-gated-backlog-not-panel-blockers) |
| AH-11/AH-15 — multi-axis Effect Contract re-litigation | A named host integration exposes a mutation/recovery gap that the existing trust/risk contracts cannot express | Host-specific schema and enforcement owner; parameter/authority binding; representative adapters; negative retry/reconciliation tests; Human Review fallback | [Harness lineage addendum AH-11/AH-15](agent-harness-convergence-survey-2026-08-25.md#technical-lineage-candidate-adoption-ledger) |
| AH-14 — Harness Reliability Benchmark | A concrete runtime-adoption decision names the target host/version and external-effect scope | Pre-registered baselines; real idempotent, transactionally coupled, and non-idempotent sinks; externally observed postconditions; process-kill/network/zombie/power tiers; latency, cost, unresolved backlog, and operator-load measures | [Harness lineage addendum AH-14](agent-harness-convergence-survey-2026-08-25.md#technical-lineage-candidate-adoption-ledger) |
| I-1 / A-5 — a tool status line or viewer preview is a claim, not the artifact | A second tool misreport in any record (I-1), or an observed read-side occurrence acted on as source (A-5); on fire, decide fold vs twin on the record | `reflective-implement` §Verification (fold) or `runtime-trust-boundary.md` §4 (twin) | [Rethink I-1](harness-intent-drift-rethink-2026-09-06.md), [Astra A-5](astra-efficiency-rules-survey-2026-09-10.md) |
| GD-19 — "deliver / autonomous / unattended" collision measurement | **Measured 2026-09-14:** nine fresh phrases 100% pre-tune; one R11 paraphrase gap fixed under holdout-before-tune | `ROUTING_CONTRACT.md` R11; ROUTE fixtures | [GW-1](governance-workflow-self-control-adoption-2026-09-14.md) |
| GD-16 — refuters GDR-1..GDR-6 host run | The first named host harness runs the contract set | GD adoption record: pass/fail per GDR | [GD adoption GD-16](governed-delivery-adoption-2026-09-03.md) |
| TK-1 — extra-work offer is not a criterion | A local run widens on a same-run offer plus chat assent without a packet criterion | `reflective-implement` Never (the AF-2 bullet) | [Agentflow TK-1](agentflow-survey-2026-09-05.md) |
| E-5 — legible acceptance over an unmet oracle | The first local `governed-delivery` acceptance closed against an unmet oracle | `governed-delivery` acceptance-record invariant | [gpt-instruct E-5](gpt-instruct-survey-2026-09-10.md) |
| GA-13 / XS-4 — live fault-injection suite | A named host-eval harness (AH-14 / FM3) | Host CI, never TeaPrompt CI | [GA survey](governable-autonomy-survey-2026-09-03.md), [GA coverage panel](ga-skills-coverage-panel-2026-09-03.md) |
| Cross-core traceability checklist (`reflective-implement` step 4 restates the `reflective-spec-plan` Decision Gate) | **Resolved 2026-09-14:** compacted to one self-contained sentence; no cross-reference policy needed | `reflective-implement` Workflow step 4 | [GW-5](governance-workflow-self-control-adoption-2026-09-14.md) |
| Ledger status vocabulary (`asserted` / `unverified` / `pending` / `open` for one epistemic state) | Unification still waits for a documented cross-skill handoff confusion; the GLOSSARY §Ledger Status Families map (2026-09-14) is the smaller alternative in force | GLOSSARY; the four ledgers | [GW-3](governance-workflow-self-control-adoption-2026-09-14.md) |
| Pack example coverage (orchestrator, router, DAG, writer-critic floor, multi-wave) | **Resolved 2026-09-14** for writer-critic floor, multi-wave, orchestrator, DAG; the conditional router stays uncovered until a host run | `skills/examples/flow-*.examples.md` | [GW-6](governance-workflow-self-control-adoption-2026-09-14.md) |
| Single-sentence reserves: E-2, E-11, E-12; JL-1, JL-9/17; AF82-11 | Each row's own named local case | Named in each record | [gpt-instruct](gpt-instruct-survey-2026-09-10.md), [LLM-judge](llm-judge-lifecycle-survey-2026-09-05.md), [8.2 delta](agentflow-8.2-delta-survey-2026-09-13.md) |

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
- P7/N12 pack routing integration — **no-change decided 2026-07-11** after
  three fresh collision groups / 9 phrases passed 100% pre-tune: packs remain
  host-invoked and outside core routing. Re-open only on the successor evidence
  trigger in the [decision record](p7-pack-routing-decision-2026-07-11.md).
- M8 blanket other-project skill promotion
  ([managed-skill record](managed-skill-promotion-panel-record-2026-07-11.md)).
- N8 meta:product ratio unless a stable guarded formula is defined first
  ([necessity record](governance-necessity-panel-record-2026-07-11.md)).
- STORM fan-out as a generator topology, per-script provenance ledger headers,
  semantic ledger columns in loop state, memory backends for loop state,
  retry-with-backoff, and other serving-layer features
  ([flow-coverage §Rejected](flow-coverage-panel-record-2026-07-11.md)).
- `skills/packs/` nesting and repo-root pack placement
  ([pack record](flow-control-pack-panel-record-2026-07-11.md)).
- AH-10 canonical nine-layer Agent Runtime architecture — study diagram only;
  re-open after a pre-registered comparison shows it prevents a failure missed by
  the smaller control/effect/ownership contracts at acceptable cost
  ([lineage addendum AH-10](agent-harness-convergence-survey-2026-08-25.md#technical-lineage-candidate-adoption-ledger)).
- AH-13 prompt-level fencing/OTP enforcement and AH-17 universal P0–P3 research
  order — runtime enforcement remains host-owned and priorities remain
  use-case-specific
  ([lineage addendum AH-13/AH-17](agent-harness-convergence-survey-2026-08-25.md#technical-lineage-candidate-adoption-ledger)).


## Falsifiability

This roadmap is wrong or stale if: a cited trigger fires and the item is acted on
without a record (queue discipline violated); the 2026-10-11 checkpoint passes
undocumented; a Standing Non-Goal is reopened without a PK direction change; or a
new deferred item appears in a panel record but not here at the next checkpoint.

Roadmap self-review 2026-09-14: the "new deferred item appears in a panel record
but not here" falsifier had fired for all thirteen September records, and the
plan's pack-registry falsifier (2→4) with it; both reconciled by the September
rows above and the [September review](september-skills-review-2026-09-14.md).
The 2026-10-11 runbook now carries the `governed-delivery` checkpoint.

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
