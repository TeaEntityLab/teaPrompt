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
## Declined to Judge
- <behavior set aside as out of scope> — <reason; who rules on it> (or "None")
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
## Traceability
| Acceptance Criteria | Artifact Evidence | Test Evidence | Status |
## Declined to Judge
- <behavior set aside as out of scope> — <reason; who rules on it> (or "None")
## Required Fixes
## Decision
## Residual Risks
```


## Example 3

Input:

```text
Review this PR description: "Refactored the cache layer; all edge cases tested and passing."
```

Expected mid-review Claims Ledger shape (illustrative rows showing ledger literals, not proof of this PR):

```markdown
| Claim | Checked How | Status |
|---|---|---|
| cache layer refactored; public API text unchanged (behavior preservation still unproven) | diff read (example); public API text compared | verified |
| all edge cases tested | test files in diff (example) | refuted (no new tests for eviction path) |
| tests passing | CI output read: example run showed suite green on 2026-09-30 (example) | verified |
```
