# Agent Execution & Assurance Taxonomy Survey — 2026-09-30

> **Status: decided — record-only; AEAT-4 acceptance-oracle join held for a named-product assessment.** This assessment does not adopt a governing taxonomy, portable runtime interface, schema, skill, or project-direction change. The original survey changed session artifacts only; the user subsequently authorized this repository record, Decision Index and Case Comparison pointers, index regeneration, and `make all`. No installation, provider run, product-repository experiment, commit, or push is authorized by this internalization.

## Research Question

Does the supplied discussion accurately distinguish workflow synthesis, fresh-worker loops, execution control, governed delivery, and project-local verification? Do its six-layer and Contract/State/Evidence proposals expose an uncovered TeaPrompt contract? The follow-through also checks the current PS2-3/PS-C1 status and distinguishes general REQ/AC traceability from a joined product-verification consumer.

Scope: bounded source verification and semantic comparison, not a new architecture specification, ecosystem census, product-repo pilot, or production deployment. Assessed 2026-09-30. The supplied 766-line artifact has SHA-256 `bcbb28c323a6715731370f151f4c432accff39dc034d8b1196e700c1ac9d9961`; author and generation process are unknown.

Provenance: the discussion was supplied as session-local `paste-2.md`; the agent-authored session survey was `execution-assurance-taxonomy-survey.md` (SHA-256 `51a1c6acf600314f8874268c3a95810be698ff23438230641b2281e409cf98a9`, minted 2026-09-30, not independently human-reviewed). Those names identify evidence, not runtime dependencies or instructions. This record preserves the findings, source identities, exercised results, and limitations without requiring session-local files. The user's persistence request is not approval to promote the proposals into operating rules. Authority class: non-authoritative research/decision archive.

Acceptance Criteria:
1. Reconcile the original deferred PS2-3/PS-C1 rows with their later pilot and promotion addenda; do not mistake general REQ/AC planning for an established product-verification join.
2. Preserve the session findings in a repository record with explicit provenance, evidence limits, existing decision precedents, and a held acceptance-oracle-join item with a specific trigger and falsifier.
3. Add a Decision Index pointer and a Case Comparison row without changing schemas, skills, adoption states, or unrelated deferred gates.
4. Regenerate the repository index and run `make all`; report the actual results in the delivery message.

## Direct Recommendation

**Agree with the responsibility distinctions; do not adopt the proposed hierarchy or schemas as a standard.** Use the five families as overlapping mechanisms and durable recovery as a cross-cutting runtime contract. `Agent Execution & Assurance Architecture` is a useful proposed umbrella for this discussion, not a verified standard or a reason to replace existing names.

| Proposed family | Useful question | Qualification | Existing TeaPrompt home |
| --- | --- | --- | --- |
| Workflow / plan synthesis | How is work decomposed? | A generated plan is not its execution. A workflow engine can execute, persist, pause, and recover; workflow does not mean only step order. | `flow-control-generator`; `reflective-spec-plan` |
| Fresh-worker / state-driven loop | How is work resumed with a fresh agent context? | Process freshness, mutable-plan ownership, backpressure, and completion authority are distinct. Shared files can carry earlier errors into a fresh context. | `flow-loop-harness` |
| Execution harness / control plane | Who starts, limits, transitions, and stops work? | Gates written into prompts are not host-enforced gates. Goal awareness does not prove truthful completion, durability, or containment. | `reflective-spec-plan` Workflow Design; `04-agent/workflow-engine.md` |
| Governed delivery / SDLC | Who authorizes effects and accepts the product? | Cross-cutting authority, not just a higher rung. Execution success is not business acceptance; independent evidence is not another model's agreement. | `governed-delivery`; `agent-governance-scaffold`; runtime trust boundary |
| Verification surface / feature map | What can a fresh verifier drive and observe? | Navigation, an oracle, evidence, and an acceptance verdict are different responsibilities. Tests can observe behavior; a screenshot is not automatically stronger. | `verification-map-generator`; `reflective-spec-plan` Test Plan Mode |

These are not exclusive classes or a maturity ladder. A durable workflow can contain fresh-worker loops and a feature-map verification stage. A low-risk single-call task need not acquire a durable recorder, broker, or six-plane framework.

## Evidence Used

All following sources checked 2026-09-30. Attesters: coordinator for direct source reads and TeaPrompt native-template smoke; delegated `RalphTaxonomyEvidence` for the pinned Ralph shell probe; delegated `PstackTaxonomyEvidence` for the verification-contract/port inventory, with coordinator source spot-checks.

- [Huntley original Ralph article](https://ghuntley.com/ralph/) (checked 2026-09-30): published 2025-07-14, page metadata modified 2026-02-19. Describes an outer Bash loop, specification/plan reconstruction, one-item guidance, separate planning/building prompts, operator tuning, and configurable test/build backpressure. Author experience and examples are not an external deterministic stopping guarantee.
- [snarktank Ralph shell](https://github.com/snarktank/ralph/blob/6c53cb0b831ebe8739c6a003e22af14902d8b0b5/ralph.sh#L84-L113) (checked 2026-09-30): current checked `main` is `6c53cb0b831ebe8739c6a003e22af14902d8b0b5`, commit dated 2026-02-02. Native completion at line 99 matches a model-emitted promise; the cap exits 1. The model is instructed to maintain PRD/progress and run checks; the shell does not make its stop depend on those checks. MIT; no upstream prompt copied into TeaPrompt.
- [pstack verification generator](https://github.com/cursor/plugins/blob/fae2c6ed95821bd85f614a73e4842e13229fa5e5/pstack/skills/create-verification-skill/SKILL.md), [map template](https://github.com/cursor/plugins/blob/fae2c6ed95821bd85f614a73e4842e13229fa5e5/pstack/skills/create-verification-skill/references/feature-map-example/README.md), and [behavior-testing principle](https://github.com/cursor/plugins/blob/fae2c6ed95821bd85f614a73e4842e13229fa5e5/pstack/skills/principle-test-behavior-not-implementation/SKILL.md) (checked 2026-09-30): checked `cursor/plugins` pin `fae2c6ed95821bd85f614a73e4842e13229fa5e5`, commit dated 2026-09-30; pstack MIT. The map pairs user actions with observable results, preserves evidence, records feature IDs/entry points, and treats skipped entry points separately. The generator requires exercising its generated instructions. These inspected surfaces are prompt contracts; pstack was not installed or run.
- [pstack-claude port](https://github.com/michael-denyer/pstack-claude/tree/eefcfaf31343a0c98d4bf0dc74a55d62b35ce9f9) and [ported generator inventory](https://api.github.com/repos/michael-denyer/pstack-claude/contents/plugins/pstack/skills/create-verification-skill?ref=eefcfaf31343a0c98d4bf0dc74a55d62b35ce9f9) (checked 2026-09-30): checked pin `eefcfaf31343a0c98d4bf0dc74a55d62b35ce9f9`, commit dated 2026-09-29, MIT. Corroborates porting skill text to other hosts, not independent live-product efficacy or the paste's unidentified index-4 citation.
- [Temporal Workflow Execution](https://docs.temporal.io/workflow-execution) and [Activities](https://docs.temporal.io/activities) (checked 2026-09-30): live official documentation, not release-pinned. Workflow state/history and replay already address orchestration recovery. Activities can retry from their initial state and are recommended to be idempotent. Durable orchestration does not alone settle arbitrary external effects.
- [Stripe idempotent requests](https://docs.stripe.com/api/idempotent_requests): live official documentation, not a live API experiment. Same-key response replay includes failures; incoming parameters must match; a key reused after pruning can initiate a new request. Receipt loss therefore requires the actual sink contract, not the word workflow or a local checkpoint.
- [Anthropic workflow/agent definitions](https://www.anthropic.com/engineering/building-effective-agents): published 2024-12-19, current page warns tooling has changed; checked 2026-09-30. Defines predefined-code workflows versus model-directed agents and explicitly favors the simplest sufficient composition. Used for vocabulary only, not current SDK/runtime efficacy.
- Local contracts read: `reflective-spec-plan/SKILL.md` Test Plan/Workflow Design/Spec Version and Acceptance Record; `flow-loop-harness/SKILL.md` Anatomy/Never/template; `verification-map-generator/SKILL.md` Generation Procedure/Failure Classification; `04-agent/runtime-trust-boundary.md` §§4/4a; `04-agent/workflow-engine.md`; current project direction and prior harness-convergence/pstack records. Local pointers are existing contracts, not evidence of host enforcement.

## Version / Date Context

Pins above are immutable evidence identities, not deployment recommendations. Public docs are live and need rechecking against a selected host/runtime/API version before implementation. The [2026-08-25 Pi/Maka/Amplio/Ankole survey](agent-harness-convergence-survey-2026-08-25.md) is prior pinned evidence with scoped internal crash tests; it is not a fresh maturity audit of those projects.

The paste's original citation set cannot be reconstructed from its seven opaque `chatgpt-content-reference` markers. `grep` with `https?://|chatgpt-content-reference` over the complete supplied artifact returned markers 0–6 and zero HTTP URLs; the same search on the Ralph source packet returned known-present URLs. A semicolon-separated local-URI search failed; it was reported and retried as separate searches. Independent sources above corroborate or qualify claims, not restore the original citations.

## Evidence vs Inference

### Source-backed corrections

1. **Ralph is not necessarily verification-gated.** The pinned native shell accepts `<promise>COMPLETE</promise>` even when the PRD still says `passes:false`. Fresh processes and prompted quality checks do not make that stop authoritative. A stable prompt within a run is compatible with operator tuning between runs; tuning alone does not refute the paste's stable-template idea. The stronger generalization across Ralph implementations remains unverified.
2. **Workflow is broader than a plan or DAG.** Temporal is a direct counterexample to reducing workflow to next-step sequencing. Conversely, replayed orchestration and local state do not prove exactly-once payments, messages, or deployments. Distinguish intent, dispatch, durable receipt, sink evidence, and `OUTCOME_UNKNOWN`; retry only under valid parameter/authority/sink conditions.
3. **Feature Map is not merely a feature inventory.** The pinned pstack template already has behavioral observations and evidence conventions. A Requirement/Acceptance Map adds a requirements-indexed traceability view; it need not replace a features-indexed navigation map or invent a second source of truth. Stable REQ/AC IDs and test planning already have a TeaPrompt home; that coverage does not establish a joined product-verification consumer. The status and join assessment below preserves this distinction.
4. **Contract/State/Evidence is a mental model, not a portable executable interface.** The supplied field lists leave types, identity/version binding, transition owners, error semantics, receipt authority, and acceptance rules to the implementation. Runtime portability would need a concrete host contract and conformance scenarios. Logical authority separation does not require four separate model deployments.
5. **Authorization belongs before each protected effect.** The paste's final `Evidence -> Authorized Effect` is safe if it means releasing a verified artifact. It is unsafe if interpreted as allowing earlier bounded execution to cause unapproved effects. Proposal, authorization, execution, observation, and named acceptance are distinct; evidence supports a scope-bound verdict rather than proving universal success.
6. **The login YAML is illustrative, not a pstack shipped spec.** A cookie's existence, dashboard route, and screenshot do not by themselves prove server-side authentication, the expected principal/tenant, persisted state, or denial paths. They are useful observations only relative to the actual acceptance predicate.

### Inferences and unknowns

- `[INFERENCE]` The proposed umbrella and five-family responsibility table can improve discussion clarity. No A/B navigation, authoring, classification, or delivery-outcome gain was measured.
- Selected projects demonstrate recurring mechanisms, not prevalence, architectural genealogy, an industry consensus, or a proven superiority of six layers.
- The exact original index-4 transplantation reference and all seven original citation URLs remain unknown. A text port and TeaPrompt's separately documented prior product pilots are distinct evidence classes.

## PS2-3 / PS-C1 Status and Product Traceability Join

The original candidate rows describe their decision-time state. Later dated addenda carry the subsequent authorization and execution history; this record does not rewrite those historical rows or treat their original deferral as the current state.

| Item | Original record | Later evidence and current qualification |
| --- | --- | --- |
| PS-C1 | Target-product control interface and maintained map initially deferred | The [2026-09-22 pilot](pstack-survey-2026-09-22.md#pilot-execution-addendum-2026-09-22) ran on wsgiLite.js; the [2026-09-23 arm×scenario matrix](pstack-survey-2026-09-22.md#full-armscenario-matrix-2026-09-23) followed explicit authorization. The [second](pstack-survey-2026-09-22.md#second-product-fpgo-2026-09-23), [third and fourth](pstack-survey-2026-09-22.md#third-and-fourth-products-fpes--fprust-2026-09-23) product runs established recurrence and registered verification-map-generator. PS-C1 is not an unstarted pilot. |
| PS2-3 | [Synthesis candidate ledger](pstack-synthesis-survey-2026-09-22.md#candidate-adoption-ledger) says deferred, pilot-design input | Its map/drift mechanism must be read alongside the later PS-C1 executions and existing event-driven map-maintenance contract. Neither that historical row nor successful drift classification establishes a REQ/AC-to-product-evidence join. |
| PS2-7 / PS2-4 | A/B/C evaluation design; durable execution remains host-owned | The [authorization addendum](pstack-synthesis-survey-2026-09-22.md#authorization-addendum-2026-09-23) accepts the PS-C1 continuation and host-owned durable-execution direction. The selected product matrix does not establish every originally proposed crash/side-effect scenario or effective-throughput gain; no new runtime or pilot permission follows here. |

Existing coverage is real but split across artifacts:

- [reflective-spec-plan Test Plan Mode](../skills/reflective-spec-plan/SKILL.md#test-plan-mode) defines stable requirement/acceptance IDs and a requirement-to-test matrix with expected results and failure signals.
- [verification-map-generator Inputs](../skills/verification-map-generator/SKILL.md#module-contract), L44–47 at this review, list two inputs: the product repo and its existing check surface. That bounded list has zero explicitly required requirement-source inputs; the two named inputs are the known-present control. [Generation Procedure](../skills/verification-map-generator/SKILL.md#generation-procedure) L62 makes `acceptance.yaml` optional; L63 checks that drive outcomes match the map, not requirement-derived correctness. An existing product suite can already supply the oracle: this is a contract-binding question, not evidence that every product lacks an oracle.
- [governed-delivery contract set](../skills/governed-delivery/SKILL.md#contract-set) records spec version, oracle class/owner/seal/change protocol, evidence provenance, and named acceptance. Those templates do not by themselves join a particular REQ/AC to a generated feature-map driver and its observation.

The closest existing judgement is [“A verification map's value is regression visibility and time-to-verify, not correctness”](../PROJECT_KNOWLEDGE.md#lesson-a-verification-maps-value-is-regression-visibility-and-time-to-verify-not-correctness), L121–124 at this review. It places independent correctness expectations in the locked acceptance spec; for libraries, an existing test suite can supply the oracle. The [original pilot design](pstack-survey-2026-09-22.md#practical-pilot-one-user-journey-not-a-whole-product-harness), L153–156, likewise derives success criteria from product requirements rather than treating current behavior as the oracle.

**Held — AEAT-4: acceptance-oracle join.** The reviewed generator contract does not require a requirement source or a per-REQ/AC binding to an independently owned acceptance check. Its optional acceptance spec and separately existing requirement-to-test guidance do not establish that binding for a particular product. The held question is whether each in-scope REQ/AC ID reaches a locked acceptance check, or an authoritative oracle-manifest entry resolving to such a check, which a feature-map driver exercises and whose observation is recorded as evidence. A concrete product may already provide this join; its absence has not been demonstrated here.

- **Reopen trigger:** a named product's requested requirements-based verification has a missing, ambiguous, stale or skipped REQ/AC→acceptance-oracle→driver→observation/evidence binding, plus explicit authorization to assess that product. Assess its existing artifacts first; neither a clean map sweep nor the absence of an `acceptance.yaml` filename establishes the gap.
- **Falsifier:** every in-scope REQ/AC already resolves to an independently owned acceptance check or a manifest entry resolving to that check, with spec/version/freshness binding; a feature-map driver actually exercises it and the observation is retained as evidence. Demonstrating that existing chain falsifies the need for a join repair on that product without adding a second map or schema.
- **Rejected probe:** generating a map on an already-buggy copy without an independent acceptance oracle, then observing a clean sweep, would only revisit the known fact that the map is not a correctness oracle. It would not confirm this acceptance-spec-leg gap and is not its falsifier. No such experiment is run or authorized here.

Line references identify the reviewed contract and judgement passages, not a portable schema. Local recurrence and benefit remain unknown, not zero. This held item's trigger/falsifier do not reopen PS-C1, authorize a new pilot, or change existing adoption/deferred gates.

## Existing Decision Precedents

These pointers explain the AEAT dispositions; they are earlier evidence, not freshly executed experiments or new governing rules.

| Candidate | Existing precedent | What it supports / what it does not establish |
| --- | --- | --- |
| AEAT-1 | [Flow-control research](agent-flow-control-research-2026-07-11.md#convergent-concepts-safe-to-build-on); [Software Factory rethink SFR-3](software-factory-rethink-panel-record-2026-09-28.md#candidate-adoption-ledger) | Compose bounded existing workflow/loop/governance surfaces; the prior duplicate-skill rejection is not an industry-wide taxonomy proof. |
| AEAT-2 | [Flow-control pack promotion and scope](agent-flow-control-research-2026-07-11.md#promotion-decision); [existing loop contract](../skills/flow-loop-harness/SKILL.md#loop-anatomy) | External-verifier loops already have a home. Scripted template controls below are not model-efficacy or production-containment evidence. |
| AEAT-3 | [PS2-4 authorization](pstack-synthesis-survey-2026-09-22.md#authorization-addendum-2026-09-23); [governable-autonomy recommendation](governable-autonomy-survey-2026-09-03.md#direct-recommendation-as-of-2026-09-03) | Durability and effect containment are host responsibilities; a recorded host-owned direction is not authorization to build a TeaPrompt runtime. |
| AEAT-4 | [Verification-map project judgement](../PROJECT_KNOWLEDGE.md#lesson-a-verification-maps-value-is-regression-visibility-and-time-to-verify-not-correctness); [PS-C1 and subsequent products](pstack-survey-2026-09-22.md#pilot-execution-addendum-2026-09-22); [PS2-3 ledger](pstack-synthesis-survey-2026-09-22.md#candidate-adoption-ledger) | The map's regression/navigation value is established; the held item concerns a REQ/AC binding to an independent acceptance oracle exercised by a driver with recorded observation/evidence, not making the map itself a correctness oracle. |
| AEAT-5 | [Governable-autonomy concept-only split and host limits](governable-autonomy-survey-2026-09-03.md#disagreements--residual-risks); [Workflow Design Mode](../skills/reflective-spec-plan/SKILL.md#workflow-design-mode) | Responsibility/state distinctions are compatible with existing design guidance; prose field lists do not establish a portable, enforced runtime interface. |
| AEAT-6 | [Four-authority core proposition](agent-governance-four-power-concepts-2026-07-17.md#core-proposition) and [effect pipeline](agent-governance-four-power-concepts-2026-07-17.md#three-stage-effect-pipeline); [runtime trust boundary](../04-agent/runtime-trust-boundary.md) | Proposal, authorization, effects and acceptance are already distinct. Authorization precedes each protected effect; evidence and named acceptance do not retroactively authorize earlier effects. |

## Candidate Adoption Ledger

| ID | Candidate | Decision | Existing coverage / boundary | Reopen condition |
| --- | --- | --- | --- | --- |
| AEAT-1 | Replace existing vocabulary/routing with five families or six mandatory layers | Record-only; no operating change | Strictness, formalization, and execution mode remain separate; `reflective-spec-plan` rejects a forced architecture | Demonstrated local classification/discovery error requiring an in-place repair; routing change keeps its own holdout gate |
| AEAT-2 | Add a new Ralph/fresh-worker verification rule or skill | No change | Existing loop pack uses an external verifier, caps, no-progress exits, and labels advisory writer-critic exceptions | Local template consumer bypasses an existing stated gate |
| AEAT-3 | Build a TeaPrompt durable-state/recovery runtime | No change; outside project boundary | Four risk-scaled contracts and explicit unknown-effect rules already specify host duties | Explicit runtime-direction change, named owner/sink, and scoped failure/recovery proof |
| AEAT-4 | Rename Feature Map to Capability/Acceptance Map; assess its independent acceptance-oracle join separately | No rename/schema adoption; acceptance-oracle join held | Inputs L44–47 require no explicit requirement source; the locked acceptance spec is optional at L62. Existing project judgement makes the independent oracle, not the map, the correctness leg | Named-product binding gap plus explicit assessment authorization; a complete existing REQ/AC→owned acceptance check/manifest→driver→recorded observation/evidence chain falsifies the need for a repair |
| AEAT-5 | Promote Contract/State/Evidence lists into a cross-host schema | Study-only mental model | Existing versioned task/oracle/authority/acceptance contracts; host enforcement not supplied by field names | Named interoperability target, executable consumers, and migration/conformance criteria |
| AEAT-6 | Add a new authorization/evidence architecture rule | No change | Runtime trust boundary §§4/4a and named acceptance already cover ordering and receipt/postcondition scope | An observed local delivery authorizes by evidence alone or reports business success before its owning commit |

No candidate is adopted into a skill, routing row, runtime, schema, or project-knowledge principle. The held AEAT-4 acceptance-oracle join is not closure of that product binding or reopening of an already exercised PS-C1 pilot. Existing AH, R8, and unrelated deferred/adoption gates are unchanged; unknown usage is not zero demand.

## Falsifiability

- A source-pinned Ralph controller whose native stop requires an independent verifier would defeat the completion-gate finding for that controller; it would not erase the observed snarktank result or prove every Ralph implementation equivalent.
- A false DONE report releasing the unchanged TeaPrompt verifier-gated loop while its verifier fails would defeat the scoped control claim; the cap and no-progress cases below exercised the opposite result.
- A concrete interoperable Contract/State/Evidence consumer with defined identities, transitions, receipt authority and conformance evidence would change AEAT-5's study-only assessment; field names alone do not.
- AEAT-4 is refuted for a named product if each in-scope REQ/AC resolves to an independently owned acceptance check or a manifest entry resolving to that check, a feature-map driver exercises it, and the observation is recorded as evidence with spec/version/freshness binding. A clean map sweep without an independent oracle is not this falsifier; a demonstrated missing binding would justify assessing an in-place repair, not automatic schema or skill adoption.

## Verification Actually Exercised

| Surface / case | Input and control | Observed result | Evidence tier |
| --- | --- | --- | --- |
| Pinned snarktank shell; delegated native run | `./ralph.sh --tool claude 5`; PATH-shadowed CLI prints false COMPLETE, PRD story stays false | `Ralph completed all tasks!`; `Completed at iteration 1 of 5`; exit 0 | Native shell with scripted stub, not real-agent behavior |
| Same shell; delegated cap control | No-promise CLI, max iterations 3 | `Ralph reached max iterations (3) without completing all tasks.`; exit 1 | Same offline rig tier |
| Unmodified TeaPrompt Verify-Gated Fix Loop | Scripted worker reports DONE and creates the observed ready postcondition | exit 0; 1 worker call, 2 verifier calls | Native repository template, deterministic stub/verifier |
| Same template; cap | DONE reports, changing failed-verifier observation, `MAX_ITER=2` | exit 2; 2 worker calls, 3 verifier calls; no VERIFIED ledger row | Same offline rig tier |
| Same template; no progress | DONE report without changed postcondition or verifier output | exit 3; 1 worker call, 2 verifier calls; NO PROGRESS ledger row | Same offline rig tier |
| Same template; missing verifier | Nonexistent VERIFY executable | exit 4 before any worker/verifier call | Same offline rig tier |

Coordinator command: `/usr/bin/python3 /private/tmp/teaprompt-assurance-loop-X4NoYx/probe.py`, running the exact fenced repository template in isolated non-git working directories with `/bin/bash`, a restricted executable PATH, no actual agent CLI, and two-iteration caps. An initial throwaway-driver SyntaxError was corrected before scenario execution; the repository template was never changed. Completed driver: `TOTAL 4 native control cases; pass=True`, exit 0. Template SHA-256: `96df544abe4aa78b5d87484844761861b62075036cf827af7a5eb531b5d22d8d`.

The original session evidence artifacts were `execution-assurance-loop-smoke.json`, `ralph-execution-assurance-evidence.md`, and `pstack-execution-assurance-evidence.md`; the observed cases, source pins, template hash, commands and limits are preserved here so this repository record does not depend on those session files. The coordinator's four-case result was `pass: true`: verified ledger `- iter 1: VERIFIED`; cap ledger ended `- cap 2 exhausted` with no VERIFIED row; no-progress ledger ended `- iter 1: NO PROGRESS, aborting`; missing-verifier ledger stayed empty and stderr reported the nonexistent executable. Every scripted worker output in the first three cases was `DONE: all requirements satisfied`; the fourth invoked no worker.

Coordinator scratch was removed and its exact-path absence checked; delegated Ralph cleanup is recorded in the original evidence packet. These runs do not demonstrate model efficacy, host sandbox enforcement, oracle immutability, crash durability, sink correctness, or production acceptance. No pstack installation, Temporal server, Stripe call, benchmark, permanent tests, or repository build/lint/test run was undertaken during the original source-only survey. For this later durable-record integration, index regeneration and `make all` results belong to the accompanying delivery report; they are documentation/fixture evidence, not another source-runtime experiment.

Repository link-validator scope: `validate_links.py` L152–153 removes fragments before checking target-file existence; a passing `make all` therefore does not prove local heading anchors resolve. This correction pass checks the record's local fragments separately with a throwaway heading/slug checker; its observed results belong to the delivery report, not the source-runtime evidence above.

## Risks / Unknowns

- Source contracts, live documentation, native scripted rigs, and real deployment outcomes must not be merged into one evidence tier.
- A stronger requirements map can still use a wrong, stale, self-confirming, or mutable oracle. Require the actual owner/version and a failure signal, not more headings.
- A six-plane diagram is not proof of independent channels, liveness, deterministic gates, authority isolation, or recoverable external effects.
- Before any real host adoption: select the concrete version and effect boundary; test the post-dispatch/pre-receipt crash with independent sink observations and an unresolved-outcome owner. This survey does not authorize that adoption or experiment.

## Handoff

The original survey's two advisor reminders referred to already completed shared-integration ownership and RRSI scratch cleanup; neither was repeated. This follow-through internalizes that survey and adds discovery pointers only. Schemas, skills, runtime code, and governing contracts remain unchanged. AEAT-4's acceptance-oracle join is held with a named-product trigger and falsifier, not an unfinished authorized implementation or experiment. Original-citation recovery and efficacy/prevalence remain unknown. Amend or retire this record if a cited source pin is corrected, an authorized product join assessment resolves AEAT-4, or an explicit governing-artifact promotion supersedes a disposition; do not silently turn this archive into policy.
