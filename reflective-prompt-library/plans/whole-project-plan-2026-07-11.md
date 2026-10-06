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
  retired; their completed milestones are recorded in the
  [Decision Index](../PROJECT_KNOWLEDGE.md#decision-index). Retired TASK-006 and
  optional OpenFugu tasks have [disposition pointers](dormant-work-specs-2026-07-11.md#domain-and-retired-plan-dispositions-2026-10-01);
  retirement does not mean every historical future task was completed.
- Open work now lives scattered across panel records as deferred candidates with
  named triggers (P6/P12/P13, M4–M7, E2, D4, N8, June backlog). Nothing
  aggregates them, so trigger drift — the failure mode every panel record's
  falsifiability clause warns about — is the main planning risk. P7/P15 are
  resolved and point to successor records below.
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

## Current State (source reconciliation, 2026-10-01; original evidence dated 2026-07-11)

### Product surfaces

| Layer | Content | State |
| --- | --- | --- |
| `00-core/`–`06-repo/` | Composable prompt sources (thinking, engineering, context, agent, domain, repo templates) | Complete; guarded by contract/cross-link/HR registries in `plans/tests/` |
| `skills/` core | Nine frozen core workflow skills (bounded routing set; frozen = gated, not never) | Complete; 4-field governance metadata on 9/9 ([skill-map](../skills/skill-map.md)) |
| `skills/` packs | Five registered domain packs outside core routing: `flow-control-generator`, `flow-loop-harness` (2026-07-11), `agent-governance-scaffold` (2026-07-17), `governed-delivery` (2026-09-03), `verification-map-generator` (2026-09-23) | Registry `DOMAIN_PACK_SKILLS` is the count of truth; owning records: [flow](flow-control-pack-panel-record-2026-07-11.md), [scaffold](agent-governance-scaffold-adoption-2026-07-17.md), [GD](governed-delivery-adoption-2026-09-03.md), [verification map](pstack-survey-2026-09-22.md). **Dated supersession 2026-10-06:** registry now holds six — `headless-agent-cli-contract` admitted (skills/headless-agent-cli-contract, evidence: runtime-skills-task001-ticket-2026-10-06 TASK-004/005 receipts). The five-pack enumeration above is the historical row and stays for record fidelity. |
| Routing | Deterministic seeded router + [ROUTING_CONTRACT.md](ROUTING_CONTRACT.md) R1–R13, including review-led inspection | Current coverage floors live in `validate_route_fixture.py`; prior 128/124/76 phrase snapshot was dated evidence, not current coverage. P7 remains no core-router integration; seeded results are regression-guard tier, not semantic proof. |
| Governance tooling | `make all`: pytest suite + eight validators + 3 route evals; CI via `.github/workflows/python-tools.yml` | Composition reconciled from Makefile; executed results live in [QUALITY_GATES_SUMMARY.md](QUALITY_GATES_SUMMARY.md) and the latest session report, not this source reconciliation |
| Docs & distribution | READMEs (EN/zh-TW), [CONTRIBUTING](../../CONTRIBUTING.md), [SKILL_INSTALLATION](../SKILL_INSTALLATION.md) core-only default with opt-in packs, cheatsheets EN/zh-TW | T2 landed 2026-07-12; pack admission/parity now follows the current registry and `PACK_SURFACES` manifest |
| Knowledge layer | [PROJECT_KNOWLEDGE.md](../PROJECT_KNOWLEDGE.md) (principles, direction, lessons, Decision Index), [GLOSSARY](../GLOSSARY.md) playbook | Validated by `validate_project_knowledge.py`; Rounds 69–101 rolled up |
| Evidence archive | `plans/` records + [surveys/](../../surveys/ornith-1.0-survey.md) | Eleven retired records carry historical-status headers (rethink E3) |

### Verification infrastructure (what `make all` runs)

`validate_links.py` (links + SKILL frontmatter incl. required `license`),
`lint_skills.py`, `validate_governance.py` (core/pack registry parity),
`validate_project_knowledge.py` (authority boundary), `validate_record_hygiene.py`
(forward record hygiene), `validate_benchmark_fixture.py` (24 golden tasks),
`validate_skill_examples.py` (`CORE_SKILLS` ∪ `DOMAIN_PACK_SKILLS`),
`validate_route_fixture.py` (coverage floors as of 2026-10-01: ROUTE-001 ≥12 intent
groups + 4 adversarial groups / 128 phrases; ROUTE-002 ≥48 groups / 138 phrases;
ROUTE-003 ≥32 groups / 108 phrases), then ROUTE-001/002/003 evals. Details:
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

- Objective: preserve routing fairness (R1–R13) without untested tuning.
- Planned work: expand ROUTE-002/003 holdouts before any router change (R8);
  keep cheatsheet quick-cue parity (playbook items 6–8). P7 closed on
  2026-07-11 after three collision groups / 9 phrases passed 100% pre-tune:
  packs remain host-invoked, with no core router or quick-cue integration
  ([decision](p7-pack-routing-decision-2026-07-11.md)).
- Acceptance: any router tune lands with pre-added holdout evidence in the same
  change; ROUTE evals stay at 100% or the failure is analyzed, not patched around;
  pack names remain absent from core route targets unless P7's successor trigger
  fires and a new decision record reverses the no-change outcome.

### WS3 — Skills surface (core + packs)

- Objective: hold the bounded core set stable; manage registered packs by evidence.
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
- Planned work: keep SKILL_INSTALLATION registry parity (N4); T2 zh-TW pack
  appendix and README Orientation were adopted 2026-07-12 as user-directed
  documentation improvements with recurrence recorded `unknown`.
- Acceptance: install helpers produce exactly 9 core + optionally the registered
  pack directories from the current `DOMAIN_PACK_SKILLS` registry; cheatsheet parity tests green.

### WS7 — Knowledge and archive hygiene

- Objective: Decision Index stays a map, not an archive; plans/ records carry
  honest status headers.
- Planned work: watch undocumented-decision warnings; roll up future mechanical
  round series; D4 record-hygiene validation is now forward-enforced for records
  dated ≥2026-07-12; E2-class destructive restructuring stays recurrence-gated.
- Acceptance: zero blocking PK/record-hygiene validation errors; new records follow
  the status/evidence/ledger/falsifiability convention; retired records keep the
  historical-header convention.

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
| T1 | **Done 2026-07-11.** Escalated P15 parity review executed: `research.md` blind-spot acceptance aligned to the STORM-decided none-found contract (prompt-layer; `reflective-research` already conformant, frozen-surface gate not fired); the four retired plans' historical banners gained open-work successor pointers; seven reflection banners no-change → [review record](frozen-core-parity-review-2026-07-11.md). | [flow-coverage record §Deferred](flow-coverage-panel-record-2026-07-11.md) | Met: record + ledger + change/no-change decisions recorded |
| T2 | **Done 2026-07-12 (user-directed; recurrence `unknown`).** zh-TW cheatsheet domain-pack appendix added after explicit user instruction; EN appendix remains the canonical source. | [adoption record](dormant-items-user-directed-adoption-2026-07-12.md) | Met: zh-TW cheatsheet carries the pack section; parity tests green |
| T3 | **Done 2026-07-11.** Manual pack-usage evidence convention established with zero-state recorded → [usage log](flow-pack-usage-log.md). TeaPrompt has no telemetry; the log is the P6 evidence base. | [necessity record N11](governance-necessity-panel-record-2026-07-11.md) | Met: convention + zero-state on record |
| T4 | **Done 2026-07-11 — trigger not fired.** Demotion-trigger evaluation executed against host-native `/goal`/`/loop`/Stop-hook surfaces (verified in the [survey](../../surveys/agent-skills-flow-control-survey-2026-07-11.md)); the model-judge stop fails the pack's deterministic bar; Host-Native Alternatives note added to the loop skill → [evaluation record](flow-pack-demotion-evaluation-2026-07-11.md). | [pack record §Demotion Triggers](flow-control-pack-panel-record-2026-07-11.md) | Met: record + not-fired decision before 2026-10-11 |

Date-, trigger-, and direction-gated items are scheduled in the
[roadmap](whole-project-roadmap-2026-07-11.md); this plan does not duplicate the
tables.

## Risks

- **Trigger drift** (highest): deferred items whose triggers fire unnoticed. Mitigation: roadmap checkpoint review; falsifiability clauses in each record.
- **Guard ossification**: adoption-state phrase pins outliving their ledger rows. Mitigation: Adoption Guard Closure audits (WS1).
- **Routing collision regression:** P7's former unmeasured debt is closed by three groups / 9 phrases at 100% pre-tune; permanent guards keep packs outside core routing. Re-open on the decision record's successor trigger, not on seeded confidence alone.
- **Evidence-tier laundering**: seeded-fixture 100% or advisory panel votes cited as semantic proof. Mitigation: tier labels required by the packet contract (N13).
- **Single-maintainer bus factor / no usage telemetry**: adoption decisions rest on manually recorded evidence; `unknown` stays `unknown` (T3 reduces, does not remove).

## Falsifiability (staleness triggers for this plan)

This plan is stale and must be revised, retired with the historical header, or
superseded if any of: a Decision Index entry contradicts a workstream objective;
the 2026-10-11 checkpoint passes with no recorded P6 outcome; a trigger-gated item
is adopted without appearing here or in the roadmap; the core-skill count or pack
registry changes; `make all` composition changes materially (validator added or
removed).

Fired and reconciled 2026-09-14: the pack registry moved 2→4 (2026-07-17, 2026-09-03)
and thirteen September records adopted trigger-gated items without a queue entry;
this plan's counts and the roadmap's September section were updated in the
[September review](september-skills-review-2026-09-14.md). The clause stays live for
the next drift.

Fired and reconciled 2026-10-01: fifth-pack admission on 2026-09-23 and R13 on
2026-09-24 had outgrown the active layer's four-pack/R1–R12 snapshot. The current
layer and roadmap admission ledger now point to five packs, R13, live route floors,
and the Makefile's record-hygiene validator. The original dated counts and gate
measurements above/below remain historical; this correction asserts source
reconciliation, not a fresh execution result.

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
