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

- Apply the six-part Loop Anatomy, with its labelled template deviations.
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
2. Caps: mandatory `MAX_ITER`; host-provided per-call timeout where available (stock macOS has none) and host-exposed cost caps. Cap exhaustion is not step failure.
3. Ledger: append iteration, verifier result and progress. Fresh agent contexts read its bounded tail, not accumulated chat; append `RESUMED` on restart with a nonempty ledger.
4. Progress detector: abort on equal content signals, not equal churn. Hash staged + unstaged binary diffs (including names/deletions) and untracked contents, excluding STATE. Outside git, disable detection and rely on caps.
5. Permission boundary: human-reviewed least-privilege host flags (e.g. `--allowedTools` / permission mode). Host MUST exclude `checks/`, canonical `state/TASKS.canon` and `prompts/critic-rubric.md` as applicable from agent writes. Comments/copies do not enforce these exclusions.
6. Exits: `0` verified done; `2` cap; `3` no progress or verify-fail stop; `4` missing/non-executable verifier or canonical backlog. Callers must distinguish them.

Selected preflight gate (shared interface): `PREFLIGHT="${PREFLIGHT:-}"` names one executable file, never shell text. Empty preserves ordinary attended behavior and claims no runtime enforcement; a workflow requiring observed host preconditions must set it, and empty never means met. When set, every template checks executability before the first/each agent dispatch — including the zero-call already-converged/already-verified/backlog-empty path — invokes it with no shell (`"$PREFLIGHT"`, per-stage capture under `$STATE/preflight-<stage>.out`; `flow.log` holds one log line per check), and exits 4 before the verifier result is accepted, the final artifact is published, the backlog line is retired, or the satisfied queue retires — including under partial multi-wave policy. Gate output is point-in-time evidence, not enforcement proof; the host owns the gate, manifests, and write exclusions. There is no cancellation manager: killing the driver does not cancel in-flight agent/child processes (driver SIGTERM can leave a stand-in child alive in its own group; examine the process group and stop only coordinator-created groups), and absence of lifecycle evidence is unknown, not kill assurance.

Templates use stdin prompts; choose a stdin-capable host command/wrapper, not argv payloads. Their headers record source/topology/date/dry-run status, task-root cwd and reviewed flag preconditions; put actual reviewed flags in AGENT_CMD, never invent allowlists. Append step start/end and gates to STATE/flow.log.

## Template: Verify-Gated Fix Loop (bash)

```bash
#!/usr/bin/env bash
# generated-by: flow-loop-harness / fix / 2026-10-01 / dry-run-required
set -euo pipefail
AGENT_CMD="${AGENT_CMD:-claude -p}" # reviewed host flags; task-root cwd; protect checks/
PREFLIGHT="${PREFLIGHT:-}" # one executable pathname, not shell text; empty = attended example, never met
VERIFY="${VERIFY:-./checks/verify.sh}"   # truth layer: exit 0 = done
MAX_ITER="${MAX_ITER:-8}"
STATE="${STATE:-./state}"; mkdir -p "$STATE"
LEDGER="$STATE/ledger.md"; touch "$LEDGER"
log() { printf '%s\n' "$*" >> "$STATE/flow.log"; }
preflight() { # $1=stage: selected gate passes, or exit 4 before dispatch/acceptance
  [ -n "$PREFLIGHT" ] || return 0
  [ -x "$PREFLIGHT" ] || { log "preflight gate=4 stage=$1 missing/not-executable"; echo "preflight missing/not executable: $PREFLIGHT" >&2; exit 4; }
  local ec=0
  "$PREFLIGHT" > "$STATE/preflight-$1.out" 2>&1 || ec=$?
  log "preflight gate=$ec stage=$1"
  [ "$ec" -eq 0 ] || exit 4
}

[ -x "$VERIFY" ] || { echo "verifier missing/not executable: $VERIFY" >&2; exit 4; }

check() {  # diagnostics are prompt data, not workspace progress
  local ec=0
  log "verify start"
  "$VERIFY" > "$STATE/verify-out.txt" 2>&1 || ec=$?
  log "verify end gate=$ec"
  return "$ec"
}
snapshot() {  # staged + unstaged diffs and untracked content; never STATE
  git rev-parse --git-dir >/dev/null 2>&1 || return 0
  local root srel
  root="$(git rev-parse --show-toplevel)"
  srel="$(cd "$STATE" && pwd -P)"
  case "$srel" in "$root"/*) srel="${srel#"$root"/}";; *) srel=.git;; esac
  (
    cd "$root"
    git diff --binary --no-ext-diff -- . ":(exclude,literal)$srel"
    git diff --cached --binary --no-ext-diff -- . ":(exclude,literal)$srel"
    git ls-files -z -o --exclude-standard -- . ":(exclude,literal)$srel" |
      while IFS= read -r -d '' f; do
        printf '%s\0' "$f"
        if [ -L "$f" ]; then readlink "$f"; else cksum < "$f"; fi
      done
  ) | cksum
}

if [ -s "$LEDGER" ]; then  # restart: mark the boundary
  echo "- RESUMED $(date -u +%Y-%m-%dT%H:%M:%SZ)" >> "$LEDGER"
fi

if check; then preflight "already-verified-post"; echo "already verified"; exit 0; fi

prev="$(snapshot)"
[ -n "$prev" ] || log "progress disabled: outside git; rely on caps"
for ((i=1; i<=MAX_ITER; i++)); do
  {
    cat prompts/fix.md
    echo; echo "## Ledger tail"; tail -n 20 "$LEDGER"
    echo; echo "## Verifier output"; cat "$STATE/verify-out.txt"
  } > "$STATE/iter-$i-prompt.md"

  preflight "iter-$i-pre"
  log "iter $i start"
  ec=0; $AGENT_CMD < "$STATE/iter-$i-prompt.md" > "$STATE/iter-$i-out.md" || ec=$?
  log "iter $i end agent-exit=$ec"

  if check; then
    preflight "iter-$i-post"
    echo "- iter $i: VERIFIED" >> "$LEDGER"; exit 0
  fi
  cur="$(snapshot)"
  echo "- iter $i: not verified; sig: ${cur:-none}" >> "$LEDGER"
  if [ -n "$cur" ] && [ "$cur" = "$prev" ]; then
    echo "- iter $i: NO PROGRESS, aborting" >> "$LEDGER"; exit 3
  fi
  prev="$cur"
done
echo "- cap $MAX_ITER exhausted" >> "$LEDGER"; exit 2
```

## Template: Evaluator-Optimizer / Writer-Critic (bash)

Deviations: advisory model ACCEPT, no ledger or progress detector; round artifacts are the trail — do not copy into verify-gated loops.

```bash
#!/usr/bin/env bash
# generated-by: flow-loop-harness / writer-critic / 2026-10-01 / dry-run-required
set -euo pipefail
AGENT_CMD="${AGENT_CMD:-claude -p}" # reviewed host flags; task-root cwd; protect checks/ + rubric
PREFLIGHT="${PREFLIGHT:-}" # one executable pathname, not shell text; empty = attended example, never met
MAX_ROUNDS="${MAX_ROUNDS:-4}"
STATE="${STATE:-./state}"; mkdir -p "$STATE"

log() { printf '%s\n' "$*" >> "$STATE/flow.log"; }
preflight() { # $1=stage: selected gate passes, or exit 4 before dispatch/acceptance
  [ -n "$PREFLIGHT" ] || return 0
  [ -x "$PREFLIGHT" ] || { log "preflight gate=4 stage=$1 missing/not-executable"; echo "preflight missing/not executable: $PREFLIGHT" >&2; exit 4; }
  local ec=0
  "$PREFLIGHT" > "$STATE/preflight-$1.out" 2>&1 || ec=$?
  log "preflight gate=$ec stage=$1"
  [ "$ec" -eq 0 ] || exit 4
}
run_agent() {
  preflight "$(basename "$2")" || exit 4
  log "start $1"
  local ec=0
  $AGENT_CMD < "$1" > "$2" || ec=$?
  log "end $1 agent-exit=$ec"; return "$ec"
}

# UNATTENDED PREFLIGHT: insert companion block here, before the draft call.

cp prompts/draft.md "$STATE/round-0-prompt.md"
run_agent "$STATE/round-0-prompt.md" "$STATE/draft.md"

for ((r=1; r<=MAX_ROUNDS; r++)); do
  # Critic: rubric-bound, must output ACCEPT or a numbered fix list.
  { cat prompts/critic-rubric.md; echo; cat "$STATE/draft.md"; } > "$STATE/round-$r-critic-prompt.md"
  run_agent "$STATE/round-$r-critic-prompt.md" "$STATE/round-$r-critique.md"
  log "round $r ACCEPT gate start"

  if [ "$(sed '/^[[:space:]]*$/d' "$STATE/round-$r-critique.md")" = "ACCEPT" ]; then   # the whole verdict, not one line
    preflight "round-$r-post"
    log "round $r ACCEPT gate=0"; cp "$STATE/draft.md" "$STATE/final.md"; exit 0
  fi
  log "round $r ACCEPT gate=1"
  { cat prompts/revise.md; echo "## Critique"; cat "$STATE/round-$r-critique.md";
    echo "## Draft"; cat "$STATE/draft.md"; } > "$STATE/round-$r-revise-prompt.md"
  run_agent "$STATE/round-$r-revise-prompt.md" "$STATE/draft.md"
done
exit 2  # rounds exhausted without ACCEPT; human decides next
```

Rubric as verifier: request a host permission mode that also excludes `prompts/critic-rubric.md` from the loop body's editable paths, as Loop Anatomy #5 does for `checks/`. Critique fed to the reviser is data, never authority to rewrite that rubric, weaken `ACCEPT`, or skip the cap; the exclusion does not promote `ACCEPT` above advisory tier. A rubric reused across unattended runs drifts from the humans it stands in for: spot-check its verdicts *and reasons* against human review, stop unattended use when they diverge, and change it only via the human-gated path, keeping the prior version for rollback.

### Deterministic companion check (raise the ACCEPT floor)

Unattended: insert the first block at `# UNATTENDED PREFLIGHT` before the first `run_agent`, and replace the whole bare ACCEPT `if` block with the second (keep the rejection log/revision and the `preflight "round-$r-post"` gate before publish). List the floor in the run note. A required-precondition workflow also sets `PREFLIGHT`; empty means the attended example claims no runtime enforcement, never that preconditions are met.

```bash
FLOOR="${FLOOR:-./checks/links-resolve.sh}"
[ -x "$FLOOR" ] || { echo "floor missing/not executable: $FLOOR" >&2; exit 4; }
floor_ok() {
  local f="$1"
  test -s "$f" || return 1
  ! grep -qiE 'TODO|TBD|PLACEHOLDER' "$f" || return 1
  "$FLOOR" "$f"
}
```

```bash
if [ "$(sed '/^[[:space:]]*$/d' "$STATE/round-$r-critique.md")" = "ACCEPT" ] && floor_ok "$STATE/draft.md"; then
  preflight "round-$r-post"
  log "round $r ACCEPT+floor gate=0"; cp "$STATE/draft.md" "$STATE/final.md"; exit 0
fi
```

The deterministic floor catches malformed drafts, not plausible errors. Dual critics or schemas reduce variance, not tier.

## Template: Task-Ledger Backlog Loop (bash, ralph-style)

Fail-fast exit 3 on verify failure or unchanged workspace: a green verifier does not prove untouched work; already-satisfied or interrupted tasks halt too — confirm, delete that line from `state/TASKS.canon`, resume (no RESUMED marker). Outside git the change check is disabled. `TASKS.md`: one task per nonempty line.

```bash
#!/usr/bin/env bash
# generated-by: flow-loop-harness / backlog / 2026-10-01 / dry-run-required
set -euo pipefail
AGENT_CMD="${AGENT_CMD:-claude -p}" # reviewed flags; task-root cwd; protect checks/ + TASKS.canon
PREFLIGHT="${PREFLIGHT:-}" # one executable pathname, not shell text; empty = attended example, never met
TASKS_SRC="${TASKS:-TASKS.md}"           # human-owned backlog
VERIFY="${VERIFY:-./checks/verify.sh}"
MAX_ITER="${MAX_ITER:-20}"               # justified: backlogs often exceed ten items
STATE="${STATE:-./state}"; mkdir -p "$STATE"
log() { printf '%s\n' "$*" >> "$STATE/flow.log"; }
preflight() { # $1=stage: selected gate passes, or exit 4 before dispatch/acceptance/retirement
  [ -n "$PREFLIGHT" ] || return 0
  [ -x "$PREFLIGHT" ] || { log "preflight gate=4 stage=$1 missing/not-executable"; echo "preflight missing/not executable: $PREFLIGHT" >&2; exit 4; }
  local ec=0
  "$PREFLIGHT" > "$STATE/preflight-$1.out" 2>&1 || ec=$?
  log "preflight gate=$ec stage=$1"
  [ "$ec" -eq 0 ] || exit 4
}
run_verify() {
  local ec=0
  log "verify start"
  "$VERIFY" > "$STATE/verify-out.txt" 2>&1 || ec=$?
  log "verify end gate=$ec"; return "$ec"
}
# Only the script retires this queue; host write exclusion is REQUIRED.
TASKS="$STATE/TASKS.canon"
[ -f "$TASKS" ] || { [ -f "$TASKS_SRC" ] && cp "$TASKS_SRC" "$TASKS"; } || { echo "canonical backlog missing: $TASKS_SRC" >&2; exit 4; }

[ -x "$VERIFY" ] || { echo "verifier missing/not executable: $VERIFY" >&2; exit 4; }
snap() {  # same content evidence as fix loop; empty outside git
  git rev-parse --git-dir >/dev/null 2>&1 || return 0
  local root srel
  root="$(git rev-parse --show-toplevel)"
  srel="$(cd "$STATE" && pwd -P)"
  case "$srel" in "$root"/*) srel="${srel#"$root"/}";; *) srel=.git;; esac
  (
    cd "$root"
    git diff --binary --no-ext-diff -- . ":(exclude,literal)$srel"
    git diff --cached --binary --no-ext-diff -- . ":(exclude,literal)$srel"
    git ls-files -z -o --exclude-standard -- . ":(exclude,literal)$srel" |
      while IFS= read -r -d '' f; do
        printf '%s\0' "$f"
        if [ -L "$f" ]; then readlink "$f"; else cksum < "$f"; fi
      done
  ) | cksum
}
run_verify || { echo "- preflight: verifier already failing" >> "$STATE/ledger.md"; exit 3; }  # a red start blames no task
[ -n "$(snap)" ] || log "progress disabled: outside git; rely on caps"

for ((i=1; i<=MAX_ITER; i++)); do
  line="$(grep -n -m1 -v '^[[:space:]]*$' "$TASKS" || true)"
  [ -z "$line" ] && { preflight "backlog-empty-post"; echo "backlog empty"; exit 0; }
  num="${line%%:*}"; task="${line#*:}"

  # Fresh context per task.
  before="$(snap)"
  printf 'Complete exactly this one task, then stop: %s\n' "$task" > "$STATE/task-$i-prompt.md"
  preflight "task-$i-pre"
  log "task $i start"
  ec=0; $AGENT_CMD < "$STATE/task-$i-prompt.md" > "$STATE/task-$i-out.md" || ec=$?
  log "task $i end agent-exit=$ec"

  run_verify || { echo "- failed verify: $task (iter $i)" >> "$STATE/ledger.md"; exit 3; }
  [ -z "$before" ] || [ "$(snap)" != "$before" ] || { echo "- no change: $task (iter $i)" >> "$STATE/ledger.md"; exit 3; }
  preflight "task-$i-post"
  # Script, not agent, retires the EXACT line it dispatched.
  sed "${num}d" "$TASKS" > "$TASKS.tmp" && mv "$TASKS.tmp" "$TASKS" || { echo "- canonical backlog missing" >> "$STATE/ledger.md"; exit 4; }
  echo "- done: $task" >> "$STATE/ledger.md"
done
# Last task retired on the final iteration is success, not cap.
[ -f "$TASKS" ] || { echo "- canonical backlog missing" >> "$STATE/ledger.md"; exit 4; }
grep -q '[^[:space:]]' "$TASKS" && { echo "- cap $MAX_ITER exhausted" >> "$STATE/ledger.md"; exit 2; }
preflight "queue-retired-post"
echo "backlog empty"; exit 0
```

## Template: Multi-Wave Fan-out (bash)

For repeated breadth, compose parallel-inside-loop first; use this only when that becomes clumsy.

```bash
#!/usr/bin/env bash
# generated-by: flow-loop-harness / multi-wave / 2026-10-01 / dry-run-required
set -euo pipefail
AGENT_CMD="${AGENT_CMD:-claude -p}" # reviewed host flags; task-root cwd; protect checks/
PREFLIGHT="${PREFLIGHT:-}" # one executable pathname, not shell text; empty = attended example, never met
VERIFY="${VERIFY:-./checks/converged.sh}"  # truth layer: exit 0 = converged
MAX_WAVES="${MAX_WAVES:-4}"                 # cap: distinct exit, not a failure
MAX_JOBS="${MAX_JOBS:-4}"                   # per-wave concurrency budget
STATE="${STATE:-./state}"; mkdir -p "$STATE"
LEDGER="$STATE/ledger.md"; touch "$LEDGER"
log() { printf '%s\n' "$*" >> "$STATE/flow.log"; }
case "$MAX_WAVES" in ""|*[!0-9]*|0) log "max_waves configuration gate=4"; exit 4 ;; esac
case "$MAX_JOBS" in ""|*[!0-9]*|0) log "max_jobs configuration gate=4"; exit 4 ;; esac
preflight() { # $1=stage file stem: selected gate passes, or exit 4 (never a tolerable branch failure)
  [ -n "$PREFLIGHT" ] || return 0
  [ -x "$PREFLIGHT" ] || { log "preflight gate=4 stage=$1 missing/not-executable"; echo "preflight missing/not executable: $PREFLIGHT" >&2; return 4; }
  local ec=0
  "$PREFLIGHT" > "$STATE/preflight-$1.out" 2>&1 || ec=$?
  log "preflight gate=$ec stage=$1"
  [ "$ec" -eq 0 ] || return 4
}
run_agent() {
  local stem
  stem="$(basename "$2" .md)"
  preflight "$stem-pre" || return 4
  log "start $1"
  if $AGENT_CMD < "$1" > "$2" && [ -s "$2" ]; then
    log "end $1 output-gate=0"
  else
    log "end $1 output-gate=1"; rm -f "$2"; return 1
  fi
  preflight "$stem-post" || { rm -f "$2"; return 4; }
}
check() {
  local ec=0
  log "verify start"
  "$VERIFY" > "$STATE/verify-out.txt" 2>&1 || ec=$?
  log "verify end gate=$ec"; return "$ec"
}

[ -x "$VERIFY" ] || { echo "verifier missing/not executable: $VERIFY" >&2; exit 4; }

if [ -s "$LEDGER" ]; then echo "- RESUMED $(date -u +%Y-%m-%dT%H:%M:%SZ)" >> "$LEDGER"; fi
rm -f "$STATE"/w*-*.md "$STATE/summary.md" "$STATE/final.md" # ledger survives; prior run outputs do not

if check; then preflight "already-converged-post"; echo "already converged"; exit 0; fi

prev_summary=""
for ((w=1; w<=MAX_WAVES; w++)); do
  pids=(); i=0; failed=0; preflight_failed=0
  wave_wait() { local p ec; for p in "$@"; do wait "$p" || { ec=$?; [ "$ec" -eq 4 ] && preflight_failed=1; failed=$((failed+1)); }; done; }
  for prompt in prompts/wave/*.md; do
    [ -e "$prompt" ] || { echo "no wave prompts found" >&2; exit 4; }
    out="$STATE/w${w}-$(basename "$prompt" .md).md"
    { cat "$prompt"; echo; echo "## Prior wave summary"; cat "$STATE/summary.md" 2>/dev/null || true; } \
      > "$STATE/w${w}-$(basename "$prompt" .md)-prompt.txt"
    run_agent "$STATE/w${w}-$(basename "$prompt" .md)-prompt.txt" "$out" &
    pids+=($!); i=$((i+1))
    if [ $((i % MAX_JOBS)) -eq 0 ]; then wave_wait "${pids[@]}"; pids=(); fi
  done
  if [ "${#pids[@]}" -gt 0 ]; then wave_wait "${pids[@]}"; fi  # tail barrier; empty array errors under bash 3.2 set -u
  [ "$preflight_failed" -eq 0 ] || { echo "- wave $w: preflight gate=4" >> "$LEDGER"; exit 4; }
  echo "- wave $w: $failed/$i branches failed or empty" >> "$LEDGER"
  [ "$failed" -lt "$i" ] || exit 3

  # Compaction: one bounded summary feeds the next wave.
  { echo "# Wave $w summary"; for f in "$STATE"/w${w}-*.md; do
      echo "## $(basename "$f")"; head -n 40 "$f"; done; } > "$STATE/summary.md"
  summary="$(cat "$STATE"/w${w}-*.md | cksum)"  # branch outputs only; the wave header would hide a stall
  echo "- wave $w: sig ${summary}" >> "$LEDGER"

  if check; then
    preflight "wave-$w-post"
    echo "- wave $w: CONVERGED" >> "$LEDGER"; cp "$STATE/summary.md" "$STATE/final.md"; exit 0
  fi
  if [ "$summary" = "$prev_summary" ]; then                  # progress detector
    echo "- wave $w: NO PROGRESS, aborting" >> "$LEDGER"; exit 3
  fi
  prev_summary="$summary"
done
echo "- cap $MAX_WAVES waves exhausted" >> "$LEDGER"; exit 2
```

Do not add a memory backend or semantic ledger columns — `state/` stays
disposable per run (`plans/flow-coverage-panel-record-2026-07-11.md` §Rejected).

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
