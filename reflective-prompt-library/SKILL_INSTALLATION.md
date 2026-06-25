Language: English | [繁體中文](SKILL_INSTALLATION.zh-TW.md)

# Skill Installation Guide

Last verified: 2026-05-24

This guide explains how to install the TeaPrompt workflow skills into Claude Code, Codex, Cursor, Google Antigravity CLI / IDE, and OpenCode.

The source skills live here:

```text
reflective-prompt-library/skills/
  reflective-brief/
  reflective-dispatch/
  reflective-handoff-retro/
  reflective-implement/
  reflective-minimality/    # gate skill — anti-bloat review, not a lifecycle workflow
  reflective-research/
  reflective-review/
  reflective-risk/
  reflective-spec-plan/
```

**Harness policy:** Nine frozen workflow skills with strictness-first routing. See [06-repo/AGENTS.md](06-repo/AGENTS.md#harness-policy-nine-skills) and [skills/SKILL_TRIGGER_CHEATSHEET.md](skills/SKILL_TRIGGER_CHEATSHEET.md).

Each install target expects this shape:

```text
<skills-root>/<skill-name>/SKILL.md
```

## Recommended Install Strategy

Use one of these scopes:

| Scope | Best for | Tradeoff |
| --- | --- | --- |
| Project-local | Team/project-specific workflows | Version controlled, but must be copied per repo |
| User-global | Your personal workflows across repos | Easy reuse, but less explicit to teammates |
| Shared `.agents/skills` | Cross-tool project portability | Supported by several tools, but not every host treats it as primary |

For this repository, project-local install is the safest default.

**Copy vs symlink:** use `cp -R` for team installs and published repos. Use `ln -s` or `ln -sfn` when you develop TeaPrompt in place and want the host to read skills directly from this checkout (see [Symlink install](#symlink-install) below).

## Install All TeaPrompt Skills

From the repo root:

```bash
for skill in reflective-prompt-library/skills/reflective-*; do
  test -d "$skill" || continue
  echo "$(basename "$skill")"
done
```

Then copy or symlink the skill directories into the target tool path shown below.

## Symlink install

Run these from the TeaPrompt repo root. `ln -sfn` replaces an existing link; use `ln -sf` if your shell's `ln` does not support `-n`.

Install one skill (example: `reflective-dispatch`):

```bash
ln -sfn "$(pwd)/reflective-prompt-library/skills/reflective-dispatch" .claude/skills/reflective-dispatch
```

Install all reflective skills into a target directory:

```bash
install_skills_symlink() {
  local dest="$1"
  mkdir -p "$dest"
  for skill in reflective-prompt-library/skills/reflective-*; do
    name="$(basename "$skill")"
    ln -sfn "$(pwd)/$skill" "$dest/$name"
  done
}
```

Run that function definition once in your shell (or paste it before the commands below). Examples in later sections call `install_skills_symlink <dest>`.

## Claude Code

Claude Code discovers skills from:

| Scope | Path |
| --- | --- |
| Project | `.claude/skills/<skill-name>/SKILL.md` |
| Personal | `~/.claude/skills/<skill-name>/SKILL.md` |

Project install (copy):

```bash
mkdir -p .claude/skills
cp -R reflective-prompt-library/skills/reflective-* .claude/skills/
```

Project install (symlink):

```bash
install_skills_symlink .claude/skills
```

Personal install (copy):

```bash
mkdir -p ~/.claude/skills
cp -R reflective-prompt-library/skills/reflective-* ~/.claude/skills/
```

Personal install (symlink):

```bash
mkdir -p ~/.claude/skills
for skill in reflective-prompt-library/skills/reflective-*; do
  name="$(basename "$skill")"
  ln -sfn "$(pwd)/$skill" "$HOME/.claude/skills/$name"
done
```

Validate:

```bash
find .claude/skills -maxdepth 2 -name SKILL.md -print
```

In Claude Code, ask:

```text
What Skills are available?
```

Notes:

- Claude Code can auto-load relevant skills by `description`.
- You can also invoke a skill directly with `/skill-name`.
- If you created the top-level `.claude/skills` directory after the session started, restart Claude Code.

## Codex

Codex-native install uses `$CODEX_HOME/skills`; when `CODEX_HOME` is unset, the default is:

```text
~/.codex/skills/<skill-name>/SKILL.md
```

Personal Codex install (copy):

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R reflective-prompt-library/skills/reflective-* "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Personal Codex install (symlink):

```bash
CODEX_SKILLS="${CODEX_HOME:-$HOME/.codex}/skills"
mkdir -p "$CODEX_SKILLS"
for skill in reflective-prompt-library/skills/reflective-*; do
  name="$(basename "$skill")"
  ln -sfn "$(pwd)/$skill" "$CODEX_SKILLS/$name"
done
```

Validate:

```bash
find "${CODEX_HOME:-$HOME/.codex}/skills" -maxdepth 2 -name SKILL.md -print
```

Restart Codex after installing so it can pick up the new skills.

Project-shared option (copy):

```bash
mkdir -p .agents/skills
cp -R reflective-prompt-library/skills/reflective-* .agents/skills/
```

Project-shared option (symlink):

```bash
install_skills_symlink .agents/skills
```

Use `.agents/skills` when you want one project-local skill location that can also be read by other Agent Skills-compatible tools. If your Codex build does not show these skills, use the Codex-native `~/.codex/skills` path.

## Cursor

Cursor has two relevant instruction surfaces:

1. **Rules**: official, stable Cursor mechanism.
2. **Agent Skills / SKILL.md**: available in newer or Agent Skills-compatible setups, but verify in your installed Cursor build.

### Option A: Agent Skills install

Prefer the shared project location when available (copy):

```bash
mkdir -p .agents/skills
cp -R reflective-prompt-library/skills/reflective-* .agents/skills/
```

Shared project location (symlink):

```bash
install_skills_symlink .agents/skills
```

Cursor-specific project location, if supported by your build (copy):

```bash
mkdir -p .cursor/skills
cp -R reflective-prompt-library/skills/reflective-* .cursor/skills/
```

Cursor-specific project location (symlink):

```bash
install_skills_symlink .cursor/skills
```

Validate:

```bash
find .agents/skills .cursor/skills -maxdepth 2 -name SKILL.md -print 2>/dev/null
```

Then reopen the project or restart Cursor and check the Agent/skills UI if available.

### Option B: Cursor Rules fallback

If Cursor does not discover `SKILL.md`, install a lightweight project rule that tells Cursor where the workflow skills live:

```bash
mkdir -p .cursor/rules
```

Create `.cursor/rules/teaprompt-skills.mdc`:

```markdown
---
description: Use TeaPrompt reflective workflow skills when planning, implementing, reviewing, researching, or handling high-risk work.
alwaysApply: false
---

When the user asks for reflective workflow help, inspect the relevant SKILL.md under:

@reflective-prompt-library/skills/skill-map.md

Prefer:
- reflective-dispatch for routing
- reflective-brief for goal/scope/acceptance
- reflective-spec-plan for specs and task slicing
- reflective-implement for coding
- reflective-minimality as a gate before implementation
- reflective-review for review
- reflective-research for docs/research
- reflective-risk for high-risk gates
- reflective-handoff-retro for handoff and retros
```

This is not a native skill install, but it preserves the workflow behavior in Cursor's official Rules system.

## Antigravity CLI / Antigravity IDE

Antigravity supports Agent Skills in these locations:

| Scope | Path |
| --- | --- |
| Workspace | `<workspace-root>/.agents/skills/<skill-name>/SKILL.md` |
| Global | `~/.gemini/antigravity/skills/<skill-name>/SKILL.md` |

Workspace install (copy):

```bash
mkdir -p .agents/skills
cp -R reflective-prompt-library/skills/reflective-* .agents/skills/
```

Workspace install (symlink):

```bash
install_skills_symlink .agents/skills
```

Global install (copy):

```bash
mkdir -p ~/.gemini/antigravity/skills
cp -R reflective-prompt-library/skills/reflective-* ~/.gemini/antigravity/skills/
```

Global install (symlink):

```bash
mkdir -p ~/.gemini/antigravity/skills
for skill in reflective-prompt-library/skills/reflective-*; do
  name="$(basename "$skill")"
  ln -sfn "$(pwd)/$skill" "$HOME/.gemini/antigravity/skills/$name"
done
```

Validate:

```bash
find .agents/skills ~/.gemini/antigravity/skills -maxdepth 2 -name SKILL.md -print 2>/dev/null
```

In Antigravity CLI / IDE:

```text
/skills
```

If skills do not appear, restart the IDE/CLI session and confirm the project root is the workspace root Antigravity opened.

## OpenCode

OpenCode discovers skills from several locations:

| Scope | Path |
| --- | --- |
| Project OpenCode | `.opencode/skills/<skill-name>/SKILL.md` |
| Global OpenCode | `~/.config/opencode/skills/<skill-name>/SKILL.md` |
| Project Claude-compatible | `.claude/skills/<skill-name>/SKILL.md` |
| Global Claude-compatible | `~/.claude/skills/<skill-name>/SKILL.md` |
| Project Agent-compatible | `.agents/skills/<skill-name>/SKILL.md` |
| Global Agent-compatible | `~/.agents/skills/<skill-name>/SKILL.md` |

Project install (copy):

```bash
mkdir -p .opencode/skills
cp -R reflective-prompt-library/skills/reflective-* .opencode/skills/
```

Project install (symlink):

```bash
install_skills_symlink .opencode/skills
```

Global install (copy):

```bash
mkdir -p ~/.config/opencode/skills
cp -R reflective-prompt-library/skills/reflective-* ~/.config/opencode/skills/
```

Global install (symlink):

```bash
mkdir -p ~/.config/opencode/skills
for skill in reflective-prompt-library/skills/reflective-*; do
  name="$(basename "$skill")"
  ln -sfn "$(pwd)/$skill" "$HOME/.config/opencode/skills/$name"
done
```

Shared project install (copy):

```bash
mkdir -p .agents/skills
cp -R reflective-prompt-library/skills/reflective-* .agents/skills/
```

Shared project install (symlink):

```bash
install_skills_symlink .agents/skills
```

OpenCode also reads Claude-compatible paths. Symlink there if you rely on that discovery mode:

```bash
install_skills_symlink .claude/skills
```

Validate:

```bash
find .opencode/skills ~/.config/opencode/skills .agents/skills -maxdepth 2 -name SKILL.md -print 2>/dev/null
```

In OpenCode:

```text
/skills
```

or ask the agent to list available skills.

## Symlink Development Mode

For active development in this repo, symlinks keep `.claude/skills`, `.agents/skills`, or `.cursor/skills` pointed at `reflective-prompt-library/skills/` so edits to `SKILL.md` are picked up without re-copying.

Copy is safer for teammates and CI; some hosts do not follow symlinks consistently.

From the TeaPrompt repo root (equivalent to `install_skills_symlink .agents/skills`):

```bash
mkdir -p .agents/skills
for skill in reflective-prompt-library/skills/reflective-*; do
  name="$(basename "$skill")"
  ln -sfn "$(pwd)/$skill" ".agents/skills/$name"
done
```

Symlink into another project that vendors TeaPrompt as a submodule or sibling checkout:

```bash
TEAPROMPT=/path/to/teaPrompt
PROJECT=/path/to/your-app
mkdir -p "$PROJECT/.agents/skills"
for skill in "$TEAPROMPT"/reflective-prompt-library/skills/reflective-*; do
  name="$(basename "$skill")"
  ln -sfn "$skill" "$PROJECT/.agents/skills/$name"
done
```

Use symlink installs only for your own workspace, not as the default team install.

## Troubleshooting Checklist

1. Confirm the path is `<skills-root>/<skill-name>/SKILL.md`.
2. Confirm the file is named exactly `SKILL.md`.
3. Confirm frontmatter contains at least:
   ```yaml
   ---
   name: reflective-brief
   description: ...
   ---
   ```
4. Confirm the skill folder name matches the `name` value.
5. Restart the host if it does not watch newly created skill roots.
6. Ask the host to list available skills.
7. If a skill triggers too often, make the `description` narrower.
8. If a skill never triggers, make the `description` more explicit and include likely user phrases.

## Security Notes

- Treat third-party skills as executable operational instructions, not passive docs.
- Read `SKILL.md` before installing.
- Avoid installing huge skill packs globally; prefer a small project-local set.
- Do not grant tool permissions or hooks unless the skill genuinely needs them.
- Keep high-risk workflows behind `reflective-risk`.

## Sources

- Claude Code skills docs: https://code.claude.com/docs/en/skills
- OpenAI skills repository: https://github.com/openai/skills
- OpenAI Codex use cases: https://developers.openai.com/codex/use-cases
- Google Antigravity skills docs: https://antigravity.google/docs/skills
- OpenCode skills docs: https://opencode.ai/docs/skills
- Cursor rules docs: https://docs.cursor.com/en/context
- GitHub CLI `gh skill install`: https://cli.github.com/manual/gh_skill_install
