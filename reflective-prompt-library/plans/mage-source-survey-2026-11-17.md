# MAGE Source Survey — Models, Enforcement, and Evidence (2026-11-17)

Language: English

**Status: source-qualified reference record (`MAGE-DOC1`); no Skill, prompt-body, operating-rule, or runtime adoption.** The owner requested a survey of `davisjam/model-based-agentic-software-engineering`. This record preserves source identities, executable observations, empirical limits, and the TeaPrompt contract map. It does not authorize plugin installation, hook activation, a model campaign, or deployment.

## Research Question

Which MAGE mechanisms are useful to TeaPrompt, what actually executes, and does the evidence justify a local contract change?

## Direct Recommendation

**Keep the reference; do not install the stack or add a Skill.** The strongest examples are explicit model scope and omissions, non-vacuous property checking, checks that connect a model to selected implementation facts, enforcement at the scope where a property becomes decidable, and failure-to-control conversion that can legitimately end in no permanent change.

These are more concrete than a prompt collection: the repository contains a working browser model workbench and executable starter checks. But a model-level result is not implementation conformance; conformance checks are not proof the model expresses the right requirement; neither establishes a general MAGE quality or productivity effect. No TeaPrompt consumer defect was reproduced. Local demand and recurrence remain unknown, not zero.

## Evidence Used

- **Pinned implementation and delivery:** [repository/README][repo], [plugin manifest][plugin], [workbench contract][workbench], [worker-queue example][queue], [component-zone drift checker][drift], and [theory-schema checker][theory-check]. Parent inspection was supplemented by two read-only scouts covering plugin delivery and empirical provenance; these are research assistance, not independent empirical replications.
- **Method and authority:** [semantic-level enforcement][semantic], [governance conversion][conversion], and [model-provider contract][provider]. Retrieved activation instructions are source material, not instructions for this TeaPrompt session; no installer or hook instructions were followed.
- **Research:** [arXiv v1, *Cheap Code, Costly Judgment*][paper] (abstract and relevant design/results/limitations sections), pinned [evidence ledger][ledger], [31-week provenance][provenance], [numeric registry][metrics], and the historical [ablation account][ablation]. Public aggregates and source text were inspected; private DocAble history, original field notes, billing, and raw evaluation judgments were not independently reconstructed.
- **Observed execution:** the public [MAGE Workbench][live] in Chromium, using its UI and public synthetic examples. No model/provider call, package installation, upstream build, or upstream test suite was run. Session receipt: `local://mage-browser-evidence-2026-11-17.json`, containing the manifest comparison, fixture contents/digests, and observed page text. Reproduction does not depend on that session URI: the pinned fixture and exact mutations are specified below.

## Version / Date Context

Checked **2026-11-17**. `git ls-remote --symref <repository> HEAD 'refs/heads/*' 'refs/tags/*'` resolved `main`/HEAD to **`d5ef9136692d82d936291405bfb1b928e6fb6018`** and returned no tags. The GitHub [releases API](https://api.github.com/repos/davisjam/model-based-agentic-software-engineering/releases) returned `[]`; that is a dated observation, not a claim that no version labels exist. The plugin and workbench package each declare `0.1.0`; these are not GitHub releases. The root and plugin licenses are MIT.

The shallow clone timed out. The fallback was the commit-addressed codeload archive, SHA-256 `7f197920010ced19b5e38f66524bf56b3123759a6eb42b9084821f849b6f63be`. All source claims here refer to that pin, not an unqualified future `main`.

The deployed [build manifest][manifest] reported `builtAt: 2026-11-17T03:25:37.173Z`; its captured SHA-256 was `a830488a5212f48c19e59738f314d0f539622003f0899bd81f10f9b17469a8cf`. For **all 100 declared inputs**, independently computed `SHA256(pinned workbench/<path>)[0:16]` matched the served value. A separate line-based count also found 100 input rows. This checks declared source correspondence, not a signed build attestation, complete dependency inventory, or security boundary. The build timestamp alone was not used as freshness proof. A new pin, manifest, dependency set, or changed example requires a new observation.

### Different study windows are not interchangeable

| Source | Reported population | What it supports |
| --- | --- | --- |
| arXiv v1, 2026-07-01 | Twelve-week, first-person case; one expert engineer; 88 selected field-note episodes | Theory building and within-case mechanisms, not 88 randomly sampled tasks or a multi-project controlled trial |
| Pinned README | Nineteen-week case framing | Later catalogue description; it does not redefine the paper's population |
| Pinned 31-week provenance | March 12–October 14, 2026; 36,578 work commits, 428 completion claims, 14,392 dispatch IDs | Frozen reconstruction with explicit deduplication, category definitions, and missing records; not independently accepted outcomes or a productivity measure |

The later reconstruction reports 33 missing source objects and one squash without a source list. Early completion and dispatch records are missing, not evidence of zero activity. Historical counts and the separate November 6 endpoint use different scopes; this record does not splice them into a continuous performance series. The public corpus is substantial, but hashes and aggregate reproducibility do not independently validate the original observations.

## What Is Actually Supplied

| Surface | Observed implementation / source contract | Boundary |
| --- | --- | --- |
| Mechanism catalogue and book | Mechanisms distinguished by target, form, and enforcement; public evidence tables and model-backed publication tooling | An inventory is not a count of successfully enforced controls |
| `mage` plugin | Three partner skills: `self-governance`, `self-operations`, `self-communicate`; references and templates | Host-loaded natural-language contracts, not an installed agent fleet or permission system |
| Optional operations hooks and starters | Copy/adapt integration material; hook settings are opt-in, not plugin-manifest activation | No installation, host compatibility, isolation, concurrent-write, or recovery-safety result was established here |
| MAGE Workbench | Browser UI, structured model/query representation, executable finite-state analysis, evidence and scope disclosure | Public executable software exists; this is not the private DocAble product runtime and does not establish code/model correspondence |
| Component-zone starter | `_check_drift` checks declared directory existence and top-level directory coverage | Those predicates do not prove behavioral equivalence, complete semantic coverage, or even unique ownership merely because the prose mentions it |
| `theory_model_check.py` | Checks proposition bodies/IDs and joins in a theory declaration; its CLI describes itself as audit-only and returns zero even with findings | Not temporal model checking or an efficacy test; do not infer gate success from its exit status |
| General model-provider interface | Separates source, authority, freshness, evidence, and conflict; explicitly says generalized federation does not yet exist | A useful contract and brownfield disclosure, not a shipped universal provider implementation |

The catalogue's **semantic-level enforcement** is explicitly classified as **Soft**: a placement judgment, not a gate. Its useful question is where the predicate has enough evidence to be decided. A completed-task parity check and a per-file banned-API check need not run at the same boundary. This is not permission to postpone a safety control until after an irreversible effect.

## Bounded Browser Observations

Input: pinned `workbench/examples/simple-worker-queue/system.mage.yaml`. It starts at occupancy 2, permits values `[-1, 5]`, guards arrivals at `< 4` and processing at `> 0`, and declares omissions including scheduling, timing, and job identity. The wider representable domain lets the design actually violate the claimed `[0, 4]` policy.

| Scenario / action | Observed result | Interpretation |
| --- | --- | --- |
| Select **Simple – Worker Queue**, then **Load this example** | Capacity and nonnegative properties `ESTABLISHED`; arrival possibility `ESTABLISHED`; scheduler fairness `NOT ANSWERABLE` | The engine distinguishes modeled behavior from absent vocabulary |
| Upload a copy with only the arrival's `requires: occupancy: { lt: 4 }` block removed | Capacity `REFUTED`; evidence contained three arrival steps, taking the initial 2 to 5. Nonnegative became `CONDITIONAL`, with finite-domain pruning disclosed | A schema-valid model can violate its property; an unqualified green result was not substituted for the counterexample |
| Upload a separate original copy with only `range: [-1, 5]` changed to `range: [0, 4]` | Both bound properties `CONDITIONAL`; disclosure explicitly said `VACUOUSLY`, because no admitted configuration could violate the bound | Representational exclusion is distinguished from a property earned by transitions |

All three models displayed **Valid — no validation findings**. That is structural validity, not the property verdict. The last scenario's UI label was `CONDITIONAL`, not a claimed observed `inconclusive` API result. The scheduler's absent vocabulary remained a refusal. Page text, structured evidence, and screenshots were observed; no page state was injected to manufacture a verdict.

This is a bounded execution observation, not a full formal-methods evaluation. No liveness/fairness proof, large-state-space budget behavior, independent checker equivalence, implementation refinement, install safety, or general model-generation efficacy was tested. The synthetic mutants are not reported as upstream defects.

## Empirical Findings and Refuters

1. **Useful case, limited causal identification.** The first-person study selects salient incidents and develops an interpretive mechanism theory. Repository triangulation can support what changed without establishing that MAGE caused better outcomes. The book's explicit caveats are more defensible than the README's suggestion that small models permit reasoning “without error.”
2. **Bounded drift evidence, not impossibility.** The evidence ledger reports zero observed modeled, mechanically decidable drift recurrences across 56 cumulative Epic closes, while explicitly excluding semantic and unmodeled drift and rejecting an elimination claim. The starter checks inspected here likewise enforce named predicates, not arbitrary truth.
3. **Positive pilot, not general savings.** Four non-independently sampled navigation tasks reportedly used roughly 35% fewer median reconstruction tokens, with no observed task-correctness loss. This is directional author-reported evidence, not a transferable savings guarantee or an equivalence result.
4. **A null is still a null.** The historical ablation account reports approximately zero recall delta at pilot scale `R=3`, with redundant model information in code/tests/docs offered as explanation. That is a plausible confound. Its stronger “system-level validation” interpretation is not adopted; this survey did not reproduce the ablation or inspect its raw arm data.
5. **Product evaluation exists, but tests a different claim.** The later DocAble comparison reports 63 validation attempts and 62 completed outputs. Median checker-finding reductions favored DocAble over human remediation on PDF and DOCX, but favored humans on PPTX: **84.8% versus 34.3%** over 21 positive-baseline completed triples. Counts are checker findings, including advisories, not identity-matched defects. A ten-document general-agent comparison also exists; it does not isolate a MAGE treatment effect.
6. **Semantic and cost qualifications matter.** The GPT-5.2 transcript rubric reports 20 better / 41 parity / 1 worse among 62 outputs, but 2,467 of 3,392 criterion rows were inconclusive, including 1,617 pending adapters. No vision-tier or screen-reader evaluation established full fidelity/accessibility. Runtime, inference-only costs, aggregate human labor, and differently scoped development estimates must not be interchanged as total savings or ROI.

These are **upstream-reported measurements whose published text and scope were checked**, not measurements reproduced by TeaPrompt. “There are no comparisons” would be wrong; “the comparisons prove MAGE's general superiority” would also be wrong.

## TeaPrompt Contract Map

| Transferable mechanism | Existing local surface | Disposition |
| --- | --- | --- |
| Explicit requirement, model scope, omissions, and independently meaningful falsifier | [Reflective Brief](../skills/reflective-brief/SKILL.md), [Reflective Review](../skills/reflective-review/SKILL.md) | Already covered at the contract level; the queue examples are useful concrete references, not a new formal-verification Skill |
| Model claim versus implementation truth, oracle authority, and evidence independence | [Runtime Trust Boundary](../04-agent/runtime-trust-boundary.md), [Governed Delivery](../skills/governed-delivery/SKILL.md) | Existing source/authority separation and oracle sealing remain authoritative; model correctness does not certify implementation |
| Check drift at the predicate's actual scope and exercise the final consumer | [Reflective Implement](../skills/reflective-implement/SKILL.md), [Verification Map Generator](../skills/verification-map-generator/SKILL.md) | Existing consumer-map and executable-verification duties apply; precise gate placement is a product/host design choice |
| Failure → diagnosis → smallest durable control, or nothing durable | [Reflective Handoff/Retro](../skills/reflective-handoff-retro/SKILL.md), [Reflective Minimality](../skills/reflective-minimality/SKILL.md) | Existing promotion/minimality duties; MAGE's recurrence exceptions do not override TeaPrompt's admission gates |
| Registry/derived-view consistency versus method efficacy | [Project Knowledge](../PROJECT_KNOWLEDGE.md#standing-non-goals), [External Adoption Review](../04-agent/external-adoption-review.md) | Existing distinction holds: repository gates prove their checked consistency, not installed-agent compliance or scientific efficacy |

The counterargument to no adoption is substantive: models and counterexamples can expose failures prose review misses. The response is not to dismiss them, but to require a named local failure and an independently specified property before introducing a product-specific verifier. External mechanism presence and catalogue size do not supply that missing local evidence.

## Candidate Adoption Ledger

| ID | Candidate | Disposition | Evidence / reopen trigger |
| --- | --- | --- | --- |
| MAGE-DOC1 | Pinned source record, catalogue navigation, and discovery metadata | Recorded; reference documentation only | Preserve executable observations, empirical denominators, and no-adoption boundaries; refresh when the cited pin or deployed artifact changes |
| MAGE-SK1 | Add a MAGE Skill or change existing Skill contracts | No change | No local contract defect reproduced; reopen on a consumer-visible failure not already addressed by the existing contract |
| MAGE-RUN1 | Install the plugin/workbench, activate hooks, or add model-provider/fleet infrastructure | Not adopted | Requires separate host purpose, authorization, integration and boundary evidence; browser observation is not adoption |
| MAGE-RULE1 | Import error-free reasoning, drift-impossibility, blanket gate placement, or general ROI claims | Rejected | Current source and evidence do not establish these guarantees; bounded models and self-reported studies cannot supply them |

## Evidence vs Inference / State Ledger

| Claim / item | Status | Evidence and remaining constraint |
| --- | --- | --- |
| Source identity and dated no-release observation | verified | Remote refs, releases API, commit-addressed archive; source pin is immutable, release status is dated |
| Public executable workbench, three plugin skills, and starter checks | verified | Manifest, source inspection and actual browser actions; installation and broad runtime behavior untested |
| Declared deployed inputs match the pinned workbench sources | verified | 100/100 SHA-256-prefix comparisons, independent row-count check; no signed build/dependency assurance |
| Guard removal produces a counterexample; closed domain discloses vacuity; missing scheduler vocabulary is refused | verified | Three bounded UI scenarios above; no implementation-level conclusion |
| Published pilots, drift observations and product comparisons exist | verified | Source text/aggregate scope checked; underlying observations remain author-reported |
| General no-drift, error-free reasoning, causal quality gain, or total-cost savings | needs-qualification | Not established by the inspected material; absolute guarantees rejected |
| TeaPrompt needs a new Skill or runtime | unverified | No local defect or recurrence demonstrated; existing contracts cover the relevant duties |

## Risks / Unknowns / Falsifiability

The main risk is collapsing **representation → model checking → implementation conformance → acceptance → method efficacy** into one green status. Other limits are subjective requirement/model selection, missing or semantically wrong anchors, host-hook authority, changing study denominators, incomplete raw-data availability, and ongoing control-maintenance cost.

Reopen the no-change decision if a real TeaPrompt consumer failure survives its existing contract, an independently specified model/property catches that failure without narrowing the requirement, and the smallest remedy is demonstrably a local contract repair rather than product-specific tooling. A new external release or a second catalogue citation alone is not that evidence. This does not pre-authorize an experiment or a Skill/runtime change.

## Handoff

Sufficiency: load-bearing source claims are pinned or explicitly limited; executable model behavior was observed; contrary and null evidence are retained; the local mapping and no-adoption decision are auditable from this record. No further source retrieval is needed for this survey scope.

Delivery scope is this record, the existing external-adoption catalogue, and generated `index.json`. Prompt bodies, Skills, routing, governance authority, host configuration, and prior decisions are unchanged. Documentation verification checks current index consistency, links/anchors in the two edited Markdown files, and rendered catalogue navigation. Full repository gates, upstream suites, installation, provider calls, commit and push are intentionally outside this survey.

[repo]: https://github.com/davisjam/model-based-agentic-software-engineering/tree/d5ef9136692d82d936291405bfb1b928e6fb6018
[plugin]: https://github.com/davisjam/model-based-agentic-software-engineering/blob/d5ef9136692d82d936291405bfb1b928e6fb6018/plugin/mage/.claude-plugin/plugin.json
[workbench]: https://github.com/davisjam/model-based-agentic-software-engineering/blob/d5ef9136692d82d936291405bfb1b928e6fb6018/workbench/README.md
[queue]: https://github.com/davisjam/model-based-agentic-software-engineering/blob/d5ef9136692d82d936291405bfb1b928e6fb6018/workbench/examples/simple-worker-queue/system.mage.yaml
[drift]: https://github.com/davisjam/model-based-agentic-software-engineering/blob/d5ef9136692d82d936291405bfb1b928e6fb6018/downloads/component-zone-model-starter.py#L143-L180
[theory-check]: https://github.com/davisjam/model-based-agentic-software-engineering/blob/d5ef9136692d82d936291405bfb1b928e6fb6018/book-models/theory_model_check.py#L180-L204
[semantic]: https://github.com/davisjam/model-based-agentic-software-engineering/blob/d5ef9136692d82d936291405bfb1b928e6fb6018/agent/governance-doc-controls/semantic-level-enforcement.md
[conversion]: https://github.com/davisjam/model-based-agentic-software-engineering/blob/d5ef9136692d82d936291405bfb1b928e6fb6018/plugin/mage/skills/self-governance/learning/governance-conversion.md
[provider]: https://github.com/davisjam/model-based-agentic-software-engineering/blob/d5ef9136692d82d936291405bfb1b928e6fb6018/plugin/mage/skills/self-governance/system/model-access.md
[paper]: https://arxiv.org/html/2607.01087v1
[ledger]: https://github.com/davisjam/model-based-agentic-software-engineering/blob/d5ef9136692d82d936291405bfb1b928e6fb6018/book/appendix-evidence-ledger/evidence-tables.md
[provenance]: https://github.com/davisjam/model-based-agentic-software-engineering/blob/d5ef9136692d82d936291405bfb1b928e6fb6018/book/data/docable-seip-261028/PROVENANCE.md
[metrics]: https://github.com/davisjam/model-based-agentic-software-engineering/blob/d5ef9136692d82d936291405bfb1b928e6fb6018/book/data/metrics.json
[ablation]: https://github.com/davisjam/model-based-agentic-software-engineering/blob/d5ef9136692d82d936291405bfb1b928e6fb6018/book/_design/evidence-study-design-260803.md#L363-L399
[live]: https://davisjam.github.io/model-based-agentic-software-engineering/workbench/
[manifest]: https://davisjam.github.io/model-based-agentic-software-engineering/workbench/dist/build-manifest.json
