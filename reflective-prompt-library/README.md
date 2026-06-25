Language: English | [繁體中文](README.zh-TW.md)

# Reflective Prompt Library

This library collects reusable prompts for reflective engineering work: deciding what to do, turning ambiguity into specs, reviewing artifacts, designing tests, choosing agent workflows, and preserving context between sessions.

Core principle:

```text
Doing the right thing > doing things right.
```

Use the prompts compositionally rather than as one giant instruction:

```text
Core identity prompt
+ task prompt
+ context mode prompt
+ validation prompt
```

## North Star

TeaPrompt helps humans and host agents choose the **right amount of rigor** for a task, record **why** decisions were made, and verify outcomes with **evidence** — using composable prompt layers and nine workflow skills as natural-language harness policy, **without** operating its own agent runtime.

## Strictness Before Skills

Pick **Strictness L1–L6** first (`skills/reflective-dispatch/SKILL.md`, [GLOSSARY.md](GLOSSARY.md)), then the skill phase. Skills declare `context_load: low|medium|high` in frontmatter so cost-aware hosts can defer heavy skills when Strictness is low.


## Governance Panel Record

Multi-agent Socratic consensus on project goals and the nine skills (Rounds 1–78, options A–ED) is recorded in [plans/multi-agent-panel-consensus-2026-06-25.md](plans/multi-agent-panel-consensus-2026-06-25.md). Run `make all` before claiming routing or governance changes are verified.

## Directory Map

- `00-core/`: core identity, custom instructions, master prompts, and controller prompts.
- `01-thinking/`: Socratic questioning, critical thinking, counterarguments, falsifiability, and Why / What / How / Done gates.
- `02-engineering/`: task start, specs, usage-first design, task slicing, implementation, review, tests, and local feedback.
- `03-context/`: small / medium / large context prompts, low-token mode, context engineering, Gemini long-document handling, and handoff summaries.
- `04-agent/`: agent selection, SOP compiler design, workflow engine design, review-rating-fix loops, retros, and memory consolidation.
- `05-domain/`: high-risk review, research, business strategy, learning, writing, and creative template prompts.
- `06-repo/`: repository-level instruction templates plus a reusable
  `PROJECT_KNOWLEDGE.template.md` for project-specific design judgement.
- `skills/`: concise `SKILL.md` workflow wrappers that map the prompt library into practical agent workflows.
- `skills/SKILL_TRIGGER_CHEATSHEET.md`: one-page trigger cues and anti-misuse rules for the 9 workflow skills.
- `skills/examples/`: worked input/output examples for each workflow skill.
- `plans/`: plan files for code-bearing or multi-agent/workflow follow-up work.
- `plans/ROUTING_CONTRACT.md`: routing fairness, observability, and risk-based default-up contract.
- `plans/route-001-paraphrase-eval.yaml`: paraphrase routing eval seed for ROUTE-001.
- `GLOSSARY.md`: operational definitions of load-bearing terms used across the library.
- `METHODOLOGY_MAP.md`: maps the source methodology families to repo prompts and workflow skills.
- `LANGUAGE_POLICY.md`: explains why operational docs are English while some prompt sources remain localized.

Install the workflow skills with [SKILL_INSTALLATION.md](SKILL_INSTALLATION.md). It covers Claude Code, Codex, Cursor, Antigravity CLI / IDE, and OpenCode.

Use [METHODOLOGY_MAP.md](METHODOLOGY_MAP.md) before adding new prompts or skills. It keeps classification stronger than forced unification.

## Skills as Workflow

The prompt files are the source material. The `skills/` directory is the operational layer: a small set of repeatable workflows that can be copied into `.claude/skills/`, `~/.codex/skills/`, `.agents/skills/`, or another SKILL.md-compatible environment when needed.

| Workflow Need | Skill |
| --- | --- |
| Route a task to the smallest useful reflective workflow | `skills/reflective-dispatch/SKILL.md` |
| Clarify goal, assumptions, scope, acceptance, falsifiability | `skills/reflective-brief/SKILL.md` |
| Write spec, usage-first design, task slices, a no-code Test Plan, or a no-code agent workflow design | `skills/reflective-spec-plan/SKILL.md` |
| Implement code with verification and traceability | `skills/reflective-implement/SKILL.md` |
| Challenge unnecessary code, dependencies, abstractions, or scope before implementation | `skills/reflective-minimality/SKILL.md` |
| Review code, plans, specs, and AI outputs | `skills/reflective-review/SKILL.md` |
| Research external docs, DeepWiki, and long sources | `skills/reflective-research/SKILL.md` |
| Gate high-risk work before execution | `skills/reflective-risk/SKILL.md` |
| Handoff, retro, and memory consolidation | `skills/reflective-handoff-retro/SKILL.md` |

The design intentionally avoids one skill per prompt. Use the prompt library for nuance and the skills for execution shape.

> Skills are prompt-level workflow wrappers: natural-language procedures interpreted by the host runtime (Claude Code, Codex, OpenCode, etc.). They do not provide a multi-agent runtime, async messaging, or role isolation.

## Recommended Defaults

Daily thinking:

```text
core-short
+ socratic-reviewer
+ critical-thinking-check
+ why-what-how-done
```

Engineering task:

```text
core-full
+ task-start
+ spec-writer
+ usage-first
+ task-slicer
+ implementation-agent
+ code-reviewer
```

High-risk task:

```text
core-full
+ high-risk
+ local-feedback
+ human review gate
```

Long research:

```text
research
+ large-context
+ gemini-long-document
+ context-handoff
```

## Use Case Selection

| Situation | Recommended Prompt |
| --- | --- |
| You are unsure what the real question is | `01-thinking/socratic-reviewer.md` |
| You want to check whether a plan is flawed | `01-thinking/critical-thinking-check.md` |
| You want to avoid optimism or overengineering | `01-thinking/counterargument.md` |
| You want to start an engineering task | `02-engineering/task-start.md` |
| You want to write a spec | `02-engineering/spec-writer.md` |
| You want to design usage before implementation | `02-engineering/usage-first.md` |
| You want to slice work into tickets | `02-engineering/task-slicer.md` |
| You want an agent to implement code | `02-engineering/implementation-agent.md` |
| You want to review code or a diff | `02-engineering/code-reviewer.md` |
| You want to design tests | `02-engineering/test-designer.md` |
| The task is high-risk | `05-domain/high-risk.md` |
| Something failed | `02-engineering/local-feedback.md` |
| You need to switch sessions | `03-context/context-handoff.md` |
| A task is complete and you want process learning | `04-agent/retro.md` |
| You need to decide Prompt vs Agent vs Workflow | `04-agent/agent-selection.md` |
| You need to convert a repeatable human SOP into an agent workflow | `04-agent/sop-compiler.md` |
| You need to design or review runtime trust boundaries | `04-agent/runtime-trust-boundary.md` |
| You need to review a leaked, mirrored, or third-party agent scaffold | `04-agent/agent-scaffold-provenance.md` |
| You need a project-specific design-judgement layer without creating a second agent rulebook | `06-repo/PROJECT_KNOWLEDGE.template.md` + `skills/reflective-handoff-retro/SKILL.md` |
