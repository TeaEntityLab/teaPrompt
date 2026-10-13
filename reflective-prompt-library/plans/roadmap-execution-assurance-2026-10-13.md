# Agent Execution Assurance, Verifier Ecosystem and Evaluation Roadmap — 2026-10-13

Language: English

> **Status: active domain roadmap (record-only; non-authoritative).** Scheduling and architectural companion derived from execution assurance, oracle verification, and evaluation survey records. Preserves standing non-goals, empirical limits of model-graded judges, and DFL-1–3 dogfooding lessons. No new runtime or core skill is adopted by this record.

## Purpose

Establish a comprehensive, evidence-based roadmap for Agent Execution Assurance, Verifiers, Acceptance-Join Validation, and Empirical Evaluation, synthesizing evidence across 10+ surveyed plans.

## Evidence vs Inference

- **Observed Repository Evidence:** Pinned sources, CLI suites, and test runs in `agent-execution-assurance-taxonomy-survey-2026-09-30.md`, `hotline-verification-redundancy-survey-2026-09-22.md`, `coordinate-codex-tasks-eval-survey-2026-09-30.md`, `llm-judge-lifecycle-survey-2026-09-05.md`, `gpt-instruct-survey-2026-09-10.md`, `skill-dogfood-test-plan-2026-10-08.md`, and `dogfood-learning-promotion-2026-10-09.md`.
- **Author-Claimed Evidence:** Upstream research benchmark numbers (arXiv:2608.18300v3, checked 2026-09-05), vendor evaluation reports, and scalar-only selection metrics.
- **[INFERENCE]:** Projections of evaluation harness scaling, synthetic oracle limitations, and cross-model judge drift patterns.

## Surveyed Plans Corpus

This roadmap derives directly from the following surveyed plans:
- `agent-execution-assurance-taxonomy-survey-2026-09-30.md` (AEAT-1..6)
- `hotline-verification-redundancy-survey-2026-09-22.md`
- `coordinate-codex-tasks-eval-survey-2026-09-30.md`
- `llm-judge-lifecycle-survey-2026-09-05.md`
- `gpt-instruct-survey-2026-09-10.md`
- `skill-dogfood-test-plan-2026-10-08.md`
- `dogfood-learning-promotion-2026-10-09.md`
- `self-governance-dogfood-2026-09-24.md`
- Proposals and Domain Packs: `acceptance-join-validator`, `arm-blinded-eval-harness`, `golden-benchmark-runner`, `verification-map-generator`

## Assurance Architecture

The assurance architecture separates verification into distinct epistemic planes:
1. **Semantic Specification Plane:** Natural-language requirements and acceptance criteria (REQ/AC) bound to test IDs.
2. **Acceptance-Join Validation:** Static lint proving declared REQ/AC IDs resolve to locked runnable checks with digest-bound reports. Explicitly discloses that `covers:` is trust-based and vacuous 0-ID scopes pass exit 0.
3. **Blinded Evaluation Plane:** `arm-blinded-eval-harness` emits scaffolds constructing label-stripped `blinded/` directories, sealed maps outside scorer search paths, private shuffled schedules, strict parent path resolution, and fresh namespaces (DFL-1); host containment of the scorer remains a host precondition.
4. **Empirical Benchmark Runner:** `golden-benchmark-runner` emits templates specifying complete-vs-censored-vs-incomplete population separation (DFL-2), `score:null` never 0, noise floors, and final-verdict type controls (DFL-3).
5. **Decoupled Validation & Judge Lifecycle:** Model judges treated as attesters, not oracles. Reason tallies must accompany verdict tallies (JD-1a). Reason-mismatched labels recorded as findings, not confirmations (JD-1b).

## Horizon Milestones

### Horizon 1 — Standing Invariants & Shipped Packs
- **Shipped Packs:** Four active domain packs: `acceptance-join-validator`, `arm-blinded-eval-harness`, `golden-benchmark-runner`, and `verification-map-generator`.
- **Accounting Invariant:** Allocations, completed comparisons, and censored/incomplete outcomes are strictly segregated. `score:null` is never converted to zero.
- **Judge Attestation Rules:** Single model family equals single epistemic channel. Reason audits must accompany verdict summaries.
- **Blinding Boundary:** Path blinding does not guarantee content or stylistic isolation.

### Horizon 2 — Review Proposal (Unscheduled)
- **Scorer & Benchmark Audit** *(proposed; record-only)*: Consider a scoped fixture/scorer audit when inputs, scoring or contracts change, or when an owner assigns a review. The P6 date does not schedule this audit or authorize model dispatch.

### Horizon 3 — Trigger-Gated Queue
- **AEAT-4 Product Binding Join:** Reopen only for an explicitly authorized named-product assessment with a missing, ambiguous, stale or skipped REQ/AC → independently owned acceptance check/manifest → driver → retained observation/evidence binding. Inspect existing artifacts first; a complete spec/version/freshness-bound exercised chain falsifies the need for repair ([owner](agent-execution-assurance-taxonomy-survey-2026-09-30.md#candidate-adoption-ledger)).
- **Stage-2 Dogfooding:** Stage-1 is accepted as inconclusive (7/36 completed, 17 censored, 12 incomplete); no Stage-1 action remains. Any Stage-2 needs a separately approved preregistered question, untouched instances and enforced envelope, per the [owner disposition](skill-dogfood-test-plan-2026-10-08.md#stage-1-outcome-disposition-2026-10-13). No generation or replay follows from this roadmap.

### Horizon 4 — Direction-Gated Non-Goals
- No continuous LLM judge monitoring service operated by TeaPrompt.
- No CI execution of live model-graded benchmark competitions.
- Never cite scalar selection scores as final performance gains (avoids selection optimism: +0.109 val vs -0.019 final).

## Falsifiability

This planning summary is wrong or stale if:
1. Static join resolvability or a vacuous zero-ID pass is reported as semantic requirement coverage.
2. Censored/incomplete allocations become completed comparisons, unavailable scores become zero, or selection scores are reported as untouched final gains.
3. An authorized product-binding gap is omitted from the AEAT-4 assessment, a complete exercised binding is called missing, or Stage-2 starts without its separate owner grant.

## Candidate Adoption Ledger

| ID | Candidate / Mechanism | Status | Evidence / Surface | Next Action / Trigger |
|---|---|---|---|---|
| EA-01 | DFL-1 Exclusive Namespace Creation | Adopted | `skills/arm-blinded-eval-harness/SKILL.md` | None |
| EA-02 | DFL-2 Population Accounting Separation | Adopted | `skills/golden-benchmark-runner/SKILL.md` | None |
| EA-03 | DFL-3 Final-Verdict Type Strictness | Adopted | `skills/golden-benchmark-runner/SKILL.md` | None |
| EA-04 | JD-1a Reason Tally + JD-1b Reason Concordance | Adopted | `04-agent/workflow-recipes.md` (:171, JD-1a) + `skills/reflective-review/SKILL.md` (:100, JD-1b) | None |
| EA-05 | Vacuous Join Output Disclosure | Adopted | `skills/acceptance-join-validator/SKILL.md` (`covers:` trust-based :47, :83; vacuous 0-ID exit-0 disclosure :51, :81) | None |
| EA-06 | Blinding Limits Disclosure (argv lint is not scorer isolation; content/stylistic leakage out of scope) | Adopted | `skills/arm-blinded-eval-harness/SKILL.md` (:60, :65–66) | None |
| EA-07 | Scoped Scorer/Fixture Audit | Proposed (Record-only in this roadmap) | Horizon 2 audit idea; existing evaluation contracts remain authoritative | Consider on a concrete scoring/fixture defect or explicit review assignment; no recurring date or campaign |
