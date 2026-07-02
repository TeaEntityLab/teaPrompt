# Workflow Recipes

This file captures recommended prompt compositions and workflow sequences.


## Purpose

Document composable prompt and workflow recipes. Primary workflow surfaces: `reflective-dispatch`, `reflective-brief`, and `reflective-spec-plan`. Pairs with `01-thinking/socratic-reviewer.md`, `01-thinking/critical-thinking-check.md`, and `01-thinking/why-what-how-done.md`.

## Scope

- In scope: recipe sequences linking thinking lenses, engineering prompts, and agent patterns.
- Out of scope: replacing frozen workflow skill contracts or router fairness rules.

## Acceptance Criteria

- Each recipe names a starting strictness level and expected artifacts.
- Thinking lenses appear before execution prompts in general sequences.
- High-blast-radius recipes include a risk or review gate.

## Falsifiability

Name one recipe that would fail if run without the thinking-lens preamble steps.

## General Thinking

Start: L1–L2. Artifacts: a decision note with explicit assumptions.

```text
Socratic Prompt
-> Critical Thinking Prompt
-> Why / What / How / Done
-> Decision
```

## Engineering Task

Start: L3. Artifacts: spec, task slices, implementation diff with tests,
review notes, retro entry.

```text
Task Start Prompt
-> Spec Writer
-> Usage-first
-> Task Slicer
-> Implementation Agent
-> Code Review
-> Test Designer
-> Retro
```

## High-risk Task

Start: L4. Artifacts: assumption audit, threat model, dry-run plan, Human
Review record, rollback check. The Human Review gate is mandatory, not
optional.

```text
High-risk Prompt
-> Assumption Audit
-> Threat Model
-> Dry-run Plan
-> Human Review
-> Implementation
-> Review
-> Rollback Check
```

## Long Research Task

Start: L2. Artifacts: document map, evidence-vs-inference synthesis, context
handoff note.

```text
Research Prompt
-> Document Map
-> Evidence Check
-> Counterargument
-> Synthesis
-> Context Handoff
```

## Agent System Design

Start: L3; move to L5 when the work is long-running and resumable. Artifacts:
agent selection record, spec, workflow engine plan, review ratings.

```text
Agent Selection Prompt
-> Why / What / How / Done
-> Spec Writer
-> Usage-first
-> Task Slicer
-> Workflow Engine Plan
-> Review-Rating-Fix
```

## Looper Topologies

Shared vocabulary with serving-layer micro-agent runtimes (Sakana Fugu, vLLM
Semantic Router loopers). Their core lesson: **the best loop is task-shaped** —
identify the task shape first, then pick the smallest topology. At the prompt
layer, `reflective-dispatch` is the recipe selector; these rows align its
routing vocabulary with the field's named patterns. Numeric budgets, runtime
traces, and enforcement belong to a serving runtime and stay out of scope here.

| Topology | Task-shape signal | Prompt-layer equivalent |
| --- | --- | --- |
| Confidence (escalate on low confidence) | High volume, easy-vs-hard mix, cost or latency pressure | `reflective-dispatch` Strictness Ladder: start L1/L2, escalate only when risk or ambiguity demands |
| Ratings (bounded parallel candidates) | Several plausible candidates under a hard concurrency cap | Parallel Lens Review with a fixed lens count; keep its falsifier |
| ReMoM (breadth, then synthesis contract) | High reasoning variance plus a strict output format | Multi-angle `reflective-research` passes, then synthesis against Acceptance Criteria from `reflective-brief` |
| Fusion (disagreement as signal) | Contested factual or judgment calls where one confident answer is brittle | Parallel Lens Review with disagreements preserved and counterargument before consensus |
| Workflows (roles under a budget) | Multi-step engineering with distinct planner/patcher/verifier roles | Engineering Task recipe + `workflow-engine.md` state model via `reflective-spec-plan` |

Caution transfer: consensus can amplify shared error. vLLM's grounded-fusion
findings default to *weighting* rather than *dropping* the least-consistent
response — three models can be confidently wrong together while the lone
dissenter is right. Mirror that in Parallel Lens Review: preserve
disagreements; never discard a dissent solely for being in the minority.

Falsifier: if these rows merely rename existing recipes without changing a
routing decision or improving shared vocabulary, this section is ceremony and
should be removed — see
[plans/vllm-micro-agent-research-record-2026-06-30.md](../plans/vllm-micro-agent-research-record-2026-06-30.md).

## Parallel Lens Review

Use this only when a conclusion needs adversarial multi-lens consensus before it becomes a decision, adoption recommendation, architecture direction, or project-knowledge entry. Do not use it for ordinary low-risk review.

Start: L2, or the gated level of the decision under review if higher.

```text
reflective-dispatch
+ evidence packet
+ parallel specialist lenses
+ synthesis with disagreements preserved
+ reflective-handoff-retro if the conclusion becomes durable knowledge
```

Expected artifacts: `local://<topic>-review-packet.md`, reviewer verdicts, and a consensus summary that separates observed evidence, author claims, and inference.

Falsifier: if one `reflective-review` or `reflective-research` pass would produce the same decision with enough evidence, this recipe is ceremony and should not run.

## Cost Modes

Strictness mapping: low-cost starts at L1–L2, medium-cost at L3, high-cost
strict at L4, agent/workflow at L5. Artifacts follow the recipes above at the
matching level.

Low-cost daily mode:

```text
core-short
+ socratic-reviewer
+ critical-thinking-check
+ why-what-how-done
```

Medium-cost engineering mode:

```text
AGENTS.md
+ spec-writer
+ usage-first
+ task-slicer
+ implementation-agent
+ code-reviewer
```

High-cost strict mode:

```text
master-prompt
+ high-risk
+ review-rating-fix
+ hidden eval
+ context-handoff
+ retro
```

Agent / workflow mode:

```text
prompt library
+ skills
+ scripts
+ state files
+ eval harness
+ dashboard
```

## Practical Principle

Do not put everything into one giant prompt. Prefer:

```text
core identity prompt
+ task prompt
+ situation prompt
+ validation prompt
```

