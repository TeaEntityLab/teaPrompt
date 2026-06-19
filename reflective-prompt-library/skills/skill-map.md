# Reflective Skill Map

This file maps the prompt library into a small skill/workflow set.

## Core Architecture

Prompt is the entry point, Skill is the action, Context is the memory, Quality Gate is the reality check, and Human Review is the high-risk insurance.

The library contains many prompts, but the workflow layer intentionally stays compact:
eight lifecycle skills plus one cross-cutting minimality gate.

1. `reflective-dispatch`
2. `reflective-brief`
3. `reflective-spec-plan`
4. `reflective-implement`
5. `reflective-review`
6. `reflective-research`
7. `reflective-risk`
8. `reflective-handoff-retro`
9. `reflective-minimality`

This keeps invocation simple while preserving prompt depth as source material.

## Module Contract Standard

To ensure structural consistency across the repository, two contract forms are supported:

### 1. Active Core Contract (5-Field)
The active core implementation of the workflow skills utilizes a highly compact, operational contract to maximize context efficiency during runtime execution:

*   **Trigger**: Intent signals for activation, not exact magic words.
*   **Methods**: The named reasoning or execution procedures it utilizes.
*   **Output**: The minimum required artifact or response shape.
*   **Never**: Specific failure behaviors the skill must avoid.
*   **Escalation**: When to route to another skill or require Human Review.

*Example: [reflective-review/SKILL.md](reflective-review/SKILL.md#L13-L37).*

### 2. Target Design Schema (9-Field Specification)
For complex domain packs, external workflows, or future evolutions of the core library, the recommended standard specification is expanded to support thorough governance:

*   **Trigger**: Cues and activation conditions.
*   **Goal**: Actionable definition of what the skill must accomplish.
*   **Inputs**: Required background data, files, or state.
*   **Procedure**: Step-by-step reasoning or tool checklists.
*   **Output**: The target response shape or deliverable format.
*   **Quality Gate**: Hard verification criteria to prevent false success.
*   **Failure Modes**: Pitfalls, cognitive fallacies, or bugs to avoid.
*   **Human Review**: Exact halting criteria for developer sign-off.
*   **Handoff**: State transfer formats for multi-agent workflows.

Routing fairness rule:
- Same intent should map to the same canonical route even when phrasing differs.
- Trigger cues are examples, not a required phrase list.

## Prompt-to-Skill Mapping

| Prompt Area | Workflow Skill |
| --- | --- |
| Core minimal, core short, master, daily minimal, global controller | `reflective-dispatch`, `reflective-brief` |
| Socratic, critical thinking, counterargument, falsifiability, Why/What/How/Done | `reflective-brief`, `reflective-review` |
| Task start, spec writer, usage-first, task slicer, test designer (plan-only), workflow engine, SOP compiler | `reflective-spec-plan`, with `04-agent/sop-compiler.md` as supporting source material |
| Implementation agent, executable tests, test design during code work, local feedback, Codex/OpenCode | `reflective-implement` |
| Code reviewer, review-rating-fix | `reflective-review` |
| Minimality, anti-overengineering, YAGNI, stdlib/native/dependency ladder | `reflective-minimality`, with `reflective-review` or `reflective-implement` as needed |
| Context engineering, long context, Gemini long document, research, scaffold provenance | `reflective-research`, with `04-agent/agent-scaffold-provenance.md` as supporting source material |
| High-risk and runtime trust boundaries | `reflective-risk`, with `04-agent/runtime-trust-boundary.md` as supporting source material |
| Context handoff, retro, memory consolidation | `reflective-handoff-retro` |

## Installation Notes

For Claude Code project skills, copy each skill directory into:

```text
.claude/skills/<skill-name>/SKILL.md
```

For Codex/OpenCode-style local libraries, keep the current directory as source and copy/adapt only the skills you actually use.
