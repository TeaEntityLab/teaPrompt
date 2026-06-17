# AGENTS.md

## Mission

This repository uses Reflective Engineering Agent Protocol.

The agent must prioritize:

> Doing the right thing > doing things right.

Do not start implementation before understanding goal, scope, risk, and acceptance criteria.

---

## Required Workflow

For every non-trivial task:

1. Read relevant docs:
   - `reflective-prompt-library/02-engineering/task-start.md`
   - `reflective-prompt-library/02-engineering/spec-writer.md`
   - `reflective-prompt-library/02-engineering/usage-first.md`
   - `reflective-prompt-library/02-engineering/task-slicer.md`
   - `reflective-prompt-library/README.md`

   > **Note**: This template assumes a code-project structure and may need adaptation for your specific repository layout.

2. Before implementation, produce:
   - goal
   - assumptions
   - scope
   - acceptance criteria
   - failure conditions
   - plan
   - files likely to change

3. During implementation:
   - make small changes
   - preserve existing behavior unless instructed
   - write tests
   - do not delete or weaken tests
   - do not change acceptance criteria
   - do not hide failures

4. Before completion:
   - run available checks
   - report commands run
   - report test results
   - produce spec-to-code traceability
   - write `review/final-report.md`

---

## Human Review Required

Stop and request human review for:

- auth / permission changes
- database migrations
- destructive file operations
- privacy-sensitive data
- security-sensitive logic
- billing / cost changes
- public API changes
- production deployment
- ambiguous requirements that affect architecture

---

## Anti-cheating Rules

Never:

- delete failing tests
- skip tests without reporting
- weaken assertions
- update snapshots blindly
- change expected outputs to match broken behavior
- claim success without evidence
- invent logs, benchmarks, or tool results

---

## Context Engineering

Keep main context clean.

Prefer:

- reading only relevant files
- summarizing large files
- writing intermediate findings to disk
- using scripts for repetitive work
- returning final distilled reports

Avoid:

- dumping large raw data into chat
- relying on conversation memory for project state
- mixing unrelated tasks in one run

---

## Project Knowledge Layer

`PROJECT_KNOWLEDGE.md` is the project's curated *rationale* layer: why the
project believes what it believes, where it is going, and what it has learned.
It is **non-normative** — it never overrides this file or any `SKILL.md`.

Read-first rule:

- For non-trivial tasks touching architecture, workflow, governance, or an
  existing decision, read the relevant section of `PROJECT_KNOWLEDGE.md` before
  planning. No human invocation is required.

Binding-migration rule:

- This file (`AGENTS.md`) and `SKILL.md` files are the only sources of binding,
  must-follow rules. If something in `PROJECT_KNOWLEDGE.md` starts prescribing
  agent behavior, move it here instead of leaving it there.
- The separation is enforced mechanically by
  `plans/validate_project_knowledge.py`, which fails on normative language in
  `PROJECT_KNOWLEDGE.md` outside explanatory blockquotes.

Promotion path:

- `reflective-handoff-retro` may propose knowledge-promotion candidates
  (durable lessons, decisions). A candidate is promoted only with evidence of
  recurrence; one-off incidents stay in plans, not in `PROJECT_KNOWLEDGE.md`.

---

## Review Standard

Every final report must include:

1. Summary
2. Acceptance criteria status
3. Tests run
4. Files changed
5. Risks
6. Spec-to-code traceability
7. Remaining work
8. Human review needs

