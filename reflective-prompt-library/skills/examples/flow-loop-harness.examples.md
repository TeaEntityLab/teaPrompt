# `flow-loop-harness` Examples

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
- check() wrapper (exit 4 when verifier broken), git+untracked progress signal,
  ledger tail fed to each fresh iteration, exits 0/2/3/4
## Human review boundary
- attended run: verifier + caps reviewed; unattended: full approval recorded first
## Verification
- Rig-tier only: stub dry run proves all four exits: toggling verifier (0), always-fail (2), no-progress stub (3), chmod -x verifier (4). This approves loop control flow, not production or host-enforcement e2e.

```

## Example 2

Input:

```text
Ralph through TASKS.md one item at a time; tests must pass after each task.
```

Expected output shape:

```markdown
## Loop
- Task-ledger backlog loop over state/TASKS.canon (canonical copy; the agent
  cannot reorder the queue), grep -n line dispatch, sed exact-line retirement
## Stop conditions
- backlog empty → 0; MAX_ITER=20 → 2; verify fail → 3; broken verifier → 4
## Escalation note
- no objective verifier for a task → keep human in the loop (reflective-brief)
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
- floor_ok(): non-empty draft, no TODO/TBD/PLACEHOLDER, ./checks/links-resolve.sh passes; ACCEPT releases only when the critic contract AND the floor both hold
## Stop conditions
- ACCEPT + floor → 0; MAX_ROUNDS exhausted → 2 (human decides; the last draft is not the result)
## Human review boundary
- unattended: rubric file excluded from the writer's write set (host permission mode); approval of verifier, caps, and blast radius recorded before the first run
## Verification
- Rig-tier (run 2026-09-14): ACCEPT + clean draft → 0; ACCEPT + draft containing TODO → 2; ACCEPT + zero-byte draft → 2; ACCEPT + failing links-resolve.sh → 2; fix list for four rounds → 2; critique "I cannot ACCEPT this" → 2 (whole-verdict match). Not proof the rubric judges well.
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
- branch failure tally per wave (all failed → exit 3), one bounded summary.md compacts each wave for the next, progress signal hashes branch outputs (never the wave header), exits 0/2/3/4
## Stop conditions
- converged → 0; MAX_WAVES exhausted → 2; branch outputs identical to the previous wave → 3; missing verifier or wave prompts → 4
## Human review boundary
- attended: verifier + caps; unattended: full approval recorded first; any branch step on the AGENTS.md Human Review list keeps a per-action pause
## Verification
- Rig-tier (run 2026-09-14): converge on the third check → 0; never converge → 2 at MAX_WAVES; identical branch outputs across waves → 3; all branches fail → 3; verifier not executable → 4; no wave prompts → 4. Not a claim about reviewer quality.
```
