# Methodology Map

## Core Conclusion

TeaPrompt should not unify every method into one master prompt.

The correct model is:

```text
Classify the task
-> choose the strictness level
-> compose the smallest useful prompt or workflow
-> verify with evidence
```

The repository should stay as a map of methods plus a small workflow layer, not a single giant methodology.

## Method Families

| Family | Source Tradition | Purpose | Repo Surface |
| --- | --- | --- | --- |
| Reflective engineering | Software engineering, requirements, TDD, RCA | Produce verifiable engineering artifacts | `00-core/`, `02-engineering/`, `reflective-implement` |
| Why / What / How / Done gates | Product management, delivery governance | Decide direction before execution | `01-thinking/why-what-how-done.md`, `reflective-brief` |
| Socratic and critical thinking | Philosophy, critical thinking, scientific method | Audit assumptions and evidence | `01-thinking/`, `reflective-review`, `reflective-risk` |
| Prompting-only | LLM prompting practice | Improve one-shot or short-session outputs | `00-core/`, context prompts |
| Agentic workflow | AI agents, tool use, orchestration | Handle long, stateful, multi-tool tasks | `04-agent/`, `skills/`, `plans/agent-workflows-plan.md` |
| Evaluation and governance | QA, observability, AI safety | Prevent false success and unsafe actions | `reflective-review`, `reflective-risk`, `reflective-implement` |
| Education and cognition | Learning science, language acquisition | Design learning systems and reduce cognitive load | `05-domain/learning-coach.md` |
| Business and transformation | Product strategy, organization design, AI transformation | Analyze market, product, and organization choices | `05-domain/business-strategy.md` |
| Systems and toolchain | Architecture, automation, durable execution | Design tool-enabled systems | `04-agent/workflow-engine.md`, `plans/code-followups-plan.md` |

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

These belong together.

- Why: goal, user value, cost of wrong problem
- What: scope, inputs, outputs, acceptance criteria
- How: options, risks, tests, rollback
- Done: evidence, verification, residual risk

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

Education and cognition concepts can inspire prompt design, but they should not become the default engineering agent process.

Use them for learning systems, language practice, feedback loops, and cognitive-load control.

### Business Strategy Is Not the Prompt Core

Business frameworks help define Why, but they should not be injected into every task.

Use them when the task is product, market, organization, or transformation strategy.

### Multi-agent Workflow Is Not a Single Prompt

Multi-agent work requires state, tools, logs, verification, and handoff artifacts. A prompt can describe the pattern but cannot replace the runtime.

## Recommended Additions

The current repo already covers the core workflow well. The useful additions are maps and guardrails, not more skills.

Recommended:

1. Keep `skills/` small.
2. Keep operational docs English.
3. Add this methodology map as the classification surface.
4. Add a language policy to clarify bilingual prompt sources.
5. Consider a future `EVALS.md` only after there are runnable evals.
6. Consider a future `locales/zh-TW/` migration only if English-only publication becomes a requirement.

Not recommended now:

- Adding separate skills for every methodology.
- Adding hooks or installers before usage pain is observed.
- Translating all prompt source files without a clear publication requirement.
- Adding agent runtime code before the workflows prove repetitive enough.

## Repo Fit Check

| Claim From Review | Current Repo Fit | Needed Action |
| --- | --- | --- |
| Classification is better than unification | Mostly aligned | Keep 8 workflow skills; add this map |
| Skills should be practical workflows | Aligned | No new skill explosion |
| High-risk work should get extra critique | Aligned | `reflective-risk` already covers it |
| Education/business should be overlays | Mostly aligned | Keep them in `05-domain/`, not core skills |
| Agent workflow needs state and artifacts | Aligned | Plans exist; no runtime needed yet |
| Repo language should be clear | Gap | Add `LANGUAGE_POLICY.md` |
| Evaluation/governance deserves explicit visibility | Partial | Document here; defer runnable evals |

