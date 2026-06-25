Language: English | [繁體中文](METHODOLOGY_MAP.zh-TW.md)

# Methodology Map

## Core Conclusion

TeaPrompt should not unify every method into one master prompt. The core architecture is a **Feedback-Gated Engineering Workflow** rather than a single monolithic "Reflective Engineering Agent".

The correct model is:

```text
Classify the task
-> choose the strictness level
-> compose the smallest useful prompt or workflow
-> verify with evidence via Quality Gates
```

The repository serves as a structured substrate of methods, context artifacts, and composable workflow skills, rather than a single giant instruction set.

## Governance Panel Record

Multi-voice Socratic deliberation (single host, six lenses) is recorded at
[plans/multi-agent-panel-consensus-2026-06-25.md](plans/multi-agent-panel-consensus-2026-06-25.md).
It is a judgment method inside `reflective-research`, not a runtime orchestrator.

## Positioning: Skills as Natural-Language Harness Policy

The 2026 agent literature gives this library a precise external frame. In current
usage (still contested — see the post-ICLR 2026 terminology debate):

- **Harness** — the execution layer around a model: calls it, runs tools, decides
  when to stop. *Agent = Model + Harness.*
- **Scaffold** — the behavior-defining layer inside the harness: prompts, tool
  descriptions, context management.
- **Skills** — externalized procedural expertise, loaded on demand.

Under this vocabulary, the `skills/` layer is **natural-language harness policy**:
editable documents that describe run-level execution behavior, interpreted by the
runtime (Claude Code, Codex, etc.) rather than hard-coded — the pattern formalized
as Natural-Language Agent Harnesses (arXiv [2603.25723](https://arxiv.org/abs/2603.25723)).
The library's broader bet — capability moved into memory, skills, and harness rather
than weights — matches the Weights → Context → Harness progression described in the
externalization review (arXiv [2604.08224](https://arxiv.org/abs/2604.08224)); see
also the [HuggingFace agent glossary](https://huggingface.co/blog/agent-glossary).
The State Ledger / Sufficiency Gate / Budget Rule sections in the long-horizon
skills apply the state-externalizing-harness design from Harness-1
(arXiv [2606.02373](https://arxiv.org/abs/2606.02373)); rationale in
`plans/harness-1-state-ledger-research.md`.

The NLAH paper — which cites `SKILL.md`-style files as a direct inspiration —
distills five design principles for harness-policy documents that this library's
skill contracts should continue to follow:

1. **State the task contract first** — inputs, outputs, allowed tools, and the
   condition under which the run is complete.
2. **Separate stages from mechanisms** — name the phases; delegate exact
   operations to scripts or tools.
3. **Make state and evidence explicit** — say where state is stored and which
   artifacts later steps must reopen.
4. **Write module boundaries for ablation** — name each module so it can be
   removed or tested cleanly.
5. **Prefer simple and enforceable language** — *"Phrases such as 'be careful,'
   'think deeply,' or 'act like an expert' are weak harness policy because they
   do not define observable behavior."*

The externalization review adds the matching success criterion for any
memory/ledger artifact: not "how much did we save?" but **"did we make the
current decision legible?"**

## The 10-Layer Taxonomy

Instead of a single prompt, the methodology is formally structured into ten distinct layers:

1. **Core Instruction Layer** (`00-core/`): Global custom instructions, system behaviors, and base settings.
2. **Reasoning / Thinking Layer** (`01-thinking/`): Socratic inquiry, critical analysis, falsifiability, and assumption auditing.
3. **Engineering / Execution Layer** (`02-engineering/`): Domain-specific engineering procedures (TDD, spec writing, implementation strategies).
4. **Context Window Layer** (`03-context/`): Context window sizing, token management, and context handoff prompts.
5. **Workflow & Agentic Layer** (`04-agent/`): SOP compiler prompts, workflow engines, recipes (Review-Rating-Fix), and memory/knowledge consolidation prompts.
6. **Domain Pack Layer** (`05-domain/`): Specialized domain overlays (business strategy, learning coach, high-risk review, creative/writing).
7. **Repository Template Layer** (`06-repo/`): Local repository instructions
   (`AGENTS.md`, `cursor-rules.md`) and a non-authoritative project-knowledge
   scaffold for project-specific design judgement.
8. **Skill / Action Layer** (`skills/`): Modular, on-demand `SKILL.md` files acting as portable procedures executed when triggered.
9. **Quality Gate / Verification Layer** (Evals/Review): Robust feedback loops, verification checklists, and rating/regression defense mechanisms.
10. **Governance / Capability Risk Layer** (Risk/Compliance): Security boundaries, non-disclosure policies, high-risk review gates, credential/tool protection, and runtime trust boundaries for data, tools, context, and side effects.

## Runtime Trust Boundary Addendum

Recent agent-runtime references reinforce that governance is not only a high-risk review step. It is also a context assembly and authority problem:

- The OpenAI Model Spec treats quoted text, attachments, multimodal content, and tool outputs as untrusted data by default unless higher-authority instructions explicitly delegate authority: [OpenAI Model Spec](https://model-spec.openai.com/2025-12-18.html).
- MCP security guidance emphasizes consent for local servers, sandboxing, token audience separation, and progressive least-privilege scopes: [MCP Security Best Practices](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices).
- Apple's Foundation Models update points toward task-specific models/adapters, guided generation, tool calling, feature-specific evaluation, and prompt injection mitigation: [Apple Foundation Models 2025 update](https://machinelearning.apple.com/research/apple-foundation-models-2025-updates).

TeaPrompt should absorb these as a lightweight runtime governance sublayer, not as a monolithic agent constitution. Use `04-agent/runtime-trust-boundary.md` when a task involves external content, tool results, entity-like records, context assembly, or side-effectful actions.

## Scaffold Provenance Addendum

Public prompt mirrors and alleged system-prompt leaks are useful only as provenance-sensitive research artifacts. The elder-plinius `CLAUDE-FABLE-5.md` mirror is observable as a third-party GitHub artifact, while Anthropic's official docs separately confirm Claude app system prompts, Claude Fable 5 release behavior, long-run scaffolding guidance, refusal categories, and reasoning-output limits. That distinction matters.

TeaPrompt should learn the taxonomy: identity, behavior, safety, memory, tool routing, artifact/workspace policy, evidence/citation/copyright, and reasoning protection. It should not copy leaked or mirrored scaffold text into operational skills. Use `04-agent/agent-scaffold-provenance.md` when comparing official docs, mirrors, user attachments, and community interpretations.

## SOP Compiler Addendum

`agentic-sop-to-work` demonstrates a useful adjacent pattern: treat human SOP as source material, compile it into single-purpose workflow stages, exchange typed artifacts, run deterministic gates, return DRAFT outputs for human approval, and use regression hooks only when the workflow has enough repeatability or risk to justify code-backed enforcement: [agentic-sop-to-work](https://github.com/s0912758806p/agentic-sop-to-work).

TeaPrompt should adopt this as a planning lens, not a runtime dependency. The project remains a compact prompt and skill library until repeated workflows prove that runner code, hooks, and deterministic verifiers would reduce total cost. Use `04-agent/sop-compiler.md` before promoting a prompt-only or artifact-only process into a code-backed workflow engine.

## Project-Knowledge Addendum

A project can need normative product and architecture principles without giving
those principles agent-instruction authority. TeaPrompt therefore separates two
questions: what should guide project-design judgement, and what authorizes an
agent to act. The first may live in project knowledge; the second belongs in
`AGENTS.md`, `SKILL.md`, higher-authority instructions, and explicit user
authorization.

Start with [`06-repo/PROJECT_KNOWLEDGE.template.md`](06-repo/PROJECT_KNOWLEDGE.template.md)
rather than a full memory taxonomy. Use `reflective-handoff-retro` to propose
evidence-backed promotions with destination, authority class, provenance,
approval, and retirement trigger. Promote a repeated operation to a
project-local skill only after its inputs, outputs, failure signals, and checks
are stable and a human confirms the promotion.

## Multi-Agent Panel Consensus Addendum

The 2026-06-25 multi-lens Socratic panel (six provider perspectives, single host)
reaffirmed the north star: **nine frozen workflow skills**, strictness-first routing,
evidence-backed evals in CI, optional multi-voice synthesis in `reflective-research`
— not a swarm runtime. Judgment record:
[plans/multi-agent-panel-consensus-2026-06-25.md](plans/multi-agent-panel-consensus-2026-06-25.md).

## Strictness Levels

| Level | Use When | Main Surface |
| --- | --- | --- |
| 1. Daily prompting | Low-risk, short answer, no state | `00-core/daily-minimal.md` |
| 2. Reflective analysis | Complex reasoning or decision | `reflective-brief` |
| 3. Engineering task | Code, system design, data flow, tests | `reflective-spec-plan` -> `reflective-implement` |
| 4. High-risk review | Security, privacy, money, deletion, production | `reflective-risk` |
| 5. Agent workflow | Long-running, multi-tool, resumable work | `reflective-dispatch` + workflow plans |
| 6. Strategy overlay | Business, education, organization, long-term systems | `05-domain/` prompts as overlays |

## Level Taxonomy Reference

The repository uses two distinct L-level taxonomies. To avoid ambiguity, every L-level reference should be qualified by its taxonomy name.

| Canonical Taxonomy | Levels | Source | Purpose |
| --- | --- | --- | --- |
| Strictness Level | L1-L6 | `skills/reflective-dispatch/SKILL.md` (also the Strictness Levels table above) | Execution rigor: how deeply to validate, review, and gate the work. L1 = daily prompting, L6 = strategy overlay. |
| Formalization Level | L0-L4 | `04-agent/sop-compiler.md` | Automation depth: how much of a process is codified into a machine-executable workflow. L0 = prompt-only, L4 = runner with gates and hook. |

**Rule:** Write `Strictness L3` or `Formalization L3` — never bare `L3`. When the taxonomy is clear from surrounding context (e.g., a "Strictness:" field in a dispatch record), the qualifier may be omitted, but the first reference in any document should be explicit.

> See [GLOSSARY.md](GLOSSARY.md) for operational definitions of both taxonomies
> and a worked example of the distinction.

## Classification Taxonomies Reference

The repository defines three distinct classification taxonomies. Each answers a different question and should be used independently.

| # | Canonical Taxonomy | Source | Question Answered | Levels |
| --- | --- | --- | --- | --- |
| 1 | Execution Mode Selection | `04-agent/agent-selection.md` | Which execution mode fits this task? | Prompt-only → Prompt+Artifact → Agentic Coding → Workflow Engine → Full Agent System |
| 2 | Formalization Level | `04-agent/sop-compiler.md` | How much of this process should be codified? | L0 (prompt-only) → L4 (runner with gates and hook) |
| 3 | Strictness Level | `skills/reflective-dispatch/SKILL.md` | How much validation and review does this task require? | L1 (daily prompting) → L6 (strategy overlay) |

Use Taxonomy 1 when deciding whether to use a prompt, an artifact, a coding agent, or a full workflow engine. Use Taxonomy 2 when designing the automation depth of a repeatable process. Use Taxonomy 3 when routing a task to the appropriate reflective workflow skill.

## What Should Be Combined

### Reflective Engineering + Why / What / How / Done

These belong together in the execution flow.

- **Why**: goal, user value, cost of wrong problem
- **What**: scope, inputs, outputs, acceptance criteria
- **How**: options, risks, tests, rollback
- **Done**: evidence, verification, residual risk

### Socratic Review + High-risk Review

Use heavier critical thinking only when risk justifies it.

- Assumption audit
- Evidence check
- Counterargument
- Fallacy scan
- Falsifiability
- Human review gate

### Prompting-only + Rubric / Checklist

This is the best daily mode.

- Goal
- Assumptions
- Classification
- Strategy
- Risks
- Acceptance criteria

## What Should Not Be Forced Together

### Learning Science Is Not the Engineering Workflow

Education and cognition concepts can inspire prompt design, but they should not become the default engineering agent process. Use them for learning systems, language practice, feedback loops, and cognitive-load control.

### Business Strategy Is Not the Prompt Core

Business frameworks help define Why, but they should not be injected into every task. Use them when the task is product, market, organization, or transformation strategy.

### Multi-agent Workflow Is Not a Single Prompt

Multi-agent work requires state, tools, logs, verification, and handoff artifacts. A prompt can describe the pattern but cannot replace the runtime.

## Repo Fit Check

| Category / Layer | Current Repo Fit | Status | Action Needed |
| --- | --- | --- | --- |
| Core Instruction Layer | Aligned | Complete | Maintain minimal base footprint. |
| Reasoning / Thinking | Aligned | Complete | Keep prompts under `01-thinking/`. |
| Engineering / Execution | Aligned | Complete | Prompts under `02-engineering/`. |
| Context Window Layer | Aligned | Complete | Manage window-size & token configurations (`03-context/`). |
| Workflow & Agentic Layer | Aligned | Extended | Workflows, SOP compiler planning, planning engine, and memory consolidation (`04-agent/`). |
| Domain Pack Layer | Aligned | Complete | Keep strategy and domain prompts in `05-domain/`. |
| Repository Template Layer | Aligned | Extended | Maintain instruction templates and the reusable project-knowledge scaffold under `06-repo/`. |
| Skill / Action Layer | Aligned | Extended | Maintain 8 lifecycle skills plus a narrow minimality gate for anti-bloat decisions. |
| Quality Gate / Verification | Aligned | Complete | Standardize skill-level quality checks. |
| Governance / Capability Risk | Aligned | Extended | Use `reflective-risk` for high-risk boundaries and `04-agent/runtime-trust-boundary.md` for instruction/data/tool authority review. |
