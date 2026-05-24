---
name: reflective-spec-plan
description: Use this to turn a requirement into a practical spec, usage-first design, and small reviewable task plan. Trigger when the user asks for a spec, PRD, tickets, implementation plan, workflow plan, or wants to avoid building the wrong thing.
---

# Reflective Spec Plan

## Purpose

Produce just enough specification to guide execution and review. Avoid beautiful but unused specs.

## Workflow

1. Write the spec.
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

2. Write usage first.
   - Most common scenarios
   - CLI / API / UI examples
   - Success examples
   - Error examples
   - Confusing parts
   - Design issues revealed by usage

3. Slice work.
   - Vertical slices first
   - 30-120 minute tickets
   - One concern per ticket
   - Dependencies explicit
   - Tests per ticket
   - Human Review flag per ticket

4. Stop at the smallest plan that can be executed and reviewed.

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

## Prompt Sources

- `02-engineering/spec-writer.md`
- `02-engineering/usage-first.md`
- `02-engineering/task-slicer.md`
- `04-agent/workflow-engine.md`

