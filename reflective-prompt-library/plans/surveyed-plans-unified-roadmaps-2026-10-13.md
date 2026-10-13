# Surveyed Plans Unified Roadmaps and Parallel Socratic Synthesis — 2026-10-13

Language: English

> **Status: Record-only, point-in-time research synthesis.** The [master index](roadmap-index-surveyed-plans-2026-10-13.md) navigates the six domain planning summaries; their cited decisions retain authority over adoption, triggers and dates. This record preserves the original drafting/review trail, including its different Roadmap IV/V grouping. Corrections below do not adopt a runtime, core skill, domain pack, router tune or campaign.

## Purpose and Scope

Synthesize the survey, review, and rethink corpus (records dating from June 2026 to October 2026) into six evidence-grounded roadmaps. Subject each domain to parallel Socratic critical thinking across seven lenses in two rounds (Round 1: Harness/Flow, Assurance/Evaluation, Governance/Trust, Prompt/Cognition; Round 2: Roadmap Integrity, Boundary Challenge, Minimality & Non-Goals) — all lenses ran on the same worker family, constituting a single epistemic channel under JD-1a — to identify hidden assumptions, unverified claims, and reachable operational failure modes.

## Evidence vs Inference

- **Observed Repository Evidence:** Pinned source code, test suites, deterministic CLI executions, and verified validator outputs recorded in the source records cited per domain below. Baseline test suite: 1,743 passing tests (`pytest-9.0.3`), 0 lint errors, 3 routing evaluation suites at 100.0% consistency (record-claimed baseline; re-verified green on 2026-10-13).
- **Author-Claimed Evidence:** Upstream vendor benchmark claims, third-party blog figures, and theoretical framework assertions cited in survey papers. These are preserved with their original attribution and explicitly marked unverified.
- **[INFERENCE]:** Architectural projections, horizon timings, and synthesis deductions that extrapolate beyond directly observed test runs.

---

## Roadmap I: Agent Harness Architecture, Flow Control & Orchestration Topology

### 1. Surveyed Evidence Base
Derived from:
- `agentflow-survey-2026-09-05.md`, `agentflow-8.2-delta-survey-2026-09-13.md`, `agentflow-8.3-delta-survey-2026-09-21.md`, `agentflow-8.3.2-delta-survey-2026-09-22.md`, `agentflow-8.4.1-delta-survey-2026-09-30.md`
- `heddle-source-survey-2026-10-12.md` (`80dccf2`, accessed 2026-10-12)
- `agent-ecosystem-harness-survey-2026-10-11.md`
- `agent-harness-convergence-survey-2026-08-25.md`
- `3xa-harness-survey-2026-08-20.md`, `oh-my-openagent-survey-2026-10-01.md`, `superpowers-v6.4-adoption-2026-10-03.md`, `prime-agent-survey-2026-08-06.md`
- `agent-flow-control-research-2026-07-11.md`, `flow-control-pack-panel-record-2026-07-11.md`, `flow-coverage-panel-record-2026-07-11.md`, `checkpoint-2026-10-11-outcome.md`
- `runtime-skills-experiments-2026-10-05.md`, `runtime-skills-workflow-spec-2026-10-06.md`

### 2. Horizon Architecture

#### Horizon 1: Standing Invariants & Shipped Packs
- Two standalone domain packs: `flow-control-generator` (one-pass topologies) and `flow-loop-harness` (bounded loops). Retained as separate packs per 2026-10-11 P6 outcome (3 and 2 conservative standalone groups; next review 2027-01-11).
- Six topologies supported: sequential pipeline, parallel fan-out/fan-in with `MIN_OK` quorum, conditional router with route-trace observability, loop-until-verified, orchestrator-workers, and handoff-as-routing.
- Loop State Hygiene: RESUMED restart stanza, tail-as-compaction-budget, disposable `state/` directory, writer-critic deviation labeling, backlog constraint-tail comments.
- Preflight: P16 templates invoke a selected host-owned checker before dispatch and before result release. An unset checker preserves the attended example and supplies no enforcement evidence.

#### Horizon 2: Date-Gated Milestones
- **2027-01-11 P6 Review Checkpoint:** Review documented standalone-generation groups under the owning usage convention. A documented zero reopens consolidation evaluation; unobserved usage is `unknown`, not zero, and generation is not efficacy or accepted delivery.

#### Horizon 3: Trigger-Gated Backlog
- **Native Loop Alternatives (F1 Watch):** Re-evaluate when `/goal` gains tool-running/deterministic evaluation or Stop hooks ship packaged loop hygiene; compare the affected template's requirements under the owning F1/F4 records rather than inferring host equivalence.
- **Emitted Disconnect/Cancel Branching** *(proposed; host-dependent)*: Consider generated-script branching for a named host's authenticated cancellation signals. OW-4's existing disconnect≠cancel contract remains adopted, and signal detection/execution remain host-owned.
- **DAG Conductor Native Primitive:** Re-evaluate the existing template when a host provides native DAG primitives; this does not approve a TeaPrompt runtime.

#### Horizon 4: Direction-Gated Non-Goals
- No TeaPrompt-owned looper runtime, WAL engine, or async daemon. Emitted bash scripts run on host kernels.
- No prompt-only loop caps: iteration counters must bind to deterministic filesystem/process state.

---

## Roadmap II: Agent Execution Assurance, Verifier Ecosystem & Empirical Evaluation

### 1. Surveyed Evidence Base
Derived from:
- `agent-execution-assurance-taxonomy-survey-2026-09-30.md` (AEAT-1..6)
- `hotline-verification-redundancy-survey-2026-09-22.md`
- `coordinate-codex-tasks-eval-survey-2026-09-30.md`
- `llm-judge-lifecycle-survey-2026-09-05.md`
- `gpt-instruct-survey-2026-09-10.md`
- `skill-dogfood-test-plan-2026-10-08.md`, `dogfood-learning-promotion-2026-10-09.md`
- `self-governance-dogfood-2026-09-24.md`
- Domain packs: `acceptance-join-validator`, `arm-blinded-eval-harness`, `golden-benchmark-runner`, `verification-map-generator`

### 2. Horizon Architecture

#### Horizon 1: Standing Invariants & Shipped Packs
- **Acceptance-Join Validation:** Static lint proving REQ/AC IDs resolve to locked runnable checks with digest-bound reports. Discloses that `covers:` is trust-based and vacuous 0-ID scope passes exit 0.
- **Blinded Evaluation:** `arm-blinded-eval-harness` emits scaffolds constructing label-stripped `blinded/` directories, sealed maps outside scorer search paths, private shuffled schedules, strict parent path resolution, and fresh namespaces (DFL-1); host containment of the scorer remains a host precondition. Discloses that content leakage and stylistic leakage are out-of-scope for filesystem blinding.
- **Golden Benchmark Runner:** `golden-benchmark-runner` emits templates specifying complete-vs-censored-vs-incomplete population separation (DFL-2), `score:null` never 0, noise floors, and final-verdict type controls (DFL-3).
- **LLM Judge Lifecycle:** Model judges treated as attesters, not oracles. Reason tallies must accompany verdict tallies (JD-1a). Reason-mismatched labels recorded as findings, not confirmations (JD-1b).

#### Horizon 2: Review Proposal (Unscheduled)
- **Scorer & Benchmark Audit (proposed; unscheduled):** Consider a fixture/scorer audit on a relevant change or at an explicitly assigned review. The P6 date does not schedule an evaluation audit or a live-model campaign.

#### Horizon 3: Trigger-Gated Backlog
- **AEAT-4 Product Binding Join:** An explicitly authorized named-product assessment with a missing/ambiguous/stale/skipped independent acceptance-oracle → driver → retained-evidence binding reopens the [owning AEAT-4 question](agent-execution-assurance-taxonomy-survey-2026-09-30.md#candidate-adoption-ledger); a complete exercised spec/version/freshness-bound chain falsifies repair need.
- **Stage-2 Dogfooding:** Stage-1 is accepted as inconclusive (7/36 completed, 17 censored, 12 incomplete). Stage-2 needs a separately approved preregistered question, untouched instances and enforced envelope; the roadmap supplies no new generation/replay grant.

#### Horizon 4: Direction-Gated Non-Goals
- No continuous LLM judge monitoring service operated by TeaPrompt.
- No CI execution of live model-graded benchmark competitions.
- Never cite scalar selection scores as final performance gains (avoids selection optimism: +0.109 val vs -0.019 final).

---

## Roadmap III: Governed Autonomy, Runtime Trust Boundaries & The Four Powers

### 1. Surveyed Evidence Base
Derived from:
- `governable-autonomy-survey-2026-09-03.md`, `governed-delivery-adoption-2026-09-03.md`, `governed-delivery-review-2026-09-13.md`
- `agent-governance-four-power-concepts-2026-07-17.md`, `agent-governance-scaffold-adoption-2026-07-17.md`, `agent-governance-scaffold-panel-record-2026-07-18.md`
- `governance-workflow-self-control-adoption-2026-09-14.md`
- `stop-that-shit-survey-2026-09-30.md` (`749c921`, accessed 2026-09-30)
- `pi-warden-survey-2026-09-20.md`, `product-runtime-ownership-panel-2026-08-25.md`, `harness-intent-drift-rethink-2026-09-06.md`

### 2. Horizon Architecture

#### Horizon 1: Standing Invariants & Shipped Packs
- **Four Powers Decomposition:** Proposal (model) != Authorization (policy/human) != Effect (tool/broker) != Acceptance (verifier). Invariants: proposer != sole authorizer, executor != sole acceptor, control-plane editor != approver.
- **Domain Packs:** `agent-governance-scaffold` and `governed-delivery`.
- **Ultra Vires Nullification:** Scaffolds state `Effect(a) = empty` for unauthorized actions, explicitly requiring broker mediation.
- **Trust Boundary Realism:** Prompts declare policies; hosts enforce them. Missing fields treated as unknown, not safe. Tool status lines treated as claims, not verified facts.

#### Horizon 2: No New Date-Gated Commitment
- **Pack Overlap Review (R6; event-gated):** Preserve the owning [GD↔AGS disposition](checkpoint-2026-10-11-outcome.md#gd-outcome): consolidation remains held, independent use is unknown, and documented coupled-only use or shared-contract divergence reopens the review. No quarterly audit is scheduled here.

#### Horizon 3: Trigger-Gated Backlog
- **GD-16 / GDR-1..6 Host Run:** Execute the full Governed Delivery refuter suite when a qualified host harness provides full container containment, protected oracles, and durable ledger sinks.
- **I-1 / A-5 — distinct conditions:** The [owning checkpoint successor](harness-intent-drift-rethink-2026-09-06.md#checkpoint-tool-claim-review-2026-10-11) keeps writer/effect recurrence separate from viewer/source misuse. I-1 retains its same-class failure/adoption gate and reserved implement destination; A-5 needs its own observed case and named smaller-alternative failure. Neither is installed by this synthesis.

#### Horizon 4: Direction-Gated Non-Goals
- No TeaPrompt-owned sandbox, hypervisor, or network proxy.
- No prompt-only containment claims: prompt text cannot prevent side-effect escape if the host provides unmanaged shell or direct network access.
- No auto-approval of high-risk actions without a non-model verification channel and human review.

---

## Roadmap IV: Prompt Engineering, Contract Taxonomy & Context Architecture

### 1. Surveyed Evidence Base
Derived from:
- `fifth-gen-prompt-taxonomy-rethink-2026-09-21.md`
- `system-prompts-leaks-survey-2026-10-07.md` (`f015440`, accessed 2026-10-07)
- `semantica-survey-2026-10-07.md` (`320761de`, accessed 2026-10-07)
- `astra-efficiency-rules-survey-2026-09-10.md` (`5576ceb`, accessed 2026-09-10)
- `openai-model-guidance-survey-2026-09-10.md`, `claude-code-system-prompts-survey-2026-07-24.md`
- `minimax-code-survey-2026-09-19.md`, `minimax-code-trace-map-survey-2026-09-19.md`
- `handover-docs-survey-2026-09-23.md`, `direction-scope-docs-adoption-2026-09-19.md`
- `diagram-design-survey-2026-10-07.md`, `pstack-survey-2026-09-22.md`, `pstack-synthesis-survey-2026-09-22.md`, `pstack-matt-lauren-survey-2026-10-03.md`

### 2. Horizon Architecture

#### Horizon 1: Standing Invariants & Shipped Prompts
- **Contract-Shaped Library:** Existing prompts use requirements, outputs, invariants and validation. The seven-category list is a user-supplied audit vocabulary with unverified exact provenance, not an adopted exhaustive taxonomy.
- **Procedure Layer Defense:** Retain `01-thinking` reasoning scaffolds, `02-engineering` workflows and `workflow-recipes.md`; the cited rethink rejects exclusivity without establishing that all procedure content improves model outcomes.
- **Context Hygiene:** Canonical packets, negative constraints and task-declared failure signatures support inspectable continuation. The surveyed 3,000-character cap was rejected, not installed; no numeric context limit is introduced by this record.
- **Data/Instruction Separation:** External tool returns and document pastes tagged as data/evidence, never instruction sources.

#### Horizon 2: Review Proposal (Unscheduled)
- **Prompt Size & Bloat Audit (proposed; unscheduled):** Consider a scoped prompt review when a named content or reference-consumption defect is observed; no recurring scan or new lint threshold is scheduled here.

#### Horizon 3: Trigger-Gated Backlog
- **SFR-4 Software Factory Routing Holdout:** A verified factory-plan → minimality failure reopens the owning assessment; fixture the boundary and satisfy R8's pre-tune checks before any router change.
- **A-5 Viewer/Source Distinction:** Preserve A5-CP1's own observed-case/smaller-alternative-failure condition. External-change verification invalidation is already adopted as A-7a, not a deferred A-5 reread feature.

#### Horizon 4: Direction-Gated Non-Goals
- No prompt-level secrecy claims: system prompts cannot be guaranteed secret against model extraction once loaded.
- Never use numeric prompt length caps as rigid rules; use progressive disclosure and contract boundaries.

---

## Roadmap V: Memory Architecture, Cognitive Foundations & Autonomous Software Factory Evolution

### 1. Surveyed Evidence Base
Derived from:
- `teabrain-concepts-experiments-survey-2026-09-21.md` (`27b4d25`, accessed 2026-09-21)
- `human-cognition-adoption-2026-10-02.md`
- `ember-snn-llm-survey-2026-09-22.md` (arXiv:2604.12167v1, checked 2026-09-22)
- `jspace-cognition-survey-2026-08-20.md`, `mgd-form-theory-survey-2026-10-02.md`
- `software-factory-rethink-panel-record-2026-09-28.md`, `software-factory-sdlc-inner-outer-loop-survey-2026-09-28.md`
- `devops-agentic-trends-survey-2026-09-28.md`, `graph-engineering-synthesis-survey-2026-09-16.md`
- `dream-rsi-survey-2026-09-18.md`, `rsiagent-survey-2026-09-16.md`, `rrsi-survey-2026-09-30.md`
- `decision-model-survey-2026-09-18.md`, `gliner2-survey-2026-09-19.md`, `nimble-survey-2026-09-19.md`
- `code-recall-survey-2026-08-20.md`, `dilinai-nuwa-jiyao-survey-2026-07-13.md`, `fable-method-survey-2026-07-16.md`

### 2. Horizon Architecture

#### Horizon 1: Standing Invariants & Shipped Concepts
- **File-Artifact Memory Substrate:** Memory externalized as version-controlled file artifacts (`intent-record`, `task-packet`, `evidence-ledger`, `acceptance-record`, `PROJECT_KNOWLEDGE.md`).
- **Human Cognition Protocol Integration:** HCC-1 adds optional diagnostics, practice and learner agency to `learning-coach.md`; HCC-2 adds scientific-source/read/design/population bounds to the research skill/prompt; HCC-3 adds construct-sensitive review and numerical-provenance honesty to the review skill/critical-thinking lens. These are compatibility-bounded guidance, not verified human effects or prediction-error guarantees.
- **Factory Recipe Realism:** The installed recipe declares an artifact-gated workflow, host oracle protection and human intent/acceptance gates. Mutation probes can reveal sensitivity to selected faults, not general correctness; `min_kill_rate: 0.85` is the surveyed blueprint's illustrative value, not a validated floor.

#### Horizon 2: Review Proposal (Unscheduled)
- **Memory Provenance Audit (proposed; unscheduled):** Consider source/authority/evidence/expiry review when a concrete memory-provenance defect is observed. The P6 checkpoint does not create a quarterly memory-maintenance duty.

#### Horizon 3: Trigger-Gated Backlog
- **TB-1 Learner Governance Reconsideration:** Explicit user direction for governance scaffolding of a self-modifying / online-learning / reward-driven agent reopens TB-1; consideration is not new pack-domain or runtime adoption.
- **RS-9 Writer-Critic Context:** An observed cross-round oscillation in a TeaPrompt-run loop reopens RS-9's review; prior-verdict context is not automatically installed.

#### Horizon 4: Direction-Gated Non-Goals
- No neural, neuromorphic (SNN), vector DB, or graph database runtime operated by TeaPrompt.
- No TeaPrompt-owned CI runner, compiler daemon, or container manager.
- Never claim autonomous software factories eliminate human code review or provably prevent defect introduction without external mutation tests and human sign-off.

---

## Roadmap VI: Ecosystem Packaging, Host Distribution, Localization & Governance Health

### 1. Surveyed Evidence Base
Derived from:
- `checkpoint-packaging-decision-2026-10-11.md`, `checkpoint-2026-10-11-outcome.md`
- `mattpocock-skills-v131-delta-survey-2026-10-07.md`
- `managed-skills-learned-survey-2026-10-06.md`
- `agnix-agent-skills-hook-survey-2026-08-04.md`, `baton-dispatch-survey-2026-07-13.md`
- `frozen-core-parity-review-2026-07-11.md`, `cross-survey-rethink-2026-10-07.md`
- `methodology-only-rethink-panel-2026-10-01.md`, `d025db7-publication-review-2026-10-02.md`, `ai-assisted-team-throughput-review-2026-08-12.md`

### 2. Horizon Architecture

#### Horizon 1: Standing Invariants & Distribution Factoring
- **Packaging Structure:** Nine core skills plus ten registered domain packs at this snapshot. The approved October 11 factoring covers `agent-governance-scaffold/ARTIFACTS.md` and the two flow packs' `TEMPLATES.md`, not every pack body.
- **Localization Parity:** `SKILL_TRIGGER_CHEATSHEET.md` and `SKILL_TRIGGER_CHEATSHEET.zh-TW.md` maintain strict lockstep parity across all 11 bullets (10 domain packs + 1 dispatch bullet).
- **Managed Skills Isolation:** Host-side managed skills in `~/.omp/agent/managed-skills` remain isolated from repository-authored skills. Memory-derived insights require `04-agent/artifact-promotion.md` §4 gates.

#### Horizon 2: Date-Gated Milestones
- **Source-Bound Reviews:** P6 is due 2027-01-11; T2 runs on registry/appendix change or that evidence review if unchanged. Other packaging/source watches retain their owning event gates, not an invented quarterly schedule.

#### Horizon 3: Trigger-Gated Backlog
- **E2 Archive Restructuring:** A second independent archive-weight complaint or a maintainer's real navigation failure attributable to the named surfaces reopens the destructive review, not automatic restructuring.
- **Localized Trigger Cues Beyond Cheatsheets:** Reconsider navigation on a verified zh-TW adoption signal; no full skill-body translation follows.

#### Horizon 4: Direction-Gated Non-Goals
- No full translation of `SKILL.md` bodies (cheatsheet, glossary, and navigation parity only).
- Never adopt host-specific CLI hooks (e.g. Agnix or private daemon plugins) into portable skill definitions.
- Never operate a centralized package registry or npm/pypi release pipeline for skills; git-native distribution remains canonical.


---

## Parallel Socratic Critical Thinking Synthesis

A two-round parallel Socratic review was executed across the survey corpus and the eight newly drafted roadmap files.

### Round 1: Survey Corpus Deep Dive (4 Specialist Lenses)
Four Socratic reviewer lenses evaluated the surveyed plan corpus (all on the same worker family — a single epistemic channel under JD-1a, not independent agreement):
- **SocraticHarnessLens** (`AGREE WITH CHANGES`): Loop caps in prose are lossy compression read by the optimizer they seek to constrain; without host-enforced counters and verifier exit codes, termination is an illusion. Tool concurrency bounds do not prove mutation independence.
- **SocraticAssuranceLens** (`AGREE WITH CHANGES`): Acceptance-join linters prove static resolvability, not runtime correctness; blinded path isolation leaks stylistic and semantic identity; scalar selection scores (+0.109 val vs -0.019 final) demonstrate inherent selection optimism.
- **SocraticGovernanceLens** (`AGREE WITH CHANGES`): Prompt-level governance cannot constrain an uncontained host agent. Ultra vires nullification ($Effect=\emptyset$) is voided by any single unmanaged shell or network bypass. Stop-hooks fail open under contention (1542ms allow-shape). Preflight checks cohere but cannot authenticate.
- **SocraticPromptCognitionLens** (`AGREE WITH CHANGES`): Challenged unsupported seven-category exclusivity, loss of negative constraints during compaction, and autonomy claims lacking protected oracles. These are review objections, not measured compaction effects or a validated mutation threshold.

### Round 2: Direct Audit of 8 Roadmap Drafts (3 Scout Lenses)
Three scout lenses (same harness worker family; decorrelated by scope only — second pass over the same channel) directly inspected the 8 new roadmap files:
- **ScoutRoadmapIntegrityLens** (`AGREE WITH CHANGES`): Confirmed all cited commit hashes, repo revisions, and source access dates match original survey records. Eliminated false access dates (e.g. corrected arXiv check dates to 2026-09-05 and 2026-09-22).
- **ScoutSocraticBoundaryChallenger** (`AGREE WITH CHANGES`): Flagged outer-vs-inner loop cap conflation, sandbox assumption fallacies, and mutation test gaming loopholes. Required explicit disclaimers on inner-turn tool hangs.
- **ScoutMinimalityGovernanceLens** (`AGREE WITH CHANGES`): Found proposals mislabeled as adoptions and requested explicit record-only status. Its checkpoint-alignment recommendation did not authorize new dates: only the owning P6/T2 decisions establish the January review scope.

### Policy Safeguards 1–8 (Status-Tagged)

1. **Host-Counted Termination Invariant** — *proposed, record-only:* Broader wording would require observed iteration/concurrency counters and host wall-clock supervision, including a hung individual call. Existing script caps do not alone supply that end-to-end guarantee.
2. **Vacuous Join Disclosure** — *adopted, verified shipped:* `acceptance-join-validator/SKILL.md` discloses that 0 IDs in scope is a vacuous pass (:51, :81) and `covers:` is a trust-based declaration (:47, :83).
3. **Blinding Limits Disclosure** — *adopted, verified shipped:* `arm-blinded-eval-harness/SKILL.md` discloses that path/argv blinding is not scorer isolation and content or stylistic leakage is out of scope (:60, :65–66).
4. **Broker-Exhaustiveness Invariant** — *adopted, verified shipped:* `agent-governance-scaffold/SKILL.md` (:49) declares any unmediated `model → privileged_tool` path a governance failure; `ARTIFACTS.md` (:36) carries `ultra_vires_nullification` and (:38) demands observed host wiring evidence.
5. **Fail-Closed Gate Bar** — *proposed, record-only:* Stop-hooks and circuit breakers must state that allow-shaped fail-open behavior under contention or lock failure is advisory only and must not be cited as an enforcement bound.
6. **Compaction Non-Goal Retention Rule** — *proposed, record-only:* Beyond shipped canonical-packet recovery, consider an explicit negative-constraint/non-goal reassertion before resuming. No new installed clause follows from this summary.
7. **Ledger Integrity Boundary** — *adopted, verified shipped:* `skills/reflective-review/SKILL.md` (:145) and `04-agent/runtime-trust-boundary.md` (:147–148) state field integrity does not establish source/actor authenticity or log completeness.
8. **Factory Title Boundary Cue** — *proposed, record-only:* Make the already-installed recipe's host-enforcement and human intent/acceptance boundary easier to discover beside the title. This is placement hardening, not an absent substantive boundary or a new runtime guarantee.

## Falsifiability

This synthesis is wrong or stale if:
1. Any surveyed candidate marked adopted is shown to be absent from the repository.
2. A trigger for a dormant Horizon 3 item is proven to have fired in a verifiable record without being scheduled for re-litigation.
3. A host platform proves that prompt-only instructions can deterministically constrain a runaway tool loop without host-level kernel, sandbox, or broker intervention.

## Candidate Adoption Ledger

| ID | Candidate / Safeguard | Destination Surface | Status | Evidence / Verification | Next Action |
|---|---|---|---|---|---|
| UR-01 | Comprehensive 6-Domain Roadmaps | This record (`plans/surveyed-plans-unified-roadmaps-2026-10-13.md`) | Recorded | Synthesized from the per-domain source records cited in each roadmap §1 | Standing reference for future checkpoint reviews |
| UR-02 | Parallel Socratic Synthesis | This record | Recorded | Seven lenses in two historical rounds; one model-review channel | Preserve the review trail; new claims need source-bound review |
| UR-03 | Selected safeguards 1–8 status summary | [Master index](roadmap-index-surveyed-plans-2026-10-13.md#parallel-socratic-critical-thinking-consensus) and domain ledgers | Recorded | Individual topics above retain four existing disclosures and four proposal groups; this summary adopts none | Reconcile when an owning row changes; retain each separate gate |
| UR-04 | Memory Provenance Review | This synthesis's Horizon 2 idea | Proposed (record-only; unscheduled) | No owning calendar decision or new memory-runtime requirement | Consider only on a concrete provenance defect or explicit review assignment |
