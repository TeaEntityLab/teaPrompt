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
- Rig-tier only: stub dry run with AGENT_CMD='cat' → exit 0, three state files; bash -n clean. This approves control flow, not production or side-effectful execution.
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
- Rig-tier only: stub dry run: 5 stub prompts, one forced failure → run aborts non-zero; happy path exit 0. This is not host-enforcement or production e2e proof.
## Escalation note
- "until every module passes lint" would be a loop → flow-loop-harness
```

## Example 3

Input:

```text
Generate a deployment pipeline that builds, runs tests, then deploys if approved.
```

Expected output shape:

```markdown
## Topology
- Sequential pipeline: build -> test -> human approval pause -> deploy
## Human Review Boundary
- deploy is production/third-party effect; generated script exits before deploy unless approval record path is supplied and non-empty
## Gates
- build: deterministic build exit 0; test: ./checks/run-tests.sh; deploy: named human approval + explicit operator command
## Verification
- Rig-tier only: AGENT_CMD='cat' dry run exercises build/test/approval-missing path and exits non-zero before deploy; bash -n clean. No production e2e proof is claimed.
```

