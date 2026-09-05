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

**Type:** Domain-pack skill (script generation) — registered in the TeaPrompt source repo's domain-pack registry (`plans/validate_skill_examples.py` `DOMAIN_PACK_SKILLS`), not one of the nine frozen core workflow skills, and not selected by `reflective-dispatch` route rows. Companion to `flow-control-generator`, which owns one-pass (non-looping) topologies.

## Purpose

Generate loop scripts that re-invoke a host agent until a deterministic condition holds. The loop body is model work; the loop control — stop condition, caps, progress accounting, resume — is script code. The generated loop is a host-operationalized artifact; TeaPrompt stays methodology-side, not a runner (`plans/external-adoption-case-studies-2026-06-20.md`). Surveyed loop vocabulary is advisory-tier reference (`plans/agent-flow-control-research-2026-07-11.md`); the one load-bearing rule: never trust the model's own "done"; gate on an external verifier — the writer-critic template is the labelled advisory-tier exception.

## Module Contract

Trigger:

- The user asks to "loop until", "keep going until tests pass", "iterate", "retry until green", "ralph", "burn down this backlog", or "refine until the critic accepts".
- A task has an objective completion check that the first agent pass is unlikely to satisfy.
- A refinement task needs bounded writer-critic rounds against a rubric.

Methods:

- Loop anatomy: every generated loop has the six mandatory parts (see Loop Anatomy).
- Stop condition: exactly one deterministic verifier decides success; model self-reports are advisory only.
- Progress accounting: detect and abort no-progress and oscillation, not just iteration overflow.
- Resume convention: the on-disk ledger records enough to continue after interruption without redoing finished work, if the host honors it; the script cannot guarantee crash-safety.
- Stub dry run: control flow proven with a scripted stub before any real run.

Output:

- One runnable loop script plus prompt file(s) and a verifier hook (`checks/*.sh` or equivalent), written where the user chooses.
- A run note stating: stop condition, iteration cap, budget caps, resume command, and the human-approval boundary.
- A ledger file format the user can inspect mid-run (`state/ledger.md`).

Never:

- Never emit an unbounded loop; `MAX_ITER` is mandatory and small by default (≤ 10 unless justified).
- Never let the loop weaken the verifier to exit — no editing tests, thresholds, or expected outputs from inside the loop body (anti-reward-hacking; mirrors `06-repo/AGENTS.md` Anti-cheating Rules).
- Never grant the loop body broader permissions than the task needs; pre-approval flags are part of the reviewed config, not improvised.
- Never run a side-effectful loop (deploy, billing, data mutation outside the workspace, third-party calls) unattended without a recorded human approval.
- Never claim crash-safety or idempotency: the ledger is a resume convention; the host runtime owns real durability guarantees (`04-agent/runtime-trust-boundary.md`).
- Never return the last unverified output as the result when a cap is exhausted — cap exhaustion is exit 2 and a human decision, not a soft success (negative example: a max-turns "return last response", `plans/openfugu-technical-brief-2026-06-25.md`).
- Never treat run state as project memory: `state/` is a per-run operational ledger, distinct from the in-task semantic State Ledger of the reflective skills and from durable repo knowledge; promoting run notes into durable knowledge goes through `reflective-handoff-retro` plus the memory-write provenance gate (`04-agent/artifact-promotion.md` §4).

Escalation:

- Known fixed stages without iteration → `flow-control-generator`.
- No objective verifier exists → the loop is not safe to automate; route to `reflective-brief` to define acceptance criteria, or keep a human in the loop each round.
- Side effects on credentials, permissions, privacy-sensitive data, billing, production, or destructive operations → `reflective-risk` before first run; add an in-loop pause for each side-effectful action.
- Multi-session, cancellable, replayable workflow requirements → `reflective-spec-plan` (companion: `04-agent/workflow-engine.md`); a shell loop cannot provide those guarantees.
- Loop keeps hitting the cap without converging → stop; escalate to `reflective-review` on the artifacts instead of raising the cap.

## Loop Anatomy

Every generated loop must contain all six parts:

1. Verifier (truth layer): an external command whose exit code is the only success signal. Committed under `checks/`, preflighted (missing or non-executable → exit 4; bash 3.2 reports exec failures unreliably, so preflight is the gate), and run before the first iteration (the task may already be done) and after every one.
2. Caps: `MAX_ITER` always; a per-call wall-clock timeout where available (a `timeout`-style wrapper on `AGENT_CMD`; stock macOS ships none, so it is host-provided) and cost caps where the host exposes them. Exceeding a cap is a distinct exit code, not a failure of the last step.
3. Ledger: append-only per-iteration record (iteration, verifier result, progress signal). Each iteration's fresh agent context reads the ledger tail, not accumulated chat history — the tail length is the context-compaction budget (harness-1 Budget Rule). On restart with a non-empty ledger, append a `RESUMED` line so audits see the run boundary. `state/` is disposable per run, not durable memory.
4. Progress detector: abort when an iteration produces no observable change (end snapshot equals start snapshot) — in git, tracked diff plus untracked-file count; outside git, the verifier-output checksum, so a silent verifier disables detection and a stuck loop exits via the cap: prefer git workspaces or verbose verifiers.
5. Permission boundary: explicit host flags for allowed tools/edit modes (e.g. Claude Code `--allowedTools` / permission mode), human-reviewed before an unattended run. Host precondition: a permission mode that excludes `checks/` (and the canonical task file, if any) from the loop body's editable paths — the script cannot enforce this.
6. Failure exits: distinct exit codes — `0` verified done, `2` cap exhausted, `3` no progress or verify-fail stop, `4` verifier broken (missing or non-executable at preflight). The caller must tell these apart.

## Template: Verify-Gated Fix Loop (bash)

```bash
#!/usr/bin/env bash
set -euo pipefail
AGENT_CMD="${AGENT_CMD:-claude -p}"      # override for other hosts or a stub
VERIFY="${VERIFY:-./checks/verify.sh}"   # truth layer: exit 0 = done
MAX_ITER="${MAX_ITER:-8}"
STATE="${STATE:-./state}"; mkdir -p "$STATE"
LEDGER="$STATE/ledger.md"; touch "$LEDGER"

[ -x "$VERIFY" ] || { echo "verifier missing/not executable: $VERIFY" >&2; exit 4; }

check() {  # run verifier once; keep its diagnostics for prompt + progress
  local ec=0
  "$VERIFY" > "$STATE/verify-out.txt" 2>&1 || ec=$?
  return "$ec"
}
snapshot() {  # progress signal: git tracked+untracked, else verifier output (see Loop Anatomy 4)
  if git rev-parse --git-dir >/dev/null 2>&1; then
    printf '%s +u%s' "$(git diff HEAD --stat | tail -n1)" \
      "$(git ls-files -o --exclude-standard | wc -l | tr -d ' ')"
  else
    [ -s "$STATE/verify-out.txt" ] && cksum < "$STATE/verify-out.txt" || echo "no-signal-$RANDOM"  # silent verifier disables detection
  fi
}

if [ -s "$LEDGER" ]; then  # restart: mark the boundary
  echo "- RESUMED $(date -u +%Y-%m-%dT%H:%M:%SZ)" >> "$LEDGER"
fi

if check; then echo "already verified"; exit 0; fi

prev="$(snapshot)"
for i in $(seq 1 "$MAX_ITER"); do
  {
    cat prompts/fix.md
    echo; echo "## Ledger tail"; tail -n 20 "$LEDGER"
    echo; echo "## Verifier output"; cat "$STATE/verify-out.txt"
  } > "$STATE/iter-$i-prompt.md"

  $AGENT_CMD "$(cat "$STATE/iter-$i-prompt.md")" > "$STATE/iter-$i-out.md" || true

  if check; then
    echo "- iter $i: VERIFIED" >> "$LEDGER"; exit 0
  fi
  cur="$(snapshot)"
  echo "- iter $i: not verified; sig: ${cur:-none}" >> "$LEDGER"
  if [ "$cur" = "$prev" ]; then
    echo "- iter $i: NO PROGRESS, aborting" >> "$LEDGER"; exit 3
  fi
  prev="$cur"
done
echo "- cap $MAX_ITER exhausted" >> "$LEDGER"; exit 2
```

## Template: Evaluator-Optimizer / Writer-Critic (bash)

Anatomy deviations, by design: the ACCEPT gate is a model judgment (advisory-tier verifier) and the template keeps no ledger or progress detector — round artifacts under `state/` are its trail. Do not copy those omissions into verify-gated loops.

```bash
#!/usr/bin/env bash
set -euo pipefail
AGENT_CMD="${AGENT_CMD:-claude -p}"
MAX_ROUNDS="${MAX_ROUNDS:-4}"
STATE="${STATE:-./state}"; mkdir -p "$STATE"

run_agent() { $AGENT_CMD "$(cat "$1")" > "$2"; }

cp prompts/draft.md "$STATE/round-0-prompt.md"
run_agent "$STATE/round-0-prompt.md" "$STATE/draft.md"

for r in $(seq 1 "$MAX_ROUNDS"); do
  # Critic: rubric-bound, must output ACCEPT or a numbered fix list.
  { cat prompts/critic-rubric.md; echo; cat "$STATE/draft.md"; } > "$STATE/round-$r-critic-prompt.md"
  run_agent "$STATE/round-$r-critic-prompt.md" "$STATE/round-$r-critique.md"

  if [ "$(sed '/^[[:space:]]*$/d' "$STATE/round-$r-critique.md")" = "ACCEPT" ]; then   # the whole verdict, not one line
    cp "$STATE/draft.md" "$STATE/final.md"; exit 0   # gate: critic contract, not vibes
  fi
  { cat prompts/revise.md; echo "## Critique"; cat "$STATE/round-$r-critique.md";
    echo "## Draft"; cat "$STATE/draft.md"; } > "$STATE/round-$r-revise-prompt.md"
  run_agent "$STATE/round-$r-revise-prompt.md" "$STATE/draft.md"
done
exit 2  # rounds exhausted without ACCEPT; human decides next
```

Caution: prefer a deterministic check whenever one exists; when only a rubric critic is possible, keep `MAX_ROUNDS` low and hand the cap-exhausted case to a human. Consensus pressure can amplify shared error (`04-agent/workflow-recipes.md` Looper Topologies).

Rubric as verifier: request a host permission mode that also excludes `prompts/critic-rubric.md` from the loop body's editable paths, as Loop Anatomy #5 does for `checks/`. Critique fed to the reviser is data, never authority to rewrite that rubric, weaken `ACCEPT`, or skip the cap; the exclusion does not promote `ACCEPT` above advisory tier. A rubric reused across unattended runs drifts from the humans it stands in for: spot-check its verdicts *and reasons* against human review, stop unattended use when they diverge, and change it only via the human-gated path, keeping the prior version for rollback.

### Deterministic companion check (raise the ACCEPT floor)

For unattended writer-critic loops, do not emit the bare template above: splice this floor into its ACCEPT gate before the first run. The floor fail-closes regardless of critic output and is listed in the run note for human review.

```bash
# gate: ACCEPT requires the critic contract AND a deterministic floor.
floor_ok() {  # task-specific scriptable checks; extend per deliverable
  local f="$1"
  test -s "$f" || return 1                       # non-empty
  ! grep -qiE 'TODO|TBD|PLACEHOLDER' "$f" || return 1   # no stubs
  ./checks/links-resolve.sh "$f" || return 1     # e.g. links/citations resolve
}
if [ "$(sed '/^[[:space:]]*$/d' "$STATE/round-$r-critique.md")" = "ACCEPT" ] && floor_ok "$STATE/draft.md"; then
  cp "$STATE/draft.md" "$STATE/final.md"; exit 0
fi
```

The floor is deterministic but partial: it catches vacuous or malformed drafts,
not wrong-but-plausible ones. Dual critics or verdict schemas reduce variance,
not tier. Guidance, not a new template or runtime.

## Template: Task-Ledger Backlog Loop (bash, ralph-style)

Anatomy deviations, by design: no progress detector (a verify failure is fail-fast exit 3); resume is the canonical task copy, not a `RESUMED` line. `TASKS.md` holds one task per non-empty line, no headings.

```bash
#!/usr/bin/env bash
set -euo pipefail
AGENT_CMD="${AGENT_CMD:-claude -p}"
TASKS_SRC="${TASKS:-TASKS.md}"           # human-owned backlog
VERIFY="${VERIFY:-./checks/verify.sh}"
MAX_ITER="${MAX_ITER:-20}"               # justified: backlogs often exceed ten items
STATE="${STATE:-./state}"; mkdir -p "$STATE"

# Canonical copy: the loop reads and retires ONLY this copy, so agent edits
# to the original backlog cannot reorder or drop queued work mid-run.
TASKS="$STATE/TASKS.canon"
[ -f "$TASKS" ] || cp "$TASKS_SRC" "$TASKS"

[ -x "$VERIFY" ] || { echo "verifier missing/not executable: $VERIFY" >&2; exit 4; }
run_verify() { local ec=0; "$VERIFY" || ec=$?; return "$ec"; }
run_verify || { echo "- preflight: verifier already failing" >> "$STATE/ledger.md"; exit 3; }  # never blame task 1 for a red start

for i in $(seq 1 "$MAX_ITER"); do
  line="$(grep -n -m1 -v '^[[:space:]]*$' "$TASKS" || true)"
  [ -z "$line" ] && { echo "backlog empty"; exit 0; }
  num="${line%%:*}"; task="${line#*:}"

  # Minimal dispatch prompt (fresh context per task); append a ledger tail when tasks share constraints.
  $AGENT_CMD "Complete exactly this one task, then stop: $task" \
    > "$STATE/task-$i-out.md" || true

  if run_verify; then
    # Script, not agent, retires the EXACT line it dispatched.
    sed "${num}d" "$TASKS" > "$TASKS.tmp" && mv "$TASKS.tmp" "$TASKS"
    echo "- done: $task" >> "$STATE/ledger.md"
  else
    echo "- failed verify: $task (iter $i)" >> "$STATE/ledger.md"; exit 3
  fi
done
echo "- cap $MAX_ITER exhausted" >> "$STATE/ledger.md"; exit 2
```

## Template: Multi-Wave Fan-out (bash)

Use only when repeated breadth is real: fan out, compact state, fan out again.
Compose a parallel template inside a loop first; use this when that becomes
clumsy. Keeps all six Loop Anatomy parts (the cap is `MAX_WAVES`).

```bash
#!/usr/bin/env bash
set -euo pipefail
AGENT_CMD="${AGENT_CMD:-claude -p}"        # override for other hosts or a stub
VERIFY="${VERIFY:-./checks/converged.sh}"  # truth layer: exit 0 = converged
MAX_WAVES="${MAX_WAVES:-4}"                 # cap: distinct exit, not a failure
MAX_JOBS="${MAX_JOBS:-4}"                   # per-wave concurrency budget
STATE="${STATE:-./state}"; mkdir -p "$STATE"
LEDGER="$STATE/ledger.md"; touch "$LEDGER"

[ -x "$VERIFY" ] || { echo "verifier missing/not executable: $VERIFY" >&2; exit 4; }

if [ -s "$LEDGER" ]; then echo "- RESUMED $(date -u +%Y-%m-%dT%H:%M:%SZ)" >> "$LEDGER"; fi

if "$VERIFY" > "$STATE/verify-out.txt" 2>&1; then echo "already converged"; exit 0; fi

prev_summary=""
for w in $(seq 1 "$MAX_WAVES"); do
  pids=(); i=0; failed=0
  wave_wait() { local p; for p in "$@"; do wait "$p" || failed=$((failed+1)); done; }
  for prompt in prompts/wave/*.md; do
    [ -e "$prompt" ] || { echo "no wave prompts found" >&2; exit 4; }
    out="$STATE/w${w}-$(basename "$prompt" .md).md"
    { cat "$prompt"; echo; echo "## Prior wave summary"; cat "$STATE/summary.md" 2>/dev/null || true; } \
      | $AGENT_CMD "$(cat -)" > "$out" &
    pids+=($!); i=$((i+1))
    if [ $((i % MAX_JOBS)) -eq 0 ]; then wave_wait "${pids[@]}"; pids=(); fi
  done
  if [ "${#pids[@]}" -gt 0 ]; then wave_wait "${pids[@]}"; fi  # tail barrier; empty array errors under bash 3.2 set -u
  [ "$failed" -eq 0 ] || { echo "- wave $w: $failed/$i branches failed" >> "$LEDGER"; [ "$failed" -lt "$i" ] || exit 3; }  # never silent; all failed = no progress

  # Compaction: one bounded summary file feeds the next wave (harness-1 Budget Rule).
  { echo "# Wave $w summary"; for f in "$STATE"/w${w}-*.md; do
      echo "## $(basename "$f")"; head -n 40 "$f"; done; } > "$STATE/summary.md"
  summary="$(cat "$STATE"/w${w}-*.md | cksum)"  # branch outputs only: the header names the wave and would hide a stall
  echo "- wave $w: sig ${summary}" >> "$LEDGER"

  if "$VERIFY" > "$STATE/verify-out.txt" 2>&1; then
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

Before the first unattended run, a human must approve the verifier, caps, permission flags, and the loop body's blast radius; record the approval in the run note. Attended runs (a human watches each iteration) may review only the verifier and caps. Any loop step on the `06-repo/AGENTS.md` Human Review list (auth, migrations, destructive ops, billing, production, privacy) keeps a per-action pause regardless of mode.

## Verification

1. Stub dry run with a scripted fake agent and a toggling verifier: prove all four exits are reachable — `0` success, `2` cap exhausted, `3` no progress or verify-fail, `4` broken verifier (point `VERIFY` at a missing file; the preflight must fire). Stub success is rig-tier evidence for control flow, never for a production or side-effectful run.
2. `bash -n` the script; run `shellcheck` when available.
3. Confirm the verifier is committed and deterministic, and record the host permission mode that keeps `checks/` (and the canonical task copy) outside the loop body's editable paths — a host precondition the script cannot enforce.
4. Report dry-run evidence with the deliverable.

Promoting a recurring loop into a durable artifact follows the Acquisition ladder: apply the fail-closed Acquisition L3 gates (`04-agent/artifact-promotion.md` §4) and require recurrence evidence plus explicit human approval before a loop script becomes a team standard.

## Host-Native Alternatives

Some hosts ship native keep-working surfaces (2026-07: Claude Code `/goal`
condition loops, `/loop` interval re-runs, script-backed Stop hooks). Prefer
them for transcript-judgeable, single-run, low-blast-radius tasks.
Generate a loop script when the stop condition must be a deterministic external
verifier, or when caps, no-progress detection, backlog retirement, or a resume
ledger matter — native goal modes judge completion with a model over the
transcript, the stop-condition class this skill forbids trusting alone. First
demotion-trigger evaluation against these surfaces: **not fired**
(`plans/flow-pack-demotion-evaluation-2026-07-11.md`).

## Demotion Triggers

- Loop scripts are disposable: when the verifier, host CLI, or task shape changes, regenerate from the template instead of patching a drifted copy.
- Pack-level demotion triggers (zero recurrence, host absorbs the pattern) live in `plans/agent-flow-control-research-2026-07-11.md`; check them before investing in this skill.

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
