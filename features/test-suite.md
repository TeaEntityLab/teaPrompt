---
feature: governance test suite
source_commit: c1cdf14
last_verified_at: 2026-09-23
verification_status: passing
---

# Governance test suite

## Entry points

- `reflective-prompt-library/plans/tests/` — 103 test files, 1287 tests at
  generation time. Pins governance records, registry cardinality, cheatsheet
  parity, boundary quick cues, and adoption-state contracts.

## Drive

```bash
python3 -m pytest reflective-prompt-library/plans/tests/ -q
```

Expected tail: `1287 passed` (count grows as tests are added — the invariant
is **0 failures**, not the exact count).

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
