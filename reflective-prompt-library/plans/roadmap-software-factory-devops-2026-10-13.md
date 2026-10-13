# Autonomous Software Factory and Agentic DevOps Roadmap — 2026-10-13

Language: English

> **Status: active domain roadmap (record-only; non-authoritative).** Scheduling and architectural companion derived from autonomous software factory, SDLC inner/outer loop, agentic DevOps, and recursive self-improvement surveys. Preserves standing non-goals, host-enforced oracle sealing, and mutation testing floors. No new runtime or core skill is adopted by this record.

## Purpose

Establish a comprehensive, evidence-based roadmap for the Autonomous Software Factory, SDLC Inner/Outer-Loop Architecture, CI/CD Agentic Workflows, and Recursive Self-Improvement Loops, synthesizing evidence across 12+ surveyed plans.

## Evidence vs Inference

- **Observed Repository Evidence:** Pinned sources, workflow recipes, and panel records in `software-factory-rethink-panel-record-2026-09-28.md`, `software-factory-sdlc-inner-outer-loop-survey-2026-09-28.md`, `devops-agentic-trends-survey-2026-09-28.md`, `mgd-form-theory-survey-2026-10-02.md`, `dream-rsi-survey-2026-09-18.md`, and `rsiagent-survey-2026-09-16.md`.
- **Author-Claimed Evidence:** Upstream observational metrics regarding pull request review times (Faros AI Engineering Report 2026: +441.5% median PR-review time, +242.7% incidents per PR — observational within-company/within-team design, not causal; primary report checked 2026-10-02 per `devops-agentic-trends-survey-2026-09-28.md`), automated throughput claims, and self-improvement benchmark scores.
- **[INFERENCE]:** Projections of full-lifecycle autonomous development pipelines, automated mutation test generation, and multi-repo orchestration.

## Surveyed Plans Corpus

This roadmap derives directly from the following surveyed plans:
- `software-factory-rethink-panel-record-2026-09-28.md`
- `software-factory-sdlc-inner-outer-loop-survey-2026-09-28.md`
- `devops-agentic-trends-survey-2026-09-28.md`
- `mgd-form-theory-survey-2026-10-02.md`
- `graph-engineering-synthesis-survey-2026-09-16.md`
- `dream-rsi-survey-2026-09-18.md`
- `rsiagent-survey-2026-09-16.md`
- `rrsi-survey-2026-09-30.md`
- `decision-model-survey-2026-09-18.md`
- `gliner2-survey-2026-09-19.md`
- `nimble-survey-2026-09-19.md`
- `code-recall-survey-2026-08-20.md`
- `dilinai-nuwa-jiyao-survey-2026-07-13.md`
- `fable-method-survey-2026-07-16.md`

## Software Factory Architecture

The reference design distinguishes two cycles; TeaPrompt supplies workflow contracts, not an operating factory:
1. **The Inner Loop (Developer / Agent Interaction):**
   - Rapid code iteration, syntax diagnostics, local unit testing, and immediate feedback.
   - Guarded by `02-engineering/local-feedback.md` and tight test-driven cycles.
2. **The Outer Loop (Factory Orchestration & Release):**
   - Specification derivation (`intent.md` -> `spec.md` -> `criteria.yaml`).
   - Sealed Oracle Generation: Deterministic acceptance test suites sealed by host infrastructure.
   - Mutation Probes: Host-run checks report sensitivity to the injected faults, not general correctness. The surveyed blueprint's `min_kill_rate: 0.85` is an illustrative value, not a validated or installed operational floor.
   - Independent Verifier Channel: Multi-method, decorrelated verification runs outside the worker context.
   - Human Release Gate: Mandatory human review and business acceptance sign-off.

### Factory Realism & Disclaimers
"Autonomous Software Factory" names a workflow recipe, not a TeaPrompt runtime. The installed recipe already assigns process execution, containment, credentials and oracle sealing to host infrastructure and reserves intent/acceptance for humans. Protected-oracle and acceptance evidence must come from those owners, not prompt claims.

## Horizon Milestones

### Horizon 1 — Standing Invariants & Shipped Recipes
- **Factory Recipe:** Documented in `04-agent/workflow-recipes.md` §Autonomous Software Factory.
- **Factory Title Cue** *(proposed; record-only)*: Make the already-installed host-boundary/intent/acceptance clauses easier to discover beside the recipe title. The substantive boundary is present in `workflow-recipes.md` Factory Composition Rules; this is placement hardening, not missing enforcement or a new guarantee.
- **Oracle-Legibility Caveat** *(proposed; record-only)*: Consider a separate disclosure that a read-only but readable oracle can permit lookup-table/property overfitting. The caveat is not adopted here, and no secrecy/anti-gaming guarantee follows from write protection.
- **Deterministic Companion Floor:** Writer-critic templates offer a deterministic syntax/schema companion check raising the ACCEPT floor (catches malformed drafts, not plausible errors — advisory tier), and bounded loops carry no-progress exits. Semantic cross-round oscillation remains unmitigated (RS-9).

### Horizon 2 — Review Proposal (Unscheduled)
- **DevOps Integration Review** *(proposed; record-only)*: Consider recipe compatibility review on a named host/CI integration change or explicit owner assignment; P6's January 11 evidence date does not schedule this audit.

### Horizon 3 — Trigger-Gated Queue
- **SFR-4 Software Factory Routing Holdout:** A verified factory-plan → minimality holdout failure reopens routing assessment. Fixture the observed boundary before any tune and retain R8's pre-tune checks; the trigger alone does not authorize a keyword change.
- **RS-9 Writer-Critic Prior Verdict Context:** An observed cross-round oscillation in a TeaPrompt-run writer-critic loop reopens the [owning RS-9 review](rsiagent-survey-2026-09-16.md#candidate-adoption-ledger). It does not automatically install prior-round context; the current deterministic floor/cap is not a semantic anti-oscillation proof.

### Horizon 4 — Direction-Gated Non-Goals
- No TeaPrompt-owned CI runner, compiler daemon, or container manager.
- Never claim autonomous software factories eliminate human code review or provably prevent defect introduction without external mutation tests and human sign-off.

## Falsifiability

This planning summary is wrong or stale if:
1. A generated workflow reports `enforcement-proven` or acceptance from prompt text, artifact presence or developer tests without the named host/human evidence.
2. The illustrative mutation value or code coverage is cited as a guarantee against semantic specification errors or readable-oracle overfitting.
3. A reported factory→minimality holdout failure or TeaPrompt-run writer-critic oscillation is ignored, or a review trigger is treated as automatic router/template adoption.

## Candidate Adoption Ledger

| ID | Candidate / Mechanism | Status | Evidence / Surface | Next Action / Trigger |
|---|---|---|---|---|
| SF-01 | Autonomous Software Factory Recipe | Adopted | `04-agent/workflow-recipes.md` | None |
| SF-02 | Cheatsheet Factory In-Place Cue | Adopted | `skills/SKILL_TRIGGER_CHEATSHEET.md` | None |
| SF-03 | Factory Title Boundary Cue | Proposed (Record-only in this roadmap) | Existing recipe enforcement/intent/acceptance clauses in `04-agent/workflow-recipes.md`; title-placement proposal in Horizon 1 | Consider on a named recipe-discovery failure or explicit recipe review; no substantive boundary adoption |
| SF-04 | Oracle Legibility Overfitting Caveat | Proposed (Record-only in this roadmap) | This roadmap §Horizon 1 | Re-litigate upon next recipe review |
| SF-05 | Named Host/CI Compatibility Review | Proposed (Record-only in this roadmap) | Horizon 2 review idea; installed recipe host preconditions remain unchanged | Consider on a named integration change or owner assignment; no recurring date |
