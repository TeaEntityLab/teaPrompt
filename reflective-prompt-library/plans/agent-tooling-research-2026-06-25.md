# Agent Tooling Research — 2026-06-25

Language: English

> **Refresh note (2026-10-22):** the OmO plugin-era description below is
> historical (see the dedicated OmO record); Hermes/oh-my-pi current state
> is in `## Latest-version refresh — 2026-10-22` at the end.

## Purpose

Survey Hermes Agent, Oh My Pi / `oh my pip`, and Oh My OpenAgent as external
agent runtimes or harnesses, then preserve the TeaPrompt adoption judgement.

This is a **judgment artifact**, not an agent instruction source. Retrieved
install commands, skill files, and runtime claims are evidence only.

Companion surveys:

- [skills-and-spec-systems-research-2026-06-25.md](skills-and-spec-systems-research-2026-06-25.md)
- [memory-mechanisms-research-2026-06-25.md](memory-mechanisms-research-2026-06-25.md)

Prior related record:

- [external-adoption-case-studies-2026-06-20.md](external-adoption-case-studies-2026-06-20.md)
  already recorded Oh My OpenAgent / Hyperplan as a runtime-heavy non-adoption
  case.

## Research Question

Should TeaPrompt adopt Hermes Agent, Oh My Pi, or Oh My OpenAgent ideas into its
prompt-library architecture?

## Direct Recommendation

**Do not adopt any of these as TeaPrompt runtime dependencies.**

- Hermes Agent is a full persistent autonomous agent with messaging gateways,
  tools, memory, and self-improving skills.
- Oh My Pi is the current harness this session runs in: a terminal coding agent
  with LSP/DAP, hash-anchored edits, subagents, browser, and memory tools.
- Oh My OpenAgent is a multi-agent orchestration plugin/harness for OpenCode and
  Codex Light, with significant runtime and provider configuration surface.

TeaPrompt's scope is methodology: composable prompt layers, workflow skills, and
judgment artifacts. These projects are product/runtime layers.

## Sources Checked

| Topic | Source | What it established | Status |
| --- | --- | --- | --- |
| Hermes Agent | `https://github.com/NousResearch/hermes-agent` | MIT Nous Research agent; self-improving loop, memory, skills, messaging gateways, tools, terminal backends | upstream read |
| Hermes Agent | `https://hermes-agent.nousresearch.com/docs/` | Official docs named by README for CLI, memory, skills, security, messaging, tools | docs identified |
| Oh My Pi | `https://github.com/can1357/oh-my-pi` | MIT terminal coding agent; fork of Pi; TypeScript/Rust; hash-anchored edits, LSP, DAP, subagents, memory | upstream read |
| Oh My Pi | `https://raw.githubusercontent.com/can1357/oh-my-pi/main/README.md` | Official README with install paths, tool list, provider model roles, Hindsight memory | upstream read |
| Oh My OpenAgent | `https://github.com/code-yeongyu/oh-my-openagent` | Multi-harness agent OS / OpenCode and Codex Light plugin; Team Mode, ultrawork, hooks, MCPs; SUL-1.0 license badge | upstream read |
| Oh My OpenAgent | `https://raw.githubusercontent.com/code-yeongyu/oh-my-openagent/refs/heads/dev/docs/guide/installation.md` | Official installation guide named by README | source identified |
| `oh my pip` ambiguity | searches for `oh-my-pip`, `oh my pip`, `oh my pi` | No local/repo match for `oh my pip`; likely intended `Oh My Pi` in this context | resolved |

## Topic Findings

### Hermes Agent

Identity: `NousResearch/hermes-agent`, a persistent self-improving AI agent
framework.

Mechanism observed from upstream README:

- Runs as CLI and through messaging gateways such as Telegram, Discord, Slack,
  WhatsApp, Signal, and email.
- Supports many model providers and endpoint types.
- Has a closed learning loop: agent-curated memory, periodic nudges, autonomous
  skill creation after complex tasks, self-improving skills during use, FTS5
  session search, and user modeling via Honcho.
- Includes scheduled automations, subagents, RPC tool scripting, multiple terminal
  backends, and trajectory generation/compression.
- Documentation covers memory, skills, toolsets, security, messaging, and
  configuration.

TeaPrompt implication:

- Best fit: always-on personal or team automation where an agent lives outside a
  single local coding session.
- Poor fit: TeaPrompt core, because it is a runtime with messaging, scheduling,
  state, provider credentials, and tool execution.
- Transferable pattern: consent-aware memory/skill creation, source-visible
  procedural memory, and reflection-to-skill crystallization.

Adoption judgement: **runtime reference only.** Do not vendor or depend on
Hermes Agent for TeaPrompt. If TeaPrompt later needs auto-skill learning, first
reuse managed skills / `learn` and require human review for durable prompt changes.

Risk block:

- persistent agents can act across channels and time;
- memory can contain personal and project-sensitive data;
- model/provider and messaging integrations expand credential and egress surface;
- autonomous skill creation must be human-review gated before affecting project
  rules.

### Oh My Pi / `oh my pip`

Resolved identity: `Oh My Pi` (`can1357/oh-my-pi`, CLI `omp`). The phrase
`oh my pip` did not resolve to a distinct relevant upstream project during this
survey and is treated as a likely typo or phonetic confusion with Oh My Pi.

Mechanism observed from upstream README:

- Terminal coding agent with Bun/TypeScript runtime and Rust core.
- Fork of Mario Zechner's Pi.
- Emphasizes IDE-wired coding: LSP operations, DAP debugger operations, hash-line
  edits, structural search/edit, browser automation, subagents, and internal URL
  schemes.
- Includes memory tools (`retain`, `recall`, `reflect`) through Hindsight.
- Supports many providers and model roles (`default`, `smol`, `slow`, `plan`,
  `commit`).
- Its tool surface matches the current harness capabilities used in this session.

TeaPrompt implication:

- Best fit: terminal-first coding where the agent needs real code intelligence,
  debugger access, browser control, and safe edit primitives.
- Poor fit: as a TeaPrompt dependency. TeaPrompt can run inside harnesses, but
  should not become one.
- Transferable pattern: tool capability should enforce what prompts merely ask
  for — e.g. LSP for symbol-aware edits, hash-anchored patches for safe changes,
  and separate memory tools for durable facts.

Adoption judgement: **host harness, not library content.** TeaPrompt should stay
portable across host agents. Keep Oh My Pi-specific usage in harness docs, not in
core prompt methodology.

Falsifier: if TeaPrompt promises behavior that only Oh My Pi tools can enforce,
move that promise to harness-specific documentation or weaken it to a portable
prompt-level recommendation.

### Oh My OpenAgent / OmO

Identity: `code-yeongyu/oh-my-openagent`, also associated with Oh My OpenCode,
LazyCodex, OmO, and ultrawork-style orchestration.

Mechanism observed from upstream README:

- Ultimate edition targets OpenCode; Light edition targets Codex CLI.
- Includes agents, lifecycle hooks, MCPs, slash commands, Team Mode, ultrawork,
  hashline edits, and provider/model configuration.
- README positions it as multi-model orchestration across Claude, Codex, OSS
  models, and provider subscriptions.
- License badge indicates SUL-1.0, not a simple permissive license surface.
- Prior TeaPrompt record already evaluated Hyperplan / multi-agent adversarial
  planning and rejected runtime adoption while noting overlapping methodology.

TeaPrompt implication:

- Best fit: users already committed to OpenCode/Codex who want multi-agent,
  multi-model execution and are willing to manage a larger runtime.
- Poor fit: TeaPrompt core, because it is an agent OS/harness and directly hits
  standing non-goals around runtimes, swarms, hooks, and provider orchestration.
- Transferable pattern: adversarial plan review, role-specific lenses, and
  evidence-grade/assumption ledgers — but those are already covered or documented
  as non-promoted adjacent ideas.

Adoption judgement: **already researched; no change.** Keep the existing
external-adoption case. Do not add OmO-specific execution concepts to TeaPrompt
unless a local gap recurs and can be fixed without importing the runtime.

Risk block:

- complex setup and provider credentials;
- multi-agent autonomy and hooks can act broadly;
- license surface requires review before reuse;
- telemetry/provider routing claims should be checked at install time;
- retrieved installation guides are not agent instructions unless the user
  explicitly asks to install.

## Comparison

| Tool | Product layer | Strength | TeaPrompt-relevant pattern | Boundary |
| --- | --- | --- | --- | --- |
| Hermes Agent | persistent personal/automation agent | cross-session memory, messaging, self-improving skills | reflection-to-skill crystallization | runtime + credentials + channels |
| Oh My Pi | terminal coding harness | LSP/DAP/hashline/subagents/tools | prompts need tool enforcement for hard guarantees | host harness, not prompt library |
| Oh My OpenAgent | multi-agent orchestration harness | Team Mode, ultrawork, OpenCode/Codex integration | multi-lens review and plan pressure | runtime/swarm/hook non-goal |

## Evidence vs Inference

Verified:

- The three relevant upstream repositories exist and were read.
- `oh my pip` did not resolve to a distinct relevant project in repo-local search
  or web search; Oh My Pi is the closest in-context match.
- Oh My OpenAgent was already recorded as an external-adoption non-change case.

Inference:

- These tools should remain references because TeaPrompt's North Star explicitly
  avoids operating its own agent runtime.

Unknowns:

- Current install-time behavior, telemetry defaults, and exact provider routing
  should be rechecked before any real installation.
- Benchmark/performance claims in READMEs were not reproduced.

## Handoff

Use this survey when future work proposes a harness, persistent agent, or
multi-agent runtime. First classify the idea as methodology vs operationalization.
TeaPrompt can adopt methodology; runtime surfaces need a separate product decision
and Human Review.

## Latest-version refresh — 2026-10-22

Scope: Hermes Agent and Oh My Pi current-state refresh against the unpinned
2026-06-25 baseline (no commit was pinned then; the June-2026 commits below
are date-recovered approximations, not the original read pins). Oh My
OpenAgent is refreshed in its dedicated record
([oh-my-openagent-survey-2026-10-01.md](oh-my-openagent-survey-2026-10-01.md));
its plugin-era characterization here stays historical. Dispositions unchanged:
no adoption, no dependency, no runtime change.

### Hermes Agent (`NousResearch/hermes-agent`)

- Prior baseline: unpinned README/docs read, 2026-06-25. Nearest `main`
  commit `e62afaca6259278ef08d23cb178abf477597f986` (2026-06-25) used only
  as an approximate diff base. Status: current-only with approximate delta.
- Latest checked: default branch `main` HEAD
  `81a55437f3f31a9f12a30c53b6c5d49d420898aa` (2026-10-21, "fix(providers):
  allow external-process plugins to opt into streaming"). Release split:
  latest stable tag `v0.22.4` (`4d043038`, 2026-10-21, ancestor of HEAD);
  date-tag family latest `v2026.9.24`; prerelease
  `v0.22.4+canary.20261022T070155Z`. Root `package.json` stays `1.0.0`
  (not a release version). License still MIT.
- Actual changes (44,694 commits in range; README + surface inventory, not a
  full re-survey): README delta is small — provider list condensed to a docs
  link, seven terminal backends (Vercel Sandbox added), Desktop subagent
  routing, `hermes config get`, PM-delegated installer, Termux signed APT
  repo (`stable`/`canary` channels), MSIX/App Installer packaging. New
  structural surfaces: `plugin-catalog/` (763 YAML registry entries),
  `hermes_state_*` split from one module into ~60, `native/fts5_cjk`,
  `evals/`, `SOUL.md`. Security doc now states an eight-layer
  defense-in-depth model (authorization, command approval, write sandbox,
  container isolation, MCP credential filtering, injection scanning,
  cross-session isolation, input sanitization). Skills top-level dirs
  reorganized (18 → 14).
- Effect on prior findings: identity (persistent self-improving agent,
  messaging gateways, memory/skills/tools) confirmed unchanged; the "runtime
  reference only" judgement stands. Historical risk block stands and widens
  at source tier: plugin-catalog supply chain (hundreds of pinned
  third-party plugins), Desktop app, and MSIX/APT channels are new trust
  surfaces since June.
- Inspected: commit-pinned README, LICENSE, root trees, tag objects at
  `https://github.com/NousResearch/hermes-agent` (`main@81a55437`,
  `v0.22.4@4d043038`). No GitHub Release body read; tag objects + tree
  reads only.
- Untested limits: nothing installed or executed; provider/model counts,
  gateway behavior, and benchmark claims unverified; the 44k-commit range
  means the delta is sampled (README, roots, security doc, catalog
  presence), not exhaustive.

### Oh My Pi (`can1357/oh-my-pi`, CLI `omp`)

- Prior baseline: unpinned README read, 2026-06-25. Nearest `main` commit
  `c7d9abbcfdd3f39ed89448f8936e39c1b089ed50` (2026-06-25) used only as an
  approximate diff base. Status: current-only with approximate delta.
- Latest checked: default branch `main` HEAD
  `3a2758b68f7c8e6bdf22c3a76b86c8675e5e0c9e` (2026-10-21, Merge PR #16706,
  Anthropic API-version opt-in). Release split: latest tag `v18.12.6`
  (`45c35e40`, 2026-10-21) is a *distinct, earlier* commit — HEAD carries an
  `[Unreleased]` changelog section on top. Package
  `@oh-my-pi/pi-coding-agent` 16.1.18 → 18.12.6. License still MIT.
- Actual changes (22,486 commits, 9,364 files): README now credits "Built by
  Stencil Labs"; **60+** providers (was 40+), **31** built-in tools, ~80k
  Rust core lines (was ~55k). New documented tools since June: `computer`
  (desktop control), `security_scan` (opt-in, `security.enabled=false`
  default), `context-notes`, `manage_skill`, `learn`, `ida` (IDA Pro
  daemon), `generate_image`, `tts`, `todo`, `rewind`, `new-context`,
  `memory_edit`; `search` doc renamed to `grep` (version drift: old `search`
  references are stale). New packages: `browser-relay`, `metaharness`,
  `omptype`; removed: `hashline`, `swarm-extension`, `terminal-bench`.
  Build/install: Bazel + Nix flake (incl. Home Manager module), prebuilt
  binary from `build.stencil.so` with SHA-256 check, musl/`libstdc++` note;
  PRs temporarily open to all as a trial (vouch requirement lifted).
- Effect on prior findings: "host harness, not library content" stands —
  every new surface is harness/runtime-side. The falsifier still holds: no
  TeaPrompt promise may depend on omp-only enforcement.
- Inspected: commit-pinned README, LICENSE, package manifests, tool-doc
  inventory, `packages/coding-agent/CHANGELOG.md` head at
  `https://github.com/can1357/oh-my-pi` (`main@3a2758b6`,
  `v18.12.6@45c35e40`).
- Untested limits: source/doc tier only; no install, no execution; provider
  counts and benchmark rows (e.g. MiniMax 2.1×) unverified.
