# Agent Flow-Control Research Record — 2026-07-11

Research record for the `flow-control-generator` and `flow-loop-harness` domain-pack skills. Follows the external-adoption case-study discipline: mechanism-vs-product, evidence tiers preserved, promotion decision recorded.

## Purpose

Ground a "skills that write flow-control scripts" capability in the current (2026-07-11) flow concepts of the main LLM/agent platforms, and record the promotion decision that created two domain-pack skills.

## Scope

- In scope: named flow/orchestration patterns from Anthropic, OpenAI, Google, LangChain, and Microsoft; script-level loop-harness practice for headless agent CLIs; the local-gap analysis and promotion decision.
- Out of scope: adopting any external runtime or SDK as a TeaPrompt dependency; building a TeaPrompt-owned runner (Standing Non-Goal); router or cheatsheet changes for the nine core workflow skills.

## Acceptance Criteria

- Each platform's flow primitives are listed with an evidence tier and a primary-source pointer.
- Convergent cross-platform concepts are separated from single-vendor concepts.
- The promotion decision names the Acquisition level, the verified local gap, and the demotion trigger.

## Falsifiability

If the two skills are not invoked on a real task within three months, or a generated script cannot pass its own stub dry-run check, the pack should be demoted back to a reference record (see Demotion Triggers).

## Method

Web research on 2026-07-11 (six searches across vendor docs, engineering blogs, and practitioner reports), cross-checked against primary documentation URLs listed under Sources. Search-derived claims that could not be confirmed against a primary source are marked `[search-derived]`.

## Platform Findings

| Platform | Flow surface | Primitives (2026-07) | Evidence tier |
| --- | --- | --- | --- |
| Anthropic (Claude Agent SDK / Claude Code) | Code-first harness around the agent loop | Workflows-vs-agents split; prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer; subagents with isolated context; lifecycle hooks for gate enforcement; headless `claude -p` for scripted loops | Primary docs + vendor engineering post |
| OpenAI (Agents SDK) | Lightweight Python/TS SDK | Agents, handoffs (delegated ownership) vs agent-as-tool, guardrails (parallel fail-fast validation), sessions, tracing; visual Agent Builder being wound down in favor of code-first SDK `[search-derived]` | Primary docs; wind-down date unverified |
| Google (ADK) | Deterministic workflow agents | `SequentialAgent`, `ParallelAgent` (fan-out/gather), `LoopAgent` (repeat until condition/escalation); shared session state via `output_key`; composable nesting; A2A for cross-framework interop | Primary docs |
| LangChain (LangGraph 1.0, Deep Agents) | Durable graph runtime | Nodes/edges, conditional edges (router functions), cycles for iterate-until-done, checkpointing every node transition, resume-after-interrupt; Deep Agents pattern: planning artifact + virtual filesystem + subagents | Primary docs |
| Microsoft (Agent Framework) | Graph workflows over executors/edges | Sequential, Concurrent (fan-out/fan-in), Handoff, Group Chat, Magentic (manager with dynamic planning); checkpointing, human-in-the-loop pauses, typed messages, OpenTelemetry observability | Primary docs |
| Practitioner layer (harness engineering) | Shell/CI loop harnesses | "Ralph" loop: `while` loop around headless agent CLI + task ledger file; external verifier as the only trusted stop condition; permission pre-approval flags; per-iteration fresh context | Practitioner posts, convergent |

## Convergent Concepts (safe to build on)

1. Deterministic code owns control flow; the model owns step content. The surveyed vendor docs separate "workflow" (code-driven) from "agent" (model-driven) and recommend moving unreliable orchestration into scripts. Scope caveat: "surveyed" means the six sources below, not the whole field.
2. Six recurring topologies: sequential pipeline, parallel fan-out/fan-in, conditional routing, loop-until-verified, orchestrator-workers, handoff. Names differ; semantics converge.
3. External verification as stop condition ("truth layer"): never trust the model's self-reported "done"; gate on exit codes of deterministic checks.
4. State files / checkpoints between steps enable resume; each surveyed framework documents checkpointing or a state-ledger convention (a host guarantee where enforced by runtime code, a convention otherwise).
5. Budgets and caps (max iterations, concurrency caps, cost ceilings) are mandatory loop hygiene.
6. Human-in-the-loop pause points are first-class for side-effectful steps.

## Divergences and Cautions

- Handoff (transfer of conversation ownership) is OpenAI/Microsoft vocabulary; Anthropic/Google express the same need as routing plus subagent delegation. The skills treat handoff as a routing variant.
- Magentic-style dynamic re-planning is a manager-model behavior, not a scriptable control structure; scripts should expose re-planning as "orchestrator step re-runs planner", not imitate it in bash.
- Durability claims (LangGraph checkpoints, MAF checkpointing) are runtime guarantees of those hosts. A generated shell script's state ledger gives resume *convention*, not crash-safety *proof* — aligned with the runtime-trust-boundary lesson that prompt/spec text cannot provide operational guarantees.
- `[search-derived]` items (AgentKit visual-builder wind-down date; a native Claude Code `/goal` grader loop) were not confirmed against primary docs during this session and must be re-verified before being relied on.

## Local Gap Analysis

Existing TeaPrompt surfaces cover adjacent needs but not this one:

- `04-agent/workflow-engine.md` — plan-only stateful workflow *specification*; produces no runnable artifact.
- `04-agent/sop-compiler.md`, `04-agent/workflow-acquisition.md` — extract/replay SOPs from observed work; not forward script generation.
- `04-agent/workflow-recipes.md` — prompt-layer sequencing and looper-topology vocabulary; no execution layer.

Gap verdict (corrected by the 2026-07-11 panel): **user-directed, structurally plausible, recurrence evidence unknown.** No surface tells an agent how to *write an executable flow-control script* (pipeline/parallel/router/orchestrator/loop) for a host agent CLI with gates, budgets, and a resume-convention state ledger — but this does not meet the STORM/Test-Plan bar of "verified" (no recurring local demand is on record; adjacent methodology exists in `workflow-recipes.md` and `reflective-implement`). Signal accounting (`external-adoption-case-studies-2026-06-20.md`): external platform convergence on these patterns is interest evidence, never local recurrence evidence — the two ledgers stay separate. The explicit user instruction of 2026-07-11 supplies the human-approval half of the promotion gate; the recurrence half is waived only under the user-directed exception below, and the Demotion Triggers are the corresponding falsifiers.

## Promotion Decision

- Destination: two domain-pack skills under `skills/` — `flow-control-generator` (one-pass DAG flows) and `flow-loop-harness` (iterative loops; separate because runaway-cost/side-effect risk differs, triggers are disjoint, and the harness-readable `human_review_required` split would be lost in a merge).
- Status: **user-directed Acquisition L2 exception** (skill drafts), recorded with demotion triggers instead of recurrence evidence. The stub dry-run (`AGENT_CMD` override) is an L3-style verifier artifact only; full Acquisition L3 additionally requires the fail-closed security gates of `04-agent/artifact-promotion.md` §4 and replay evidence from a real task.
- Explicitly **not** core workflow skills: the nine-skill routing surface is unchanged; `reflective-dispatch` gains no route row. Discoverability is provided by the registered-domain-pack sections in `skills/skill-map.md` and the trigger cheatsheet, plus escalation notes inside the pack (2026-07-11 panel, RoutingDiscovery lens).
- Registration: `DOMAIN_PACK_SKILLS` in `plans/validate_skill_examples.py`, enforced by `plans/validate_governance.py` (unregistered-directory check, domain-pack self-label, no core context-load row) and the amended nine-core guard tests.
- TeaPrompt still operates no runtime: generated scripts run on the host; their operational guarantees are the host's to prove.

## Demotion Triggers

- Zero invocations after three months, or generated scripts repeatedly fail stub dry runs → fold both skills back into a reference section of `workflow-recipes.md` and retire the pack.
- A host-native flow feature (e.g., a first-party goal/loop mode) covering all pack templates with enforcement → demote the loop skill first (host-native beats local scripts).

## Panel Review and Candidate Adoption Ledger (2026-07-11)

The pack was adversarially reviewed the same day by a six-lens parallel panel — see [flow-control-pack-panel-record-2026-07-11.md](flow-control-pack-panel-record-2026-07-11.md). Consensus `AGREE WITH CHANGES` (6/6). A second six-lens panel the same day reviewed pack COVERAGE against the whole `plans/` survey corpus — see [flow-coverage-panel-record-2026-07-11.md](flow-coverage-panel-record-2026-07-11.md) (rows P8+). Panel ceremony is proportionate by design: pack-wide governance or coverage changes get a parallel-lens panel; routine L1–L2 template tweaks do not (`workflow-possibilities-constraints-review-2026-07-06.md`, Constraints Judged Too Rigid #6). Adoption state of the panels' candidates:

| # | Candidate | Status | Evidence | Next action / trigger |
| --- | --- | --- | --- | --- |
| P1 | Option B placement: CORE_SKILLS vs DOMAIN_PACK_SKILLS registry + guard amendment | Adopted 2026-07-11 | `plans/validate_skill_examples.py`, `plans/validate_governance.py`, amended tests in `plans/tests/` | none |
| P2 | Fix nine confirmed template bugs (B1–B9) | Adopted 2026-07-11 | Both SKILL.md templates; rig transcript in panel record | none |
| P3 | Runtime-boundary wording C1–C6 (resume convention, L2/L3 relabel, permission boundary, §4 gates) | Adopted 2026-07-11 | Both SKILL.md files; this record | none |
| P4 | Evidence relabel: gap = user-directed exception, tier caveats propagated | Adopted 2026-07-11 | This record, Convergent Concepts + Local Gap Analysis | none |
| P5 | Discoverability: skill-map + EN cheatsheet domain-pack sections; no dispatch route row | Adopted 2026-07-11 | `skills/skill-map.md`, `skills/SKILL_TRIGGER_CHEATSHEET.md`, guard test `test_skill_map_lists_domain_packs` | zh-TW cheatsheet parity when EN stable |
| P6 | Merge to one skill (Minimality lens) | Deferred | Panel record, Disagreements | Re-litigate if either skill sees zero solo invocations by 2026-10-11 |
| P7 | Router/quick-cue integration for pack boundaries | No-change decided 2026-07-11 | [P7/N12 decision](p7-pack-routing-decision-2026-07-11.md): three collision groups / 9 phrases passed 100% pre-tune; packs remain host-invoked | Re-open only on a documented TeaPrompt-local misroute/discoverability failure attributable to pack exclusion, or a host that cannot invoke registered packs directly |
| P8 | Coverage-panel governance wording: methodology-vs-operationalization in both Purposes; Never additions (platform-vocabulary mandate ban, gate tampering, epistemic-vs-execution fan-out, no last-response fallback, run-state ≠ project memory); demotion-trigger sections; stub≠deploy tier; recurrence-before-team-standard; generated-by provenance comment; timeout wording; orchestrator data-not-authority + Stop-Doing boundary | Adopted 2026-07-11 | Both SKILL.md files; guard `plans/tests/test_flow_pack_adoption_state.py` | none |
| P9 | Parallel quorum gate: `MIN_OK` explicit partial-failure policy (ReMoM `min_successful_responses`); strict default counts failures and non-empty outputs | Adopted 2026-07-11 | `flow-control-generator` parallel template; rig transcript in coverage panel record | none |
| P10 | Router route-trace observability + explicit fail-closed vs default-up policy comment (ROUTING_CONTRACT R4/R5) | Adopted 2026-07-11 | `flow-control-generator` router template; rig transcript | none |
| P11 | Loop state hygiene: RESUMED restart stanza, tail-as-compaction-budget wording, disposable `state/`, writer-critic deviation label, backlog constraint-tail comment | Adopted 2026-07-11 | `flow-loop-harness` Loop Anatomy + templates; rig transcript | none |
| P12 | Conductor-style DAG executor template (OpenFugu, stdlib topological order + visibility-scoped prompts) | Adopted 2026-07-12 (user-directed; recurrence `unknown`) | `flow-control-generator` §Template: DAG Executor; guards `plans/tests/test_dormant_item_watch.py`, `test_dormant_conditional_contracts.py` | Regenerate on host DAG primitive; `/batch`-solvable tasks do not need it |
| P13 | Dedicated multi-wave ReMoM template | Adopted 2026-07-12 (user-directed; recurrence `unknown`) | `flow-loop-harness` §Template: Multi-Wave Fan-out (composition note retained) | Prefer compose-first for single-wave work |
| P14 | `workflow-recipes.md` cross-references: Looper Topologies see-also block; Parallel Lens Review input-contract/merge-owner line | Adopted 2026-07-11 | `04-agent/workflow-recipes.md` | none |
| P15 | Frozen-core parity items (reflective-research Blind Spots section; historical-banner forward pointers) | **Resolved 2026-07-11** — prompt-layer change + no-change pair; frozen-surface gate not fired | [Parity review record](frozen-core-parity-review-2026-07-11.md) | none |

## Sources

Primary documentation (retrieved 2026-07-11):

- Anthropic, Building Effective Agents — https://www.anthropic.com/engineering/building-effective-agents
- Anthropic, Claude Agent SDK overview — https://docs.claude.com/en/api/agent-sdk/overview
- Anthropic, Claude Code headless/CLI — https://docs.claude.com/en/docs/claude-code/cli-reference
- OpenAI, Agents SDK — https://openai.github.io/openai-agents-python/
- Google, ADK workflow agents — https://google.github.io/adk-docs/agents/workflow-agents/
- A2A protocol — https://a2a-protocol.org/
- LangChain, LangGraph docs — https://langchain-ai.github.io/langgraph/
- LangChain, Deep Agents — https://blog.langchain.com/deep-agents/
- Microsoft, Agent Framework — https://learn.microsoft.com/en-us/agent-framework/
- Geoffrey Huntley, Ralph pattern — https://ghuntley.com/ralph/

Secondary/search-derived (2026-07-11 web search snapshots): Anthropic 2026 Agentic Coding Trends Report summary; AgentKit wind-down reports; practitioner loop-harness posts. Treat as `[search-derived]` until re-verified.
