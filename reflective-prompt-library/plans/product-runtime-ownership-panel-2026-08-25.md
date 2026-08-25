# Product / Runtime Ownership Boundary — Panel Record (2026-08-25)

> **Status: decided, implemented, guarded, and verified.** This is a non-authoritative decision record. TeaPrompt remains a natural-language policy library: no Heddle dependency, hosted execution service, persistence adapter, replay engine, or tenth core workflow skill is introduced.

## Panel Consensus

- **Decision:** `AGREE WITH CHANGES` — unanimous, **7 of 7 lens verdicts** (`EvidenceAuditor-2`, `ArchitectureReviewer-2`, `ReproducibilityEngineer`, `ProvenanceSecurity-3`, `CodeCorrectness-2`, `UsabilityReviewer-2`, `StrategicSynthesis-3`); no pure `AGREE` and no `DISAGREE`.
- The scout host schema reduced initial yields to summary-shaped objects. All seven settled lenses were recovered through **tier-1 DM-wake** and delivered findings, Socratic questions, a steelman, exact wording recommendations, and an explicit verdict before synthesis. No provider-specific persona or model routing is claimed.
- **Use-case recommendation:**
  - `study` — **yes**: use the three-layer ownership frame, record-specific durability analysis, product-acceptance boundary, transport/lifecycle distinction, and promise-scaled architecture as external reference concepts.
  - `reproduce` — **bounded / host-only**: a concrete product/runtime integration must test stale-revision rejection, disconnect survival, cursor replay, optimistic session concurrency, one absorbing terminal outcome, and tenant-bound ingress. Prompt text cannot reproduce those guarantees.
  - `adopt` — **narrow in-place wording and deterministic guards only**: OW-1–OW-4 and OW-8 below. The named five-stage ladder and full external checklist are not imported as canonical TeaPrompt taxonomies.
  - `deploy` — **blocked on this review alone**: the external packages are unpinned and unverified, and TeaPrompt does not operate a runtime. Deployment requires host code and tests for authorization, concurrency, durability, credential isolation, replay, cancellation, and external-effect recovery.

## Required Wording Changes

1. **Ownership and product acceptance — `04-agent/runtime-trust-boundary.md`:** distinguish runtime execution truth, host product truth, and infrastructure realization; state that runtime completion is a proposal until the host authorizes, checks the current canonical version, commits, and verifies the result.
2. **Record-specific durability and lifecycle — `04-agent/runtime-trust-boundary.md`:** reject a boolean durability claim; name only the record classes that exist and their consistency, retention, locality, and security requirements. A client disconnect ends observation, not business intent; cancellation is explicit and authenticated.
3. **Planning contract — `skills/reflective-spec-plan/SKILL.md`:** add a product-truth contract and require the lowest architecture that satisfies the user-visible promise. Named stages remain optional external reference vocabulary, not a maturity ladder.
4. **Risk contract — `skills/reflective-risk/SKILL.md`:** gate stale canonical writes, premature success, ambient product credentials, unscoped tenant records, and transport/cancellation conflation.
5. **Method and judgement references — `METHODOLOGY_MAP.md` and `PROJECT_KNOWLEDGE.md`:** record the orthogonal product-truth boundary and link this evidence record without claiming prompt-level enforcement.
6. **No change:** `reflective-handoff-retro` already preserves state, trust boundaries, blockers, tests, and ambiguous external outcomes. The whole-project roadmap gains no open item: adopted changes land now; deferred candidates have explicit triggers in the ledger.

## Shared Findings

- `observed` — The supplied article text separates runtime execution semantics, host business authority, and infrastructure adapters, and illustrates `execution success ≠ business acceptance` with a stale canonical revision. The panel found this orthogonal to, and compatible with, TeaPrompt's Four Powers and the existing control-state/effect/ownership-liveness contracts.
- `observed` — The source distinguishes sessions, compaction archives, active-run coordination, replay buffers, product transcripts, canonical results, traces, artifacts, approvals/memory, and credentials. These record classes have different consistency, retention, locality, and security needs; one `durable: true` label cannot establish all of them.
- `observed` — A dropped SSE/WebSocket/browser connection is an observation failure, not authenticated cancellation. A host can still enforce budgets, deadlines, leases, and explicit cancellation without coupling run intent to a subscriber socket.
- `observed` — TeaPrompt already handles ambiguous external effects as `OUTCOME_UNKNOWN` with sink-specific reconciliation. Product revision checks complement that rule but do not resolve a remote effect dispatched before its receipt is committed.
- `author-claimed` — Heddle's package split and SlideX integration are presented as implementation evidence for the architecture. This review did not inspect a pinned Heddle repository, package tarball, license, provenance attestation, failure corpus, or current hosted deployment.
- `[INFERENCE]` — The boundary vocabulary may reduce shadow-backend drift and premature distributed-system design, but no adopter outcome data was supplied. Its value is therefore a falsifiable design/review aid, not an efficacy claim.

## Socratic Questions and Disposition

1. **What if the canonical sink has no CAS/ETag?** Runtime completion remains a proposal. The host must define another decisive precondition, serialize the mutation, or stop for Human Review; absence of a concurrency mechanism does not authorize last-write-wins.
2. **Does `disconnect ≠ cancel` create zombie runs?** No implicit socket cancellation is allowed, but the host must still define authenticated cancellation, bounded execution, lease/deadline policy, and an owner for interrupted runs.
3. **Do three ownership layers compete with TeaPrompt's Four Powers?** No. The layers locate state and implementation responsibility; Proposal, Authorization, Effectuation, and Acceptance separate decision authority. They are orthogonal lenses.
4. **Must every product implement all listed durability record classes?** No. Specify only the classes required by the user-visible promise, including which state is intentionally volatile. The vector is an honesty check, not a mandatory storage architecture.
5. **Can product CAS make external side effects exactly once?** No. Remote effects still need parameter-bound identity, sink-enforced idempotency or decisive query evidence, and `OUTCOME_UNKNOWN` reconciliation.

## Disagreements / Residual Risks

- **Architecture versus usability:** architecture lenses favored explicit ownership and record tables; usability warned that copying the full five-stage and sixteen-question material would add ceremony. Resolution: adopt only the boundary invariants and lowest-sufficient-promise heuristic.
- **Reproduction scope:** some lenses recommended host fault tests; the evidence lens correctly blocked claims about Heddle itself because no pinned source or executable package was inspected. Resolution: reproduce generic contracts only in a named host, never label those tests Heddle verification.
- **License and provenance:** the Medium snapshot and package names carry no verified reuse license in this packet. The adopted wording is a clean-room conceptual restatement; no source table, checklist, code, or package is copied.
- **Security:** Stage-4/5-style remote execution remains a data-egress and ambient-authority risk without capability-scoped access, tenant-bound repositories, credential scrubbing, and explicit replay authorization.
- **External effects:** optimistic concurrency protects the host's canonical commit, not an already-escaped payment, message, publish, or delete. Existing `OUTCOME_UNKNOWN` rules remain load-bearing.

## Candidate Adoption Ledger

| ID | Candidate | Status | Evidence | Next action or trigger |
|---|---|---|---|---|
| OW-1 | Runtime execution truth / host product truth / infrastructure realization boundary | **Adopted** 2026-08-25 by explicit user direction | 7/7 lenses; source ownership sections; local gap in the existing trust-boundary lens | Guard the three owners in `test_product_runtime_ownership_panel_record.py`; re-litigate if a host cannot assign one authoritative owner per state class |
| OW-2 | `Execution Success ≠ Business Acceptance`, including current-version validation and commit-before-success | **Adopted** 2026-08-25 | 7/7 lenses; stale-revision scenario; aligns with Four-Power Acceptance | Guard trust, spec, risk, and methodology surfaces; a host implementation must still provide behavioral CAS/ETag tests |
| OW-3 | Durability is record-specific, not a boolean or universal storage adapter | **Adopted as a design checklist** 2026-08-25 | 6/7 lenses explicitly supported; prior durable-harness survey already separates control/effect/ownership contracts | Guard record-specific wording; re-litigate only if the checklist forces unused storage classes or causes measured workflow overhead |
| OW-4 | Subscriber disconnect is not run cancellation; one run lifecycle owner and one terminal outcome | **Adopted** 2026-08-25 | 7/7 lenses; falsifiable reconnect/cancellation scenario | Guard trust/spec/risk wording; behavioral proof remains host-only |
| OW-5 | Named five-stage Heddle integration ladder | **Partial** 2026-08-25: adopt only the lowest-sufficient-promise heuristic; named stages remain study-only | Panel usability/minimality resolution; no cross-domain adopter data | Reconsider named taxonomy only after repeated TeaPrompt specs need it and a deterministic usability comparison favors it |
| OW-6 | Five mistakes and sixteen-question checklist | **Partial** 2026-08-25: distill failure conditions; do not copy the external checklist verbatim | Useful review coverage but unverified reuse license and substantial overlap with existing skills | Re-open only with licensed/pinned upstream text and a demonstrated uncovered checklist gap |
| OW-7 | Import or deploy `@heddleagent/*`, SlideX, a hosted-run service, or a DB adapter | **Deferred / blocked** 2026-08-25 | Unpinned packages, unknown license/provenance, retired public SlideX, TeaPrompt Standing Non-Goals | Needs explicit project-direction change, pinned source/license/SBOM, named host owner, security review, and executed integration/fault tests |
| OW-8 | Tenant-bound repositories, replay authorization, and no ambient product DB credentials in execution hosts | **Adopted as a required host precondition** 2026-08-25 | Provenance/security lens; source states product scope and credential separation; existing least-privilege policy | Guard trust/risk wording; production use requires host authorization and egress tests |
| OW-9 | SlideX as proof of current availability or general production efficacy | **Deferred / study-only** 2026-08-25 | Source says public deployment retired; no telemetry or comparative failure corpus | May change only with pinned operational evidence and a defined comparison population |

## Evidence Actually Checked

- **Coordinator-executed:** repository revision `ce42045a9f8adeebc3c9913345a66dcccc7f4081` on attached branch `main`; source artifact SHA-256 `d2e50ad46463dac1eae302acd9a5503dde25e1fb4f811a3f78ef3a76b3600164`; shared packet SHA-256 `75719b81196ca0659933fc587ef044f44fbe9659e821c69b024b9877f49cf768`; reads of the canonical repository policy, project knowledge, trust boundary, affected skills, methodology map, prior durable-harness record, and guard conventions.
- **Read by lenses:** all seven lenses read `review-packet-paste2-ownership-2026-08-25.md` first; the Evidence Auditor read the full 2,427-line source in six ranges; other lenses inspected the load-bearing source ranges and named TeaPrompt contracts.
- **Lens-phase execution:** none. Reviewers were read-only and ran no project-wide tests. No Heddle source checkout, npm package inspection, SlideX deployment, power-loss test, network partition, or real external-sink test occurred.
- **Inferred and kept qualified:** cross-domain generalizability, reduced adopter defects, and Heddle implementation fidelity.
- **Post-adoption verification:** focused guard `6 passed`; affected contract set `96 passed`; complete plans suite `1052 passed`; final post-cleanup `make all` repeated the 1,052 tests and passed link validation (169 files, 0 errors), lint (0 errors; one pre-existing long-pack warning), governance (12/12), project-knowledge validation, record hygiene (0 errors/warnings), benchmark fixture (24 tasks, 9/9 workflows), skill examples (9 core + 3 packs), route fixtures, and ROUTE-001/002/003 at 100%.
- **Cleanup:** the repo-root packet was deleted only after this synthesis, Candidate Adoption Ledger, and guard existed. Its SHA-256 remains above so the reviewed input is identifiable without making the temporary wrapper a durable dependency.

## Falsifiability

This decision must be re-litigated if: (1) an adopted surface disappears while its deterministic guard still passes; (2) a TeaPrompt artifact claims runtime completion proves canonical product acceptance; (3) a design says `durable: true` without naming the persisted record and failure boundary; (4) a transport disconnect silently authorizes cancellation; (5) an execution host receives ambient product credentials or serves an unscoped durable record; or (6) pinned Heddle evidence contradicts the author-claimed architecture summarized here.

## Completion Ledger

| Item | Status | Evidence |
|---|---|---|
| Durable panel record and Candidate Adoption Ledger | `verified` | this file; focused guard passed |
| Trust-boundary ownership, durability, lifecycle, and credential wording | `verified` | `04-agent/runtime-trust-boundary.md`; focused + full suite passed |
| Spec/risk contract wording | `verified` | `skills/reflective-spec-plan/SKILL.md`, `skills/reflective-risk/SKILL.md`; affected contract set passed |
| Methodology, project-knowledge, and case-study pointers | `verified` | `METHODOLOGY_MAP.md`, `PROJECT_KNOWLEDGE.md`, `external-adoption-case-studies-2026-06-20.md`; links/knowledge/record hygiene passed |
| Deterministic adoption guard | `verified` | `plans/tests/test_product_runtime_ownership_panel_record.py`: 6 passed |
| Focused and repository verification | `verified` | affected set 96 passed; full suite and `make all`: 1052 passed |
| Temporary packet removal and branch re-check | `verified` | packet removed after synthesis; shared worktree remained attached to `main` |
