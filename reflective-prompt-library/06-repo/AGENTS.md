# AGENTS.md

## Purpose

Repository-level harness policy for reflective engineering agents. Primary workflow surfaces: `reflective-dispatch`, `reflective-implement`, and `reflective-spec-plan`. Pairs with `01-thinking/why-what-how-done.md`, `01-thinking/critical-thinking-check.md`, and `01-thinking/socratic-reviewer.md`.

## Scope

- In scope: strictness-first routing, nine frozen workflow skills, evidence-backed completion, project-knowledge authority boundary.
- Out of scope: multi-agent runtime, tenth core skill without promotion gate, silent rigor downgrade.

## Acceptance Criteria

- Non-trivial tasks produce goal, scope, acceptance criteria, and test-backed completion evidence.
- High-blast-radius work stops for human review before irreversible action.

## Falsifiability

Name one task that would fail if this harness policy were ignored at session start.

## Human Review

Escalate to `reflective-risk` for irreversible or high-blast-radius work; see **Human Review Required** below for category triggers.

## Mission

This repository uses Reflective Engineering Agent Protocol.

The agent must prioritize:

> Doing the right thing > doing things right.

Do not start implementation before understanding goal, scope, risk, and acceptance criteria.

---

## Harness Policy (Nine Skills)

TeaPrompt workflow skills are **natural-language harness policy** — not a multi-agent
runtime. For non-trivial routing, governance, or skill-selection work:

1. **Strictness before skills** — pick L1–L6 first, then the smallest workflow.
   See [README.md](../README.md#strictness-before-skills) and [GLOSSARY.md](../GLOSSARY.md).
2. **Nine frozen workflow skills** — do not add a tenth core skill without the
   three-recurrence promotion gate ([PROJECT_KNOWLEDGE.md](../PROJECT_KNOWLEDGE.md)).
3. **Fast routing** — [skills/SKILL_TRIGGER_CHEATSHEET.md](../skills/SKILL_TRIGGER_CHEATSHEET.md)
   (繁中: [`.zh-TW.md`](../skills/SKILL_TRIGGER_CHEATSHEET.zh-TW.md)).
4. **Fairness contract** — equivalent intent must route equivalently with visible
   route trace; see [plans/ROUTING_CONTRACT.md](../plans/ROUTING_CONTRACT.md).
5. **Panel / multi-voice rethink** — optional method inside
   `reflective-research` (single host, persona lenses); judgment record at
   [plans/multi-agent-panel-consensus-2026-06-25.md](../plans/multi-agent-panel-consensus-2026-06-25.md).

Run `make all` before claiming routing or governance changes are verified.

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

`PROJECT_KNOWLEDGE.md` is the project's curated *judgement* layer: why the
project believes what it believes, where it is going, and what it has learned.
It is **non-authoritative**, not non-normative: project-design principles may
guide product and architecture choices, but they never grant agent authority or
override this file, higher-authority instructions, user authorization, or any
`SKILL.md`.

Read-first rule:

- For non-trivial tasks touching architecture, workflow, governance, or an
  existing decision, read the relevant section of `PROJECT_KNOWLEDGE.md` before
  planning. No human invocation is required.

Binding-migration rule:

- This file (`AGENTS.md`) and `SKILL.md` files are the only repository sources of
  agent operating rules. If `PROJECT_KNOWLEDGE.md` starts prescribing agent
  execution, permissions, tools, or required workflow, move that rule here or
  into the relevant skill. Keep project-design rationale and constraints in the
  knowledge layer.
- The separation is enforced mechanically by
  `plans/validate_project_knowledge.py`, which verifies the authority boundary
  and catches explicit agent-directed rules without banning ordinary normative
  language used by project-design principles.

Promotion path:

- `reflective-handoff-retro` owns the promotion-candidate contract: candidate,
  evidence, destination, authority class, proposed action, approval state,
  sources, and review/retirement trigger.
- A candidate enters the long-term project-judgement layer only after explicit
  human approval. One-off incidents stay in plans or retros. Repeated procedures
  become project-local skill candidates rather than prose lessons.

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
