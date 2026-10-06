---
name: headless-agent-cli-contract
description: Use when dispatching a task to a named third-party agent CLI headlessly. Given a target CLI plus intended mode (read-only proposal vs tool-using), emit a per-provider invocation recipe — prompt transport, headless permission flags, output isolation, and side-channels to strip — after a zero-cost inventory probe, and block when the CLI has no non-interactive mode.
license: MIT
compatibility: Requires a POSIX host with the named agent CLIs installed (zero-cost inventory probe first); recipes are per-provider spellings — TeaPrompt runs none of them.
metadata:
  risk_level: medium
  human_review_required: true
  external_io: true
  context_load: low
---

# Headless Agent CLI Contract

**Type:** Domain-pack skill (contract emission) — registered in the TeaPrompt source repo's domain-pack registry (`plans/validate_skill_examples.py` `DOMAIN_PACK_SKILLS`), not one of the nine frozen core workflow skills, and not selected by `reflective-dispatch` route rows; the host harness may invoke it directly.

## Purpose

Every agent CLI spells "run headlessly" differently, and guessing the spelling wastes billable invocations or silently corrupts outputs. This pack turns the observed 2026-10-06 dry-run receipts into a contract: given a target CLI and an intended mode, emit the exact invocation recipe for that provider — or block, with reasons, when the CLI cannot run non-interactively. Evidence: `plans/runtime-skills-task001-ticket-2026-10-06.md` TASK-004/005 receipts.

## Module Contract

### Trigger

- The host harness must invoke a named third-party agent CLI (`ollama`, `devin`, `cursor-agent`, `agy`, `claude`, `codex-cli`, `gemini`, `cx`, …) without an interactive terminal.
- A new CLI appears in inventory, or an existing recipe's flags stop working (version drift), or a run's output contains unexplained first-line/last-line noise.

### Inputs

1. `target_cli` — exact binary name and pinned version (from inventory, not memory).
2. `mode` — one of:
   - `read-only-proposal`: model returns a proposal; no tools, no writes, no approvals.
   - `tool-using`: model may execute tools; permission flags and human approval required.
3. `prompt_source` — prompt file path or stdin bytes (never inlined secrets).

### Methods

1. **Zero-cost inventory probe first.** Before any billable call: `command -v <cli>` then the CLI's zero-cost listing (`devin models list`, `ollama list`, equivalent). Record binary presence, version, and cheapest adequate model. Observed 2026-10-06: `devin models list` showed `swe-2-max` on the Free tier — the pilot's arm choice came from inventory, not guessing. Installed set pinned that day: claude 2.1.290, codex-cli 0.160.1, gemini 0.43.0, cursor-agent 2026.10.01, devin, agy, ollama (`qwen2.5-coder:1.5b` cached), cx 0.7.4 — dated facts, re-probe before reuse.
2. **Emit the per-provider recipe.** Each recipe names all five slots; unknown slots stay `UNKNOWN`, never defaulted:
   - *Prompt transport* — exact flag and spelling: `ollama` reads the prompt on **stdin**; `devin` / `cursor-agent` / `agy` take the prompt as a **CLI argv argument** (their own prompt flags, distinct from any wrapper's flags). Argv transport MUST use array-form exec with no shell interpolation, and the recipe MUST state the prompt-length cap handling for that CLI.
   - *Headless permission flags* — exact skip/approval flags needed so a non-interactive run does not stall on a prompt. For `agy` in `tool-using` mode the receipt prescribes an allow-rule under `permissions.allow` in `settings.json` (e.g. `command(<target>)`); the `--dangerously-skip-permissions` alternative is recorded but NEVER auto-selected — it requires explicit human approval per the `reflective-risk` boundary.
   - *Output-isolation flags* — flags separating proposal stdout from logs/stats (or, where none exist, the capture discipline: redirect stdout/stderr to separate files at the call site).
   - *Side-channels to strip* — provider-specific noise observed in receipts: `cursor-agent` stderr `claude-mem …` hook lines (side-path, not the proposal); `ollama` spinner glyphs (`⠙ ⠹ …`) and timing/stat block (`total duration: …`, `eval rate: …`) — channel varies run-to-run: 2026-10-06 run A put spinner+stats on **stdout**, run B put ANSI-wrapped spinner on **stderr** with stats absent entirely. Strip rules MUST cover both streams. TASK-005 B-control failed its oracle because stdout spinner pollution dropped the `## Next` heading form.
   - *Known malformed spellings* — `devin -p -` treats the literal dash as the prompt text (observed malformed invocation, re-run; receipt kept in `evidence/task005/`). Never assume `-` means stdin for a CLI that defines its own prompt argv.
3. **Blocking policy.** When the CLI lacks a non-interactive mode, or headless would require auto-approving destructive permissions, output `BLOCKED: <reason>` and stop. No pseudo-tty hacks, no expect-scripts, no silent `--dangerously-skip-permissions`. `agy` in the dry run is the reference case: headless auto-denied the `command` tool permission and produced no output — a provider policy, not a model failure; the correct outcome is a blocked receipt, not a retry with wider permissions.
4. **Mode separation.** `read-only-proposal` recipes MUST NOT include tool-use permission flags; `tool-using` recipes MUST name the human approval recorded before first unattended run (per flow-control-generator's Human Review Boundary) and the blast radius (host write-exclusions, egress stance).

### Never

- Never inline secrets or credentials into prompt payloads or recipe text.
- Never auto-select `--dangerously-skip-permissions`-class flags; they require explicit human approval per `reflective-risk`.
- Never default an `UNKNOWN` recipe slot (transport, permission flags, strip list) — emit it as `UNKNOWN` and require a probe.
- Never bypass a `BLOCKED` verdict with pseudo-tty hacks, expect-scripts, or widened permissions.
- Never re-bill a provider call to "fix" strip-list noise; fix the strip list on the existing receipt.
- Never claim a recipe is current beyond its pinned-version evidence; flag drift invalidates until re-probed.


### Output

- One invocation recipe for the (`target_cli`, `mode`) pair: transport spelling, permission flags, output-isolation discipline, strip list, inventory evidence — or a `BLOCKED` verdict with reason.
- One read-only proposal run per named CLI with raw receipts (stdout/stderr captured separately, exit code, artifact hashes) filed under the task's evidence dir.

### Escalation

- New CLI with no recipe and no non-interactive mode → `BLOCKED`, route to `reflective-risk` if the task still needs that provider.
- Steps touching credentials, billing tiers, production, or third parties → `reflective-risk` before the first billable call.
- Whether a model call is needed at all → `reflective-minimality`.
- Multi-step orchestration around the call → `flow-control-generator` (this contract supplies that script's `AGENT_CMD`).

### Failure signals

- Receipt's first line is spinner glyphs, hook chatter, or a stats block → strip-list incomplete; update the recipe, re-strip, never re-bill to "fix" it.
- `devin -p -`-class literal interpretation → malformed transport; fix spelling, re-run.
- Tool-permission auto-denial with zero output (`agy.out` shape) in `read-only-proposal` mode → wrong mode selected or CLI misclassified; in `tool-using` mode → missing allow-rule, human decision required.
- Any provider invocation succeeding while its caps envelope is `UNKNOWN` → governance failure (cf. TASK-004+ formal caps prerequisite); halt and route to owner.

### Verification

Before the recipe is handed to a host harness:

1. Run the zero-cost inventory probe; record binary, version, model list.
2. Run one `read-only-proposal` per named CLI with stdout/stderr split; file raw receipts. Expected shapes: `ollama`/`devin`/`cursor-agent` return the minimal fix (`return a + b` on the A-code fixture); `agy` without an allow-rule returns the policy-denial receipt (blocked, not failed).
3. Score only the stripped stdout against the oracle; confirm the strip rules turn the observed polluted outputs into passes without touching model content.
4. Confirm no billable call ran before inventory, and no `BLOCKED` verdict was bypassed with widened permissions.

## Honest Limits

- All provider invocations ran host-side: seatbelt denies the egress they need (even ollama's loopback), so every receipt is host-context evidence. A sandboxed *model* worker has zero evidence; containment claims scope to the stub worker.
- Treatment/control pilot arms differed in model *and* guidance (`devin swe-2-max` vs `ollama qwen2.5-coder:1.5b`) — composite effect only, n=1 per arm, directional.
- Recipes pin observed versions; CLI flag drift invalidates a recipe until re-probed.
- No recipe covers cost/latency envelopes: host-enforced caps stayed `UNKNOWN` (no budgeted model calls in the dry run) and remain a hard prerequisite before repeated or tool-using runs.

## Examples

Companion examples live in the installed `<skills-root>/examples/headless-agent-cli-contract.examples.md` tree when examples are co-installed. They show the recipe five-slot shape, strip-list receipts, and the `BLOCKED` verdict format, not provider endorsements.

## Prompt Sources

*Provenance: TeaPrompt source-repository paths (`reflective-prompt-library/`), not runtime dependencies — the installed skill is self-contained.*

- `04-agent/runtime-trust-boundary.md`
- `04-agent/agent-scaffold-provenance.md`
- `plans/runtime-skills-workflow-spec-2026-10-06.md` (RSD-2)
- `plans/runtime-skills-task001-ticket-2026-10-06.md` (receipts)
