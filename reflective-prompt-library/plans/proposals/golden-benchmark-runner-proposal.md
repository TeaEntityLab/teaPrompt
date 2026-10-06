---
name: golden-benchmark-runner
description: Use to run a baseline-vs-skill comparison over the golden benchmark tasks — each task runs twice (bare prompt vs prompt+skill layer) with deterministic structural scoring, an optional declared-but-not-required LLM-judge slot, and a results ledger carrying per-task deltas plus confound notes.
license: MIT
metadata:
  risk_level: medium
  human_review_required: true
  external_io: true
  context_load: medium
---

# Golden Benchmark Runner

**Status:** ADOPTED 2026-10-06 — registered domain pack; live contract at `skills/golden-benchmark-runner/SKILL.md`. This file is the admission record.

**Type:** Domain-pack skill proposal — inert until admission review. NOT registered; NOT edited into `skill-map.md`.

## Purpose

Turn "did the skill layer help?" into a bounded, provider-neutral, locally-runnable comparison — not a CI gate, not a leaderboard. Each golden task runs twice (bare prompt vs prompt+skill layer), is scored by deterministic structural checks where possible, and lands in a results ledger with per-task deltas. Any skill-effect claim the ledger supports must carry its confound notes; a composite measurement is never reported as an isolated skill effect.

## Module Contract

Trigger:

- The user asks to "compare baseline vs skill", "measure skill effect", "run the golden benchmark", or "prove the skill layer helps".
- A claim about skill utility needs evidence beyond fixture-shape validation or routing consistency.

Methods:

- Task source reuse: import `BenchmarkSet` from `plans/benchmark_tasks.py` (24 golden tasks across 9 skills) — never duplicate the task list. The CI fixture-shape validator (`plans/validate_benchmark_fixture.py`) stays the CI gate; this runner is local-only and never runs in CI.
- Paired arms: for each selected task, run arm C (control: bare prompt) and arm T (treatment: prompt + skill layer) against the same frozen fixture snapshot. Alternate arm order per task (A: control-first; B: treatment-first), fresh contexts per invocation.
- Provider-neutral transport: the agent under test is a shell template from `AGENT_CMD` (env), with a declared prompt-passing convention (`{prompt_file}` placeholder; stdin vs argv spelled out per provider — TASK-004 receipts show ollama takes stdin while devin/cursor-agent/agy take CLI argv flags). Bounded caps: per-invocation timeout, max task count, total spend envelope; human run/cost approval precedes any metered invocation.
- Deterministic structural scoring first: per-task scorer registry (`task id → scorer script`, e.g. arithmetic assertions like fixture `A-code/oracle.py`, required-section + substance checks like fixture `B-content/oracle.py`). Tasks with no scorer get a generic structural heuristic (acceptance-criteria heading/keyword presence, after `plans/eval_harness.py` rubric style) and are marked `structural-heuristic-only`.
- Optional LLM-judge slot: declared interface (`JUDGE_CMD` env + rubric), never required. Ledger marks each score `structural` vs `judge-backed`; judge-backed scores name the judge model and rubric version.
- Hold arm: preflight-hold fixtures (C-hold pattern: stale binding → exit 4, zero dispatch) are scored separately and excluded from the repair-pair denominator.
- Discard discipline: malformed or environment-incomplete invocations are re-run correctly and the discarded receipts are kept for audit — never silently dropped, never counted in the denominator.

Output:

- Results ledger (JSONL, one row per task-arm): task id, arm, agent identity + version, candidate hash, score, scorer id, judge-backing flag, arm order, observed_at, caps envelope. Plus a per-task delta table (T − C) and a confound block (below) on every reported effect.
- Verdict vocabulary: `directional` (single run per arm), `stable` (repeated runs agree), `composite` (arms differ in more than guidance — see confounds). No `proves` language at n=1.

Escalation:

- Human review required before any metered run (cost approval + caps envelope); `human_review_required: true` fronts this, not the content risk.
- Route fixture-shape regressions to `validate_benchmark_fixture.py`; routing-quality questions to the ROUTE-001/002/003 gates; delivery containment to `governed-delivery`.

Inputs:

- Task subset (default: all 24; verification self-run: 2 tasks).
- `AGENT_CMD` template + prompt-passing convention; `JUDGE_CMD` + rubric (optional).
- Caps envelope: per-invocation timeout, max tasks, total spend; named approver.
- Scorer scripts for selected tasks (stdlib-only, deterministic).

Failure signals:

- Either arm errors on all tasks → transport misconfiguration, not a skill finding.
- Treatment and control use different models without declaration → composite misreported as skill effect (hard stop; re-run with matched models or relabel `composite`).
- Scorer passes an empty or prompt-echoing candidate → scorer too weak; mark `structural-heuristic-only` and refuse the delta.
- Hold-fixture dispatches work → containment failure; halt the run.

Verification:

- Self-run on 2 tasks with a `cat`-stub `AGENT_CMD` (fixed candidate file, zero model spend): exercises transport plumbing, scorer execution, ledger append, and delta computation. Deterministic candidates must reproduce byte-identical ledger rows across two runs.
- Scorer check: each scorer must fail the broken fixture and pass the fixed fixture (A-code pattern: `return a - b` fails, `return a + b` passes) before it may score arms.

## Evidence

- `reflective-prompt-library/plans/benchmark_tasks.py` — 24 golden tasks (`B001`–`B024`) across the 9 frozen workflow skills, each with `acceptance_criteria` and `expected_workflow`; header declares manual execution only, CI runs the fixture-shape validator.
- `reflective-prompt-library/plans/QUALITY_GATES_SUMMARY.md` §7 — benchmark set as fixture-gated (shape in CI, LLM comparisons optional local experiments); routing gates as fixture regression guards, not semantic-quality proofs.
- `reflective-prompt-library/plans/eval_harness.py` — deterministic rubric-scoring precedent (structural/content regex checks, pass/warn/fail → 100/50/0); the runner's structural scorers follow this pattern per task.
- `reflective-prompt-library/plans/runtime-skills-task001-ticket-2026-10-06.md` TASK-005 pilot — the working prototype this proposal generalizes: A-code (broken `add`, arithmetic oracle), B-content (section + substance oracle; control failed on spinner-glyph pollution dropping the `## Next` heading), C-hold (stale → exit 4, scored separately, n=2 repair-pair denominator). Recorded confounds adopted as mandatory ledger fields: treatment ran `devin swe-2-max` vs control `ollama qwen2.5-coder:1.5b` (composite, not isolated skill effect); scorer not arm-blinded at extraction; single run per arm (directional only); provider invocations ran host-side under a declared sandbox exception.
- Dry-run receipts at `/tmp/teaprompt-dryrun/host-task/`: `fixtures/{A-code,B-content,C-hold}/`, `evidence/task005/{A,B}-*.out`, `evidence/task004/` (per-provider transport + identity receipts).

## Honest Limits

- At one run per arm the ledger is directional single-case evidence; stability needs repeats the caps envelope may not fund.
- Unless both arms run the same model with fresh contexts and blinded extraction, the delta measures guidance + model + setup composite — the ledger says so explicitly.
- Structural scorers check form and frozen assertions, not semantic quality; the LLM-judge slot is declared but unvalidated, and same-model judging is one epistemic channel, not independent verification.
- The `cat`-stub self-run verifies harness mechanics only; it says nothing about model utility.
- Research-category tasks (e.g. `B005`) have no deterministic oracle; they are `judge-backed` or excluded, never structurally scored.
