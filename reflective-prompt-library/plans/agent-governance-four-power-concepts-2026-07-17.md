# Agent Governance — Four-Power Architecture Concepts — 2026-07-17

> **Status: recorded (non-authoritative); concepts + feature→artifact map.** This
> record captures the concepts of the user-provided *代理治理四權架構 spec
> v1.1-RC1* (attachment, 2026-07-17) and maps each declarable feature to a
> scaffold artifact so the `agent-governance-scaffold` domain pack has a single
> source for its concept vocabulary. Authority chain unchanged:
> `06-repo/AGENTS.md` and the invoked `SKILL.md` contracts govern; this record is
> evidence and design judgement, not an operating rule. If it and a governed
> surface disagree, the governed surface wins.

## Purpose

Record the four-power agent-governance concepts as a durable plan so the new
domain-pack skill (`agent-governance-scaffold`) and future work reference one
concept vocabulary instead of re-deriving it from the raw spec. The adoption
decision, candidate ledger, and demotion triggers live in the sibling
[adoption record](agent-governance-scaffold-adoption-2026-07-17.md); this file is
concepts only.

## Scope

- In scope: the core proposition, the four authorities and their invariants, the
  three-stage effect pipeline, the fifteen invariants, the five-element ×
  failure-class table, the theory genealogy, the keyword glossary, and the
  feature → scaffold-artifact mapping.
- Out of scope: adopting any TeaPrompt-owned runtime, effect broker, policy
  engine, or verifier service (Standing Non-Goal — TeaPrompt operates no
  runtime); running the spec's §13 experiments; changing the nine core routing
  skills.

## Evidence vs Inference

- **Source (given):** the spec text is a user-provided attachment dated
  2026-07-17. Every concept below is transcribed or condensed from it.
- **Evidence tier:** architecture/methodology tier. The spec self-declares (its
  §0, §12, §13) that its claims are *proposals* whose final status is decided by
  unrun experiments; it is not empirical evidence. This record inherits that
  tier and does not upgrade it.
- **`[INFERENCE]`** marks this record's own design judgements (e.g. which
  concept maps to which scaffold artifact); they are not spec claims.
- Not independently verified here: the theory-genealogy attributions (Ashby,
  Clark–Wilson, Kerckhoffs, Rice, Thompson, etc.) are reproduced as the spec
  states them; no external source was fetched for this record.

## Core Proposition

A reliable agent is not a model turned into a trusted subject, but a model
constrained to *propose strongly yet never make its own proposals effective*:
policy authorizes, tools produce effects, evidence decides acceptance, a named
owner is accountable, and the control rules themselves get constitutional-tier
protection. This is **power decomposition, not trust relocation** —
`trust(model, propose)` is retained and necessary; the model may help recommend
authorization, prepare execution, and read evidence, but must never be the sole
authority for `authorize` / `effect` / `accept`.

Engineering reading: control comes from "cheap deterministic trigger shell +
contract-hardwired behavior bounds + script-guaranteed invocation", not from
prompt wording. A prompt declaration is a probabilistic call; a hook/script
turns "did the required procedure start" from a model choice into a runtime
event — it raises *invocation reliability*, not execution success or output
correctness (those belong to acceptance authority). Non-invocation must emit an
explicit failure event, never a silent skip.

## The Four Authorities

| # | Authority | Holds | Never |
| --- | --- | --- | --- |
| 1 | Proposal (提案權) | Model defines candidate goals, plans, changes | May not make them effective |
| 2 | Authorization (授權權) | Policy / human decides allowed operations, scope, duration | Not a single unbounded source |
| 3 | Effect (效果權) | Tool / broker acts only inside approved capability | May not exceed capability or self-issue receipts |
| 4 | Acceptance (驗收權) | Evidence / verifier decides if the goal is met | Approval is not evidence; self-report is not acceptance |

Cross-cutting controls: Accountability / Audit / Constitutional protection /
Escalation / Rollback / Context isolation.

High-risk role invariants (nominal condition only; the real condition is failure
independence, §5.2 of the spec):

```
proposer  ≠ sole authorizer
executor  ≠ sole acceptor
control-plane editor ≠ control-plane approver
```

## Three-Stage Effect Pipeline

Model speech is not action. Every external effect crosses three stages, and each
**cross-stage hand-off** is verified:

1. **Claim** — model asserts "should do X"; pure statement, no force.
2. **Authorized intent** — policy layer rules "may do X, within scope Y, until Z".
3. **Effect** — executor changes state inside approved capability; the broker
   issues the receipt.

Naive function calling omits stage 2 (`model output → weakly validated args →
privileged tool → immediate effect`), which is equivalent to executing model
output as code. Inserting schema validation, capability check, policy decision,
human approval, transaction staging, idempotency, and a commit gate demotes
model output to a **candidate operation request**.

## Fifteen Invariants

Effects & evidence: (1) model output is not an effect; (2) approval is not
evidence; (3) execution success is not goal success; (4) an audit record is not
accountability itself; (5) roll-back-able does not mean no external harm.

Authorization & independence: (6) role separation is not failure independence;
(7) a scope string is not a scope; (8) risk classification is itself a proposal;
(9) a new session is not a new authorization; (10) a review conclusion is not
evidence.

Composition & time: (11) authority is monotone non-increasing along a delegation
chain; (12) a sub-agent report is untrusted input; (13) escalation must not be
absorbed by an intermediate layer; (14) authorization is a lease, not a grant;
(15) control must remain effective under full disclosure.

Note (#15): "full disclosure" means policy, architecture, and defense mechanisms
may be known to the agent; it does **not** include keys, unused nonces, approval
tokens, or private credentials — implicit trust is eliminated, secrets are not.

## Five Elements × Failure Class

| Element | Failure class it treats | Erosion condition |
| --- | --- | --- |
| Strong model | Capability ceiling (judgement) | Always chase the frontier |
| Skill | Cognitive step-skipping / disorder | Model gains reliable procedural memory |
| Hook | Procedure bypassed | Reminder-type hooks erode first (attention-mediated); permission/effect-interception hooks do not |
| Script | Ultra-vires / unbounded action | Almost never (security externality) — only while the script is a protected TP |
| Test | False completion claims | Persists while proposer↔delegator information asymmetry exists; form rotates |

The durable layer is the *governance function* each element carries (judgement,
procedure externalization, event/policy enforcement, permission isolation,
independent verification), not the element as a natural kind. Real redundancy
lives *inside each function* (e.g. permission isolation via tool allowlist ×
filesystem ACL × container sandbox × scoped credential × effect broker);
replacing a function re-correlates previously independent failures.

## Theory Genealogy (as stated by the spec; not re-verified here)

- **Ashby requisite variety** (design heuristic, not derivation): shrink the
  ungoverned action space, but keep `V(legal) ≤ V(allowed) < V(unbounded)`; an
  over-narrow allowlist manufactures false escalation.
- **Principal–agent theory**: a worker's "done" claim costs nothing → auditability
  is a *relationship property* between agent and delegator, not a property of the
  agent; self-report is never sufficient acceptance evidence.
- **Clark–Wilson (1987 integrity model)**: the correct lineage is integrity, not
  Bell–LaPadula confidentiality; but non-isomorphic — the model spans User, TP
  selector, and IVP interpreter roles. Isomorphism prerequisite: move tools,
  verifiers, and policy files out of the model's writable range first.
- **Confused deputy**: the precise shape of prompt injection; the fix is
  permission-provenance binding (capability binding), not allowlists alone.
- **Scientific management + its correction**: externalized work procedure =
  planning/execution split; the escalate-over-guess contract is Taylorism's
  de-skilling fix — route judgement back to the cognitive layer.
- **Kerckhoffs' principle**: policy lives in the agent's context = structural full
  disclosure; a control that depends on the agent not knowing the rules is born
  broken.
- **Rice's theorem + Thompson "Trusting Trust"**: Rice limits *general* semantic
  decision over Turing-complete programs; closed/formal sub-domains can close on
  specific properties. Thompson is unaffected — the trust anchor must live
  outside the agent-writable universe.
- **OS isomorphism** (predictor): subagent≈process, tool allowlist≈seccomp,
  read-only/workspace-write≈capability-scoped filesystem mode, escalate≈trap to
  kernel, audit trail≈syslog; W^X's meta-governance landing is
  `policy-write XOR immediate-policy-execution`.

## Proposal Lifecycle, Execution Stack, and Verification Concepts

- **Proposal lifecycle × control decision (§1.4):** `proposal_state` (`draft`,
  `evaluated`, `approved`, `executing`, `verifying`, `accepted`, `rejected`,
  `rolled_back`) tracks the proposal artifact; `control_decision` (`continue`,
  `pause`, `escalate`, `abort`) tracks runtime control. Merging the two lets an
  approval masquerade as acceptance or an escalation disappear in a worker layer.
- **Seven-layer execution stack (§1.3):** Goal / Planning / Specification holds
  proposal authority; Dispatch holds authorization; Worker holds effect; Evidence
  & Audit holds acceptance. Replaceability depends on semantic interfaces (task
  contract schema, authority semantics, state transitions, effect receipts,
  acceptance criteria, audit schema), not model branding.
- **Conformance suite (§7.5):** a backend is commodity only within the scope where
  it passes the same contract. Divergent first-pass acceptance rates under the
  same contract falsify the claim that the contract captured the important
  variables.
- **Twin Check vs heterogeneous evidence (§7.3):** Twin Check searches the whole
  project for the same defect pattern after one fix; heterogeneous evidence
  reconciles deterministic traces, independent verifiers, dual-copy checks, and
  external observations. They answer different completeness risks and must not be
  collapsed into one gate.
- **Experiment protocol (§13):** H1–H6 need baseline ladder A–E, task strata, full
  cost accounting, and pre-registered thresholds in `experiments/hypotheses.yaml`
  plus `experiments/analysis-plan.md` before data collection. Until then, they
  stay architecture-tier hypotheses, not evidence.

## Composition, Adversarial Economy, and Accountability Concepts

- **Composition semantics — the delegation tree (§8):** a single cell's four
  powers do not auto-compose. An orchestrator is *acceptor* to its sub-agents but
  *proposer* to its delegator, so a three-layer tree (orchestrator → lieutenants →
  wrapper shell → headless CLI) is `proposer == acceptor` at the composite layer —
  the whole tree's "done" is self-declared unless **at least one top-level
  acceptance authority is not solely controlled by the proposer** (external fixed
  AC, immutable acceptance test, human acceptance, or independent effect
  observation). Authority is monotone non-increasing down the chain (#11): scope
  takes the **intersection**, prohibitions the **union**; you cannot delegate a
  capability you do not hold. Escalation must be **transitive** (#13) — a
  mechanical middle layer that silently absorbs an escalation breaks the contract.
  A sub-agent report is **untrusted input** to its parent (#12): injection also
  arrives from below the tree, so prompt-defense scope includes internal reports.
  Per-layer broker receipts generalize "shell holds verification, CLI does not" to
  every layer — each layer's evidence is produced by that layer's infrastructure,
  not self-reported, or the self-report problem is merely deferred one level.
- **Adversarial model — Kerckhoffs razor (§9.1):** policy sits inside the agent's
  context, so governance is structurally fully disclosed to the governed. Keep
  only controls that survive full disclosure — **passes:** sandbox, effect broker,
  cryptographic verification, out-of-band approval; **fails:** behavioral
  exhortation, in-context self-check. Full-disclosure survivability and
  capability-extension survivability are related but not equivalent; a control
  must pass **both**.
- **Ultra-vires nullification (§9.2):** the acceptance condition is
  `∀ a ∉ AuthorizedActions, Effect(a) = ∅` — the unauthorized action produces no
  effect, not merely a logged "denied". Any one of these voids the guarantee: the
  agent can modify policy, obtain high-privilege credentials, call an unmanaged
  shell, or bypass the effect broker.
- **Approval bandwidth economy (§9.3–§9.5):** approval demand grows with
  throughput while human attention is constant, forcing the human from
  *in-the-loop* to *on-the-loop* (per-policy + sampled audit). Three endgames:
  rubber-stamp decay, throughput ceiling (governance becomes the bottleneck), or
  hierarchical adjudication. Tiered **approval budget** — low risk: batch/sample;
  mid: summary with diff+risk; high: itemized, named, non-delegable. The approval
  screen needs a minimum payload (what changes, why, blast radius, no-approval
  consequence, rollback, verification) or it is a redundant button. Rubber-stamp
  is measured **behaviorally, not by count (§9.4):** approval latency,
  meaningful-rejection rate, post-approval incident rate, review depth; the
  **approver canary** injects synthetic violations at a known base rate and
  requires **behavioral exchangeability** (H6) — detection-rate and
  decision-latency gap versus paired real violations < ε. Governance is an
  **enabler, not a tax (§9.5):** long-horizon cheap delegation is economical only
  because deterministic acceptance exists — "the brake is what lets the car go
  fast".
- **Accountability decomposition (§11):** an audit answers **attributability**
  (which identity, when, did what, which version, approved by whom); accountability
  additionally needs **answerability**. Five parts: Traceability (what happened),
  Attribution (who executed/approved), Answerability (who must explain), Liability
  (who bears legal/financial consequence), Remediation duty (who fixes the
  system). Every gate is **named** even in a single-person system (John as
  requester, John as approver, Agent as executor, System as evidence recorder) so
  responsibility never collapses into "the system decided" — the **moral crumple
  zone** failure.

## Keyword Glossary / Concept Index

原理層：deterministic trigger、wrapper shell、mechanical executor contract、three-no
principle、contract invariant。權力分解：proposal authority、authorization
authority、effect authority、acceptance authority、three-stage effect pipeline。
授權層：checker profile、authorization epoch、capability binding、Gate 2.0、lease
semantics、mechanized escalation predicate。效果層：bounded-policy agent、scope
string is not scope、TOCTOU、capability class、broker receipt、cumulative-effect
accounting。驗收層：Twin Check、heterogeneous evidence reconciliation、L0–L5
acceptance ladder、conformance suite、constitutional verifiers、phantom-source
discipline、pre-registered acceptance rules。組合與後設層：composite
self-acceptance、authority monotonicity down delegation chains、upward injection,
constitutional paths、policy monotonicity、out-of-band activation、mutation suite,
approver canary。問責層：traceability、attribution、answerability、liability,
remediation duty、named gate、moral crumple zone。

## Heddle Mapping and Market Positioning (spec §14)

- **Component mapping:** Goal / proposal artifact maps to proposal authority;
  approval chains map to authorization authority; workspace ownership + worker
  maps to effect authority; audit / verification maps to acceptance authority;
  continue/pause/complete/escalate are runtime control decisions, not proposal
  lifecycle states; protected control paths are meta-governance; heartbeat is a
  lease-renewal point.
- **Positioning claim:** the spec does not claim individual controls are absent
  in the market. Its stronger claim is composition: proposal, authorization,
  execution, acceptance, and meta-governance become one versioned, testable,
  auditable protocol. This is recorded as a product/architecture framing, not
  empirical proof.
- **Roadmap interpretation:** heartbeat lease renewal, Kerckhoffs-surviving
  controls, formal proposal-state/control-decision separation, constitutional
  paths, broker receipts, cumulative-effect accounting, mutation suite, approver
  canary, Twin Check, and heterogeneous evidence reconciliation are features the
  scaffold can emit or point to; host runtime still owns enforcement.

## Feature → Scaffold Artifact Map `[INFERENCE]`

This is this record's design judgement, mapping the spec's §14.3 declarable
features and §15 skeleton to the artifacts the `agent-governance-scaffold` domain
pack emits. It is not a spec claim.

| Spec feature (§) | Scaffold artifact the pack emits |
| --- | --- |
| Proposal lifecycle and control decision separation (§1.4) | `proposal_state` + `control_decision` schema |
| Seven-layer stack, semantic interfaces, backend replaceability (§1.3, §7.5) | `semantic_interface` + `conformance_suite` manifest |
| Gate 2.0 risk-thickness sizing (§5.4, §5.5, §5.6) | Gate-thickness sizing method + handover note |
| Evidence by effect type, phantom-source discipline, Twin Check, heterogeneous evidence (§7.1, §7.3) | `verification_plan` with evidence map, `twin_check`, and `heterogeneous_evidence_reconciliation` |
| H1–H6 experiments, baseline ladder A–E, task strata, pre-registration (§13) | `experiment_protocol` stubs for `hypotheses_yaml` + `analysis_plan` |
| Wrapper / bounded-policy agent, three-no contract (§6.4, §15.1) | Wrapper agent contract file |
| Read-only / workspace-write run interface (§6.4, §15.2) | `run-<cli>.sh` interface stub |
| Mechanized escalate predicates (§5.8, §15.3) | `escalate_if` predicate list |
| AuthorityPolicy, capability token (§5.1, §5.3) | Authorization + capability objects |
| Broker receipt, per-layer receipts (§6.2, §8) | Effect-receipt schema |
| Cumulative effect accounting (§6.3) | `cumulative_effect_key` + `effect_budget` (lease-keyed) |
| Checker profile, failure independence (§5.2) | `checker_profile` multi-axis object |
| Lease / heartbeat renewal (§5.7) | State-predicate lease + heartbeat semantics |
| Acceptance ladder L0–L5, verifier split (§7.2, §7.4) | `constitutional_verifiers` vs `task_mutable_tests` |
| Constitutional paths, out-of-band activation, monotonicity (§10) | `constitutional_paths` + `policy_activation` |
| Named accountability gate, five-part decomposition (§11) | Named `approval` object |
| Agenda check, counterproposals, intent–spec trace (§4.2) | `agenda_check` object |
| Mutation suite (H3 five items + approver canary) (§9.4, §13) | Mutation-check scaffold |
| Fifteen invariants | Invariant checklist embedded in the scaffold |

## Residual Risk (spec §12, condensed)

- **Spec–intent gap** is a structural residual of the *general* open domain, not
  a theorem; formalizable sub-domains can close specific properties.
- **Trust root** extends to the build/signing/execution chain (Thompson); source
  checks are a necessary start, not a complete end.
- **Cognitive face is bare by design** — judgement budget belongs where
  mechanization is impossible (proposal framing, high-risk authorization,
  contradictory-evidence adjudication, novel escalation, L5 acceptance, framing
  error re-review), not spread over everything.
- **Friction accumulation → process hardening**: hooks need GC, and the deletion
  test is positive — an uncaught mutation is a *broken* control (fix first, do
  not delete).

## Falsifiability

This concepts record is wrong if: the `agent-governance-scaffold` skill's
governance objects diverge from the concepts named here without this file being
updated; the feature→artifact map lists an artifact the skill does not emit; or
the record is cited as empirical evidence rather than architecture-tier design
judgement. Any of those means the concept vocabulary drifted from its
implementation and must be re-reconciled.

## Prompt / Source Pointers

- User-provided spec *代理治理四權架構 v1.1-RC1* (attachment, 2026-07-17) — the source of every concept above.
- [agent-governance-scaffold-adoption-2026-07-17.md](agent-governance-scaffold-adoption-2026-07-17.md) — adoption decision + candidate ledger + demotion triggers.
- [../skills/agent-governance-scaffold/SKILL.md](../skills/agent-governance-scaffold/SKILL.md) — the domain-pack skill that emits these artifacts.
- [../04-agent/runtime-trust-boundary.md](../04-agent/runtime-trust-boundary.md) — instruction/data separation and least-privilege lens (adjacent methodology).
- [external-adoption-case-studies-2026-06-20.md](external-adoption-case-studies-2026-06-20.md) — methodology-vs-operationalization boundary and local-gap gate.
