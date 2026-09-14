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
## Gates
- Branch quorum: explicit `MIN_OK` or strict (`FAILED=0`, at least one non-empty output); merged deliverable: `./checks/verify-merged.sh state/final.md`
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


## Example 4

Input:

```text
Let a planner agent split this migration into tasks and hand them to worker agents, then merge.
```

Expected output shape:

```markdown
## Topology
- Orchestrator-workers (Python, stdlib): planner emits a JSON task list (fenced JSON stripped, must parse as a list), MAX_WORKERS=4 / MAX_TASKS=12 budget caps, worker ids sanitized to [A-Za-z0-9-_]
## Gates
- planner output must be a list or the run exits 2 before any worker starts; any worker exception aborts; merged deliverable: ./checks/verify-merged.sh state/final.md (the worker tally alone never passes)
## Human Review Boundary
- migration = AGENTS.md Human Review item: the generated script stops before any apply step; workers get read-only plus a scratch dir
## Verification
- Rig-tier only: stub planner returning prose (not a list) → exit 2; one raising worker → non-zero; happy path → verify-merged.sh runs. Not proof of migration safety.
```

## Example 5

Input:

```text
Spec first, then API and client in parallel, then integration tests only after both — as a script.
```

Expected output shape:

```markdown
## Topology
- DAG executor (Python, stdlib): nodes spec → {api, client} → integration; topological order with bounded concurrency MAX_WORKERS=4; each node's prompt receives its dependencies' outputs
## Gates
- cycle or dangling dependency → exit 4 before any node runs; per-node gate on output presence; quorum MIN_OK or strict (any failed node → exit 2); sink node checked by ./checks/verify-merged.sh
## Escalation note
- regenerate from the template when the node set changes; never patch a drifted copy (plans/agent-flow-control-research-2026-07-11.md P12)
## Verification
- Rig-tier only: a stub DAG with an injected cycle exits 4; one failing stub node exits 2 under strict; happy path reaches the merged gate. Not proof the generated code is correct.
```
