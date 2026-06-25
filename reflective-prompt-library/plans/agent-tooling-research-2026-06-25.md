# Agent Tooling Research — 2026-06-25

Language: English

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
