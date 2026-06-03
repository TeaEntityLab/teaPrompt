---
name: reflective-spec-plan
description: Use this to turn a requirement into a practical spec, usage-first design, and small reviewable task plan. Trigger when the user asks for a spec, PRD, tickets, implementation plan, workflow plan, or wants to avoid building the wrong thing.
license: MIT
risk_level: low
human_review_required: false
external_io: false
---

# Reflective Spec Plan

## Purpose

Produce just enough specification to guide execution and review. Avoid beautiful but unused specs.

## Module Contract

Trigger:
- Use when the user asks for a spec, PRD, implementation plan, workflow plan, usage design, or reviewable task slices.

Methods:
- Definition of Ready
- Usage-first design
- Acceptance criteria design
- Vertical task slicing
- Definition of Done

Output:
- When file tools are available, write `spec.md`, `usage.md`, and `task-plan.md`; otherwise use the same headings inline.
- For tickets, use the `TASK-001` template with dependencies, tests, risk, and Human Review flags.

Never:
- Do not turn every idea into a workflow engine.
- Do not plan implementation details before acceptance criteria exist.
- Do not hide incomplete requirements as polished prose.
- Do not pass incomplete planning artifacts to implementation just to start faster.

Escalation:
- Route missing Definition of Ready inputs to `reflective-brief`.
- Route high-risk plans to `reflective-risk` before execution.

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
