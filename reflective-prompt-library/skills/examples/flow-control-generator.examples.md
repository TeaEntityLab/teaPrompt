# `flow-control-generator` Examples

Illustrative output shapes, not new execution evidence. Every generated script carries the shared selected-preflight gate: `PREFLIGHT` names one executable pathname (never shell text); empty preserves the attended example below and claims no runtime enforcement, and a workflow requiring observed host preconditions names its gate in the run note. When set, the gate is checked before each agent dispatch and after that dispatch before acceptance/publication, including zero-call already-done paths; failure exits 4 and is never swallowed by `MIN_OK`/partial policy. Gate output is point-in-time evidence, never enforcement proof; no cancellation manager is added. Every script also carries the repeated-failure discipline: on agent failure the driver appends a prompt-identity signature to `FAIL_SIGS` (default a driver-owned `state/../fail-signatures.jsonl`, rejected if configured inside worker-writable `STATE`); an identical redispatch exits 3 (`refuse-identical-retry`) — a hold never swallowed by quorum — unless a new `RETRY_REASON` names the changed strategy or corrected input; raw `<out>.failed-<exit>` receipts stay on disk. `AGENT_CMD` unset falls back to the documented example; explicitly empty or whitespace-only exits 4 before any dispatch.

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
  gates after each stage, caps, permission flags, flow.log, documented exits)
- prompts/01-spec.md, 02-implement.md, 03-review.md
## Gates
- stage 1: test -s state/01-spec.md; stage 2: ./checks/run-tests.sh; stage 3: gate: none (accepted); every dispatch carries the shared `PREFLIGHT` gate before and after (empty = attended, unchanged)
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
- Parallel fan-out/fan-in, MAX_JOBS=4 (canonical positive decimal validated before first dispatch and before any arithmetic evaluation; invalid `00`/`08`/empty/expression/overflow → 4 with zero dispatches), per-pid wave waits, synthesis step
## Gates
- Branch quorum: explicit `MIN_OK` or strict (`FAILED=0`, at least one non-empty output); `MIN_OK=0` is the zero-quorum spelling — zero survivors still run synthesis on a zero-survivor note and reach the merged gate; noncanonical quorum → 4; merged deliverable: `./checks/verify-merged.sh state/final.md`; selected-preflight failure and repeated-failure holds exit 4/3 under either policy
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
## Run note
- dry-run/run commands, state and log locations (`state/`, `flow.log`), budget caps, human approval required for the deploy step
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
- Orchestrator-workers (Python, stdlib): planner emits a JSON list, MAX_WORKERS=4 / MAX_TASKS=12; create parent STATE directories; send prompts via stdin, not argv
## Gates
- Validate every nonempty string id/task and unique nonempty sanitized output id
  before dispatch. Duplicate ids and sanitization collisions exit 2; no worker
  starts. Worker failure/empty output aborts; ./checks/verify-merged.sh checks final.
  Selected `PREFLIGHT` (fixed `[PREFLIGHT]` argv, no shell) gates every dispatch and the final publish; failure exits 4.
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
- cycle/dangling dependency or missing/nonterminal FINAL_NODE → exit 4 before any node runs.
  FINAL_NODE explicitly names the acceptance artifact; other terminal nodes and
  dictionary order cannot replace it. Strict or MIN_OK quorum both require that
  final node done in this run, then ./checks/verify-merged.sh checks its output.
  Selected-node `PREFLIGHT` failure is configuration (exit 4), never quorum-tolerable.
## Escalation note
- regenerate from the template when the node set changes; never patch a drifted copy (plans/agent-flow-control-research-2026-07-11.md P12)
## Verification
- Rig-tier (run 2026-09-14; sink case re-run 2026-09-16): injected cycle and dangling dependency each exit 4 with zero nodes run; one failing node exits 2 under strict and under MIN_OK=3; a node exiting 0 with zero bytes exits 2; a failing sink under MIN_OK=3 exits 2 even when a prior run's sink file is present; failing sink gate exits 2; happy path exits 0. Not proof the generated code is correct.
```
