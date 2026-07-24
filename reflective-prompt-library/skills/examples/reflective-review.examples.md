# `reflective-review` Examples

## Example 1

Input:

```text
Review this diff against acceptance criteria and tests.
```

Expected output shape:

```markdown
## Findings
- <file>:L<line>: <severity> — <defect>; failure scenario or violated invariant: <reachable evidence>
## Traceability
| Acceptance Criteria | Artifact Evidence | Test Evidence | Status |
## Required Fixes
## Decision
## Residual Risks
```

## Example 2

Input:

```text
Review this plan and tell me if we are overengineering.
```

Expected output shape:

```markdown
Mode: Plan/Spec Review
## Findings
- missing gate / strictness mismatch / unnecessary workflow depth
## Decision
```


## Example 3

Input:

```text
Review this PR description: "Refactored the cache layer; all edge cases tested and passing."
```

Expected mid-review Claims Ledger shape:

```markdown
| Claim | Checked How | Status |
|---|---|---|
| cache layer refactored, behavior preserved | diff read; public API unchanged | verified |
| all edge cases tested | test files in diff | refuted (no new tests for eviction path) |
| tests passing | CI run link | verified |
```
