# Governed Autonomy, Runtime Trust Boundaries and Four-Power Governance Roadmap — 2026-10-13

Language: English

> **Status: active domain roadmap (record-only; non-authoritative).** Scheduling and architectural companion derived from governed autonomy, runtime trust boundary, and four-power governance surveys. Preserves standing non-goals, host-enforcement boundaries, and ultra-vires nullification limits. No new runtime or core skill is adopted by this record.

## Purpose

Summarize Governed Autonomy, Runtime-Trust Boundaries, Capability Leases and Four-Power Separation using the source records listed below; proposals remain distinct from adopted contracts and host enforcement.

## Evidence vs Inference

- **Observed Repository Evidence:** Pinned sources, security probes, and governance panel records in `governable-autonomy-survey-2026-09-03.md`, `governed-delivery-adoption-2026-09-03.md`, `governed-delivery-review-2026-09-13.md`, `agent-governance-four-power-concepts-2026-07-17.md`, `agent-governance-scaffold-adoption-2026-07-17.md`, `governance-workflow-self-control-adoption-2026-09-14.md`, `stop-that-shit-survey-2026-09-30.md` (`749c921`, accessed 2026-09-30), and `product-runtime-ownership-panel-2026-08-25.md`.
- **Author-Claimed Evidence:** Upstream claims regarding zero-trust multi-agent containment, theoretical formal verification proofs, and vendor-reported incident metrics.
- **[INFERENCE]:** Projections of OS-level broker integration, capability token enforcement mechanisms, and automated compliance auditing.

## Surveyed Plans Corpus

This roadmap derives directly from the following surveyed plans:
- `governable-autonomy-survey-2026-09-03.md` (GA-1..20)
- `governed-delivery-adoption-2026-09-03.md`
- `governed-delivery-review-2026-09-13.md`
- `agent-governance-four-power-concepts-2026-07-17.md`
- `agent-governance-scaffold-adoption-2026-07-17.md`
- `agent-governance-scaffold-panel-record-2026-07-18.md`
- `governance-workflow-self-control-adoption-2026-09-14.md`
- `stop-that-shit-survey-2026-09-30.md`
- `pi-warden-survey-2026-09-20.md`
- `product-runtime-ownership-panel-2026-08-25.md`
- `harness-intent-drift-rethink-2026-09-06.md`

## Governance Architecture: The Four Powers

To prevent the composite self-acceptance antipattern (where a single agent or tree proposes, authorizes, executes, and accepts its own work), the architecture declares separation of four distinct powers (host brokers and execution environments must enforce them):
1. **Legislative (Policy Authority):** Declares constitution, constraints, capability schemas, and acceptable operational risk boundaries.
2. **Judicial (Oracle & Acceptance Authority):** Evaluates observable post-execution evidence against sealed acceptance criteria.
3. **Executive (Agent / Orchestrator):** Proposes plans, generates code, and requests tool invocations within assigned capability tokens.
4. **Oversight (Audit & Broker Authority):** Intercepts mutations, validates active capability leases, records append-only ledgers, and enforces circuit breakers.

### Critical Invariants
- `proposer != sole authorizer`
- `executor != sole acceptor`
- `control-plane editor != approver`
- **Ultra Vires Nullification:** For all actions $a \notin \text{AuthorizedActions}$, $\text{Effect}(a) = \emptyset$. This declared policy requires broker mediation and is voided if any unmanaged shell, network, or credential bypass exists on the host.

## Horizon Milestones

### Horizon 1 — Standing Invariants & Shipped Packs
- **Shipped Packs:** `agent-governance-scaffold` and `governed-delivery`.
- **Broker-Exhaustiveness Disclosure:** Governance scaffolds declare any unmediated `model → privileged_tool` path a governance failure, and artifact presence alone is never evidence of broker mediation.
- **Fail-Closed Gate Bar** *(proposed; record-only)*: Stop-hooks and circuit breakers would state that allow-shaped fail-open behavior under contention is advisory only and not an enforcement bound; no shipped surface carries this wording yet.
- **Attestation Authentication Boundary:** Emitted preflight checks are disclosed as point-in-time record-coherence checks — they validate coherence, never that events occurred, sealing holds continuously, or delivery is accepted; self-report is not attestation.

### Horizon 2 — No New Date-Gated Commitment
- **GD↔AGS Redundancy Review (R6):** The [checkpoint disposition](checkpoint-2026-10-11-outcome.md#gd-outcome) holds consolidation; independent use remains unknown. Preserve the owning coupled-only-use/shared-contract-divergence trigger rather than inventing a quarterly boilerplate audit.

### Horizon 3 — Trigger-Gated Queue
- **GD-16 / GDR-1..6 Host Run:** Execute the full Governed Delivery refuter suite when a qualified host harness provides full container containment, protected oracles, and durable ledger sinks.
- **I-1 Writer/Effect Disagreement:** The [owning successor](harness-intent-drift-rethink-2026-09-06.md#checkpoint-tool-claim-review-2026-10-11) distinguishes a second same-class writer/effect mismatch from read/parser behavior. Reopening requires the original I-1/S-1 gate and explicit adoption review; the reserved destination is `reflective-implement` Verification.
- **A-5 Viewer/Source Misuse:** Reopen only on its own observed case and named smaller-alternative failure, per A5-CP1 in that successor. Do not merge it into I-1 or install reserved text from a general tool discrepancy.

### Horizon 4 — Direction-Gated Non-Goals
- No TeaPrompt-owned sandbox, hypervisor, or network proxy.
- No prompt-only containment claims: prompt text cannot prevent side-effect escape if the host provides unmanaged shell or direct network access.
- No auto-approval of high-risk actions without a non-model verification channel and human review.

## Falsifiability

This planning summary is wrong or stale if:
1. Four-power compliance is claimed despite an unmediated privileged-tool path or worker-writable authority/receipt evidence.
2. Preflight record coherence or artifact presence is used to prove authentication, continuous sealing or accepted delivery.
3. A read/parser failure is classified as writer/effect recurrence, I-1 and A-5 are merged without their own ruling, or a host refuter is reported passed without current per-refuter evidence.

## Candidate Adoption Ledger

| ID | Candidate / Mechanism | Status | Evidence / Surface | Next Action / Trigger |
|---|---|---|---|---|
| GA-01 | Four-Power Decomposition Model | Adopted | `skills/agent-governance-scaffold/SKILL.md` | None |
| GA-02 | Governed Delivery Lifecycle & Manifests | Adopted | `skills/governed-delivery/SKILL.md` | None |
| GA-03 | Broker-Exhaustiveness Invariant | Adopted | `skills/agent-governance-scaffold/SKILL.md` (:49) + `ARTIFACTS.md` (:36, :38) | None |
| GA-04 | Preflight Coherence vs Auth Disclosure | Adopted | `skills/governed-delivery/SKILL.md` (:54, :177, :227–229) | None |
| GA-05 | Fail-Closed Stop-Hook Bar | Proposed (Record-only in this roadmap) | This roadmap §Horizon 1 | Re-litigate upon host sandbox integration |
