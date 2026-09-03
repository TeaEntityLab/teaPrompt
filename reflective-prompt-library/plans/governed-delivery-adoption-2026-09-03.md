# Governed Delivery — Feature Adoption Record — 2026-09-03

> **Status: decided (non-authoritative); user-directed adoption record.** Records the decision to implement the governable-autonomous-delivery feature set in TeaPrompt skills at feature depth: phase-local features land in the core skill that runs that phase; system-level features land in one new registered **domain pack**, `governed-delivery` (not a tenth core workflow skill). Authority chain unchanged: `06-repo/AGENTS.md` and the invoked `SKILL.md` contracts govern; this record is evidence, not an operating rule. If it and a governed surface disagree, the governed surface wins.

## Purpose

The user instruction was: *"I want Governable Autonomous Delivery's features as possible implemented in skills. reconsider the best proper ways."* It follows the same-day survey ([governable-autonomy-survey-2026-09-03.md](governable-autonomy-survey-2026-09-03.md)) that adopted GA-1–GA-9 as narrow sentences, and the same-day all-skills panel ([ga-skills-coverage-panel-2026-09-03.md](ga-skills-coverage-panel-2026-09-03.md)) that chose minimality (two Never sentences, no extra skill). Those decisions optimized for minimality under "if worth it". This instruction changes the objective to coverage. This record supersedes the panel's XS-8 (narrowed) and XS-9 (rejected) rows **by explicit user direction**; recurrence remains `unknown`.

## Acceptance provenance

**Composite self-acceptance (disclosed):** one host session reconsidered the options, authored the pack, deepened nine core skills through parallel workers, wrote this ledger, the guards, and the registry edits, and ran `make all`. Proposer and acceptor were the same session; the explicit user instruction supplied human approval. No independent review ran before landing; the first independent acceptance layer is a future Parallel Lens Review (see Demotion Triggers).

## Reconsidered options

| Option | Shape | Verdict | Why |
| --- | --- | --- | --- |
| A | Feature-depth absorption into the nine core skills only | Partial | Right home for phase-local features; wrong home for the gate sequence, contract set, envelope, and refuters — scattering them across nine files destroys the feature |
| B | One new domain pack only | Partial | Right home for system-level features; leaves brief/spec/implement/review/risk/handoff without the discipline they run day to day |
| C | A + B, layered | **Adopted** | Each feature lands where the task that needs it runs; the pack composes the lifecycle and declares host preconditions; exact precedent: `agent-governance-scaffold` (user-directed, recurrence `unknown`) |
| D | Extend an existing pack | Rejected | `agent-governance-scaffold` is already above the lint length threshold and owns effect authority, not the delivery lifecycle; the flow packs own control flow |
| E | Tenth core skill | Rejected | `06-repo/AGENTS.md` Harness Policy item 3: a user-directed exception admits a domain pack and never waives the tenth-core promotion gate |
| F | TeaPrompt runtime, context compiler, outbox, sandbox | Rejected | Standing Non-Goal; prompt text cannot seal, isolate, or persist — declared as host preconditions instead |

## Design limits honored (not refusals; design choices)

- **Clean-room.** The corpus is unlicensed; every feature is restated in TeaPrompt vocabulary. No lettered ladders, practice numbers, checklist tables, inequality strings, arXiv identifiers, or vendor figures appear on any skill surface.
- **No fourth lettered ladder.** Autonomy is expressed through the existing strictness ladder and Gate 2.0 thickness; the pack states this verbatim.
- **No universal retry count (ATT-7).** Failure-signature limits and budgets are task-declared in the envelope.
- **No standalone assumption ledger (Hyperplan 2026-06-21).** Assumption status lives inside `reflective-brief` and the pack's `intent-record` template, not as a separate skill or core surface.
- **P7.** The pack is discoverable (skill-map, cheatsheet appendices, install helpers) and never appears on `reflective-dispatch` route rows or ROUTE fixtures.
- **Small-Change Fast Path** in `reflective-implement` is untouched.

## Feature → destination map

| ID | Feature (TeaPrompt restatement) | Destination | Anchor |
| --- | --- | --- | --- |
| GD-1 | Intent fidelity: name what the spec will not capture; assumption status with `stale` propagation | `reflective-brief` | A1, A2 |
| GD-2 | Oracle manifest: class, owner, host sealing precondition, change protocol | `reflective-spec-plan`; pack `oracle-manifest` | B1 |
| GD-3 | Spec version; mid-task change marks dependents `stale` | `reflective-spec-plan`; pack `spec` gate, GDR-6 | B2 |
| GD-4 | Task packet / continuation packet, never the transcript | `reflective-implement`, `reflective-handoff-retro`; pack `task-packet`, GDR-4 | C1, G1 |
| GD-5 | Failure signature and its three exits | `reflective-implement`; pack `failure-log`, GDR-3 | C2 |
| GD-6 | Verification channels and independence; high-risk PASS needs a non-model channel | `reflective-review`; pack `verification-plan`, GDR-5 | D1 |
| GD-7 | Evidence entry fields: claim, source, attester, freshness kind, date | `reflective-research`; pack `evidence-ledger` | E1 |
| GD-8 | Sink inventory and unattended envelope | `reflective-risk`; pack `envelope`, GDR-2 | F1, F2 |
| GD-9 | Acceptance record by a named accepter; execution success never closes | `reflective-spec-plan`; pack `acceptance-record`, `acceptance` gate | B3 |
| GD-10 | Gate retro; policy change separate from activation | `reflective-handoff-retro`; pack `gate-retro`, `retro` gate | G2 |
| GD-11 | Governance ceremony faces delete-before-add | `reflective-minimality` | H1 |
| GD-12 | Delivery gate sequence (`intent`, `spec`, `plan`, `execution`, `verification`, `acceptance`, `retro`) with releaser and evidence tier | pack | — |
| GD-13 | Autonomy envelope without a new ladder | pack | — |
| GD-14 | Delivery invariants (restated) | pack | — |
| GD-15 | Host preconditions: sealing, sink isolation, budget enforcement, durable ledgers, human decision channel | pack | — |
| GD-16 | Adversarial refuters GDR-1–GDR-6 as host-run checks, `unknown` until run | pack | — |
| GD-17 | Pack admission surfaces: registry, self-label, examples, skill-map, cheatsheets, install helpers, guard | repo | — |

Host-only, declared not implemented: oracle sealing, sandbox and egress control, credential brokering, durable ledger storage, context compilation, fault injection in TeaPrompt CI, exactly-once external effects.

## Candidate Adoption Ledger

| # | Candidate | Status | Evidence | Next action / trigger |
| --- | --- | --- | --- | --- |
| GD-1 | Intent fidelity + assumption status in `reflective-brief` | Adopted 2026-09-03 (user-directed; recurrence `unknown`) | anchors A1, A2; guard `test_governed_delivery_adoption_state.py` | none |
| GD-2 | Oracle manifest in `reflective-spec-plan` and pack | Adopted 2026-09-03 | anchor B1; pack `### oracle-manifest` | none |
| GD-3 | Spec version + `stale` propagation | Adopted 2026-09-03 | anchor B2; pack GDR-6 | none |
| GD-4 | Task packet / continuation packet | Adopted 2026-09-03 | anchors C1, G1; pack `### task-packet`, GDR-4 | none |
| GD-5 | Failure signature and exits | Adopted 2026-09-03 | anchor C2; pack `### failure-log`, GDR-3 | none |
| GD-6 | Verification channels | Adopted 2026-09-03 | anchor D1; pack `### verification-plan`, GDR-5 | none |
| GD-7 | Evidence entry fields | Adopted 2026-09-03 | anchor E1; pack `### evidence-ledger` | none |
| GD-8 | Sink inventory + unattended envelope | Adopted 2026-09-03 | anchors F1, F2; pack `### envelope`, GDR-2 | none |
| GD-9 | Acceptance record | Adopted 2026-09-03 | anchor B3; pack `### acceptance-record` | none |
| GD-10 | Gate retro | Adopted 2026-09-03 | anchor G2; pack `### gate-retro` | none |
| GD-11 | Minimality test for governance ceremony | Adopted 2026-09-03 | anchor H1 | none |
| GD-12 | Delivery gate sequence | Adopted 2026-09-03 | pack `## Delivery Gate Sequence` | none |
| GD-13 | Autonomy envelope, no new ladder | Adopted 2026-09-03 | pack `## Autonomy Envelope` | none |
| GD-14 | Delivery invariants | Adopted 2026-09-03 | pack `## Delivery Invariants` | none |
| GD-15 | Host preconditions | Adopted 2026-09-03 | pack `## Host Preconditions` | none |
| GD-16 | Adversarial refuters | Adopted 2026-09-03 (contracts only; all six `unknown`) | pack `## Adversarial Refuters` | Run on the first named host harness; record pass/fail per GDR |
| GD-17 | Pack admission surfaces | Adopted 2026-09-03 | `DOMAIN_PACK_SKILLS`, Type line, examples, skill-map, EN/zh-TW cheatsheets, `SKILL_INSTALLATION.md`, guard | none |
| GD-18 | Independent post-land panel | Deferred | Composite self-acceptance disclosed above | Run a Parallel Lens Review before the 2026-10-11 checkpoint |
| GD-19 | Collision measurement for "deliver / autonomous / unattended" vocabulary against core routes | Deferred | No pre-tune observation recorded | Same rule as G9: ≥3 fresh holdout groups before touching quick cues or fixtures |

## Demotion Triggers

- **Recurrence checkpoint (2026-10-11)** — zero observed host invocations of `governed-delivery` by the checkpoint → demote: fold the gate sequence, contract set, and refuters into a reference section of this record and remove the pack from `DOMAIN_PACK_SKILLS` with the full surface unwind (registry, examples, skill-map, cheatsheets, install helpers, guard).
- **Host absorbs the pattern** — a target host shipping enforced gate sequencing, oracle sealing, and acceptance records as first-party primitives retires the pack.
- **Contract drift** — when the host's oracle, sink, or ledger model changes, regenerate from the Contract Set; a patched drifted copy is not the pack's output.
- **Core-skill regression** — if any deepened core skill trips a lint length warning or a ROUTE fixture regresses, shrink that skill's added subsection to its anchor sentence.

## Evidence Actually Checked

- **Observed (this session):** twelve prior `SKILL.md` Module Contracts; registry-driven guard set (`test_readme_governance.py`, `test_dormant_item_watch.py`, `test_validate_governance.py`, `test_skill_module_contract.py`, `test_quality_gates_summary.py`) confirming most pack surfaces follow `DOMAIN_PACK_SKILLS`; `validate_governance.py` self-label rule; `lint_skills.py` 20,000-char warning threshold; the `agent-governance-scaffold` adoption ledger G1–G9 as the admission precedent.
- **Executed:** recorded in the Completion Ledger after the gates ran.
- **Not executed:** any host run of the emitted contract set; refuters GDR-1–GDR-6; benchmark or fault-injection evidence. All are `unknown`.

## Falsifiability

This record is wrong if: an anchor sentence disappears while its guard passes; the pack appears on a `reflective-dispatch` route row or ROUTE fixture; a skill surface carries a lettered ladder, practice number, arXiv identifier, or vendor figure from the corpus; a refuter is reported as passed without a named host run; or the pack reaches the 2026-10-11 checkpoint with zero invocations and no demotion decision.

## Completion Ledger

| Item | Status | Evidence |
| --- | --- | --- |
| Pack `governed-delivery` SKILL.md + examples | `verified` | `skills/governed-delivery/SKILL.md` (14,687 chars, under the 20,000-char lint threshold), `skills/examples/governed-delivery.examples.md` (2,040 chars); governance validator 13/13 |
| Nine core skills deepened (A1–H1) | `verified` | 42 inserted lines, 0 deletions across the nine core skills; every anchor present exactly once; Small-Change Fast Path byte-identical |
| Registry, install helpers, skill-map, cheatsheets | `verified` | `DOMAIN_PACK_SKILLS` = 4; EN/zh-TW install guides and cheatsheet appendices; skill-map row; registry-driven guards passed |
| Deterministic guard | `verified` | `plans/tests/test_governed_delivery_adoption_state.py`: 15 passed |
| Prior guards reconciled | `verified` | `test_ga_skills_coverage_panel_record.py` cardinality 4 with supersession comment; `test_skill_scenario_panel_adoption_state.py` and `test_dormant_conditional_contracts.py` made registry-driven instead of hard-coded 12/4; `QUALITY_GATES_SUMMARY.md` counts 13/13, 9 core + 4 packs, floor 1060+ → 1080+ |
| Decision Index and case-study rows | `verified` | `PROJECT_KNOWLEDGE.md`, `external-adoption-case-studies-2026-06-20.md` |
| Repository verification | `verified` | `make all`: 1080 passed; links 174 files / 0 errors; lint 0 errors / 1 pre-existing warning (`agent-governance-scaffold` length, not the new pack); governance 13/13; benchmark 24 tasks / 9 of 9; examples 9 core + 4 packs; ROUTE-001/002/003 100% (16/44/22 groups); no pack on any routing surface (P7 guards) |
