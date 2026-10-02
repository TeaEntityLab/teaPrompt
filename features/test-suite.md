---
feature: governance test suite
source_commit: f0f986d98af86702c5ecacac6daf095a06849686
last_verified_at: 2026-10-02
verification_status: passing
---

# Governance test suite

## Entry points

- `reflective-prompt-library/plans/tests/` — 106 `test_*.py` files; the
  2026-10-02 verification drive reported 1358 passing tests. Pins governance
  records, registry cardinality, cheatsheet parity, boundary quick cues and
  adoption-state contracts.

Generation-time baseline (2026-09-24, `7147e91`): 99 files and 1290 tests.
The metadata now names the current committed source baseline; this repair
changes covered documentation, not test code. Run receipts and limits are
recorded in `review/final-report.md`.

## Drive

```bash
python3 -m pytest reflective-prompt-library/plans/tests/ -q
```

Observed tail on 2026-10-02: `1358 passed`. The invariant is **0 failures**,
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
