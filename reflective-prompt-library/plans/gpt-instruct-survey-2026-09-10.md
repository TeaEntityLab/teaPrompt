# Evaluation and Release Methodology (`MDX-Tom/gpt-instruct`) — Survey and Panel Record (2026-09-10)

> **Status: decided — record-only; no installed-surface adoption.** Eight read-only lenses delivered complete reviews over hub; all eight returned `AGREE WITH CHANGES`. The object is a self-described jailbreak pack, but only its evaluation/release documentation, CI definition, and provenance metadata were studied. No prompt payload, bank, or archived tool was opened or executed. The panel's reason splits and the coordinator's subsequent primary-source corrections are preserved below. Verification state lives in the Completion Ledger.

## Research Question

User instruction: “Survey and socratic critical thinking in multi roles” over the named repository. What does its evaluation methodology actually establish, how does it compare with TeaPrompt, and does any transferable practice justify changing an installed surface?

The working frame was “disciplined evaluation with a purpose/objective mismatch”; the competing frame was “rigor-shaped documentation that lends credibility to unverifiable results.” The review tests both, not just the proposed adoptions.

## Direct Recommendation (as of 2026-09-10)

- **Study: yes.** The documentation is a useful example of method-identity bookkeeping, disclosed exceptions, and the limits of a proxy score. Study does not endorse the payload, efficacy claims, or installation instructions.
- **Reproduce: not undertaken.** No provider evaluation, payload execution, or offline re-scoring was performed. The examined sources do not supply the run records needed to reproduce their counts; obtaining or running the excluded corpus is outside this survey.
- **Adopt: no.** No skill, domain pack, glossary entry, or agent-method document changes. Four candidates remain record-only, with E-5's smallest possible amendment deferred. Their triggers reopen review, not automatic adoption.
- **Deploy: no.** This task authorizes a survey, not installing instructions into a host configuration. The documented account-risk warning and untested configuration effects remain material.
- The resemblance is **convergence in documented practices, not consensus, efficacy evidence, or proof of independent origin**. No surveyed vocabulary, release threshold, or fixed resource cap is promoted into installed surfaces.

## Method

The coordinator fetched the landing page, three methodology documents, the CI workflow, and commit metadata, then embedded the in-scope text and a local concept map in one repo-readable packet. Eight specialist tasks ran concurrently against that packet, without edits or project-wide validation. Full reviews arrived by hub even though the minimality worker's final yield failed; four full messages were re-delivered unchanged after conversation archival truncated their previews. There was no new vote or replacement of an unfavorable verdict.

After the panel, the coordinator read the exact-commit versions of the three documents and CI workflow, plus `.gitignore`, `LICENSE`, and commit metadata (S1–S7 below). These reads narrowed several shared claims, including the central title/objective claim. Those corrections are coordinator findings, not retroactively unanimous panel verdicts. No provider-model identity is inferred from role names; these reviews are advisory perspectives, not eight independent measurements.

**Scope / acceptance:** map all thirteen concepts; preserve all eight reviews' reasons and the four candidate dispositions; distinguish checked source text from unverified outcomes; add the record guard and two existing index entries; keep all thirteen installed skill contracts unchanged; run `make all` from the repository root. No runtime, payload research, new skill, or external deployment is part of this work.

## What the Artifact Is

Three distinguishable surfaces are described: a behavior-changing instruction payload; an evaluation/release method with a runner, scorer, and observer; and a configuration installer with rollback support. This is more than the static instruction profile surveyed earlier, but the runner, scorer, observer, and installer behavior were **not validated here**. “Documented harness” is the warranted description, not “verified harness.”

Relative to TeaPrompt, the closest overlap is verification and acceptance, not the entire intent-to-retro delivery sequence. The README names an upstream jailbreak project; the checked material documents no shared TeaPrompt source lineage. That is not proof that the practices arose independently.

## Panel Consensus

**Decision tally:** 8/8 complete reviews; 0 `AGREE`, 8 `AGREE WITH CHANGES`, 0 `DISAGREE`. All eight opposed immediate installed-surface adoption. Their reasons were not identical.

`Record-only` and `Defer` below preserve the reviewers' terms rather than manufacturing a unanimous candidate verdict. No cell means adopt now.

| Lens | Verdict | E-2 | E-5 | E-11 | E-12 |
| --- | --- | --- | --- | --- | --- |
| GIEvidence | AGREE WITH CHANGES | Record-only | Record-only | Record-only; closest candidate | Record-only |
| GIMethodology | AGREE WITH CHANGES | Record-only | Defer; invariant clause | Record-only | Record-only |
| GIRedTeam | AGREE WITH CHANGES | Reject | Record-only; field draft | Record-only | Record-only |
| GIProvenance | AGREE WITH CHANGES | Record-only | Record-only; field plus invariant | Record-only | Record-only |
| GIUsability | AGREE WITH CHANGES | Defer | Defer; field plus invariant | Record-only | Record-only |
| GIMinimality | AGREE WITH CHANGES | Record-only | Defer; invariant clause | Record-only | Record-only |
| GIMeasurement | AGREE WITH CHANGES | Record-only | Record-only | Record-only | Record-only |
| GIStrategy | AGREE WITH CHANGES | Record-only | Record-only; deferred wording | Record-only | Record-only |

**Frame-test result:** the documents disclose the unmet B threshold, unrun C tier, historical aggregates, and a regression in artifact gates despite a higher case score. That supports disciplined reporting *as text*. The excluded run data and CI scope prevent validating the measurements. Disclosure neither proves honest execution nor establishes deceptive intent; the packet's assertion that a credibility-seeking author would have “no reason” to disclose failures is not a discriminating test of motive.

## Shared Findings

1. **A score is not its purpose statement.** S1 declares an AI-safety-research purpose. S3 explicitly defines the current objective as unrestricted/non-refusal regression and marks refusal, fallback, and missing completion fields as failures. That does not directly measure safety, correctness, or harm prevention. Attack-success measurement can be part of legitimate safety research; the scoring direction alone neither disproves that purpose nor establishes that this project achieves it. The missing link is evidence connecting the proxy to the claimed safety benefit.
2. **The title claim needed correction.** `safety-eval` occurs in S3's filename, not its displayed heading, which is “gpt-5.6-sol Prompt Bank Evaluation.” The scope change is disclosed in the first paragraph. An unchanged filename beside an explicit new objective is a source-interpretation caution, not proof of a covert objective inversion. The earlier heading and its revision history were not inspected.
3. **Release decision and passing a gate are different states.** S1/S2 report formal v1 promoted at **52/66 cases, 60/74 turns, 15/16 artifact gates**, below the B requirement; C remains unrun and v45 remains the stable default. These are author-claimed outcomes. The text discloses the exception rather than claiming the gate passed. B still gates C even though it did not prevent naming a formal release: “hard” needs a named transition, not an all-or-nothing verdict about the whole release process.
4. **Reproducibility stops at the evidence boundary.** S5 ignores `reports/`, `tests/`, and plaintext evaluation scripts; S4 explicitly excludes prompt capability and scorer/bank verification from its CI verdict. Published hashes identify claimed input bytes; they do not validate outcomes, authorship, or efficacy. No archive digest was recomputed here.
5. **Generic scorer code is not a neutral measurement.** S3 places completion markers in the bank and describes a scorer without domain-specific marker vocabulary. Separating code from criteria is useful modularity; it does not make the bank's objective neutral or establish the scorer's independence. Neither the implementation nor the relationship between `heuristic_verdict` and final `passed` was inspected.
6. **Historical results retain different meanings.** S2 segregates the old 60-case release evidence from the current 66-case comparison. It also reports a legacy **115/120 first pass plus 5/5 targeted audit**, yielding an audited aggregate not eligible under the current first-failure rule. That is an external example of the practice the current rule excludes, not a demonstrated current silent overwrite.
7. **Starting work is not completing the right work.** The continuation observer's documented action-start criterion distinguishes an edit/evaluation attempt from inspection or planning. It does not establish useful progress, correctness, authorization, or safety. No observer behavior was exercised.

## Concept Map

“Covered” means the relevant policy principle is already present, not that TeaPrompt operates the surveyed mechanism. E-1/E-2 retain separate IDs for traceability: method identity and preservation of attempt outcomes are related, but one does not mechanically imply the other.

| ID | Surveyed concept | Closest TeaPrompt surface | Disposition / boundary |
| --- | --- | --- | --- |
| E-1 | Comparable method identity; denominator provenance | `reflective-research/SKILL.md:46,103-106` — command/input set, freshness, second-method check | Covered in principle; a command label alone does not identify every hidden environment or sampling input. Retroactively marking an added unrun case failed is an administrative reassessment, not a new observation. |
| E-2 | Preserve first valid verdict; resume interrupted work without silently replacing failures | `reflective-implement/SKILL.md:147,149,168-170`; `governed-delivery/SKILL.md:177` | Record-only; existing fix/rerun and evidence rules are adjacent, not an explicit first-verdict rule. No local unchanged-rerun overwrite was found in the reviewed records. |
| E-3 | Infrastructure interruption, provider block, and model failure have different meanings | `reflective-implement/SKILL.md:149,170`; `governed-delivery/SKILL.md:34` | Covered failure-classification principle; the surveyed classifier's accuracy remains unknown. |
| E-4 | Disposable home/configuration state and isolated evaluation | `governed-delivery/SKILL.md:50,236`; `runtime-trust-boundary.md:97,112` | Host-owned mechanism; documentation is not isolation proof. |
| E-5 | Disclose a decision to close against an unmet oracle | `governed-delivery/SKILL.md:38,52,179-191,227` | Deferred representation clarification. Existing references can carry an exception; the template has no explicit surface-level naming obligation. |
| E-6 | Observable action-start, not plan/read theater | `reflective-implement/SKILL.md:141`; `flow-control-generator/SKILL.md:361` | Covered at the evidence principle; action initiation is a weaker outcome than verified completion. |
| E-7 | Scorer/verifier separation and bank-owned criteria | `governed-delivery/SKILL.md:35`; `reflective-research/SKILL.md:106`; `flow-loop-harness/SKILL.md:161` | Covered decorrelation principle; different files or generic code alone do not establish independent validation. |
| E-8 | Freeze expansion after repeated failure | `reflective-implement/SKILL.md:168-170`; `flow-loop-harness/SKILL.md:33` | Covered stop/escalation principle. The surveyed fixed retry count is not adopted. |
| E-9 | Avoid tuning a general prompt to one case phrase | `PROJECT_KNOWLEDGE.md:64-66,83-89`; artifact-promotion evidence gate | Convergent maintenance goal, not an equivalent statistical anti-overfit guarantee. |
| E-10 | Local evidence, input hashes, CI limited to project functionality | `reflective-review/SKILL.md:82-100`; `PROJECT_KNOWLEDGE.md:59` | Record-only application of installed evidence-tier rules; every external result stays author-claimed. |
| E-11 | Metric name/purpose versus the actual verdict rule | `reflective-review/SKILL.md:82-96`; `reflective-research/SKILL.md:46,105`; compression Lesson | Record-only reading check. Literal wording is absent; broader evidence checks exist. Filename/title and historical-drift claims corrected above. |
| E-12 | Outer task frames inner adversarial material as data | `runtime-trust-boundary.md:63-67,90-98`; `reflective-risk/SKILL.md:42` | Record-only threat-model note; authority order and sink permissions, not the word “research,” determine the allowed task. |
| E-13 | Snapshot, scoped reset, dry-run, explicit restore | `reflective-risk/SKILL.md:38,121-122`; `runtime-trust-boundary.md:112` | Host-owned and not exercised. Described reversibility does not authorize installing the payload or prove safe rollback. |

## Socratic Questions and Disposition

### Questions about the surveyed method

1. **What does a pass establish beyond the absence of refusal and the presence of declared output features?** The visible definition does not establish correctness or a safety benefit. Marker-only false positives and safety-caveat false negatives are plausible risks, not reproduced scorer defects. A construct-validity study would need an independently assessed criterion and access to the relevant evidence; this survey supplies neither.
2. **Can an adversarial non-refusal metric be safety research?** Yes in principle, as attack-success or robustness measurement. A high attack-success score is not itself improved safety. The documented distribution and optimization objective warrant scrutiny, but motive and benefit cannot be settled by the sign of the score.
3. **Which transition does the B “hard gate” block?** S1/S2 show it still blocks C, while a separate release decision promoted v1 below it. Disclosure is a positive reporting practice; release labels should not be read as a full A/B/C pass. No host enforcement was checked.
4. **Does first-verdict preservation solve noisy evaluation?** It prevents replacing a failed attempt with a more favorable later one. It does not estimate variance or prohibit valid, predeclared repeated-sampling protocols that preserve all attempts. The current-method documents provide no sufficient repeat/sampling protocol or uncertainty estimate for assessing small version deltas. `workers=1` specifies concurrency, not sample count; no numerical error bar is inferred here.
5. **Who can relabel a failure as an interruption or an invalid observation?** S2 allows an observer-invalid attempt to be rerun when the observer stopped on a read-only action; real refusals remain valid. That distinction requires reason-preserving classification and observer-version provenance. Its implementation and resistance to opportunistic relabeling are unknown.
6. **What would make counts independently checkable?** An authorized auditor would need the exact applicable criteria, scorer version, run records, and provenance of any manual decisions. Offline re-scoring could check a score conditional on those records without regenerating responses, but would not by itself prove they came from the claimed model run. No such audit occurred. Privacy or sensitive-content controls may bound access; they do not make all future verification logically impossible.
7. **Why archive scripts instead of keeping plaintext?** S5 explicitly attributes this to sensitive prompt/judgment samples. ZIPs are inspectable artifacts, not inherently opaque code; they do reduce direct plaintext diff/search visibility. The stated reason is observed text, not proof of the author's full motive or of the files' safety. The archives remain unopened.
8. **How can the same data/instruction boundary support opposite goals?** Treating inner text as data answers whether it can instruct the agent, not whether the outer task is authorized. TeaPrompt's authority map keeps user tasks below system/project constraints; its sink gate bounds effects. A research label cannot raise the task above either boundary.
9. **Which source is current?** S3 still calls v42 the default production release and discusses active v50 development; S1/S2 designate v45 stable and report formal v1. This is a verified within-pin currency divergence. The record uses S1/S2 for release status and attributes S3's rules to that note, rather than silently applying every S3 default to every later release.

### Questions about the coordinator and panel

- **Was “no sibling text” confused with no existing defense?** Yes for the broad E-11 claim. The evidence lens confirmed the precise sentence absent, while other lenses identified the four evidence dimensions and audit-the-reason rule. These are compatible findings, not grounds to force a new sentence.
- **Did E-5 require a new data field?** No demonstrated data-capacity defect exists: the current manifest/evidence references can point to an exception decision. The plausible residue is visibility at the acceptance record, not permission to override or a runtime failure. A clause is smaller than a new field and remains deferred.
- **Did the panel establish bad faith or impossible verification?** No. Its strongest rhetoric exceeded the checked evidence. Shared corrections are not eight independent confirmations, and the coordinator rejects the motive and impossibility claims.
- **Was a recurrence rule invented?** The packet's “two records, same pattern” was not an exact quotation of `PROJECT_KNOWLEDGE.md:64-66`, which admits recurrence or concrete evidence. Its in-place-repair caveat at `:85` also remains valid. Deferral here is a scoped choice based on missing local failure evidence and existing coverage, not a new universal veto on reading-found repairs.

## Candidate Adoption Ledger

These are review triggers, not queued implementation instructions. `untriggered` means no qualifying local event was identified in the reviewed evidence; it does not claim exhaustive knowledge of all TeaPrompt use.

| ID | Candidate | Status | Trigger state | Evidence / smaller alternative | Next action or trigger / destination |
| --- | --- | --- | --- | --- | --- |
| E-2 | Preserve unsuccessful attempts instead of selecting an unchanged passing rerun | Record-only | untriggered | E-2 map; evidence/usability find a narrow literal gap, red team calls it covered, measurement questions transfer to deterministic fixtures. Keep the existing evidence record instead of installing a universal first-draw rule. | A local record silently replaces a valid failure with an unchanged passing rerun. Reassess `reflective-implement` Verification, distinguishing diagnostics and predeclared repeat studies from selective replacement; no adopted draft. |
| E-5 | Make acceptance over an unmet oracle legible on the record | Deferred | untriggered | E-5 map; no qualifying local governed-delivery acceptance was found. Existing references can carry the decision, so reject a new field before testing the smaller labeling clause. | First local governed-delivery acceptance closed against an unmet oracle. Inspect whether the record already identifies it; if not, review the reserved clause at `governed-delivery` acceptance-record invariant only. |
| E-11 | Read the verdict definition before trusting a metric's name or stated purpose | Record-only | untriggered | S1/S3 mismatch in what a score can establish; actual heading and disclosed objective narrow the panel claim. Existing four-dimension evidence review is the smaller defense. | A local citation treats a metric's label as proof of a property its rule does not measure. Reassess source evaluation in `reflective-research`; a new Durable Lesson would require its own evidence and approval, not this row alone. |
| E-12 | Distinguish data classification from outer-task authorization | Record-only | untriggered | Authority and sink boundaries already exist. Record this external threat-model example rather than another operating rule. | A second independent record demonstrates outer-task framing crossing an authority or sink boundary. Reassess a Durable Lesson against the existing trust-boundary text; no automatic skill change. |

**Reserved E-5 wording, not adopted** — replace only the existing acceptance-record invariant if a later review authorizes it:

> Invariant: execution success alone never closes this record; when a named decision closes it against an oracle that did not hold, the record names that oracle and the deciding reference — a bare `closed: true` never stands for an oracle that held.

The field alternative, `unmet_oracles: []`, is rejected for now as heavier than the clause; empty population would not prove there were no unmet oracles. Neither form enforces honesty. The named accepter, constitutional-path ownership, host evidence, and oracle status remain distinct responsibilities.

## Required Wording Changes

Only this record and its index summaries change. No installed wording is adopted.

- Attribute every pass count and runtime assertion; use “documented” rather than “well-built” or “verified” for unexecuted machinery.
- Name the **filename**, actual heading, explicit objective, and README purpose separately. Record historical inversion as an inference, not an observed timeline.
- Distinguish release promotion from satisfying B and permission to start C.
- Describe E-5 as representation/visibility, not absent permission or a proven executable-template defect.
- Preserve the no-adoption outcome without treating current host non-operation as proof that prompt-level recording rules can never help a downstream user.

## Packet Corrections and Post-panel Source Checks

1. `PROJECT_KNOWLEDGE.md:54` is the domain-pack admission/recurrence rule, not an acceptance-record override mechanism. Its analogy does not prove E-5 is already implemented.
2. The Lessons introduction is not an exact “two-record” rule. The in-place-repair caveat also precludes turning this survey's default into a general prohibition.
3. The governed-delivery guard pins template names and other contracts, not the acceptance-record YAML field set. Adding a field would not collide with the claimed field-set pin. No field was added.
4. `governed-delivery` measured **15,146 Unicode characters** at synthesis, not the packet's 15,161. One lens also called `wc -c` bytes characters. Size headroom was not an adoption argument.
5. “CI tests only the installer” was too narrow: the workflow covers deployment, archive sync, and star-history functionality; capability/scorer/bank validation remains excluded.
6. Pinned S3 corrected the shared “document titled safety-eval” claim. Its heading explicitly says Prompt Bank Evaluation. The strong historical “objective inverted under an unchanged title” claim was not established.
7. S5 supplies an explicit sensitive-fixture explanation for archive packaging. No archive was inspected; “unreviewable,” covert scan-evasion, and authenticity conclusions from packaging alone are not adopted.
8. `workers=1` does not prove one sample per case. The panel's illustrative variance estimates, “random walk” characterization, and claim of abandoned repeat sampling are not measured findings. The absence of a sufficient published uncertainty protocol is the narrower supported observation.
9. Independent origin, permanent unverifiability, and the claim that attack-success scoring cannot serve safety research are not established. These are narrowed even where several reviewers agreed.
10. S3's v42/default and v50/development statements conflict with S1/S2's current release descriptions. The divergence is retained, not reconciled by copying either default into TeaPrompt.

## Disagreements / Residual Risks

- **E-2:** one reject, one defer, six record-only. Some reviewers treated existing rules as complete coverage; evidence/usability distinguished a no-change rerun residue. A deterministic fixture is not the whole universe of downstream skill use, and prompt text lacking enforcement is not automatically worthless. No local failure was found, so the record—not a new universal rule—is sufficient now.
- **E-5 shape:** methodology/minimality preferred a clause; usability/provenance preferred field plus invariant; red team preferred field plus a pointer while warning about self-assertion. The coordinator selects a deferred clause as the smallest candidate, without claiming the shape was unanimous.
- **E-11 locus:** strategy argued intent-to-spec; methodology argued spec-to-oracle and stale propagation; evidence saw the strongest absent reading check; other lenses called it covered. The primary-source correction prevents adopting any single historical-drift taxonomy as established. Current claim-to-measure mismatch is the retained observation.
- **Threat-model framing:** “value-neutral” is incomplete without who authorizes the outer task and which higher constraints still bind it. E-12 records both. No safety bypass procedure is retained.
- **Sampling, classifier validity, authority, and configuration effects remain unknown.** The documents and arithmetic do not prove them; an audit of sensitive records would need an appropriately authorized scope. No claim of provider terms violation is made from the account-risk warning alone.
- **Governance weight:** this is an archived decision plus structural guard, not another operational rulebook. No tenth core skill, new pack, runtime, benchmark service, or automatic deployment path is introduced.

## Evidence Used

All sources below were accessed on 2026-09-10 at the immutable pin `0ad8ec58e1989f4a058e01ce4e15cf226e8067bf`. Source identifiers used above refer to this table. The stated release/model labels belong to the surveyed repository; their upstream availability was not independently checked.

| ID | Source | Checked | Verified scope / unresolved boundary |
| --- | --- | --- | --- |
| S1 | [README_EN.md](https://github.com/MDX-Tom/gpt-instruct/blob/0ad8ec58e1989f4a058e01ce4e15cf226e8067bf/README_EN.md) | accessed 2026-09-10 | Purpose, release labels, gates, account-risk warning, documented install/reset behavior. No install or outcome proof. |
| S2 | [Comparison Tests](https://github.com/MDX-Tom/gpt-instruct/blob/0ad8ec58e1989f4a058e01ce4e15cf226e8067bf/docs/comparison-tests-en.md) | accessed 2026-09-10 | Gate and observer definitions, table figures, historical separation, local-evidence note. All runtime results author-claimed. |
| S3 | [Prompt Bank Evaluation](https://github.com/MDX-Tom/gpt-instruct/blob/0ad8ec58e1989f4a058e01ce4e15cf226e8067bf/docs/gpt-5.6-sol-safety-eval.md) | accessed 2026-09-10 | Actual heading, current objective, verdict rules, legacy result attribution, stale release references. No scorer or bank inspection. |
| S4 | [CI workflow](https://github.com/MDX-Tom/gpt-instruct/blob/0ad8ec58e1989f4a058e01ce4e15cf226e8067bf/.github/workflows/test-codex-instruct.yml) | accessed 2026-09-10 | Workflow definition, Python 3.8/3.13 matrix, read-only repository permission, explicit capability/scorer exclusion. No CI execution. |
| S5 | [.gitignore](https://github.com/MDX-Tom/gpt-instruct/blob/0ad8ec58e1989f4a058e01ce4e15cf226e8067bf/.gitignore) | accessed 2026-09-10 | Exclusion patterns and stated sensitive-fixture rationale. Ignore patterns alone are not a full tracked-tree inventory. |
| S6 | [LICENSE](https://github.com/MDX-Tom/gpt-instruct/blob/0ad8ec58e1989f4a058e01ce4e15cf226e8067bf/LICENSE) | accessed 2026-09-10 | MIT text; copyright 2026 li lingbo and yynxxxxx. License is not effect authorization. |
| S7 | [Commit metadata](https://api.github.com/repos/MDX-Tom/gpt-instruct/commits/0ad8ec58e1989f4a058e01ce4e15cf226e8067bf) | accessed 2026-09-10 | SHA, 2026-09-07T09:31:07Z date, unsigned status. No inference of compromise from lack of a signature. |

## Evidence vs Inference

- **Observed:** the exact pinned source text in S1–S7; the local skill/template fields cited above; the review messages and reason split; the source-derived arithmetic calculation below. Observing a result table proves what the author reports, not the underlying run.
- **Author-claimed:** all pass counts, gate outcomes, model identities, release-byte equivalences and archive digests, scorer neutrality, verifier success, isolation, and rollback behavior. None was reproduced here. No stars/forks count is used as efficacy or adoption evidence.
- **[INFERENCE]:** a generic marker-based scorer could misclassify useful or incorrect outputs; a static filename could encourage a reader to infer the wrong construct; omitted classification/provenance controls could enable selective relabeling. These are plausible risks, not exercised exploits or verified defects.
- **Not established:** a covert or historical objective inversion, malicious motive, independent origin, numerical variance, a blanket inability to audit safely, or downstream safety benefit.

## Evidence Actually Checked

The source-text check used `read` on each S1–S7 exact-commit URL (raw-file equivalents for S1–S6). It did not use a clone, prompt archive, bank, screenshot, or model run. Local checks read the acceptance-record invariant and Delivery Invariants, the research/review evidence contracts, the authority map, the promotion rationale, and the adoption-state guard. Reviewers additionally searched the plan records for unchanged-rerun replacement and undisclosed oracle overrides; none was identified in that search, which is not proof that no user has encountered either failure.

**Arithmetic only:** Bun/JavaScript `reduce` summed the case/turn columns transcribed from S2's four family tables; percentages used `(passed / total * 100).toFixed(2)`. Inputs and outputs:

| Version | Case numerators | Turn numerators | Sum / denominators | Recomputed case / turn percentages |
| --- | --- | --- | --- | --- |
| v1 | 7,11,0,8,13,13 | 9,15,0,8,13,15 | 52/66; 60/74 | 78.79%; 81.08% |
| v42 | 5,9,0,7,10,12 | 7,13,0,7,10,14 | 43/66; 51/74 | 65.15%; 68.92% |
| v44 | 4,8,0,7,16,14 | 5,11,0,7,16,16 | 49/66; 55/74 | 74.24%; 74.32% |
| v45 | 4,10,0,8,16,16 | 6,14,0,8,16,18 | 54/66; 62/74 | 81.82%; 83.78% |

Case denominators were 8,12,6,8,16,16; turn denominators 10,16,6,8,16,18. The v1 artifact numerator is 7+8=15; 66−52=14 matches the reported one provider block plus thirteen returned-result failures. The v45−v42 delta is eleven cases and eleven turns. The evidence lens independently re-added the tables. This checks arithmetic and transcription only; it supplies no independent evaluation result.

The clean-room scan covers `skills/*/SKILL.md`, both `SKILL_INSTALLATION*.md` guides, `GLOSSARY.md`, and `04-agent/*.md`, excluding dated records where source names belong. The guard checks record identity, the concept and candidate ledgers, trigger states, reserved-content separation, and discoverability. Following Adoption Guard Closure, it does not pin the report's interpretive paragraphs or turn deferred wording into an adopted skill contract.

**Sufficiency:** every load-bearing source claim is checked or explicitly unknown; both frames, the scope exclusions, the reason splits, and the local-gap question have dispositions. More payload access is unnecessary to decide this survey's no-adoption recommendation.

## Falsifiability

Reopen this record if a candidate's named trigger is observed and left unreviewed; if an existing installed sentence is shown not to cover a claimed covered concept; if authorized independent evidence validates or refutes the reported outcomes; or if exact-revision evidence contradicts the source interpretation above. A later pin changes freshness, not the historical record. A new safety-benefit study could change the E-11 assessment without proving that this survey observed one.

The record is also wrong if any excluded payload or tool was actually executed, a claimed lens deliverable is missing, a result silently upgrades from author-claimed to reproduced, or deferred wording appears on an installed surface without an explicit ledger decision. The guard binds repository authors and record consistency, not agent-session behavior.

## Completion Ledger

| Item | Status | Evidence |
| --- | --- | --- |
| Pinned source and eight-lens synthesis | verified | S1–S7; full review messages; coordinator qualifications recorded separately |
| All thirteen concepts and four candidate decisions | recorded | Concept Map; Candidate Adoption Ledger; no installed adoption |
| Survey guard and index integration | verified | `plans/tests/test_gpt_instruct_survey_record.py`; Decision Index; Case Comparison and State Ledger rows updated |
| Final repository verification | verified | `make all` 1144 passed; validators 0 errors; lint 1 pre-existing warning; record hygiene 0/0 |
