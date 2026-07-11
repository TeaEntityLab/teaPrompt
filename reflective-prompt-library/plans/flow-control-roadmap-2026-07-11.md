# Flow-Control Roadmap — 2026-07-11

> **Status: active planning artifact (non-authoritative).** Domain roadmap for the
> flow-control capability (the two registered domain packs plus host-native flow
> features), extending the [whole-project roadmap](whole-project-roadmap-2026-07-11.md)
> with the [2026-07-11 survey](../../surveys/agent-skills-flow-control-survey-2026-07-11.md)
> deltas. Owning decisions stay in the
> [pack panel record](flow-control-pack-panel-record-2026-07-11.md) and
> [coverage panel record](flow-coverage-panel-record-2026-07-11.md); this file
> schedules their triggers and adds one new evaluation forced by the landscape
> change. No adoption or demotion is decided here.

## What changed today

The survey verified that host-native loop surfaces now exist in Claude Code:
`/goal` (condition loop, **model-judge** stop), `/loop` (interval re-run), Stop
hooks (**deterministic when script-backed**), `/batch` (worktree fan-out with
per-unit tests and PRs), bundled dynamic workflows, and out-of-session
schedulers (`/schedule` routines, scheduled tasks). The pack's demotion trigger
— "a host-native flow feature covering all pack templates with enforcement →
demote the loop skill first" — is now a live question instead of a hypothetical.

## F1 — Demotion-trigger evaluation for `flow-loop-harness` (Now; the new item)

Run a focused evaluation record (own ledger; human approval for any outcome
that edits pack surfaces). Seed analysis from the survey, to be tested not
assumed:

| Pack template | Nearest host-native surface | Coverage gap the evaluation must test |
| --- | --- | --- |
| Verify-gated fix loop | `/goal` + auto mode; Stop hook + script | `/goal`'s evaluator is a model judge over the transcript — fails the pack's deterministic-stop bar on its face; a script Stop hook is deterministic but unpackaged (no caps/ledger/no-progress detection out of the box) |
| Task-ledger backlog loop | `/goal` over a backlog file; `/batch` for parallelizable backlogs | `/batch` is one-shot decomposition, not a retire-line ledger loop; `/goal` inherits the model-judge caveat |
| Writer-critic rounds | `/goal` with critic-in-condition | Already the pack's advisory-tier gate; host offers no deterministic critic either |

Decision space (exactly one, recorded with evidence): (a) trigger **not fired**
— add a host-native cross-reference to the pack's Verification/Escalation prose
so users know when `/goal`/Stop hooks suffice; (b) trigger **partially fired** —
demote specific templates, keep the rest; (c) trigger **fired** — fold the loop
skill back into `workflow-recipes.md` per the recorded demotion path.
Evaluation must run the pack's own falsifier honestly: "host-native beats local
scripts" applies only where enforcement is at least as strong — a model judge is
not enforcement by TeaPrompt's verifier rule
([reflective-spec-plan](../skills/reflective-spec-plan/SKILL.md) Workflow Design
Mode; [runtime-trust-boundary](../04-agent/runtime-trust-boundary.md)).

Timing: before or at the 2026-10-11 checkpoint, so the P6 merge re-litigation
and this evaluation land on the same evidence base.

## F2 — Usage evidence for the 2026-10-11 checkpoint (Now)

Unchanged from the whole-project plan's T3: establish the manual usage-log
convention now; record the zero-state. Without it, P6 (merge) and F1 (demotion)
both re-litigate on `unknown`. One log serves both.

## F3 — Template evolution queue (trigger-gated; unchanged triggers, new context)

| Item | Trigger (owned by cited record) | New context from the survey |
| --- | --- | --- |
| P12 Conductor-style DAG executor | First local task needing dependency-gated fan-out beyond pipeline/parallel/orchestrator | `/batch` covers the *host-side* worktree fan-out case; a local task solved acceptably by `/batch` does **not** fire P12 — note this in the eventual evaluation |
| P13 multi-wave ReMoM template | Recurrence of real multi-wave runs | Composition note (parallel template inside loop harness) remains the answer until recurrence |
| Writer-critic deterministic companion | User demand for a non-model gate | Host offers none either; unchanged |
| P7 pack routing integration | Fresh ROUTE-002/003 holdout groups first | Holdout design pre-work now exists: [routing-holdout plan](routing-holdout-plan-2026-07-11.md) |

## F4 — Host-feature watch table (standing; re-check before reliance)

| Watch | Where | Fires what |
| --- | --- | --- |
| `/goal` gains tool-running / deterministic evaluation | code.claude.com goal docs | Re-run F1 — the model-judge caveat is the load-bearing fact |
| Stop-hook ecosystem ships packaged loop hygiene (caps, ledgers, no-progress) | Claude Code hooks docs/changelog | Re-run F1 template-by-template |
| Codex Record & Replay matures (skill-from-demonstration) | learn.chatgpt.com | Reference-note candidate for [workflow-acquisition](../04-agent/workflow-acquisition.md); M4's three-recurrence gate unchanged |
| Antigravity CLI replaces Gemini CLI (free tier) | geminicli.com banner | SKILL_INSTALLATION host-coverage check (S4 in the skills-surface plan) |
| AgentKit wind-down confirmation | OpenAI docs | Retire or confirm the `[search-derived]` note in both survey records |
| agentskills.io spec change (frontmatter table, allowed-tools) | agentskills.io/specification | Re-run S1 conformance before any migration work |

## Non-goals restated (pointers)

No TeaPrompt-owned runtime, recorder, replay engine, or side-effect enforcer;
no third pack without the [AGENTS item-3 admission rule](../06-repo/AGENTS.md#harness-policy-nine-skills);
no pack trigger phrases in the core router before P7's holdouts
([Standing Non-Goals](../PROJECT_KNOWLEDGE.md#standing-non-goals)).

## Falsifiability

This roadmap is stale if: F1 has no record by the 2026-10-11 checkpoint; a
watch-table row fires without its named follow-up; or a pack surface changes
without a ledger row. Wrong if the survey's `/goal` characterization is
contradicted by the primary docs it cites (then F1's seed analysis must be
rebuilt, not patched).
