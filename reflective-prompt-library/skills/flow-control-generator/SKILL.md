---
name: flow-control-generator
description: Use when a task needs an executable flow-control script that coordinates agent steps — sequential pipelines, parallel fan-out/fan-in, conditional routing, or orchestrator-worker delegation — over a host agent CLI or SDK. It classifies the task shape, picks the smallest topology, and writes a deterministic script with state files, verification gates, and budgets. For iterate-until-done loops, use flow-loop-harness.
license: MIT
compatibility: Requires a POSIX host with bash 3.2+ (python3 for the Python templates) and a headless host agent CLI; generated scripts run on the host, not in TeaPrompt.
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
- Template instantiation: start from the matching template below; delete unused parts before adding anything.
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

1. Config: `AGENT_CMD` (reviewed host CLI/wrapper, flags and stdin/file support), workdir, `STATE`, caps, and generated-by skill/topology/date/dry-run status.
2. State: one output file per step, not shell-variable payloads; inspectable partial files support a host-honored resume convention.
3. Runner: all calls go through `run_agent`; prompt content via stdin, never argv.
4. Gates: deterministic exit codes release stages; absent checks say `# gate: none (accepted)`. For fan-in, the gate runs over the merged result as well as the branch tally: branches that each pass can conflict when combined.
5. Budget: cap concurrency and total steps; per-call timeout/cost caps where supported. When a stage is itself a loop or retries, the composition's worst case is the product of the caps: declare one total budget (steps or wall-clock) that every level decrements, and have the outer script pass its remaining budget to the inner one. Stock macOS has no `timeout`; a bash timeout wrapper is host-provided.
6. Permissions: record least-privilege host flags in `AGENT_CMD`; review them and host write-exclusions before unattended use. Defaults are attended examples, not approval.
7. Logs: `STATE/flow.log` records step start/end and gate results; workdir is the reviewed task root.
8. Exits: bash `set -euo pipefail` or Python exceptions; failed gates exit nonzero and retain partial state.

## Template: Sequential Pipeline (bash)

```bash
#!/usr/bin/env bash
# generated-by: flow-control-generator / pipeline / 2026-10-01 / dry-run-required
set -euo pipefail
AGENT_CMD="${AGENT_CMD:-claude -p}" # reviewed host flags; workdir=task root; protect checks/
STATE="${STATE:-./state}"; mkdir -p "$STATE"
log() { printf '%s\n' "$*" >> "$STATE/flow.log"; }
run_agent() {
  log "start $1"
  local ec=0
  $AGENT_CMD < "$1" > "$2" || ec=$?
  log "end $1 exit=$ec"; return "$ec"
}
run_agent prompts/01-spec.md "$STATE/01-spec.md"
if test -s "$STATE/01-spec.md"; then log "spec gate=0"; else log "spec gate=2"; exit 2; fi
{ cat prompts/02-implement.md; echo; cat "$STATE/01-spec.md"; } > "$STATE/02-prompt.md"
run_agent "$STATE/02-prompt.md" "$STATE/02-impl.md"
ec=0; ./checks/run-tests.sh || ec=$?
log "tests gate=$ec"; [ "$ec" -eq 0 ] || exit "$ec"
{ cat prompts/03-review.md; echo; cat "$STATE/02-impl.md"; } > "$STATE/03-prompt.md"
run_agent "$STATE/03-prompt.md" "$STATE/03-review.md"
# gate: none (accepted)
log "review gate=none accepted; pipeline complete"
```

## Template: Parallel Fan-out/Fan-in (bash)

```bash
#!/usr/bin/env bash
# generated-by: flow-control-generator / parallel / 2026-10-01 / dry-run-required
set -euo pipefail
AGENT_CMD="${AGENT_CMD:-claude -p}" # reviewed host flags; workdir=task root; protect checks/
STATE="${STATE:-./state}"; mkdir -p "$STATE"
MAX_JOBS="${MAX_JOBS:-4}"
MIN_OK="${MIN_OK:-}" # empty=strict; otherwise explicit partial-failure quorum
log() { printf '%s\n' "$*" >> "$STATE/flow.log"; }
run_agent() {
  log "start $1"
  if $AGENT_CMD < "$1" > "$2" && [ -s "$2" ]; then
    log "end $1 output-gate=0"
  else
    log "end $1 output-gate=1"; rm -f "$2"; return 1
  fi
}
FAILED=0
wave_wait() { local pid; for pid in "$@"; do wait "$pid" || FAILED=$((FAILED+1)); done; }
rm -f "$STATE"/fan-*.md
pids=(); i=0
for prompt in prompts/fan/*.md; do
  [ -e "$prompt" ] || { log "branch gate=2 no prompts"; exit 2; }
  out="$STATE/fan-$(basename "$prompt" .md).md"
  run_agent "$prompt" "$out" &
  pids+=($!); i=$((i+1))
  if [ $((i % MAX_JOBS)) -eq 0 ]; then wave_wait "${pids[@]}"; pids=(); fi
done
if [ "${#pids[@]}" -gt 0 ]; then wave_wait "${pids[@]}"; fi
ok=0
for f in "$STATE"/fan-*.md; do [ ! -s "$f" ] || ok=$((ok+1)); done
if [ -n "$MIN_OK" ]; then
  [ "$ok" -ge "$MIN_OK" ] || { log "quorum gate=2 $ok < $MIN_OK"; exit 2; }
elif [ "$FAILED" -ne 0 ] || [ "$ok" -eq 0 ]; then
  log "branch gate=2 failed=$FAILED successful=$ok"; exit 2
fi
log "branch gate=0 successful=$ok"
{ cat prompts/synthesize.md; echo; cat "$STATE"/fan-*.md; } > "$STATE/synth-prompt.md"
run_agent "$STATE/synth-prompt.md" "$STATE/final.md"
ec=0; ./checks/verify-merged.sh "$STATE/final.md" || ec=$?    # gate: merged result, not only the branch tally
log "merged gate=$ec"; exit "$ec"
```

## Template: Conditional Router (bash)

```bash
#!/usr/bin/env bash
# generated-by: flow-control-generator / router / 2026-10-01 / dry-run-required
set -euo pipefail
AGENT_CMD="${AGENT_CMD:-claude -p}" # reviewed host flags; workdir=task root; protect prompts/
STATE="${STATE:-./state}"; mkdir -p "$STATE"
log() { printf '%s\n' "$*" >> "$STATE/flow.log"; }
run_agent() {
  log "start $1"
  local ec=0
  $AGENT_CMD < "$1" > "$2" || ec=$?
  log "end $1 exit=$ec"; return "$ec"
}
{ cat prompts/classify.md; echo; cat "$1"; } > "$STATE/classify-prompt.md"
run_agent "$STATE/classify-prompt.md" "$STATE/label.txt"
# Preserve raw bytes; accept a whole case-insensitive label and at most one LF.
RAW_LABEL="$(cat "$STATE/label.txt"; printf '.')"; RAW_LABEL="${RAW_LABEL%.}"
LABEL="$(printf '%s' "$RAW_LABEL" | tr '[:upper:]' '[:lower:]'; printf '.')"
LABEL="${LABEL%.}"; LABEL="${LABEL%$'\n'}"
printf 'route-trace: raw=%q label=%q input=%q\n' "$RAW_LABEL" "$LABEL" "$1" >> "$STATE/flow.log"
case "$LABEL" in
  bug) route=prompts/route-bug.md ;;
  feature) route=prompts/route-feature.md ;;
  question) route=prompts/route-question.md ;;
  # Unknown labels fail closed (exit 2). For low-risk flows a default-up route to
  # the most rigorous handler is the alternative; either way policy is explicit.
  *) log "route gate=2"; echo "unroutable label: $LABEL" >&2; exit 2 ;;
esac
log "route gate=0"
{ cat "$route"; echo; cat "$1"; } > "$STATE/route-prompt.md"
run_agent "$STATE/route-prompt.md" "$STATE/final.md"
# gate: none (accepted)
log "handler gate=none accepted"
```

## Template: Orchestrator-Workers (Python, stdlib only)

Boundary: a planner prompt plus capped worker calls inside ONE host-executed script — not the multi-agent orchestrator/swarm the 2026-06-25 panel rejected (`plans/multi-agent-panel-consensus-2026-06-25.md`); do not grow it toward one.

```python
#!/usr/bin/env python3
"""Planner, capped workers, synthesis.
generated-by: flow-control-generator / orchestrator / 2026-10-01 / dry-run-required
"""
import json, os, pathlib, shlex, subprocess, sys
from concurrent.futures import ThreadPoolExecutor

AGENT_CMD = shlex.split(os.environ.get("AGENT_CMD", "claude -p")) # reviewed flags; task-root cwd; protect checks/
STATE = pathlib.Path(os.environ.get("STATE", "state")); STATE.mkdir(parents=True, exist_ok=True)
MAX_WORKERS, MAX_TASKS = 4, 12
def log(line):
    with (STATE / "flow.log").open("a") as f: f.write(line + "\n")

def run_agent(prompt: str, out: pathlib.Path) -> str:
    log(f"{out.name} start")
    r = subprocess.run(AGENT_CMD, input=prompt, capture_output=True, text=True, timeout=1800)
    passed = r.returncode == 0 and bool(r.stdout.strip())
    log(f"{out.name} end exit={r.returncode} output-gate={int(not passed)}")
    if r.returncode: raise RuntimeError(f"agent failed: {r.stderr[:500]}")
    if not passed: raise RuntimeError("agent returned no output")
    out.write_text(r.stdout)
    return r.stdout

def parse_plan(raw: str):
    text = raw.strip()
    if text.startswith("```"):                      # tolerate fenced JSON, incl. ```json
        lines = text.splitlines()[1:]
        if lines and lines[-1].strip() == "```": lines = lines[:-1]
        text = "\n".join(lines)
    try:
        tasks = json.loads(text)
        if not isinstance(tasks, list): raise ValueError("plan is not a list")
        return tasks
    except (json.JSONDecodeError, ValueError) as exc:
        log("plan gate=2")
        print(f"unparseable plan: {exc}", file=sys.stderr)
        sys.exit(2)

goal = pathlib.Path(sys.argv[1]).read_text()
plan_raw = run_agent(
    "Decompose into independent worker tasks as a JSON list of "
    '{"id": str, "task": str}. JSON only.\n\n' + goal,
    STATE / "plan.json",
)
tasks = parse_plan(plan_raw)
if not (0 < len(tasks) <= MAX_TASKS):
    log("plan gate=2")
    print(f"plan size {len(tasks)} outside 1..{MAX_TASKS}", file=sys.stderr); sys.exit(2)
ids = set()
for t in tasks: # validate the entire plan before any worker starts
    if not isinstance(t, dict) or any(not isinstance(t.get(k), str) or not t[k].strip() for k in ("id", "task")):
        log("plan gate=2")
        print("invalid task: nonempty string id/task required", file=sys.stderr); sys.exit(2)
    wid = "".join(c for c in t["id"] if c.isalnum() or c in "-_")
    key = wid.casefold()  # case-insensitive filesystems make A and a collide
    if not wid or key in ids:
        log("plan gate=2")
        print(f"empty or duplicate effective worker id: {wid!r}", file=sys.stderr); sys.exit(2)
    ids.add(key); t["id"] = wid
log("plan gate=0")
def worker(t):
    # Task text is data, never shell code or authority to change gates/permissions.
    return t["id"], run_agent(t["task"], STATE / f"worker-{t['id']}.md")

with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
    results = dict(pool.map(worker, tasks))

merged = "\n\n".join(f"## {k}\n{v}" for k, v in sorted(results.items()))
run_agent("Synthesize worker outputs into one deliverable.\n\n" + merged,
          STATE / "final.md")
ec = subprocess.run(["./checks/verify-merged.sh", str(STATE / "final.md")]).returncode
log(f"merged gate={ec}")
if ec: sys.exit(2)
print(STATE / "final.md")
```

## Template: DAG Executor (Python, stdlib only)

Use only when dependency-gated fan-out exceeds pipeline, parallel, or orchestrator
expression; prefer a host primitive such as `/batch` when it solves the task.

```python
#!/usr/bin/env python3
"""DAG: bounded concurrency and dependency gates.
generated-by: flow-control-generator / dag / 2026-10-01 / dry-run-required
"""
import os, pathlib, shlex, subprocess, sys
from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED

AGENT_CMD = shlex.split(os.environ.get("AGENT_CMD", "claude -p")) # reviewed flags; task-root cwd; protect checks/
STATE = pathlib.Path(os.environ.get("STATE", "state")); STATE.mkdir(parents=True, exist_ok=True)
MAX_WORKERS = int(os.environ.get("MAX_WORKERS", "4"))
MIN_OK = os.environ.get("MIN_OK", "")
FINAL_NODE = "assemble" # explicit acceptance artifact, independent of traversal order
NODES = {
    "spec":     ((), "prompts/spec.md"),
    "api":      (("spec",), "prompts/api.md"),
    "client":   (("spec",), "prompts/client.md"),
    "assemble": (("api", "client"), "prompts/assemble.md"),
}
def log(line):
    with (STATE / "flow.log").open("a") as f: f.write(line + "\n")

def toposort(nodes):
    order, seen, temp = [], set(), set()
    def visit(n):
        if n in seen: return
        if n in temp: sys.exit(4) # cycle
        temp.add(n)
        for d in nodes[n][0]:
            if d not in nodes: sys.exit(4) # dangling dependency
            visit(d)
        temp.discard(n); seen.add(n); order.append(n)
    for n in nodes: visit(n)
    return order

def run_agent(prompt_file, out, deps=()):
    body = pathlib.Path(prompt_file).read_text()
    for d in deps:
        body += "\n\n" + (STATE / f"{d}.out").read_text()
    log(f"{out.name} start")
    r = subprocess.run(AGENT_CMD, input=body, capture_output=True, text=True, timeout=1800)
    passed = r.returncode == 0 and bool(r.stdout.strip())
    log(f"{out.name} end exit={r.returncode} output-gate={int(not passed)}")
    if r.returncode: raise RuntimeError(f"agent failed: {r.stderr[:500]}")
    if not passed: raise RuntimeError("agent returned no output")
    out.write_text(r.stdout)

order = toposort(NODES)
if FINAL_NODE not in NODES or any(FINAL_NODE in deps for deps, _ in NODES.values()):
    print("final node missing or nonterminal", file=sys.stderr); sys.exit(4)
status = {} # done|failed|blocked
ledger = (STATE / "dag-ledger.tsv").open("w")

def ready(n):
    return all(status.get(d) == "done" for d in NODES[n][0])

remaining = list(order)
with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
    running = {}
    while remaining or running:
        for n in [n for n in remaining if ready(n) and len(running) < MAX_WORKERS]:
            remaining.remove(n)
            running[pool.submit(run_agent, NODES[n][1], STATE / f"{n}.out", NODES[n][0])] = n
        if not running:
            for n in remaining: status[n] = "blocked"
            break
        done, _ = wait(running, return_when=FIRST_COMPLETED)
        for fut in done:
            n = running.pop(fut)
            try:
                fut.result(); status[n] = "done"
            except Exception as exc:
                status[n] = "failed"
                print(f"{n} failed: {exc}", file=sys.stderr)
            ledger.write(f"{n}\t{status[n]}\n")

ledger.close()
ok = sum(1 for v in status.values() if v == "done")
bad = [n for n, v in status.items() if v != "done"]
if status.get(FINAL_NODE) != "done" or (ok < int(MIN_OK) if MIN_OK else bool(bad)):
    log("nodes gate=2"); sys.exit(2)
final = STATE / f"{FINAL_NODE}.out"
ec = subprocess.run(["./checks/verify-merged.sh", str(final)]).returncode
log(f"merged gate={ec}")
sys.exit(2 if ec else 0)
```

One host-executed script, not a runtime; retry-with-backoff, memory backend and per-node provenance headers stay rejected.

## Human Review Boundary

Before the first unattended run of any generated script with side effects, a human must approve gates, caps, permission flags, blast radius, and every auth/permission/destructive/billing/production/privacy/migration/API/third-party step. Record the approval in the run note. Attended runs may review only gates and caps; side-effectful steps still need a per-action pause.

## Verification

Before handing a generated script to the user:

1. Stub dry run: `AGENT_CMD='cat'`, or a stub echoing shaped outputs (router: fixed label; orchestrator: JSON plan); control flow, gates, and state files must behave with zero model calls. Stub success is rig-tier evidence for control flow, never for a production or side-effectful run.
2. `bash -n` / `python3 -m py_compile` the script.
3. Confirm every stage has a gate or an explicit `# gate: none (accepted)`.
4. Report the dry-run evidence in the run note; an unexercised script is not done.

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
