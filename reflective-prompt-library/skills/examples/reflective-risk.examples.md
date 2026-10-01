# `reflective-risk` Examples

## Example 1

Input:

```text
We need to run a production migration that changes permission checks.
```

Proportional subset of the contract Output showing the safety spine for a production migration; a real gate emits the full contract Output. `Sink Inventory` and `Unattended Envelope` are recorded before any dry-run.

```markdown
## Threat Model
## Authority / Tool Boundary
## Sink Inventory
## Unattended Envelope
## Safe Dry-run Plan
## Rollback Plan
## Bounded Execution
## Audit Log Plan
## Human Review Required
## Human Approval Gate
## Go / No-go Decision
```

## Example 2

Input:

```text
Delete legacy customer records older than 5 years.
```

Proportional subset of the contract Output for pre-execution scoping; before any dry-run, record `Sink Inventory` and `Unattended Envelope` per the contract.

```markdown
## Assets at Risk
## Authority / Tool Boundary
## Sink Inventory
## Unattended Envelope
## Failure Modes
## Worst-case Scenario
## Human Review Required
## Acceptance Criteria
```
