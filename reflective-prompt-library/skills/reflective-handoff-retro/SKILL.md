---
name: reflective-handoff-retro
description: Use this when a task needs context handoff, session transfer, retrospective, reusable memory, process learning, or conversion of repeated experience into rules, checklists, skills, scripts, or tests.
license: MIT
risk_level: low
human_review_required: false
external_io: false
context_load: medium
---

# Reflective Handoff Retro

**Type:** Prompt-level workflow

## Purpose

Preserve only the context needed for continuation and turn repeated lessons into maintainable process improvements.

## Module Contract

Trigger:
- Use when work needs session transfer, agent handoff, context compaction, retrospective, reusable memory, or conversion of repeated patterns into rules, skills, scripts, or tests.

Methods:
- Context distillation
- Decision capture
- Remaining-work inventory
- Authority boundary preservation
- Retrospective root-cause analysis
- Anti-regression rule extraction

Output:
- For handoff, output the handoff template with current state, decisions, artifacts, trust boundaries, risks, blockers, tests, and next action.
- For retro, output the retro template with process failures, reusable rules, and improvement candidates.
- When durable project knowledge may have formed, append the Project-Knowledge Promotion Candidates contract below.

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
## Trust Boundaries / External Data
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
- Trust-boundary lesson, if external data, tools, or side effects contributed to the issue

Do not turn one-off accidents into permanent bureaucracy.

## Project-Knowledge Promotion Contract

Use this only when the repository has a project-knowledge layer or the user asks
to establish one. A retro may *propose* long-term knowledge; it does not silently
promote it.

```markdown
## Project-Knowledge Promotion Candidates

### Candidate: <short name>
- Claim / Procedure:
- Evidence of recurrence: <at least two independent occurrences, or one explicit project decision>
- Destination: governing principle | current direction | durable lesson | decision index | project-local skill | skill + verifier/test | runtime/orchestration | no change
- Authority class: project-design judgement | agent operating rule
- Proposed action: add | amend | supersede | retire | keep in draft
- Human approval: required | explicitly granted in this task | pending
- Source artifacts: <plans, tests, commits, incidents, or decisions>
- Review / retirement trigger:
```

Promotion rules:

- `project-design judgement` belongs in the project-knowledge artifact. It may
  guide product and architecture decisions but cannot authorize agent actions.
- `agent operating rule` belongs in `AGENTS.md` or the relevant `SKILL.md`, not
  in project knowledge.
- A repeated operation becomes a `project-local skill` candidate only when its
  recurrence, inputs, outputs, failure signals, and verification are concrete.
  Promotion requires human confirmation because executable knowledge has a
  larger failure surface than prose.
- The nine core workflow skills are frozen — frozen means gated, not never: a new core skill needs recurrence evidence and explicit human approval; otherwise fold the material into an existing skill, lens, verifier/test, or no-change record.
- Prefer `skill + verifier/test` when the task recurs and objective deterministic pass/fail exists; use runtime/orchestration only for persistence, replay, cancellation, idempotency, role isolation, enforced transitions, side-effect gating, or memory/identity ACLs that prompt/skill/verifier cannot guarantee.
- A one-off event remains in its plan, retro, or draft. Do not manufacture a
  permanent lesson merely to fill the knowledge file.
- Superseded decisions remain traceable through the decision index; record the
  transition instead of deleting the old rationale.

## Prompt Sources

- `03-context/context-handoff.md`
- `04-agent/retro.md`
- `01-thinking/socratic-reviewer.md`
- `04-agent/memory-consolidation.md`
- `04-agent/artifact-promotion.md`
- `04-agent/runtime-trust-boundary.md`
- `06-repo/PROJECT_KNOWLEDGE.template.md`
