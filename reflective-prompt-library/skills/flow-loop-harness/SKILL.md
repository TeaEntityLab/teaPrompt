---
name: flow-loop-harness
description: Use when an agent must iterate until a condition is verified — fix-until-tests-pass, writer-critic refinement, backlog burn-down, ralph-style loops — over a host agent CLI in headless mode. It writes loop scripts whose stop conditions are external deterministic verifiers, with iteration and budget caps, no-progress detection, human-review gates before unattended or side-effectful runs, and state ledgers as a resume convention the host must honor.
license: MIT
risk_level: medium
human_review_required: true
external_io: false
context_load: medium
---

# Flow Loop Harness

**Type:** Domain-pack skill (script generation) — registered in `plans/validate_skill_examples.py` `DOMAIN_PACK_SKILLS`, not one of the nine frozen core workflow skills, and not selected by `reflective-dispatch` route rows. Companion to `flow-control-generator`, which owns one-pass (non-looping) topologies.

## Purpose

Generate loop scripts that re-invoke a host agent until a deterministic condition holds. The loop body is model work; the loop control — stop condition, caps, progress accounting, resume — is script code. TeaPrompt stays on the methodology side of the methodology-vs-operationalization boundary (`plans/external-adoption-case-studies-2026-06-20.md`): the generated loop is a host-operationalized artifact, not a TeaPrompt-operated runner. The cross-platform loop vocabulary referenced here (ADK `LoopAgent`, LangGraph cycles, MAF checkpointed workflows, Anthropic evaluator-optimizer, practitioner "ralph" harnesses) is advisory-tier reference material; the one load-bearing rule is: never trust the model's own "done"; gate on an external verifier (see `../../plans/agent-flow-control-research-2026-07-11.md`).

## Module Contract

Trigger:

- The user asks to "loop until", "keep going until tests pass", "iterate", "retry until green", "ralph", "burn down this backlog", or "refine until the critic accepts".
- A task has an objective completion check that the first agent pass is unlikely to satisfy.
- A refinement task needs bounded writer-critic rounds against a rubric.

Methods:

- Loop anatomy enforcement: every generated loop has the six mandatory parts (see Loop Anatomy).
- Stop-condition design: exactly one deterministic verifier decides success; model self-reports are advisory only.
- Progress accounting: detect and abort no-progress and oscillation, not just iteration overflow.
- Resume-convention state: the on-disk ledger records enough to continue after interruption without redoing finished work — provided the host honors it; the script cannot guarantee crash-safety.
- Stub dry run: control flow proven with a scripted stub before any real run.

Output:

- One runnable loop script plus prompt file(s) and a verifier hook (`checks/*.sh` or equivalent), written where the user chooses.
- A run note stating: stop condition, iteration cap, budget caps, resume command, and the human-approval boundary.
- A ledger file format the user can inspect mid-run (`state/ledger.md`).

Never:

- Never emit an unbounded loop; `MAX_ITER` is mandatory and small by default (≤ 10 unless justified).
- Never let the loop weaken the verifier to exit — no editing tests, thresholds, or expected outputs from inside the loop body prompt (anti-reward-hacking; mirrors `06-repo/AGENTS.md` Anti-cheating Rules).
- Never grant the loop body broader permissions than the task needs; permission pre-approval flags are part of the reviewed config, not improvised.
- Never run a side-effectful loop (deploy, billing, data mutation outside the workspace, third-party calls) unattended without an explicit human approval recorded first.
- Never claim crash-safety or idempotency: the ledger is a resume convention; the host runtime owns real durability guarantees (`04-agent/runtime-trust-boundary.md`).
- Never return the last unverified output as the result when a cap is exhausted — cap exhaustion is exit 2 and a human decision, not a soft success (negative example: OpenFugu's max-turns "return last response", `plans/openfugu-technical-brief-2026-06-25.md`).
- Never treat run state as project memory: `state/` is a per-run operational ledger, distinct from the in-task semantic State Ledger of the reflective skills and from durable repo knowledge; promoting run notes into durable knowledge goes through `reflective-handoff-retro` plus the memory-write provenance gate of `04-agent/artifact-promotion.md` §4.

Escalation:

- Known fixed stages without iteration → `flow-control-generator`.
- No objective verifier exists → the loop is not safe to automate; route to `reflective-brief` to define acceptance criteria, or keep the human in the loop each round.
- Side effects on credentials, permissions, privacy-sensitive data, billing, production, or destructive operations → `reflective-risk` before first run; add an in-loop pause step for each side-effectful action.
- Multi-session, cancellable, replayable workflow requirements → `reflective-spec-plan` with `04-agent/workflow-engine.md`; a shell loop cannot provide those guarantees.
- Loop keeps hitting the cap without converging → stop; escalate to `reflective-review` on the artifacts rather than raising the cap.

## Loop Anatomy

Every generated loop must contain all six parts:

1. Verifier (truth layer): an external command whose exit code is the only success signal. Committed under `checks/`, preflighted before the loop (missing or non-executable verifier → exit 4; exit-code capture of exec failures is unreliable on bash 3.2, so the preflight is the deterministic gate), and executed before the first iteration (the task may already be done) and after every iteration.
2. Caps: `MAX_ITER` always; a per-call wall-clock timeout where available (`timeout`-style wrapper on `AGENT_CMD` — stock macOS ships no `timeout(1)`, treat it as host-provided) and cost caps where the host exposes them. Exceeding a cap is a distinct exit code, not a failure of the last step.
3. Ledger: append-only per-iteration record (iteration, verifier result, progress signal). Fresh agent context each iteration reads the ledger tail instead of accumulating chat history — the tail length is the loop's context-compaction budget (harness-1 Budget Rule); tune it in the template when iterations carry more state. On restart with a non-empty ledger, append a `RESUMED` line so audits can see the run boundary. `state/` is disposable per run: keep it for the post-run review, then archive or delete — it is not a durable memory surface.
4. Progress detector: abort when two consecutive iterations produce no observable change — in a git workspace, tracked-diff plus untracked-file count; outside git, the verifier output checksum. Non-git limitation: a silent verifier (no diagnostic output) disables progress detection there, and a stuck loop then exits via the cap instead; prefer git workspaces or verbose verifiers.
5. Permission boundary: explicit host flags for allowed tools/edit modes (e.g. Claude Code `--allowedTools` / permission mode); reviewed by a human before an unattended run. Host-runtime precondition: request a permission mode that excludes `checks/` (and the canonical task file, if any) from the loop body's editable paths — the script itself cannot enforce this.
6. Failure exits: distinct exit codes — `0` verified done, `2` cap exhausted, `3` no progress or verify-fail stop, `4` verifier broken (missing or non-executable at preflight). The caller must be able to tell these apart.

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

check() {  # run verifier once; capture its diagnostics for prompt + progress
  local ec=0
  "$VERIFY" > "$STATE/verify-out.txt" 2>&1 || ec=$?
  return "$ec"
}
snapshot() {  # progress signal: git tracked+untracked, else verifier output
  # (non-git fallback needs a verifier that prints diagnostics; see Loop Anatomy 4)
  if git rev-parse --git-dir >/dev/null 2>&1; then
    printf '%s +u%s' "$(git diff --stat | tail -n1)" \
      "$(git ls-files -o --exclude-standard | wc -l | tr -d ' ')"
  else
    cksum < "$STATE/verify-out.txt" 2>/dev/null || echo none
  fi
}

if [ -s "$LEDGER" ]; then  # restart of a prior run: mark the boundary
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

Anatomy deviations, by design: the ACCEPT gate is a model judgment (advisory-tier verifier), and the template keeps no ledger or progress detector — round artifacts under `state/` are its only trail. Do not copy those omissions into verify-gated loops.

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

  if grep -qx 'ACCEPT' "$STATE/round-$r-critique.md"; then
    cp "$STATE/draft.md" "$STATE/final.md"; exit 0   # gate: critic contract, not vibes
  fi
  { cat prompts/revise.md; echo "## Critique"; cat "$STATE/round-$r-critique.md";
    echo "## Draft"; cat "$STATE/draft.md"; } > "$STATE/round-$r-revise-prompt.md"
  run_agent "$STATE/round-$r-revise-prompt.md" "$STATE/draft.md"
done
exit 2  # rounds exhausted without ACCEPT; human decides next
```

Caution: a model critic is a soft, advisory-tier verifier — this template's ACCEPT gate is a model judgment, not the deterministic truth layer the other templates use. Prefer a deterministic check whenever one exists; when only a rubric critic is possible, keep `MAX_ROUNDS` low and hand the cap-exhausted case to a human. Consensus pressure can amplify shared error (`04-agent/workflow-recipes.md` Looper Topologies caution).

## Template: Task-Ledger Backlog Loop (bash, ralph-style)

```bash
#!/usr/bin/env bash
set -euo pipefail
AGENT_CMD="${AGENT_CMD:-claude -p}"
TASKS_SRC="${TASKS:-TASKS.md}"           # human-owned backlog
VERIFY="${VERIFY:-./checks/verify.sh}"
MAX_ITER="${MAX_ITER:-20}"
STATE="${STATE:-./state}"; mkdir -p "$STATE"

# Canonical copy: the loop reads and retires ONLY this copy, so agent edits
# to the original backlog cannot reorder or drop queued work mid-run.
TASKS="$STATE/TASKS.canon"
[ -f "$TASKS" ] || cp "$TASKS_SRC" "$TASKS"

[ -x "$VERIFY" ] || { echo "verifier missing/not executable: $VERIFY" >&2; exit 4; }
run_verify() { local ec=0; "$VERIFY" || ec=$?; return "$ec"; }

for i in $(seq 1 "$MAX_ITER"); do
  line="$(grep -n -m1 -v '^[[:space:]]*$' "$TASKS" || true)"
  [ -z "$line" ] && { echo "backlog empty"; exit 0; }
  num="${line%%:*}"; task="${line#*:}"

  # Dispatch prompt is intentionally minimal (fresh context per task). When tasks
  # share constraints, append a ledger tail the same way the fix loop does.
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
exit 2
```

## Human Review Boundary

Before the first unattended run, a human must approve: the verifier, the caps, the permission flags, and the blast radius of the loop body. Record the approval in the run note. Attended runs (human watches each iteration) may relax this to reviewing the verifier and caps only. Any loop step matching the `06-repo/AGENTS.md` Human Review list (auth, migrations, destructive ops, billing, production, privacy) keeps a per-action pause regardless of mode.

## Verification

1. Stub dry run with a scripted fake agent and a toggling verifier: prove all four exits are reachable — `0` success, `2` cap exhausted, `3` no progress or verify-fail, `4` broken verifier (point `VERIFY` at a missing or non-executable file; the preflight must fire). Stub success is rig-tier evidence only — it approves the control flow, never a production or side-effectful run.
2. `bash -n` the script; run `shellcheck` when available.
3. Confirm the verifier is committed and deterministic, and record the host permission mode that keeps `checks/` (and the canonical task copy) outside the loop body's editable paths — a host-runtime precondition this script cannot enforce.
4. Report dry-run evidence with the deliverable.

Promoting a recurring loop into a durable artifact follows the Acquisition ladder: apply the fail-closed L3 gates of `04-agent/artifact-promotion.md` §4 before registering it anywhere, and require recurrence evidence plus explicit human approval before elevating any loop script to a team standard.

## Demotion Triggers

- Loop scripts are disposable: when the verifier, host CLI, or task shape changes, regenerate from the template rather than patching a drifted copy.
- Pack-level demotion triggers (zero recurrence, host support absorbing the pattern) live in `../../plans/agent-flow-control-research-2026-07-11.md` — check them before investing in this skill's outputs.

## Prompt Sources

- `../../plans/agent-flow-control-research-2026-07-11.md`
- `../../plans/flow-control-pack-panel-record-2026-07-11.md`
- `../../plans/flow-coverage-panel-record-2026-07-11.md`
- `../../plans/harness-1-state-ledger-research.md` (three-layer split: project memory in repo Markdown; in-task semantic State Ledger in reflective skills; per-run operational ledger here)
- `../../04-agent/workflow-recipes.md`
- `../../04-agent/runtime-trust-boundary.md`
- `../../04-agent/artifact-promotion.md`
- `../../06-repo/AGENTS.md`
