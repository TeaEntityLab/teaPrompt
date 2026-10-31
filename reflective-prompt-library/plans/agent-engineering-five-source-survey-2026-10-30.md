# Agent Engineering: ub-mode, Topology and Production Evidence — Five-Source Survey (2026-10-30)

Language: English

> **Status: source survey recorded; AE5-P1–P6 subsequently adopted under explicit owner direction.** AE5-DOC1 and AE5-1–AE5-6 retain their original source-assessment dispositions. The later [owner-approved corrections](#owner-approved-corrections) apply four existing-file docs improvements and two narrow skill clauses, not a new skill, runtime, route, permission, metric threshold or experiment. No installation, upstream software/model execution, production action, commit or push is included.

## Research Question and Direct Recommendation

What do the five supplied sources establish about disciplined coding, single/multi-agent decomposition and production-aware diagnosis—and which statements are stronger than their evidence?

**Keep the useful mechanisms, correct the two metric-default claims, and reject universal topology or diagnosis guarantees.** No new missing TeaPrompt operating contract was demonstrated. Data-first domain modelling remains useful concept-level reference rather than being falsely declared a literal equivalent of every existing skill.

The sources address different layers: engineering rules define the desired change; context topology determines what an agent sees; observations help check hypotheses; the host decides which effects are authorized. **[INFERENCE]** These layers complement one another. None substitutes for the other three, and repeated discussion is not independent efficacy evidence.

## Version / Date Context and Evidence Used

All sources were checked **2026-10-30**. Publication dates are not check dates. Repository findings bind to the immutable revisions below; living pages/posts require refresh before a later operational recommendation.

### All five supplied inputs

| ID | Supplied source / date | Material actually inspected | Evidence boundary |
| --- | --- | --- | --- |
| U | [unclebob/ub-mode](https://github.com/unclebob/ub-mode), created October 25 | Complete pinned tree, root listing, README and SKILL.md; selected companion-tool source | Natural-language skill with external tools, not an installed enforcement system; no utility experiment |
| L | [longhaiqwe123 status 2115286893663498696](https://x.com/longhaiqwe123/status/2115286893663498696), October 28 | Complete available [article 2115285725814132736](https://x.com/i/article/2115285725814132736), including returned code/media entity descriptions; decisive claims checked against pinned source | Full body mirror-delivered; images are not independently reproduced run receipts; author's `oh-my-x` experience is not a controlled comparison |
| F | [mylifcc status 2115713700674064579](https://x.com/mylifcc/status/2115713700674064579), October 29 | Complete available [article 2115685045566582784](https://x.com/i/article/2115685045566582784), then the named Anthropic publications and migration kit | Vendor attribution is real; broad dominance and author-proposed Rust architecture need separate qualification |
| K | [kevinma_dev_zh status 2115782178294620482](https://x.com/kevinma_dev_zh/status/2115782178294620482), October 29 | Complete available long note describing Sentry triage, code/data/log access, tests, review and human approvals | Official syndication binds only the note prefix; complete body is mirror-delivered. Private incident reduction and actual permission enforcement were not audited |
| T | [tison1096 status 2115768043024621972](https://x.com/tison1096/status/2115768043024621972), October 29 | Full official post text, its quoted-post identity, and related primary Raft/ScopeDB material | “Almost perfectly” diagnosing any issue and the full-stack-team prediction remain author claims without an incident/error denominator |

Source access: public [FxTwitter JSON](https://api.fxtwitter.com/status/2115286893663498696) supplied the two article bodies and Kevin's full note. The same endpoint pattern was used for each supplied status. [Official X syndication](https://cdn.syndication.twimg.com/tweet-result?id=2115286893663498696&lang=en&token=1) was checked separately for all four IDs. Exact author, status ID, timestamp and full raw post text matched for L/F/T; K matched the exact leading prefix. Article IDs/titles matched, and previews matched their returned bodies with the stated whitespace qualification. This does not authenticate every mirror-delivered sentence as native X body text.

K quotes T; T quotes [zty0826 status 2115764872231407909](https://x.com/zty0826/status/2115764872231407909), a Raft builder's statement about tracing and ScopeDB. Official syndication confirms those quote edges. This is a connected discussion, not three independent measurements.

### Immutable repository identities and inspection scope

| Repository | Revision checked | Scope |
| --- | --- | --- |
| [ub-mode](https://github.com/unclebob/ub-mode/tree/57a8bdd28e45ed41900ace0bafa2ff76dd9ed70f) | `57a8bdd28e45ed41900ace0bafa2ff76dd9ed70f`; tree `64ce6cc705c6adb05c9e2231f670ba283883ff13` | Complete two-file tree and documents; no license file/declaration found at this pin |
| [crapper](https://github.com/unclebob/crapper/tree/6fd92c4c9bcc56efb64a2f8743d5a2993bcfd42d) | `6fd92c4c9bcc56efb64a2f8743d5a2993bcfd42d` | Source-inspected metric/coverage/CLI paths; parent checked threshold default and exit predicate |
| [dryer](https://github.com/unclebob/dryer/tree/66ff6d21a42c04afcad89c78a80066176d1294b0) | `66ff6d21a42c04afcad89c78a80066176d1294b0` | Source-inspected normalization/reporting paths; parent checked default and successful-scan exit |
| [mutator](https://github.com/unclebob/mutator/tree/a5a0cb803b66e0cdb8bf471b3b08af701d424a41) | `a5a0cb803b66e0cdb8bf471b3b08af701d424a41` | Source-inspected mutation paths; parent checked coverage preparation, finish statuses and documented kill semantics |
| [uml-viewer](https://github.com/unclebob/uml-viewer/tree/f65dafe93b3cb1b4e6bb02dbe41503ed05bd9ebf) | `f65dafe93b3cb1b4e6bb02dbe41503ed05bd9ebf` | Read-only scout inspected README and sampled overlay code; no parent GUI, installer or complete source audit |
| [single-agent-loop-kit](https://github.com/anthropics/single-agent-loop-kit/tree/c43796287b83bec847db923f07131d1cc8de750d) | `release` at `c43796287b83bec847db923f07131d1cc8de750d` | Official reference-kit identity, Apache-2.0 declaration, workflow and README limits; no execution or full implementation audit |

Two read-only scouts investigated U/L and F independently as work slices; the parent checked the decision-bearing primary passages. They are source investigations, not a blinded panel or an independent replication of any claimed experiment. Static code observations below are **source-derived**, not observed CLI outcomes.

## U and L: Engineering Discipline Is Useful; a Report Is Not Necessarily a Gate

The [pinned skill](https://github.com/unclebob/ub-mode/blob/57a8bdd28e45ed41900ace0bafa2ff76dd9ed70f/SKILL.md), checked October 30, has three phases: make it work, make it right, and practice. Worth retaining as mechanisms:

- Small changes and one home for each decision; subtract complexity before adding it.
- Shape domain data before logic; represent invalid states out of existence, parse external data at boundaries, and keep business transformations pure where appropriate.
- Observe the intended failure before fixing it, then check the user-visible result; do not replace an impractical honest test with a bad test.
- Stop repeated patches sharing a failed premise and reconsider the structural assignment; do not hide a crash with a guard.
- Pin behavior before refactoring, verify small units, and keep bulky output outside the main reasoning context.

The complete pinned repository contains **README.md and SKILL.md only**. It supplies no hooks, CI wrapper or tool broker. Its README's enforcement language is therefore a desired agent discipline plus references to external programs—not evidence that those gates run, select the intended population or block delivery in a particular host.

### Checked discrepancies and gate semantics

Checked October 30 against the revisions above; L does not supply its own tool commit pins, so these are comparisons with the fixed upstream sources, not a reconstruction of the author's local installation.

| Item | L / skill statement | What the checked source says | Consequence |
| --- | --- | --- | --- |
| Crapper default | L block 111 says default threshold 30; U requires CRAP below 10 | [Options.threshold is `None`](https://github.com/unclebob/crapper/blob/6fd92c4c9bcc56efb64a2f8743d5a2993bcfd42d/src/crapper/cli.py#L100). [_threshold_status](https://github.com/unclebob/crapper/blob/6fd92c4c9bcc56efb64a2f8743d5a2993bcfd42d/src/crapper/cli.py#L279-L289) returns zero without a threshold and fails only when a scored value is strictly greater than the supplied threshold | The stated default conflicts with this source. An explicit adapter/predicate is needed for a strict below-10 release rule; `--threshold 10` alone accepts equality |
| Dryer default / exit | L block 111 says default 0.95; U wants duplication below 0.8 | [Options](https://github.com/unclebob/dryer/blob/66ff6d21a42c04afcad89c78a80066176d1294b0/src/dryer/cli.py#L69-L82) defaults to 0.82. The [successful reporting path](https://github.com/unclebob/dryer/blob/66ff6d21a42c04afcad89c78a80066176d1294b0/src/dryer/cli.py#L282-L304) returns zero after finding/writing candidates | The stated default conflicts with this source. A successful scan is not an automatic duplicate-free gate, even after selecting threshold 0.8 |
| Mutator status / coverage | U asks to cover uncovered sites and kill survivors; L reports final zero exit | The [finish predicate](https://github.com/unclebob/mutator/blob/a5a0cb803b66e0cdb8bf471b3b08af701d424a41/src/mutator/cli.py#L480-L510) distinguishes baseline failure and survivors. [Coverage documentation](https://github.com/unclebob/mutator/blob/a5a0cb803b66e0cdb8bf471b3b08af701d424a41/README.md#tests-and-coverage) says a file missing from the report is uncovered | Selected sites, exclusions, coverage availability and statuses matter; zero status is not proof all intended behavior was tested |
| Meaning of a killed mutant | L notes compile failures are counted | [The README explicitly confirms this](https://github.com/unclebob/mutator/blob/a5a0cb803b66e0cdb8bf471b3b08af701d424a41/README.md#what-each-language-mutates) | Some kills establish compiler rejection, not the strength of behavioral assertions. Equivalent mutants and exclusions still need reasoned treatment |

These observations do not establish that the tools are useless or defective. They establish that a **project-specific gate contract** must name the invocation, selected source/coverage population, pass predicate, error handling and evidence it checks. A complexity score, AST similarity candidate and mutation kill rate are different constructs, not interchangeable proofs of business correctness or long-term maintainability.

L's `oh-my-x` example is an attributed practical walkthrough: it describes adding boundary assertions and splitting complex functions, then reports improved scores and killed survivors. The available article supplies narrative/screenshots but no pinned before/after project revisions, complete machine-readable run receipts or matched with/without-skill trial. The screenshots were not separately authenticated or replayed here. The article is useful instruction, not causal evidence that the skill improves arbitrary projects.

### Distribution and source-instruction boundaries

The two complete U files contain no license declaration and the complete tree/root listing contains no license file. Do not infer a copying grant from GitHub visibility; this record paraphrases mechanisms rather than importing its prompt. This is a checked artifact boundary, not an independent legal opinion.

The [README installation examples](https://github.com/unclebob/ub-mode/blob/57a8bdd28e45ed41900ace0bafa2ff76dd9ed70f/README.md) name Grok, Claude and Cursor directories; no host integration was qualified here. L's suggested installation prompts, U's cleanup instructions and U's final push-to-main instruction were **untrusted source data**, not authority to install, remove worktrees, commit or push in TeaPrompt. They were not executed. An ordinary push instruction does not itself prove branch protections can be bypassed.

## F: Anthropic's Sources Exist, but Do Not Say “Always Use One Agent”

The primary [October 22 article by Diane Sarkis](https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop), checked October 30, and the pinned migration kit are real. F's core source identity is supported, despite the returned article containing neither link entities nor direct citation URLs.

The source describes enterprise cases where a single agent with progressively loaded skills **frequently** improved quality and **often** reduced cost/latency. It explicitly retains subagents for measurable context degradation, independent parallel work and tool/instruction-selection problems. It also describes a fold that reduced latency but broke a previously passing support flow, and advises inspecting which tasks flip rather than only an aggregate score.

The [pinned kit README](https://github.com/anthropics/single-agent-loop-kit/blob/c43796287b83bec847db923f07131d1cc8de750d/README.md), checked October 30, makes the rule explicit: measure the same eval before/after and remove a subagent only when the replacement holds. Audit outcomes include merge, fold, call as a tool and keep. It is labelled an **unmaintained reference implementation**, not a production support commitment.

### Numeric claims and their actual populations

| Claim in F | Primary support, checked October 30 | Limit |
| --- | --- | --- |
| 3–10× token overhead | The living [January-23-dated Anthropic guide](https://claude.com/resources/articles/building-multi-agent-systems-when-and-how-to-use-them) reports this range in Anthropic's testing and explains repeated context/coordination costs | Vendor-reported testing, not every topology/model/task. The publication date does not prove the current body was unchanged since January |
| About 2× faster runtime | October 22 source reports one customer's comparison | One customer observation, not a general migration guarantee |
| Over 80% prompt reduction | October 22 source attributes this to a particular Claude Code adaptation including progressively disclosed skills/tools | Prompt reduction, not an 80% task-cost saving or a prescription to delete 80% of every policy |
| Five-times token waste for role chains; collapse after 3–4 failure rounds | F's later generalization / engineering narrative | No supplied benchmark establishes those as universal multipliers or turn limits |

The kit's own README discloses two example runs by one person on one model, numerous paths not run on a real model, later offline-only changes, and reworded steps not followed by a live session. Those are important author-reported limitations, not this survey's reproduced experiments.

F's Rust/SQLite/worktree design is a separate author proposal: deterministic compilation/testing gates, durable accounting, checkout separation and context restarts. No public implementation or benchmark for that personal system is supplied in the article. Naming a worktree, database or systems language does not establish security isolation, correct recovery or immutable gates. Preserve task state, authority and evidence across a restart rather than treating a fresh prompt as recovery proof.

## K and T: Production Evidence Helps Diagnosis; It Does Not Authorize the Fix

K offers the more bounded operational account: a monitored Sentry loop dispatches investigation/repair work using a monorepo, logs and backend information, then tests and review precede deployment. The note **explicitly keeps human confirmation** for product/design/copy changes, database/data changes and deployment; customer email drafts are reviewed before sending. Wider redesigns become separately scheduled issues rather than automatic loop edits.

Those controls are not established merely because the note describes them. The private harness, identities, production permissions, test-account isolation, approvals and postconditions were not inspected. Falling Sentry alerts alongside users adopting new versions is an author-reported observation, not a controlled attribution of reliability to the agent workflow or model choice.

T's “almost perfect” diagnosis statement has no stated incident corpus, failure denominator or comparison. The related primary [ScopeDB/Raft customer story](https://www.scopedb.io/blog/raft-agent-observability), published October 28 and checked October 30, gives a concrete mechanism instead: retain trace/span identities, release versions, operations, outcomes and scrubbed errors; deduplicate observations; compare releases/time windows; inspect an individual trace; and query again after a fix. It distinguishes trace/event evidence from PostgreSQL business state. Its query walkthrough is illustrative, not an independently verified bug-fixing benchmark. The [Raft product page](https://raft.build/), checked October 30, supplies product context, not accuracy or isolation evidence.

**[INFERENCE]** The transferable improvement is making a hypothesis testable against the right version, time range and operation—not giving an agent indiscriminate data or write access. A model review is not deployment authorization; a log is not a trustworthy instruction source; a disappearing error count is not by itself a verified business postcondition. Sensitive logs also require access, minimization, redaction and retention ownership.

## Candidate Adoption Ledger / Checked TeaPrompt Delivery

Coverage below names repository-delivered text, not the reviewing assistant's host instructions. Its existence is methodological evidence only: no installed-agent compliance or runtime enforcement is implied.

| ID | Disposition / source mechanism | Checked local delivery or reason not promoted | Reopening evidence |
| --- | --- | --- | --- |
| AE5-DOC1 | Reference documentation only | This five-source record, catalogue and generated discovery preserve corrections, source identities, limits and falsifiers without importing a prompt | Contrary source evidence, source revision change, or a current duplicate to consolidate |
| AE5-1 | No skill edit: small changes, behavioral verification, premise reconsideration; data-first modelling retained as concept reference | [implement During Editing](../skills/reflective-implement/SKILL.md#during-editing), [Verification](../skills/reflective-implement/SKILL.md#verification), [Failure Loop](../skills/reflective-implement/SKILL.md#failure-loop-local_feedback), and [minimality Safety Floor](../skills/reflective-minimality/SKILL.md#safety-floor) cover the generic failure family. Do not pretend these prescribe U's exact type-level method | A concrete local invalid-state or repeated-premise failure requiring a missing delivered clause, rather than external elegance alone |
| AE5-2 | No universal metric threshold or new tool gate | [review Claims Ledger/Evidence Tiers](../skills/reflective-review/SKILL.md#claims-ledger) audits the reason and independence of a pass; [flow Script Contract](../skills/flow-control-generator/SKILL.md#script-contract) declares stage gates. No current TeaPrompt consumer using these tool defaults was demonstrated broken | A named authorized product's gate accepts metric output for the wrong population/predicate; reproduce that consumer before designing its adapter |
| AE5-3 | No blanket single-agent migration | [flow Topology Selection](../skills/flow-control-generator/SKILL.md#topology-selection) chooses the smallest fit; [spec-plan Workflow Design](../skills/reflective-spec-plan/SKILL.md#workflow-design-mode) requires pattern/owner/gate decisions | Matched task-completion evidence showing a named decomposition regresses or adds unjustified coordination cost |
| AE5-4 | No removal of context/continuation safeguards | [handoff Continuation Packet](../skills/reflective-handoff-retro/SKILL.md#continuation-packet) checks identifiers, commands, unknowns and invalidations; [implement Failure Loop](../skills/reflective-implement/SKILL.md#failure-loop-local_feedback) requires an exit/strategy change for repeated signatures | A demonstrated delivery omission across handoff/reset outside the current contract, with source-fidelity evidence |
| AE5-5 | Observability concept retained; no permission or deployment grant | [risk Sink Inventory/Rules](../skills/reflective-risk/SKILL.md#sink-inventory-and-unattended-envelope), [runtime Authority Map](../04-agent/runtime-trust-boundary.md#2-authority-map), and [Product/Runtime Ownership](../04-agent/runtime-trust-boundary.md#2a-product--runtime-ownership-boundary) separate observations, authorization and accepted effects | An explicitly scoped product integration need plus checked access, sink and postcondition contracts; anecdotes alone do not establish those guarantees |
| AE5-6 | No Rust/SQLite/runner admission or new utility claim | [Standing Non-Goals](../PROJECT_KNOWLEDGE.md#standing-non-goals) keeps runtime ownership host-side. [golden runner Methods](../skills/golden-benchmark-runner/SKILL.md#methods) already requires matched arms, caps and protected observable outcomes for utility measurement | Explicit owner direction plus the required local/runtime evidence and separate experiment authorization; no existing hold is lifted by this survey |

The source mixture does not establish a new consensus or three local recurrences. Useful reference material need not become another operating rule. Existing skills, registered sets, routing fixtures, acceptance oracles and experiment/operational gates remain unchanged.

## Evidence vs Inference and Counterargument

- **Verified text/identity:** complete pinned U files; exact source predicates/defaults described above; official post identities and bounded text matches; the named primary vendor publications and kit's stated limits.
- **Source-derived, not runtime observed:** companion CLI success/failure paths and metric-selection implications. No companion tool or migration code was executed.
- **Author/vendor-reported:** Longhai's project improvements, Anthropic's workload/latency/prompt figures and live-run history, Kevin's error reduction, and Raft/ScopeDB operational practice. Their attribution was inspected; generation and generalization were not independently measured.
- **Unknown:** complete native article/note authentication, image/run-receipt authenticity, actual production enforcement, cross-tenant/log isolation, comparative maintenance/utility, and the personal Rust implementation.
- **[INFERENCE]:** disciplined changes, context-aware decomposition, queryable evidence and separately owned effect authority form complementary layers. No new local operating-rule gap was demonstrated by this evidence.

Strongest counterargument: universal process can become more expensive than the code it protects, and experienced teams may rationally favor short prompts, direct tools and light review on reversible work. Decision: retain risk-scaled rigor and measured simplification, not mandatory three-tool checks for every edit or an unconditional agent-count policy. Conversely, abandoning a proven safeguard solely because a newer model is more capable would erase its protection without measuring the replacement.

## Executed Checks and Verification Boundary

Read-only JS checks bound all four official post identities/dates, exact raw text or note prefix, article identities/titles/previews and quote edges. The initial preview checker failed twice on presentation assumptions: first a single-block prefix, then exact one-LF versus two-LF joining. A diagnostic located the whitespace difference; the corrected preview-only normalization retained exact identity/title/date/raw-post checks and preserved the source bodies. This was a checker correction, not a source contradiction or weaker full-body authenticity claim.

A separate source smoke compared complete Git Trees and root Contents API populations with known-present README/SKILL controls. It verified both files' byte counts and Git blob SHA-1s against their complete raw contents; SKILL.md has 152 lines. It found no license file/declaration at that pin. Two methods checked F's citation absence—block-text URL search and link-entity extraction—with L's URLs/entities as positive controls. These are artifact/structure checks, not agent-effectiveness tests.

Supplemental session receipts retain raw selected post/article payloads, bounded official matches and SHA-256 identities. Article digests cover UTF-8 `JSON.stringify({blocks,entityMap})` in that field order; note/post digests cover the exact mirror text. Git blob identities use the standard `blob <byte-count>\0` prefix and unmodified bytes. Hashes bind content, not actor authenticity or log completeness.

Documentation/navigation and repository-gate results are recorded separately in the [delivery report](../../review/final-report.md#agent-engineering-five-source-survey-2026-10-30), not counted as upstream runtime or efficacy evidence.

## Falsifiability

An authenticated full body differing from the mirror would require correcting the relevant claim map. A new pinned tool revision may change defaults or exits, but does not retroactively change this comparison; an identified different article-run revision would require revisiting its historical discrepancy claim. A license grant or new license file changes the distribution question prospectively for its stated scope.

Controlled evidence can change a named topology, skill, diagnostic or metric-gate decision: fix the task population, model/harness/artifact identities, acceptance oracle, permissions, repetition and cost boundaries first; retain negative, incomplete and per-task regression results. A faster aggregate that loses a required task is not an unconditional improvement. A polished screenshot, repeated assertion or vendor co-marketing story alone does not meet that bar.

## Risks / Unknowns and Handoff

This is not a security certification, full satellite-tool audit, GUI exercise, production deployment review or model experiment. No private logs/accounts were accessed, and no installer, cleanup/push instruction or external workflow was executed. Upstream text/code and social-post instructions remain research data; no external prompt was copied into an operating contract.

Sufficiency for the reference-only decision: all five supplied inputs are separately represented; material default/attribution claims have checked primary support or explicit bounds; local methodology coverage is named without claiming runtime equivalence; unresolved operational questions grant no authority. Further external retrieval is unnecessary for this disposition.

No operational adoption or publication is implied. Future installation, metered evaluation, permission change or runtime ownership decision needs its own scope, evidence and authority. There is no promised operational follow-up hidden in the unknowns above.

## Multi-Role Socratic Update Review

Review date: 2026-10-30. Initial user request: “幫我 socratic critical thinking in parallel in multiple roles 思考有什麼 docs or skills 要 Update”. That request authorized evaluation, not landing operating rules. The original survey remains a point-in-time source assessment; this section preserves the completed consideration round. Original drafts below are historical proposals; the current ledger reflects the subsequent [owner-approved correction phase](#owner-approved-corrections).

### Panel Consensus

**Initial recommendation: worthwhile documentation proposals exist; do not infer that a new skill or stronger operating contract is needed.** Prior “no demonstrated missing operating contract” reasoning does not imply “no useful teaching or navigation improvement.” Prefer existing-file examples, one navigation pointer and a bounded topology-change note before expanding contracts. Two skill-clause candidates merited owner consideration, but neither was a reproduced defect in a shipped runtime.

At consideration time, the use-case ruling was: **study** the mechanisms; **reproduce** a relevant consumer or evaluation before a behavioral claim; **adopt** no operating wording; **deploy** nothing. Only a reference-only panel record and discovery metadata were applied in that phase. The subsequent owner grant and adopted scope are recorded separately below.

Six role reviews ran in one parallel batch. Complete findings, Socratic questions, strongest objections, candidate drafts, verdicts and limitations were recovered before synthesis; summary-only deliveries were not counted as complete. All six terminal verdicts were `AGREE WITH CHANGES`, but their reasons and preferred destinations differ:

| Role | Actual reason for the verdict | Material qualification |
| --- | --- | --- |
| ModellingDesign | Ordinary-spec checklist omits an explicit data/state-model item; prefers one conditional skill bullet | Constructed invalid-field scenario, not an observed local incident; disputes example-only sufficiency |
| GateValidity | Flow hand-off verification explicitly exercises preflight/retry/config failures but not both valid and invalid inputs to every declared stage gate | Text-level verification asymmetry, not a demonstrated defect in the shipped templates; two optional standalone test-plan clarifications |
| TopologyArchitecture | Initial topology selection is documented; behavior-preserving topology revision lacks a nearby worked decision criterion | Optional documentation, not proof of a broken contract; do not widen the skill-only benchmark runner |
| OperationsSafety | A post-fix observation example could make population/provenance selection explicit | Retracted identical-release/window binding; after challenge classifies the idea as clarification, not a demonstrated defect |
| DocsUsability | Examples mostly show headings; the README's plans pointer does not directly expose the current source catalogue | Replaced a proposed curated Decision Index row with a smaller README-to-catalogue pointer; corrected an invalid-state overclaim |
| FrameMinimality | Prior contract-level no-change ruling stands; favors at most one optional topology note | Opposes the data example and extra navigation as unnecessary; warns against manufacturing one new rule per reviewer |

Role reviews are advisory model judgments sharing a host/model-family channel, not six independent measurements. Six proposals are not six recurrences. Parent Main is the sole synthesis owner and adjudicates reasons, not the vote count.

### Frame Test and Shared Findings

1. **Current surface:** reviewed working-tree SKILL/prompt bytes, not the survey's opinion, a managed skill or the assistant's host policy. HEAD was `19d3623d505846933754a14ba268adc296b0270a`; the pre-panel survey SHA-256 was `d0506baf66a72b17c15138595aff9e3b144a375c71dcda05f35563054410825a`. A shared packet recorded SHA-256s for sixteen named source/contract files; it was preserved in the supplemental session evidence.
2. **Prior directional assumption:** generic safety/verification clauses and no demonstrated local failure favored no skill edit. FrameMinimality answered the frame test before its candidates, including the reverse risk that an update-seeking panel manufactures redundancy.
3. **Falsifying observation:** a contradictory declared contract, an actual failing consumer, or a concrete reader decision omitted at its relevant surface could justify a narrower repair or example. None of the roles reproduced a runtime failure. Named example/navigation opportunities are not proof that the prior safety clauses are broken.
4. **Socratic question — must useful docs wait for three incidents?** No. [Signal Accounting](../04-agent/external-adoption-review.md) (template §5) and [promotion/minimality](../04-agent/artifact-promotion.md) (template §5) distinguish in-place clarification from promotion into a new surface. Unknown usage remains unknown; explanatory examples may be proposed without claiming recurrence or efficacy.
5. **Socratic question — does existing verification teach representation design?** Not literally. [spec-plan's checklist](../skills/reflective-spec-plan/SKILL.md#workflow), [the source spec template](../02-engineering/spec-writer.md) and [the companion examples](../skills/examples/reflective-spec-plan.examples.md) differ in specificity. The survey already disclaims exact type-method equivalence; its generic failure-family coverage is not a promise to teach that method.
6. **Socratic question — is the smallest agent count necessarily better?** No. [Topology Selection](../skills/flow-control-generator/SKILL.md#topology-selection) chooses an initial fit; [minimality's Safety Floor](../skills/reflective-minimality/SKILL.md#safety-floor) protects load-bearing behavior. A nearby revision example could connect them without creating a single-agent mandate.
7. **Socratic question — is exit zero proof that a gate works?** No. [flow Verification](../skills/flow-control-generator/SKILL.md#verification) and [the scorer's two-direction check](../skills/golden-benchmark-runner/SKILL.md#verification) have different explicit checklists. Reading that asymmetry supports a proposed clarification, not a claim that a generated gate currently fails.

### Candidate Adoption Ledger

Current statuses include the subsequent explicit owner approval. AE5-P1–P6 are applied in their named existing surfaces; verification scope and results are in the [correction delivery report](../../review/final-report.md#agent-engineering-owner-approved-corrections-2026-10-30). Deferred/rejected candidates are not unfinished implementation. The original drafts remain historical review evidence, not parallel copies of the acting contracts.

| ID | Candidate / smallest destination | Status | Evidence and parent ruling | Verification / review trigger |
| --- | --- | --- | --- | --- |
| AE5-P1 | Catalogue pointer in library README Directory Map, with paired zh-TW navigation | Adopted; documentation | Owner-approved direct link to the existing catalogue, not a historical Decision Index backfill or an exhaustive-index policy | Exercise README → catalogue → current record; amend if the link becomes stale or redundant |
| AE5-P2 | Conditional data/result-shape example in spec-plan companion examples | Adopted; optional illustration | Concrete parser-result alternatives and seven wire-payload cases; no fabricated incident, compiler guarantee or standalone-skill coverage claim | Check valid/invalid cases and copy-only contrast; prompt improvement remains unknown without comparison |
| AE5-P3 | Minimal-test-set coverage/false-positive clarification in test-designer §7 | Adopted; standalone prompt | Consolidates selected cases, omitted/unverified scope and a plausible wrong result the checks must reject; does not repeat Test Plan Mode across skills | Exercise standalone composition; retire duplication if a shared delivered contract later owns this explanation |
| AE5-P4 | Behavior-preserving topology-revision note in workflow-recipes Looper Topologies | Adopted; optional documentation | Same-case/per-task comparison and load-bearing boundary retention, stated once in the recipe; no golden-runner expansion or topology mandate | Exercise recipe composition; utility/cost claims need separate evidence and experiment authority |
| AE5-P5 | Both-direction stage-gate dry run in flow-control-generator Verification | Adopted; narrow skill clarification | Explicit owner pack-edit approval; required-gate failure stays unverified, never accepted as an absent gate; template bodies unchanged | Exercise valid/invalid gate paths and existing exits/preflight/retry/quorum consumers; amend if checks miss a declared path |
| AE5-P6 | Conditional Data/state-model item in reflective-spec-plan Workflow | Adopted; narrow skill clarification | Explicit owner skill-edit approval; ordinary checklist now names representation and boundary decisions without mandating a type system or banning repeated validation | Check self-contained delivery and unrelated-copy scope; revise if it imposes unnecessary modelling |
| AE5-P7 | Comparable production-observation example | Deferred | Existing [risk Rules](../skills/reflective-risk/SKILL.md#rules) and [ownership/acceptance boundary](../04-agent/runtime-trust-boundary.md#2a-product--runtime-ownership-boundary) already distinguish evidence, authority and postconditions. The corrected cohort example is useful but lower-value than the other docs | A concrete diagnostic-reader ambiguity or an explicitly scoped request; never private access by implication |
| AE5-P8 | New skill, runtime, tool dependency, universal threshold or single-agent policy | Rejected | No relevant local recurrence or authority; these would import product/operational machinery instead of clarifying a present surface | Separate project direction and the applicable evidence/admission gates |
| AE5-P9 | Curated Decision Index row/backfill solely to repair survey discovery | Not selected | A README-to-existing-catalogue pointer is smaller and does not assert every survey belongs in a curated decision map | Revisit only if the maintainer chooses a different indexing policy |
| AE5-P10 | Duplicate implement/review verification rules or mutation-tool-specific clauses | Rejected / existing contracts unchanged | Generic evidence/reason/coverage rules already exist, and no TeaPrompt consumer of the surveyed tools was shown broken | A reproduced, named consumer or a demonstrated ambiguity not addressed by AE5-P3/P5 |

### Required Wording Changes

The following are **original consideration-time drafts**, retained to make corrections and rejected alternatives auditable. Acting wording lives only at the named adopted surfaces; these drafts are not a second operating contract. They deliberately avoid copying the unlicensed source, introducing numeric thresholds, or asserting operational guarantees.

- **AE5-P1 — README Directory Map:** “External-source survey catalogue: [current reference status](external-adoption-case-studies-2026-06-20.md). Source checks and open limits are reference evidence, not operating authority.” At the proposed README seat, the link is `plans/external-adoption-case-studies-2026-06-20.md`.
- **AE5-P2 — companion example:** “For a document-parser API, specify alternative internal results `Parsed(document)` and `Rejected(reason)` rather than independent success/error flags. State which field combinations the chosen representation excludes, and validate unknown external payloads before constructing a result. Boundary rejection remains a runtime check; it is not proof that arbitrary JSON is statically impossible. A copy-only edit needs no new domain model.”
- **AE5-P3 — test-designer §7:** “For the minimal test set, name selected cases, omitted scope and a plausible false positive the selected checks must reject; omitted scope remains unverified.” Keep its bilingual prompt convention on any later landing.
- **AE5-P4 — existing recipe note:** “When simplifying an existing topology while preserving behavior, compare the same acceptance cases and inspect per-task outcomes, not only an aggregate. Retain a boundary whose relevant context-isolation or independent-work property is lost by the replacement. Use the smallest existing runnable checks; unrun comparisons remain unverified, and changing an acceptance criterion remains a separate owner decision.” This is comparison discipline, not authorization to spend or a new benchmark-runner mode.
- **AE5-P5 — existing Verification item:** “Show each declared stage gate accepting a known-valid stub result and rejecting a shaped-invalid result. A required gate that cannot reject is unverified and must be repaired or escalated; do not relabel it `# gate: none (accepted)`. Explicitly accepted optional no-gate paths remain separate.”
- **AE5-P6 — ordinary-spec checklist:** “Data/state model, when relevant: identify valid alternatives, forbidden field combinations and boundary validation points; prefer a representation excluding forbidden combinations when the implementation language and task scope support it.” Validation at a later trust boundary is not prohibited.

### Disagreements / Residual Risks

- **Clause versus example:** ModellingDesign preferred a binding checklist item and rejected example-only as insufficient. DocsUsability preferred a teaching example without a rule change; FrameMinimality would omit that example. Main initially recommended the optional example first and a separately approval-dependent skill bullet. The later owner approved both bounded changes; no behavioral experiment settles the original disagreement.
- **Gate scope:** GateValidity calls the missing two-direction stage-gate check an internal contract asymmetry; the broader frame lens views generic verification as adequate. Main accepts the textual difference, not an observed runtime defect. Its original draft would downgrade a vacuous required gate to `none (accepted)`; Main rejected that, and GateValidity acknowledged the correction.
- **Observation populations:** OperationsSafety's initial “same release/window binding” would query pre-fix or empty data after a release changes. Main's counterexample led to a revised proposal using explicit comparable pre/post populations, provenance, operation definition, deduplication and appropriate denominators. That does not prove causal incident reduction; the candidate remains deferred.
- **Representation precision:** DocsUsability's initial transition-pair example called runtime-rejected pairs “unrepresentable” and confused an action with a target state. Main rejected it; the role withdrew the claim. The proposed parser-result example separates representation invariants from runtime boundary validation.
- **Navigation:** DocsUsability initially preferred a new Decision Index row; FrameMinimality rejected extra pointers. Main selected a direct link to the already-maintained catalogue, later owner-approved, without treating a curated index as an exhaustive archive. An index pointer for the subsequent adoption decision is distinct from survey-discovery backfill.
- **Aggregate verdict versus reasons:** identical terminal verdicts do not establish agreement on the drafts, their seats, severity or necessity. No public source, model vote or missing usage count grants permission to land an operating rule.

### Evidence Actually Checked

Parent checked current spec-plan Workflow/Test Plan Mode, the source spec/test prompts through an actual composer invocation, companion spec/risk examples, flow Topology Selection/Script Contract/Verification, golden-runner scorer verification, risk Rules, runtime ownership/acceptance, README Directory Map/use-case table, skill-map and the curated Decision Index. These reads support the bounded differences above, not absence across every synonym or delivery.

Executed during this consideration round: `cx overview .`, source SHA-256 calculation, one six-role task batch, and the actual `prompt_composer.py spec-writer test-designer --task …` CLI. The CLI returned both prompt bodies and the supplied task; it did not invoke an agent or demonstrate that a draft improves planning. Semantic find failed provider 403; known-file reads and literal searches were used without converting failure into absence.

Supplemental packet and complete reviewer outputs retain the role IDs, questions, objections and source identities. The original packet is session evidence, not a new governed source. The [consideration-phase delivery report](../../review/final-report.md#agent-engineering-multi-role-update-review-2026-10-30) preserves that round's checks; later correction verification is reported separately. Persistent guards follow Adoption Guard Closure, not exact paragraph pins.

The consideration-only request was completed before the subsequent owner approval below. That later approval applies only to the six selected corrections; it does not reopen deferred operational access, other holds or Standing Non-Goals.

## Owner-Approved Corrections

Date: 2026-10-30. Subsequent user instruction: “好的，幫我記錄所有想法及推理，並且開始修正”. This approves the preceding recommendation: four existing-file documentation improvements (AE5-P1–P4) and two narrow existing-skill clauses (AE5-P5–P6). It supersedes the consideration-only approval state, not the original source findings or evidence limits. AE5-P7 remains deferred; AE5-P8–P10 are not selected. No new skill, runtime, registry member, threshold, permission, installation, model campaign, commit or push follows.

Application state: the six approved corrections are applied. The following evidence-linked reasoning summaries preserve all six roles, their strongest objections, rejected alternatives and final scope. Questions consolidate the review rather than quote each review verbatim. Role count remains neither recurrence evidence nor independent efficacy evidence.

### ModellingDesign — Representation Is a Design Decision, Not a Validation Slogan

- **Claim / checked evidence:** the ordinary-spec Workflow checklist lists inputs, outputs, edge cases and failures but no explicit data/state-model decision. The source spec template's conditional Data / Schema field and the existing workflow-design state section do not make that ordinary checklist item explicit.
- **Socratic questions:** Can a plan satisfy every current heading while leaving contradictory success/error flags? Which combinations does the proposed representation actually exclude? Does an unrelated copy edit need a new model?
- **Strongest counterargument:** the invalid-field example is constructed, not a reproduced local incident; a universal modelling mandate or prescribed type system adds ceremony, and validation can legitimately recur at different trust boundaries.
- **Decision:** adopt AE5-P6 as one conditional checklist item, and AE5-P2 as one optional concrete illustration. Do not add a new method/skill, ban repeated boundary validation or call arbitrary JSON statically impossible. The example alone is not coverage in a standalone skill; the clause is therefore self-contained.
- **Verification / falsifier:** check valid result alternatives and reject mixed/missing payload cases at the declared boundary; contrast a copy-only task. A runtime-checked state is not unrepresentable. Actual planning improvement remains unknown without a controlled comparison; amend or remove the item if it imposes unrelated modelling work.

### GateValidity — A Gate Must Distinguish Acceptance From Rejection

- **Claim / checked evidence:** flow Verification explicitly covers selected preflight, retry refusal and empty command configuration, but does not explicitly require both-direction inputs for each declared stage gate. Spec-plan's Test Plan Mode already names gaps and false-positive guards; the standalone test-designer §7 does not.
- **Socratic questions:** Would an always-successful gate pass the hand-off checklist? Which plausible wrong result must be rejected? Can a failed required check be renamed an accepted absent check?
- **Strongest counterargument:** generic verification already describes meaningful checks, and no shipped-template runtime failure was reproduced. A new paragraph must not weaken required acceptance or duplicate Test Plan Mode across skills.
- **Decision:** adopt AE5-P5 by extending the existing Verification item and AE5-P3 by clarifying the standalone minimal-set question. Reject the original required-gate-to-`none (accepted)` downgrade. Explicitly accepted optional no-gate paths remain separate; an unverified required gate needs repair or escalation.
- **Verification / falsifier:** execute valid and shaped-invalid stub cases on extracted templates with zero model calls, retain existing preflight/retry/quorum checks, and exercise actual standalone prompt composition. These prove exercised control paths and delivered content, not arbitrary gate semantics or prompt efficacy.

### TopologyArchitecture — Simplify Boundaries Only While Preserving Their Work

- **Claim / checked evidence:** existing Topology Selection chooses an initial fit. The nearby Looper Topologies recipe lacks a bounded comparison criterion for changing an already-working decomposition.
- **Socratic questions:** Are both designs solving the same acceptance cases? Could an unchanged aggregate conceal a task-specific regression? Is a context-isolation or independent-work boundary load-bearing?
- **Strongest counterargument:** minimality and the Safety Floor already protect behavior; another operating rule or paid benchmarking requirement would be disproportionate, and fewer agents is not inherently better.
- **Decision:** adopt AE5-P4 once in the existing recipe, not also in the flow skill. Preserve same-case/per-task comparison, proportional runnable checks and a reason to retain a useful boundary. Do not widen the skill-only golden runner, mandate one topology or authorize an experiment.
- **Verification / falsifier:** check the recipe's actual composed output and linked contracts. No topology migration or comparative agent run occurs here; utility, latency and cost effects remain unknown until separately measured.

### OperationsSafety — Comparable Evidence Is Not Permission or Causation

- **Claim / checked evidence:** risk Rules and the product/runtime ownership boundary already separate observations, authorization, accepted effects and postconditions. A worked observation-population example could improve teaching.
- **Socratic questions:** After a fix changes release and time window, would the old filters select pre-fix or empty data? Are operation definitions and denominators comparable? Who authorized the action and who accepts its outcome?
- **Strongest counterargument:** identical-release/window binding breaks post-fix confirmation. Even comparable observations do not prove causal incident reduction or enforce access controls.
- **Decision:** retain AE5-P7 as deferred; preserve the corrected idea of explicit comparable pre/post populations, provenance, operation definition, deduplication and denominators, without landing another safety clause. The user approved the preceding six selected corrections, not private production access.
- **Verification / reopening:** a concrete diagnostic-reader ambiguity or separately scoped request may reopen this example. No customer, production, deployment or observation system is accessed; operational effectiveness remains unknown.

### DocsUsability — Teach One Decision and Link Existing Navigation

- **Claim / checked evidence:** spec-plan examples mainly expose headings and ticket fields; the library README's plans line points to a curated Decision Index, while the maintained catalogue already exposes the current survey and its limits.
- **Socratic questions:** Can a reader make a representation choice from headings alone? Can a new reader reach the survey without conversation memory? Is another curated history entry smaller than linking the catalogue?
- **Strongest counterargument:** illustrative content is not binding runtime behavior, another pointer can be redundant, and the initial transition example incorrectly called runtime-rejected pairs unrepresentable.
- **Decision:** adopt AE5-P2's corrected parser-result illustration and AE5-P1's catalogue link, including paired zh-TW navigation. Reject the transition/action confusion and a Decision Index backfill solely for survey discovery (AE5-P9). The later adoption decision may have its own index pointer; it does not make the index an exhaustive survey catalogue.
- **Verification / falsifier:** exercise README → catalogue → current record, actual composer/list entry points, and changed example metadata. No reader study or demonstrated usability gain is claimed; remove redundant navigation if it ceases to resolve a useful reader decision.

### FrameMinimality — Bound the Whole Batch, Not Only Each Addition

- **Claim / checked evidence:** the prior no-new-skill ruling holds; six locally plausible additions can still create redundant policy. Missing usage data stays `unknown`, not evidence of no demand.
- **Socratic questions:** Which surface is current? What would falsify the update-seeking frame? Does a simpler explanation close the decision without importing another rule or runtime?
- **Strongest counterargument:** existing generic clauses may already suffice; this role preferred at most the optional topology note and opposed the example/navigation additions.
- **Decision:** preserve that dissent rather than claim unanimous support for six edits. Owner approval selects four existing-file docs improvements and two bounded clauses, each stated once at its acting surface. Reject AE5-P8/P10's new skill/runtime/tool/threshold, universal single-agent policy and duplicate implement/review rules; do not add permanent paragraph-pinning tests.
- **Verification / retirement:** use existing structural, registry and executable consumers plus a disposable changed-surface smoke, following [Adoption Guard Closure](../GLOSSARY.md#adoption-guard-closure). No controlled prompt-utility or maintenance-cost comparison exists. Later evidence of redundancy or a superseding contract can retire an addition without erasing this decision trail.

### Landing and Verification Contract

The Candidate Adoption Ledger is the current status map; the original drafts and disagreements remain historical review evidence. Land only the six approved changes, preserving accepted optional no-gate paths, required-gate failure exits, trust boundaries and the nine-core/registered-pack sets. Refresh generated discovery after the final indexed-document edits. Exercise the actual composer and a disposable standalone package copy; run existing executable template consumers and the full repository gate. Record observed results and any failures in the delivery report, not as claims of model utility, runtime enforcement or production readiness.
