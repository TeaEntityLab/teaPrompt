Language: English

# Project Knowledge — TeaPrompt

> **NON-AUTHORITATIVE FILE.** This file records *why* the project believes what
> it believes, *where* it is going, and *what* it has learned. Its project-design
> principles may guide product and architecture choices, including choices not
> already covered by an operating rule. It does not grant authority to an agent,
> authorize actions, or override system/developer instructions, the user's
> request, [`06-repo/AGENTS.md`](06-repo/AGENTS.md), or
> [`skills/*/SKILL.md`](skills/). Agent operating rules belong in AGENTS.md or a
> SKILL.md; project-design judgement belongs here.
>
> [`plans/validate_project_knowledge.py`](plans/validate_project_knowledge.py)
> verifies this authority declaration and catches explicit agent-directed rules.
> It does not pretend to infer authority from modal words alone. Dead links are
> caught separately by `plans/validate_links.py`.

## Governing Principles

> Existing principles are **pointed to**, not restated, so there is exactly one
> source of truth. Project-specific principles may be stated here when no
> canonical source exists; include their rationale and practical implication.

- Doing the right thing > doing things right — see [METHODOLOGY_MAP.md](METHODOLOGY_MAP.md)
- Smallest useful workflow; escalate strictness only when risk demands it — see [skills/reflective-dispatch/SKILL.md](skills/reflective-dispatch/SKILL.md)
- Anti-bloat / prefer deletion and existing capability — see [skills/reflective-minimality/SKILL.md](skills/reflective-minimality/SKILL.md)
- Instruction/data separation and least-privilege action gates — see [04-agent/runtime-trust-boundary.md](04-agent/runtime-trust-boundary.md)
- Evidence over confidence; do not claim unrun checks — see [01-thinking/critical-thinking-check.md](01-thinking/critical-thinking-check.md)

## Current Direction

> The active problem the project is solving now, with explicit non-goals so scope
> does not silently expand. Each milestone carries a `Status:` of
> `active`, `planned`, or `done`. A `done` milestone is a candidate for removal,
> not a permanent record (history belongs in the Decision Index).

### Milestone: Governance layer maturity
- Status: active
- Problem: keep the routing contract, quality gates, and minimality gate trustworthy as the skill set grows, without turning the library into a monolith.
- Non-goals: a runtime engine, an agent swarm, a vector/RAG memory store, vendor lock-in.
- Target: routing and minimality gates remain evidence-backed and pass on every change.

### Milestone: Project judgment layer
- Status: active
- Problem: the repo had an authoritative instruction layer (AGENTS + skills) and a task/session memory layer (handoff-retro, plans, ledgers) but no curated, auto-loaded *project rationale* layer — so cross-session "why" lived only in scattered plans.
- Non-goals: importing Knowie's full toolchain; adding a tenth core workflow skill; auto-harvesting long-term memory from every conversation.
- Target: a reusable project-judgement scaffold, an explicit authority boundary, an evidence-gated promotion contract, and deterministic structural checks that do not masquerade as semantic review.

## Durable Lessons

> Only patterns that recurred or carry concrete evidence belong here. A one-off
> incident is out of scope for this section. Each lesson carries an `Evidence:`
> pointer to a plan, test, or commit; a lesson without evidence fails validation.

### Lesson: Prompt wording cannot fix execution-layer failures
- Pattern: asking the model in prose to ignore information it can see (e.g. final state during hindsight rationalization) does not hold; runtime masking, harness checks, and tests are required.
- Evidence: [plans/project-adjustment-reflection-2026-06-11.md](plans/project-adjustment-reflection-2026-06-11.md), [04-agent/runtime-trust-boundary.md](04-agent/runtime-trust-boundary.md)
- Review trigger: any time a new guarantee is proposed as prompt text alone.

### Lesson: Prefer a source doc or supporting lens over a new core skill
- Pattern: capabilities were repeatedly proposed as new workflow skills when a reference doc or an existing lens already covered the need; adding skills inflates surface area.
- Evidence: [plans/project-adjustment-reflection-2026-06-11.md](plans/project-adjustment-reflection-2026-06-11.md), [plans/ponytail-minimality-reflection-2026-06-17.md](plans/ponytail-minimality-reflection-2026-06-17.md)
- Review trigger: a promotion gate of at least three cross-session recurrences before a new skill or directory is created.

### Lesson: External-tool adoption is mechanism-vs-product, local-gap-gated
- Pattern: external tools/methods are repeatedly evaluated for adoption; most warrant no change because the capability is already covered, out of scope (a non-goal), or behind an unmet promotion gate. Only a verified *local* structural gap warrants a change (STORM). External interest in a deferred capability is not local promotion evidence; record "no change" outcomes too, or they get re-litigated.
- Evidence caveat: unavailable usage data is `unknown`, not evidence of zero demand. Decide narrow, reversible repairs from the best available local evidence, external evidence when the claim depends on it, explicit counterarguments, blast radius, and falsifiable verification. The recurrence gate applies to promotion into a new skill, directory, runner, or other durable surface; it does not veto an in-place repair to an existing declared contract.
- Layer caveat: distinguish the *methodology* layer (a prompt, lens, or triggerable skill — e.g. `sop-compiler`) from the *operationalization* layer (a recorder, skill generator, persisted state, replay verification). A spec covering a capability is not the capability. "Methodology-complete" must not be read as "operationally complete"; the operational/runtime layer is a deliberate non-goal, not an oversight.
- Evidence: [plans/external-adoption-case-studies-2026-06-20.md](plans/external-adoption-case-studies-2026-06-20.md), [plans/storm-perspective-discovery-reflection-2026-06-18.md](plans/storm-perspective-discovery-reflection-2026-06-18.md), [plans/agentic-sop-workflow-reflection-2026-06-13.md](plans/agentic-sop-workflow-reflection-2026-06-13.md)
- Review trigger: when evaluating a new external tool or disputing an implementation decision, run the corrected procedure in the case study, preserve unknowns, and record the outcome even when it is "no change."

## Decision Index

> Pointers to the causal trail — plans, reflections, tests, commits. Detail is
> not duplicated here; this is a map, not an archive.

- 2026-06-11 Add `runtime-trust-boundary` as a lens, not a ninth skill → [record](plans/project-adjustment-reflection-2026-06-11.md)
- 2026-06-17 Adopt a minimal project-judgment contract instead of importing Knowie → [initial record](plans/knowie-project-knowledge-reflection-2026-06-17.md)
- 2026-06-17 Refine the contract from non-normative to non-authoritative, connect promotion, and publish a reusable scaffold → [decision](plans/project-knowledge-authority-promotion-decision-2026-06-17.md)
- 2026-06-18 Adopt STORM's source-grounded perspective discovery as an optional `reflective-research` method, not a new skill → [record](plans/storm-perspective-discovery-reflection-2026-06-18.md)
- 2026-06-20 Synthesize external-adoption case studies, then correct the evidence and promotion-gate scope after the Test Plan routing counterexample → [record](plans/external-adoption-case-studies-2026-06-20.md)
