# `flow-control-generator` Examples

## Example 1

Input:

```text
Script this for me: spec agent, then implementer, then reviewer, each feeding the next, using claude -p.
```

Expected output shape:

```markdown
## Topology
- Sequential pipeline (fixed known stages)
## Deliverable
- pipeline.sh (Script Contract: AGENT_CMD header, state/ dir, run_agent fn,
  gates after each stage, caps, permission flags, flow.log)
- prompts/01-spec.md, 02-implement.md, 03-review.md
## Gates
- stage 1: test -s state/01-spec.md; stage 2: ./checks/run-tests.sh; stage 3: gate: none (accepted)
## Verification
- stub dry run with AGENT_CMD='cat' → exit 0, three state files; bash -n clean
```

## Example 2

Input:

```text
Fan out one agent per module doc, then merge the summaries. Keep it to 4 at a time.
```

Expected output shape:

```markdown
## Topology
- Parallel fan-out/fan-in, MAX_JOBS=4, per-pid wave waits, synthesis step
## Verification
- stub dry run: 5 stub prompts, one forced failure → run aborts non-zero; happy path exit 0
## Escalation note
- "until every module passes lint" would be a loop → flow-loop-harness
```
