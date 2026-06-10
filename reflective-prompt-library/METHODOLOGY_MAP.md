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
5. **Workflow & Agentic Layer** (`04-agent/`): Workflow engines, recipes (Review-Rating-Fix), and memory/knowledge consolidation prompts.
6. **Domain Pack Layer** (`05-domain/`): Specialized domain overlays (business strategy, learning coach, high-risk review, creative/writing).
7. **Repository Template Layer** (`06-repo/`): Local repository instructions (`AGENTS.md`, `cursor-rules.md` templates).
8. **Skill / Action Layer** (`skills/`): Modular, on-demand `SKILL.md` files acting as portable procedures executed when triggered.
9. **Quality Gate / Verification Layer** (Evals/Review): Robust feedback loops, verification checklists, and rating/regression defense mechanisms.
10. **Governance / Capability Risk Layer** (Risk/Compliance): Security boundaries, non-disclosure policies, high-risk review gates, and credential/tool protection.

## Strictness Levels

| Level | Use When | Main Surface |
| --- | --- | --- |
| 1. Daily prompting | Low-risk, short answer, no state | `00-core/daily-minimal.md` |
| 2. Reflective analysis | Complex reasoning or decision | `reflective-brief` |
| 3. Engineering task | Code, system design, data flow, tests | `reflective-spec-plan` -> `reflective-implement` |
| 4. High-risk review | Security, privacy, money, deletion, production | `reflective-risk` |
| 5. Agent workflow | Long-running, multi-tool, resumable work | `reflective-dispatch` + workflow plans |
| 6. Strategy overlay | Business, education, organization, long-term systems | `05-domain/` prompts as overlays |

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
| Workflow & Agentic Layer | Aligned | Complete | Workflows, planning engine, and memory consolidation (`04-agent/`). |
| Domain Pack Layer | Aligned | Complete | Keep strategy and domain prompts in `05-domain/`. |
| Repository Template Layer | Aligned | Complete | Maintain `AGENTS.md` and `cursor-rules.md` templates under `06-repo/`. |
| Skill / Action Layer | Aligned | Complete | Maintain 8 core composable skills. |
| Quality Gate / Verification | Aligned | Complete | Standardize skill-level quality checks. |
| Governance / Capability Risk | Aligned | Complete | Use `reflective-risk` for high-risk boundaries. |
