---
name: reflective-handoff-retro
description: Use this when a task needs context handoff, session transfer, retrospective, reusable memory, process learning, or conversion of repeated experience into rules, checklists, skills, scripts, or tests.
license: MIT
---

# Reflective Handoff Retro

## Purpose

Preserve only the context needed for continuation and turn repeated lessons into maintainable process improvements.

## Module Contract

Trigger:
- Use when work needs session transfer, agent handoff, context compaction, retrospective, reusable memory, or conversion of repeated patterns into rules, skills, scripts, or tests.

Methods:
- Context distillation
- Decision capture
- Remaining-work inventory
- Retrospective root-cause analysis
- Anti-regression rule extraction

Output:
- For handoff, output the handoff template with current state, decisions, artifacts, risks, blockers, tests, and next action.
- For retro, output the retro template with process failures, reusable rules, and improvement candidates.

Never:
- Do not dump raw context when a compact continuation brief is enough.
- Do not turn one-off accidents into permanent bureaucracy.
- Do not omit blockers, skipped checks, or Human Review requirements.

Escalation:
- Route active implementation back to `reflective-implement`.
- Route unresolved high-risk blockers to `reflective-risk`.

## Handoff Workflow

Use when switching tools, agents, models, sessions, or context windows.

```markdown
## Goal
## Current State
## Decisions Made
## Assumptions
## Files / Artifacts
## Completed Work
## Remaining Work
## Risks
## Blockers
## Acceptance Criteria
## Commands / Tests Run
## Next Recommended Action
## Do Not Do
## Human Review Required
```

## Retro Workflow

Use after task completion:

```markdown
## What Went Well
## What Went Wrong
## Misunderstandings
## Wrong Assumptions
## Token or Time Waste
## Weak Gates
## Test Adequacy
## Overengineering / Underspecification
## Reusable Rules
## Skill / Script / Test Candidates
## Next Process Improvement
```

## Memory Consolidation

Only institutionalize repeated patterns:

- Repeated pattern
- Root cause
- New rule or checklist
- New skill or script candidate
- Anti-regression test

Do not turn one-off accidents into permanent bureaucracy.

## Prompt Sources

- `03-context/context-handoff.md`
- `04-agent/retro.md`
- `04-agent/memory-consolidation.md`
