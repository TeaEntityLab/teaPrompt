---
name: reflective-dispatch
description: Use this when a user asks to apply the Reflective Prompt Library, convert prompts into skills or workflows, choose prompt-only vs artifact vs agentic workflow, or route a non-trivial task before execution. It selects the smallest useful reflective workflow and keeps Doing the right thing > doing things right.
license: MIT
---

# Reflective Dispatch

## Core Rule

Start with intent, not procedure:

```text
Doing the right thing > doing things right.
```

Use the smallest workflow that can produce a verifiable result. Do not create a large plan, agent swarm, or multi-file process unless the task actually needs state, tools, tests, or review.

## Module Contract

Trigger:
- Use when the request asks to apply this library, choose prompt-only vs workflow, or route a task that mixes planning, risk, research, and execution.

Methods:
- Task classification
- Strictness ladder
- Smallest useful workflow
- Risk gate routing

Output:
- For routing-only work, output `Mode`, `Strictness`, `Goal`, `Assumptions`, `Workflow`, `Human Review`, and `Next Action`.

Never:
- Do not create a large plan, agent swarm, or multi-file process when a smaller workflow can produce the result.
- Do not skip the risk gate when high-risk signals appear.
- Do not claim execution, tests, source review, or verification that did not happen.

Escalation:
- Route high-risk tasks to `reflective-risk` before execution.
- Route unclear tasks to `reflective-brief` or `reflective-spec-plan` before implementation.

## Route

Choose one primary workflow:

| Task shape | Use |
| --- | --- |
| Ambiguous request, decision, task kickoff | `reflective-brief` |
| Spec, usage design, ticket slicing, planning | `reflective-spec-plan` |
| Coding, refactor, debugging with edits | `reflective-implement` |
| Code/artifact/plan review, critique, rating | `reflective-review` |
| Current external research, DeepWiki, docs, long sources | `reflective-research` |
| Security, privacy, money, data loss, auth, production | `reflective-risk` first |
| Handoff, retro, memory consolidation | `reflective-handoff-retro` |

If more than one applies, pick one primary workflow and one gate. Example: coding a privacy-sensitive feature uses `reflective-risk` as the gate and `reflective-implement` as the execution workflow.

## Strictness Ladder

Choose the lowest strictness level that still controls risk:

| Level | Use When | Primary Workflow |
| --- | --- | --- |
| `L1` | Low-risk, short request, no state | `prompt-only` or `reflective-brief` |
| `L2` | Non-trivial analysis, still low-risk | `reflective-brief` |
| `L3` | Engineering work with files/tests | `reflective-spec-plan` -> `reflective-implement` |
| `L4` | High-risk actions or irreversible impact | `reflective-risk` + execution workflow |
| `L5` | Long-running, multi-tool, resumable work | `reflective-dispatch` + workflow artifacts |
| `L6` | Strategy/education/business framing | Domain prompts as overlays, not core execution |

Escalate only when needed. De-escalate once risk is controlled.

## Output

For routing-only responses, keep it short:

```markdown
Mode:
Strictness:
Goal:
Assumptions:
Workflow:
Human Review:
Next Action:
```

## Guardrails

- If safe ambiguity remains, state assumptions and continue.
- If an irreversible or high-risk branch appears, stop for Human Review.
- Prefer artifacts over conversation memory for any task that may resume later.
- Prefer evidence over confidence. Do not claim tool execution, tests, source review, or verification that did not happen.
