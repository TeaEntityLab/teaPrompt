# `flow-loop-harness` Templates

Portable sibling to `SKILL.md` in this directory; this file carries the moved loop template sections byte-for-byte, not a second copy. Read `SKILL.md` for the Module Contract, Loop Anatomy, Human Review Boundary, Verification, Demotion Triggers and provenance; those rules govern every body here. Templates are host-executable starts: instantiate the matching one, delete unused parts before adding anything, and prove control flow with a stub agent before real use.

## Template: Verify-Gated Fix Loop (bash)

```bash
#!/usr/bin/env bash
# generated-by: flow-loop-harness / fix / 2026-10-01 / dry-run-required
set -euo pipefail
AGENT_CMD="${AGENT_CMD-claude -p}" # reviewed host flags; task-root cwd; protect checks/; unset-only default
PREFLIGHT="${PREFLIGHT:-}" # one executable pathname, not shell text; empty = attended example, never met
VERIFY="${VERIFY:-./checks/verify.sh}"   # truth layer: exit 0 = done
MAX_ITER="${MAX_ITER-8}"
STATE="${STATE:-./state}"; mkdir -p "$STATE"
LEDGER="$STATE/ledger.md"; touch "$LEDGER"
log() { printf '%s\n' "$*" >> "$STATE/flow.log"; }
case "${AGENT_CMD//[[:space:]]/}" in "") log "agent_cmd configuration gate=4"; echo "agent_cmd configuration gate=4: empty AGENT_CMD" >&2; exit 4 ;; esac
case "$MAX_ITER" in ""|0|0*|*[!0-9]*) log "max_iter configuration gate=4: $MAX_ITER"; echo "max_iter configuration gate=4: $MAX_ITER" >&2; exit 4 ;; esac
MAX_ITER_LEN="${#MAX_ITER}"
if [ "$MAX_ITER_LEN" -gt 10 ] || { [ "$MAX_ITER_LEN" -eq 10 ] && [ "$MAX_ITER" \> 2147483647 ]; }; then log "max_iter configuration gate=4: $MAX_ITER"; echo "max_iter configuration gate=4: $MAX_ITER" >&2; exit 4; fi
unset MAX_ITER_LEN
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
  if [ "$ec" -eq 4 ]; then echo "- iter $i: worker failed agent-exit=4" >> "$LEDGER"; exit 5; fi

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
AGENT_CMD="${AGENT_CMD-claude -p}" # reviewed host flags; task-root cwd; protect checks/ + rubric; unset-only default
PREFLIGHT="${PREFLIGHT:-}" # one executable pathname, not shell text; empty = attended example, never met
MAX_ROUNDS="${MAX_ROUNDS-4}"
STATE="${STATE:-./state}"; mkdir -p "$STATE"
log() { printf '%s\n' "$*" >> "$STATE/flow.log"; }
case "${AGENT_CMD//[[:space:]]/}" in "") log "agent_cmd configuration gate=4"; echo "agent_cmd configuration gate=4: empty AGENT_CMD" >&2; exit 4 ;; esac
case "$MAX_ROUNDS" in ""|0|0*|*[!0-9]*) log "max_rounds configuration gate=4: $MAX_ROUNDS"; echo "max_rounds configuration gate=4: $MAX_ROUNDS" >&2; exit 4 ;; esac
MAX_ROUNDS_LEN="${#MAX_ROUNDS}"
if [ "$MAX_ROUNDS_LEN" -gt 10 ] || { [ "$MAX_ROUNDS_LEN" -eq 10 ] && [ "$MAX_ROUNDS" \> 2147483647 ]; }; then log "max_rounds configuration gate=4: $MAX_ROUNDS"; echo "max_rounds configuration gate=4: $MAX_ROUNDS" >&2; exit 4; fi
unset MAX_ROUNDS_LEN
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
  log "end $1 agent-exit=$ec"
  if [ "$ec" -eq 4 ]; then log "worker gate=5 agent-exit=4"; return 5; fi
  return "$ec"
}

# UNATTENDED PREFLIGHT: insert companion block here, before the draft call.

cp prompts/draft.md "$STATE/round-0-prompt.md"
run_agent "$STATE/round-0-prompt.md" "$STATE/draft.md" || { ec=$?; log "draft gate=$ec"; exit "$ec"; }

for ((r=1; r<=MAX_ROUNDS; r++)); do
  # Critic: rubric-bound, must output ACCEPT or a numbered fix list.
  { cat prompts/critic-rubric.md; echo; cat "$STATE/draft.md"; } > "$STATE/round-$r-critic-prompt.md"
  run_agent "$STATE/round-$r-critic-prompt.md" "$STATE/round-$r-critique.md" || { ec=$?; log "round $r critic gate=$ec"; exit "$ec"; }
  log "round $r ACCEPT gate start"

  if [ "$(sed '/^[[:space:]]*$/d' "$STATE/round-$r-critique.md")" = "ACCEPT" ]; then   # the whole verdict, not one line
    preflight "round-$r-post"
    log "round $r ACCEPT gate=0"; cp "$STATE/draft.md" "$STATE/final.md"; exit 0
  fi
  log "round $r ACCEPT gate=1"
  { cat prompts/revise.md; echo "## Critique"; cat "$STATE/round-$r-critique.md";
    echo "## Draft"; cat "$STATE/draft.md"; } > "$STATE/round-$r-revise-prompt.md"
  run_agent "$STATE/round-$r-revise-prompt.md" "$STATE/draft.md" || { ec=$?; log "round $r revise gate=$ec"; exit "$ec"; }
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
AGENT_CMD="${AGENT_CMD-claude -p}" # reviewed flags; task-root cwd; protect checks/ + TASKS.canon; unset-only default
PREFLIGHT="${PREFLIGHT:-}" # one executable pathname, not shell text; empty = attended example, never met
TASKS_SRC="${TASKS:-TASKS.md}"           # human-owned backlog
VERIFY="${VERIFY:-./checks/verify.sh}"
MAX_ITER="${MAX_ITER-20}"               # justified: backlogs often exceed ten items
STATE="${STATE:-./state}"; mkdir -p "$STATE"
log() { printf '%s\n' "$*" >> "$STATE/flow.log"; }
case "${AGENT_CMD//[[:space:]]/}" in "") log "agent_cmd configuration gate=4"; echo "agent_cmd configuration gate=4: empty AGENT_CMD" >&2; exit 4 ;; esac
case "$MAX_ITER" in ""|0|0*|*[!0-9]*) log "max_iter configuration gate=4: $MAX_ITER"; echo "max_iter configuration gate=4: $MAX_ITER" >&2; exit 4 ;; esac
MAX_ITER_LEN="${#MAX_ITER}"
if [ "$MAX_ITER_LEN" -gt 10 ] || { [ "$MAX_ITER_LEN" -eq 10 ] && [ "$MAX_ITER" \> 2147483647 ]; }; then log "max_iter configuration gate=4: $MAX_ITER"; echo "max_iter configuration gate=4: $MAX_ITER" >&2; exit 4; fi
unset MAX_ITER_LEN
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
if [ ! -e "$TASKS" ]; then
  if [ -f "$TASKS_SRC" ] && [ ! -d "$TASKS_SRC" ]; then cp "$TASKS_SRC" "$TASKS" || { echo "canonical backlog missing: $TASKS_SRC" >&2; exit 4; }
  else echo "canonical backlog missing: $TASKS_SRC" >&2; exit 4; fi
fi
if [ ! -f "$TASKS" ] || [ ! -r "$TASKS" ]; then echo "canonical backlog unreadable: $TASKS" >&2; exit 4; fi
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
  if [ ! -f "$TASKS" ] || [ ! -r "$TASKS" ]; then echo "canonical backlog unreadable: $TASKS" >&2; exit 4; fi
  ec=0; line="$(grep -n -m1 -v '^[[:space:]]*$' "$TASKS")" || ec=$?
  if [ "$ec" -gt 1 ]; then echo "canonical backlog unreadable: $TASKS" >&2; exit 4; fi
  [ -z "$line" ] && { preflight "backlog-empty-post"; echo "backlog empty"; exit 0; }
  num="${line%%:*}"; task="${line#*:}"

  # Fresh context per task.
  before="$(snap)"
  printf 'Complete exactly this one task, then stop: %s\n' "$task" > "$STATE/task-$i-prompt.md"
  preflight "task-$i-pre"
  log "task $i start"
  ec=0; $AGENT_CMD < "$STATE/task-$i-prompt.md" > "$STATE/task-$i-out.md" || ec=$?
  log "task $i end agent-exit=$ec"
  if [ "$ec" -eq 4 ]; then echo "- worker failed: $task (iter $i) agent-exit=4" >> "$STATE/ledger.md"; exit 5; fi
  [ "$ec" -eq 0 ] || { echo "- worker failed: $task (iter $i) agent-exit=$ec" >> "$STATE/ledger.md"; exit 3; }

  run_verify || { echo "- failed verify: $task (iter $i)" >> "$STATE/ledger.md"; exit 3; }
  [ -z "$before" ] || [ "$(snap)" != "$before" ] || { echo "- no change: $task (iter $i)" >> "$STATE/ledger.md"; exit 3; }
  preflight "task-$i-post"
  # Script, not agent, retires the EXACT line it dispatched.
  sed "${num}d" "$TASKS" > "$TASKS.tmp" && mv "$TASKS.tmp" "$TASKS" || { echo "- canonical backlog missing" >> "$STATE/ledger.md"; exit 4; }
  echo "- done: $task (iter $i)" >> "$STATE/ledger.md"
done
# Last task retired on the final iteration is success, not cap.
if [ ! -f "$TASKS" ] || [ ! -r "$TASKS" ]; then echo "canonical backlog unreadable: $TASKS" >> "$STATE/ledger.md"; echo "canonical backlog unreadable: $TASKS" >&2; exit 4; fi
ec=0; grep -q '[^[:space:]]' "$TASKS" || ec=$?
if [ "$ec" -eq 0 ]; then echo "- cap $MAX_ITER exhausted" >> "$STATE/ledger.md"; exit 2; fi
if [ "$ec" -gt 1 ]; then echo "canonical backlog unreadable: $TASKS" >> "$STATE/ledger.md"; echo "canonical backlog unreadable: $TASKS" >&2; exit 4; fi
preflight "queue-retired-post"
echo "backlog empty"; exit 0
```

## Template: Multi-Wave Fan-out (bash)

For repeated breadth, compose parallel-inside-loop first; use this only when that becomes clumsy.

```bash
#!/usr/bin/env bash
# generated-by: flow-loop-harness / multi-wave / 2026-10-01 / dry-run-required
set -euo pipefail
AGENT_CMD="${AGENT_CMD-claude -p}" # reviewed host flags; task-root cwd; protect checks/; unset-only default
PREFLIGHT="${PREFLIGHT:-}" # one executable pathname, not shell text; empty = attended example, never met
VERIFY="${VERIFY:-./checks/converged.sh}"  # truth layer: exit 0 = converged
MAX_WAVES="${MAX_WAVES-4}"                 # cap: distinct exit, not a failure
MAX_JOBS="${MAX_JOBS-4}"                   # per-wave concurrency budget
STATE="${STATE:-./state}"; mkdir -p "$STATE"
LEDGER="$STATE/ledger.md"; touch "$LEDGER"
log() { printf '%s\n' "$*" >> "$STATE/flow.log"; }
case "${AGENT_CMD//[[:space:]]/}" in "") log "agent_cmd configuration gate=4"; echo "agent_cmd configuration gate=4: empty AGENT_CMD" >&2; exit 4 ;; esac
case "$MAX_WAVES" in ""|0|0*|*[!0-9]*) log "max_waves configuration gate=4: $MAX_WAVES"; echo "max_waves configuration gate=4: $MAX_WAVES" >&2; exit 4 ;; esac
MAX_WAVES_LEN="${#MAX_WAVES}"
if [ "$MAX_WAVES_LEN" -gt 10 ] || { [ "$MAX_WAVES_LEN" -eq 10 ] && [ "$MAX_WAVES" \> 2147483647 ]; }; then log "max_waves configuration gate=4: $MAX_WAVES"; echo "max_waves configuration gate=4: $MAX_WAVES" >&2; exit 4; fi
unset MAX_WAVES_LEN
case "$MAX_JOBS" in ""|0|0*|*[!0-9]*) log "max_jobs configuration gate=4: $MAX_JOBS"; echo "max_jobs configuration gate=4: $MAX_JOBS" >&2; exit 4 ;; esac
MAX_JOBS_LEN="${#MAX_JOBS}"
if [ "$MAX_JOBS_LEN" -gt 10 ] || { [ "$MAX_JOBS_LEN" -eq 10 ] && [ "$MAX_JOBS" \> 2147483647 ]; }; then log "max_jobs configuration gate=4: $MAX_JOBS"; echo "max_jobs configuration gate=4: $MAX_JOBS" >&2; exit 4; fi
unset MAX_JOBS_LEN
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

