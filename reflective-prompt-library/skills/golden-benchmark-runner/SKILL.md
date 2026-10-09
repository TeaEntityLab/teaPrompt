---
name: golden-benchmark-runner
description: Use to run a baseline-vs-skill comparison over the golden benchmark tasks — each task runs twice (bare prompt vs prompt+skill layer) with deterministic structural scoring, an optional declared-but-not-required LLM-judge slot, and a results ledger carrying per-task deltas plus confound notes.
license: MIT
compatibility: Requires plans/benchmark_tasks.py corpus (or equivalent task set) and an AGENT_CMD runner; verdicts are directional/stable/composite vocabulary — never proves-at-n=1.
metadata:
  risk_level: medium
  human_review_required: true
  external_io: true
  context_load: medium
---

# Golden Benchmark Runner

**Type:** Domain-pack skill (local comparison harness) — registered in the TeaPrompt source repo's domain-pack registry (`plans/validate_skill_examples.py` `DOMAIN_PACK_SKILLS`), not one of the nine frozen core workflow skills, and not selected by `reflective-dispatch` route rows; the host harness may invoke it directly.

## Purpose

Turn "did the skill layer help?" into a bounded, provider-neutral, locally-runnable comparison — not a CI gate, not a leaderboard. Each golden task runs twice (bare prompt vs prompt+skill layer), is scored by deterministic structural checks where possible, and lands in a results ledger with per-task deltas. Any skill-effect claim the ledger supports carries its confound notes; a composite measurement is never reported as an isolated skill effect.

## Module Contract

### Trigger

- The user asks to "compare baseline vs skill", "measure skill effect", "run the golden benchmark", or "prove the skill layer helps".
- A claim about skill utility needs evidence beyond fixture-shape validation or routing consistency.

### Inputs

1. Task subset (default: all 24; verification self-run: 2 tasks).
2. `AGENT_CMD` template + prompt-passing convention; `JUDGE_CMD` + rubric (optional).
3. Caps envelope: per-invocation timeout, max tasks, total spend; named approver.
4. Scorer scripts for selected tasks (stdlib-only, deterministic).

### Methods

1. **Task source reuse.** Import `BenchmarkSet` from `plans/benchmark_tasks.py` (24 golden tasks across 9 skills) — never duplicate the task list. The CI fixture-shape validator (`plans/validate_benchmark_fixture.py`) stays the CI gate; this runner is local-only and never runs in CI.
2. **Paired arms.** For each selected task, run arm C (control: bare prompt) and arm T (treatment: prompt + skill layer) against the same frozen fixture snapshot. Declare the exact treatment artifact and revision/hash, full text versus named excerpt, delivery slot, and composition rule in the run report; fix that rule and any task-to-skill mapping before the run. Control omits only that declared layer; all other setup stays matched. Alternate arm order per task (A: control-first; B: treatment-first), fresh contexts per invocation.
3. **Provider-neutral transport.** The agent under test is a shell template from `AGENT_CMD` (env), with a declared prompt-passing convention (`{prompt_file}` placeholder; stdin vs argv spelled out per provider). Bounded caps: per-invocation timeout, max task count, total spend envelope; human run/cost approval precedes any metered invocation.
4. **Deterministic structural scoring first.** Per-task scorer registry (`task id → scorer script`, e.g. arithmetic assertions like fixture `A-code/oracle.py`, required-section + substance checks like fixture `B-content/oracle.py`). Respect task-declared value types at the final scoring consumer, not just admission: an integer oracle rejects booleans and floats even when numeric equality holds. Functional correctness of executable candidates needs independently protected host-oracle results bound to the candidate hash and scorer executable/revision; candidate-authored `ok`, expected answers or error text are not that evidence. Tasks with no scorer get a generic structural heuristic (acceptance-criteria heading/keyword presence, after `plans/eval_harness.py` rubric style) and are marked `structural-heuristic-only`.
5. **Optional LLM-judge slot.** Declared interface (`JUDGE_CMD` env + rubric), never required. The ledger marks each score `structural` vs `judge-backed`; judge-backed scores name the judge model and rubric version.
6. **Hold fixture.** Preflight-hold fixtures (C-hold pattern: stale binding → exit 4, zero dispatch) are scored separately and excluded from the task-pair denominator: one control/treatment comparison per selected task, called a repair pair in a TASK-005-style repair pilot.
7. **Receipt and allocation discipline.** Preserve raw receipts; exclusive-create a fresh run namespace for a replay or corrected audit rather than overwriting prior evidence or regrading historical outputs under a changed oracle. Malformed or environment-incomplete invocations remain discard records; ticket-authorized re-runs charge the declared caps and never enter the pair denominator. Retain every allocated pair, including unrun or incomplete arms. Report allocated, completed and censored/incomplete totals separately; compute deltas only for pairs with two completed, scorable arms. A protected execution-error row is a completed candidate failure only with independent host attribution `error_origin='candidate'` and explicit boolean `censored=False`; oracle-side, unknown or missing attribution and cap-censored rows stay unscored (`score: null`). Candidate error text cannot declare censoring. An admitted complete failure takes precedence over a diagnostic error/timeout, but never overrides a blocked/no-dispatch containment hold.
8. **Measurement preflight.** Before attributing any delta to the skill layer, the run report names (a) the noise floor basis — repeated-baseline spread, or an explicit single-run caveat; (b) failure categorization — a delta is not attributable to the treatment until noise, grader error, harness failure, and task impossibility are ruled out; (c) selection-vs-report separation — the score that selected a winner is a selection statistic, not a reportable final gain; a final claim needs a pre-registered untouched evaluation.

### Output

- Results ledger (JSONL, one row per task-arm): task id, arm, agent identity + version, candidate hash, score (`null` when unscored — censored, incomplete, or oracle-side error — never a zero-score loss), `completion` (`completed` | `censored` | `incomplete`) plus `status_reason` (`scorer-verdict`, `cap-exhausted`, `oracle-error`, `hold-no-dispatch`, …), scorer executable path plus `scorer_revision` content hash (the pinned deterministic oracle; `semantic_scorer_person` is a separately named human role and stays `null` on structural rows), judge-backing flag, arm order, observed_at, caps envelope. Plus allocated/completed/censored pair totals, a per-task delta table for complete scorable pairs only, the declared treatment construction, and a confound block on every reported effect.
- Verdict vocabulary: `directional` (single run per arm), `stable` (repeated runs agree), `composite` (arms differ in more than guidance — see confounds). No `proves` language at n=1.

### Never

- Never duplicate the benchmark task list — import it from `plans/benchmark_tasks.py`.
- Never run this runner in CI, and never present it as a CI gate or leaderboard; it is local-only.
- Never report a composite measurement (arms differing in model, setup, or extraction) as an isolated skill effect — relabel `composite` or re-run with matched arms.
- Never claim `proves`, and never claim stability from a single run per arm — one run per arm is `directional` only.
- Never run a metered invocation without human cost approval and a caps envelope up front.
- Never silently drop discarded receipts, and never count discards in the denominator.
- Never count hold-fixture rows in the task-pair denominator.
- Never let a scorer that passes an empty or prompt-echoing candidate contribute a delta — mark `structural-heuristic-only` and refuse the delta.
- Never structurally score research-category tasks with no deterministic oracle — they are `judge-backed` or excluded.
- Never treat the `cat`-stub self-run as evidence of model utility — it verifies harness mechanics only.
- Never report a delta inside the declared noise floor as improvement — within-noise is not a demonstrated effect.
- Never cite a selection-validation score as a reportable final gain — selection and final measurements are separate populations; a final claim needs untouched final data.

### Escalation

- Fixture-shape regressions → `plans/validate_benchmark_fixture.py` (the CI gate owns shape; this runner does not).
- Routing-quality questions → the ROUTE-001/002/003 gates.
- Delivery containment questions → `governed-delivery`.
- Metered runs, billing, or production-adjacent execution → `reflective-risk` before the first billable call.
- Whether a comparison is needed at all → `reflective-minimality`.
- Multi-step orchestration around the run → `flow-control-generator` (this runner's ledger is that script's evidence).

### Failure signals

- Oracle/transport errors, diagnostic-only results or an incomplete/censored arm → preserve the receipt and mark the pair unscored, not a skill success/failure or zero-score delta.
- Treatment and control use different models without declaration → composite misreported as skill effect (hard stop; re-run with matched models or relabel `composite`).
- Scorer passes an empty or prompt-echoing candidate → scorer too weak; mark `structural-heuristic-only` and refuse the delta.
- Hold-fixture dispatches work → containment failure; halt the run.
- A delta is reported without a named noise-floor basis or with noise/grader/harness/task-impossibility unruled-out → measurement misreport; halt and repair the report before scoring.

### Verification

- Self-run on 2 tasks with a `cat`-stub `AGENT_CMD` (fixed candidate file, zero model spend): exercises transport plumbing, scorer execution, ledger append, and delta computation. Across two runs, deterministic candidates must reproduce byte-identical ledger rows after removing only `observed_at`; retain the original timestamped receipts and require every other field to match.
- Scorer check: each scorer must fail the broken fixture and pass the fixed fixture before it may score arms. For an integer arithmetic task, include a constant answer, a wrong unseen answer and numerically equal wrong-type answers as negatives; verify the final verdict rejects them. Exercise host-attributed completed errors, oracle/unknown errors and cap-censored rows separately; only complete scorable pairs contribute deltas.

## Evidence

- `reflective-prompt-library/plans/benchmark_tasks.py` — 24 golden tasks (`B001`–`B024`) across the 9 frozen workflow skills, each with `acceptance_criteria` and `expected_workflow`; header declares manual execution only, CI runs the fixture-shape validator.
- `reflective-prompt-library/plans/QUALITY_GATES_SUMMARY.md` §7 — benchmark set as fixture-gated (shape in CI, LLM comparisons optional local experiments); routing gates as fixture regression guards, not semantic-quality proofs.
- `reflective-prompt-library/plans/eval_harness.py` — deterministic rubric-scoring precedent (structural/content regex checks, pass/warn/fail → 100/50/0); the runner's structural scorers follow this pattern per task.
- `reflective-prompt-library/plans/runtime-skills-task001-ticket-2026-10-06.md` TASK-005 pilot — the working prototype this skill generalizes: A-code (broken `add`, arithmetic oracle), B-content (section + substance oracle; control failed on spinner-glyph pollution dropping the `## Next` heading), C-hold (stale → exit 4, scored separately, n=2 repair-pair denominator). Recorded confounds adopted as mandatory ledger fields: treatment ran a hosted model vs control a local small model (composite, not isolated skill effect); scorer not arm-blinded at extraction; single run per arm (directional only); provider invocations ran host-side under a declared sandbox exception.

## Honest Limits

- At one run per arm the ledger is directional single-case evidence; stability needs repeats the caps envelope may not fund.
- Unless both arms run the same model with fresh contexts and blinded extraction, the delta measures guidance + model + setup composite — the ledger says so explicitly.
- Structural scorers check form and frozen assertions, not semantic quality; the LLM-judge slot is declared but unvalidated, and same-model judging is one epistemic channel, not independent verification.
- The `cat`-stub self-run verifies harness mechanics only; it says nothing about model utility.
- Research-category tasks (e.g. `B005`) have no deterministic oracle; they are `judge-backed` or excluded, never structurally scored.

## Examples

Companion examples live at `<skills-root>/examples/golden-benchmark-runner.examples.md` when co-installed. They show ledger, delta-table, and verdict shapes with confound labeling, not proof that a skill effect was measured.

## Prompt Sources

*Provenance: TeaPrompt source-repository paths (`reflective-prompt-library/`), not runtime dependencies — the installed skill is self-contained.*

- `reflective-prompt-library/plans/benchmark_tasks.py` (24 golden tasks; manual-execution header)
- `reflective-prompt-library/plans/eval_harness.py` (deterministic rubric-scoring precedent)
- `reflective-prompt-library/plans/QUALITY_GATES_SUMMARY.md` (§7: fixture-gated benchmark set)
- `reflective-prompt-library/plans/runtime-skills-task001-ticket-2026-10-06.md` (TASK-005 pilot arms and confounds)
- `reflective-prompt-library/plans/validate_benchmark_fixture.py` (CI fixture-shape gate this runner never replaces)
