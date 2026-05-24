# Reflective Skill Map

This file maps the prompt library into a small skill/workflow set.

## Design Choice

The library contains many prompts, but the workflow layer intentionally has only eight skills:

1. `reflective-dispatch`
2. `reflective-brief`
3. `reflective-spec-plan`
4. `reflective-implement`
5. `reflective-review`
6. `reflective-research`
7. `reflective-risk`
8. `reflective-handoff-retro`

This keeps invocation simple while preserving prompt depth as source material.

## Prompt-to-Skill Mapping

| Prompt Area | Workflow Skill |
| --- | --- |
| Core minimal, core short, master, daily minimal, global controller | `reflective-dispatch`, `reflective-brief` |
| Socratic, critical thinking, counterargument, falsifiability, Why/What/How/Done | `reflective-brief`, `reflective-review` |
| Task start, spec writer, usage-first, task slicer, workflow engine | `reflective-spec-plan` |
| Implementation agent, test designer, local feedback, Codex/OpenCode | `reflective-implement` |
| Code reviewer, review-rating-fix | `reflective-review` |
| Context engineering, long context, Gemini long document, research | `reflective-research` |
| High-risk | `reflective-risk` |
| Context handoff, retro, memory consolidation | `reflective-handoff-retro` |

## Installation Notes

For Claude Code project skills, copy each skill directory into:

```text
.claude/skills/<skill-name>/SKILL.md
```

For Codex/OpenCode-style local libraries, keep the current directory as source and copy/adapt only the skills you actually use.

