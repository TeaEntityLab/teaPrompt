---
name: reflective-dispatch
description: Use this when a user asks to apply the Reflective Prompt Library, convert prompts into skills or workflows, choose prompt-only vs artifact vs agentic workflow, or route a non-trivial task before execution. It selects the smallest useful reflective workflow and keeps Doing the right thing > doing things right.
---

# Reflective Dispatch

## Core Rule

Start with intent, not procedure:

```text
Doing the right thing > doing things right.
```

Use the smallest workflow that can produce a verifiable result. Do not create a large plan, agent swarm, or multi-file process unless the task actually needs state, tools, tests, or review.

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

## Output

For routing-only responses, keep it short:

```markdown
Mode:
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

