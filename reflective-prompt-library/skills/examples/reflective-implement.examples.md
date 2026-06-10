# `reflective-implement` Examples

## Example 1

Input:

```text
Implement retry logic for transient 503 responses in payment status polling.
```

Expected output shape:

```markdown
## Goal
## Files Changed
## Implementation Summary
## Acceptance Criteria Status
## Tests / Checks Run
## Failures or Skipped Checks
## Residual Risks
## Next Action
```

## Example 2

Input:

```text
Tests are failing after my refactor. Help recover.
```

Expected output shape:

```markdown
## Step
## Evidence
## Error Type
## Root Cause
## Correction
## Next Action
## Verification
## Anti-regression Rule
```

## Example 3

Input:

```text
Migrate the three report exporters to the new formatter API. Keep output identical.
```

Expected mid-task State Ledger shape:

```markdown
| Item | Status | Evidence |
|---|---|---|
| csv exporter migrated | verified | exporter tests pass, diff reviewed |
| pdf exporter migrated | failed | golden file mismatch on footer |
| xlsx exporter migrated | pending | |
| output identical for all three | pending | blocked on pdf fix |
```
