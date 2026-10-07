# `reflective-spec-plan` Examples

## Example 1

Input:

```text
Create a spec and task plan for migrating file uploads to signed URLs.
```

Expected output shape:

```markdown
## Definition of Ready check
## Spec
- Version: <spec version>; a mid-task change bumps it and marks spec_version-keyed artifacts stale
- Acceptance record: a named accepter closes it; execution success does not
## Usage
## Task Plan
## Definition of Done check
```

## Example 2

Input:

```text
Write tickets for adding audit logging to admin actions.
```

Expected output shape:

Tickets-only mode writes the TASK template, not titles alone. TASK-002 and TASK-003 use the same fields.

```markdown
### TASK-001: logging schema and event contract
- Goal:
- Spec Version:
- Scope:
- Inputs:
- Outputs:
- Dependencies:
- Authority / Data Boundary:
- Runtime / Tool Gates:
- Acceptance Criteria:
- Tests:
- Files likely touched:
- Risk:
- Parallelizable: yes/no
- Human Review Required: yes/no
### TASK-002: backend write path
### TASK-003: query and review UI
```
