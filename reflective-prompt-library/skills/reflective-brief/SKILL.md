---
name: reflective-brief
description: Use this to start non-trivial tasks, clarify real goals, define assumptions, scope, acceptance criteria, falsifiability, and the minimal next step before planning or implementation. Especially useful when a request is broad but safe to proceed with explicit assumptions.
license: MIT
---

# Reflective Brief

## Purpose

Turn a request into a small, testable task brief before deeper work.

## Workflow

1. Identify the real goal.
2. Separate problem, symptom, and proposed solution.
3. State assumptions and unknowns.
4. Define scope in / scope out.
5. Define inputs and outputs.
6. Define failure conditions.
7. Define acceptance criteria.
8. Define falsifiability: what evidence would prove this direction wrong.
9. Choose the minimal next step.

## Output

```markdown
## Goal

## Why

## Assumptions

## Scope
- In:
- Out:

## Inputs / Outputs

## Failure Conditions

## Acceptance Criteria

## Falsifiability

## Minimal Plan

## Human Review Triggers

## Next Action
```

## Operating Rules

- Ask only when missing information changes safety, architecture, cost, privacy, data loss, or irreversibility.
- If ambiguity is safe, proceed with explicit assumptions.
- Do not expose hidden chain-of-thought; provide concise reasoning summaries and clean artifacts.

## Prompt Sources

Use these library prompts for exact wording when needed:

- `00-core/core-short.md`
- `02-engineering/task-start.md`
- `01-thinking/why-what-how-done.md`
- `01-thinking/falsifiability.md`
