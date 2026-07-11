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

1. Deterministic code owns control flow; the model owns step content. All five vendors now separate "workflow" (code-driven) from "agent" (model-driven) and recommend moving unreliable orchestration into scripts.
2. Six recurring topologies: sequential pipeline, parallel fan-out/fan-in, conditional routing, loop-until-verified, orchestrator-workers, handoff. Names differ; semantics converge.
3. External verification as stop condition ("truth layer"): never trust the model's self-reported "done"; gate on exit codes of deterministic checks.
4. State files / checkpoints between steps enable resume; every platform ships checkpointing or a state-ledger convention.
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

Verified gap: no surface tells an agent how to *write an executable flow-control script* (pipeline/parallel/router/orchestrator/loop) for a host agent CLI with gates, budgets, and resumable state. User instruction on 2026-07-11 explicitly requested such skills, supplying the human authorization the promotion gate requires.

## Promotion Decision

- Destination: two domain-pack skills under `skills/` — `flow-control-generator` (one-pass DAG flows) and `flow-loop-harness` (iterative loops; separate because runaway-cost/side-effect risk differs and triggers are disjoint).
- Acquisition level: L2 (skill draft) with an L3 property built in: every generated script must support a stub dry run (`AGENT_CMD` override) as a deterministic verifier.
- Explicitly **not** core workflow skills: the nine-skill routing surface and cheatsheet are unchanged; the pack is reachable by host-harness skill discovery and by escalation notes inside the pack.
- TeaPrompt still operates no runtime: generated scripts run on the host; their operational guarantees are the host's to prove.

## Demotion Triggers

- Zero invocations after three months, or generated scripts repeatedly fail stub dry runs → fold both skills back into a reference section of `workflow-recipes.md` and retire the pack.
- A host-native flow feature (e.g., a first-party goal/loop mode) covering all pack templates with enforcement → demote the loop skill first (host-native beats local scripts).

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
