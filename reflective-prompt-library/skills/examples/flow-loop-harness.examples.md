# `flow-loop-harness` Examples

Illustrative output shapes, not new execution evidence. Dated rig results below are historical, not verification of the 2026-10-01 repairs. Every generated loop carries the shared selected-preflight gate: `PREFLIGHT` names one executable pathname (never shell text); empty preserves the attended example below and claims no runtime enforcement, and a workflow requiring observed host preconditions names its gate in the run note. When set, the gate is checked before each agent dispatch and after that dispatch before acceptance/publication/retirement — including the zero-call already-done path — with per-stage capture under `$STATE/preflight-<stage>.out`; failure exits 4 and is never a tolerable branch failure under partial multi-wave policy. Gate output is point-in-time evidence, never enforcement proof; no cancellation manager is added (driver SIGTERM can leave an in-flight child alive; examine the process group).

## Example 1

Input:

```text
Keep running claude on this repo until the test suite passes. Cap it sensibly.
```

Expected output shape:

```markdown
## Loop
- Verify-gated fix loop: VERIFY=./checks/verify.sh (truth layer), MAX_ITER=8
## Anatomy
- check() wrapper (exit 4 when verifier broken), staged+unstaged binary diffs
  and untracked content checksums excluding STATE (including logs/probes),
  bounded ledger tail per fresh iteration, exits 0/2/3/4; shared `PREFLIGHT` gate
  before each dispatch and after it before acceptance, including the zero-call
  already-verified path (selected failure → 4)
- Equal-churn content changes continue; unchanged git workspace halts.
  Outside git progress detection is explicitly disabled: rely on caps,
  never infer workspace stall from constant verifier diagnostics.
## Human review boundary
- attended: verifier + caps; unattended: full approval first, including host exclusion of checks/ from agent writes
## Verification
- Rig-tier only proposed checks (unrun here): toggling verifier (0), changing agent + always-fail verifier (2), no-op agent with STATE inside an un-ignored worktree (3), non-executable verifier before any call (4). Rig control flow is not production or host-enforcement proof.

## Run note
- stop condition, iteration cap, budget caps, resume command (`rerun the generated script`), human-approval boundary; prompt file(s), verifier hook, inspectable `state/ledger.md`

```

## Example 2

Input:

```text
Ralph through TASKS.md one item at a time; tests must pass after each task.
```

Expected output shape:

```markdown
## Loop
- Task-ledger backlog loop over state/TASKS.canon (canonical copy), grep -n
  dispatch, sed exact-line retirement. The agent cannot reorder this queue
  only when the host excludes state/TASKS.canon from agent writes.
## Host boundary
- Exclude canonical tasks and checks/; exclude prompts/critic-rubric.md
  if composed with writer-critic. Copying a backlog supplies no protection.
  Content progress excludes STATE; outside git the change check is disabled.
## Stop conditions
- backlog empty → 0; MAX_ITER=20 → 2; verify fail or unchanged workspace after a task → 3 (a green global verifier does not retire untouched work; an already-satisfied or interrupted task halts here too — confirm it, delete its line from state/TASKS.canon, rerun); broken verifier or missing TASKS.canon → 4; selected-preflight failure before dispatch/retirement → 4
## Escalation note
- no objective verifier for a task → keep human in the loop (reflective-brief)
## Human review boundary
- attended: verifier + caps; unattended: recorded approval of verifier, caps, flags, blast radius before the first run

```

## Example 3

Input:

```text
Have one agent draft the release notes and another critique them until they're good. Run it overnight.
```

Expected output shape:

```markdown
## Loop
- Writer-critic (evaluator-optimizer): MAX_ROUNDS=4; critic is rubric-bound and must return the single word ACCEPT or a numbered fix list
## Deterministic companion floor (required: "overnight" = unattended)
- Insert FLOOR executable preflight and floor_ok() at UNATTENDED PREFLIGHT, before draft dispatch; missing/non-executable floor → 4 with zero agent calls.
- Replace the entire bare ACCEPT if block with ACCEPT && floor_ok(): non-empty draft, no TODO/TBD/PLACEHOLDER, reviewed links-resolve.sh passes.
## Stop conditions
- ACCEPT + floor → 0; MAX_ROUNDS exhausted → 2 (human decides; the last draft is not the result); selected `PREFLIGHT` failure before dispatch/publication → 4
## Human review boundary
- unattended: host excludes checks/ and prompts/critic-rubric.md from agent writes; recorded approval of verifier/floor, caps, flags and blast radius before the first run
## Verification
- Rig-tier (run 2026-09-14): ACCEPT + clean draft → 0; ACCEPT + draft containing TODO → 2; ACCEPT + zero-byte draft → 2; ACCEPT + failing links-resolve.sh → 2; fix list for four rounds → 2; critique "I cannot ACCEPT this" → 2 (whole-verdict match). Not proof the rubric judges well.
- Repair acceptance checks (unrun here): missing and non-executable FLOOR → 4 before draft; present passing FLOOR + clean ACCEPT → 0. The historical run above did not exercise executable preflight.
```

## Example 4

Input:

```text
Fan out five reviewers each round and re-run with a merged summary until the converge check passes.
```

Expected output shape:

```markdown
## Loop
- Multi-wave fan-out: MAX_WAVES=4; VERIFY=./checks/converged.sh (truth layer); per-wave branch prompts under prompts/wave/*.md
## Anatomy
- Preserve resume ledger, clear prior-run branch outputs/summary/final, count failed or zero-byte branches before compaction (all failed/empty → 3). Only successful nonempty current-wave outputs enter summary/checksum/final; one bounded summary feeds the next wave. Hash output content, never the wave header; exits 0/2/3/4. Selected-preflight failure in any branch propagates as exit 4, never a tolerable branch failure.
## Stop conditions
- converged → 0; MAX_WAVES exhausted → 2; branch outputs identical to the previous wave → 3; missing verifier or wave prompts → 4; selected preflight → 4 before dispatch and before convergence publish
## Human review boundary
- attended: verifier + caps; unattended: full approval first, including host checks/ write exclusion; Human Review actions retain per-action pauses
## Verification
- Rig-tier (run 2026-09-14): converge on the third check → 0; never converge → 2 at MAX_WAVES; identical branch outputs across waves → 3; all branches fail → 3; verifier not executable → 4; no wave prompts → 4. Not a claim about reviewer quality.
- Repair acceptance checks (unrun here): reused STATE cannot import a deleted branch, old summary or final; failed/empty branch evidence is tallied and excluded. The historical run above did not prove those cases.
## Run note
- stop condition, wave cap, budget caps, resume command (`rerun the generated script`), human-approval boundary; prompt file(s), verifier hook, inspectable `state/ledger.md`

```
