# Master Roadmap Index of Surveyed Plans — 2026-10-13

Language: English

> **Status: master planning index (record-only; non-authoritative).** Unified entry point indexing all six domain roadmaps derived from the surveyed-plan corpus. Establishes the relationship to [whole-project-roadmap-2026-07-11.md](whole-project-roadmap-2026-07-11.md) and incorporates parallel Socratic critical thinking findings. No new runtime or core skill is adopted by this record.

## Purpose

Provide a single navigation index across the six domain roadmaps established on 2026-10-13. The domain files own their planning summaries; the cited decisions own adoption, triggers and authority. [whole-project-roadmap-2026-07-11.md](whole-project-roadmap-2026-07-11.md) remains the scheduling companion, and [surveyed-plans-unified-roadmaps-2026-10-13.md](surveyed-plans-unified-roadmaps-2026-10-13.md) preserves the point-in-time synthesis and review trail. None supersedes an owning decision.

## Evidence vs Inference

- **Observed Repository Evidence:** Survey records in `reflective-prompt-library/plans/` cited per domain below (each domain roadmap's evidence base cites its source records by name), 1,743 passing tests in `plans/tests/` (verified 2026-10-13), and verified checkpoint receipts through 2026-10-11.
- **Author-Claimed Evidence:** Upstream research papers, vendor documentation snapshots, and un-reproduced benchmark scores.
- **[INFERENCE]:** Horizon sequencing, cross-domain dependency mapping, and projected ecosystem convergence dates.

## Relationship to Whole-Project Roadmap (2026-07-11)

[whole-project-roadmap-2026-07-11.md](whole-project-roadmap-2026-07-11.md) established the four-horizon scheduling discipline for TeaPrompt. This 2026-10-13 Master Index extends and deepens that structure by:
1. Confirming the successful execution of **Horizon 2 (2026-10-11 Checkpoint)** as recorded in [checkpoint-2026-10-11-outcome.md](checkpoint-2026-10-11-outcome.md).
2. Decomposing the general roadmap into six granular, domain-specific roadmaps grounded in the subsequent surveyed plan corpus.
3. Recording eight selected safeguards from the two-round parallel Socratic review: four existing policy boundaries and four record-only proposal groups, not eight newly adopted mechanisms.

## Domain Roadmaps Index

| Domain | Document | Scope & Survey Basis |
|---|---|---|
| **I. Harness & Flow Control** | [roadmap-harness-flow-control-2026-10-13.md](roadmap-harness-flow-control-2026-10-13.md) | Agentflow (8.2–8.4.1), Heddle (`80dccf2`), 3xA, Superpowers, OmO, Prime Agent, Two-Pack Flow Control, Stop-hooks, Conductor DAG, Quorum gates |
| **II. Execution Assurance** | [roadmap-execution-assurance-2026-10-13.md](roadmap-execution-assurance-2026-10-13.md) | AEAT-1..6, Hotline verification redundancy, Coordinate Codex Tasks, LLM judge lifecycle, GPT Instruct, Dogfooding Stage-1/2, Join validation, Blinded eval, Golden runner |
| **III. Governed Autonomy** | [roadmap-governed-autonomy-2026-10-13.md](roadmap-governed-autonomy-2026-10-13.md) | Governed delivery, Agent governance scaffold, Four Powers, Ultra vires nullification, Epoch fencing, Preflight controls, Stop That Shit, Product runtime ownership |
| **IV. Prompt & Context Architecture** | [roadmap-prompt-cognition-memory-2026-10-13.md](roadmap-prompt-cognition-memory-2026-10-13.md) | Seven prompt categories, Procedure layer defense, System prompt leaks, Semantica, Astra efficiency rules, Claude Code system prompts, MiniMax trace maps, Handover docs, Pstack |
| **V. Software Factory & DevOps** | [roadmap-software-factory-devops-2026-10-13.md](roadmap-software-factory-devops-2026-10-13.md) | Autonomous software factory recipe, SDLC inner/outer loop, Agentic DevOps trends, MGD form theory, Graph engineering, Dream-RSI, RSIAgent, Mutation testing floors |
| **VI. Ecosystem Packaging** | [roadmap-ecosystem-packaging-2026-10-13.md](roadmap-ecosystem-packaging-2026-10-13.md) | TEMPLATES/ARTIFACTS packaging, Multi-host distribution (Claude/Codex/Cursor/OMP), Matt Pocock skills v1.3.1, Managed skills boundary, Bilingual cheatsheet parity (T2) |

## Parallel Socratic Critical Thinking Consensus

Seven Socratic reviewer lenses across two parallel rounds evaluated the survey corpus and the resulting roadmap drafts. All lenses ran on the same worker family — under JD-1a this is a single epistemic channel, not independent agreement:
- **Round 1 (Domain Scope):** `SocraticHarnessLens`, `SocraticAssuranceLens`, `SocraticGovernanceLens`, `SocraticPromptCognitionLens`
- **Round 2 (Roadmap Drafts):** `ScoutRoadmapIntegrityLens`, `ScoutSocraticBoundaryChallenger`, `ScoutMinimalityGovernanceLens`

### Consensus Verdict: AGREE WITH CHANGES (single-channel consensus)
The recorded seven-lens verdict was conditional on distinguishing policy from host enforcement and proposals from adoptions. The selected topics below are not an exhaustive count of domain-ledger candidates; each linked row owns its status and reconsideration condition.

| Safeguard | Status | Owning domain-ledger row |
|---|---|---|
| 1. Host-counted loop termination | Proposed (record-only) | [HF-03](roadmap-harness-flow-control-2026-10-13.md#candidate-adoption-ledger) |
| 2. Vacuous-join disclosure | Adopted (existing disclosure) | [EA-05](roadmap-execution-assurance-2026-10-13.md#candidate-adoption-ledger) |
| 3. Blinding-limits disclosure | Adopted (existing disclosure) | [EA-06](roadmap-execution-assurance-2026-10-13.md#candidate-adoption-ledger) |
| 4. Broker-exhaustiveness boundary | Adopted (existing disclosure) | [GA-03](roadmap-governed-autonomy-2026-10-13.md#candidate-adoption-ledger) |
| 5. Stop-hook fail-open / fail-closed disclosure | Proposed (record-only) | [HF-04](roadmap-harness-flow-control-2026-10-13.md#candidate-adoption-ledger), [GA-05](roadmap-governed-autonomy-2026-10-13.md#candidate-adoption-ledger) |
| 6. Post-compaction non-goal reassertion | Proposed (record-only) | [PC-02](roadmap-prompt-cognition-memory-2026-10-13.md#candidate-adoption-ledger) |
| 7. Field-integrity limits | Adopted (existing disclosure) | [PC-03](roadmap-prompt-cognition-memory-2026-10-13.md#candidate-adoption-ledger) |
| 8. Factory title boundary cue | Proposed (record-only) | [SF-03](roadmap-software-factory-devops-2026-10-13.md#candidate-adoption-ledger) |

Other candidates remain in their domain ledgers, including the existing GA-04 preflight-coherence boundary and proposed SF-04 oracle-legibility caveat. Grouped navigation neither merges their conditions nor grants implementation authority.

## Consolidated Scheduling Horizons

### Horizon 1 — Standing Cadence (Continuous)
- Automated linting, link validation, and record hygiene (`validate_links.py`, `lint_skills.py`, `validate_governance.py`, `validate_record_hygiene.py`).
- Re-run `ROUTE-001`, `ROUTE-002`, and `ROUTE-003` against their existing fixture thresholds. The recorded 100% consistency is bounded fixture evidence, not a new universal routing gate.

### Horizon 2 — Source-Bound Next Review
- **P6 (2027-01-11):** The [checkpoint outcome](checkpoint-2026-10-11-outcome.md#p6-outcome) schedules the next standalone-generation evidence review for the two flow packs.
- **T2:** The [owning parity decision](checkpoint-2026-10-11-outcome.md#t2-decision) calls for a registry/appendix-change check, or the January 11 evidence review if unchanged; parity follows the live registry, not a permanently frozen eleven-bullet count.
- **F4 and dormant-queue review:** Preserve the existing source-refresh and event-review duties in the [scheduling companion](whole-project-roadmap-2026-07-11.md). This record assigns neither a new recurring calendar nor a blanket next date to unrelated candidates.
- **Additional audit ideas:** EA-07 (scorer/fixtures), PC-05 (prompt/references), UR-04 (memory provenance) and SF-05 (host/CI compatibility) are unscheduled proposals in their owning roadmap ledgers. R6 retains its separate event condition; none borrows P6's date as implementation authority.

### Horizon 3 — Trigger-Gated Queue (Active Watch)
- Queue entries preserve their owning conditions: E2's complaint/navigation event; AEAT-4's authorized named-product binding gap; I-1's same-class writer/effect recurrence; A-5's own viewer/source case and smaller-alternative failure; GD-16's named qualified host; SFR-4's verified holdout failure. A fired review condition is not automatic adoption, model dispatch or destructive-action permission.

### Horizon 4 — Direction-Gated Non-Goals
- Standing Non-Goals remain invariant: no TeaPrompt runtime, no tenth core skill, no full SKILL.md translation, no CI LLM benchmarks, no false runtime guarantees.

## Falsifiability

This master index is falsified if:
1. Any indexed domain roadmap fails repository record hygiene or contains broken links.
2. A source-bound review date or event condition is silently changed, or the P6/T2 reviews above pass their owning checkpoint without a recorded disposition.
3. A dormant item is adopted into the codebase without its triggering condition being documented in a candidate adoption ledger.

## Candidate Adoption Ledger

| ID | Candidate / Mechanism | Status | Evidence / Surface | Next Action / Trigger |
|---|---|---|---|---|
| MR-01 | Domain Roadmap Decomposition | Recorded | 6 domain roadmap files | Maintained as active planning reference |
| MR-02 | Navigation for selected safeguards 1–8 | Recorded | Status table above; linked domain-ledger rows own the individual Adopted / Proposed dispositions | Reconcile when an owning row changes; no adoption by this summary |
| MR-03 | P6 next review and conditional T2 check | Scheduled | [P6](checkpoint-2026-10-11-outcome.md#p6-outcome), [T2](checkpoint-2026-10-11-outcome.md#t2-decision) | P6 on 2027-01-11; T2 on registry/appendix change or that review if unchanged |
