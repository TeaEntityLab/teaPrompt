# P7 / N12 Pack-Routing Decision — 2026-07-11

> **Status: decided — no core-router integration.** User-authorized re-litigation
> of P7/N12 after the required ROUTE-002/003 collision holdouts were measured
> pre-tune. This is a `plans/` decision record, not an operating-rule source.
> Canonical boundaries remain in [`06-repo/AGENTS.md`](../06-repo/AGENTS.md),
> [`PROJECT_KNOWLEDGE.md`](../PROJECT_KNOWLEDGE.md), and the registered skill
> surfaces. If this record disagrees with those surfaces, they win.

## Purpose

Close the deferred question: should the nine-core deterministic router and
`reflective-dispatch` route directly to the two registered domain packs after
pack/core collision vocabulary is measured?

## Scope

- In scope: nine new collision phrases, pre-tune observation, fixture adoption,
  floor ratchets, and the route/no-route decision.
- Out of scope: merging the packs (P6), changing a pack contract, adding router
  keywords, adding a tenth core workflow, changing the EN domain-pack appendix,
  or accelerating T2 zh-TW parity.

## Acceptance Criteria

- Fresh ROUTE-002/003 collision phrases are observed against the existing router
  before any router rule change (ROUTING_CONTRACT R8).
- Plan-only pipeline/orchestration intent remains `reflective-spec-plan`.
- Workflow-selection intent remains `reflective-dispatch`.
- Executable flow-script authoring remains `reflective-implement` at the core
  workflow layer; a capable host may invoke the named domain pack directly.
- The pack names remain absent from the core router, route fixtures'
  `expected_workflow` values, `VALID_WORKFLOWS`, and dispatch route table.
- Fixture floors ratchet upward; full `make all` stays green.

## Evidence Actually Checked

Evidence tiers:

- **Regression-guard evidence:** the deterministic seeded router and exact
  fixtures below.
- **Repository fact:** both domain packs are registered as host-invoked and not
  core-routed in AGENTS.md, skill-map, and the EN cheatsheet appendix.
- **Unknown:** real consumer discoverability and invocation distribution; no
  telemetry exists. The decision does not reinterpret `unknown` as zero demand.

Pre-tune observation was run against the unmodified `ParaphraseRouter` using
three temporary fixture groups. No router rule or keyword changed before or
following the observation.

| Group | Fixture | Expected core workflow | Pre-tune result | Adopted phrases |
| --- | --- | --- | --- | ---: |
| `pack_vocab_plan_holdout` | ROUTE-002 | `reflective-spec-plan` | 3/3, 100% | 3 |
| `pack_vocab_route_holdout` | ROUTE-002 | `reflective-dispatch` | 3/3, 100% | 3 |
| `pack_vocab_implement_not_plan_trap` | ROUTE-003 | `reflective-implement` | 3/3, 100% | 3 |

Aggregate: **9/9 phrases routed as expected pre-tune**. The evidence therefore
found vocabulary collision coverage debt, but no router defect requiring a
tune.

## Decision Analysis

- **Claim:** pack-adjacent words (`pipeline`, `orchestrate`, `fan-out`, runnable
  flow script) can preserve equivalent core intent without making packs core
  route targets.
- **Evidence:** all nine fresh phrases passed pre-tune across the three intended
  core outcomes; existing H1/H2 already cover goal-mode and loop-script
  boundaries; the EN appendix already exposes direct host invocation.
- **Unknowns:** whether users who consult only core routing fail to discover the
  packs; whether a future host cannot invoke packs directly.
- **Strongest counterargument:** direct dispatch rows would improve
  discoverability and could avoid the two-layer distinction between core
  implementation intent and host pack selection.
- **Response:** adding route targets changes the bounded core product semantics,
  duplicates host skill selection, creates EN/zh-TW quick-cue obligations, and
  solves no observed misroute. Discoverability already has a dedicated appendix.
- **Decision:** prefer the smaller, already-correct boundary. Preserve core
  workflow routing by artifact intent; preserve packs as host-invoked contracts.
- **Verification:** fixture groups, permanent pack-absence guard, route evals,
  governance validators, and full `make all`.

## Decision

**P7/N12 resolves as no core-router integration.**

1. Adopt the three collision groups into ROUTE-002/003.
2. Raise deterministic floors from 42 groups / 118 phrases to 44 / 124 for
   ROUTE-002, and from 21 groups / 73 phrases to 22 / 76 for ROUTE-003.
3. Make no change to `route_paraphrase_eval.py`, `VALID_WORKFLOWS`, the
   `reflective-dispatch` route table, or cheatsheet quick cues.
4. Keep the EN `Domain packs (host-invoked; not core routing)` appendix as the
   discoverability surface. T2 keeps its independent stability gate.
5. Close the prior "collision remains unmeasured" risk. Do not claim semantic
   routing is solved: 9/9 is seeded regression evidence only.

## Candidate Adoption Ledger

| ID | Candidate | Status | Evidence / surface | Re-open or retirement trigger |
| --- | --- | --- | --- | --- |
| P7-A | Add pack/core collision holdouts | **Adopted 2026-07-11** | Three fixture groups; 9 phrases; floor guards and probe tests | Retain as regression guards; ratchet only upward |
| P7-B / N12 | Add domain packs to core router / dispatch route table | **No-change decided 2026-07-11** | 9/9 correct pre-tune; packs already host-invoked; no observed route defect | Re-open on a documented TeaPrompt-local misroute or discoverability failure attributable to pack exclusion, or a host that cannot invoke registered packs directly |
| P7-C | Add new pack quick cues to the core boundary block | **No-change decided 2026-07-11** | EN domain-pack appendix already owns the distinction; R12 frequency bar not met | Re-open only with the same evidence as P7-B plus quick-cue frequency evidence |

## Verification

Executed evidence:

- focused P7/routing/adoption guards: 122 pytest tests passed;
- `validate_route_fixture.py`: ROUTE-002 floor 44 groups / 124 phrases,
  ROUTE-003 floor 22 groups / 76 phrases;
- ROUTE-002: 44 groups / 124 phrases at 100%;
- ROUTE-003: 22 groups / 76 phrases at 100%;
- permanent guard: pack names absent from the core router, route targets,
  `VALID_WORKFLOWS`, and dispatch route surface;
- repository-root `make all`: 887 pytest tests passed; 146 files passed
  link/schema validation; linter 146 files / 0 errors / 0 warnings; all 11
  registered skills valid; ROUTE-001/002/003 each 100%.

## Falsifiability

Re-open this decision if a TeaPrompt-local request is demonstrably misrouted or
cannot discover/invoke the appropriate pack because packs are excluded from core
routing; if a supported host cannot invoke registered packs directly; or if any
of the nine collision phrases stops routing to its named core workflow. The
re-open requires a successor decision record and fresh holdouts before tuning.

This record is wrong if pack names enter the core route table or
`VALID_WORKFLOWS` while P7-B remains no-change; if the adopted groups disappear
or floors shrink; or if 9/9 seeded consistency is cited as proof of broad
semantic routing quality.
