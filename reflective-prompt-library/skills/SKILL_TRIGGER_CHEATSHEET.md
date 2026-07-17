Language: English | [繁體中文](SKILL_TRIGGER_CHEATSHEET.zh-TW.md)

# Skill Trigger Cheatsheet

This page is a fast selector for the 9 TeaPrompt **core** workflow skills; optional host-invoked domain packs are listed separately at the end.

> **Output conventions:** A compact deliverable specification belongs in the
> Module Contract's `Output:` field. Add a standalone `## Output` section only
> when the skill produces a substantive output template (e.g., markdown block,
> multi-field structure). Skills with procedural steps (before/during/after)
> generally do not need a standalone Output section.

Use it when you need quick routing instead of reading each `SKILL.md` in full.

Routing fairness note:
- Each skill frontmatter includes `context_load: low|medium|high` for cost-aware routing.
- Trigger cues below are examples, not required wording.
- Equivalent intent should route equivalently even when phrasing differs.
- Fast keyword routing is allowed, but it must not silently reduce quality for equivalent intent.
- At Strictness L1–L2, defer `context_load: high` skills unless risk or explicit demand requires them; list deferred skills in route trace.
- When a task uses external content, tool outputs, entity-like records, or side-effectful actions, apply `04-agent/runtime-trust-boundary.md` as a supporting lens with the selected skill.


Boundary quick cues (ROUTE-002 holdout + ROUTE-003 adversarial):
- **Plan-only (no code)** → `reflective-spec-plan` — tickets, rollout plans, or acceptance criteria with explicit no-code context.
- **Plain review (non-production)** → `reflective-review` — diff/PR review for readability or regressions when production risk is out of scope.
- **Approved spec delivery** → `reflective-implement` — implement or land an approved spec in the repository; not plan-only.
- **Brief before plan** → `reflective-brief` — narrow scope or stakeholder alignment before PRD/tickets.
- **Research not brief** → `reflective-research` — multi-voice debates or source-backed comparisons, not goal clarification.
- **Trivial fix not review** → `reflective-implement` — small code patches in the repo, not diff review.
- **Production risk not plain review** → `reflective-risk` — auth/production/billing changes need a risk gate, not readability review.
- **Recurring deterministic check** → primary workflow + `verifier/test` artifact (Acquisition L3) — do not jump to a runner unless a prompt-impossible guarantee is required.
- **Doc edit not review** → `reflective-implement` — revising repository documents or content against acceptance criteria; critique-only stays `reflective-review`.
- **Prototype/spike (criteria emerge by building)** → `reflective-brief` first — frame the spike as a falsifiable question plus a timebox, then `reflective-implement` with a disposable-artifact label; full `reflective-spec-plan` waits until the direction sticks.

## `reflective-dispatch`

Trigger cues:

- "Help me choose prompt-only vs workflow."
- "Route this task before doing implementation."
- "This request mixes planning, risk, and execution."
- "This task includes external data, tool results, or action authority questions."

- "Which skill handles session handoff in this library?"
- "Which workflow skill should run for this library task?"
- "Which reflective workflow skill covers handoff retro?"
- "Which reflective workflow skill fits a routing-only mixed intent?"
- "Which reflective workflow skill should handle routing-only mixed intent?"

Do not use when:

- The task is already clearly a single skill path.
- You only need final execution and no routing decision.

L1 fast path:

- When Strictness is L1 and the task is trivial, answer directly with a minimal route trace instead of routing to `reflective-brief`.

## `reflective-brief`

Trigger cues:

- "Clarify goal, scope, assumptions, and acceptance first."
- "I know what I want roughly, but the task is still fuzzy."
- "Define failure conditions and falsifiability before planning."

- "Narrow scope and assumptions before writing the PRD."
- "Stakeholder alignment before choosing architecture."
- "Align stakeholders on goals before writing tickets."
- "釐清目標再拆工單."

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
- "Write tickets from the approved spec without implementing."
- "Plan the approved spec without repo changes."
- "Plan 已核准 spec without repo changes."
- "Draft rollout plan from approved spec without repo edits."

- "Write tickets and acceptance criteria without touching the repo."
- "Compare two API designs on paper only no implementation."
- "Compare API designs on paper without touching the repository."
- "Compare API design options on paper without touching the repository."
- "Design comparison on paper without repo changes."
- "比較兩個 API 設計方案但不要寫 code."
- "把規格寫出來但不要改程式."
- "Design a handoff workflow specification without runtime code."
- "把這個 idea break down into tickets with acceptance criteria."

Do not use when:

- Definition of Ready inputs are missing; use `reflective-brief` first.
- The request is only to critique an existing plan; use `reflective-review`.
- The request includes executable test or production-code edits; use `reflective-implement` for that phase.

## `reflective-implement`

Trigger cues:

- "Implement this change in the repo."
- "Implement the approved spec in the repository."
- "在 repository 實作已核准 spec."
- "Implement 已核准 spec in the repository."
- "Land the approved spec into the codebase."
- "落地已核准規格到 codebase."
- "Refactor or debug with acceptance criteria and tests."
- "Ship a minimal safe patch with verification."
- "Patch the trivial null check in code."
- "幫我 patch 這個 trivial null check and run tests."
- "Automate the recurring manual release check as a deterministic test in the repo."
- "Keep working until every test in test/auth passes."
- "Write a bash loop that reruns the agent until the verifier passes."
- "持續修到整個測試套件全綠為止."

Minimality signal scan (inside this skill):

- When bloat signals appear (new dependency, extra files, new abstraction), run the Minimality Signal Scan in the skill before editing; escalate to `reflective-minimality` if the cut is disputed.

Do not use when:

- The task is high-risk and not yet gated; run `reflective-risk` first.
- Requirements are still unclear; use `reflective-brief` or `reflective-spec-plan`.

## `reflective-minimality`

Trigger cues:

- "Avoid overengineering, bloat, boilerplate, or unnecessary dependencies."
- "Can this be deleted, narrowed, deferred, or solved with stdlib/native behavior?"
- "Run a YAGNI / minimality / Ponytail-style gate before coding."
- "Review this diff only for complexity we can cut."

- "What dependencies can we remove from this module?"
- "Dependency removal review for this module."

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

- "Review the README for clarity not security."
- "Check the diff for readability not production deploy."
- "Review this PR for style and logic before merge."
- "審查 README 清晰度不是安全風險."
- "Inspect this patch for regressions before merge."

Do not use when:

- You are still defining the first draft; use `reflective-brief` or `reflective-spec-plan`.
- The task is pure implementation with no review ask.

## `reflective-research`

Trigger cues:

- "Research current best practices with sources."
- "Inspect docs, DeepWiki, and long references."
- "Separate evidence from inference."
- "Compare official docs, third-party mirrors, and community analysis."
- "Review whether a prompt leak or mirror is trustworthy and transferable before adoption."
- "Research current workflow frameworks or orchestration patterns."
- "Multi-model or multi-perspective strategic rethink (use Optional Method: Multi-Voice Panel in the skill)."
- "Six-lens debate on whether to merge these skills."
- "Compare official docs for both libraries before deciding."

Do not use when:

- The answer is fully repo-local and needs no external grounding.
- The task is fully repo-local dependency removal or anti-bloat; use `reflective-minimality`. Use `reflective-spec-plan` for paper-only architecture tradeoffs.

## `reflective-risk`

Trigger cues:

- "This touches auth, privacy, money, production, or deletion."
- "Need dry-run, rollback, and approval gates."
- "Assess blast radius before execution."
- "A tool action could be influenced by untrusted or incomplete data."
- "Verify production auth change will not expose secrets."

Do not use when:

- The task is low-risk and reversible with narrow blast radius.
- You are trying to replace normal implementation planning.

## `reflective-handoff-retro`

Trigger cues:

- "Prepare handoff for another agent/session."
- "Run retro and capture process improvements."
- "Convert repeated incidents into reusable rules."
- "Lessons learned retro after this sprint."

Do not use when:

- Work is still in active implementation and no handoff is needed.
- You only need a code review decision.

## Fast Routing Rule

If uncertain, apply this order:

1. `reflective-dispatch`
2. `reflective-risk` (if any high-risk or side-effect authority signal appears)
3. `reflective-brief` or `reflective-spec-plan`
4. `reflective-research` (if current external sources, source-backed comparison, multi-voice synthesis, or scaffold provenance evidence is load-bearing)
5. `reflective-minimality` (if bloat, dependency, abstraction, or scope creep risk appears)
6. `reflective-implement`
7. `reflective-review`
8. `reflective-handoff-retro`

When uncertain and low-risk:
- Prefer a visible default-up to a silent downgrade.
- Show available enhancements such as tests, security review, and performance checks.

## Domain packs (host-invoked; not core routing)

- **Runnable one-pass flow script** → `flow-control-generator` — chain, pipeline, fan-out, orchestrate agent CLI steps as a script; not plan-only workflow design (`reflective-spec-plan`).
- **Runnable loop script** → `flow-loop-harness` — loop until, ralph, fix-until-green with external verifier; not an in-repo `verifier/test` artifact on the primary workflow (Acquisition L3 quick cue above).
- **Governance scaffolding for an effect-producing agent** → `agent-governance-scaffold` — split proposal/authorization/effect/acceptance authority, capability tokens, broker receipts, lease-keyed effect budgets, constitutional paths; emits host-run contracts, does not enforce them; high-risk artifacts still gate through `reflective-risk`.
- **Workflow choice / library routing** → still `reflective-dispatch`; this section does not replace the nine-skill Fast Routing Rule.
