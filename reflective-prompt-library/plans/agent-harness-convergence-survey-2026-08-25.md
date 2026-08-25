# Agent Harness Durable-State Convergence Survey — 2026-08-25

> **Status: decided (non-authoritative); external-concept panel record, no
> runtime adoption.** The checked systems support a shared architectural pattern,
> not an industry consensus or one production-ready architecture. TeaPrompt keeps
> the examples as study material. No candidate changed a TeaPrompt skill, lens,
> dependency, runtime, or project-knowledge rule; the only executable addition is
> a deterministic guard for this record and its no-adoption dispositions.
> `06-repo/AGENTS.md` and governed skill contracts remain authoritative.

## Purpose

Preserve the completed six-lens survey prompted by the claim that Pi, Maka,
Amplio, and Ankole show agent harnesses converging on old OS/database ideas:
persist facts, derive state/context/UI, recover from committed facts, and place
durable intent/outcome records around external effects. The decision question is
which parts are observed, which are specifications or maintainer claims, which
come from database/distributed-systems literature, and what TeaPrompt should
study, reproduce, adopt, or deploy.

## Research Question

Do the four checked repositories justify saying that agent harnesses are
converging on an OS + database architecture, and does `intent → execute →
receipt` make tool effects safely replayable after a crash?

## Targets and Version Context

Checked 2026-08-25 at exact identities:

| Target | Exact identity | Version / maturity evidence | License |
| --- | --- | --- | --- |
| [Pi](https://github.com/earendil-works/pi), checked 2026-08-25 | `dcd461925db2edf69a43c8135db1180d418afd54` | `@earendil-works/pi-agent-core` 0.84.3; harness specification plus storage/reducer code; execution and restore remain scaffolded | MIT |
| [Apache Maka](https://github.com/apache/maka), checked 2026-08-25 | `3a9824a7ea251c084ed40759b2f74ccac1e215b4` | root 0.2.0, runtime packages 0.1.0; T1/T2 and process-crash recovery implemented; production generic reconciler and workspace restore remain future work | Apache-2.0; ASF incubating disclaimer |
| [Amplio](https://github.com/google-deepmind/amplio), checked 2026-08-25 | `8c2e009bb26595d7cad9c93626d9707074daee3a` | no reachable release tag in the shallow clone; DB event-loop recovery implemented; missing tool outcomes become synthetic interrupted results | Apache-2.0 |
| [Ankole](https://github.com/AgentBull/ankole), checked 2026-08-25 | `29cfcd3e11e61b08fc59706d8aa025e0f33756da` | tag `v0.76.2`; addressable actor/runtime architecture and provider outbox inspected; production claims not independently verified | Apache-2.0 |

Primary conceptual sources checked:

- C. Mohan et al., [ARIES](https://research.ibm.com/publications/aries-a-transaction-recovery-method-supporting-fine-granularity-locking-and-partial-rollbacks-using-write-ahead-logging), ACM TODS 1992, DOI `10.1145/128765.128770`; checked 2026-08-25.
- Garcia-Molina and Salem, [SAGAS](https://www.cs.princeton.edu/research/techreps/598), Princeton TR-070-87, 1987; checked 2026-08-25.
- Pat Helland, [Life Beyond Distributed Transactions](https://www.cidrdb.org/cidr2007/papers/cidr07p15.pdf), CIDR 2007; checked 2026-08-25.
- Microsoft Research, [Orleans Virtual Actors](https://www.microsoft.com/en-us/research/project/orleans-virtual-actors/), checked 2026-08-25.
- Erlang/OTP, [Supervisor Behaviour](https://www.erlang.org/doc/system/sup_princ.html), documentation v29.0.5; checked 2026-08-25.
- Apache Flink, [Fault Tolerance](https://nightlies.apache.org/flink/flink-docs-stable/docs/learn-flink/fault_tolerance/), documentation v2.3; checked 2026-08-25.
- Chris Richardson, [Transactional Outbox](https://microservices.io/patterns/data/transactional-outbox.html) and [Idempotent Consumer](https://microservices.io/post/microservices/patterns/2020/10/16/idempotent-consumer.html), supplemental pattern references; checked 2026-08-25.

Volatility rule: every repository claim is scoped to the commit above. Re-pin
before relying on a later revision; current roadmap or production status may
change independently of this record.

## Panel Execution Mode

Method contract: `04-agent/workflow-recipes.md` §Parallel Lens Review with the
host `parallel-lens-review-packet` wrapper.

1. The merge owner cloned all four repositories at the exact commits above,
   inspected load-bearing code/docs/tests, checked primary literature, and ran
   the deterministic commands listed below.
2. One shared packet was written at a repo-readable path. Its SHA-256 was
   `120dbf79376747e58c73c03202cbd689dfe79e5173c0b9ee3789bbe051aa8abe`.
   It separated observed, author-claimed, `[INFERENCE]`, and unknown claims.
3. Six read-only scout lenses fanned out in one batch: evidence audit,
   architecture convergence, reproducibility, provenance/security,
   side-effect correctness, and strategic synthesis. All six complete structured
   deliverables arrived without schema-recovery or refan.
4. The merge owner, not the lenses, executed builds and tests. Lenses did not
   edit files, run project-wide tests, or move repository HEADs.
5. Role labels are review perspectives, not claims that distinct named model
   providers or personas were invoked.

## Lenses

| Lens | Load-bearing question | Main result | Verdict |
| --- | --- | --- | --- |
| Evidence audit | Does “consensus” outrun the checked evidence? | Yes. Pi is a spec/scaffold, Amplio lacks a distinct post-preflight dispatch intent, Maka's generic reconciliation is future work, and Ankole's strongest proof is subsystem-specific | AGREE WITH CHANGES |
| Architecture convergence | What is truly common, and what is conflated? | Durable facts/projections/recovery are common; recovery granularity differs; actor/OTP supervision is orthogonal to effect settlement | AGREE WITH CHANGES |
| Reproducibility | What was executed versus mocked, read, or blocked? | Pi reducer/scaffold, Maka process-crash, and Amplio recovery tests passed; no power-loss or real external-effect test; Ankole tests were not run locally | AGREE WITH CHANGES |
| Provenance/security | Which claims are adoption or deployment blockers? | Maintainer production claims and author backgrounds remain unverified; log durability and sandbox claims cannot be upgraded into side-effect or isolation guarantees | AGREE WITH CHANGES |
| Side-effect correctness | What is safe in every crash window? | A dispatched/no-receipt operation is unknown; reconciliation is adapter-specific; synthetic error results preserve protocol shape but can hide business uncertainty | AGREE WITH CHANGES |
| Strategic synthesis | What is the smallest useful local conclusion? | Study a family of patterns; do not create a TeaPrompt runtime, skill, or dependency; require host proof before deployment | AGREE WITH CHANGES |

## Panel Consensus

- **Decision:** `AGREE WITH CHANGES` — unanimous, **6 of 6 lens verdicts**;
  no `AGREE` and no `DISAGREE`.
- **Direct recommendation:** describe the result as a **shared durable-state-machine
  pattern** or **family resemblance**, not an “industry consensus,” standard, or
  uniform architecture.
- **Observed common core:** committed execution/conversation facts and stable
  identities outrank process memory and chat transcripts; model context, UI, and
  lifecycle state are derived views; restart reads durable state rather than
  asking the model to infer the program counter.
- **Critical correction:** **event replay is not side-effect replay.** A local
  intent proves only that dispatch became possible; a local receipt proves only
  what the runtime durably learned. Neither makes an uncontrolled remote sink
  transactional.
- **Effect rule:** after dispatch but before a durable outcome, the operation is
  `unknown` / `indeterminate`. Automatic retry is allowed only when the same
  stable idempotency identity is enforced by the sink, or tool-specific query
  evidence proves non-execution. Otherwise reconcile, compensate, or stop for
  Human Review.
- **Actor rule:** addressable actors, mailboxes, fencing, and OTP supervision
  solve identity, placement, liveness, backpressure, and failure-domain problems.
  They do not independently settle payments, emails, publishes, deletes, or
  other external effects.
- **TeaPrompt fit:** no local runtime or new workflow surface. Existing
  `runtime-trust-boundary`, `reflective-risk`, external-adoption discipline, and
  the standing prompt-vs-runtime boundary already classify missing enforcement
  evidence as unknown / no-go.

### Exact Qualified Conclusion

> The surveyed systems show a shared durable-state-machine pattern, not a
> demonstrated industry consensus or one architecture. Committed local facts and
> operation identities are treated as authoritative; model context, UI, and
> lifecycle state are projections; recovery reconstructs state from committed
> facts. This makes internal history explainable, but it does not guarantee
> exactly-once external effects. A tool that can mutate state outside the local
> transaction boundary needs a durable pre-dispatch intent, a stable operation
> identity mapped to a sink-enforced idempotency key or query handle, a durable
> outcome receipt, and an explicit `unknown → reconcile | compensate | Human
> Review` path before any retry. Actor addressing and supervision improve
> lifecycle and failure isolation, but remain orthogonal to external-effect
> settlement.

### Use-Case Recommendation

| Use case | Recommendation |
| --- | --- |
| `study` | **yes** — study Maka's T1/T2 and resolver, Ankole's provider outbox and actor fencing, Amplio's simple step boundary, and Pi's total-state specification |
| `reproduce` local crash semantics | **yes, bounded** — the checked Pi, Maka, and Amplio tests reproduce their named internal contracts; reproduce Ankole only with its documented Elixir/PostgreSQL environment |
| `adopt` as a runtime design checklist | **yes, concept only** — durable identities, fact/projection separation, explicit unknown state, adapter-specific reconciliation, version/fence checks, and Human Review fallback |
| `adopt` code/dependencies into TeaPrompt | **no** — no verified local runtime gap; TeaPrompt intentionally does not operate a recorder, replay engine, actor runtime, outbox, or effect enforcer |
| `deploy` for high-stakes external effects | **blocked on this survey alone** — require sink idempotency or query reconciliation, fencing, version migration, chaos/failover and power-loss evidence, monitoring, and an operator path for unresolved unknowns |

## Required Wording Changes

1. Replace **“agent harness consensus”** with **“shared pattern across the four
   surveyed systems”** or **“family resemblance.”** Four selected repositories,
   with different maturity and possible intellectual cross-pollination, are not
   a representative ecosystem sample.
2. Replace **“Pi and Maka implement the same architecture”** with **“Pi's current
   specification and Maka's implemented runtime share intent/effect/settlement
   semantics.”** Pi 0.84.3 still rejects restore, prompt, resume, and action
   execution paths with `HarnessNotImplemented`.
3. Do not say Amplio has the same T1 boundary. It persists the assistant tool call
   before execution and repairs a missing result after restart, but the checked
   loop has no distinct post-preflight dispatch-intent commit or generic
   reconciliation protocol.
4. Scope Ankole's strongest side-effect claim to its provider outbox and other
   named durable subsystems. Its actor/OTP architecture is not proof that every
   Agent Computer tool has transactional outcome recovery.
5. Replace **“WAL makes effects recoverable”** with **“WAL/log-first state makes
   local recovery explainable; outbox/inbox, idempotent sinks, reconciliation,
   sagas/compensation, or Human Review handle cross-boundary effects.”**
6. Replace **“interrupted/failed result”** with a machine-readable uncertainty
   contract where real-world completion cannot be proved: `outcome=unknown`,
   `retrySafe=false`, operation identity, reconciliation evidence, and next
   allowed action. A synthetic error may preserve provider call/result pairing,
   but it must not silently assert that the effect failed.
7. Qualify every “replay” button or API as one of: read-only diagnostic replay,
   pure reducer/projection replay, model re-execution, or external-effect
   re-execution. These have different safety semantics.
8. Qualify “checkpoint” as a recovery contract: for each failure window it names
   the next safe action. A JSON snapshot without effect and version semantics is
   not sufficient.

## Candidate Adoption Ledger

| ID | Candidate | Status | Evidence | Next action or trigger |
| --- | --- | --- | --- | --- |
| AH-1 | Use “shared durable-state-machine pattern / family resemblance,” not “industry consensus” | Adopted in this record only 2026-08-25 | Six lenses agreed the four systems share a core but differ in topology, maturity, and effect semantics | Guard this record's conclusion. Revisit only after a representative ecosystem sample and common conformance contract exist |
| AH-2 | Add a new TeaPrompt canonical rule for `unknown → reconcile | compensate | Human Review` | No change 2026-08-25 | `runtime-trust-boundary.md` already makes missing data/enforcement unknown/no-go; `reflective-risk` already requires side-effect, rollback, audit, and Human Review gates | Reconsider as an in-place repair only after a documented local review authorizes blind retry after a lost receipt, or a host-integration task needs the exact state vocabulary |
| AH-3 | A/B/C kill-point benchmark: memory-only vs transcript-only vs explicit state/intent/receipt/reconciliation | Deferred / study-only 2026-08-25 | The supplied design is falsifiable and useful, but TeaPrompt owns no agent runtime and no current benchmark target was selected | Fire for a specific host-runtime adoption decision; include real instrumented idempotent and non-idempotent sinks, process kill, failover, and power-loss boundaries |
| AH-4 | Create a TeaPrompt recorder, reducer, outbox, reconciler, or actor runtime | Rejected / standing non-goal 2026-08-25 | Runtime enforcement is prompt-impossible but TeaPrompt's product boundary explicitly leaves it to host code/tests; no verified local operational gap changes project direction | Reopen only by explicit project-direction change plus runtime owner, threat model, rollback, migration, and deterministic crash/effect evidence |
| AH-5 | Promote Ankole-style actors, mailboxes, or OTP supervision into core methodology | Rejected / no local gap 2026-08-25 | Addressability and supervision are useful runtime mechanisms but orthogonal to TeaPrompt's prompt/skill layer and do not settle external effects | Study for a concrete host runtime; do not add a routing skill or new architecture layer from external interest alone |
| AH-6 | Import Pi, Maka, Amplio, or Ankole code/dependencies | Rejected 2026-08-25 | Different maturity, storage, license, sandbox, and operational surfaces; no local dependency need; no cross-project external-effect conformance proof | Re-evaluate one pinned component only for a concrete implementation target and local gap, under separate security/license/reproduction review |
| AH-7 | Add a new Project Knowledge lesson or core skill for durable harness recovery | No change 2026-08-25 | Existing durable lessons already state that prompt wording cannot fix execution-layer failures and methodology-complete is not operationally complete; one survey is not local recurrence | Reopen after repeated TeaPrompt-local drift not covered by existing trust-boundary/risk surfaces; new core skill still needs explicit human approval |
| AH-8 | Treat a synthetic interrupted tool result as proof the external action failed | Rejected as a general safety policy 2026-08-25 | Pi spec and Amplio use synthetic results to preserve call/result coherence; neither proves remote non-execution. Maka and Ankole preserve or expose indeterminate/unknown states | Permit only for proven read-only/replay-safe effects, or pair the synthetic provider result with a hard machine-readable unknown gate that blocks automatic retry |

No candidate changed a TeaPrompt skill, lens, dependency, runtime, or
project-knowledge rule. Deterministic guard for this record:
`plans/tests/test_agent_harness_convergence_survey_record.py`.

## Shared Findings

### 1. The common architecture is narrower than “OS + DB”

All four checked systems move authority away from process memory and conversational
prose toward durable identities and records. The useful common shape is:

```text
durable facts + stable identities
  → pure or deterministic reduction
  → operational state
  → model-context projection
  → UI / telemetry projection
```

That is compatible with event sourcing, WAL discipline, explicit state machines,
and materialized views. It does not require every implementation to use a pure
append-only log: Pi's specification also uses current-value registers; Amplio
uses a step/status model; Ankole has several PostgreSQL-owned subsystem ledgers.

### 2. Tool-boundary evidence differs materially

| System | What is observed | What is not established |
| --- | --- | --- |
| Pi | Specification defines total operation state, effect sandwich, reserved result IDs, and `replay: safe | never`; record types and reducer exist | Full `AgentHarness` execution/restore; general reconciliation; end-to-end external effects |
| Maka | T1 commits call + `toolDispatch` after preflight; T2 commits `function_response` before model continuation; resolver blocks dispatch/no-response; SIGKILL prefix tests pass | Production generic Phase-3 reconciler, file evidence, workspace restore, power-loss and real-sink exactly-once |
| Amplio | Assistant tool calls are durable before execution; results append as tools finish; restart repairs missing results and redoes incomplete LLM turns | Distinct post-preflight dispatch intent, per-tool replay policy, operation-id reconciliation, proof that an orphan tool did not mutate external state |
| Ankole | Provider outbox persists intent, marks `sending` before adapter call, reconciles when supported/evidenced, otherwise records `unknown_after_send`; actor fencing rejects stale workers | Universal coverage of arbitrary Agent Computer tools; provider exactly-once where the API lacks keys/query evidence; independent production verification |

### 3. Crash windows need different recovery actions

| Last durable fact | What is known | Only safe default |
| --- | --- | --- |
| No intent | No admitted external action | Replan or decide again |
| Intent committed; dispatch contract proves tool not called | Effect did not cross the boundary | Dispatch once, after current authorization/version checks |
| Dispatch committed; no durable receipt | The effect may or may not have happened | Mark `unknown`; query with the same operation identity, compensate, or stop for Human Review; do not blind-retry |
| Durable receipt committed; reducer/projection not advanced | External outcome is known at the evidence tier of the receipt | Re-run pure reduction/projection only; never call the tool again |
| Terminal state committed | Local operation is closed | Do not infer end-to-end business success without postconditions/acceptance evidence |

A stable local `operation_id` is necessary but insufficient. It must map to a
sink-enforced idempotency key, provider receipt/query handle, or domain-specific
reconciliation evidence. Reusing the same string at a non-idempotent sink does
nothing by itself.

### 4. The literature supplies several mechanisms, not one silver bullet

- **ARIES/WAL:** log-before-page and repeat-history ideas explain local durable
  recovery when one system controls log and data pages. They do not enroll a
  remote API in the transaction.
- **Event sourcing/materialized views:** explains fact authority and rebuildable
  context/UI, but does not make effect handlers replay-safe.
- **Transactional outbox/inbox + idempotent consumer:** atomically records local
  intent/business change; the relay may still publish twice, so sink or consumer
  deduplication remains required.
- **Sagas/compensation:** models hours/days of locally committed work and semantic
  repair when global ACID is unavailable.
- **Helland's entities/activities:** makes stable entity identity, at-least-once
  messaging, durable relationship state, and explicit uncertainty central.
- **Orleans actors + OTP supervision:** provide stable addressing, activation,
  failure isolation, and restart strategy; persistence and effect semantics
  remain separate contracts.
- **Flink's exactly-once distinction:** replay can make managed local state
  exactly-once while end-to-end exactly-once still requires replayable sources
  and transactional or idempotent sinks.

### 5. The supplied recoverable-run fields are sound, with one structural caveat

The six groups in the supplied article are all load-bearing:

1. immutable task identity and tenant/creator;
2. explicit execution position, plan version, step, attempt, checkpoint;
3. versioned context-artifact/evidence references;
4. pending external action, stable operation/idempotency identity, and real
   receipt or explicit unknown state;
5. approval, authority, budget, deadline, cancellation, and compensation state;
6. model/prompt/code/tool-policy/state-schema versions.

They need not live in one mutable JSON document. A durable log plus validated
current-state projections can be safer, provided every field has one authority,
atomic transition rules, migration semantics, and a rebuild path.

### 6. Long pauses and deployment changes are state transitions

Approval binds to a plan/parameter/resource version, not merely an operation
name. Resume after hours or days must revalidate principal authorization,
resource versions, plan digest, deadlines, budgets, cancellation, tool schema,
and relevant external state. A checkpoint crossing a deployment must select
compatible old code, perform a total migration, or enter `needs_human`; silently
starting from scratch can repeat effects and loses provenance.

### 7. Context compression is a projection, never the only fact source

Summaries reduce tokens but can omit parameters, failures, approvals, and
versions. Durable raw facts or artifact references remain authoritative; a
summary is replaceable context material assembled under the current budget.
This finding is supported directly by Pi and Maka designs and is compatible with
Amplio/Ankole's database-owned histories.

### 8. A falsifiable evaluation should include external-state evidence

The supplied A/B/C design is directionally strong:

- A: memory-only loop;
- B: transcript-only restart;
- C: explicit state, pending intent, receipt, versions, and reconciliation.

For a real adoption decision, inject failures after model output, before/after
intent commit, after external success before receipt, after receipt before
reduction, during approval, after compaction, during cancellation, and across a
schema/code deployment. Include both a sink with client idempotency/query and a
controlled non-idempotent sink. Measure recovery correctness, duplicate effects,
lost progress, unknown-resolution rate, manual interventions, MTTR, and
persistence latency/storage cost. A process-kill-only mock suite is not power-loss
or end-to-end proof.

## Evidence vs Inference

| Claim | Status | Basis |
| --- | --- | --- |
| Pi documents the effect sandwich and replay policy | Observed / source-read | pinned `packages/agent/docs/harness.md` |
| Pi's current full harness executes that specification | Refuted at checked revision | `AgentHarness` methods reject; scaffold tests confirm |
| Maka implements T1/T2, resolver classification, and process-crash committed-prefix recovery | Observed / source-read + executed | targeted builds and 40 tests across runtime/runtime-host |
| Maka generically reconciles arbitrary external effects | Refuted at checked revision | current resume architecture marks production Phase 3 reconciler future |
| Amplio resumes the loop and repairs orphan call/result pairs | Observed / source-read + executed | event-loop package and targeted crash tests |
| Amplio proves the orphan tool did not execute | Refuted | synthetic result has no external reconciliation evidence |
| Ankole implements provider-outbox unknown/reconcile semantics | Observed / source-read; repository test-read | `OutboxEntry`, `outbox.ex`, recovery tests |
| Ankole's complete production behavior and all arbitrary tool boundaries work as claimed | Unknown | local Elixir tests and deployment evidence unavailable |
| Four projects prove an industry consensus | Unsupported inference | selected sample is too small and heterogeneous |
| The projects show a useful family resemblance | Supported inference | common durable fact/projection/recovery pattern across pinned sources |
| Maka's core authors' database backgrounds caused the design | Unknown / non-load-bearing | no contributor provenance audit; causation unnecessary to the architecture finding |

## Disagreements / Residual Risks

- **Convergence strength:** one lens used “converge” for the shared core; the
  evidence and strategy lenses preferred “family resemblance.” Merge decision:
  retain convergence only as a bounded pattern across these four, never as
  ecosystem consensus.
- **Harness responsibility:** a strong objection says the harness may own only
  internal consistency, leaving reconciliation to tools/adapters. Accepted with
  a boundary condition: then the harness must still preserve `unknown`, block
  unsafe automatic retry, and require the adapter/sink contract rather than
  converting uncertainty into ordinary failure.
- **Synthetic results:** they are valid for provider protocol pairing and can be
  safe for proven read-only operations. They are unsafe as business-state truth
  for non-idempotent effects unless paired with a machine-readable unknown gate.
- **Database analogy:** useful inside the local authority boundary; misleading
  across remote systems because the database does not control the external sink.
- **Selection bias:** Pi/Maka/Amplio/Ankole were selected because they relate to
  the thesis. LangChain, AutoGen, Temporal-backed systems, cloud workflow
  engines, and other harnesses were not sampled. No ecosystem-frequency claim
  survives this limitation.
- **Power and storage failures:** checked crash evidence covers process death and
  committed prefixes, not fsync/controller/power-loss behavior.
- **Workspace drift:** a correct event ledger can coexist with a changed
  filesystem, revoked permission, replaced tool schema, or external resource.
- **Operational unknown backlog:** fail-closed design needs monitoring, ownership,
  deadlines, and an operator queue; otherwise safety becomes indefinite limbo.
- **Isolation:** runtime durability says nothing about sandbox strength or data
  egress. Those require separate host security evidence.

## Evidence Actually Checked

### Executed by merge owner

- Four shallow clones; `git rev-parse HEAD` matched every identity above.
- Pi: `npm ci --ignore-scripts`; model-data hydration; targeted harness scaffold
  and reducer run — **2 files, 135 tests passed**. The first attempt exposed the
  documented generated-model-data prerequisite; hydration then produced the
  successful run.
- Maka: dependency install; builds of core, storage, MCP, runtime, and
  runtime-host; targeted T1/refusal, resolver, phase-0/phase-1 SIGKILL,
  client-capability, host recovery, and continuation tests — **25 runtime tests
  passed** and **15 runtime-host tests passed**.
- Amplio: `go test ./internal/agent/eventloop` passed; targeted orphan-tool,
  mid-LLM, and complete-unfinalized crash tests passed.
- TeaPrompt shared branch remained `main` before synthesis.

### Read but not executed

- Pi harness specification, record/reducer/scaffold code, changelog, and tests.
- Maka runtime-event, T1/T2, resolver, resume/status-boundary code/docs/tests.
- Amplio README, step/lifecycle docs, event loop, SQLite store, and tests.
- Ankole README, RuntimeFabric, known limits, provider outbox code, Slack adapter,
  and recovery tests.
- The official/primary conceptual sources listed under Targets.

### Unverified / blocked

- Ankole Elixir tests: host lacked the required Elixir toolchain; PostgreSQL and
  runtime prerequisites were not provisioned.
- Real payment/refund/email/publish/delete effects under crash, failover, and
  network partition.
- Power-loss durability and durable-volume failover.
- Pi full harness execution, because it is not implemented at the checked pin.
- Broad industry adoption frequency, causal author-background claims, Ankole
  deployment/production claims, and any behavior of the truncated X article URL
  beyond the user-supplied text.

## Local TeaPrompt Fit

| Mechanism | Existing coverage | Verified local gap? |
| --- | --- | --- |
| Evidence versus runtime guarantees | `PROJECT_KNOWLEDGE`, `runtime-trust-boundary`, `artifact-promotion`, external-adoption review | no |
| Unknown/missing enforcement → no-go | `runtime-trust-boundary` Data Policy and Human Review | no |
| High-risk side-effect authorization, rollback, audit, Human Review | `reflective-risk` | no |
| Proposal/authorization/effect/acceptance separation and broker receipts | governance concepts/domain pack | no runtime claim; host-owned |
| Persistent recorder/replay/reconciliation/actor runtime | explicit standing non-goal | out of scope |
| Exact crash-window benchmark | no owned runtime to test | deferred until a specific host-runtime decision |

Therefore the smallest sufficient destination is this external-survey decision
record plus its adoption-state guard. External interest does not count as local
promotion recurrence.

## Falsifiability

This decision is wrong if any of the following becomes true:

1. A representative, pre-registered ecosystem sample shows the shared pattern is
   rare or unnecessary for comparable long-running, side-effectful tasks.
2. Pi at the checked revision can execute prompt/tool/restore paths despite the
   inspected `HarnessNotImplemented` code and tests.
3. Maka's checked generic production reconciler or workspace restore already
   settles arbitrary external effects, contrary to its current status document.
4. Amplio's checked loop carries a durable post-preflight dispatch identity and
   external reconciliation evidence not present in the inspected path.
5. Ankole's provider outbox proves universal arbitrary-tool recovery rather than
   a subsystem-specific contract.
6. A local log alone prevents duplicates at a non-idempotent, non-queryable sink
   after external success and before local receipt; this would overturn the
   central event-replay/effect-replay distinction.
7. TeaPrompt develops a verified local runtime gap that existing trust/risk
   surfaces cannot describe; then AH-2/AH-3/AH-4 must be re-litigated rather than
   silently retained.
8. Any rejected or deferred candidate ships without changing this ledger and its
   deterministic guard.

## 2026-08-25 Technical Lineage Addendum

> **Status: decided (non-authoritative); scoped addendum, no new runtime or
> governed method adoption.** This addendum reviews the incremental
> Temporal/LangGraph/DBOS/Restate/Orleans/OTP lineage and the proposed nine-layer
> runtime, Effect Contract, effect taxonomy, first-class `UNKNOWN`, fencing
> invariant, and fault benchmark. It does not change AH-2–AH-8 or TeaPrompt's
> no-owned-runtime boundary.

### Target and provenance

- User-supplied analysis: `local://paste-1.md`, 2,795 lines, SHA-256
  `b07cb166cd2345e7a04c7b79e922bc0a000f721c6a92b64585db06737fe2c8d9`;
  checked 2026-08-25. Author, creation tool/model, and generation process are
  unknown.
- Shared packet: repo-readable temporary file, SHA-256
  `903527f5fe84498f1ce6191402c5292ec2fdc8ac6b4c5c3efa1232b01bdf939d`.
- Incremental sources: official live documentation for Temporal, LangGraph,
  DBOS, and Restate, checked 2026-08-25; Microsoft Learn Orleans page at source
  commit `a4303ce92aa169102f57793c84aae0603c75c3a3`; Erlang System Documentation
  v29.0.5 / `OTP-29.0.5`; and AWS Well-Architected idempotency guidance.
- Volatility boundary: Temporal, LangGraph, DBOS, Restate, and AWS pages were
  live documentation, not pinned release artifacts. Recheck release-to-doc
  correspondence before relying on them for implementation or deployment.
- Broken source pointer: the supplied Pi path
  `packages/agent/docs/harness-v2.md` returned HTTP 404. The current path is
  `packages/agent/docs/harness.md`; the prior exact Pi revision and scaffold
  maturity findings in the main survey remain authoritative for this record.

### Panel Consensus

- **Decision:** `AGREE WITH CHANGES` — unanimous, **7 of 7 lens verdicts**;
  no `AGREE` and no `DISAGREE`.
- **Panel execution:** seven read-only scout perspectives—evidence,
  architecture, reproducibility, provenance/security, effect correctness,
  usability, and strategic fit—read one shared packet. All seven complete
  structured deliverables arrived without schema recovery, refan, or
  merge-owner inference of a missing verdict.
- **Incremental result:** the expanded sources strengthen the **mechanism map**:
  durable orchestration, step/journal replay, shared-resource transactions,
  runtime-mediated actions, actor identity, and supervision solve distinct
  failure classes. They do not prove genealogy, independent invention,
  ecosystem frequency, one minimal architecture, or industry consensus.
- **Replay result:** Temporal Workflow replay reuses recorded Activity results,
  while Activity executions themselves retry and must tolerate duplication;
  LangGraph time travel explicitly re-executes post-checkpoint nodes; DBOS
  transactions are exactly-once only when application writes and the durability
  record share one transaction; Restate's strongest guarantees attach to
  runtime-mediated journal operations. None turns a raw third-party call into an
  exactly-once external effect.
- **Architecture result:** the proposed nine layers are a useful discussion
  diagram, not a verified minimal stack. Journal/facts and current state may be
  separate stores, one log plus materialization, or total-state registers.
  Supervision and fencing are ownership/liveness controls, not a layer that
  settles external outcomes.
- **Effect result:** the linear `Pure | Read | IdempotentWrite | ...` taxonomy
  compresses independent dimensions. It is study material, not a sound
  automatic retry type system at this evidence tier.
- **Local fit:** no verified TeaPrompt gap. The smallest durable destination is
  this addendum and its guard. No skill, prompt lens, runtime, dependency, MCP
  extension, or Project Knowledge rule is added.

#### Exact qualified conclusion

> The expanded lineage shows recurring mechanisms, not a proven family tree or
> one future Agent Runtime standard. Durable control state and replay can recover
> local orchestration; context and UI are usually projections; supervision and
> fencing constrain ownership and local commits. None of those guarantees
> exactly-once external effects. A cross-boundary mutation is safe to retry only
> when its exact parameters and authorization remain valid and the sink enforces
> a retained idempotency contract or exposes decisive reconciliation evidence.
> Otherwise the durable outcome is `UNKNOWN`: automatic retry stops, an owner
> reconciles or compensates, and Human Review may close the operation with an
> explicit unresolved disposition. Recovery is a protocol, not a prompt.

#### Use-case recommendation

| Use case | Recommendation |
| --- | --- |
| `study` | **yes** — compare Temporal replay/Activity retry, LangGraph node re-execution, DBOS shared-resource transactions, Restate journal/epoch mechanics, Orleans addressability, and OTP supervision as distinct contracts |
| `reproduce` | **deferred by target** — first choose a concrete host/version; run the fault matrix with real idempotent and controlled non-idempotent sinks rather than treating official docs as execution proof |
| `adopt` into TeaPrompt methodology | **no new surface** — the existing trust-boundary, risk, adoption, and main-survey rules already require runtime proof and unknown/no-go discipline |
| `adopt` in a host runtime | **concept checklist only** — durable intent, parameter-bound identity, receipt, explicit unknown, reconciliation owner, authorization/version binding, and fencing at the actual commit authority |
| `deploy` high-risk mutation recovery | **blocked by this evidence** — no real-sink, power-loss, failover, privacy/retention, or operator-queue proof was executed |

### Required Wording Changes

1. Replace **“Temporal Activity runs once”** with: **“Workflow replay reuses a
   recorded Activity result; Activity execution may retry and must be safe under
   its retry policy.”** Replay suppression is not external exactly-once.
2. Replace **“Temporal is the direct ancestor”** with **“Temporal is a strong
   prior-art analogue.”** No source-history or influence evidence establishes
   genealogy.
3. Scope DBOS exactly-once to `RunAsTransaction` when application writes and the
   DBOS durability record commit atomically in the same database transaction.
   Ordinary/external steps remain at-least-once and need idempotency.
4. Scope Restate guarantees to Restate Context operations and journal-mediated
   actions. Raw side effects in unmediated user code do not inherit journal
   replay suppression, epochs, or exactly-once behavior.
5. State that LangGraph replay is **execution replay** after the chosen
   checkpoint: LLM calls, API requests, and interrupts can fire again. An
   interrupt-containing node restarts from its beginning.
6. Replace **“fencing prevents zombie effects”** with **“fencing rejects stale
   commits or messages only where the epoch authority is checked.”** It cannot
   recall a request already accepted by an external sink.
7. Replace **“the nine layers are the final architecture”** with **“the diagram
   is one study decomposition.”** Facts and current state can share one durable
   substrate, and liveness, effects, projections, and policy are orthogonal
   contracts rather than a mandatory stack.
8. Replace the linear effect sum type with a **multi-axis descriptor candidate**.
   Read/write shape, transactional coupling, sink idempotency, queryability,
   compensation, reversibility, privacy, cost, rate limits, concurrency scope,
   and authorization lifetime can coexist.
9. Replace **“every effect eventually reaches success/failure”** with **“every
   admitted effect eventually reaches an explicit durable disposition.”** A
   non-queryable sink may end as unresolved/abandoned under Human Review rather
   than a fabricated success or failure.
10. Replace **“accepted model output is immutable”** with **“runtime-accepted
    transition identity and provenance are durable at the host's evidence tier.”**
    Correction, supersession, precise rewrite, redaction, retention, and deletion
    requirements still need explicit policy.
11. Remove the unsupported **“bottom 70–80% is not AI”** percentage. The sources
    support mechanism reuse, not a measured allocation of architecture or work.
12. Describe the P0–P3 priority table as a **risk-specific hypothesis**. A
    read-only local assistant and a payment-capable long-running service do not
    warrant the same effect, fencing, supervision, or operator machinery.

### Technical Lineage Candidate Adoption Ledger

| ID | Candidate | Status | Evidence | Next action or trigger |
| --- | --- | --- | --- | --- |
| AH-9 | Add the Temporal/LangGraph/DBOS/Restate/Orleans/OTP technical-lineage qualification to the existing survey | Adopted in this record only 2026-08-25 | Seven lenses found the lineage useful after replay/exactly-once/genealogy qualifications; a scoped addendum avoids duplicating the decided four-system survey | Guard source/packet identity, 7/7 verdict, mechanism boundaries, and no-runtime disposition; recheck live docs before later implementation claims |
| AH-10 | Treat the nine-layer diagram as TeaPrompt's canonical/minimal Agent Runtime architecture | Rejected as canonical; study-only 2026-08-25 | No comparative implementation or fault experiment proves its minimality; facts/state may share a substrate and several layers are orthogonal | Reopen only after a pre-registered comparison shows the decomposition prevents failures a smaller control/effect/ownership design misses at acceptable cost |
| AH-11 | Promote `Pure | Read | IdempotentWrite | TransactionalWrite | ReconciliableWrite | CompensatableWrite | IrreversibleWrite` as an automatic retry type system | Deferred / study-only 2026-08-25 | The labels collapse independent axes; no schema, checker, adapters, or conformance suite was executed | Fire for one concrete host integration after defining multi-axis semantics, sink retention/parameter binding, negative tests, and a Human Review fallback |
| AH-12 | Add first-class `UNKNOWN` as a new TeaPrompt canonical rule | No change 2026-08-25; AH-2 unchanged | The main survey and `runtime-trust-boundary` already classify missing outcome/enforcement as unknown/no-go and forbid evidence-tier upgrades | Reopen only after documented local wording permits blind retry or a host contract needs a machine-readable state schema |
| AH-13 | Encode fencing epochs or OTP supervisor strategies in prompts/core methodology | Rejected / host-runtime only 2026-08-25 | Prompt variables cannot reject stale commits; OTP process restart does not settle external effects; Restate/DBOS fencing is enforced by runtime state authorities | Reopen for a named host runtime with an enforcement owner, lease/epoch store, stale-writer tests, and external-sink boundary analysis |
| AH-14 | Expand AH-3 into the proposed Harness Reliability Benchmark | Deferred / study-only 2026-08-25; AH-3 unchanged | The fault matrix adds zombie, network, power, version, approval, and cancellation cases, but no benchmark target or result exists | Fire only for a concrete adoption decision; pre-register baselines, real sinks, postconditions, cost/latency metrics, power/failover tier, and operator burden |
| AH-15 | Add an Effect Contract prompt lens, core skill, MCP extension, compiler, or runtime dependency | Rejected / no verified local gap 2026-08-25 | No MCP spec audit, interoperability test, host target, or TeaPrompt recurrence supports another surface; enforcement is explicitly outside TeaPrompt | Re-evaluate one destination only after a named host/adaptor needs it and existing trust/risk contracts cannot express the gap |
| AH-16 | Persist every accepted raw model output as permanently immutable execution history | No change / needs host retention design 2026-08-25 | Stable accepted-transition provenance is useful, but the proposal omits correction, supersession, privacy, redaction, retention, and precise-rewrite semantics | Reopen for a host-specific evidence schema with data classification, minimum retention, deletion/rewrite authority, audit trail, and migration tests |
| AH-17 | Adopt the universal P0–P3 research priority order | Rejected as universal; use-case-specific 2026-08-25 | No incident, efficacy, cost, or latency data shows one order fits low-risk/read-only and high-risk/mutating systems | Revisit per product using measured failure frequency, effect severity, operator load, and current enforcement gaps |
| AH-18 | Promote the guarded lineage synthesis into high-traffic docs and the trigger-gated roadmap | Adopted 2026-08-25 by explicit user direction; recurrence `unknown` | The user explicitly requested recording the conclusions in docs and roadmaps; the guarded addendum supplies the evidence/unknown split, while minimality rejects a new skill, prompt lens, runtime, glossary, or directory | Keep one concise three-contract reference in `METHODOLOGY_MAP.md`, source-triggered rows in the whole-project roadmap, and a Decision Index pointer; reopen additional surfaces only after a named local navigation or host-integration gap |

No AH-9–AH-18 row creates a TeaPrompt runtime, dependency, skill, prompt lens,
MCP extension, or governing Project Knowledge rule. AH-9 is record-level
wording; AH-18 adds reference documentation, roadmap triggers, and a Decision
Index pointer only.


### Shared Findings

#### 1. The lineage is a mechanism map, not a genealogy

Official documentation supports recurring solutions to recurring failure
classes:

| Mechanism | Checked analogue | Evidence boundary |
| --- | --- | --- |
| deterministic orchestration replay | Temporal Workflow Event History | completed Activity results are reused during Workflow replay; Activity attempts can still retry |
| checkpoint-based node re-execution | LangGraph time travel / interrupts | post-checkpoint nodes and pre-interrupt node code execute again |
| shared-resource atomic durability | DBOS `RunAsTransaction` | exactly-once only inside the database transaction coupling application write and durability record |
| log/journal-mediated durable actions | Restate Context and replicated log | strongest claims attach to mediated actions; raw external calls remain outside the proof |
| stable logical identity/lifecycle | Orleans virtual actors | addressability and activation do not imply external-effect atomicity |
| failure hierarchy/restart strategy | Erlang/OTP supervisors | controls child process liveness, not business compensation or remote settlement |

This comparison strengthens the claim that durable Agent systems reuse mature
mechanisms. It does not establish that these products caused later Agent designs,
that their implementations are equivalent, or that most Agent systems use them.

#### 2. Three contracts are smaller than nine mandatory layers

A minimal review model can ask for three independently enforceable contracts:

1. **Control-state contract:** durable task/run identity, accepted transition,
   current program counter or reducible facts, schema/execution versions, and
   rebuildable context/UI projections.
2. **Effect contract:** authorized parameter-bound intent, dispatch boundary,
   sink contract, outcome receipt, explicit unknown state, reconciliation,
   compensation, postcondition verification, and Human Review fallback.
3. **Ownership/liveness contract:** lease or owner identity, epoch/fencing scope,
   cancellation, supervision/restart policy, and stale-writer rejection at the
   actual commit authority.

Model output is an input proposal to the control-state contract. Policy,
authorization, budgets, deadlines, data handling, and observability cut across
the three contracts. Implementations may split these concerns into more modules
or collapse them into one transactional substrate; the contract boundaries, not
the number of boxes, carry the safety claim.

#### 3. Effect behavior is multi-axis

The supplied taxonomy is useful vocabulary but unsafe as a mutually exclusive
sum type. A host-specific effect descriptor would need to bind at least:

- **identity:** `operation_id`, exact parameter digest, schema/tool/code version,
  and resource identity/version;
- **authority:** principal, approval/plan digest, scope, issue/expiry time,
  cancellation state, and dispatch owner/epoch;
- **boundary:** local pure, transactionally coupled, runtime-mediated remote, or
  raw external effect;
- **sink contract:** idempotency key scope, retention/TTL, parameter comparison,
  response replay semantics, query handle, and concurrency behavior;
- **recovery:** allowed retries and caps, reconciliation adapter/evidence,
  compensation preconditions, unresolved owner/deadline, and Human Review path;
- **acceptance:** receipt schema, expected postconditions, independent verifier,
  and final business disposition;
- **risk/data:** reversibility, privacy/data classification, redaction/retention,
  cost/budget, rate limits, and deadline.

This is a study schema, not an implemented TeaPrompt contract. No source in this
panel proves the list sufficient or interoperable.

#### 4. `UNKNOWN` needs operations, not only a label

The post-dispatch/pre-receipt window cannot be truthfully collapsed into
`FAILED`. A practical durable state model distinguishes:

```text
AUTHORIZED
  → INTENT_COMMITTED
  → DISPATCH_COMMITTED / OUTCOME_PENDING
  → SETTLED_SUCCESS | SETTLED_FAILURE
  → OUTCOME_UNKNOWN
       → RECONCILING
       → SETTLED_SUCCESS | SETTLED_FAILURE
       → COMPENSATING → COMPENSATED
       → NEEDS_HUMAN → UNRESOLVED_CLOSED | ABANDONED
```

`DISPATCH_COMMITTED` means the implementation may have crossed the boundary; it
does not prove the sink received the request. `OUTCOME_UNKNOWN` forbids automatic
retry unless the sink's retained idempotency contract makes the exact retry safe
or decisive query evidence proves `NOT_STARTED`. The record also needs an owner,
next action, deadline, attempt/cost budget, and operator decision. “Closure” means
an explicit durable disposition, not invented certainty about the external world.

#### 5. Fencing has a precise authority boundary

Restate epochs and DBOS conflicting-checkpoint handling illustrate the value of
rejecting stale journal/checkpoint commits. They do not cancel an HTTP request
already accepted by a third party. Fencing helps only when:

1. the stale attempt carries the epoch or ownership proof;
2. every relevant commit passes through an authority that compares it;
3. the authority durably rejects superseded epochs; and
4. an external sink either participates in that identity contract or is handled
   separately through idempotency/reconciliation.

Thus **durability is not exclusive execution**, but neither is local fencing a
universal external-effect fence.

#### 6. Runtime-accepted proposals need provenance and lifecycle

Re-running an LLM after a crash can propose a different transition, so the exact
proposal accepted by runtime—including parameter and policy versions—should be
recoverable. That does not require every raw token or private context to remain
immutable forever. A host must define which accepted fact/reference is durable,
how corrections and supersession are represented, what can be redacted or
precisely rewritten, retention/deletion authority, and how old executions bind
to compatible code/model/tool semantics.

Hashes are identities and change detectors, not semantic compatibility proofs.
Remote model snapshots may be unavailable; the correct fallback may be pinned
old execution, explicit migration, or `needs_human`, not a claim that a hash
recreates the old model.

#### 7. The smallest useful engineer checklist is risk-scaled

For a tool that may mutate external state:

1. Name the exact mutation, resource, principal, approval/plan version, and
   expiry.
2. Persist a parameter-bound intent and stable operation identity before
   dispatch.
3. Verify what the sink actually enforces: idempotency key, retention window,
   parameter matching, response replay, or query handle.
4. Persist a real receipt and validate business postconditions before success.
5. On an ambiguous result, enter owned `OUTCOME_UNKNOWN`; do not blind-retry.
6. Reconcile, compensate, or route to Human Review with a deadline and audit
   record.
7. Fence stale local commits at the runtime authority and separately account for
   already-escaped external requests.
8. Inject a crash in the post-dispatch/pre-receipt window and observe the sink,
   not just the local log.

Low-risk pure computation does not need this ceremony. Read-only operations may
still need privacy, cost, rate-limit, freshness, and audit policy, but they do
not automatically inherit the mutation protocol.

#### 8. The benchmark remains a candidate test plan

The proposed fault matrix usefully adds model/intent/dispatch/receipt/reducer
boundaries, lease expiry, zombies, network partitions, approval delays,
version/schema upgrades, and cancellation propagation. A real comparison must
pre-register:

- baselines: memory-only, transcript/checkpoint, graph checkpoint, explicit
  durable state, and effect-aware treatment;
- controlled sinks: one with retained idempotency + query, one transactionally
  coupled resource, and one deliberately non-idempotent/non-queryable sink;
- postconditions observed outside the runtime;
- process-kill, durable-volume failover, network ambiguity, stale-worker, and
  power-loss tiers kept separate;
- duplicate/lost effects, silent unknowns, invalid transitions, stale commits,
  unresolved backlog, MTTR, Human Review load, latency, storage, and cost.

Until that executes, the matrix falsifies nothing and proves no architectural
ranking.

### Evidence vs Inference

| Claim | Status | Basis |
| --- | --- | --- |
| Temporal Workflow replay uses recorded history and reuses completed Activity results | Official documentation read, not runtime execution | live Temporal docs checked 2026-08-25 |
| Temporal Activities execute exactly once | Refuted as a general claim | official retry docs say Activity executions retry and expect idempotent code |
| LangGraph time travel re-executes post-checkpoint LLM/API/interrupt nodes | Official documentation read | live LangGraph docs checked 2026-08-25 |
| DBOS can atomically couple application DB writes and durability records | Official documentation read; scoped | `RunAsTransaction` on a shared transactional database resource |
| DBOS external steps are exactly-once | Refuted as a general claim | official outbox/workflow docs describe ordinary/external steps as at-least-once/idempotent |
| Restate uses a replicated log, journal replay, and attempt epochs | Official documentation read | live Restate docs checked 2026-08-25 |
| Restate epochs prevent every external duplicate | Unsupported inference | epochs fence runtime-mediated records; raw escaped calls were not tested |
| Orleans provides stable virtual actor identity and lifecycle | Official documentation read | Microsoft Learn source identity recorded above |
| OTP provides restart strategies and bounded restart intensity | Official documentation read | Erlang System Documentation v29.0.5 |
| Temporal/DBOS/Restate are direct ancestors of Agent harnesses | Unknown | no source-history or influence study |
| Nine layers or the effect taxonomy improve reliability/cost | Unknown | no baseline/treatment run |
| The lineage changes TeaPrompt's runtime direction | Refuted locally | no verified gap; standing non-goal and AH-4 remain |

### Disagreements / Residual Risks

- **Formal stack versus minimal contracts:** the strongest objection says a
  formal nine-layer model prevents ad hoc integration. The panel retained its
  vocabulary as study material but rejected canonical layering until a smaller
  design demonstrably misses failures.
- **Simple effect tags versus multi-axis policy:** simple tags are ergonomic, but
  the panel rejected using them alone for automatic retry. A host may expose a
  friendly label only if it compiles to explicit sink, authority, recovery, and
  risk semantics.
- **Generic versus adapter-specific reconciliation:** a generic runtime can own
  the `UNKNOWN` state machine, evidence schema, budgets, and escalation. The
  observation/query that resolves a particular external operation remains
  adapter- and sink-specific.
- **Fail-closed versus operational limbo:** blocking blind retry is correct but
  incomplete. An unowned unknown queue is a reliability failure; it needs
  deadlines, escalation, monitoring, operator tools, and an explicit unresolved
  terminal disposition.
- **Immutable history versus data lifecycle:** durable provenance is valuable,
  but raw immutable content may conflict with correction, retention, deletion,
  or privacy obligations. The exact legal requirement is deployment-specific
  and was not researched here.
- **Fencing illusion:** epochs stop only commits that consult the epoch authority.
  HTTP clients, SDK retries, and remote sinks can execute beyond that boundary.
- **Selection bias:** the sources were chosen because they expose durable
  execution, log, actor, and supervision mechanisms. No ecosystem-frequency or
  universal necessity claim survives.
- **Evidence tier:** this addendum read official docs and prior local records. It
  did not launch or fault-inject the incremental systems; documentation drift and
  implementation divergence remain possible.

### Evidence Actually Checked

#### Coordinator-executed in this addendum phase

- Parsed and read bounded sections of the 2,795-line supplied artifact; recorded
  SHA-256 `b07cb166cd2345e7a04c7b79e922bc0a000f721c6a92b64585db06737fe2c8d9`.
- Read official Temporal Workflow, Event History, retry-policy, and Go-versioning
  documentation.
- Read official LangGraph time-travel and interrupt documentation.
- Read official DBOS workflow, Go transaction, transactional-outbox, and
  concurrent-execution documentation.
- Read official Restate architecture and request-lifecycle documentation.
- Read Microsoft Learn Orleans overview at recorded source commit, Erlang/OTP
  v29.0.5 supervision docs, AWS idempotency guidance, and the current Pi harness
  path; confirmed the supplied Pi `harness-v2.md` URL is HTTP 404.
- Built one 564-line shared packet, SHA-256
  `903527f5fe84498f1ce6191402c5292ec2fdc8ac6b4c5c3efa1232b01bdf939d`,
  and ran seven read-only lenses in parallel.

#### Read from the prior durable record, not re-run here

- Pi's 135 targeted scaffold/reducer tests.
- Maka's builds and 40 targeted runtime/runtime-host tests, including process-kill
  committed-prefix recovery.
- Amplio's event-loop package and targeted crash tests.
- Ankole source/test inspection and the prior Elixir-toolchain blocker.

#### Not executed / still unknown

- No incremental Temporal, LangGraph, DBOS, Restate, Orleans, or OTP runtime,
  clone, build, test suite, provider call, network partition, zombie execution,
  power-loss, or real external-effect scenario.
- No source-history study establishing genealogy or independent convergence.
- No benchmark comparing nine layers, three contracts, outbox-only, graph
  checkpoints, or transcript-only baselines.
- No MCP specification/interoperability review and no complete Effect Contract
  implementation.
- No legal determination about retention/deletion; only a deployment requirement
  to define data lifecycle and authority.

### Addendum Falsifiability

This addendum is wrong or must be re-litigated if:

1. a pinned Temporal version proves Activity external effects execute once across
   post-effect/pre-completion crashes without sink idempotency or reconciliation;
2. a pinned DBOS or Restate runtime proves a raw non-idempotent third-party call
   cannot duplicate outside its transactional/journal mediation boundary;
3. a pre-registered fault benchmark shows the nine-layer design prevents a
   material failure that the smaller control/effect/ownership contracts cannot,
   at acceptable latency, storage, and operator cost;
4. a formal multi-axis effect schema and conformance suite demonstrate that the
   linear taxonomy alone is sound for retries across representative adapters;
5. a host runtime can prevent an already-accepted remote mutation solely by
   changing its local fencing epoch;
6. a TeaPrompt-local incident exposes a gap not expressible by the existing
   trust-boundary, risk, external-adoption, or main-survey contracts;
7. AH-10–AH-17 status changes without the recorded trigger and deterministic
   guard changing with it.
