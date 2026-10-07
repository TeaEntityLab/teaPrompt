# `reflective-risk` Examples

## Example 1

Input:

```text
We need to run a production migration that changes permission checks.
```

The contract Output for a production migration. `Sink Inventory` and `Unattended Envelope` are recorded before any dry-run. Backup, dry-run, rollback, and approval stay in the gate.

```markdown
## Goal
## Stakeholders
## Assets at Risk
## Threat Model
## Assumption Audit
## Evidence Check
## Authority / Tool Boundary
## Effect Recovery Decision
## Failure Modes
## Worst-case Scenario
## Sink Inventory
## Unattended Envelope
## Safe Dry-run Plan
## Rollback Plan
## Bounded Execution
## Audit Log Plan
## Human Review Required
## Human Approval Gate
## Acceptance Criteria
## Go / No-go Decision
```

## Example 2

Input:

```text
Delete legacy customer records older than 5 years.
```

The contract Output for a destructive delete, before execution. Dry-run, rollback, and approval are part of the gate. `Sink Inventory` and `Unattended Envelope` are recorded before any dry-run.

```markdown
## Goal
## Stakeholders
## Assets at Risk
## Threat Model
## Assumption Audit
## Evidence Check
## Authority / Tool Boundary
## Effect Recovery Decision
## Failure Modes
## Worst-case Scenario
## Sink Inventory
## Unattended Envelope
## Safe Dry-run Plan
## Rollback Plan
## Bounded Execution
## Audit Log Plan
## Human Review Required
## Human Approval Gate
## Acceptance Criteria
## Go / No-go Decision
```
