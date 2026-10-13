# Harness Architecture and Flow-Control Roadmap — 2026-10-13

Language: English

> **Status: active domain roadmap (record-only; non-authoritative).** Scheduling and architectural companion derived from the flow-control and harness survey corpus. Preserves standing non-goals, host-enforcement boundaries, and the two-pack split (`flow-control-generator` and `flow-loop-harness`). No new runtime or core skill is adopted by this record.

## Purpose

Establish a comprehensive, evidence-based roadmap for Agent Harness Architecture, Flow Control, and Multi-Agent Orchestration, synthesizing evidence across 15+ surveyed plans.

## Evidence vs Inference

- **Observed Repository Evidence:** Pinned sources and execution receipts in `agentflow-survey-2026-09-05.md`, `agentflow-8.2-delta-survey-2026-09-13.md`, `agentflow-8.4.1-delta-survey-2026-09-30.md`, `heddle-source-survey-2026-10-12.md` (`80dccf2`, accessed 2026-10-12), `agent-flow-control-research-2026-07-11.md`, and `checkpoint-2026-10-11-outcome.md`.
- **Author-Claimed Evidence:** Upstream vendor claims regarding `/goal` tool execution, Stop-hook guarantees, and multi-agent framework speeds.
- **[INFERENCE]:** Projections of future host harness API evolutions and convergence timelines.

## Surveyed Plans Corpus

This roadmap derives directly from the following surveyed plans:
- `agentflow-survey-2026-09-05.md`
- `agentflow-8.2-delta-survey-2026-09-13.md`
- `agentflow-8.3-delta-survey-2026-09-21.md`
- `agentflow-8.3.2-delta-survey-2026-09-22.md`
- `agentflow-8.4.1-delta-survey-2026-09-30.md`
- `heddle-source-survey-2026-10-12.md`
- `agent-ecosystem-harness-survey-2026-10-11.md`
- `agent-harness-convergence-survey-2026-08-25.md`
- `3xa-harness-survey-2026-08-20.md`
- `oh-my-openagent-survey-2026-10-01.md`
- `superpowers-v6.4-adoption-2026-10-03.md`
- `prime-agent-survey-2026-08-06.md`
- `agent-flow-control-research-2026-07-11.md`
- `flow-coverage-panel-record-2026-07-11.md`
- `runtime-skills-experiments-2026-10-05.md`

## Architecture and Core Topologies

The surveyed reference vocabulary separates deterministic control flow from model-produced step content. The two packs specify host-run templates; host isolation, timeout supervision and effect containment are not supplied by prompt text.
1. **Sequential Pipeline:** Step-by-step linear chains with fail-closed exits.
2. **Parallel Fan-out / Fan-in:** Strict branch-success policy by default; `MIN_OK` selects an explicit partial-failure quorum, including a zero-quorum mode that still requires the merged-result gate.
3. **Conditional Routing:** Normalized route labels and route-trace logging, with the fail-closed/default-up choice explicit.
4. **Loop-Until-Verified:** Host-run scripts bound iterations; a hung individual tool call needs host timeout/cancellation supervision.
5. **Orchestrator-Workers:** Parent orchestration with explicit subtask contracts; process/filesystem isolation remains a host precondition.
6. **Baton-Passing / Handoff:** Sequential authority delegation with structured context transfer.

## Horizon Milestones

### Horizon 1 — Standing Invariants & Shipped Packs
- **Pack Separation:** Retain separate `flow-control-generator` (one-pass) and `flow-loop-harness` (bounded loops) packs per the 2026-10-11 P6 checkpoint closure.
- **Quorum Policy:** Parallel templates implement `MIN_OK` quorum checks where non-empty output does not equal correct output.
- **State Hygiene:** Loops use disposable `state/`, RESUMED restart stanzas, and tail compaction budgets.
- **Preflight:** P16 invokes a selected host-owned `PREFLIGHT` executable before dispatch and before result acceptance. An unset checker preserves an attended example, not proof that host preconditions are met.
- **Host-Counted Termination Invariant** *(proposed; record-only)*: Broader termination wording would require observed iteration/concurrency counters and host wall-clock supervision, including the single-call hang boundary; it is not a shipped end-to-end guarantee.
- **Stop-Hook Fail-Open Disclosure** *(proposed; record-only)*: Emitted loop documentation would disclose that host stop-hooks can fail open under contention; no shipped template carries this wording yet.

### Horizon 2 — Date-Gated Checkpoints
- **2027-01-11 P6 Review Checkpoint:** Review documented standalone-generation use under the [owning usage convention](checkpoint-2026-10-11-outcome.md#p6-outcome). A documented zero reopens consolidation evaluation; unavailable host usage remains `unknown`, not zero, and generation is not accepted delivery or efficacy.

### Horizon 3 — Trigger-Gated Queue
- **Native Loop Alternatives (F1 Watch):** Re-evaluate when `/goal` gains tool-running/deterministic evaluation **or** Stop hooks ship packaged loop hygiene, per the [owning trigger](flow-pack-demotion-evaluation-2026-07-11.md#ledger). Compare the affected template's caps, verifier gate, ledger, progress, backlog and wave behavior; a source update alone does not demote a pack.
- **Emitted Disconnect/Cancel Branching** *(proposed; host-dependent)*: Consider a generated-script branch only for a named host integration exposing authenticated cancellation signals. [OW-4](product-runtime-ownership-panel-2026-08-25.md#candidate-adoption-ledger) already separates observation loss from cancellation; that adopted contract is not reopened by this proposal.
- **DAG Conductor Native Primitive:** Re-evaluate the existing DAG template on a native host primitive, under the owning P12 condition; this does not authorize a TeaPrompt runtime.

### Horizon 4 — Direction-Gated Non-Goals
- No TeaPrompt-owned looper runtime, WAL engine, or async daemon. Emitted bash scripts run on host kernels.
- No prompt-only loop caps: iteration counters must bind to deterministic filesystem/process state.

## Falsifiability

This planning summary is wrong or stale if:
1. It describes an unset preflight or an iteration cap as proof of host containment or termination of a hung individual call.
2. Either F1 source trigger is observed but the affected-template comparison is omitted, or source-read evidence is reported as executed host equivalence.
3. The source-bound P6 review lacks a recorded disposition, or missing usage is converted to zero to force a merge.

## Candidate Adoption Ledger

| ID | Candidate / Mechanism | Status | Evidence / Surface | Next Action / Trigger |
|---|---|---|---|---|
| HF-01 | Separate Flow Packs Retained | Adopted | `checkpoint-2026-10-11-outcome.md` | Re-audit at 2027-01-11 checkpoint |
| HF-02 | Parallel `MIN_OK` Quorum Gate | Adopted | `skills/flow-control-generator/SKILL.md` | None |
| HF-03 | Host-Enforced Termination Invariant | Proposed (Record-only in this roadmap) | This roadmap §Horizon 1 | Re-litigate upon host looper integration |
| HF-04 | Stop-Hook Fail-Open Disclosure | Proposed (Record-only in this roadmap) | This roadmap §Horizon 1 | Re-litigate upon host looper integration |
