---
name: flow-control-generator
description: Use when a task needs an executable flow-control script that coordinates agent steps — sequential pipelines, parallel fan-out/fan-in, conditional routing, or orchestrator-worker delegation — over a host agent CLI or SDK. It classifies the task shape, picks the smallest topology, and writes a deterministic script with state files, verification gates, and budgets. For iterate-until-done loops, use flow-loop-harness.
license: MIT
compatibility: Requires a POSIX host with bash 3.2+ (Python 3.9+ for the Python templates — no union annotations or post-3.9 stdlib) and a headless host agent CLI; generated scripts run on the host, not in TeaPrompt.
metadata:
  risk_level: medium
  human_review_required: false
  external_io: false
  context_load: medium
---

# Flow Control Generator

**Type:** Domain-pack skill (script generation) — registered in the TeaPrompt source repo's domain-pack registry (`plans/validate_skill_examples.py` `DOMAIN_PACK_SKILLS`), not one of the nine frozen core workflow skills, and not selected by `reflective-dispatch` route rows; the host harness may invoke it directly.

## Purpose

Turn a multi-step agent task into a small, deterministic, host-executable flow-control script. The script owns control flow; the model owns step content. TeaPrompt stays methodology-side: host-operationalized artifacts, not a runtime (`plans/external-adoption-case-studies-2026-06-20.md`).

## Module Contract

Trigger:

- The user asks to chain, pipeline, fan out, route, orchestrate, or script multiple agent-CLI steps.
- The task decomposes into ordered or independent steps whose sequencing must not be left to model improvisation, or a prompt-only recipe keeps losing ordering, gates, or intermediate outputs.

Methods:

- Task-shape classification: map the task to the smallest sufficient topology (see Topology Selection).
- Script contract: every generated script carries the eight parts listed under Script Contract, in order.
- Template instantiation: start from the matching template in `TEMPLATES.md`; delete unused parts before adding anything.
- Stub dry run: verify the script's control flow with a deterministic stub agent before any real run.

Output:

- One runnable script (bash for CLI glue; Python stdlib for bounded concurrency or richer state) plus per-step prompt files, written where the user chooses.
- A run note: dry-run/run commands, state and log locations, budget caps, and the human approval required when any step has side effects.
- Named gates: which deterministic check releases each stage.

Never:

- Never generate a fix-until-green loop here; use `flow-loop-harness`.
- Never let the model decide known control flow at runtime; encode it in the script.
- Never script epistemic perspective expansion (STORM-style discovery) as parallel execution; it belongs in `reflective-research`.
- Never treat agent self-report as a gate; gates are deterministic exit codes.
- Never embed secrets, auto-approve destructive permissions, widen tool allowlists, or let a stage edit its own gates/checks/plan.
- Never claim persistence, crash-safety, or idempotency; `state/` is only a host-honored resume convention.
- Never choose topology from platform prestige; choose from task shape and local need.

Escalation:

- Iterative refinement or fix-until-green loops → `flow-loop-harness`.
- Unclear goal or acceptance criteria → `reflective-brief` first.
- Long-running, resumable, multi-session workflow design → `reflective-spec-plan` (companion: `04-agent/workflow-engine.md`).
- Steps touching credentials, permissions, privacy-sensitive data, billing, production, data deletion, destructive operations, or third parties → `reflective-risk` before the script runs; insert an explicit human-approval pause step.
- Whether the flow should exist at all (one agent call might do) → `reflective-minimality`.

## Topology Selection

Pick the smallest topology that fits. Composition is allowed; justify each layer. Multi-wave breadth belongs inside `flow-loop-harness`.

| Task shape | Topology |
| --- | --- |
| Fixed known stages, each consumes the previous output | Sequential pipeline |
| Independent subtasks, results merged once | Parallel fan-out/fan-in |
| Input classes need different handling | Conditional router |
| Subtasks unknown until a planner sees the task | Orchestrator-workers |
| Quality must converge over rounds | Loop → `flow-loop-harness` |

If no row fits, the task is probably a single agent call; say so.

## Script Contract

Every generated script must contain, in order:

1. Config: `AGENT_CMD` (reviewed host CLI/wrapper, flags and stdin/file support; unset falls back to the documented example default — explicitly empty or whitespace-only is a configuration failure, exit 4 before any dispatch), workdir, `STATE`, caps, `PREFLIGHT` (optional executable pathname, not shell text; empty = attended example without claimed runtime enforcement), `FAIL_SIGS`/`RETRY_REASON` (repeated-failure discipline below), and generated-by skill/topology/date/dry-run status. Every arithmetic cap (`MAX_JOBS`, `MIN_OK`, `MAX_WORKERS`) is validated as canonical positive decimal before first dispatch and before any arithmetic evaluation — `1`–`2147483647` with no leading zero, no empty value, no expression, and no silent env-default fallback when the variable is explicitly set but empty (`MIN_OK` additionally allows empty for strict mode and `0` for its zero-quorum spelling). Invalid caps exit 4 with zero dispatches and zero command expansion.
2. State: one output file per step, not shell-variable payloads; inspectable partial files support a host-honored resume convention.
3. Runner: all calls go through `run_agent`; prompt content via stdin, never argv. In Python that means `subprocess.run(AGENT_CMD, input=prompt, ...)` — do not append the prompt to `AGENT_CMD` (for `bash`-class workers, argv text becomes the *command*, silently executing the prompt as code). Note the invocation spelling matters: `bash -lc` parses `-lc` as `-l`+`-c`, shifting the real command into `$0` — observed failure 2026-10-06, exit 134.
4. Gates: deterministic exit codes release stages; absent checks say `# gate: none (accepted)`. For fan-in, the gate runs over the merged result as well as the branch tally: branches that each pass can conflict when combined. When `PREFLIGHT` is set, its exit-4 gate runs before each agent dispatch and after that dispatch before the stage gate accepts, publishes, or merges; gate output is evidence, never enforcement proof.
5. Budget: cap concurrency and total steps; per-call timeout/cost caps where supported. When a stage is itself a loop or retries, the composition's worst case is the product of the caps: declare one total budget (steps or wall-clock) that every level decrements, and have the outer script pass its remaining budget to the inner one. Stock macOS has no `timeout`; a bash timeout wrapper is host-provided.
6. Permissions: record least-privilege host flags in `AGENT_CMD`; review them and host write-exclusions before unattended use. Defaults are attended examples, not approval. macOS seatbelt specifics observed 2026-10-06: profiles must use canonical paths (`/tmp` is a symlink to `/private/tmp` — deny rules on `/tmp/...` do not match); `deny default` without a `file-read*` grant aborts `bash` at launch (SIGABRT), so worker *read* scope is effectively unscoped — declare confidentiality-not-claimed or use a non-shell worker; a write allowlist covering a parent dir subsumes everything under it (scope scratch grants to a sibling dir).
7. Logs: `STATE/flow.log` records step start/end and gate results; workdir is the reviewed task root.
8. Exits: bash `set -euo pipefail` or Python exceptions; failed gates exit nonzero and retain partial state. Selected-preflight missing/non-executable/nonzero and topology configuration failures (including empty `AGENT_CMD` and a `FAIL_SIGS` path inside worker-writable `STATE`) exit 4; a refused identical-redispatch hold exits 3 and is never quorum-tolerable; partial-failure quorums never swallow exit 3 or 4. Raw worker exit codes are logged as evidence; the generator reserves no exit code for worker use.

Repeated-failure discipline (observed 2026-10-06 dry run): on agent failure, record a failure signature (e.g. hash of the prompt/task identity plus error class) in a driver-owned path outside the worker's write allowlist (`STATE/` counts only if the worker cannot write it) and check it before dispatch; a re-dispatched identical signature escalates (exit nonzero / hold) instead of retrying identically, while a distinct signature may proceed within budget. A bare `exit` on failure alone leaves identical-retry as the default behavior — record it, don't assume it. Observed defect 2026-10-06: `fail-signatures.jsonl` under worker-writable `STATE/` let the sandboxed worker truncate or forge it, silently defeating the refusal.
Concrete signature mechanics in every shipped template: `FAIL_SIGS` names a driver-owned file outside the worker write allowlist (default `fail-signatures.jsonl` beside the resolved state dir — a sibling of `STATE`, writable only where the host says so; setting it inside worker-writable `STATE/` silently re-creates the 2026-10-06 forgery defect and is rejected as configuration). On agent failure the driver appends a line holding the prompt-identity signature (`cksum` of the prompt file in bash, `sha256` in Python), the raw exit code, and the error class; before every dispatch the driver refuses an identical stored signature (exit 3, logged `refuse-identical-retry`) unless `RETRY_REASON` names the changed strategy or corrected input — `RETRY_REASON` is stamped on that dispatch's record, must differ from a previous one to re-authorize the same signature, and never rewrites or deletes earlier receipts. Raw failed-run outputs (`<out>.failed-<exit>`) and log lines stay on disk as receipts.

`AGENT_CMD` configuration: unset falls back to the documented example default; explicitly empty or whitespace-only is a configuration failure — exit 4 before any dispatch with a diagnostic, never a silent provider default.

Selected preflight gate (shared interface): `PREFLIGHT="${PREFLIGHT:-}"` names one executable file, never shell text. Empty preserves ordinary attended behavior and claims no runtime enforcement; a task requiring observed host preconditions must set it, and empty never means met. When set, every template checks executability before the first/each agent dispatch (zero-call already-done paths check too), invokes with no shell (Python passes `[PREFLIGHT]` argv; bash runs `"$PREFLIGHT"`), captures output per stage (`$STATE/preflight-<stage>.out`, per-branch files under parallel fan-out; `flow.log` holds one log line per check), and exits 4 before the stage gate accepts, the merged result publishes, or the queue retires — including under `MIN_OK`/partial policies. Gate output is point-in-time evidence, not enforcement proof; the host owns the gate, manifests, and write exclusions. There is no cancellation manager: killing the driver does not cancel in-flight agent/child processes (examine the process group; stop only coordinator-created groups), and absence of lifecycle evidence is unknown, not kill assurance.

## Templates

Instantiate the matching template in `TEMPLATES.md` — the portable sibling in
this skill's package directory (installed at
`<skills-root>/flow-control-generator/TEMPLATES.md` when the package is
copied); it travels with `SKILL.md` outside the TeaPrompt checkout. Menu:

| Topology | Template section |
| --- | --- |
| Sequential pipeline | `## Template: Sequential Pipeline (bash)` |
| Parallel fan-out/fan-in | `## Template: Parallel Fan-out/Fan-in (bash)` |
| Conditional router | `## Template: Conditional Router (bash)` |
| Orchestrator-workers | `## Template: Orchestrator-Workers (Python, stdlib only)` |
| DAG executor | `## Template: DAG Executor (Python, stdlib only)` |

Start from the matching template; delete unused parts before adding anything.
The bodies there keep their exact executable bytes, exit behavior, caps,
signature discipline and runtime-honesty labels — regenerate or re-copy from
`TEMPLATES.md` rather than patching a drifted copy.


## Human Review Boundary

Before the first unattended run of any generated script with side effects, a human must approve gates, caps, permission flags, blast radius, and every auth/permission/destructive/billing/production/privacy/migration/API/third-party step. Record the approval in the run note. Attended runs may review only gates and caps; side-effectful steps still need a per-action pause.

## Verification

Before handing a generated script to the user:

1. Stub dry run: `AGENT_CMD='cat'`, or a stub echoing shaped outputs (router: fixed label; orchestrator: JSON plan); control flow, gates, and state files must behave with zero model calls. Stub success is rig-tier evidence for control flow, never for a production or side-effectful run. With `PREFLIGHT` unset the attended path is unchanged; with a failing/missing selected gate the script exits 4 before dispatch and before acceptance, including under `MIN_OK` and in zero-call paths.
2. `bash -n` / `python3 -m py_compile` the script.
3. Confirm every stage has a gate or an explicit `# gate: none (accepted)`, plus the shared `preflight()` gate before each dispatch and after it before acceptance, the `FAIL_SIGS` refusal path (a second identical failing stub run must exit 3 with zero new dispatches before any `RETRY_REASON` run), and the `AGENT_CMD` empty → exit 4 config check.
4. Report the dry-run evidence in the run note; an unexercised script is not done. A required-precondition workflow's run note names the selected `PREFLIGHT` executable; never imply an empty gate means met.

Promoting a generated flow into a durable artifact needs fail-closed Acquisition L3 gates (prompt-injection authority boundary, supply-chain provenance, memory-write provenance; `04-agent/artifact-promotion.md` §4), recurrence evidence and explicit human approval.

## Demotion Triggers

- Generated scripts are disposable: regenerate on host CLI, task shape or gate changes; pack-level demotion triggers (zero recurrence, host absorption) live in `plans/agent-flow-control-research-2026-07-11.md`.

## Examples

Companion examples live at `<skills-root>/examples/flow-control-generator.examples.md` when co-installed. They show script shapes and rig-tier checks, not production or unattended-run proof.

## Prompt Sources

*Provenance: TeaPrompt source-repository paths (`reflective-prompt-library/`), not runtime dependencies — the installed skill is self-contained.*

- `plans/agent-flow-control-research-2026-07-11.md`
- `plans/flow-control-pack-panel-record-2026-07-11.md`
- `plans/flow-coverage-panel-record-2026-07-11.md`
- `04-agent/workflow-recipes.md`
- `04-agent/workflow-engine.md`
- `04-agent/runtime-trust-boundary.md`
- `04-agent/artifact-promotion.md`
