---
feature: route paraphrase evals
source_commit: 7d8de92
last_verified_at: 2026-09-24
verification_status: passing
---

# Route paraphrase evals

## Entry points

`reflective-prompt-library/plans/route_paraphrase_eval.py` runs a seeded
deterministic ParaphraseRouter over YAML fixtures:

```bash
P=reflective-prompt-library/plans
python3 $P/route_paraphrase_eval.py $P/route-001-paraphrase-eval.yaml
python3 $P/route_paraphrase_eval.py $P/route-002-holdout-eval.yaml
python3 $P/route_paraphrase_eval.py $P/route-003-adversarial-eval.yaml
```

## Observable outcomes

- Each prints per-group consistency + `✅ Eval passed: Phase-1 consistency
  threshold met`, exit 0.
- Current measured: 100.0% consistency on all three fixtures. This is a
  **regression-guard tier** result (seeded fixture), not proof of semantic
  routing — see `plans/QUALITY_GATES_SUMMARY.md`.
- Known low-confidence groups (ROUTE-003, still passing):
  `approved_spec_verify_not_implement_trap` ~0.45,
  `pack_vocab_implement_not_plan_trap` ~0.53. Confidence near the trace
  threshold is a weak spot, not a failure.

## Failure paths

- Consistency below the fixture's Phase-1 threshold → product regression in
  the router's keyword/boundary rules.
- A group flipping canonical workflow → product regression unless R8
  holdout-first procedure was followed (fixture updated first, with the
  failing phrase recorded).
- Missing YAML / parse error → harness failure.

## Evidence

Group name, consistency %, avg confidence. Results also land in gitignored
`plans/route-00X-results.json`.
