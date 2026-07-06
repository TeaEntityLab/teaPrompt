# Workflow Possibilities and Constraints Review — 2026-07-06

## Purpose

Record the parallel-lens discussion and decision for the question: **"Based on all surveys and docs, rethink about the workflow possibilities and is all constraints reasonable or unnecessary."**

This record is governance / methodology evidence. It is not a standard, a compliance guide, a runtime commitment, or an agent operating rule. Any wording change it proposes is a candidate; none is applied by this record alone.

## Panel Packet

The review used the `parallel-lens-review-packet` protocol. A shared evidence packet was written to `local://workflow-review-packet.md` and its key evidence embedded in each reviewer assignment (subagents cannot resolve `local://`). The packet separated observed repository evidence, author-claimed evidence, and `[INFERENCE]`.

State at review time:

- Branch `main`, commit `3ec4771`, working tree clean, local date `2026-07-06`.

Observed inputs included:

- `README.md` / `reflective-prompt-library/README.md`: North Star is right-rigor + evidence via composable prompt layers and nine workflow skills, without operating an agent runtime; skills are prompt-level wrappers, not a multi-agent runtime.
- `PROJECT_KNOWLEDGE.md` Standing Non-Goals: no TeaPrompt-owned runtime/swarm/async messaging/recorder/replay/side-effect enforcer; nine frozen workflow skills; seeded routing evals are regression guards, not semantic-routing proof; methodology-complete is not operationally complete; skills may specify runtime guarantees but cannot enforce them.
- `04-agent/artifact-promotion.md`, `04-agent/workflow-acquisition.md`, `04-agent/runtime-trust-boundary.md`: the promotion ladder no change → decision/lens → SOP → skill → skill plus deterministic verifier → runner, and the prompt-vs-runtime enforcement split.
- `04-agent/workflow-recipes.md`: prompt-only, brief, spec/plan, implementation, review/research/risk overlays, looper topologies, and parallel-lens review, each with a ceremony falsifier.
- `plans/skills-runtime-legitimacy-panel-record-2026-07-06.md`: runtime is legitimate only for prompt-impossible guarantees proven by deterministic verifier/runtime code, with risk gates and Human Review.
- `plans/QUALITY_GATES_SUMMARY.md` and `plans/ROUTING_CONTRACT.md`: holdout-before-tune, route-trace observability, and the seeded-fixture-not-semantic-proof caveat.
- 2026-06-25 skills / memory / agent-tooling surveys and `plans/external-adoption-case-studies-2026-06-20.md`: external tools/models/memory are references unless a verified local gap exists (STORM is the exception folded into `reflective-research`).
- `surveys/ornith-1.0-survey.md`: maintainer-reported, unreproduced benchmark claims.

## Panel Lenses

Three reviewer lenses returned usable output:

- Workflow architecture / maintainer usability: `AGREE WITH CHANGES`
- Evidence auditor / reproducibility: `AGREE WITH CHANGES`
- Security / provenance / data-egress: `AGREE WITH CHANGES` (recorded as `overall_correctness: incorrect` on the packet's synthesis-as-load-bearing framing; the constraints themselves were judged safety floors)

## Panel Consensus

**Decision:** `AGREE WITH CHANGES`

**Core finding:** Most constraints are reasonable — they are safety floors and minimality gates, not unnecessary friction. The defects are in wording, reachability, and evidence-tiering, not in the constraints themselves. No constraint should be removed or loosened beyond the qualifications already recorded.

**Use-case recommendation:**

| Use case | Recommendation |
| --- | --- |
| `study` | Keep surveying external runtimes, memory systems, model/scaffold releases, and agent workflows as reference material. |
| `reproduce` | Reproduce narrow mechanisms only in sandboxed/isolated settings; mock/sandbox success is not deploy evidence. |
| `adopt` | Adopt by folding ideas into existing prompts, lenses, SOPs, or skill plus deterministic verifier before adding surface. |
| `deploy` | Runtime/runner is legitimate only for prompt-impossible guarantees proven by host-runtime tests, with accepted risk gates. |

## Constraints Judged Reasonable (keep)

- No prompt-only claims for runtime guarantees — prompt text cannot enforce persistence, replay, cancellation, idempotency, role isolation, side-effect gates, audit logs, or memory ACLs.
- Nine compact workflow skills as the default surface, recurrence-gated for a tenth.
- Local-gap gate for external adoption; STORM is the proven exception pattern.
- Holdout-before-tune and no semantic-routing overclaim from seeded fixtures.
- Artifact-promotion ladder preventing both documentation clutter and premature runtime code.
- Human Review / stop / no-go when a required gate cannot be deterministically enforced.

## Constraints Judged Too Rigid Only If Read As Absolute (qualify, do not remove)

- "No runtime" is not "never runtime" — the runtime-legitimacy record already allows runtime for prompt-impossible guarantees with enforcement proof.
- "No tenth skill" is gated, not infinite — a verified recurring workflow with stable trigger/inputs/outputs/failure signals/checks plus explicit human approval remains promotable.
- "Repo-native memory only" is right for project knowledge, not universal product advice — the memory survey notes application memory can need a runtime substrate.
- "Methodology-complete" must stay scoped to prompt/spec/lens coverage.
- Parallel-lens review must keep its ceremony falsifier so it does not run for routine L1-L2 work.

## Required Wording Changes (candidates; not applied by this record)

1. **Qualify "frozen" at high-traffic entry points.** `skills/skill-map.md` and `METHODOLOGY_MAP.md` state "nine frozen workflow skills" without the inline gate. Append: "frozen means gated, not never; a tenth core skill needs the three-recurrence promotion gate and explicit human approval." Note: `test_readme_governance.py`, `test_skill_module_contract.py`, and `test_validate_benchmark_fixture.py` assert the literal phrase — keep "nine frozen workflow skills" and append the gloss to stay low-churn.
2. **Disambiguate the three L-ladders.** `GLOSSARY.md` names Strictness L1-L6 and Formalization L0-L4 but not Acquisition L0-L4 (`workflow-acquisition.md`). Add: "Acquisition L0-L4 is the promotion-time view of the same automation-depth ladder as Formalization L0-L4; Acquisition L3 and Formalization L3 both mean skill plus deterministic verifier; do not introduce a fourth L-ladder."
3. **Surface the L3 verifier path in routing.** Add a `reflective-dispatch` Route row and a `workflow-recipes` note: "recurring task with an objective deterministic pass/fail check → primary workflow skill plus a `verifier/test` artifact (Acquisition L3); do not jump to a runner unless a prompt-impossible guarantee is required." No new skill; the verifier is an artifact destination.
4. **Make security gates fail-closed at L3, not only L4.** The L3 verifier definition (panel record and `artifact-promotion.md`) should require, when relevant: (a) a data-not-instruction / prompt-injection authority-boundary check; (b) a supply-chain provenance / license / SBOM / telemetry-default record; (c) a memory-write provenance tag (source, authority class, evidence-vs-instruction, scope, expiry/review, rollback path).
5. **Tier the evidence explicitly.** Label panel consensus as advisory / model-vote-tier (not operational proof), ROUTE fixtures as regression-guard-tier, external surveys as stale-unless-refreshed before adopt/deploy, and Ornith benchmark numbers as non-load-bearing for workflow constraints.

## Shared Findings

1. The compact nine-skill surface and no-owned-runtime default remain correct as defaults.
2. The strongest under-used workflow possibility is L3 skill plus deterministic verifier — enforcement without a runner — currently under-routed and under-specified.
3. Security controls the runtime-legitimacy panel names at L4 (prompt-injection isolation, supply-chain provenance, memory-write provenance) are not fail-closed at L3, so they depend on reviewer recall of the catch-all no-go rule.
4. Evidence tiers in the packet are honestly separated in isolation but the synthesis reasons from advisory/model-vote and no-operator-data classes as if load-bearing.

## Disagreements / Residual Risks

- Evidence auditor pushed hardest: no fresh operator-usage dataset proves which constraints cause toil, so "unnecessary friction" claims are recurrence-gated hypotheses, not adopt-ready recommendations. By the project's own three-recurrence gate, a relaxation claim needs the same recurrence evidence as a promotion claim.
- Workflow architect agreed the constraints stand; issues are wording and discoverability.
- Security reviewer found no adoption/deployment blocker but three verifier-layer specification gaps to close so gates trigger at promotion time.
- Residual risk: without change 3, maintainers under-formalize recurring checks inside `reflective-implement` or over-formalize into a runner, because the L3 surface is invisible at the decision point.

## Evidence Actually Checked

- Executed (this session, read-only): `cx overview` of repo/`04-agent`/`plans`/`skills`; `git rev-parse`/`branch`/`status`; `date`; `grep` for survey mentions, methodology-complete wording, and runtime/adapter wording; direct reads of README (both), `PROJECT_KNOWLEDGE.md`, `METHODOLOGY_MAP.md`, `GLOSSARY.md`, `skill-map.md`, `reflective-dispatch`/`reflective-minimality` SKILLs, `workflow-recipes.md`, `workflow-acquisition.md`, `artifact-promotion.md`, `runtime-trust-boundary.md`, `ROUTING_CONTRACT.md`, `QUALITY_GATES_SUMMARY.md` (selected), the three 2026-06-25 surveys (selected), `external-adoption-case-studies-2026-06-20.md` (selected), `skills-runtime-legitimacy-panel-record-2026-07-06.md`, `five-layer-agent-sop-reference-record-2026-07-04.md` (selected), `vllm-micro-agent-research-record-2026-06-30.md` (selected), `surveys/ornith-1.0-survey.md`; three parallel-lens reviewer subagents.
- Read but not re-executed: full contents of the surveys' upstream sources.
- Author-claimed, not reproduced here: `validate_links.py` 121 files / 0 errors; ROUTE-001/002/003 at 100%; benchmark_tasks.py 24 tasks; panel reviewer transcripts; Ornith benchmark numbers.
- Not run: `make all`, project-wide validators/tests, fresh external web/API recency checks. `plans/` coverage was targeted (survey/workflow/routing/quality-gate/runtime surfaces), not exhaustive.

## Falsifiability

This record is wrong if a later session finds the constraints block a verified recurring workflow that meets the promotion gate, or if the five candidate wording changes are never adopted and never re-litigated. Either signal means promote the relevant change or correct the constraint. Until then the constraints stand as recorded and the wording changes remain recurrence-gated candidates.
