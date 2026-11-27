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

- "Catalog questions about which skill owns a library workflow, including handoff or retro, stay here."
- "A routing-only mix is still a catalog question, not a request to execute the mix."

Do not use when:

- The task is already clearly a single skill path.
- You only need final execution and no routing decision.

L1 fast path:

- When Strictness is L1, the task is trivial, and no high-risk, trust-boundary, or side-effect authority signal appears, answer directly with the full ten-field route trace using compact values, instead of routing to `reflective-brief`. If any of these signals is ambiguous, default up to `reflective-brief`.

## `reflective-brief`

Trigger cues:

- "Clarify goal, scope, assumptions, and acceptance first."
- "I know what I want roughly, but the task is still fuzzy."
- "Define failure conditions and falsifiability before planning."

- "Settle scope and assumptions before a PRD is written."
- "Get stakeholder alignment before an architecture is chosen."
- "Agree on goals with stakeholders prior to opening tickets."
- "先把目標講清楚，再決定要不要拆成工單."

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
- "Open tickets from an already accepted specification and stop before coding."
- "Turn an accepted specification into a plan and leave the repo untouched."
- "已核准規格只做計畫，repo 先不要動."
- "Draft the rollout on paper from an accepted specification, with no repo edits."

- "Write the tickets and the acceptance checks, and do not edit the repository."
- "Compare two interface designs on paper and stop before any implementation."
- "Paper-only API comparison; do not edit the repository."
- "Paper-only comparison of API options; repository stays untouched."
- "A design comparison that never leaves the page and never edits the repo."
- "兩個 API 方案只做紙上對照，不寫實作."
- "把規格整理成文件，程式先不要動."
- "Specify the handoff workflow and stop before any runtime code."
- "把這個想法拆成工單並附驗收標準，先不要實作."

Do not use when:

- Definition of Ready inputs are missing; use `reflective-brief` first.
- The request is only to critique an existing plan; use `reflective-review`.
- The request includes executable test or production-code edits; use `reflective-implement` for that phase.

## `reflective-implement`

Trigger cues:

- "Implement this change in the repo."
- "Code the accepted specification into the repo."
- "把已核准的規格寫進 repo."
- "把已核准規格 implement 進 repo."
- "Land the approved spec into the codebase."
- "把已核准規格合併進程式庫."
- "Refactor or debug with acceptance criteria and tests."
- "Ship a minimal safe patch with verification."
- "Fix that one-line null guard in the implementation."
- "請直接改掉這個很小的空值檢查，並跑測試."
- "Turn the repeated manual release check into an in-repo deterministic test."
- "Stay on the change until the auth suite is fully green."
- "Author a shell loop that re-invokes the agent until an external verifier succeeds."
- "一直改到整包測試都變綠."

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

- "Which libraries could this module drop?"
- "Review whether this module's extra libraries can be cut."

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

- "Read the README for clarity while security assessment stays out of scope."
- "Read the diff for readability while production rollout stays out of scope."
- "Comment on style and logic in this pull request ahead of the merge."
- "看 README 好不好懂，這次不評估安全."
- "Look for regressions in this patch prior to merge."

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
- "Debate a skill-merge decision through several distinct lenses."
- "Read both libraries' vendor documentation before choosing."

Do not use when:

- The answer is fully repo-local and needs no external grounding.
- The task is fully repo-local dependency removal or anti-bloat; use `reflective-minimality`. Use `reflective-spec-plan` for paper-only architecture tradeoffs.

## `reflective-risk`

Trigger cues:

- "This touches auth, privacy, money, production, or deletion."
- "Need dry-run, rollback, and approval gates."
- "Assess blast radius before execution."
- "A tool action could be influenced by untrusted or incomplete data."
- "A production authentication edit must be checked so secrets stay unexposed."

Do not use when:

- The task is low-risk and reversible with narrow blast radius.
- You are trying to replace normal implementation planning.

## `reflective-handoff-retro`

Trigger cues:

- "Prepare handoff for another agent/session."
- "Run retro and capture process improvements."
- "Convert repeated incidents into reusable rules."
- "After this sprint, capture lessons and process changes."

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
- **Deliver end-to-end under governance (Software Factory / AI-native SDLC)** → `governed-delivery` — autonomous or unattended delivery run with a gate sequence, oracle manifest, task packet, failure-signature exits, decorrelated verification, evidence ledger, and named acceptance; emits a host-run delivery contract set, does not enforce it; side effects still gate through `reflective-risk`.
- **Agent-drivable verification surface for a product repo** → `verification-map-generator` — emits VERIFY.md + features/ map + optional locked acceptance spec inside the product repo so a fresh agent can verify and classify failures (product regression / doc drift / spec-oracle error / harness failure); not a loop runner (`flow-loop-harness`) or a no-code test plan (`reflective-spec-plan`).
- **Headless invocation of a named agent CLI** → `headless-agent-cli-contract` — emits a per-provider recipe (prompt transport spelling, permission flags, output isolation, side-channel strip list) after a zero-cost inventory probe; `BLOCKED` verdict when the CLI has no non-interactive mode; never auto-approves permission-widening flags.
- **With/without-skill pilot with blinded scoring** → `arm-blinded-eval-harness` — label-stripped extraction, sealed arm map, leak assertion, discarded-invocation ledger; by-construction guarantees.
- **Lint a repo's REQ/AC acceptance surface** → `acceptance-join-validator` — every ID joins to a locked runnable check; static only, never executes.
- **Baseline-vs-skill run over the golden corpus** → `golden-benchmark-runner` — paired arms + deterministic scoring + confound ledger; directional verdicts only.
- **Check a route trace against the Router Output Contract** → `router-trace-linter` — field presence, confidence parse, R5 rationale, R4/R7 Human Review presence.
- **Workflow choice / library routing** → still `reflective-dispatch`; this section does not replace the nine-skill Fast Routing Rule.
