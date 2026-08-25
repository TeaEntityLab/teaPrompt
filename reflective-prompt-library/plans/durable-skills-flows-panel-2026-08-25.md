# Durable-State Rethink of Skills & Flows — Panel Record (2026-08-25)

> **Status: decided (non-authoritative).** TeaPrompt remains a prompt/skill library, not a runtime. No new core skill, no pack merge, no owned WAL/replay. Only narrow in-place clarifications that keep prompt text from being mistaken for host durability were adopted.

## Panel Consensus

- **Decision:** `AGREE WITH CHANGES` — unanimous, **7 of 7 lenses** (`EvidenceAuditor`, `ArchitectureReviewer`, `ReproEngineer`, `ProvenanceSecurity-2`, `CodeCorrectness`, `UsabilityReviewer`, `StrategicSynthesis-2`); no `DISAGREE`, no pure `AGREE`.
- **Use-case recommendation:**
  - `study` — **yes**: WAL / durable program counter / effect sandwich / unknown→reconcile, plus host priors (Temporal, DBOS, Restate, Orleans, Erlang/OTP, ARIES/SAGAS, Helland) as reference architecture.
  - `reproduce` — **deferred / host-only**: requires concrete host runtime + crash/replay/fencing harness with power-loss & real-sink tiers; not reproducible at prompt layer.
  - `adopt` (TeaPrompt prompt/skills) — **only narrow in-place clarifications** (AH-20, AH-21) + already-landed AH-18/AH-19; all other candidates rejected/deferred.
  - `deploy` (as harness) — **blocked**: no new durability proof at prompt layer; external-effect durability needs host enforcement owner + sink idempotency / query contract.

## Required Wording Changes

### AH-20a — `04-agent/workflow-recipes.md` `## Looper Topologies` (anti-collapse: WAL/event-reduction stay host-runtime)

```diff
 vocabulary with the field's named patterns. Numeric budgets, runtime traces,
-and enforcement belong to a serving runtime and stay out of scope here.
+durable write-ahead logs (WAL), event reduction, and persistence enforcement
+belong strictly to a host serving runtime and stay out of scope here. Prompt text
+must never be treated as a durable write-ahead log, and ephemeral skill state
+must never be confused with authoritative durable facts.
```

**Surface:** `reflective-prompt-library/04-agent/workflow-recipes.md`
**Guard:** `plans/tests/test_flow_pack_adoption_state.py` (presence of `durable write-ahead logs (WAL)` / `Prompt text must never be treated as a durable write-ahead log`)

### AH-20b — `04-agent/workflow-engine.md` `## 4. State Model` (durable facts vs derived projections)

```diff
 ## 4. State Model
 定義：
 - state fields
+- durable facts vs derived projections (state fields define operational contracts; durable facts require host persistence, not prompt context)
 - persisted artifacts
 - checkpoint points (recovery contracts specifying the next safe action per failure window)
 - resume behavior (distinguish pure reducer replay from external side-effect re-execution)
```

**Surface:** `reflective-prompt-library/04-agent/workflow-engine.md`
**Guard:** same `test_flow_pack_adoption_state.py` extended

### AH-21a — `04-agent/runtime-trust-boundary.md` `## 4a. External Effect Recovery Boundary` (data protection row)

```diff
 | Durable progress | intent committed, dispatch committed, receipt committed, reducer/projector advanced |
+| Data protection | credentials, bearer tokens, and sensitive PII redacted from durable intent/receipt payload logs |
```

**Surface:** `reflective-prompt-library/04-agent/runtime-trust-boundary.md`
**Guard:** `plans/tests/test_agent_harness_convergence_survey_record.py` (presence of `Data protection` row)

### AH-21b — `skills/agent-governance-scaffold/SKILL.md` `## 4a. External Effect Recovery Boundary` equivalent rule (Never: no raw secrets in durable artifacts)

```diff
 Never:
+- Never store raw credentials, plaintext authentication tokens, or unredacted personal data (PII) inside durable intent payloads, broker receipts, or audit records; apply secret scrubbing and data-sanitization before committing contract artifacts (cross-ref: `04-agent/runtime-trust-boundary.md` §3).
 - Never claim TeaPrompt enforces the four powers ...
```

**Surface:** `reflective-prompt-library/skills/agent-governance-scaffold/SKILL.md`
**Guard:** `plans/tests/test_agent_governance_scaffold_adoption_state.py` (presence of `Never store raw credentials`)

> No other file is touched by this panel. In particular: no edit to `PROJECT_KNOWLEDGE.md` Standing Non-Goals, no edit to 9 core skill contracts, no edit to `SKILL_TRIGGER_CHEATSHEET.md` / `ROUTING_CONTRACT.md`. Those omissions are intentional — see Shared Findings.

## Shared Findings

- **Prompt wording cannot fix execution-layer failures.** WAL, durable program counter, outbox/inbox, and fencing are host-storage/network primitives; prompt text cannot `fsync`, cannot hold a transactional lock, cannot fence a lease. (`PROJECT_KNOWLEDGE.md:63-68` Lesson 1; packet §[INFERENCE] — observed)
- **Skill topology is bounded and orthogonal.** 9 frozen core skills + 3 host-invoked domain packs already satisfy artifact-promotion gate §4; durability-awareness lives in `runtime-trust-boundary.md §4a` + `reflective-risk` OUTCOME_UNKNOWN + `whole-project-plan` triggers, not in a new skill. (observed — `skill-map.md`, `validate_skill_examples.py`, `validate_governance.py`)
- **Prior in-place repairs are sufficient.** AH-18 (reference docs) + AH-19 (OUTCOME_UNKNOWN / sink-scoped retry proof / fencing scope in 5 skills + trust-boundary lens) already cover the legitimate prompt-layer invariants. Adding generic WAL wording would duplicate them without new failure signal. (observed — survey ledger, `test_agent_harness_convergence_survey_record.py`)
- **Flow templates disclaim durability by design.** `flow-control-generator` / `flow-loop-harness` `Never` clauses state `state/` is host-honored resume convention only; `agent-governance-scaffold` disclaims enforcement/host preconditions. Those disclaimers are load-bearing, not to be removed. (observed — SKILL.md Never)
- **Small-Change Fast Path and trigger routing must be preserved.** Scattering durable-state keywords across core skills breaks intent normalization and causes ROUTE-002/003 collisions; trivial edits must stay trivial. (observed — `reflective-implement` Fast Path, `SKILL_TRIGGER_CHEATSHEET.md`, `ROUTING_CONTRACT.md`)
- **Evidence tier remains study/reference.** Prior survey’s executed tier was local unit tests (Pi 135, Maka 40, Amplio event-loop); no power-loss, partition, or real-sink replay proof. Treating it as deployment proof would be tier inflation. (observed — packet §Evidence Actually Checked)

## Disagreements / Residual Risks

- **Architecture vs Usability tension (resolved as AGREE WITH CHANGES):** Architecture lens wanted explicit anti-collapse wording; Usability lens warned against ceremony. Synthesis keeps only two surgical anti-collapse sentences (AH-20) — no new ceremony, no new skill, no change to fast path.
- **Provenance sanitization (resolved as narrow AH-21):** Security lens wanted broader PII/credential hygiene. Adopted only the minimal “redact before persisting durable intent/receipt” rows — no new retention/privilege system, no new pack.
- **Effect-type taxonomy / 9-layer / benchmark:** Remains study-only. Effect flags are host-runtime type contracts; nine-layer is discussion diagram, not canonical stack. Benchmark stays trigger-gated (AH-14). Promoting them now would be prompt theater.
- **Residual:** Host runtime still needed to enforce WAL/replay/fencing/OUTCOME_UNKNOWN reconciliation; any skill-doc drift without guards will silently reintroduce “prompt = durability” folklore.

## Candidate Adoption Ledger

| ID | Candidate | Status | Evidence | Next action / trigger |
|---|---|---|---|---|
| AH-20 | Clarify in `workflow-recipes.md` & `workflow-engine.md` that durable facts/WAL/event-reduction are host-runtime only (anti-collapse) | **Adopted** 2026-08-25 | 7 lenses confirm orthogonality; workflow recipes conflated prompt state with durable truth | Guard in `test_flow_pack_adoption_state.py`; revert only if host runtime proves prompt state is durable (falsifier never hit) |
| AH-21 | Redact secrets/PII before persisting durable intent/receipt payloads (trust-boundary + governance scaffold) | **Adopted** 2026-08-25 | Provenance lens: durable registries risk credential leakage without scrubbing | Guard in `test_agent_harness_convergence_survey_record.py` + `test_agent_governance_scaffold_adoption_state.py`; re-litigation only with new host evidence |
| AH-22 | New 10th core skill for durable-state / WAL / program counter | **Rejected** / Standing Non-Goal 2026-08-25 | No 3-recurrence gate; 9 frozen skills + host-runtime non-goal | Re-litigation needs explicit human + recurrence + host enforcement owner |
| AH-23 | Merge domain packs into one orchestrator pack | **Rejected** 2026-08-25 | Packs have distinct execution topologies; merge increases ceremony | Re-litigation via `reflective-minimality` with usage evidence |
| AH-24 | Effect-type taxonomy / 9-layer as canonical skill contract | **Deferred / study-only** 2026-08-25 | No host enforcement owner; remains reference architecture | Needs host spec + enforcement test before skill promotion |
| AH-25 | Parallel doc+skill bulk update without ledger/guard | **Rejected** 2026-08-25 | Violates A1/A3 drift discipline | Only via ledger + guard path |

## Evidence Actually Checked

- **Coordinator-executed (observed):** `git rev-parse 4c604b1`, `branch main`, packet SHA `52cf6fa9...`, reads of `review-packet-durable-skills-flows-2026-08-25.md`, `skill-map.md`, `PROJECT_KNOWLEDGE.md`, `workflow-recipes.md:108-135`, `workflow-engine.md:1-60`, `runtime-trust-boundary.md:80-130`, `agent-governance-scaffold/SKILL.md:40-70`, `agent-harness-convergence-survey-2026-08-25.md`, guard tests listed above.
- **Read by lenses (observed):** All 7 lenses read packet before inspection; each reported ≥3 findings + ≥3 Socratic questions + steelman + verbatim verdict (AGREE WITH CHANGES ×5, AGREE ×2).
- **Inferred (marked):** That prompt wording could by itself provide crash-safety/idempotency/fencing — refuted as `[INFERENCE]` in ≥3 lenses.
- **Not executed:** No skill edits in lens phase, no `make all`, no power-loss / real-sink replay harness — such evidence would be host-runtime tier, not prompt tier.

## Falsifiability

This record is wrong and must be re-litigation if: (1) a host runtime demonstrates 3 cross-session recurrences where TeaPrompt prompt text prevented a duplicate external effect without host enforcement; (2) `test_flow_pack_adoption_state.py` or `test_agent_governance_scaffold_adoption_state.py` guards fail while durable wording is absent; (3) a deferred candidate gains a host enforcement owner + ledger + guard and still claims to be study-only.
