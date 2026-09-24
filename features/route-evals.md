---
feature: route paraphrase evals
source_commit: 7147e91
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
- Group confidence is not a pass criterion. A route that is **contested**
  (runner-up within one point) is capped at 0.45 and its trace names the
  alternate — that is the gate working, not a failure. Lowest measured at
  `7147e91`: ROUTE-003 `review_led_cut_not_review_trap` 0.45 (minimality vs
  review, contested and visible), `pack_vocab_implement_not_plan_trap` 0.53
  (single signal, uncontested). ROUTING_CONTRACT R13 moved review-led
  spec/plan inspection from 0.45 to 0.80.

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
