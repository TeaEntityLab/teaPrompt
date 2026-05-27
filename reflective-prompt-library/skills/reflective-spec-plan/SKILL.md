---
name: reflective-spec-plan
description: Use this to turn a requirement into a practical spec, usage-first design, and small reviewable task plan. Trigger when the user asks for a spec, PRD, tickets, implementation plan, workflow plan, or wants to avoid building the wrong thing.
license: MIT
---

# Reflective Spec Plan

## Purpose

Produce just enough specification to guide execution and review. Avoid beautiful but unused specs.

## Workflow

1. Validate entry criteria (Definition of Ready).
   - Goal exists
   - Intended outcome exists
   - Scope and acceptance criteria are at least minimally defined
   - Known high-risk constraints are identified
   - If these are missing, route to `reflective-brief` first

2. Write the spec.
   - Problem
   - Goals
   - Non-goals
   - Actors
   - Inputs / outputs
   - Functional requirements
   - Non-functional requirements
   - Edge cases
   - Failure modes
   - Open questions

3. Write usage first.
   - Most common scenarios
   - CLI / API / UI examples
   - Success examples
   - Error examples
   - Confusing parts
   - Design issues revealed by usage

4. Slice work.
   - Vertical slices first
   - 30-120 minute tickets
   - One concern per ticket
   - Dependencies explicit
   - Tests per ticket
   - Human Review flag per ticket

5. Define completion checks (Definition of Done for planning).
   - Spec has measurable acceptance criteria
   - Usage examples cover normal and error paths
   - Task slices are independently testable
   - Human Review points are explicit

6. Stop at the smallest plan that can be executed and reviewed.

## Artifact Output

When file tools are available, write:

- `spec.md`
- `usage.md`
- `task-plan.md`

When chat-only, use the same headings inline.

## Ticket Template

```markdown
### TASK-001: <name>
- Goal:
- Scope:
- Inputs:
- Outputs:
- Dependencies:
- Acceptance Criteria:
- Tests:
- Files likely touched:
- Risk:
- Parallelizable: yes/no
- Human Review Required: yes/no
```

## Guardrails

- Do not turn every idea into a workflow engine.
- Do not plan implementation details before acceptance criteria exist.
- Mark unknowns instead of hiding them in vague wording.
- Do not pass incomplete planning artifacts to implementation just to "start coding faster."

## Prompt Sources

- `02-engineering/spec-writer.md`
- `02-engineering/usage-first.md`
- `02-engineering/task-slicer.md`
- `04-agent/workflow-engine.md`
