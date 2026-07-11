# Flow-Loop-Harness Demotion-Trigger Evaluation — 2026-07-11

> **Status: decision record (user-approved execution, 2026-07-11).** First
> scheduled evaluation of the host-native demotion trigger recorded in
> [flow-control-pack-panel-record-2026-07-11.md](flow-control-pack-panel-record-2026-07-11.md)
> and [agent-flow-control-research-2026-07-11.md](agent-flow-control-research-2026-07-11.md)
> §Demotion Triggers, fulfilling T4/F1 of the
> [whole-project plan](whole-project-plan-2026-07-11.md) and
> [flow-control roadmap](flow-control-roadmap-2026-07-11.md). Evidence base:
> [2026-07-11 survey](../../surveys/agent-skills-flow-control-survey-2026-07-11.md)
> (primary docs: code.claude.com goal/commands/skills pages, read that session).

## Trigger under evaluation

> "A host-native flow feature (e.g., a first-party goal/loop mode) covering all
> pack templates **with enforcement** → demote the loop skill first (host-native
> beats local scripts)."

Both conditions must hold: (1) coverage of all pack templates, (2) enforcement
at least as strong as the pack's bar — a deterministic external verifier as the
only trusted stop condition, plus iteration/budget caps, no-progress detection,
and a resume convention.

## Template-by-template analysis

| Pack template | Host-native candidate | Coverage | Enforcement | Verdict |
| --- | --- | --- | --- | --- |
| Verify-gated fix loop | `/goal` + auto mode | Shape matches (work until condition) | **Fails the bar:** evaluator is a small fast model judging the transcript; "It does not call tools, so it can only judge what Claude has already surfaced." No hard iteration cap (turn bounds are condition prose, also model-judged) | Not covering |
| Verify-gated fix loop | Stop hook + script | Deterministic check ✓ | A primitive, not a packaged loop: no caps, no no-progress detection, no ledger/resume convention ship with it; user assembles those by hand — which is precisely what the pack generates | Not covering |
| Task-ledger backlog loop | `/goal` over a backlog; `/batch` | `/batch` is one-shot decomposition (5–30 units, worktrees, PRs), not an iterating retire-line ledger; `/goal` inherits the model-judge stop | Same gaps | Not covering |
| Writer-critic rounds | `/goal` with critic condition | The pack's own critic is already advisory-tier; host adds no deterministic critic either | No enforcement delta | Not covering |

## Decision

**Trigger NOT FIRED.** Neither coverage nor enforcement holds: the only
deterministic host primitive (script Stop hook) covers no template as a packaged
artifact, and the packaged host feature (`/goal`) uses exactly the stop-condition
class ("model judges its own done") that the pack exists to avoid — per the
verifier rule in [reflective-spec-plan](../skills/reflective-spec-plan/SKILL.md)
Workflow Design Mode and
[runtime-trust-boundary](../04-agent/runtime-trust-boundary.md).

Adopted action (option a from the roadmap's decision space): a short
**Host-Native Alternatives** note in `flow-loop-harness`'s body so users reach
for `/goal`/`/loop`/Stop hooks when those genuinely suffice, plus a dated
evaluation-status line in its Demotion Triggers section. No demotion, no merge,
no template change.

## Ledger

| Item | Status | Evidence | Next trigger |
| --- | --- | --- | --- |
| Host-native demotion trigger, first evaluation | **Not fired — 2026-07-11** | Survey primary docs; table above | Re-run when `/goal` gains tool-running/deterministic evaluation or Stop hooks ship packaged loop hygiene (watch table, [flow-control roadmap F4](flow-control-roadmap-2026-07-11.md)) |
| Host-Native Alternatives note in loop skill | Adopted 2026-07-11 | `skills/flow-loop-harness/SKILL.md` §Host-Native Alternatives | Keep one paragraph; expand only on user confusion evidence |
| Zero-invocation demotion trigger (separate) | Live, unaffected | [usage log](flow-pack-usage-log.md) | 2026-10-11 P6 review |

## Falsifiability

Wrong if the cited goal-mode docs described a tool-running or deterministic
evaluator on 2026-07-11, or if a packaged host loop artifact (caps + verifier
gate + ledger) existed in Claude Code at that date. Stale when any F4 watch row
fires; the re-run must rebuild the table from current primary docs, not patch
this one.
