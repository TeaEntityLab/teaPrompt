# `reflective-risk` Examples

## Example 1

Input:

```text
We need to run a production migration that changes permission checks.
```

Expected output shape:

```markdown
## Threat Model
## Authority / Tool Boundary
## Safe Dry-run Plan
## Rollback Plan
## Bounded Execution
## Audit Log Plan
## Human Approval Gate
## Go / No-go Decision
```

## Example 2

Input:

```text
Delete legacy customer records older than 5 years.
```

Expected output shape:

```markdown
## Assets at Risk
## Authority / Tool Boundary
## Failure Modes
## Worst-case Scenario
## Human Review Required
## Acceptance Criteria
```
