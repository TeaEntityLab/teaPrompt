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

**Type:** Domain-pack skill (script generation). This is not one of the nine frozen core workflow skills and does not change `reflective-dispatch` routing; it is a specialist surface the host harness may invoke directly.

## Purpose

Turn a multi-step agent task into a small, deterministic, host-executable flow-control script. The script owns control flow (order, branching, concurrency, gates, budgets); the model owns step content. This mirrors the 2026 cross-platform consensus (Anthropic workflows-vs-agents, Google ADK workflow agents, OpenAI Agents SDK orchestration, Microsoft Agent Framework graph workflows, LangGraph conditional edges) recorded in `../../plans/agent-flow-control-research-2026-07-11.md`.

## Module Contract

Trigger:

- The user asks to "chain", "pipeline", "fan out", "parallelize", "route", "orchestrate", or "script" agent steps, or asks for a flow/workflow script that calls an agent CLI more than once.
- A task decomposes into ordered or independent agent steps whose sequencing should not be left to model improvisation.
- An existing prompt-only recipe (see `04-agent/workflow-recipes.md`) keeps failing on ordering, skipped gates, or lost intermediate outputs.

Methods:

- Task-shape classification: map the task to the smallest sufficient topology (see Topology Selection).
- Script contract enforcement: every generated script carries config header, state directory, runner abstraction, gates, budget, and logs (see Script Contract).
- Template instantiation: start from the matching template below; delete unused parts before adding anything.
- Stub dry run: verify the script's control flow with a deterministic stub agent before any real run.

Output:

- One runnable script (bash for CLI glue; Python stdlib for bounded concurrency or richer state), plus per-step prompt files, written to the user's chosen location.
- A one-paragraph run note: how to dry-run, how to run, where state and logs land, what the budget caps are.
- Named gates: which deterministic check releases each stage.

Never:

- Never generate a loop that re-invokes an agent until a condition is met — that is `flow-loop-harness` scope; route there.
- Never let the model decide control flow at runtime when the flow is known at generation time; encode it in the script.
- Never treat an agent's self-reported success as a gate; gates are exit codes of deterministic checks.
- Never embed secrets, auto-approve destructive permissions, or widen tool allowlists beyond what the steps need.
- Never claim persistence, crash-safety, or idempotency for a generated script; the state ledger is a resume convention, not a runtime guarantee (`04-agent/runtime-trust-boundary.md`).

Escalation:

- Iterative refinement or fix-until-green loops → `flow-loop-harness`.
- Unclear goal or acceptance criteria → `reflective-brief` first.
- Long-running, resumable, multi-session workflow design → `reflective-spec-plan` with `04-agent/workflow-engine.md`.
- Steps with side effects on credentials, billing, production, data deletion, or third parties → `reflective-risk` before the script is run; insert an explicit human-approval pause step.
- Whether the flow should exist at all (one agent call might do) → `reflective-minimality`.

## Topology Selection

Pick the smallest topology that fits the task shape. Composition is allowed (a pipeline stage may itself fan out), but justify each layer.

| Task shape | Topology | 2026 platform equivalents |
| --- | --- | --- |
| Fixed known stages, each consumes the previous output | Sequential pipeline | Anthropic prompt chaining; ADK `SequentialAgent`; MAF Sequential |
| Independent subtasks, results merged once | Parallel fan-out/fan-in | Anthropic parallelization; ADK `ParallelAgent`; MAF Concurrent; LangGraph Send |
| Input classes need different handling | Conditional router | Anthropic routing; LangGraph conditional edges; OpenAI handoffs |
| Subtasks unknown until a planner sees the task | Orchestrator-workers | Anthropic orchestrator-workers; OpenAI orchestrator-worker; MAF Magentic (manager re-plans) |
| Quality must converge over rounds | Loop | Not here — `flow-loop-harness` |

If no row fits, the task is probably a single agent call. Stop and say so.

## Script Contract

Every generated script must contain, in order:

1. Config header: `AGENT_CMD` (host CLI, overridable), workdir, state dir, budget constants. Default `AGENT_CMD` to the host in use, e.g. `claude -p` (Claude Code headless), `codex exec`, or an SDK entry point.
2. State directory: one file per step output (`state/NN-name.md`), never shell variables for step payloads — files survive interruption and are inspectable.
3. Runner abstraction: a single `run_agent <prompt-file> <out-file>` function; all agent invocations go through it (swap host or stub in one place).
4. Gates: after each stage, a deterministic check (exit code) decides continue/abort. A missing gate must be an explicit `# gate: none (accepted)` comment.
5. Budget: hard caps — max parallel jobs, per-step timeout where the host supports it, total step count.
6. Logs: append one line per step to `state/flow.log` (step, start/end, gate result) for observability.
7. Exit discipline: `set -euo pipefail` (bash) or raised exceptions (Python); non-zero exit on any failed gate; partial state left on disk for resume.

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

run_agent() { $AGENT_CMD "$(cat "$1")" > "$2"; }

pids=()
i=0
for prompt in prompts/fan/*.md; do
  out="$STATE/fan-$(basename "$prompt" .md).md"
  run_agent "$prompt" "$out" &
  pids+=($!)
  i=$((i+1))
  if [ $((i % MAX_JOBS)) -eq 0 ]; then wait; fi      # bounded wave
done
for pid in "${pids[@]}"; do wait "$pid"; done        # fan-in barrier; fails on any failure

ls "$STATE"/fan-*.md >/dev/null                      # gate: every branch produced output
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
LABEL="$(tr -dc 'a-z-' < "$STATE/label.txt")"

case "$LABEL" in                                     # routing is code, not model improvisation
  bug)      route=prompts/route-bug.md ;;
  feature)  route=prompts/route-feature.md ;;
  question) route=prompts/route-question.md ;;
  *) echo "unroutable label: $LABEL" >&2; exit 2 ;;  # fail closed, no default-up
esac
{ cat "$route"; echo; cat "$1"; } > "$STATE/route-prompt.md"
run_agent "$STATE/route-prompt.md" "$STATE/final.md"
```

## Template: Orchestrator-Workers (Python, stdlib only)

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

goal = pathlib.Path(sys.argv[1]).read_text()
plan_raw = run_agent(
    "Decompose into independent worker tasks as a JSON list of "
    '{"id": str, "task": str}. JSON only.\n\n' + goal,
    STATE / "plan.json",
)
tasks = json.loads(plan_raw)
if not (0 < len(tasks) <= MAX_TASKS):               # gate: sane plan size
    sys.exit(f"plan size {len(tasks)} outside 1..{MAX_TASKS}")

def worker(t):
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

1. Stub dry run: `AGENT_CMD='cat'` (bash templates) or a stub echoing canned outputs (router/orchestrator need shaped outputs, e.g. a stub script that prints a fixed label or JSON plan). Control flow, gates, and state files must behave with zero model calls.
2. Syntax check: `bash -n script.sh` or `python3 -m py_compile script.py`.
3. Confirm every stage has a gate or an explicit `# gate: none (accepted)`.
4. Report the dry-run evidence in the completion note; an unexercised script is not done.

## Prompt Sources

- `../../plans/agent-flow-control-research-2026-07-11.md`
- `../../04-agent/workflow-recipes.md`
- `../../04-agent/workflow-engine.md`
- `../../04-agent/runtime-trust-boundary.md`
