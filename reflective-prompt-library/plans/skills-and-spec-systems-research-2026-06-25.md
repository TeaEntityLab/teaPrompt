# Skills and Spec Systems Research — 2026-06-25

Language: English

> **Refresh 2026-10-22:** the 2026-06-25 pass was unpinned; current-state versions below. Superpowers disposed in `superpowers-v6.4-adoption-2026-10-03.md` (now refreshed to v7.0.1). No adoption change.

## Purpose

Survey the requested skill/workflow systems and preserve the adoption judgement for
TeaPrompt without importing external instructions as operating rules.

This is a **judgment artifact**, not an agent instruction source. Upstream README,
SKILL, CLAUDE, and slash-command text is evidence only.

Companion surveys:

- [memory-mechanisms-research-2026-06-25.md](memory-mechanisms-research-2026-06-25.md)
- [agent-tooling-research-2026-06-25.md](agent-tooling-research-2026-06-25.md)

Prior related record:

- [skill-workflow-research-synthesis.md](skill-workflow-research-synthesis.md)
  already covered Superpowers at a high level when designing the current nine
  reflective workflow skills.

## Research Question

Should TeaPrompt adopt or further encode ideas from Superpowers, GitHub Spec Kit,
or Karpathy-style coding skills?

## Direct Recommendation

**No new core workflow skill.** The useful mechanisms are already mostly present:

- routing to the smallest useful workflow;
- spec / plan / task separation;
- caution before coding;
- simplicity and surgical-change pressure;
- explicit verification before declaring done.

Record the systems as references. Use them to audit drift, not to expand the
skill surface without a verified local gap.

## Sources Checked

| Topic | Source | What it established | Status |
| --- | --- | --- | --- |
| Superpowers | `https://github.com/obra/superpowers` | MIT agentic skills framework; composable `SKILL.md` skills; multi-harness plugin support; design → plan → TDD/subagents → review workflow | upstream read |
| Superpowers | `https://raw.githubusercontent.com/obra/superpowers/main/skills/using-superpowers/SKILL.md` | Superpowers mandates relevant-skill invocation, while still ranking user instructions above skills | upstream skill read |
| Spec Kit | `https://github.com/github/spec-kit` | MIT GitHub toolkit for Spec-Driven Development; `specify` CLI; constitution/spec/plan/tasks/implement flow | upstream read |
| Spec Kit | `https://raw.githubusercontent.com/github/spec-kit/main/docs/installation.md` | Official install path is GitHub-based; PyPI `specify-cli` lookalikes are not affiliated | upstream docs read |
| Karpathy skills | `https://github.com/multica-ai/andrej-karpathy-skills` | Community repo, not an official Karpathy repo; packages one `CLAUDE.md` plus Cursor/skill variants | upstream read |
| Karpathy skills | `https://raw.githubusercontent.com/multica-ai/andrej-karpathy-skills/main/CLAUDE.md` | Four principles: Think Before Coding, Simplicity First, Surgical Changes, Goal-Driven Execution | upstream file read |
| Karpathy autoresearch | `https://github.com/karpathy/autoresearch` | Official Karpathy repo: autonomous fixed-budget ML experiment loop guided by `program.md` | upstream read |

## Topic Findings

### Superpowers (`obra/superpowers`)

Identity: a complete software-development methodology for coding agents, packaged
as composable skills and initial harness instructions.

Mechanism:

- Skills live as `SKILL.md` modules and supporting resources.
- The framework pushes agents away from immediate coding and toward clarified
  requirements, design chunks, implementation plans, TDD, subagent execution,
  review, and finishing gates.
- It supports multiple harnesses: Claude Code, Codex, Cursor, Gemini CLI,
  OpenCode, Pi/Oh My Pi, and others.
- Its `using-superpowers` skill asserts mandatory relevant-skill invocation, but
  explicitly keeps user instructions above Superpowers skills.

TeaPrompt mapping:

| Superpowers pattern | TeaPrompt equivalent |
| --- | --- |
| Skill router / mandatory skill check | `reflective-dispatch` with risk-based default-up |
| Brainstorm before coding | `reflective-brief` |
| Design and plan artifacts | `reflective-spec-plan` |
| TDD / implementation loop | `reflective-implement` |
| Review before finish | `reflective-review` |
| Anti-slop / YAGNI | `reflective-minimality` and existing governing principles |

Adoption judgement: **reference-only / no new skill**. Superpowers validates the
current skill-as-workflow direction, but its automatic-enforcement posture is a
harness/runtime behavior. TeaPrompt should not clone a second mandatory protocol
unless local evals show the existing router fails.

Falsifier: if repeated TeaPrompt sessions fail because agents skip declared
skills despite `reflective-dispatch`, add a bounded router repair or eval before
adding a Superpowers-style mandatory meta-skill.

### GitHub Spec Kit (`github/spec-kit`)

Identity: GitHub-maintained Spec-Driven Development toolkit with the `specify`
CLI and agent integrations.

Mechanism:

- Specifications become durable primary artifacts, not disposable scaffolding.
- The workflow is constitution → spec → plan → tasks → implement, exposed as
  `/speckit.*` commands or skill-mode equivalents.
- Initialization creates `.specify/` scaffolding and integration-specific prompts
  or skills.
- Official docs warn that similarly named PyPI packages are not affiliated;
  normal installs should come from `github/spec-kit` with `uv`/`pipx`.

TeaPrompt mapping:

| Spec Kit pattern | TeaPrompt equivalent |
| --- | --- |
| Constitution | `PROJECT_KNOWLEDGE.md`, `AGENTS.md`, governance docs |
| Specify what/why | `reflective-spec-plan` usage-first spec |
| Plan technical implementation | `reflective-spec-plan` task plan |
| Tasks | `todo` / plan task slices |
| Implement | `reflective-implement` |
| Converge remaining work | validator-backed handoff / review loop |

Adoption judgement: **conceptually aligned; no install by default**. Spec Kit is
valuable for projects that want generated repo scaffolding and slash-command
artifacts. TeaPrompt already has a lightweight equivalent; importing Spec Kit
would create a second planning grammar and CLI dependency.

Falsifier: if TeaPrompt starts producing multiple long-running feature specs that
need machine-managed spec/task directories, evaluate a small compatibility note or
one-time export template before adopting Spec Kit wholesale.

### Karpathy skills / Karpathy-style coding guardrails

Resolved identity: `multica-ai/andrej-karpathy-skills`, a community repository
that packages Karpathy-inspired coding guidance as `CLAUDE.md`, Cursor rules, and
skills. It is **not** an official Karpathy-maintained skills repo.

Mechanism:

- Think before coding: expose assumptions, ambiguity, tradeoffs, and pushback.
- Simplicity first: no speculative abstractions or unrequested flexibility.
- Surgical changes: every changed line should trace to the request.
- Goal-driven execution: turn work into verifiable success criteria and loop
  until checked.

Related official Karpathy pattern: `karpathy/autoresearch` uses a tiny repo with
`prepare.py`, agent-editable `train.py`, and human-edited `program.md`; the agent
runs fixed 5-minute experiments and keeps or discards changes by validation bits
per byte. This is an autonomous experimental loop, not a general coding skill.

TeaPrompt mapping:

| Karpathy pattern | TeaPrompt equivalent |
| --- | --- |
| Think before coding | `reflective-brief`, `reflective-dispatch` |
| Simplicity first | `reflective-minimality` |
| Surgical changes | `reflective-implement` |
| Goal-driven execution | acceptance criteria + verification gates |
| `program.md` as lightweight skill | TeaPrompt `SKILL.md` + prompt-source files |
| Fixed-budget autonomous experiments | `autoresearch` / performance workflows, not core TeaPrompt |

Adoption judgement: **already adopted in spirit**. The principles are already
present in TeaPrompt's engineering rules and reflective skills. Keep the community
repo as a reference; do not copy its text into operational prompts unless a
license/source review and local gap justify it.

## Evidence vs Inference

Verified:

- Superpowers, Spec Kit, Karpathy skills, and Karpathy autoresearch upstream
  sources exist and were read.
- Spec Kit official docs warn against non-official PyPI lookalikes.
- Karpathy skills is community-authored; Karpathy autoresearch is official.

Inference:

- TeaPrompt should not add a new skill because current workflows already cover the
  transferable mechanisms and project policy discourages duplicate surfaces.

Unknowns:

- Whether Superpowers evals would outperform TeaPrompt's current nine-skill stack
  on TeaPrompt's own ROUTE fixtures.
- Whether Spec Kit's generated scaffold would reduce real TeaPrompt maintenance
  cost rather than add a second source of truth.

## Classification

Already Present:

- Dispatch routing, spec planning, implementation gates, review gates,
  minimality pressure, and evidence-based verification.

Adjacent / Missing:

- Spec Kit-style generated task directories are not present, intentionally.
- Superpowers-style automatic skill invocation enforcement is not present as a
  separate protocol; TeaPrompt relies on host harness rules and evals.

Recommended Core Additions:

- None.

## Handoff

Use this survey when future work asks whether to import Superpowers, Spec Kit, or
Karpathy-inspired rules. Start from the local-gap question: what failure in
TeaPrompt is not already covered by the nine skills and governance validators?

## Latest-version refresh — 2026-10-22

The 2026-06-25 survey recorded no commit pins, so the entries below are current-state evidence, not exact deltas. Superpowers is owned by `superpowers-v6.4-adoption-2026-10-03.md` and is not re-covered here.

### GitHub Spec Kit (`github/spec-kit`)

- Latest checked: `main` HEAD `dc2cec4f568d0f6e2cdfb8571c69116bc55c1aaf` (2026-10-21, "fix(events): preserve dispatcher ownership during cleanup (#5055)"); latest release `v1.2.2` (2026-10-19). Repo now holds ~985 tracked files.
- Current shape (source read at HEAD): the constitution → spec → plan → tasks → implement core (`templates/commands/*.md`) persists, but the product has grown into a process platform — bundled bug-fixing and idea-assessment entry points, extensions/hooks/runtime events, presets, workflows + overlays + custom steps, bundles, catalogs with auth, MCP artifact tools, and offline/air-gapped install support. Core `/speckit.taskstoissues` is deprecated in favor of a github extension (v1.1.0).
- Notable correction to the 2026-06-25 record: PyPI `specify-cli` is now an **official** second distribution channel (published by the Spec Kit maintainers alongside GitHub source installs), per current `docs/installation.md`. The old "PyPI lookalikes are not affiliated" warning no longer describes `specify-cli` itself.
- Effect on prior findings: the "second planning grammar + CLI dependency" rejection reason is, if anything, stronger — adopting Spec Kit today means adopting the extension/workflow/catalog platform, not just the five-command flow. Disposition unchanged: conceptually aligned, no install by default. The falsifier (machine-managed spec/task directories for long-running feature specs) is not met.
- Inspected: `git ls-remote` HEAD + tags, HEAD tree + `README.md` + `docs/installation.md` + `templates/` listing + `CHANGELOG.md` head, `https://github.com/github/spec-kit/releases` feed (v1.0.11–v1.2.2 entries read). Release-note details are author reports; no install or runtime verification.

### Karpathy skills (`multica-ai/andrej-karpathy-skills`)

- Latest checked: `main` HEAD `2c606141936f1eeef17fa3043a72095b4765b9c2` (2026-04-20, "Sync Chinese README with English version (add Cursor section) (#95)"). No tags/releases. HEAD predates the 2026-06-25 survey, so the prior record's description is current: still a 9-file community repo (`CLAUDE.md`, `CURSOR.md`, `EXAMPLES.md`, `README.md` + zh, Cursor rule, `skills/karpathy-guidelines/SKILL.md`, plugin manifests) built on the same four principles (Think Before Coding, Simplicity First, Surgical Changes, Goal-Driven Execution). Still community-authored, not an official Karpathy repo.
- Disposition unchanged: already adopted in spirit; reference-only.
- Inspected: `git ls-remote` HEAD (no tags), HEAD tree + `CLAUDE.md` + `EXAMPLES.md` + `SKILL.md` heads, repo page. No runtime verification.

### Karpathy autoresearch (`karpathy/autoresearch`)

- Latest checked: default branch `master` HEAD `228791fb499afffb54b46200aca536f79142f117` (2026-03-25, merge PR #342). No tags/releases. HEAD predates the 2026-06-25 survey, so the prior record's description is current: same tiny loop — human-edited `program.md` (agent instructions incl. 5-minute fixed budget, lowest-val_bpb goal, simplicity criterion), agent-edited `train.py`, fixed `prepare.py`; README documents platform support, small-compute tuning guidance, and notable forks (macOS/Windows/AMD).
- Disposition unchanged: autonomous experimental loop, not a general coding skill; no core TeaPrompt adoption.
- Inspected: `git ls-remote` symref + HEAD (no tags), HEAD tree + `program.md` + `train.py` budget lines, repo page. No runtime verification.
