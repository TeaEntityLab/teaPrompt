# Agent Governance Scaffold — Domain-Pack Adoption Record — 2026-07-17

> **Status: decided (non-authoritative); user-directed adoption record.** Records
> the decision to admit one script/artifact-generation skill,
> `agent-governance-scaffold`, as a registered **domain pack** (not a tenth core
> workflow skill) operationalizing the user-provided *代理治理四權架構 spec
> v1.1-RC1*. Authority chain unchanged: `06-repo/AGENTS.md` and the invoked
> `SKILL.md` contracts govern; this record is evidence, not an operating rule. If
> it and a governed surface disagree, the governed surface wins.

## Purpose

The user instruction was: *"Perfect implement features into skills and record the
concepts into plans"*, attaching the four-power agent-governance spec. This record
is the admission decision for the skill half; the concept half is
[agent-governance-four-power-concepts-2026-07-17.md](agent-governance-four-power-concepts-2026-07-17.md).

## Acceptance provenance

**Composite self-acceptance (disclosed):** on 2026-07-17 one host session authored
the skill, the concepts record, this adoption ledger, the structural guards, the
registry/discoverability edits, and the `make all` evidence below — proposer and
acceptor were the same session, the exact §8 composite-self-acceptance shape the
spec warns about. The explicit user instruction supplied human approval; no
independent review ran before landing. The first independent acceptance layer is
a post-land six-lens panel of 2026-07-18 — see
[panel record](agent-governance-scaffold-panel-record-2026-07-18.md); its adopted
changes are ledgered there (R1–R16; R17 fired-partial on the lite-ad schema track with runtime rig deferred; R18–R24 closure rows). Recurrence remains `unknown`.


## Decision

**AGREE WITH CHANGES** — admit `agent-governance-scaffold` under the Option B
domain-pack registry split (the same mechanism the 2026-07-11 flow-control pack
used), never as a tenth core workflow skill and never on the `reflective-dispatch`
route table.

Rationale, following the binding admission rule in
[`06-repo/AGENTS.md`](../06-repo/AGENTS.md) item 3 and the precedent in
[flow-control-pack-panel-record-2026-07-11.md](flow-control-pack-panel-record-2026-07-11.md):

- **Class fit `[INFERENCE]`.** The spec is written as an implementation brief: §15 is literally
  a "minimal reproducible skeleton", §14.3 lists "declarable features and roadmap
  items", and §5/§6/§10/§11 give ready-to-land object contract templates. That is a
  *host-operationalized artifact generator* — the same class as
  `flow-control-generator`, not a reasoning workflow. It belongs in a domain
  pack, not core routing.
- **Not a core skill.** The nine-skill routing surface is unchanged; the frozen
  core promotion gate (three-recurrence + explicit human approval) is untouched.
  A governance-artifact generator is not a reasoning-workflow route.
- **User-directed exception.** Per the established precedent, an explicit user
  instruction supplies the human-approval component of the domain-pack admission
  rule; recurrence evidence stays `unknown` (no prior local recurrence is on
  record), never recorded as proof of recurrence. **Local structural gap:**
  `unknown` — no verified local recurrence or gap assessment exists beyond class
  fit and the explicit instruction; this is not a STORM-grade verified gap.
- **TeaPrompt operates no runtime.** The skill emits governance *scaffolding*
  (contract files, typed contract templates, mutation-check stubs) for a host to run and
  enforce. TeaPrompt does not become an effect broker, policy engine, verifier
  service, or approval runtime. The spec's brokers/verifiers/policy engines are
  host responsibilities; the skill only writes their contracts.

### Rejected alternatives

- **Tenth core skill** — rejected: violates the frozen-nine gate; a governance
  scaffolder is not a reasoning-workflow route.
- **Fold into `flow-control-generator`** — rejected: disjoint trigger (governance
  artifacts vs flow scripts), disjoint object vocabulary, and a merged contract
  would blur the machine-readable `human_review_required: true` (this pack gates
  on high-risk auth/permission/policy artifacts) against the generator's `false`.
- **Build a TeaPrompt runtime that enforces the four powers** — rejected: Standing
  Non-Goal (no TeaPrompt-owned runtime); the spec itself assigns
  broker/verifier/policy enforcement to the host.
- **`skills/packs/` nesting** — rejected as a bad-faith glob evasion, exactly as
  the 2026-07-11 panel ruled.

## Candidate Adoption Ledger

| # | Candidate | Status | Evidence | Next action / trigger |
| --- | --- | --- | --- | --- |
| G1 | Register `agent-governance-scaffold` as a domain pack (Option B): add to `DOMAIN_PACK_SKILLS`, self-label in body, no core context-load row | Adopted 2026-07-17 (user-directed; recurrence `unknown`) | `plans/validate_skill_examples.py`, `plans/validate_governance.py`, skill body Type line | none |
| G2 | `SKILL.md` with Module Contract (Trigger/Methods/Output/Never/Escalation), Demotion Triggers, Prompt Sources provenance disclaimer | Adopted 2026-07-17 | `skills/agent-governance-scaffold/SKILL.md`; guard `test_skill_module_contract.py` | none |
| G3 | Worked example file ≥ 200 chars | Adopted 2026-07-17 | `skills/examples/agent-governance-scaffold.examples.md`; guard `test_validate_skill_examples.py` | none |
| G4 | Structural adoption-state guard for the pack's named contracts | Adopted 2026-07-17 | `plans/tests/test_agent_governance_scaffold_adoption_state.py` | none |
| G5 | Discoverability: skill-map row + EN/zh-TW cheatsheet appendix bullet; **no** dispatch route row | Adopted 2026-07-17 | `skills/skill-map.md`, both cheatsheets; guards `test_skill_map_lists_domain_packs`, `test_en_cheatsheet_domain_pack_appendix_lists_registry`, `test_t2_zh_tw_pack_appendix_parity_when_present` | none |
| G6 | Install helpers list the pack; `SKILL_INSTALLATION.md` registry + loops updated | Adopted 2026-07-17 | `reflective-prompt-library/SKILL_INSTALLATION.md`; guard `test_installation_defaults_to_core_and_opts_into_registered_packs` | none |
| G7 | Concepts recorded in a plan with feature→artifact map | Adopted 2026-07-17 | `plans/agent-governance-four-power-concepts-2026-07-17.md` | none |
| G8 | Decision Index + QUALITY_GATES counts updated (three domain packs) | Adopted 2026-07-17 | `PROJECT_KNOWLEDGE.md`, `plans/QUALITY_GATES_SUMMARY.md` | none |
| G9 | Governance-pack / core collision holdouts (ROUTE-002/003) | Deferred 2026-07-18 — measure before any router or boundary quick-cue tune | No pre-tune observation recorded for govern/gate/approval/constrain/make-safe phrasing against core workflows | Re-open on a TeaPrompt-local misroute of that vocabulary among `reflective-risk`, `reflective-spec-plan`, and the host-invoked pack, or a documented discoverability failure attributable to missing holdout coverage; ≥3 fresh holdout groups + pre-tune observation per `ROUTING_CONTRACT.md` R8 before tuning `route_paraphrase_eval.py`, quick cues, or dispatch rows; if no fire event occurs by the 2026-10-11 checkpoint, record a proceed/hold/close re-litigation with the zero-invocation demotion review |

## Demotion Triggers

- **Minimality / recurrence checkpoint (2026-10-11)** — a first lite-ad solo emit
  (2026-07-17; see `agent-governance-scaffold-field-use-panel-2026-07-17.md`) falsifies
  the zero-use leg only; it does **not** clear the checkpoint. Re-litigate minimality
  compliance + recurrence; if still unused or still oversized without an adopted shrink,
  demote to a concepts-plan reference section and remove `agent-governance-scaffold`
  from `DOMAIN_PACK_SKILLS` with the full surface unwind (registry, guards, cheatsheets,
  install docs).
- **Host absorbs the pattern** — a target host shipping an equivalent enforced
  four-power governance surface (broker + policy engine + constitutional paths as
  first-party primitives) folds this pack back into
  `agent-governance-four-power-concepts-2026-07-17.md` and retires it.
- **Emitted-scaffold drift** — when the host broker, policy, or effect model
  changes, regenerate from the Artifact Set; a patched drifted copy is not the
  pack's output.

## Evidence Actually Checked

- **Executed (this session; author-claimed relative to any future reader — re-run
  `make all` to reproduce):** `make all` green before the change (929 pytest +
  all validators + ROUTE-001/002/003). After the change, `make all` re-run green
  with the new pack registered (three domain packs); the new skill validated by
  `lint_skills.py`, `validate_governance.py`, `validate_links.py`,
  `validate_skill_examples.py`, and `validate_record_hygiene.py`; the skeleton the
  skill's Output contract describes is a static artifact set (no runtime).
  Structural admission evidence = the validator/guard pass set above plus a
  schema-parse smoke (all fenced YAML/JSON objects parse); `validate_skill_examples.py`
  checks example **file presence** (≥200 chars), not example↔output parity.
  **Semantic correctness of emitted scaffolding on invocation is author-claimed,
  not reproduced — no invocation-level rig was run in the authoring session.**
- **Read (targeted):** the user-provided spec attachment; the flow-control pack
  precedent (`flow-control-pack-panel-record-2026-07-11.md`,
  `agent-flow-control-research-2026-07-11.md`); the Option B guards
  (`validate_skill_examples.py`, `validate_governance.py`, `test_readme_governance.py`,
  `test_quality_gates_summary.py`, `test_dormant_*`,
  `test_flow_pack_adoption_state.py`); `06-repo/AGENTS.md` admission rule;
  `runtime-trust-boundary.md`.
- **Not verified:** the spec's theory attributions and empirical hypotheses
  (H1–H6) are architecture-tier proposals the spec itself defers to unrun
  experiments; this record does not upgrade their tier.

## Disagreements / Residual Risks

- **Minimality dissent `[INFERENCE]`:** a reviewer could hold that the governance
  scaffold is documentation, not a skill, and belongs only in the concepts plan.
  Ruled against: the spec's §15 skeleton is a *generator* contract (per-CLI
  wrapper, run interface, typed contract templates), which is action, not reference —
  the same reasoning that admitted the flow packs. Dissent preserved; re-litigate if
  the 2026-10-11 checkpoint finds no recurrence beyond the first lite-ad emit.
- **Runtime-boundary risk:** the biggest failure mode is the skill implying
  TeaPrompt *enforces* the four powers. Mitigated in the skill's Purpose, Never,
  and Escalation: the pack emits host-run scaffolding only; brokers, verifiers,
  policy engines, and approval gates are host responsibilities; high-risk
  auth/permission/policy artifacts route to `reflective-risk` and Human Review.
- **Recurrence unknown:** every utility claim beyond "the scaffold validates" is
  `[INFERENCE]` until a real task invokes it. `human_review_required: true` is a
  declaration; the host enforces it.

## Falsifiability

This record is wrong if: the pack's guards pass while the skill directory is
unregistered; the skill body omits its domain-pack self-label or claims a core
context-load row; the skill implies a TeaPrompt-owned enforcement runtime; or the
adopted ledger rows (G1–G8) are absent from their named surfaces. Any of those
means the admission ritual failed and the Option B discipline must be re-applied.

## Prompt / Source Pointers

- User-provided spec *代理治理四權架構 v1.1-RC1* (attachment, 2026-07-17).
- [agent-governance-four-power-concepts-2026-07-17.md](agent-governance-four-power-concepts-2026-07-17.md) — concepts + feature→artifact map.
- [flow-control-pack-panel-record-2026-07-11.md](flow-control-pack-panel-record-2026-07-11.md) — the domain-pack admission precedent this decision follows.
- [../06-repo/AGENTS.md](../06-repo/AGENTS.md) — binding domain-pack admission rule (item 3).
- [../04-agent/runtime-trust-boundary.md](../04-agent/runtime-trust-boundary.md) — instruction/data/least-privilege lens.
