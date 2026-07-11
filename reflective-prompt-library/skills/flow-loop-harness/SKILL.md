---
name: flow-loop-harness
description: Use when an agent must iterate until a condition is verified — fix-until-tests-pass, writer-critic refinement, backlog burn-down, ralph-style loops — over a host agent CLI in headless mode. It writes loop scripts whose stop conditions are external deterministic verifiers, with iteration and budget caps, no-progress detection, resumable state ledgers, and human-review gates before unattended or side-effectful runs.
license: MIT
risk_level: medium
human_review_required: true
external_io: false
context_load: medium
---

# Flow Loop Harness

**Type:** Domain-pack skill (script generation). Not one of the nine frozen core workflow skills; does not change `reflective-dispatch` routing. Companion to `flow-control-generator`, which owns one-pass (non-looping) topologies.

## Purpose

Generate loop scripts that re-invoke a host agent until a deterministic condition holds. The loop body is model work; the loop control — stop condition, caps, progress accounting, resume — is script code. This encodes the 2026 consensus across ADK `LoopAgent`, LangGraph cycles, Microsoft Agent Framework checkpointed workflows, Anthropic evaluator-optimizer, and practitioner "ralph" harnesses: never trust the model's own "done"; gate on an external verifier (see `../../plans/agent-flow-control-research-2026-07-11.md`).

## Module Contract

Trigger:

- The user asks to "loop until", "keep going until tests pass", "iterate", "retry until green", "ralph", "burn down this backlog", or "refine until the critic accepts".
- A task has an objective completion check that the first agent pass is unlikely to satisfy.
- A refinement task needs bounded writer-critic rounds against a rubric.

Methods:

- Loop anatomy enforcement: every generated loop has the six mandatory parts (see Loop Anatomy).
- Stop-condition design: exactly one deterministic verifier decides success; model self-reports are advisory only.
- Progress accounting: detect and abort no-progress and oscillation, not just iteration overflow.
- Resume-first state: the ledger on disk is sufficient to continue after interruption without redoing finished work.
- Stub dry run: control flow proven with a scripted stub before any real run.

Output:

- One runnable loop script plus prompt file(s) and a verifier hook (`checks/*.sh` or equivalent), written where the user chooses.
- A run note stating: stop condition, iteration cap, budget caps, resume command, and the human-approval boundary.
- A ledger file format the user can inspect mid-run (`state/ledger.md` or `TASKS.md`).

Never:

- Never emit an unbounded loop; `MAX_ITER` is mandatory and small by default (≤ 10 unless justified).
- Never let the loop weaken the verifier to exit — no editing tests, thresholds, or expected outputs from inside the loop body prompt (anti-reward-hacking; mirrors `06-repo/AGENTS.md` Anti-cheating Rules).
- Never grant the loop body broader permissions than the task needs; permission pre-approval flags are part of the reviewed config, not improvised.
- Never run a side-effectful loop (deploy, billing, data mutation outside the workspace, third-party calls) unattended without an explicit human approval recorded first.
- Never claim crash-safety or idempotency: the ledger is a resume convention; the host runtime owns real durability guarantees (`04-agent/runtime-trust-boundary.md`).

Escalation:

- Known fixed stages without iteration → `flow-control-generator`.
- No objective verifier exists → the loop is not safe to automate; route to `reflective-brief` to define acceptance criteria, or keep the human in the loop each round.
- Side effects on credentials, permissions, privacy data, billing, production, or destructive operations → `reflective-risk` before first run; add an in-loop pause step for each side-effectful action.
- Multi-session, cancellable, replayable workflow requirements → `reflective-spec-plan` with `04-agent/workflow-engine.md`; a shell loop cannot provide those guarantees.
- Loop keeps hitting the cap without converging → stop; escalate to `reflective-review` on the artifacts rather than raising the cap.

## Loop Anatomy

Every generated loop must contain all six parts:

1. Verifier (truth layer): an external command whose exit code is the only success signal. Committed under `checks/`, run before the first iteration (task may already be done) and after every iteration.
2. Caps: `MAX_ITER` always; wall-clock or cost caps where the host exposes them. Exceeding a cap is a distinct exit code, not a failure of the last step.
3. Ledger: append-only per-iteration record (iteration, prompt hash, verifier result, changed-file count or diff stat). Fresh agent context each iteration reads the ledger tail instead of accumulating chat history — this is what makes ralph-style loops resumable.
4. Progress detector: abort when two consecutive iterations produce no observable change (empty diff, identical verifier output) — the loop is stuck, more iterations only spend budget.
5. Permission boundary: explicit host flags for allowed tools/edit modes (e.g. Claude Code `--allowedTools` / permission mode); reviewed by a human before an unattended run.
6. Failure exits: distinct exit codes — `0` verified done, `2` cap exhausted, `3` no progress, `4` verifier itself broken. The caller must be able to tell these apart.

## Template: Verify-Gated Fix Loop (bash)

```bash
#!/usr/bin/env bash
set -euo pipefail
AGENT_CMD="${AGENT_CMD:-claude -p}"      # override for other hosts or a stub
VERIFY="${VERIFY:-./checks/verify.sh}"   # truth layer: exit 0 = done
MAX_ITER="${MAX_ITER:-8}"
STATE="${STATE:-./state}"; mkdir -p "$STATE"
LEDGER="$STATE/ledger.md"; touch "$LEDGER"

snapshot() { git -C . diff --stat | tail -n1; }      # progress signal

if "$VERIFY"; then echo "already verified"; exit 0; fi

prev="$(snapshot)"
for i in $(seq 1 "$MAX_ITER"); do
  {
    cat prompts/fix.md
    echo; echo "## Ledger tail"; tail -n 20 "$LEDGER"
    echo; echo "## Verifier output"; "$VERIFY" 2>&1 || true
  } > "$STATE/iter-$i-prompt.md"

  $AGENT_CMD "$(cat "$STATE/iter-$i-prompt.md")" > "$STATE/iter-$i-out.md" || true

  if "$VERIFY"; then
    echo "- iter $i: VERIFIED" >> "$LEDGER"; exit 0
  fi
  cur="$(snapshot)"
  echo "- iter $i: not verified; diff: ${cur:-none}" >> "$LEDGER"
  if [ "$cur" = "$prev" ]; then
    echo "- iter $i: NO PROGRESS, aborting" >> "$LEDGER"; exit 3
  fi
  prev="$cur"
done
echo "- cap $MAX_ITER exhausted" >> "$LEDGER"; exit 2
```

## Template: Evaluator-Optimizer / Writer-Critic (bash)

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

Caution: a model critic is a soft verifier. Prefer a deterministic check when one exists; when only a rubric critic is possible, keep `MAX_ROUNDS` low and hand the cap-exhausted case to a human — consensus pressure can amplify shared error (`04-agent/workflow-recipes.md` Looper Topologies caution).

## Template: Task-Ledger Backlog Loop (bash, ralph-style)

```bash
#!/usr/bin/env bash
set -euo pipefail
AGENT_CMD="${AGENT_CMD:-claude -p}"
TASKS="${TASKS:-TASKS.md}"               # one task per line; agent-editable is forbidden
VERIFY="${VERIFY:-./checks/verify.sh}"
MAX_ITER="${MAX_ITER:-20}"
STATE="${STATE:-./state}"; mkdir -p "$STATE"

for i in $(seq 1 "$MAX_ITER"); do
  task="$(grep -m1 -v '^[[:space:]]*$' "$TASKS" || true)"
  [ -z "$task" ] && { echo "backlog empty"; exit 0; }

  $AGENT_CMD "Complete exactly this one task, then stop: $task" \
    > "$STATE/task-$i-out.md" || true

  if "$VERIFY"; then
    # Script, not agent, retires the task line — the ledger stays trustworthy.
    tail -n +2 "$TASKS" > "$TASKS.tmp" && mv "$TASKS.tmp" "$TASKS"
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

1. Stub dry run with a scripted fake agent and a toggling verifier: prove all four exits (0/2/3/4) are reachable — success path, cap path, no-progress path, broken-verifier path as applicable.
2. `bash -n` the script; run `shellcheck` when available.
3. Confirm the verifier is committed, deterministic, and not writable by the loop body's allowed tools.
4. Report dry-run evidence with the deliverable.

## Prompt Sources

- `../../plans/agent-flow-control-research-2026-07-11.md`
- `../../04-agent/workflow-recipes.md`
- `../../04-agent/runtime-trust-boundary.md`
- `../../06-repo/AGENTS.md`
