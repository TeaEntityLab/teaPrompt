# TeaPrompt

TeaPrompt is a reflective prompt and workflow library for AI-assisted engineering work.

Core principle:

```text
Doing the right thing > doing things right.
```

The repository contains:

- `reflective-prompt-library/`: reusable Markdown prompts for thinking, planning, implementation, review, research, risk handling, and context handoff.
- `reflective-prompt-library/skills/`: concise `SKILL.md` workflow wrappers that turn the prompt library into practical agent workflows.
- `reflective-prompt-library/plans/`: design notes and follow-up plans for code tooling or workflow automation.

## Quick Start

Use the prompt library directly:

```text
reflective-prompt-library/README.md
```

Or copy a workflow skill into a compatible skills directory:

```text
.claude/skills/<skill-name>/SKILL.md
.codex/skills/<skill-name>/SKILL.md
```

Recommended starting points:

- `reflective-dispatch`: choose the smallest useful workflow.
- `reflective-brief`: clarify goals, assumptions, scope, acceptance criteria, and falsifiability.
- `reflective-spec-plan`: write specs, usage-first docs, and task slices.
- `reflective-implement`: implement with tests, traceability, and verification.
- `reflective-review`: review code, plans, specs, and AI outputs.
- `reflective-risk`: gate high-risk work before execution.

## Design Philosophy

TeaPrompt keeps prompts and workflows separate:

- Prompts provide nuance, judgment frames, and reusable wording.
- Skills provide repeatable execution shape.
- Plans capture future code or workflow automation without overengineering the current library.

The workflow layer intentionally uses a small number of broad, composable skills instead of one skill per prompt.

## License

MIT. See [LICENSE](LICENSE).

