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
- Evidence over confidence; do not claim unrun checks — see [01-thinking/critical-thinking-check.md](01-thinking/critical-thinking-check.md) (claim audit) and [06-repo/AGENTS.md](06-repo/AGENTS.md) § Anti-cheating Rules (execution claims)

## Current Direction

### North Star (2026-06-25)

TeaPrompt helps humans and host agents choose the right amount of rigor for a task,
record why decisions were made, and verify outcomes with evidence — using composable
prompt layers, nine core workflow skills, and optional registered domain packs as
natural-language harness policy, without operating its own agent runtime. See
[README.md](README.md#north-star).

> The active problem the project is solving now, with explicit non-goals so scope
> does not silently expand. Completed milestones are retired from this section;
> their outcomes live in the Decision Index.

**Ongoing (post Round 68 panel):** maintain ROUTE-001/002/003 evals, governance validators,
and holdout expansion before router tuning — see [GLOSSARY.md](GLOSSARY.md) Governance
Maintenance Playbook. Post-panel maintenance (e.g. ROUTING_CONTRACT R11 approved-spec delivery)
follows the same holdout-before-tune rule. No open implementation blockers from Rounds 8–20;
deferred promotions are recurrence-gated — see [panel backlog](plans/multi-agent-panel-consensus-2026-06-25.md#recurrence-gated-backlog-not-panel-blockers).

### Standing Non-Goals
- TeaPrompt does not operate its own multi-agent runtime, swarm, async peer messaging layer, recorder, replay engine, or side-effect enforcer; runtime designs remain references unless project direction changes.
- The core routing layer remains nine frozen workflow skills; nine is the current bounded-set cardinality, not an optimality claim. A tenth core skill needs the three-recurrence promotion gate and explicit human approval.
- Registered domain packs are host-invoked contracts outside core routing and follow the binding admission rule in [06-repo/AGENTS.md](06-repo/AGENTS.md#harness-policy-nine-skills); a user-directed exception records recurrence as `unknown`, never as proof of recurrence.
- Full `SKILL.md` localization is not current direction; zh-TW supports navigation, cheatsheet routing, and glossary lines while English stays canonical for skill contracts.
- Router tuning follows [ROUTING_CONTRACT.md](plans/ROUTING_CONTRACT.md) R8: add holdout evidence before tuning. Seeded routing evals are regression guards, not proof of general semantic routing quality.
- "Methodology-complete" does not mean "operationally complete"; prompt/spec coverage does not promise persistence, replay, cancellation, idempotency, or role isolation.
- Skills and prompt lenses may specify required runtime guarantees as preconditions, but TeaPrompt does not enforce or warrant them; host-runtime code and tests are the authority for operational guarantees, and missing enforcement evidence is `unknown` / no-go.


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
> not duplicated here; this is a map, not an archive. Mechanical panel rounds
> are rolled up; the round-by-round trail lives in the panel record.

- 2026-07-11 Managed-skill promotion review — six-lens panel over the host agent's 27 agent-authored managed skills decided `AGREE WITH CHANGES`: promote exactly two surgical extracts (Parallel Lens Review packet-and-verdict contract subsection in `04-agent/workflow-recipes.md`; memory-derived-source rule in `04-agent/artifact-promotion.md` Evidence rules); everything else no-change, deferred with triggers (doc-internalization deltas, README orientation, redaction methodology), or rejected (persona-driven panel-round retired host-side; 21 other-project skills blanket-rejected; primer/promotion wrappers duplicate governed surfaces) → [panel record](plans/managed-skill-promotion-panel-record-2026-07-11.md)
- 2026-07-11 Flow-control domain pack (user-directed exception) — six-lens panel decided `AGREE WITH CHANGES`: two script-generation skills (`flow-control-generator`, `flow-loop-harness`) registered as domain packs outside the nine-core routing surface via an Option B registry split (CORE_SKILLS vs DOMAIN_PACK_SKILLS guards); nine template bugs fixed with executed rig evidence; gap relabeled user-directed/recurrence-unknown; merge-to-one-skill and router integration deferred with triggers → [panel record](plans/flow-control-pack-panel-record-2026-07-11.md), [research](plans/agent-flow-control-research-2026-07-11.md)
- 2026-07-11 Governance rules rethink — seven-lens parallel review of all principles, skills, plans, and surveys decided `AGREE WITH CHANGES`: every constraint reaffirmed as a safety floor (nine-skill surface, no-owned-runtime, local-gap gate, holdout-before-tune, prompt-vs-runtime split, PK authority boundary); defects were operational — untracked candidate adoption, root AGENTS.md dual-authority ambiguity, oversized unenforced Required Workflow, literal-phrase test pins, archive creep. Applied with human approval: 2026-07-06 candidates #1–#5 adopted (#3 completed via workflow-recipes annotation; E4 decided annotate-not-fold), adoption ledger + guard test, parity/label fixes, root AGENTS.md authority stub, strictness-scaled Required Workflow, README non-goals refresh, count-based test pins, Decision Index rollup, historical headers on retired plans; panel-transcript demotion and 00-core/03-context merges stay recurrence-gated → [record](plans/governance-rules-rethink-review-2026-07-11.md)
- 2026-07-06 Workflow possibilities and constraints review — parallel-lens review decided `AGREE WITH CHANGES`: keep the nine-skill surface, no-owned-runtime default, local-gap adoption gate, holdout-before-tune, and prompt-vs-runtime enforcement split as safety/minimality floors; candidate wording changes qualify "frozen" as gated-not-never, disambiguate Formalization vs Acquisition L0-L4, surface the L3 skill-plus-deterministic-verifier route, fail-close prompt-injection/supply-chain/memory-write gates at L3, and tier panel/survey/routing evidence; relaxations stay recurrence-gated; adoption ledger 2026-07-11: all five adopted (#3 second pass — recipes note; ROUTE-003 verifier-artifact trap + router boundary added same day, holdout-before-tune order kept) → [record](plans/workflow-possibilities-constraints-review-2026-07-06.md)
- 2026-07-06 Skills runtime legitimacy panel — parallel-lens review decided that skills may declare required runtime guarantees but TeaPrompt does not enforce them; runtime is legitimate only for prompt-impossible guarantees proven by deterministic verifier/runtime code, accepted risk gates, Human Review for high-risk side effects, and host-runtime enforcement → [record](plans/skills-runtime-legitimacy-panel-record-2026-07-06.md)
- 2026-07-06 Goals and skill-routing review — parallel-lens review clarified Standing Non-Goals, aligned minimality/scaffold-provenance/dependency routing in existing skills, refreshed quality-gate/index truth, and preserved nine-skill/no-runtime scope → [quality gates](plans/QUALITY_GATES_SUMMARY.md), [dispatch](skills/reflective-dispatch/SKILL.md)
- 2026-07-06 Post-goals route holdout expansion — raised ROUTE-002 to 40 holdout groups / 114 phrases and ROUTE-003 to 18 adversarial groups / 62 phrases before any router tuning; added promotion-routing, runtime-trust side-effect, scaffold-provenance, dependency-deletion, and zh-TW context-load deferral probes → [quality gates](plans/QUALITY_GATES_SUMMARY.md)
- 2026-07-06 Five-layer concept verification — verified the 5+1 frame as a risk-routed reference lens, added scope / analogy / TeaPrompt-boundary caveats, disambiguated cognitive L1-L5 from engineering α-ζ, and kept runtime and memory-ACL mechanisms reference-only → [record](plans/five-layer-agent-sop-reference-record-2026-07-04.md#2026-07-06-concept-verification-update)
- 2026-07-05 Five-layer SOP candidate promotion — explicit project decision fired the reference record's re-promotion trigger; high-volatility fact discipline promoted in place into `skills/reflective-research/SKILL.md`, four-dimensional evidence split into `skills/reflective-review/SKILL.md`; all other five-layer concepts stay no-change → [record](plans/five-layer-agent-sop-reference-record-2026-07-04.md)
- 2026-07-04 Five-layer Agent SOP reference internalization — temporary root `five_layer_agent*` delivery files distilled into a no-change / recurrence-gated reference record; preserve high-volatility fact discipline and four-dimensional evidence ledger as concept candidates, reject new skills/runtime commitments → [record](plans/five-layer-agent-sop-reference-record-2026-07-04.md)
- 2026-07-02 vLLM Micro-Agent §7.3 applied — "Looper Topologies" section in [workflow-recipes](04-agent/workflow-recipes.md) maps the five looper patterns to task-shape signals and existing skills; runtime gaps (budgets, trace/replay, contract-repair) confirmed as non-goals → [research](plans/vllm-micro-agent-research-record-2026-06-30.md), [brief](plans/vllm-micro-agent-technical-brief-2026-06-30.md)
- 2026-07-02 Harness-1 re-check — still v1, no replication/peer review; authors released full checkpoint + training data 2026-06-15; performance numbers stay author-reported → [research](plans/harness-1-state-ledger-research.md)
- 2026-06-25 OpenFugu research and parallel lens review — reference-only mechanism source; reject runtime adoption; TRINITY reproduction deferred until artifact boundary fixed → [research](plans/openfugu-research-record-2026-06-25.md), [brief](plans/openfugu-technical-brief-2026-06-25.md), [plan](plans/openfugu-reference-plan-2026-06-25.md)
- 2026-06-25 Skills/memory/agent tooling survey — Superpowers, Spec Kit, Karpathy skills, mem0, ChatGPT Memory, LLM Wiki, MemPalace, Hermes Agent, Oh My Pi, and Oh My OpenAgent are references; no new core skill/runtime/memory dependency without a verified local gap → [skills](plans/skills-and-spec-systems-research-2026-06-25.md), [memory](plans/memory-mechanisms-research-2026-06-25.md), [tooling](plans/agent-tooling-research-2026-06-25.md)
- 2026-06-25 Memory-to-artifact promotion list — add prompt lenses for artifact promotion, workflow acquisition, and external adoption review; still no new core workflow skill or runtime → [artifact promotion](04-agent/artifact-promotion.md), [workflow acquisition](04-agent/workflow-acquisition.md), [external adoption](04-agent/external-adoption-review.md)
- 2026-06-25 Rounds 83–101 panels — cross-category library-registry DRY series: Primary-workflow-surface parity, Human Review preamble guards and required/exempt set parity, contract-heading / score-floor / cross-link / coverage / path / governance-surface-path registries in `plans/tests/` → [record](plans/multi-agent-panel-consensus-2026-06-25.md)
- 2026-06-25 Rounds 69–82 panels — standardized prompt contracts (Purpose/Scope/Acceptance/Falsifiability) across all seven prompt categories, thinking ↔ engineering/skill cross-links with reciprocal pytest, Module Contract escalation anti-drift, governance pytest mirrors → [record](plans/multi-agent-panel-consensus-2026-06-25.md)
- 2026-06-25 Post-Round 68 holdout expansion — ROUTE-003 minimality trap + thin adversarial group refresh (15 groups / 53 phrases) → [QUALITY_GATES_SUMMARY.md](plans/QUALITY_GATES_SUMMARY.md)
- 2026-06-11 Add `runtime-trust-boundary` as a lens, not a ninth skill → [record](plans/project-adjustment-reflection-2026-06-11.md)
- 2026-06-17 Adopt a minimal project-judgment contract instead of importing Knowie → [initial record](plans/knowie-project-knowledge-reflection-2026-06-17.md)
- 2026-06-17 Refine the contract from non-normative to non-authoritative, connect promotion, and publish a reusable scaffold → [decision](plans/project-knowledge-authority-promotion-decision-2026-06-17.md)
- 2026-06-18 Adopt STORM's source-grounded perspective discovery as an optional `reflective-research` method, not a new skill → [record](plans/storm-perspective-discovery-reflection-2026-06-18.md)
- 2026-06-20 Synthesize external-adoption case studies, then correct the evidence and promotion-gate scope after the Test Plan routing counterexample → [record](plans/external-adoption-case-studies-2026-06-20.md)
- 2026-06-21 Evaluate Hyperplan / multi-agent adversarial planning — no change (runtime = non-goal; methodology overlaps; possible gaps not promoted) → [record](plans/external-adoption-case-studies-2026-06-20.md)
- 2026-06-25 Post-Round 68 holdout refresh — ROUTE-002 design-comparison variant; ROUTE-003 approved-spec plan-only + dispatch-meta paraphrases → [QUALITY_GATES_SUMMARY.md](plans/QUALITY_GATES_SUMMARY.md)
- 2026-06-25 Post-Round 68 cheatsheet parity — ROUTE-002 design-comparison holdout phrase + ROUTE-003 dispatch-meta probe in EN/zh-TW cheatsheets → [QUALITY_GATES_SUMMARY.md](plans/QUALITY_GATES_SUMMARY.md)
- 2026-06-25 Post-Round 68 holdout expansion — ROUTE-002 design comparison phrase; ROUTE-003 approved-spec plan-only trap + dispatch routing probe → [ROUTING_CONTRACT.md](plans/ROUTING_CONTRACT.md#r11-approved-spec-delivery)
- 2026-06-25 Round 68 panel — full-doc drift sync, README/methodology-map anti-drift, reject holdout expansion at 100% → [record](plans/multi-agent-panel-consensus-2026-06-25.md)
- 2026-06-25 Post-Round 68 maintenance — nine-skill wording parity (METHODOLOGY_MAP, skill-map, QUALITY_GATES), benchmark B024 dispatch (24 tasks, 9/9 workflows) → [QUALITY_GATES_SUMMARY.md](plans/QUALITY_GATES_SUMMARY.md)
- 2026-06-25 Round 67 panel — CONTRIBUTING R8–R12 sync, ROUTING_CONTRACT related artifacts, contract anti-drift tests → [record](plans/multi-agent-panel-consensus-2026-06-25.md)
- 2026-06-25 Round 66 panel — R12 boundary quick-cue contract, probe-snippet anti-drift, reject quick-cue expansion → [record](plans/multi-agent-panel-consensus-2026-06-25.md)
- 2026-06-25 R11 zh-TW approved-spec delivery holdout — mixed-language ROUTE-003 phrases + router fairness → [ROUTING_CONTRACT.md](plans/ROUTING_CONTRACT.md#r11-approved-spec-delivery)
- 2026-06-25 R11 approved-spec delivery routing — `implement_not_plan_trap` fix, ROUTE-003 back to 100%, contract + anti-drift test → [ROUTING_CONTRACT.md](plans/ROUTING_CONTRACT.md#r11-approved-spec-delivery)
- 2026-06-25 Rounds 51–65 panel — brief-before-plan, design comparison, dispatch-meta, readme plain review holdouts → [record](plans/multi-agent-panel-consensus-2026-06-25.md)
- 2026-06-25 Round 21 panel audit — no implementation blockers; recurrence-gated backlog formalized; QUALITY_GATES drift fixed → [record](plans/multi-agent-panel-consensus-2026-06-25.md)
- 2026-06-25 Rounds 36–50 panel — plan-only/plain-review holdouts, production-negation boundaries, ROUTE-002/003 expansion → [record](plans/multi-agent-panel-consensus-2026-06-25.md)
- 2026-06-25 Rounds 8–20 panel — milestones closed, ROUTE-003 adversarial eval, skill examples gate, maintenance playbook → [record](plans/multi-agent-panel-consensus-2026-06-25.md)
- 2026-06-25 Round 7 panel — AGENTS harness-policy alignment, zh-TW ROUTE-002 holdout, metrics sync → [record](plans/multi-agent-panel-consensus-2026-06-25.md)
- 2026-06-25 Round 6 panel — undocumented-decisions warning, ROUTE-002 holdout expansion, benchmark fixture CI, reject full SKILL i18n → [record](plans/multi-agent-panel-consensus-2026-06-25.md)
- 2026-06-25 Round 5 panel — ROUTE-002 holdout expansion, context_load deferral rule, reject benchmark-in-CI → [record](plans/multi-agent-panel-consensus-2026-06-25.md)
- 2026-06-25 Round 4 panel close — Minimality Signal Scan, ROUTE-002 in CI, partial TW localization → [record](plans/multi-agent-panel-consensus-2026-06-25.md)
- 2026-06-25 Multi-agent panel rethink — consensus: freeze nine skills, L1 fast path, context_load metadata, optional multi-voice in research; reject reflective-panel skill → [record](plans/multi-agent-panel-consensus-2026-06-25.md)
