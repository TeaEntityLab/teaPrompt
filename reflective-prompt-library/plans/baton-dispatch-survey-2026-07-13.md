# Baton Dispatch Skill Survey — 2026-07-13

> **Status: decided (non-authoritative); external-adoption panel record.**
> Baton is retained as study/reference material only. No TeaPrompt workflow skill,
> supporting lens, domain pack, verifier, dependency, or runtime surface was
> adopted. `06-repo/AGENTS.md` and governed skill contracts remain authoritative;
> this record is evidence and a no-change decision, not an operating rule.

## Purpose

Preserve the completed survey of CabLate's `baton-dispatch` skill so the same
external-adoption question is not re-litigated from chat memory. The decision
question was whether Baton's dispatch brake, execution primitives, ownership
maps, worker briefs, failure handling, and verification model reveal a verified
TeaPrompt-local structural gap.

## Target and Version

- User-supplied moving entrypoint: [`main` `SKILL.md`](https://raw.githubusercontent.com/cablate/baton/refs/heads/main/SKILL.md), checked 2026-07-13.
- Pinned review target: [`baton-dispatch` v0.1.1](https://github.com/cablate/baton/releases/tag/v0.1.1), checked 2026-07-13.
- Commit: [`77f12e600406065a6e62a22a66347355e278a9d7`](https://github.com/cablate/baton/commit/77f12e600406065a6e62a22a66347355e278a9d7), checked 2026-07-13.
- Upstream license: MIT, verified from the repository/API on 2026-07-13.
- Volatility trigger: re-check the release, tag target, source tree, and evidence
  status before relying on any later Baton version.

## Panel Execution Mode

Method contract: `04-agent/workflow-recipes.md` §Parallel Lens Review and the
host `parallel-lens-review-packet` wrapper.

1. One shared packet, `review-packet-baton-2026-07-13.md`, was written at the
   repository root with target/version/date, prior hypothesis, observed evidence,
   author claims, unknowns, blockers, source/command ledger, and exact reviewer
   questions. It was transient and deleted after synthesis.
2. The first parallel fan-out of seven read-only scout lenses failed before
   producing review content with provider `429 RESOURCE_EXHAUSTED`.
3. The mandated identical default-worker fallback also failed before producing
   review content with `resource_exhausted`.
4. An auxiliary stateless-completion fallback was excluded: one attempt received
   an unresolved packet value; corrected requests hit the same quota. None of
   those outputs entered synthesis.
5. A third parallel batch of seven specialist reviewer agents completed. Every
   full deliverable was read, not merely its preview. The role labels below are
   review perspectives; reviewer count is not evidence and no claim is made that
   seven distinct model providers were used.
6. Shared-worktree branch was verified as `main` after the panel. No reviewer
   edited the repository.

## Lenses (all seven: AGREE WITH CHANGES)

| Lens | Load-bearing question | Main result |
| --- | --- | --- |
| Evidence / provenance | Are version, license, release, benchmark, and attribution claims correctly tiered? | Source ledger sound; two wording/path clarifications; no evidence-tier upgrade found. |
| Dispatch architecture | Are the trigger, brake, primitives, ordering, ownership, recovery, and synthesis internally coherent? | Mostly coherent; topology and workspace mode are collapsed, ordering and integration ownership need clarification. |
| Reproducibility | Can the published benchmark establish Baton-specific value? | No concrete fixture, per-trial schema, primary outcome, success threshold, active control, or results. |
| Trust / provenance | What does the package itself enforce, and what remains host responsibility? | Small text-only surface and careful install prose; no runtime enforcement or delegated-data boundary. |
| TeaPrompt local gap | Does any mechanism survive overlap, minimality, recurrence, and standing-non-goal gates? | No verified local structural gap; current destination is no-change plus reference study. |
| Usability / portability | Can operators trigger, apply, and stop the skill without excess ceremony? | Strong progressive disclosure; direct-work output default and minimal template variants are missing. |
| Adversarial operations | How does it handle stale packs, missing workers, malformed output, secondary writes, drift, and budgets? | Failure table omits common cases; prose controls cannot guarantee runtime behavior. |

## Panel Consensus

- **Decision:** `AGREE WITH CHANGES` (7/7 completed lenses).
- **Direct recommendation:** study Baton as a prompt-level dispatch-governance
  reference; do not adopt it into TeaPrompt and do not treat it as a runtime or
  safety control.
- **Local-gap decision:** `[INFERENCE]` Baton's methodology is already present or
  adjacent across `reflective-dispatch`, `04-agent/agent-selection.md`,
  `04-agent/workflow-recipes.md`, the registered `flow-control-generator` pack,
  and the active host delegation policy. The absence of one consolidated generic
  checklist is a surface difference, not a verified local problem.
- **Promotion decision:** local recurrence remains `unknown`; this external survey
  is not local promotion evidence. The frozen-core, domain-pack, and runtime gates
  remain closed.

### Use-Case Recommendation

| Use case | Decision | Evidence boundary |
| --- | --- | --- |
| `study` | **yes** | Dispatch brake, ownership map, bounded fan-out, centralized verification, and synthesis rules are useful reference patterns. |
| `reproduce` | **not as published** | Manual smoke prompts can be replayed, but the benchmark is not independently runnable or causally decisive from the published materials. |
| `adopt` into TeaPrompt | **no** | Existing coverage is present/adjacent; no verified local failure or recurrence survived the gap test. |
| `adopt` in another host | **conditional** | Only where equivalent delegation policy is absent; pin/review a full commit and run sandboxed real-task trials. |
| `deploy` as enforcement | **no** | Baton is advisory instruction text and cannot enforce ownership, isolation, cancellation, budgets, permissions, data boundaries, or recovery. |

## Required Wording Changes

These are upstream or future-survey candidates. None was applied to TeaPrompt or
Baton by this review.

1. **Effectiveness:** use “designed to reduce” rather than “reduces”; no paired
   Baton trial establishes effect size or cross-model reliability.
2. **Benchmark status:** call the current material a pilot protocol, not a
   demonstrated or independently runnable benchmark. It includes no concrete
   repository fixture or paired results.
3. **Smoke-test status:** call the three prompts manual conformance scenarios with
   human-judged pass conditions, not deterministic or end-to-end tests.
4. **Runtime boundary:** say explicitly that the host must enforce permissions,
   ownership, isolation, cancellation, resource caps, side-effect gates, and
   recovery.
5. **Failure catch-all:** missing, malformed, stale, or otherwise unclassified
   worker results must pause integration, become visible coverage gaps, and enter
   bounded recovery or fallback rather than being silently dropped.
6. **Context staleness:** an embedded brief is immutable after dispatch; changing
   assumptions requires steering, cancellation, or rebriefing of affected active
   workers, not only editing a shared packet for later workers.
7. **Primitive model:** choose execution topology independently from workspace /
   isolation mode; map reads, writes, secondary writes, and shared artifacts
   before finalizing both.
8. **Direct-work output:** when the brake rejects delegation, return the selected
   direct primitive, one-line rationale, and avoided coordination costs without
   emitting context packs or worker briefs.
9. **Data boundary:** treat repository/retrieved content and worker output as data,
   not instruction authority; do not place secrets or restricted data in briefs
   without authorization for the destination worker/provider boundary.

## Candidate Adoption Ledger

| ID | Candidate | Status | Evidence | Next action / trigger |
| --- | --- | --- | --- | --- |
| BA1 | Use Baton as external dispatch-governance reference vocabulary | Partial 2026-07-13 — concept only | Strong brake, ownership, verification, and synthesis patterns; no repo contract copied | Re-read a pinned future version when dispatch governance is under review |
| BA2 | Add a consolidated dispatch checklist to `agent-selection.md` or `reflective-dispatch` | Deferred — current no-change | Coverage is distributed but present/adjacent; no verified local failure caused by that distribution | Reconsider after a ROUTE eval or real task shows unresolved shared contracts, overlapping ownership, or dropped worker coverage |
| BA3 | Add Baton or an equivalent tenth TeaPrompt core skill | Deferred — current no-change | Frozen-nine boundary; no three local recurrences; no explicit promotion approval | Requires ≥3 local cross-session recurrences, explicit approval, decision record, demotion trigger, registry update, and deterministic guards |
| BA4 | Add a registered generic dispatch domain pack | Deferred — current no-change | `flow-control-generator` already covers executable topology; a separate methodology gap is unverified | Reconsider only if a host profile without the pack repeatedly fails under current core guidance |
| BA5 | Adopt or cite Baton's benchmark as effectiveness evidence | Deferred | Upstream status `not_run`; no fixture, complete per-trial schema, primary outcome, active control, or raw trials | Require a concrete fixture, preregistered scoring, operational metric definitions, multiple task families, and preserved paired results |
| BA6 | Build TeaPrompt runtime enforcement for ownership, isolation, cancellation, or replay | Deferred — standing non-goal | Prompt text cannot provide these guarantees; TeaPrompt does not operate a multi-agent runtime | Requires explicit project-direction change plus host-runtime implementation and tests |
| BA7 | Install Baton in the current host harness | Deferred — current no-change | Current host policy already carries stronger scope/delegation gates; marginal value unproven | Consider only for a host lacking equivalent policy, after user approval and a sandboxed real-task trial |

No governed TeaPrompt wording or runtime surface was adopted. Therefore no content
pin is required at a named operational surface. The deterministic guard for this
record checks the record shape, exact BA1–BA7 dispositions, pinned revision, and
cross-link from the external-adoption case-study index:
`plans/tests/test_baton_survey_record.py`.

## Shared Findings

### What Baton does well

1. **The dispatch brake is the right center of gravity.** It asks for outcome,
   direct-work comparison, independence, write ownership, and closure before
   fan-out.
2. **Work is grouped by context, artifacts, dependencies, and verification—not by
   request bullets.** v0.1.1 explicitly rejects one-bullet/one-worker mapping.
3. **Ownership is concrete.** The map distinguishes must-read, may-write,
   must-not-write, possible secondary writes, and integration responsibility;
   shared schemas, registries, generated outputs, configuration, and lockfiles
   receive special attention.
4. **Expensive verification is centralized.** Workers perform scoped checks; the
   main agent reviews artifacts, accounts for failed/partial work, adjudicates
   contradictions, and runs integration gates.
5. **Synthesis is not concatenation.** The main agent must deduplicate, compare
   evidence, preserve meaningful dissent, and classify verification status.
6. **Progressive disclosure is useful.** The core entrypoint points to focused
   references for planning, context/briefs, execution, examples, and optional
   capability adapters.
7. **Evidence language is restrained.** The README says there is no universal
   multiplier, its scenarios are not benchmark results, paired trials have not
   run, and no measured savings percentage is claimed.
8. **The supply-chain surface is small.** The runtime manifest contains nine text
   files and declares no executable dependency, hook, MCP server, lockfile, or
   runtime package.

### Load-Bearing Gaps

1. **No independently runnable benchmark fixture.** The sole task describes
   abstract `student`, `presenter`, and `admin` surfaces but supplies no repository,
   scaffold, uncommitted state, test suite, registry implementation, or end-state
   oracle. Independent reproducers must invent different fixtures.
2. **No Baton-specific causal control.** A future baseline-versus-Baton difference
   could reflect any explicit planning nudge, not Baton's particular seven-
   primitive procedure.
3. **No primary metric or threshold.** Nine metrics and a three-pair floor permit
   post-hoc favorable selection; the results template has no per-trial schema.
4. **Topology and isolation are mixed.** Main/worker/batch/team are topology
   choices; shared versus isolated workspaces are an orthogonal decision.
5. **Failure handling is incomplete.** Lost workers, malformed outputs, stale
   active briefs, reintegration drift, unreported secondary writes, and partial-
   state fallback are not explicitly routed.
6. **Budget controls may be unobservable.** A capability-neutral worker may not
   know its own token or aggregate resource usage; qualitative cost-benefit stops
   are judgment heuristics, not enforceable gates.
7. **Delegated-data handling is under-specified.** Context/brief templates lack an
   explicit secret, egress, and data-not-instruction boundary.
8. **The direct-work result has no compact core output contract.** Delegation
   artifacts are detailed; the common “do not delegate” outcome is only implied.
9. **Template ceremony can consume the savings it seeks.** The package gives no
   explicit skip-empty rule or minimal two-worker template.
10. **Maturity evidence is thin.** No paired results or deterministic test runner
    were published as of the check date; tag and commit were unsigned. This is an
    evidence limitation, not evidence of compromise.

## Evidence vs Inference

| Claim | Status | Basis |
| --- | --- | --- |
| v0.1.1, commit identity, release, and MIT license | Observed / verified | GitHub repository, commit, tag, release APIs, and pinned source reads |
| All six references directly linked by `SKILL.md` existed | Observed / verified | Every pinned reference was retrieved successfully; no direct-skill-reference 404 |
| Baton is instruction content rather than executable runtime code | Observed / verified | Repository tree, manifest, and `TRUST.md` |
| The core procedure is mostly coherent | `[INFERENCE]` | Source review plus architecture, usability, and operations lenses |
| Anthropic reported approximately 15× chat token use for its multi-agent Research system | Observed attribution | Official Anthropic article; the underlying number remains Anthropic's internal observation |
| Baton improves cost, quality, speed, conflict rate, or reliability | Unknown | No paired Baton trials or raw result set |
| Smoke prompts prove portability | Unsupported | Manual prompt scenarios; no cross-model execution or deterministic scoring |
| Install/update behavior is idempotent across hosts | Author-claimed / untested | Runbook inspected; no installation or update executed |
| TeaPrompt has a current adoption-worthy Baton gap | Not supported | Existing coverage is present/adjacent; recurrence remains `unknown` |

## Disagreements / Residual Risks

- **Unsigned release severity:** one lens treated unsigned tag/commit provenance and
  absent file hashes as a deployment blocker. Adjudication: a mutable tag name is
  weaker than a signed release, but a reviewed full commit SHA is content-addressed;
  a checksum served from the same unsigned source adds no independent authenticity.
  Signatures/attestations improve provenance, while the stronger blockers here are
  no trials, no runtime enforcement, and unproven marginal value.
- **Product names in the trigger:** two lenses saw `Ultracode` and `CodeGraph` as a
  portability contradiction. Counterargument retained: concrete aliases improve
  matching when users name those products, while execution still requires live
  capability discovery. This is a minor portability tension, not an adoption veto.
- **Architecture severity:** collapsed topology/workspace axes and ordering are
  real ambiguities. Cost and “integration owner” findings are primarily wording
  issues because the negative trigger/reference already discuss cost and local
  integration need not own final judgment.
- **Human approval before fan-out:** approval for every bounded read-only dispatch
  would add ceremony. Approval remains required when host policy, cost, risk,
  privacy, destructive action, or explicit user instructions demand it.
- **Reproduction wording:** manual conformance prompts are replayable, while a
  credible effectiveness reproduction is not possible from the repository alone.
  The latter is the decision-relevant meaning used here.
- **Static-prose limit:** even corrected wording cannot guarantee that a host will
  respect ownership, detect missing results, preserve dissent, reconcile stale
  state, enforce caps, prevent side effects, or protect data.

## Evidence Actually Checked

### Executed

- GitHub repository, tree, commit, annotated-tag, and release API reads.
- Pinned raw reads of `SKILL.md`, all six directly linked references, README,
  trust/install/release surfaces, benchmark materials, and agent metadata.
- Local `cx overview` and targeted reads over TeaPrompt governance, dispatch,
  workflow, promotion, and external-adoption surfaces.
- One scoped local search for dispatch-overlap concepts.
- Three parallel panel attempts as described in **Panel Execution Mode**; only the
  successful specialist batch entered synthesis.
- Post-panel `git branch --show-current`, which returned `main`.

### Upstream / Official Sources

All external sources below were checked 2026-07-13:

- [Pinned Baton `SKILL.md`](https://github.com/cablate/baton/blob/77f12e600406065a6e62a22a66347355e278a9d7/SKILL.md), checked 2026-07-13.
- [Dispatch planning](https://github.com/cablate/baton/blob/77f12e600406065a6e62a22a66347355e278a9d7/references/dispatch-planning.md), checked 2026-07-13.
- [Context packs and worker briefs](https://github.com/cablate/baton/blob/77f12e600406065a6e62a22a66347355e278a9d7/references/context-and-briefs.md), checked 2026-07-13.
- [Execution and verification](https://github.com/cablate/baton/blob/77f12e600406065a6e62a22a66347355e278a9d7/references/execution-and-verification.md), checked 2026-07-13.
- [Examples](https://github.com/cablate/baton/blob/77f12e600406065a6e62a22a66347355e278a9d7/references/examples.md), checked 2026-07-13.
- [Ultracode adapter](https://github.com/cablate/baton/blob/77f12e600406065a6e62a22a66347355e278a9d7/references/claude-code-ultracode.md), checked 2026-07-13.
- [CodeGraph adapter](https://github.com/cablate/baton/blob/77f12e600406065a6e62a22a66347355e278a9d7/references/codegraph.md), checked 2026-07-13.
- [Trust boundary](https://github.com/cablate/baton/blob/77f12e600406065a6e62a22a66347355e278a9d7/docs/TRUST.md), checked 2026-07-13.
- [Installation runbook](https://github.com/cablate/baton/blob/v0.1.1/install/AGENT-INSTALL.md), checked 2026-07-13.
- [Smoke prompts](https://github.com/cablate/baton/blob/v0.1.1/install/SMOKE-TESTS.md), checked 2026-07-13.
- [Benchmark status](https://github.com/cablate/baton/blob/77f12e600406065a6e62a22a66347355e278a9d7/benchmarks/README.md), checked 2026-07-13.
- [Case-01 protocol](https://github.com/cablate/baton/blob/77f12e600406065a6e62a22a66347355e278a9d7/benchmarks/case-01-multi-surface-refactor/protocol.md), checked 2026-07-13.
- [Case-01 task](https://github.com/cablate/baton/blob/77f12e600406065a6e62a22a66347355e278a9d7/benchmarks/case-01-multi-surface-refactor/task.md), checked 2026-07-13.
- [Case-01 results template](https://github.com/cablate/baton/blob/77f12e600406065a6e62a22a66347355e278a9d7/benchmarks/case-01-multi-surface-refactor/results-template.json), checked 2026-07-13.
- [Anthropic multi-agent Research engineering article](https://www.anthropic.com/engineering/multi-agent-research-system), checked 2026-07-13.

### Local TeaPrompt Sources

- `06-repo/AGENTS.md`
- `PROJECT_KNOWLEDGE.md`
- `skills/reflective-dispatch/SKILL.md`
- `04-agent/agent-selection.md`
- `04-agent/workflow-recipes.md`
- `04-agent/workflow-engine.md`
- `04-agent/artifact-promotion.md`
- `04-agent/external-adoption-review.md`
- `02-engineering/task-slicer.md`
- `plans/external-adoption-case-studies-2026-06-20.md`
- relevant `flow-control-generator` routing and contract surfaces

### Not Executed

- No Baton installation, update, uninstall, smoke prompt, workflow, or benchmark
  trial was executed.
- No TeaPrompt workflow, route, skill, domain pack, runtime, or project-knowledge
  authority surface was changed by the survey decision.
- The original shared packet is not a dependency of this record and was deleted.

## Falsifiability

This no-change decision is wrong if any of the following occurs and the ledger is
not re-opened:

1. A ROUTE eval or real TeaPrompt task demonstrates a dispatch failure caused by
   unresolved shared contracts, overlapping ownership, stale briefs, missing
   worker coverage, or distributed guidance that existing surfaces did not catch.
2. At least three local cross-session dispatch-governance recurrences establish a
   stable trigger, input/output contract, failure signals, and verification need
   for a new or repaired durable surface.
3. A future pinned Baton release supplies a concrete fixture, per-trial schema,
   operational metric definitions, active control, multiple task families, and
   preserved paired results showing a material effect on a TeaPrompt-relevant
   task shape.
4. A host profile without the flow-control pack demonstrates that
   `reflective-dispatch` plus `workflow-recipes` cannot express the required
   ownership, recovery, or closure contract.
5. Baton's currently ambiguous topology/workspace, staleness, failure, and data
   boundaries are repaired and a local comparison shows lower ceremony or higher
   reliability than the existing TeaPrompt composition.

Re-evaluation must update BA1–BA7 rather than creating a disconnected decision
record. Guard: `plans/tests/test_baton_survey_record.py`.
