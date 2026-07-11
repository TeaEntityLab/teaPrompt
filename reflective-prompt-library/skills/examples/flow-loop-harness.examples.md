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
- stub dry run proves all four exits: toggling verifier (0), always-fail (2),
  no-progress stub (3), chmod -x verifier (4)
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
