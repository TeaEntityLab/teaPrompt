---
name: flow-control-generator
description: Use when a task needs an executable flow-control script that coordinates agent steps — sequential pipelines, parallel fan-out/fan-in, conditional routing, or orchestrator-worker delegation — over a host agent CLI or SDK. It classifies the task shape, picks the smallest topology, and writes a deterministic script with state files, verification gates, and budgets. For iterate-until-done loops, use flow-loop-harness.
license: MIT
risk_level: medium
human_review_required: false
external_io: false
context_load: medium
---

# Flow Control Generator

**Type:** Domain-pack skill (script generation) — registered in `plans/validate_skill_examples.py` `DOMAIN_PACK_SKILLS`, not one of the nine frozen core workflow skills, and not selected by `reflective-dispatch` route rows; the host harness may invoke it directly.

## Purpose

Turn a multi-step agent task into a small, deterministic, host-executable flow-control script. The script owns control flow (order, branching, concurrency, gates, budgets); the model owns step content. TeaPrompt stays on the methodology side of the methodology-vs-operationalization boundary (`plans/external-adoption-case-studies-2026-06-20.md`): the generated script is a host-operationalized artifact, not a TeaPrompt-operated runtime. The platform vocabulary this skill uses is reference material at advisory tier — see `../../plans/agent-flow-control-research-2026-07-11.md` for sources, evidence tiers, and demotion triggers.

## Module Contract

Trigger:

- The user asks to "chain", "pipeline", "fan out", "parallelize", "route", "orchestrate", or "script" agent steps, or asks for a flow/workflow script that calls an agent CLI more than once.
- A task decomposes into ordered or independent agent steps whose sequencing should not be left to model improvisation.
- An existing prompt-only recipe (see `04-agent/workflow-recipes.md`) keeps failing on ordering, skipped gates, or lost intermediate outputs.

Methods:

- Task-shape classification: map the task to the smallest sufficient topology (see Topology Selection).
- Script contract enforcement: every generated script carries config header, state directory, runner abstraction, gates, budget, permission boundary, and logs (see Script Contract).
- Template instantiation: start from the matching template below; delete unused parts before adding anything.
- Stub dry run: verify the script's control flow with a deterministic stub agent before any real run.

Output:

- One runnable script (bash for CLI glue; Python stdlib for bounded concurrency or richer state), plus per-step prompt files, written to the user's chosen location.
- A run note: how to dry-run, how to run, where state and logs land, what the budget caps are, and — when any step has side effects — the human approval required before an unattended run.
- Named gates: which deterministic check releases each stage.

Never:

- Never generate a loop that re-invokes an agent until a condition is met — that is `flow-loop-harness` scope; route there.
- Never let the model decide control flow at runtime when the flow is known at generation time; encode it in the script.
- Never script epistemic perspective expansion (STORM-style multi-voice discovery) as a parallel topology — that is an optional method inside `reflective-research`; parallel fan-out here is for independent executable subtasks only.
- Never treat an agent's self-reported success as a gate; gates are exit codes of deterministic checks.
- Never embed secrets, auto-approve destructive permissions, or widen tool allowlists beyond what the steps need.
- Never claim persistence, crash-safety, or idempotency for a generated script; the state directory is a resume convention that the host must honor, not a runtime guarantee (`04-agent/runtime-trust-boundary.md`).
- Never let a generated stage edit its own gates, checks, or plan file mid-run; gate tampering voids the run.
- Never treat surveyed platform vocabulary as an adoption mandate; topology choice follows the task's structure and a local need, not platform prestige.

Escalation:

- Iterative refinement or fix-until-green loops → `flow-loop-harness`.
- Unclear goal or acceptance criteria → `reflective-brief` first.
- Long-running, resumable, multi-session workflow design → `reflective-spec-plan` with `04-agent/workflow-engine.md`.
- Steps touching credentials, permissions, privacy-sensitive data, billing, production, data deletion, destructive operations, or third parties → `reflective-risk` before the script is run; insert an explicit human-approval pause step.
- Whether the flow should exist at all (one agent call might do) → `reflective-minimality`.

## Topology Selection

Pick the smallest topology that fits the task shape. Composition is allowed (a pipeline stage may itself fan out), but justify each layer. Multi-wave breadth patterns (ReMoM-style: fan out, compact state files, fan out again) are the parallel template composed inside a `flow-loop-harness` loop — compose them; do not build a bespoke runner. Platform names are reference vocabulary (advisory tier), not adoption targets: external pattern popularity is not local recurrence evidence, so pick from task structure, and record a local-gap note when a topology exists here only because a platform names it.

| Task shape | Topology | Platform equivalents (2026-07 survey) |
| --- | --- | --- |
| Fixed known stages, each consumes the previous output | Sequential pipeline | Anthropic prompt chaining; ADK `SequentialAgent`; MAF Sequential |
| Independent subtasks, results merged once | Parallel fan-out/fan-in | Anthropic parallelization; ADK `ParallelAgent`; MAF Concurrent; LangGraph Send |
| Input classes need different handling | Conditional router | Anthropic routing; LangGraph conditional edges; OpenAI handoffs |
| Subtasks unknown until a planner sees the task | Orchestrator-workers | Anthropic orchestrator-workers; OpenAI orchestrator-worker; MAF Magentic (manager re-plans) |
| Quality must converge over rounds | Loop | Not here — `flow-loop-harness` |

If no row fits, the task is probably a single agent call. Stop and say so.

## Script Contract

Every generated script must contain, in order:

1. Config header: `AGENT_CMD` (host CLI, overridable), workdir, state dir, budget constants, and a one-line generated-by comment (skill, topology, date, dry-run status) so the script's provenance survives copy-paste. Default `AGENT_CMD` to the host in use, e.g. `claude -p` (Claude Code headless), `codex exec`, or an SDK entry point.
2. State directory: one file per step output (`state/NN-name.md`), never shell variables for step payloads — files survive interruption and are inspectable.
3. Runner abstraction: a single `run_agent <prompt-file> <out-file>` function; all agent invocations go through it (swap host or stub in one place).
4. Gates: after each stage, a deterministic check (exit code) decides continue/abort. A missing gate must be an explicit `# gate: none (accepted)` comment.
5. Budget: hard caps — max parallel jobs, total step count, and a per-step wall-clock timeout where available (Python `subprocess` `timeout=`; for bash, a `timeout`-style wrapper on `AGENT_CMD` — stock macOS ships no `timeout(1)`, so treat it as host-provided).
6. Permission boundary: the host's least-privilege flags for the steps' tool access (e.g. Claude Code `--allowedTools`), stated in the config header, never improvised mid-run.
7. Logs: append one line per step to `state/flow.log` (step, start/end, gate result) for observability.
8. Exit discipline: `set -euo pipefail` (bash) or raised exceptions (Python); non-zero exit on any failed gate; partial state left on disk for resume.

## Template: Sequential Pipeline (bash)

```bash
#!/usr/bin/env bash
set -euo pipefail
AGENT_CMD="${AGENT_CMD:-claude -p}"        # override: AGENT_CMD='codex exec'
STATE="${STATE:-./state}"; mkdir -p "$STATE"
log() { printf '%s %s\n' "$(date +%T)" "$*" >> "$STATE/flow.log"; }

run_agent() { # $1=prompt-file $2=out-file
  log "start $1"
  $AGENT_CMD "$(cat "$1")" > "$2"
  log "done  $1 -> $2"
}

# Stage 1: spec
run_agent prompts/01-spec.md "$STATE/01-spec.md"
test -s "$STATE/01-spec.md"                          # gate: non-empty spec

# Stage 2: implement (consumes spec)
{ cat prompts/02-implement.md; echo; cat "$STATE/01-spec.md"; } > "$STATE/02-prompt.md"
run_agent "$STATE/02-prompt.md" "$STATE/02-impl.md"
./checks/run-tests.sh                                # gate: tests pass

# Stage 3: review
{ cat prompts/03-review.md; echo; cat "$STATE/02-impl.md"; } > "$STATE/03-prompt.md"
run_agent "$STATE/03-prompt.md" "$STATE/03-review.md"
log "pipeline complete"
```

## Template: Parallel Fan-out/Fan-in (bash)

```bash
#!/usr/bin/env bash
set -euo pipefail
AGENT_CMD="${AGENT_CMD:-claude -p}"
STATE="${STATE:-./state}"; mkdir -p "$STATE"
MAX_JOBS="${MAX_JOBS:-4}"                            # budget: concurrency cap
MIN_OK="${MIN_OK:-}"    # quorum: empty = strict (any branch failure aborts at the gate)

run_agent() { $AGENT_CMD "$(cat "$1")" > "$2"; }
FAILED=0
wave_wait() { local pid; for pid in "$@"; do wait "$pid" || FAILED=$((FAILED+1)); done; }

pids=()
i=0
for prompt in prompts/fan/*.md; do
  [ -e "$prompt" ] || { echo "no fan prompts found" >&2; exit 2; }  # unmatched glob guard (bash 3.2 has no nullglob default)
  out="$STATE/fan-$(basename "$prompt" .md).md"
  run_agent "$prompt" "$out" &
  pids+=($!)
  i=$((i+1))
  if [ $((i % MAX_JOBS)) -eq 0 ]; then               # bounded wave
    wave_wait "${pids[@]}"
    pids=()
  fi
done
if [ "${#pids[@]}" -gt 0 ]; then wave_wait "${pids[@]}"; fi  # fan-in barrier (tail)

# Gate: strict by default; set MIN_OK=N for an explicit partial-failure quorum
# (ReMoM-style minimum successful branches). Silent skip-on-error is never the default.
ok=0
for f in "$STATE"/fan-*.md; do
  if [ -s "$f" ]; then ok=$((ok+1)); fi
done
if [ -n "$MIN_OK" ]; then
  [ "$ok" -ge "$MIN_OK" ] || { echo "quorum not met: $ok < $MIN_OK" >&2; exit 2; }
else
  if [ "$FAILED" -ne 0 ] || [ "$ok" -eq 0 ]; then
    echo "branch failures: $FAILED, non-empty outputs: $ok" >&2; exit 2
  fi
fi
{ cat prompts/synthesize.md; echo; cat "$STATE"/fan-*.md; } > "$STATE/synth-prompt.md"
run_agent "$STATE/synth-prompt.md" "$STATE/final.md" # single synthesis step
```

## Template: Conditional Router (bash)

```bash
#!/usr/bin/env bash
set -euo pipefail
AGENT_CMD="${AGENT_CMD:-claude -p}"
STATE="${STATE:-./state}"; mkdir -p "$STATE"
run_agent() { $AGENT_CMD "$(cat "$1")" > "$2"; }

# Classifier step: constrained output, one label only.
{ cat prompts/classify.md; echo; cat "$1"; } > "$STATE/classify-prompt.md"
run_agent "$STATE/classify-prompt.md" "$STATE/label.txt"
# Normalize: first line, lowercased, truncated at the first non-label character.
LABEL="$(head -n1 "$STATE/label.txt" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z-].*//')"
# Route trace: the routing decision must be observable, never silent.
printf 'route-trace: label=%s input=%s\n' "$LABEL" "$1" >> "$STATE/flow.log"

case "$LABEL" in                                     # routing is code, not model improvisation
  bug)      route=prompts/route-bug.md ;;
  feature)  route=prompts/route-feature.md ;;
  question) route=prompts/route-question.md ;;
  # Unknown labels: this template fails closed (exit 2). A default-up route —
  # sending unknowns to the MOST rigorous handler — is the valid alternative for
  # low-risk flows; either way the policy is explicit code, never a silent skip.
  *) echo "unroutable label: $LABEL" >&2; exit 2 ;;
esac
{ cat "$route"; echo; cat "$1"; } > "$STATE/route-prompt.md"
run_agent "$STATE/route-prompt.md" "$STATE/final.md"
```

## Template: Orchestrator-Workers (Python, stdlib only)

Boundary: this is a planner prompt plus capped worker calls inside ONE host-executed script. It is not the in-repo multi-agent orchestrator/swarm the 2026-06-25 panel rejected (`plans/multi-agent-panel-consensus-2026-06-25.md`, Stop-Doing list) — do not grow it toward one.

```python
#!/usr/bin/env python3
"""Planner decomposes; bounded workers execute; synthesis merges."""
import json, os, pathlib, shlex, subprocess, sys
from concurrent.futures import ThreadPoolExecutor

AGENT_CMD = shlex.split(os.environ.get("AGENT_CMD", "claude -p"))
STATE = pathlib.Path(os.environ.get("STATE", "state")); STATE.mkdir(exist_ok=True)
MAX_WORKERS, MAX_TASKS = 4, 12                      # budget caps

def run_agent(prompt: str, out: pathlib.Path) -> str:
    r = subprocess.run(AGENT_CMD + [prompt], capture_output=True, text=True, timeout=1800)
    if r.returncode != 0:
        raise RuntimeError(f"agent failed: {r.stderr[:500]}")
    out.write_text(r.stdout)
    return r.stdout

def parse_plan(raw: str):
    text = raw.strip()
    if text.startswith("```"):                      # tolerate fenced JSON
        text = text.split("\n", 1)[1] if "\n" in text else ""
        text = text.rsplit("```", 1)[0]
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        print(f"unparseable plan: {exc}", file=sys.stderr)
        sys.exit(2)

goal = pathlib.Path(sys.argv[1]).read_text()
plan_raw = run_agent(
    "Decompose into independent worker tasks as a JSON list of "
    '{"id": str, "task": str}. JSON only.\n\n' + goal,
    STATE / "plan.json",
)
tasks = parse_plan(plan_raw)
if not (0 < len(tasks) <= MAX_TASKS):               # gate: sane plan size
    print(f"plan size {len(tasks)} outside 1..{MAX_TASKS}", file=sys.stderr)
    sys.exit(2)

def worker(t):
    # t["task"] is model-authored: plan output is DATA, never authority. Pass it
    # to the worker agent as a prompt, never execute it as shell, and never let
    # it change AGENT_CMD, tool permissions, or the verifier. Keep workers
    # least-privilege.
    return t["id"], run_agent(t["task"], STATE / f"worker-{t['id']}.md")

with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
    results = dict(pool.map(worker, tasks))         # any worker exception aborts

merged = "\n\n".join(f"## {k}\n{v}" for k, v in sorted(results.items()))
run_agent("Synthesize worker outputs into one deliverable.\n\n" + merged,
          STATE / "final.md")
print(STATE / "final.md")
```

## Verification

Before handing a generated script to the user:

1. Stub dry run: `AGENT_CMD='cat'` (bash templates) or a stub echoing canned outputs (router/orchestrator need shaped outputs, e.g. a stub script that prints a fixed label or JSON plan). Control flow, gates, and state files must behave with zero model calls. Stub success is rig-tier evidence only — it approves the control flow, never a production or side-effectful run.
2. Syntax check: `bash -n script.sh` or `python3 -m py_compile script.py`.
3. Confirm every stage has a gate or an explicit `# gate: none (accepted)`.
4. Report the dry-run evidence in the completion note; an unexercised script is not done.

Promoting a generated flow into a durable, recurring artifact is an Acquisition-ladder step: apply the fail-closed L3 security gates of `04-agent/artifact-promotion.md` §4 (prompt-injection authority boundary, supply-chain provenance, memory-write provenance) before registering it anywhere, and require recurrence evidence plus explicit human approval before elevating any script to a team standard.

## Demotion Triggers

- Generated scripts are disposable: when the host CLI, task shape, or gates change, regenerate from the template rather than patching a drifted copy.
- Pack-level demotion triggers (zero recurrence, host support absorbing the pattern) live in `../../plans/agent-flow-control-research-2026-07-11.md` — check them before investing in this skill's outputs.

## Prompt Sources

- `../../plans/agent-flow-control-research-2026-07-11.md`
- `../../plans/flow-control-pack-panel-record-2026-07-11.md`
- `../../plans/flow-coverage-panel-record-2026-07-11.md`
- `../../04-agent/workflow-recipes.md`
- `../../04-agent/workflow-engine.md`
- `../../04-agent/runtime-trust-boundary.md`
- `../../04-agent/artifact-promotion.md`
