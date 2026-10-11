---
name: flow-loop-harness
description: Use when an agent must iterate until a condition is verified — fix-until-tests-pass, writer-critic refinement, backlog burn-down, ralph-style loops — over a host agent CLI in headless mode. It writes loop scripts whose stop conditions are external deterministic verifiers.
license: MIT
compatibility: Requires a POSIX host with bash 3.2+ and a headless host agent CLI; git enables progress detection; unattended or side-effectful loop runs stay human-gated.
metadata:
  risk_level: medium
  human_review_required: true
  external_io: false
  context_load: medium
---

# Flow Loop Harness

**Type:** Domain-pack script-generation skill, registered in `DOMAIN_PACK_SKILLS`; outside the nine frozen core skills and `reflective-dispatch` route rows. `flow-control-generator` owns one-pass topologies.

## Purpose

Generate host-executed loop scripts: model work inside, deterministic caps, progress and resume control outside. TeaPrompt is methodology, not a runner; the script is a host-operationalized artifact (`plans/external-adoption-case-studies-2026-06-20.md`). Never trust model "done": require an external verifier; writer-critic is the labelled advisory-tier exception. Survey vocabulary is advisory (`plans/agent-flow-control-research-2026-07-11.md`).

## Module Contract

Trigger:

- The user asks to "loop until", "keep going until tests pass", "iterate", "retry until green", "ralph", "burn down this backlog", or "refine until the critic accepts".
- A task has an objective completion check that the first agent pass is unlikely to satisfy.
- A refinement task needs bounded writer-critic rounds against a rubric.

Methods:

- Apply the six-part Loop Anatomy, with its labelled template deviations; instantiate the matching loop template from `TEMPLATES.md`.
- Use a resume ledger only as a host-honored convention, never crash-safety.
- Prove control flow with a scripted stub before real use.

Output:

- One runnable loop script plus prompt file(s) and a verifier hook (`checks/*.sh` or equivalent), written where the user chooses.
- A run note stating: stop condition, iteration cap, budget caps, resume command, and the human-approval boundary.
- A ledger file format the user can inspect mid-run (`state/ledger.md`).

Never:

- Never emit an unbounded loop; `MAX_ITER` is mandatory and small by default (≤ 10 unless justified).
- Never weaken tests, thresholds, or expected outputs to exit (Anti-cheating Rules).
- Never grant the loop body broader permissions than the task needs; pre-approval flags are part of the reviewed config, not improvised.
- Never run a side-effectful loop (deploy, billing, data mutation, third-party calls) unattended without a recorded human approval.
- Never claim crash-safety or idempotency: the host owns durability (`04-agent/runtime-trust-boundary.md`).
- Never return the last unverified output as the result when a cap is exhausted — cap exhaustion is exit 2 and a human decision, not a soft success (negative example: a max-turns "return last response", `plans/openfugu-technical-brief-2026-06-25.md`).
- Never treat run state as project memory: `state/` is a per-run operational ledger, distinct from the in-task State Ledger and durable knowledge; promote it via `reflective-handoff-retro` plus the memory-write provenance gate (`04-agent/artifact-promotion.md` §4).

Escalation:

- Known fixed stages without iteration → `flow-control-generator`.
- No objective verifier exists → the loop is not safe to automate; route to `reflective-brief` to define acceptance criteria, or keep a human in the loop each round.
- Side effects on credentials, permissions, privacy-sensitive data, billing, production, or destructive operations → `reflective-risk` before first run; add an in-loop pause for each side-effectful action.
- Multi-session, cancellable, replayable workflow requirements → `reflective-spec-plan`; a shell loop cannot provide those guarantees.
- Loop keeps hitting the cap without converging → stop; escalate to `reflective-review` on the artifacts instead of raising the cap.

## Loop Anatomy

Every generated loop must contain all six parts:

1. Verifier: committed deterministic command under `checks/`; exit code alone decides success. Preflight executable availability → exit 4 (bash 3.2 exec failures are unreliable); run before the first iteration and after each. Preflight unattended writer-critic floor executables before **any** agent call.
2. Caps: mandatory `MAX_ITER` (`MAX_ROUNDS`/`MAX_WAVES`/`MAX_JOBS` where the template composes them); every arithmetic cap is validated as canonical positive decimal before first dispatch and before any arithmetic evaluation — `1`–`2147483647` with no leading zero, no empty value, no expression, and no silent env-default fallback when the variable is explicitly set but empty. Invalid caps exit 4 with zero dispatches and zero command expansion. Cap exhaustion is not step failure.
3. Ledger: append iteration, verifier result and progress. Fresh agent contexts read its bounded tail, not accumulated chat; append `RESUMED` on restart with a nonempty ledger.
4. Progress detector: abort on equal content signals, not equal churn. Hash staged + unstaged binary diffs (including names/deletions) and untracked contents, excluding STATE. Outside git, disable detection and rely on caps.
5. Permission boundary: human-reviewed least-privilege host flags (e.g. `--allowedTools` / permission mode). Host MUST exclude `checks/`, canonical `state/TASKS.canon` and `prompts/critic-rubric.md` as applicable from agent writes. Comments/copies do not enforce these exclusions.
6. Exits: `0` verified done; `2` cap; `3` no progress, verify-fail stop, or worker failure; `4` missing/non-executable verifier, invalid cap, missing/unreadable canonical backlog, or selected-preflight failure; `5` raw worker exit 4 remapped away from the reserved configuration class. Callers must distinguish them.

Selected preflight gate (shared interface): `PREFLIGHT="${PREFLIGHT:-}"` names one executable file, never shell text. Empty preserves ordinary attended behavior and claims no runtime enforcement; a workflow requiring observed host preconditions must set it, and empty never means met. When set, every template checks executability before the first/each agent dispatch — including the zero-call already-converged/already-verified/backlog-empty path — invokes it with no shell (`"$PREFLIGHT"`, per-stage capture under `$STATE/preflight-<stage>.out`; `flow.log` holds one log line per check), and exits 4 before the verifier result is accepted, the final artifact is published, the backlog line is retired, or the satisfied queue retires — including under partial multi-wave policy. Gate output is point-in-time evidence, not enforcement proof; the host owns the gate, manifests, and write exclusions. There is no cancellation manager: killing the driver does not cancel in-flight agent/child processes (driver SIGTERM can leave a stand-in child alive in its own group; examine the process group and stop only coordinator-created groups), and absence of lifecycle evidence is unknown, not kill assurance.

Templates use stdin prompts; choose a stdin-capable host command/wrapper, not argv payloads. Their headers record source/topology/date/dry-run status, task-root cwd and reviewed flag preconditions; put actual reviewed flags in AGENT_CMD, never invent allowlists. Append step start/end and gates to STATE/flow.log.

## Templates

Instantiate the matching template in `TEMPLATES.md` — the portable sibling in
this skill's package directory (installed at
`<skills-root>/flow-loop-harness/TEMPLATES.md` when the package is copied); it
travels with `SKILL.md` outside the TeaPrompt checkout. Menu:

| Loop shape | Template section |
| --- | --- |
| Verify-gated fix loop | `## Template: Verify-Gated Fix Loop (bash)` |
| Evaluator-optimizer / writer-critic | `## Template: Evaluator-Optimizer / Writer-Critic (bash)` (+ `### Deterministic companion check`) |
| Task-ledger backlog | `## Template: Task-Ledger Backlog Loop (bash, ralph-style)` |
| Multi-wave fan-out | `## Template: Multi-Wave Fan-out (bash)` |

Start from the matching template; delete unused parts before adding anything.
The bodies there keep their exact executable bytes, exit codes, caps, ledger
and progress-detector discipline, and runtime-honesty labels — regenerate or
re-copy from `TEMPLATES.md` rather than patching a drifted copy. Writer-critic
keeps its labelled advisory-tier ACCEPT verdict plus the deterministic
companion floor; do not copy those deviations into the verify-gated loops.


## Human Review Boundary

Unattended: recorded approval of verifier, caps, host flags and blast radius. Attended: verifier and caps. Every auth, migration, destructive, billing, production or privacy action still needs a per-action pause.

## Verification

1. Stub dry run: prove exits 0/2/3/4, including missing verifier/floor before calls, equal-churn content changes, true stalls and reused STATE with failed/empty branches. With `PREFLIGHT` unset the attended path is unchanged; with a failing/missing selected gate the script exits 4 before dispatch and before acceptance, including the zero-call already-done path and partial multi-wave tallies. This is rig-tier control-flow evidence, not production or host-enforcement proof.
2. `bash -n` the script; run `shellcheck` when available.
3. Confirm the verifier is committed and deterministic, every dispatch carries the shared `preflight()` gate before and after, and record the Anatomy #5 host permission mode.
4. Report dry-run evidence with the deliverable. A required-precondition workflow's run note names the selected `PREFLIGHT` executable; never imply an empty gate means met.

Durable promotion requires fail-closed Acquisition L3 gates (`04-agent/artifact-promotion.md` §4), recurrence evidence and explicit human approval.

## Host-Native Alternatives

Prefer host-native keep-working modes for transcript-judgeable, single-run, low-blast-radius tasks. Generate scripts for deterministic verifiers, caps, progress detection, retirement or resume ledgers — the stop-condition class this skill forbids trusting alone to a model over the transcript.

## Demotion Triggers

- Regenerate disposable scripts when verifier, host CLI or task shape changes; check pack demotion triggers (zero recurrence / host absorption) in `plans/agent-flow-control-research-2026-07-11.md`.

## Examples

Companion examples live at `<skills-root>/examples/flow-loop-harness.examples.md` when co-installed. They show loop shapes and rig-tier checks, not production proof.

## Prompt Sources

*Provenance: TeaPrompt source-repository paths (`reflective-prompt-library/`), not runtime dependencies — the installed skill is self-contained.*

- `plans/agent-flow-control-research-2026-07-11.md`
- `plans/flow-control-pack-panel-record-2026-07-11.md`
- `plans/flow-coverage-panel-record-2026-07-11.md`
- `plans/harness-1-state-ledger-research.md`
- `04-agent/workflow-recipes.md`
- `04-agent/runtime-trust-boundary.md`
- `04-agent/artifact-promotion.md`
- `06-repo/AGENTS.md`
