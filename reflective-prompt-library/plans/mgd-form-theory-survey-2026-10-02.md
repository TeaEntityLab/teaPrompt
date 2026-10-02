# Misfit-Governed Development Form-Theory Survey (2026-10-02)

> **Status: decided — research-reference-only; no skill, runtime, schema, routing or oracle adoption.**
> The paper supplies a useful account of bounded harness assurance, not evidence for a new MGD workflow.
> Positive local contract matches are recorded below; predicate-level coverage is an adjacent audit target,
> not a verified TeaPrompt defect. This decision archive does not prescribe agent operating rules.

## Research Question and Authority

Initial request: "Survey https://arxiv.org/abs/2610.01372"; sources checked 2026-10-02. Subsequent direction:
"Review Update and Commit Push". The initial research-only delivery made no repository changes;
this follow-through publishes its evidence and discovery pointers, alongside the separately reviewed
recent-survey source repairs. Publication authorization does not change adoption decisions or grant
permission to amend governing oracles, install a runner, or lift the runtime non-goal.

What does Misfit-Governed Development (MGD) actually establish, how strong is its empirical evidence,
and which mechanisms differ from TeaPrompt's existing loop, governance and verification contracts?

## Direct Recommendation

- **Study:** yes. The distinction between an open misfit enumeration, incomplete execution of that
  enumeration, and a wrong specification is useful for interpreting a green run.
- **Documentation:** publish this reference and links from the existing factory recipe, Decision Index
  and external case-study index; do not turn the paper's prescriptions into new local operating rules.
- **Skills/runtime:** no change. Existing inner/outer-loop, oracle-owner, consumer-chain and four-way
  failure-classification contracts have positive matches. No new SDLC entry point, MGD pack, compulsory
  four-form expansion or duplicate source of authority is warranted by the checked evidence.
- **Replication/deployment:** not performed. The reference application and its governing artifacts are
  not released in the paper's Availability statement. The synthetic counterexamples below are not
  execution of that implementation, PIT, or a product-bound host audit.

## Source Identity, Version and Access

| Item | Checked source / scope |
| --- | --- |
| Paper | [A Design Theory for AI-Assisted Software Development Derived from Christopher Alexander's Theory of Form](https://arxiv.org/abs/2610.01372v1); checked 2026-10-02 |
| Authors | Chien-Tsun Chen and Yu Chin Cheng; arXiv `cs.SE` metadata, not a peer-review claim |
| Version | `2610.01372v1`, published and updated 2026-10-01T09:41:50Z; checked 2026-10-02 |
| Metadata | [Official arXiv Atom API](https://export.arxiv.org/api/query?id_list=2610.01372), read raw; checked 2026-10-02 |
| Full text | [Versioned PDF](https://arxiv.org/pdf/2610.01372v1), converted text read completely: §§1–9, Tables 1–5, Appendix A, Availability and AI Use Statement; 928 extracted lines |
| Retrieval limit | Unversioned HTML returned HTTP 404; the pinned PDF supplied full text, not merely the abstract |
| Availability | Supporting libraries described as public; reference application, problem-frame specifications, gates, rule catalog and doctrine/pattern corpus not publicly released in v1 |
| Provenance | Authors retain responsibility for claims; AI Use Statement says Claude generated implementation and some specifications/gates/patterns, and wrote telemetry/corpus-count scripts under their direction |
| Competing interests | Chen declares founding Teddysoft, which offers relevant training/consulting and publishes the supporting libraries; Cheng declares none. This is source disclosure, not a causal explanation of the results. |
| Freshness trigger | New paper version, released application/governing artifacts or a product-bound local failure; public-artifact inventory outside the paper was not exhaustively audited |

## Mechanisms and Claim Boundaries

The paper derives obligations from Alexander's account of form/context fit, with Jackson's problem
frames supplying problem classification. Table 1 claims a unified derivation, **not exclusivity** or
exhaustiveness; its concrete machinery is one binding, not a required universal architecture (§2.5).

| Mechanism | Published meaning | Boundary |
| --- | --- | --- |
| Negative fit | Absence of enumerated, mechanized misfits under a fixed governing representation | No claim about unenumerated requirements or unevaluated predicates; Appendix A.1 |
| Law vs harness | Law fixes norms; deterministic machinery detects and stops violations | Prompt guidance and generator confidence are not enforcement; §§3–4 |
| Four-form pattern | Doctrine, template, prohibition and deterministic gate, per implemented pattern node | Good/bad fixtures establish detector liveness; real invocations establish intended scan reachability. Not every gate belongs to a pattern; §3.4 |
| Fix loop | Frozen specification/framework target; failure-class batching; regression guard after each layer's repair | Optional semantic review stays advisory and outside deterministic convergence; §3.6 |
| Legislative circuit | Builder may propose but cannot authorize governing changes | Escape extends/corrects enumeration or receives an explicit exclusion ruling and named non-gate coverage; §§3.7, 4.4 |
| Primary/proxy split | Compiler/runtime truth or an authorized human ruling may ground a representation | Consistent proxies do not establish the ruling's fitness to the world; §4.2 |
| S = P = T = W | Structural conformance, scenario coverage and test execution are machine-checked families; specification/world judgment remains human | Equality signs denote agreement, not mathematical identity; S = T semantic faithfulness is least directly verified; Appendix A.2 and §8 |
| Locality and cadence | Bound propagation, detect residual regressions; machine-priced and human-priced feedback have different cadences | DDD/Clean Architecture/CQRS/event sourcing are reference mechanisms, not universal obligations; §§3.3, 4.3, 8 |

### Enumerated vs Actually Evaluated

In clean notation for Appendix A.1:

```text
G: governing specification/tradition, fixed within the repair window
M: finite set of mechanized misfit predicates
M_eval: subset successfully evaluated in this run
fit_M,G(a) iff every m in M returns 0 on artifact a

A run's clear returned verdicts establish fit only over M_eval.
The claim over M additionally requires M_eval = M.
An unresolved subject is unevaluated, not an evaluated 0.
```

Detector liveness/reachability, determinism, and governing-representation/proxy validity are
**meta-level admissibility conditions**, not extra conjuncts smuggled into the definition of fit.
Advisory/model review and non-mechanized classes stay outside M. A complete execution of M still says
nothing about omitted misfits or whether the specification serves its stakeholders.

The implementation does **not uniformly meet this execution-completeness obligation**. Its runner
counts a gate that cannot run as skipped, never passed; §8 discloses that a gate can nevertheless scan
only part of its intended subjects, or none. Several empty-scan checks were added, but uniform
predicate-level reporting of the missing set remains future engineering. The formal obligation and
current implementation evidence must not be cited as equivalent.

## Empirical Evidence — Author-Reported, Not Reproduced

Source text checked 2026-10-02; the numbers below remain author-reported.
[§5/Table 3 and §8](https://arxiv.org/pdf/2610.01372v1#page=30) describe repeated builds of **one Scrum
system**, not a controlled benchmark against another methodology.

| Quantity / observation | Reported scope and denominator |
| --- | --- |
| System / specification | Four event-sourced aggregates; 64 problem-frame specifications |
| Generated tests | About 1,300 tests, run under in-memory and full outbox/PostgreSQL infrastructure profiles |
| Blocking gates | 28 = 1 specification-quality + 1 dual-profile + 18 per-use-case structural + 7 aggregate closeout + 1 deterministic-review; advisory and model-review mechanisms excluded |
| Current rules | 188 deterministic-review catalog rules; 95 always-active prohibitions are a subset, not an additional catalog |
| Telemetry window | 5,807 recorded deterministic-review runs, 2026-03-01 through 2026-08-16; instrument added partway through the project |
| Violation reports | 216,148 repeated reports at 1,748 distinct rule-and-file sites across 235 historical rules; neither reports nor sites are a count of independent defects |
| Rule populations | 235 is the historical union, 188 the current catalog, 95 its always-active subset |
| Most recent rebuilds | All blocking gates passed and tests green under both profiles, as reported by the authors |
| PIT strength | 95–100% killed/covered mutants across four aggregates; not a denominator over all business requirements or proof of S = T faithfulness |

Published observations include dropped input fields, unreachable controller error branches, lost
reconstructed state and unwired reactions; audits also found stale counts, retired-doctrine hooks
and silently narrowed scan sets. This verifies what the **source reports**, not its private telemetry.
All observed builders came from one model family. One main legislator/domain expert supplied problem
elicitation, specifications and S = W judgments. There is no controlled causal improvement estimate,
demonstrated portability, measured human benefit or harness/spec-authoring ROI.

The blocking boundary encloses the backend. Frontend/backend HTTP-field drift remained possible while
local checks were green; a field-level cross-boundary audit is opt-in. Scheduled inhabitation review,
its institution, and non-engineer participation in formalization remain proposed, not completed (§8).

## Verification Actually Exercised

Two deterministic constructive probes ran in the retained **Bun 1.4.2** kernel during the original
survey, without files, installations or repository tests. They check the survey's interpretation,
not the authors' code. Exact inputs and results are retained in the survey ledger.

| Coverage trace | Required / evaluated predicates | Returned violations | Bounded fit established |
| --- | --- | --- | --- |
| Full clear | 2 / 2 | 0 | true |
| Partial clear | 2 / 1; controller-error reachability unevaluated | 0 | false |
| Empty scan | 2 / 0; both input-field chain and controller-error reachability unevaluated | 0 | false |
| Detected misfit | 2 / 2 | 1 | false |

Second probe: specification `eligible iff age >= 18`; generated program `age > 18`; oracle rows
`(17,false), (18,false), (19,true)`. The wrong program passes that oracle. Four explicitly selected
mutants (`>=`, `<`, always-false, always-true) all fail it: **4/4 killed under this toy operator set**.
Yet age 18 violates the specification, and correcting the program to `>=` is rejected by the wrong
oracle. This is not a PIT score: it demonstrates that perfect sensitivity to selected program mutants
can coexist with a jointly wrong program/test boundary rule.

No inference about prevalence, product regression, empirical gain or efficacy follows from these
constructive examples. Repository guards and publication-reader checks are separate delivery evidence
in `review/final-report.md`, not replication of MGD.

## Candidate Adoption Ledger and Existing TeaPrompt Mapping

Mappings below are positive **textual contract matches**, not claims that an installed host enforces
them. All `SKILL.md` surfaces remain unchanged.

| ID | Mechanism / classification | Checked existing surface | Decision / reopen condition |
| --- | --- | --- | --- |
| MGD-1 | Inner deterministic loop / human intent and acceptance: already present | [Factory recipe](../04-agent/workflow-recipes.md#autonomous-software-factory-ai-native-sdlc), [flow-loop-harness](../skills/flow-loop-harness/SKILL.md) Loop Anatomy, [governed-delivery](../skills/governed-delivery/SKILL.md) §§Scope/Oracle split | No new workflow. Reopen on a local consumer bypassing an existing stated gate. |
| MGD-2 | Separate builder from governing-oracle authority: already present | `governed-delivery` Oracle split and host seal; [reflective-implement](../skills/reflective-implement/SKILL.md) Never / failure classification | No new authority schema. Reopen on observed unauthorized governing mutation, through the existing owner protocol. |
| MGD-3 | Repair checker/oracle/docs vs conforming product: already present | `reflective-implement` failure classification; [verification-map-generator](../skills/verification-map-generator/SKILL.md) four-way failure classification | No new failure-class taxonomy. Reopen on consumer-visible misclassification under the current contract. |
| MGD-4 | Cross-boundary propagation and actual consumer proof: already present | `reflective-implement` consumer map / coverage check; `verification-map-generator` Drive and Failure paths | No new map schema. A named missed consumer boundary would justify a local assessment, not this paper alone. |
| MGD-5 | Live/reached detector plus required/evaluated predicate subjects: adjacent / local deficit unknown | Appendix A.1 and §§3.4, 8; existing loop verifier preflight and implementation coverage contract | Reference-only product-bound audit target. Reopen on a named product's expected/evaluated subject mismatch with a reproducible false-green trace and assessment authorization; complete accounting plus liveness/reachability evidence falsifies that local gap. |
| MGD-6 | Proxy/source/ruling/runtime separation: already present | [Project boundary](../PROJECT_KNOWLEDGE.md#standing-non-goals), [reflective-review](../skills/reflective-review/SKILL.md) Four Evidence Dimensions, [reflective-research](../skills/reflective-research/SKILL.md) State Ledger | No promoted principle. Reopen on a concrete local source/verdict conflation at its owning surface. |
| MGD-7 | Four-form pattern network and synchronized restatements: reference binding | Paper §§2.5, 3.3–3.4, 8; TeaPrompt's existing uniqueness/size/authority contracts | No compulsory duplication or architecture copy. Reopen only on a local failure requiring that mechanism after smaller in-place alternatives are rejected. |

MGD-5 adds evidence for evaluating bounded execution; it does not close or change
[AEAT-4's held independent acceptance-oracle join](agent-execution-assurance-taxonomy-survey-2026-09-30.md#candidate-adoption-ledger).
Unknown local usage remains unknown, not zero demand. No unrelated held candidate, promotion gate,
core registry or host boundary is reopened by this publication.

## Evidence vs Inference, Risks and Handoff

| Claim | Evidence status |
| --- | --- |
| Paper identity, formal definitions, prescriptions, numerical text and disclosed limits | Verified source text at v1; not raw-data or implementation replication |
| Existing TeaPrompt loop/oracle/classification/consumer obligations | Verified positive source matches; installed-agent compliance and host sealing unknown |
| Zero returned violations can hide incomplete evaluation; selected mutants can miss a wrong business rule | Constructive probes exercised on explicit toy inputs only |
| Strongest transferable lesson is bounded liveness/reachability/subject-accounting scrutiny | **[INFERENCE]** from source theory, its disclosed limits and the constructive probes |
| Rebuild evidence supports feasibility within this binding, not causal superiority or portability | Authors' scope disclosure; no independently reproduced performance claim |
| Local predicate-accounting defect, optimal guidance size, cost-effectiveness and S = W benefit | Unknown / not measured here |

Counterarguments retained: established verification practice already covers many obligations; the paper
claims unity rather than novelty of each mechanism. Four forms are a costly binding and the authors
warn that externalization may not pay for one-off exploration. More machinery cannot repair a wrong
oracle or supply stakeholder judgment. Do not make the formula or a large harness mandatory on that basis.

## Falsifiability

- A checked local surface lacking an obligation attributed to it would falsify that mapping; repair the
  citation/owning surface, not a supposed missing runtime inferred from the paper.
- For MGD-5, a named product's complete expected/evaluated predicate-and-subject binding, detector
  good/bad controls and real reachability evidence would refute a missing-execution claim at that scope.
  The source's incomplete implementation does not establish a local gap.
- A reproducible local false-green or a released/new-version source correcting a figure or limitation
  would reopen the corresponding row. New external examples alone do not establish local recurrence
  or authorize adoption, and a complete M cannot refute an omitted-world-requirement concern.

Evidence: `local://mgd-paper-survey-2610-01372-2026-10-02.json`; repository-publication receipt is tracked
separately. Session URI is historical provenance, not a runtime dependency or the public source link.
The retained initial "no repository change" decision applies to the original research turn; this dated
publication supersedes only that publication status. Reference-only candidate dispositions are unchanged.

**Handoff:** research and durable discovery are complete. A named-product host audit, a second binding,
released artifacts or a new paper version may reopen the relevant row; none is an unfinished authorized
implementation. Any later norm/oracle/permission cutover keeps its existing Human Review gate. No
permanent tests, skills, runtime code or installation are added by this record.
