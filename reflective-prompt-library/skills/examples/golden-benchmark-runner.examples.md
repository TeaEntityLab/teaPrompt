# golden-benchmark-runner — Examples

Companion examples for the domain-pack skill. These show expected ledger,
delta-table, and verdict shapes with confound labeling — not proof that a
skill effect was measured.

## Example 1 — Paired run with structural scorers (A-code shape)

Input:

```text
Run the golden comparison on 2 tasks with AGENT_CMD="run-agent --model <model> --prompt-file {prompt_file}", per-invocation timeout 120s, max 4 invocations, approver named.
```

Expected output shape:

```jsonl
{"task_id": "B001", "arm": "C", "agent": "<agent-id>", "agent_version": "<version>", "candidate_sha256": "<hash>", "score": 0, "scorer": "b001-arithmetic", "judge_backed": false, "arm_order": "control-first", "observed_at": "<utc>", "caps": {"timeout_s": 120, "max_tasks": 2, "spend": "<envelope>"}}
{"task_id": "B001", "arm": "T", "agent": "<agent-id>", "agent_version": "<version>", "candidate_sha256": "<hash>", "score": 100, "scorer": "b001-arithmetic", "judge_backed": false, "arm_order": "control-first", "observed_at": "<utc>", "caps": {"timeout_s": 120, "max_tasks": 2, "spend": "<envelope>"}}
```

```markdown
## Delta table (T − C)
- B001: raw structural difference +100 (scorer b001-arithmetic) — withheld as a skill-effect claim

## Treatment construction
- artifact: `<skills-root>/reflective-brief/SKILL.md`, revision/hash pinned in the run manifest
- payload: full skill text; delivery slot: user prompt
- composition: base task text, newline, then skill text; control receives only the base text
- task-to-skill mapping and composition rule fixed before either arm runs; model, CLI, fixture, and caps matched

## Measurement preflight
- noise_floor_basis: single-run caveat (one run per arm; no repeated-baseline spread)
- failure_categorization: unresolved — noise, grader error, harness failure, and task impossibility are not ruled out, so the difference is not attributed to the skill layer
- selection_vs_final: not-a-final-claim (this score was not an untouched final evaluation)

## Confounds
- single run per arm → verdict `directional`, not stable, never `proves`
- scorer extraction not arm-blinded (recorded; blind on repeat)
```

The scorer passed its check first: it fails the broken fixture
(`return a - b`) and passes the fixed fixture (`return a + b`).
The ledger may record the raw scores. It may not call +100 an improvement:
a delta with an unresolved failure categorization is a measurement misreport.

## Example 2 — Composite arms must be relabeled, not reported as skill effect

Input:

```text
Treatment ran <model-t> and control ran <model-c>. Report the delta.
```

Expected output shape:

```markdown
## Delta table (T − C)
- B002: raw difference +50 — verdict `composite`, not an isolated skill effect and not an improvement

## Measurement preflight
- noise_floor_basis: single-run caveat (one run per arm; no repeated-baseline spread)
- failure_categorization: not attributable — arms differ in model, so harness/setup confound is not ruled out
- selection_vs_final: not-a-final-claim

## Confounds
- treatment model <model-t> vs control model <model-c>: guidance + model + setup composite
- single run per arm → `directional` only
```

Hard stop applied: the run is NOT reported as an isolated skill effect.
Re-run with matched models and fresh contexts, or keep the `composite` label.

## Example 3 — Hold fixture scored separately; discards kept for audit

Input:

```text
Score the C-hold fixture row and one malformed invocation (missing prompt file).
```

Expected output shape:

```markdown
## Hold fixture
- C-hold: stale binding → exit 4, zero dispatch — scored separately, excluded
  from the task-pair denominator (two control/treatment task comparisons, n=2, not n=3).

## Discards
- task B003 arm T: malformed (missing prompt file) → re-run correctly;
  discarded receipt kept under evidence/discards/, never counted in the denominator.
```

Had the hold fixture dispatched work, the run would halt (containment failure).

## Example 4 — Deterministic self-run with distinct timestamps

Two stub runs produce identical candidates and scores, but different
`observed_at` values. Keep both raw ledgers. Compare rows after removing only
that timestamp field: equality passes; a changed candidate hash, score,
scorer, arm order, identity, or caps fails. Timestamp normalization must not
hide a measurement or setup difference. This is a mechanics check, not a
model-utility comparison.
