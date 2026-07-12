Language: English | [繁體中文](SKILL_INSTALLATION.zh-TW.md)

# Skill Installation Guide

Last verified: 2026-07-11

This guide explains how to install the nine TeaPrompt core workflow skills—and, when explicitly wanted, the optional registered domain packs—into Claude Code, Codex, Cursor, Gemini CLI, Google Antigravity CLI / IDE, and OpenCode.

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

  # Optional registered domain packs (host-invoked; not core routing)
  flow-control-generator/
  flow-loop-harness/
```

**Harness policy:** Nine frozen **core** workflow skills with strictness-first routing; registered domain packs are opt-in and remain outside core routing. See [06-repo/AGENTS.md](06-repo/AGENTS.md#harness-policy-nine-skills), [skills/skill-map.md](skills/skill-map.md#registered-domain-packs-not-core-routing), and [skills/SKILL_TRIGGER_CHEATSHEET.md](skills/SKILL_TRIGGER_CHEATSHEET.md).

Each install target expects this shape:

```text
<skills-root>/<skill-name>/SKILL.md
```

## No Agent Skills support?

If your host cannot discover `SKILL.md` files at all, fall back to the library's prompt layer: every skill ends with a `## Prompt Sources` list naming the `00-core`–`06-repo` prompts it compiles. Paste the relevant skill body (or its listed source prompts) directly into the host's system/custom-instruction surface. The skills are prompt-level workflows by design, so this degrades cleanly — you lose auto-triggering by description, not the method.

## Recommended Install Strategy

Use one of these scopes:

| Scope | Best for | Tradeoff |
| --- | --- | --- |
| Project-local | Team/project-specific workflows | Version controlled, but must be copied per repo |
| User-global | Your personal workflows across repos | Easy reuse, but less explicit to teammates |
| Shared `.agents/skills` | Cross-tool project portability | Supported by several tools, but not every host treats it as primary |

For this repository, project-local install is the safest default.

**Copy vs symlink:** use `cp -R` for team installs and published repos. Use `ln -s` or `ln -sfn` when you develop TeaPrompt in place and want the host to read skills directly from this checkout (see [Symlink install](#symlink-install) below).

## Choose an Install Tier

The default commands below install only the nine core `reflective-*` skills. This
keeps optional script-generation packs out of host auto-discovery unless you
choose them.

From the repository root, list the core skills:

```bash
for skill in reflective-prompt-library/skills/reflective-*/; do
  test -f "$skill/SKILL.md" || continue
  echo "$(basename "$skill")"
done
```

The optional domain-pack registry currently contains:

```text
flow-control-generator
flow-loop-harness
```

Use the core helpers for the default install. Afterward, call the matching
`install_domain_packs_*` helper with the same destination only when those
host-invoked script generators are wanted.

## Symlink install

Run these definitions from the TeaPrompt repository root. Every helper accepts
the destination first and an optional TeaPrompt `skills/` source directory
second. It copies or links only directories containing `SKILL.md`.

```bash
install_core_skills_copy() {
  local dest="$1"
  local source_root
  source_root="$(cd "${2:-$(pwd)/reflective-prompt-library/skills}" && pwd)"
  mkdir -p "$dest"
  for skill in "$source_root"/reflective-*/; do
    skill="${skill%/}"
    test -f "$skill/SKILL.md" || continue
    cp -R "$skill" "$dest/"
  done
}

install_core_skills_symlink() {
  local dest="$1"
  local source_root
  source_root="$(cd "${2:-$(pwd)/reflective-prompt-library/skills}" && pwd)"
  mkdir -p "$dest"
  for skill in "$source_root"/reflective-*/; do
    skill="${skill%/}"
    test -f "$skill/SKILL.md" || continue
    name="$(basename "$skill")"
    ln -sfn "$skill" "$dest/$name"
  done
}

install_domain_packs_copy() {
  local dest="$1"
  local source_root
  source_root="$(cd "${2:-$(pwd)/reflective-prompt-library/skills}" && pwd)"
  mkdir -p "$dest"
  for name in flow-control-generator flow-loop-harness; do
    skill="$source_root/$name"
    test -f "$skill/SKILL.md" || return 1
    cp -R "$skill" "$dest/"
  done
}

install_domain_packs_symlink() {
  local dest="$1"
  local source_root
  source_root="$(cd "${2:-$(pwd)/reflective-prompt-library/skills}" && pwd)"
  mkdir -p "$dest"
  for name in flow-control-generator flow-loop-harness; do
    skill="$source_root/$name"
    test -f "$skill/SKILL.md" || return 1
    ln -sfn "$skill" "$dest/$name"
  done
}
```

Run these definitions once (or paste them before a command below).
`ln -sfn` replaces an existing link; use `ln -sf` if the host `ln` lacks `-n`.
Examples below install core skills by default:

```bash
install_core_skills_copy <destination>
install_core_skills_symlink <destination>
```

Opt in to both registered domain packs with:

```bash
install_domain_packs_copy <destination>
# or
install_domain_packs_symlink <destination>
```

Install one skill directly when needed:

```bash
ln -sfn "$(pwd)/reflective-prompt-library/skills/reflective-dispatch" .claude/skills/reflective-dispatch
```

## Claude Code

Claude Code discovers skills from:

| Scope | Path |
| --- | --- |
| Project | `.claude/skills/<skill-name>/SKILL.md` |
| Personal | `~/.claude/skills/<skill-name>/SKILL.md` |

Project install (copy):

```bash
install_core_skills_copy .claude/skills
```

Project install (symlink):

```bash
install_core_skills_symlink .claude/skills
```

Personal install (copy):

```bash
install_core_skills_copy "$HOME/.claude/skills"
```

Personal install (symlink):

```bash
install_core_skills_symlink "$HOME/.claude/skills"
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

Current Codex docs (checked 2026-07-11) additionally document Agent Skills tiers:
repository `.agents/skills` scanned from the working directory up to the repo
root, user `$HOME/.agents/skills`, and admin `/etc/codex/skills`; `$skill-installer`
installs curated skills. The `~/.codex/skills` path below is the Codex-native
location that predates those tiers.

Personal Codex install (copy):

```bash
install_core_skills_copy "${CODEX_HOME:-$HOME/.codex}/skills"
```

Personal Codex install (symlink):

```bash
install_core_skills_symlink "${CODEX_HOME:-$HOME/.codex}/skills"
```

Validate:

```bash
find "${CODEX_HOME:-$HOME/.codex}/skills" -maxdepth 2 -name SKILL.md -print
```

Restart Codex after installing so it can pick up the new skills.

Project-shared option (copy):

```bash
install_core_skills_copy .agents/skills
```

Project-shared option (symlink):

```bash
install_core_skills_symlink .agents/skills
```

Use `.agents/skills` when you want one project-local skill location that can also be read by other Agent Skills-compatible tools. If your Codex build does not show these skills, use the Codex-native `~/.codex/skills` path.

User-scope shared option (works for every `.agents/skills`-aware host):

```bash
install_core_skills_copy "$HOME/.agents/skills"
# or
install_core_skills_symlink "$HOME/.agents/skills"
```

## Cursor

Cursor has two relevant instruction surfaces:

1. **Rules**: official, stable Cursor mechanism.
2. **Agent Skills / SKILL.md**: available in newer or Agent Skills-compatible setups, but verify in your installed Cursor build.

### Option A: Agent Skills install

Prefer the shared project location when available (copy):

```bash
install_core_skills_copy .agents/skills
```

Shared project location (symlink):

```bash
install_core_skills_symlink .agents/skills
```

Cursor-specific project location, if supported by your build (copy):

```bash
install_core_skills_copy .cursor/skills
```

Cursor-specific project location (symlink):

```bash
install_core_skills_symlink .cursor/skills
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

## Gemini CLI

Gemini CLI implements the Agent Skills standard with these discovery tiers
(lowest to highest precedence: built-in, extension, user, workspace; within a
tier the `.agents/skills` alias beats `.gemini/skills`):

| Scope | Path |
| --- | --- |
| Workspace | `.gemini/skills/<skill-name>/SKILL.md` or `.agents/skills/<skill-name>/SKILL.md` |
| User | `~/.gemini/skills/<skill-name>/SKILL.md` or `~/.agents/skills/<skill-name>/SKILL.md` |

The shared helpers work as for other hosts:

```bash
install_core_skills_copy .agents/skills          # workspace
install_core_skills_symlink "$HOME/.agents/skills"  # user
```

Gemini CLI also manages skills natively:

```bash
gemini skills list --all
gemini skills link "$(pwd)/reflective-prompt-library/skills/reflective-brief" --scope user
gemini skills install <git-url> --path reflective-prompt-library/skills/reflective-brief --consent
gemini skills uninstall reflective-brief --scope user
```

Notes (verified on macOS, 2026-07-11): `gemini skills list` reads
`~/.agents/skills`; `link` asks an interactive security confirmation (`install`
accepts `--consent` to skip it); duplicate names across tiers are reported as
conflicts with the higher tier winning; skill activation in-session shows a
consent prompt naming the skill and the directory it gains access to. Google
has announced that unpaid-tier and Google One users' Gemini CLI is being
replaced by Antigravity CLI (see the next section), so free-tier users should
prefer the Antigravity paths.

## Antigravity CLI / Antigravity IDE

Antigravity supports Agent Skills in these locations:

| Scope | Path |
| --- | --- |
| Workspace | `<workspace-root>/.agents/skills/<skill-name>/SKILL.md` |
| Global | `~/.gemini/antigravity/skills/<skill-name>/SKILL.md` |

Workspace install (copy):

```bash
install_core_skills_copy .agents/skills
```

Workspace install (symlink):

```bash
install_core_skills_symlink .agents/skills
```

Global install (copy):

```bash
install_core_skills_copy "$HOME/.gemini/antigravity/skills"
```

Global install (symlink):

```bash
install_core_skills_symlink "$HOME/.gemini/antigravity/skills"
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
install_core_skills_copy .opencode/skills
```

Project install (symlink):

```bash
install_core_skills_symlink .opencode/skills
```

Global install (copy):

```bash
install_core_skills_copy "$HOME/.config/opencode/skills"
```

Global install (symlink):

```bash
install_core_skills_symlink "$HOME/.config/opencode/skills"
```

Shared project install (copy):

```bash
install_core_skills_copy .agents/skills
```

Shared project install (symlink):

```bash
install_core_skills_symlink .agents/skills
```

OpenCode also reads Claude-compatible paths. Symlink there if you rely on that discovery mode:

```bash
install_core_skills_symlink .claude/skills
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

From the TeaPrompt repository root:

```bash
install_core_skills_symlink .agents/skills
# Optional:
install_domain_packs_symlink .agents/skills
```

Symlink into another project that vendors TeaPrompt as a submodule or sibling checkout:

```bash
TEAPROMPT=/path/to/teaPrompt
PROJECT=/path/to/your-app
SOURCE="$TEAPROMPT/reflective-prompt-library/skills"
install_core_skills_symlink "$PROJECT/.agents/skills" "$SOURCE"
# Optional:
install_domain_packs_symlink "$PROJECT/.agents/skills" "$SOURCE"
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
9. Validate spec conformance: `python3 reflective-prompt-library/plans/validate_links.py`
   in this repo, or the reference tool (`pip install skills-ref`, then
   `agentskills validate <skill-dir>`). Only `name`, `description`, `license`,
   `compatibility`, `metadata`, and `allowed-tools` are spec-valid top-level
   frontmatter fields; TeaPrompt's governance fields live under `metadata:`.

## Security Notes

- Treat third-party skills as executable operational instructions, not passive docs.
- Read `SKILL.md` before installing.
- Avoid installing huge skill packs globally; prefer a small project-local set.
- Do not grant tool permissions or hooks unless the skill genuinely needs them.
- Keep high-risk workflows behind `reflective-risk`.

### Enforcing TeaPrompt's review gates host-side

TeaPrompt skills declare intent via `metadata.human_review_required`; hosts, not
TeaPrompt, enforce it. When installing `reflective-risk` or `flow-loop-harness`
(both `human_review_required: true`), map the declaration to your host's
invocation control:

| Host | Mechanism |
| --- | --- |
| Claude Code | add `disable-model-invocation: true` to your installed copy so only explicit `/skill-name` runs it |
| Codex | `agents/openai.yaml` with `policy.allow_implicit_invocation: false` |
| Gemini CLI | activation already shows a per-skill consent prompt; keep it enabled |

These are host features documented at the sources below; TeaPrompt cannot
verify or enforce them (runtime-trust boundary).

## Sources

- Agent Skills specification: https://agentskills.io/specification
- Claude Code skills docs: https://code.claude.com/docs/en/skills
- Codex skills docs: https://learn.chatgpt.com/docs/build-skills
- Gemini CLI skills docs: https://geminicli.com/docs/cli/skills/
- OpenAI skills repository: https://github.com/openai/skills
- Google Antigravity skills docs: https://antigravity.google/docs/skills
- OpenCode skills docs: https://opencode.ai/docs/skills
- Cursor rules docs: https://docs.cursor.com/en/context
- GitHub CLI `gh skill install`: https://cli.github.com/manual/gh_skill_install
