# Whole-Project Plan — TeaPrompt (2026-07-11)

> **Status: active planning artifact (non-authoritative).** This plan consolidates
> the project's current state, workstreams, and open-work register into one place
> after the four earlier whole-project plans were retired as historical records on
> 2026-07-11. It is a `plans/`-layer record, not an operating-rule source: agent
> operating rules live in [`06-repo/AGENTS.md`](../06-repo/AGENTS.md) and invoked
> [`skills/*/SKILL.md`](../skills/skill-map.md) contracts; durable direction and
> non-goals live in [`PROJECT_KNOWLEDGE.md`](../PROJECT_KNOWLEDGE.md). If this plan
> and a governed surface disagree, the governed surface wins.
>
> Companion scheduling artifact: [whole-project-roadmap-2026-07-11.md](whole-project-roadmap-2026-07-11.md).

## Why

- The previous planning artifacts ([build plan](prompt-library-build-plan.md),
  [agent workflows](agent-workflows-plan.md), [code follow-ups](code-followups-plan.md),
  [runtime governance learning](runtime-governance-learning-plan-2026-06-11.md)) are all
  retired; their milestones are complete and recorded in the
  [Decision Index](../PROJECT_KNOWLEDGE.md#decision-index).
- Open work now lives scattered across panel records as deferred candidates with
  named triggers (P6/P7/P12/P13/P15, M4–M7, E2, D4, N8, June backlog). Nothing
  aggregates them, so trigger drift — the failure mode every panel record's
  falsifiability clause warns about — is the main planning risk.
- This plan aggregates; it does not re-decide. Every row points at the record that
  owns the decision.

## What (scope)

- In scope: current-state snapshot with evidence, per-workstream objectives and
  acceptance criteria, a consolidated open-work register, risks, and staleness
  falsifiers.
- Out of scope: new governance rules, new skills or packs, router tuning, changes
  to any deferred item's trigger, and anything listed under
  [Standing Non-Goals](../PROJECT_KNOWLEDGE.md#standing-non-goals). Scheduling
  semantics (cadence / date / trigger / direction gates) belong to the roadmap.

## Current State (evidence snapshot, 2026-07-11)

### Product surfaces

| Layer | Content | State |
| --- | --- | --- |
| `00-core/`–`06-repo/` | Composable prompt sources (thinking, engineering, context, agent, domain, repo templates) | Complete; guarded by contract/cross-link/HR registries in `plans/tests/` |
| `skills/` core | Nine frozen core workflow skills (bounded routing set; frozen = gated, not never) | Complete; 4-field governance metadata on 9/9 ([skill-map](../skills/skill-map.md)) |
| `skills/` packs | Two registered domain packs outside core routing: `flow-control-generator`, `flow-loop-harness` | Adopted 2026-07-11 via user-directed exception; demotion triggers live ([record](flow-control-pack-panel-record-2026-07-11.md)) |
| Routing | Deterministic seeded router + [ROUTING_CONTRACT.md](ROUTING_CONTRACT.md) R1–R12 | ROUTE-001/002/003 at 100% on seeded fixtures (128/114/66 phrases) — regression-guard tier, not semantic proof |
| Governance tooling | `make all`: pytest suite + 9 validators + 3 route evals; CI via `.github/workflows/python-tools.yml` | Green; last recorded full run 782 tests ([necessity record](governance-necessity-panel-record-2026-07-11.md)); re-verified below |
| Docs & distribution | READMEs (EN/zh-TW), [CONTRIBUTING](../../CONTRIBUTING.md), [SKILL_INSTALLATION](../SKILL_INSTALLATION.md) core-only default with opt-in packs, cheatsheets EN/zh-TW | Current as of the 2026-07-11 adoption wave |
| Knowledge layer | [PROJECT_KNOWLEDGE.md](../PROJECT_KNOWLEDGE.md) (principles, direction, lessons, Decision Index), [GLOSSARY](../GLOSSARY.md) playbook | Validated by `validate_project_knowledge.py`; Rounds 69–101 rolled up |
| Evidence archive | `plans/` records + [surveys/](../../surveys/ornith-1.0-survey.md) | Eleven retired records carry historical-status headers (rethink E3) |

### Verification infrastructure (what `make all` runs)

`validate_links.py` (links + SKILL frontmatter incl. required `license`),
`lint_skills.py`, `validate_governance.py` (core/pack registry parity),
`validate_project_knowledge.py` (authority boundary), `validate_benchmark_fixture.py`
(24 golden tasks), `validate_skill_examples.py` (`CORE_SKILLS` ∪ `DOMAIN_PACK_SKILLS`),
`validate_route_fixture.py` (coverage floors: ROUTE-002 ≥ 40 groups / 114 phrases,
ROUTE-003 ≥ 19 groups / 66 phrases), then ROUTE-001/002/003 evals. Details:
[QUALITY_GATES_SUMMARY.md](QUALITY_GATES_SUMMARY.md).

## Operating constraints (pointers, not restatements)

1. Strictness before skills; smallest useful workflow — [dispatch](../skills/reflective-dispatch/SKILL.md).
2. Nine frozen core skills; tenth requires three-recurrence gate + human approval — [AGENTS.md](../06-repo/AGENTS.md#harness-policy-nine-skills).
3. Domain-pack admission is registry-gated with ledger + demotion triggers; packs never enter core routing by implication — same section.
4. Holdout-before-tune (R8); fixture floors only ratchet up — [ROUTING_CONTRACT.md](ROUTING_CONTRACT.md).
5. No owned runtime; skills may declare runtime guarantees but TeaPrompt does not enforce them — [Standing Non-Goals](../PROJECT_KNOWLEDGE.md#standing-non-goals).
6. Promotion needs recurrence evidence; missing usage data is `unknown`, never zero demand — [artifact-promotion](../04-agent/artifact-promotion.md).
7. Adoption guards close per [Adoption Guard Closure](../GLOSSARY.md#adoption-guard-closure); maintenance follows the [Governance Maintenance Playbook](../GLOSSARY.md#governance-maintenance-playbook--治理維護手冊).

## Workstreams

### WS1 — Governance and quality gates (steady state)

- Objective: keep `make all` green from the repository root on every governance or
  routing change; keep coverage floors ratcheting only upward.
- Planned work: playbook items 1–5 as standing cadence; audit adoption-state guards
  against Adoption Guard Closure whenever a ledger row flips.
- Acceptance: CI green; no floor decrease ever lands; every governance-surface
  change gains a Decision Index entry (playbook operational test).
- Verification: `make all`; `validate_project_knowledge.py` warning stream.

### WS2 — Routing and dispatch

- Objective: preserve routing fairness (R1–R12) without untested tuning.
- Planned work: expand ROUTE-002/003 holdouts before any router change (R8);
  build P7 pack-trigger holdout groups when pack routing integration is
  re-litigated; keep cheatsheet quick-cue parity (playbook items 6–8).
- Acceptance: any router tune lands with pre-added holdout evidence in the same
  change; ROUTE evals stay at 100% or the failure is analyzed, not patched around.
- Known unmeasured risk: trigger-phrase collisions ("pipeline", "loop until",
  "orchestrate") between pack triggers and core routes until P7 holdouts exist
  ([pack record §Disagreements](flow-control-pack-panel-record-2026-07-11.md)).

### WS3 — Skills surface (core + packs)

- Objective: hold the bounded core set stable; manage the two packs by evidence.
- Planned work: collect manual pack-usage evidence (T3 below) ahead of the
  2026-10-11 P6/N11 re-litigation; keep pack Module Contracts at full parity
  (N5 guards); no new pack without the AGENTS item-3 admission rule.
- Acceptance: 2026-10-11 review happens with recorded usage evidence or an explicit
  `unknown` verdict; registry parity tests stay green.

### WS4 — Prompt library content

- Objective: keep the seven prompt categories contract-complete and cross-linked.
- Planned work: T1 (P15 escalated parity review, below); otherwise drift-repair
  only, guarded by the `plans/tests/` registries (playbook items 10–33).
- Acceptance: per-category eval-harness and registry tests green; any core-skill
  edit passes the frozen-surface gate (human approval).

### WS5 — Adoption and promotion pipeline

- Objective: run external-adoption and promotion reviews with ledgers, preserving
  no-change outcomes so they are not re-litigated.
- Planned work: process trigger-gated candidates (register below) when their
  triggers fire; every future panel/pack record carries a Candidate Adoption
  Ledger and evidence-tier labels (N13 forward rule).
- Acceptance: no candidate adopted without ledger row + named surface + guard;
  no deferred content asserted as adopted (Adoption Guard Closure).

### WS6 — Distribution, docs, localization

- Objective: consumers can install core-only or core+packs deterministically;
  zh-TW navigation surfaces stay in sync.
- Planned work: T2 (zh-TW cheatsheet pack-appendix parity once the EN appendix is
  stable); keep SKILL_INSTALLATION registry parity (N4); README orientation
  section stays deferred (M6) unless the newcomer-orientation gap recurs.
- Acceptance: install helpers produce exactly 9 core + optionally 2 pack
  directories; cheatsheet parity tests green.

### WS7 — Knowledge and archive hygiene

- Objective: Decision Index stays a map, not an archive; plans/ records carry
  honest status headers.
- Planned work: watch undocumented-decision warnings; roll up future mechanical
  round series; E2-class destructive restructuring stays recurrence-gated.
- Acceptance: zero blocking PK validation errors; new records follow the
  historical-header convention when retired.

### WS8 — Evidence and benchmarks

- Objective: keep evidence tiers honest (regression-guard vs advisory vs
  author-claimed).
- Planned work: optional manual `benchmark_tasks.py` baseline-vs-skill runs;
  re-verify `[search-derived]` claims before reliance; N8 meta:product ratio is
  retired unless someone defines and guards a stable formula first.
- Acceptance: no load-bearing claim cites an advisory-tier number without label.

## Consolidated open-work register

Near-term actionable (unblocked today; smallest real work first):

| ID | Task | Source | Acceptance |
| --- | --- | --- | --- |
| T1 | Run the escalated P15 parity review: `reflective-research` Blind Spots parity with `05-domain/research.md`; historical-banner forward pointers in June plans. Outcome may be no-change; any core-skill edit needs the frozen-surface gate. | [flow-coverage record §Deferred](flow-coverage-panel-record-2026-07-11.md) | Review record exists with its own ledger; decision (change/no-change) recorded |
| T2 | zh-TW cheatsheet domain-pack appendix parity, once the EN appendix is stable (no edits between now and the next checkpoint qualifies as stable). | [pack record §Required Changes item 6](flow-control-pack-panel-record-2026-07-11.md) | zh-TW cheatsheet carries the pack section; parity tests green |
| T3 | Establish the manual pack-usage evidence convention (a dated usage-log section in the pack panel record or a small plans/ note per real invocation) so the 2026-10-11 P6 decision is evidential. TeaPrompt has no telemetry; without this, P6 re-litigates on `unknown`. | [necessity record N11](governance-necessity-panel-record-2026-07-11.md) | Convention noted; at least the zero-state recorded before 2026-10-11 |
| T4 | Run the `flow-loop-harness` demotion-trigger evaluation against the now-verified host-native loop surfaces (`/goal` model-judge loop, `/loop`, script-backed Stop hooks). Added 2026-07-11 after the [skills/flow-control survey](../../surveys/agent-skills-flow-control-survey-2026-07-11.md); seed analysis and decision space in the [flow-control roadmap F1](flow-control-roadmap-2026-07-11.md). | [pack record §Demotion Triggers](flow-control-pack-panel-record-2026-07-11.md) | Evaluation record exists with ledger; fired / partially fired / not-fired decision recorded before or at 2026-10-11 |

Date-, trigger-, and direction-gated items are scheduled in the
[roadmap](whole-project-roadmap-2026-07-11.md); this plan does not duplicate the
tables.

## Risks

- **Trigger drift** (highest): deferred items whose triggers fire unnoticed. Mitigation: roadmap checkpoint review; falsifiability clauses in each record.
- **Guard ossification**: adoption-state phrase pins outliving their ledger rows. Mitigation: Adoption Guard Closure audits (WS1).
- **Routing collision debt**: pack trigger phrases unmeasured until P7. Accepted until holdouts exist; documented in both pack records.
- **Evidence-tier laundering**: seeded-fixture 100% or advisory panel votes cited as semantic proof. Mitigation: tier labels required by the packet contract (N13).
- **Single-maintainer bus factor / no usage telemetry**: adoption decisions rest on manually recorded evidence; `unknown` stays `unknown` (T3 reduces, does not remove).

## Falsifiability (staleness triggers for this plan)

This plan is stale and must be revised, retired with the historical header, or
superseded if any of: a Decision Index entry contradicts a workstream objective;
the 2026-10-11 checkpoint passes with no recorded P6 outcome; a trigger-gated item
is adopted without appearing here or in the roadmap; the core-skill count or pack
registry changes; `make all` composition changes materially (validator added or
removed).

## Verification (this plan)

- Authored against: PROJECT_KNOWLEDGE.md, QUALITY_GATES_SUMMARY.md, GLOSSARY
  playbook/closure sections, ROUTING_CONTRACT headings, skill-map, the five
  2026-07-11/07-06 panel and review records, June panel backlog, retired plan
  headers, Makefile, and `validate_project_knowledge.py` warning logic — all read
  this session.
- Mechanical check: `python3 reflective-prompt-library/plans/generate_index.py`
  regenerated and `make all` run green from the repository root after adding this
  file and the roadmap (results recorded in the companion roadmap's Verification
  section).
