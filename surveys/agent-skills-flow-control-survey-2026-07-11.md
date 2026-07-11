# Agent Skills and Flow-Control Survey — 2026-07-11

> **Status: reference survey (advisory tier).** Primary-documentation survey of the
> agent-skills standard and host flow-control surfaces as of 2026-07-11. Kept as
> reference evidence per the surveys convention; it decides nothing. Adoption of
> anything here goes through the external-adoption and promotion gates
> ([artifact-promotion](../reflective-prompt-library/04-agent/artifact-promotion.md),
> [external-adoption-review](../reflective-prompt-library/04-agent/external-adoption-review.md)).
> External interest is never local promotion evidence. Companion planning artifacts:
> [skills-surface plan](../reflective-prompt-library/plans/skills-surface-plan-2026-07-11.md),
> [flow-control roadmap](../reflective-prompt-library/plans/flow-control-roadmap-2026-07-11.md),
> [routing-holdout plan](../reflective-prompt-library/plans/routing-holdout-plan-2026-07-11.md).

## Method and evidence tiers

Read directly this session (2026-07-11) from primary documentation: the Agent
Skills specification and adopter registry (agentskills.io), Claude Code docs
(skills, commands, goal), Codex skills docs (learn.chatgpt.com), Gemini CLI
skills docs, and the OpenAI Agents SDK index. Everything below is **primary-doc
tier unless marked** `[search-derived]` (unconfirmed) or `[INFERENCE]`.
This survey extends, and does not replace, the flow-control research record of
the same date ([agent-flow-control-research-2026-07-11.md](../reflective-prompt-library/plans/agent-flow-control-research-2026-07-11.md));
that record's six-source platform table remains valid.

## Part 1 — The Agent Skills standard (major delta)

### Specification state

Spec at agentskills.io/specification: a skill = directory with `SKILL.md`
(YAML frontmatter + markdown body) plus optional `scripts/`, `references/`,
`assets/`.

| Field | Spec status | Constraint |
| --- | --- | --- |
| `name` | Required | ≤64 chars, lowercase/digits/hyphens, must match parent directory name |
| `description` | Required | ≤1024 chars, what + when |
| `license` | Optional | short name or bundled-file pointer |
| `compatibility` | Optional | ≤500 chars, environment requirements |
| `metadata` | Optional | arbitrary string map — the spec's designated home for non-spec properties |
| `allowed-tools` | Optional, experimental | space-separated pre-approved tools |

Progressive-disclosure guidance: metadata ~100 tokens at startup; body <5000
tokens on activation; resources on demand; keep `SKILL.md` under 500 lines.
A reference validator exists: `skills-ref validate` (github.com/agentskills/agentskills).

### Adoption

The registry lists 30+ hosts including Claude Code, Claude (platform), OpenAI
Codex, Gemini CLI, GitHub Copilot, VS Code, Cursor, OpenCode, Goose, JetBrains
Junie, Amp, Roo Code, Letta, Factory, OpenHands, Mistral Vibe, TRAE, Spring AI,
Databricks Genie Code, Qodo, Laravel Boost, pi. The format TeaPrompt chose for
its workflow skills is now a cross-vendor standard, not an Anthropic-only
convention.

**Cross-host path convention:** `.agents/skills/` is the interoperable location —
Codex scans `$CWD/.agents/skills` up to repo root plus `~/.agents/skills`
(user), `/etc/codex/skills` (admin); Gemini CLI treats `.agents/skills/` as a
higher-precedence alias of `.gemini/skills/`; Claude Code keeps `.claude/skills/`
but reads nested and parent directories.

### Context budgets for skill listings (affects description writing)

- Codex: the initial skills list gets at most **2% of the context window or
  8,000 chars**; descriptions are shortened first, then skills omitted with a
  warning. Front-load trigger words.
- Claude Code: combined `description` + `when_to_use` truncated at **1,536
  chars** in the listing.
- TeaPrompt conformance today (measured this session): all 11 skills pass the
  directory-name rule; longest description 450 chars — within every budget.

### Invocation control and trust (converging pattern)

- Claude Code: `disable-model-invocation`, `user-invocable`, `allowed-tools` /
  `disallowed-tools`, per-skill `hooks`, `paths`-scoped activation.
- Codex: `agents/openai.yaml` → `policy.allow_implicit_invocation: false`,
  declared tool dependencies (MCP).
- Gemini CLI: explicit **consent prompt** on activation (shows skill name,
  purpose, directory access it will gain); `--consent` flag for installs;
  enable/disable per scope.

[INFERENCE] Hosts are building exactly the machine-readable gating TeaPrompt's
governance frontmatter (`human_review_required`, `external_io`) anticipates —
but under different, host-specific field names. TeaPrompt's four governance
fields are top-level frontmatter, which the spec does not define; the spec's
designated extension point is the `metadata` map. **Outcome (same day):**
`skills-ref` 0.1.1 *rejects* unknown top-level fields (observed FAIL on all 11
skills); the fields were migrated under `metadata:` and 11/11 now validate —
see the skills-surface plan Execution Ledger (S1).

### Skill-generating and skill-acquiring machinery

- Codex `$skill-creator` (interactive authoring), `$skill-installer` (curated
  installs), **Record & Replay** (records a demonstrated workflow, drafts a
  reusable skill from it) — the sop-compiler/workflow-acquisition methodology
  operationalized host-side.
- Claude Code `/run-skill-generator` (records a project's build/launch recipe
  as a per-project skill), plugins + marketplaces for distribution; skills can
  be chained (up to six per message) and merged with commands.
- Gemini CLI `gemini skills install <git-url>` with security acknowledgment.

## Part 2 — Flow-control deltas (host-native loops arrived)

### Claude Code native surfaces (primary docs, all verified this session)

| Surface | Semantics | Stop condition owner |
| --- | --- | --- |
| `/goal <condition>` (v2.1.139+) | Cross-turn loop: after each turn a small fast model (default Haiku) judges the condition against the transcript; "no" starts another turn with the reason as guidance. Condition ≤4,000 chars; turn/time bounds only as condition clauses; works headless (`claude -p "/goal …"`); survives resume | **Model judge** (prompt-based Stop hook wrapper); does not run commands or read files |
| `/loop [interval] [prompt]` | Re-run a prompt on a time interval (or self-paced) while the session is open; `.claude/loop.md` default prompt | Operator stop, or model decides done |
| Stop hooks | Fire after every turn; **can run a script for deterministic checks** or a prompt for model-evaluated ones; settings-scoped | Script (deterministic) or prompt (model) |
| `/batch <instruction>` | Decomposes a large change into 5–30 independent units, one background subagent per unit in an isolated git worktree, each runs tests and opens a PR | Plan approval + per-unit tests |
| Bundled workflows (`/deep-research`) + `ultracode` effort | Dynamic multi-subagent fan-out in the background; `ultracode` = xhigh reasoning + automatic workflow orchestration | Host runtime |
| `/schedule` (cloud routines), desktop scheduled tasks | Work runs independent of any open session; skills can be a scheduled task's prompt | Scheduler |
| `/autofix-pr`, `/background`, `/fork` | PR-watch fix loop in cloud; detached background sessions; forked subagents inheriting full conversation | Host runtime |

**The decisive detail for TeaPrompt's flow packs:** `/goal`'s evaluator is a
model judge that "does not call tools, so it can only judge what Claude has
already surfaced." The pack's own operating principle (and
`reflective-spec-plan`'s verifier rule) requires deterministic external checks
as the only trusted stop condition. Native `/goal` therefore does **not** meet
the bar the pack sets; a Stop hook running a script does, but ships no packaged
ledger/backlog/writer-critic structure. Demotion-trigger analysis is scheduled,
not decided, in the [flow-control roadmap](../reflective-prompt-library/plans/flow-control-roadmap-2026-07-11.md).

### OpenAI Agents SDK (still active, code-first)

Confirmed current at openai.github.io/openai-agents-python: agents, handoffs /
agents-as-tools, parallel guardrails, sessions (persistent memory layer),
human-in-the-loop, tracing — plus new since the prior record: **Sandbox agents**
(isolated per-agent workspaces, manifest-defined files, resumable sandbox
sessions) and realtime agents. The AgentKit visual-builder wind-down claim
remains `[search-derived]` — no primary source encountered confirms or denies
it; the docs migration (developers.openai.com/codex → learn.chatgpt.com, plugins
distributing to "ChatGPT Work") is consistent with a consolidation but proves
nothing. Recorded as **unknown**.

### Google

Gemini CLI adopted Agent Skills (activation via `activate_skill` tool with
consent UI). Platform churn note on the docs banner: unpaid-tier and Google One
users' Gemini CLI "will be replaced by Antigravity CLI on June 18th" — watch
item for SKILL_INSTALLATION host coverage.

## Part 3 — TeaPrompt impact map (no decisions here; pointers only)

| Finding | Existing surface it touches | Disposition |
| --- | --- | --- |
| `/goal` native + confirmed | Pack record demotion trigger ("host-native flow feature") | Evaluated 2026-07-11: **not fired** → [record](../reflective-prompt-library/plans/flow-pack-demotion-evaluation-2026-07-11.md) |
| `/loop`, Stop hooks, `/schedule` | Same trigger family; looper-topology vocabulary in [workflow-recipes](../reflective-prompt-library/04-agent/workflow-recipes.md) | Watch + F1 input |
| `/batch` worktree fan-out | Orchestrator-workers template; P12 DAG deferral | No change; P12 trigger unchanged |
| Spec `metadata` map vs top-level governance fields | All 11 SKILL.md frontmatter; `validate_links.py` schema | S1 executed: skills-ref FAIL observed → fields migrated under `metadata:`; 11/11 validate |
| Spec `compatibility` field | Pack host-precondition prose | Candidate S5 (gated) |
| Description/context budgets | Skill descriptions; cheatsheet | Conformant today; guard candidate S2 |
| `.agents/skills/` convention | [SKILL_INSTALLATION](../reflective-prompt-library/SKILL_INSTALLATION.md), README quick start | Parity check S4 |
| Plugins / marketplaces / `gemini skills install` | Distribution (copy/symlink only today) | Candidate S3 (adoption-signal gated) |
| Record & Replay, `$skill-creator`, `/run-skill-generator` | [workflow-acquisition](../reflective-prompt-library/04-agent/workflow-acquisition.md), sop-compiler | Reference note candidate; M4 trigger unaffected |
| Consent-gated activation (Gemini) | [runtime-trust-boundary](../reflective-prompt-library/04-agent/runtime-trust-boundary.md) | Vocabulary reference only |
| Sandbox agents (OpenAI) | Standing Non-Goal (no owned runtime) | Reference only |

## Verification ledger

- **Executed locally:** frontmatter conformance check over `skills/*/SKILL.md`
  (11/11 directory-name match; description lengths 195–450 chars).
- **Read (primary):** agentskills.io home + specification; code.claude.com docs
  for skills, commands, goal; learn.chatgpt.com build-skills; geminicli.com
  skills; openai.github.io/openai-agents-python index.
- **Not verified:** AgentKit wind-down (unknown); `/loop` full skill body
  behavior beyond the commands-reference entry; every claim about hosts not
  listed in "Read" above. (The formerly untested skills-ref unknown-field
  behavior was settled same-day: strict rejection, observed — see S1.)

## Falsifiability

This survey is wrong if any cited primary page did not state the quoted
behavior on 2026-07-11 (all quotes trace to the listed URLs), or stale once a
cited surface changes — re-verify before reliance; the flow-control roadmap's
watch table owns re-check triggers.

## Sources (retrieved 2026-07-11)

- https://agentskills.io/home and https://agentskills.io/specification
- https://code.claude.com/docs/en/skills
- https://code.claude.com/docs/en/commands
- https://code.claude.com/docs/en/goal
- https://learn.chatgpt.com/docs/build-skills (Codex skills)
- https://geminicli.com/docs/cli/skills/
- https://openai.github.io/openai-agents-python/
