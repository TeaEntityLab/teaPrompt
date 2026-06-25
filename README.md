Language: English | [繁體中文](README.zh-TW.md)

# TeaPrompt

TeaPrompt is a reflective prompt and workflow library for AI-assisted engineering work.

Core principle:

```text
Doing the right thing > doing things right.
```



## North Star

TeaPrompt helps humans and host agents choose the **right amount of rigor** for a task, record **why** decisions were made, and verify outcomes with **evidence** — using composable prompt layers and nine workflow skills as natural-language harness policy, **without** operating its own agent runtime.

Full library docs: [reflective-prompt-library/README.md](reflective-prompt-library/README.md).

## Governance

- **Contributing:** [CONTRIBUTING.md](CONTRIBUTING.md) — quality gates, routing maintenance (R8–R12), `make all`
- **Panel record:** [multi-agent-panel-consensus](reflective-prompt-library/plans/multi-agent-panel-consensus-2026-06-25.md) — six-lens Socratic consensus (Rounds 1–87)
- **Operator playbook:** [GLOSSARY.md](reflective-prompt-library/GLOSSARY.md) — Governance Maintenance Playbook

The repository contains:

- `reflective-prompt-library/`: reusable Markdown prompts for thinking, planning, implementation, review, research, risk handling, and context handoff.
- `reflective-prompt-library/skills/`: concise `SKILL.md` workflow wrappers that turn the prompt library into practical agent workflows.
- `reflective-prompt-library/plans/`: design notes and follow-up plans for code tooling or workflow automation.
- `reflective-prompt-library/SKILL_INSTALLATION.md`: install instructions for Claude Code, Codex, Cursor, Antigravity CLI / IDE, and OpenCode.
- `reflective-prompt-library/METHODOLOGY_MAP.md`: classification map for choosing the right strictness level.
- `reflective-prompt-library/LANGUAGE_POLICY.md`: language policy for English operational docs and localized prompt sources.

## Quick Start

Use the prompt library directly:

```text
reflective-prompt-library/README.md
```

Or copy a workflow skill into a compatible skills directory:

```text
.claude/skills/<skill-name>/SKILL.md
~/.codex/skills/<skill-name>/SKILL.md
.agents/skills/<skill-name>/SKILL.md
```

For host-specific paths, see [Skill Installation Guide](reflective-prompt-library/SKILL_INSTALLATION.md).

For repository method boundaries, see [Methodology Map](reflective-prompt-library/METHODOLOGY_MAP.md).
For language conventions, see [Language Policy](reflective-prompt-library/LANGUAGE_POLICY.md).

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
- Skills provide repeatable execution shape — they are prompt-level workflow descriptors interpreted by the user's agent runtime, not a multi-agent orchestration layer.
- Plans capture future code or workflow automation without overengineering the current library.

The workflow layer intentionally uses a small number of broad, composable skills instead of one skill per prompt.

## License

MIT. See [LICENSE](LICENSE).
