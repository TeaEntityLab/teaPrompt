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
- planner output must be a list of 1..12 tasks or the run exits 2 before any worker starts; a worker that fails or returns no output aborts the run; merged deliverable: ./checks/verify-merged.sh state/final.md (the worker tally alone never passes)
## Human Review Boundary
- migration = AGENTS.md Human Review item: the generated script pauses before any apply step and records the approval; worker task text is model-authored data — never run as shell, never allowed to change AGENT_CMD, permissions, or the verifier
## Verification
- Rig-tier (run 2026-09-14): stub planner returning prose → exit 2 with zero workers started; 13 tasks → exit 2; one raising worker → exit 1; fenced JSON plan accepted; failing verify-merged.sh → exit 2; worker id `b/../evil` written as `worker-bevil.md`. Not proof of migration safety.
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
- cycle or dangling dependency → exit 4 before any node runs; a node that fails or returns no output counts as failed; strict (any failed node → exit 2) or quorum MIN_OK, which also requires the sink node done in this run (a stale sink file from a prior run never passes); sink node checked by ./checks/verify-merged.sh
## Escalation note
- regenerate from the template when the node set changes; never patch a drifted copy (plans/agent-flow-control-research-2026-07-11.md P12)
## Verification
- Rig-tier (run 2026-09-14; sink case re-run 2026-09-16): injected cycle and dangling dependency each exit 4 with zero nodes run; one failing node exits 2 under strict and under MIN_OK=3; a node exiting 0 with zero bytes exits 2; a failing sink under MIN_OK=3 exits 2 even when a prior run's sink file is present; failing sink gate exits 2; happy path exits 0. Not proof the generated code is correct.
```
