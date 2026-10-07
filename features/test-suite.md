---
feature: governance test suite
source_commit: 13fc95c
last_verified_at: 2026-10-07
verification_status: passing
---

# Governance test suite

## Entry points

- `reflective-prompt-library/plans/tests/` — governance records, registry
  cardinality, cheatsheet parity, boundary quick cues, adoption-state
  contracts, and emitted-script consumer regressions.

Historical snapshots: the generation-time baseline (2026-09-24, `7147e91`)
had 99 files and 1290 tests; the 2026-10-02 drive reported 106 files and
1358 passing tests.
`source_commit` now names the committed base; the verified working tree
includes the current runtime-review and consumer-regression repairs.
This map refresh changes documentation, not test code. Run receipts and
limits are recorded in `review/final-report.md`.

## Drive

```bash
python3 -m pytest reflective-prompt-library/plans/tests/ -q
```

Observed tail on 2026-10-07: `1533 passed`. The invariant is **0 failures**,
not the exact count; re-verify after covered source changes.

Per-area selection uses `-k` or a file path, e.g.:

```bash
python3 -m pytest reflective-prompt-library/plans/tests/test_ga_skills_coverage_panel_record.py -q
```

## Observable outcomes

- Exit 0, all tests pass.
- Any `FAILED` line names the pinned contract that broke.

## Failure paths

- A failing `test_*` = product regression in the pinned surface (or a
  deliberately changed contract — then the test change must accompany the
  source change in the same commit).
- `ModuleNotFoundError` / collection errors = harness failure (pytest missing
  or wrong cwd).

## Evidence

Paste the pytest summary line plus any FAILED test ids.
