Language: English | [繁體中文](SKILL_TRIGGER_CHEATSHEET.zh-TW.md)

# Skill Trigger Cheatsheet

This page is a fast selector for the 9 TeaPrompt workflow skills.

Use it when you need quick routing instead of reading each `SKILL.md` in full.

Routing fairness note:
- Trigger cues below are examples, not required wording.
- Equivalent intent should route equivalently even when phrasing differs.
- Fast keyword routing is allowed, but it must not silently reduce quality for equivalent intent.
- When a task uses external content, tool outputs, entity-like records, or side-effectful actions, apply `04-agent/runtime-trust-boundary.md` as a supporting lens with the selected skill.

## `reflective-dispatch`

Trigger cues:

- "Help me choose prompt-only vs workflow."
- "Route this task before doing implementation."
- "This request mixes planning, risk, and execution."
- "This task includes external data, tool results, or action authority questions."

Do not use when:

- The task is already clearly a single skill path.
- You only need final execution and no routing decision.

## `reflective-brief`

Trigger cues:

- "Clarify goal, scope, assumptions, and acceptance first."
- "I know what I want roughly, but the task is still fuzzy."
- "Define failure conditions and falsifiability before planning."

Do not use when:

- A complete reviewed spec already exists.
- The task is only a quick factual lookup.

## `reflective-spec-plan`

Trigger cues:

- "Write a spec / PRD / implementation plan."
- "Turn this into tickets with dependencies and tests."
- "Do usage-first design before coding."
- "Design a rigorous Test Plan from this spec without writing code."
- "Plan tool gates, authority boundaries, and side effects."
- "Design a resumable workflow, state model, or orchestration plan without runtime code."

Do not use when:

- Definition of Ready inputs are missing; use `reflective-brief` first.
- The request is only to critique an existing plan; use `reflective-review`.
- The request includes executable test or production-code edits; use `reflective-implement` for that phase.

## `reflective-implement`

Trigger cues:

- "Implement this change in the repo."
- "Refactor or debug with acceptance criteria and tests."
- "Ship a minimal safe patch with verification."

Do not use when:

- The task is high-risk and not yet gated; run `reflective-risk` first.
- Requirements are still unclear; use `reflective-brief` or `reflective-spec-plan`.

## `reflective-minimality`

Trigger cues:

- "Avoid overengineering, bloat, boilerplate, or unnecessary dependencies."
- "Can this be deleted, narrowed, deferred, or solved with stdlib/native behavior?"
- "Run a YAGNI / minimality / Ponytail-style gate before coding."
- "Review this diff only for complexity we can cut."

Do not use when:

- Requirements are still unclear; use `reflective-brief` or `reflective-spec-plan` first.
- The simplification may remove security, privacy, auth, data-loss prevention, accessibility, compatibility, or explicit requirements.
- A full correctness review is needed; pair it with `reflective-review`.

## `reflective-review`

Trigger cues:

- "Review this code / diff / plan / spec / output."
- "Find risks, regressions, and missing tests."
- "Audit assumptions and evidence quality."
- "Check whether external content is being treated as data instead of instructions."
- "Review whether a prompt leak or mirror is trustworthy and transferable."

Do not use when:

- You are still defining the first draft; use `reflective-brief` or `reflective-spec-plan`.
- The task is pure implementation with no review ask.

## `reflective-research`

Trigger cues:

- "Research current best practices with sources."
- "Inspect docs, DeepWiki, and long references."
- "Separate evidence from inference."
- "Compare official docs, third-party mirrors, and community analysis."
- "Research current workflow frameworks or orchestration patterns."

Do not use when:

- The answer is fully repo-local and needs no external grounding.
- The task is only dependency selection; treat that as a dedicated evaluation lane.

## `reflective-risk`

Trigger cues:

- "This touches auth, privacy, money, production, or deletion."
- "Need dry-run, rollback, and approval gates."
- "Assess blast radius before execution."
- "A tool action could be influenced by untrusted or incomplete data."

Do not use when:

- The task is low-risk and reversible with narrow blast radius.
- You are trying to replace normal implementation planning.

## `reflective-handoff-retro`

Trigger cues:

- "Prepare handoff for another agent/session."
- "Run retro and capture process improvements."
- "Convert repeated incidents into reusable rules."

Do not use when:

- Work is still in active implementation and no handoff is needed.
- You only need a code review decision.

## Fast Routing Rule

If uncertain, apply this order:

1. `reflective-dispatch`
2. `reflective-risk` (if any high-risk or side-effect authority signal appears)
3. `reflective-brief` or `reflective-spec-plan`
4. `reflective-minimality` (if bloat, dependency, abstraction, or scope creep risk appears)
5. `reflective-implement`
6. `reflective-review`
7. `reflective-handoff-retro`

When uncertain and low-risk:
- Prefer a visible default-up to a silent downgrade.
- Show available enhancements such as tests, security review, and performance checks.
