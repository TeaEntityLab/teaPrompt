# `reflective-review` Examples

## Example 1

Input:

```text
Review this diff against acceptance criteria and tests.
```

Expected output shape:

```markdown
## Findings
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

