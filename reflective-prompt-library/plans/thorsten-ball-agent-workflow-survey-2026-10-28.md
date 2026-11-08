# Thorsten Ball: How I Work with Agents — Source Survey (2026-10-28)

Language: English

> **Status: recorded; reference-only, non-authoritative.** The user requested “Survey” of the supplied X status. TB-DOC1 preserves the research and source qualifications; TB-1–TB-7 adopt no skill, runtime, route or operating rule. Earlier update/commit/push grants for other surveys do not carry into this task. No model experiment, installation, production access, publication or change to an existing gate is authorized here.
>
> **2026-11-07 follow-through:** the owner's “Survey” of a supplied secondary reading (Paul Kuo, paulkuo.tw, 2026-11-07) adds [`TB-DOC2`](#secondary-reading-follow-through--2026-11-07): an unchanged-body recheck of S2, secondary fidelity verdicts and a mapping of its evidence lists to delivered contracts. Reference documentation only; TB-1–TB-7 are unchanged.

## Research Question

What does Thorsten Ball's October 2026 working-practice article actually recommend, which qualifications appear in his related primary presentation, and what—if anything—does it expose beyond TeaPrompt's current delivered methods?

## Direct Recommendation

**Preserve the operational synthesis, not a new prompt recipe or a reduced safety floor.** The most useful interpretation is to reduce synchronous human micromanagement while improving the agent's ability to exercise the system and produce inspectable evidence. That is a judgement about the method, not a demonstrated productivity effect.

The central unit is the **agent–codebase–process combination**, rather than the prompt alone. Outcome-oriented instructions work in his account alongside accessible tools, runnable environments, production observations, task history, feature flags, explicit human decisions and a team capable of evaluating results. The short article is not evidence that these conditions can be removed.

No missing portable TeaPrompt instruction was demonstrated. Keep the existing evidence, context-fidelity, evaluation and effect-authority contracts. A new source's endorsement of similar ideas is external corroboration, not local recurrence or an efficacy result.

## Version / Date Context and Evidence Used

All sources below were checked **2026-10-28**. Their publication dates remain distinct.

| ID | Source and identity | What was actually read | Evidence limit |
| --- | --- | --- | --- |
| S1 | [Supplied X status](https://x.com/thorstenball/status/2114386050638336082), Thorsten Ball; `2026-10-25T15:58:12Z`; linked article ID `2114385531811319808` | [Official X syndication JSON](https://cdn.syndication.twimg.com/tweet-result?id=2114386050638336082&lang=en&token=1): author, exact post text, date, article title/ID and preview | Native X read was blocked. Official syndication does not supply the complete article body. |
| S2 | [How I work with Agents](https://x.com/i/article/2114385531811319808), full body delivered by [public FxTwitter mirror](https://api.fxtwitter.com/status/2114386050638336082) | All returned article blocks; mirror creation/modification fields both identify October 25 | Full body is a mirror representation, not an authenticated native-X body comparison. S1 independently binds the status/article identity and preview, not every body sentence. |
| S3 | [Amp Time Capsule 6: How Thorsten Ball Uses Amp](https://ampcode.com/time-capsules/6), published October 13, duration 34:31 | Official page, chapters and complete published transcript, described as automatically generated and lightly edited | No audio/video watched; demonstrations and internal thread results were not independently executed. This earlier talk contextualizes—but does not amend or prove unchanged policy in—the October 25 article. |
| S4 | [Amp: What Are Orbs?](https://ampcode.com/what-are-orbs) | Public product description of per-thread machines, setup, inter-agent communication, pause/wake and host-managed billing | Vendor feature description, not an isolation/security audit, cost measurement or deployment qualification. |

S3 and S4 are primary vendor/author material, not independent replications. Source publication confirms what is claimed, not the underlying efficacy. Refresh these living pages and host capabilities before any later operational recommendation; retain the dates and historical attribution above.

### Executed source-identity and extraction check

A small read-only JS check fetched the two known JSON endpoints, compared status ID, article ID, author, title and exact post text, then extracted the article's block text. It found **16 body blocks: one date lead and 15 advice units**. An independent scan for 15 manually enumerated opening clauses matched each exactly once; it did not reuse the bold-style extraction logic.

The article's returned block-link entity count was zero. The official post's one URL was a positive control for link discovery. This is a bounded statement about those returned fields, not all replies, embeds or the author's other posts.

Snapshot SHA-256: `9a26fbeb7a4bfe9a10562627194b0b9fe673c38335783076827f8fc98b888a93` over UTF-8 block texts joined with two LF characters and one final LF, without Unicode normalization. A digest identifies the extracted snapshot; it does not authenticate the mirror or prove completeness beyond the returned payload. The supplemental session receipt `thorsten-source-snapshot-2026-10-28.json` preserves the selected source fields, extraction and independent-count checks. No executable author code or model was run.

## What the Article Recommends

The table paraphrases S2 rather than reproducing its prose. S3 timestamps identify contextual qualifications, not new experiments.

| Unit | Advice in the article | Assessment / qualification |
| --- | --- | --- |
| A1 | Prefer the most capable current models over apparent token-price savings | Plausible total-task-cost hypothesis, not a universal ranking. S3 at 07:18 expressly allows cheaper models meeting evals for predefined classification/routing workloads. The article's percentage/person-hiring analogy is not measured model error or cost data. |
| A2 | Reconsider the assumption that agent-generated clutter inevitably makes a codebase unmaintainable | Author's changing belief, not longitudinal maintenance evidence. Better repair tools can change economics without eliminating complexity, regressions or data-loss risk. |
| A3 | Describe desired outcomes rather than dictating the implementation path | Useful when outcome, invariants and acceptance are clear. The compiler/VM speedup example is an author-reported toy-project case, not a portable guarantee. A speed target still needs correctness, workload, baseline, noise and resource bounds. |
| A4 | Make the whole development lifecycle observable and exercisable | Strong design direction, but tool access does not eliminate hallucinations or misinterpretation. S3 at 18:44 permits read-only access according to risk; visibility and authority are separate. |
| A5 | Supply tools for diagnostics, health, customer communication and feature flags | An integration pattern, not permission to send messages, expose logs, grant credits or change production. The talk includes explicit human actions and approvals. |
| A6 | Experiment on whether agents actually consume repository knowledge | The strongest methodological point: observe tool/script use and resulting state in fresh controlled runs, rather than merely checking that documentation exists. Five agents is an illustrative setup, not statistical sufficiency or proof of blinding. |
| A7 | Prefer isolated remote task environments over conflicting local processes | Host-platform option with useful resource and lifecycle separation. Remote machines are not automatically secret isolation, reproducible builds, unlimited resources or authorization. Platform-specific tasks can still need local runners; S3 at 22:00 discusses them. |
| A8 | Have the agent create variants or diagnostic experiments instead of making the human drive every iteration | Useful for bounded exploration and inspectable comparisons. S3 at 12:21 acknowledges exceptions, including infrastructure work. Twenty variants and four hypotheses are examples, not required quotas. |
| A9 | Demand concrete proof: walkthroughs, before/after measurements and real-system evidence | Useful evidence request; the phrase does not make proof irrefutable. A video, a selected success path or an agent-written test matrix does not establish complete correctness, independent checking or oracle integrity. |
| A10 | Batch larger tasks and interact asynchronously instead of watching every turn | Appropriate when boundaries, stop conditions and handoffs are explicit. Time-to-first-token is not the same objective as safe completion or human waiting time; neither async nor a larger task supplies ownership or a budget automatically. |
| A11 | Use scheduled wake-ups and checks for long-running follow-through | A host liveness feature, not a prompt capability. Durable schedules, identity, expiry, caps, cancellation and approval remain host concerns. No scheduler was installed or qualified here. |
| A12 | Let the host compact context; keep one task per thread | Reduce token micromanagement where the host supports it; do not discard durable task state. S3 at 08:36 also says to obtain and use a plan. Long-thread message examples are anecdotes, not a compaction-fidelity benchmark. |
| A13 | Use searchable threads linked to commits as organizational memory | Useful historical rationale and discovery. Retrieved discussions remain dated evidence, not current authority or canonical acceptance; lifecycle, access, invalidation and retention need owners. |
| A14 | Avoid agent-written interpersonal prose while permitting mechanical explanations/reports | A communication preference with explicit exceptions, not a general capability result or a ban on documentation. Human accountability and audience fit matter more than a universal text-generation rule. |
| A15 | Concentrate manual code review on high-blast-radius changes | Risk-weight review effort; do not interpret the author's small central-file count as a project-independent threshold. S3 at 14:01 and 25:30 places this in a senior team with end-to-end evidence, dogfooding, feature flags and recoverability. |

## Three Load-Bearing Distinctions

### Outcome delegation is not contract deletion

**[INFERENCE]** The valuable shift is from prescribing every keystroke to defining a result and making its validation possible. Requirements, invariants, compatibility bounds, acceptance and authorization still constrain the work. A3 does not establish that every procedural skill is obsolete or that all prompt content outside a short taxonomy is harmful.

The [delivered spec-plan contract](../skills/reflective-spec-plan/SKILL.md#workflow) already says requirements name outcome and acceptance rather than route, except where the product fixes the route. It also asks plans to carry decisions the executor cannot recover. That is more precise than either mandatory micromanagement or an unrestricted instruction to optimize indefinitely.

### Legibility and autonomy do not transfer authority

S3 at [18:44](https://ampcode.com/time-capsules/6?t=1124#video) explicitly permits risk-based read-only visibility. At [20:28](https://ampcode.com/time-capsules/6?t=1228#video) the speaker describes manually granting production access; at [32:45](https://ampcode.com/time-capsules/6?t=1965#video) he describes human feature-flag approval. The OOM case is narrowed further to a flag affecting him and a reproducible check. These are stated source qualifications, not proof that the underlying permission system is secure.

The direct-to-main/no-PR account at 25:30 is a team-specific process choice, not evidence that review or authorization is universally unnecessary. This survey does not recommend removing TeaPrompt's gates or reproduce Amp's deployment topology. No production, customer-email, credit-grant or feature-flag action was taken.

### Evidence production, behavioral checks and efficacy are different outcomes

S3 at [29:04–30:33](https://ampcode.com/time-capsules/6?t=1744#video) describes fresh environments, controls and checking whether a documented script/plugin was used. That is closer to a useful behavior probe than asking an agent to repeat the rule. It still leaves assignment, oracle protection, scorer blinding, hidden-answer access, complete allocation accounting, cost and final holdout measurement unspecified in the material reviewed.

The published transcript narrates successful examples; this survey did not inspect their private receipts or replay them. Successful instruction consumption is not automatically better engineering output. Likewise, generating a demo establishes neither all-path correctness nor independent verification. The right evidence burden depends on the particular claim.

## Candidate Adoption Ledger and Checked Local Coverage

These are current repository-delivered paths/sections, not the reviewing assistant's host instructions. Coverage means the named methodological clause exists; it does not prove operational enforcement or compliance by an installed agent.

| ID | Disposition | Checked local surface / source units | Reopening evidence |
| --- | --- | --- | --- |
| TB-DOC1 | Recorded as reference evidence only | This source-bound survey, existing catalogue and generated discovery. Preserves the mirror/native/ASR boundary, source dates and all fifteen units without adding a new operating rule. | Consolidate a current duplicate; correct contrary source identity/text or attribution. |
| TB-1 | Outcome-first planning already explicit; no skill edit | A3/A8: [spec-plan Definition of Done and Workflow Design](../skills/reflective-spec-plan/SKILL.md#workflow), [minimality Purpose/Safety Floor](../skills/reflective-minimality/SKILL.md#safety-floor). Existing contracts distinguish the result from optional implementation choices. | A reproduced local over-prescriptive plan or missing experiment/acceptance contract not covered by the delivered instructions. |
| TB-2 | Operational legibility is useful; no new SDLC entry point or privilege grant | A4/A5/A9: [verification-map generator](../skills/verification-map-generator/SKILL.md#generation-procedure), [implementation Verification](../skills/reflective-implement/SKILL.md#verification), [risk Rules](../skills/reflective-risk/SKILL.md#rules), [runtime trust boundary](../04-agent/runtime-trust-boundary.md). A runnable discovery surface does not supply deployment authority. | A named product's fresh consumer cannot exercise an intended authorized surface because a specific delivered instruction is missing. |
| TB-3 | Behavioral evaluation corroborates existing methodology; no campaign or efficacy claim | A6/A9: [golden runner Methods](../skills/golden-benchmark-runner/SKILL.md#methods), [blinded harness Honest Limits](../skills/arm-blinded-eval-harness/SKILL.md#honest-limits), [review Claims Ledger/Evidence Tiers](../skills/reflective-review/SKILL.md#claims-ledger). Protected observable outcomes, matched arms, noise and separate final evaluation remain necessary. | A reproducible local measurement defect exposing a missing instruction, or controlled new evidence bearing on a named skill; new execution still needs its own scope and caps. |
| TB-4 | Bounded async/variant work is a task-shape option; remote environments and schedules remain host-owned | A7/A8/A10/A11: [spec-plan Workflow Design](../skills/reflective-spec-plan/SKILL.md#workflow-design-mode), [flow generator Script Contract](../skills/flow-control-generator/SKILL.md#script-contract), [Standing Non-Goals](../PROJECT_KNOWLEDGE.md#standing-non-goals). No new scheduler, unlimited fan-out or cloud dependency. | Demonstrated local liveness/resource failure plus an explicit owner decision about the required host guarantee. |
| TB-5 | Do not retire ledgers/handoffs or elevate thread history to authority | A12/A13: [handoff Continuation Packet](../skills/reflective-handoff-retro/SKILL.md#continuation-packet), [context engineering](../03-context/context-engineering.md), [memory consolidation](../04-agent/memory-consolidation.md). Automatic compaction and faithful durable state are separate concerns. | Source-bound host evidence that a replacement preserves identifiers, commands, unknowns and invalidations across reset, plus authority to replace the existing mechanism. |
| TB-6 | No universal newest-model, clutter-tolerance or minimal-review policy | A1/A2/A15: [review Four Evidence Dimensions](../skills/reflective-review/SKILL.md#four-evidence-dimensions), [minimality Safety Floor](../skills/reflective-minimality/SKILL.md#safety-floor), [risk Sink Inventory/Rules](../skills/reflective-risk/SKILL.md#sink-inventory-and-unattended-envelope). Do not trade maintainability/security for an unmeasured cost or model-quality assumption. | Controlled task-cost/quality and longitudinal maintenance evidence for the target workload, with unchanged acceptance and risk constraints. |
| TB-7 | Communication preference retained as context; no core text-generation prohibition | A14: no public result here establishes a general writing capability limit. Existing output/acceptance ownership can express an audience-specific requirement without a new skill. | A concrete team/user communication requirement or measured audience outcome, not one author's taste alone. |

The [current accepted-inconclusive dogfood outcome](skill-dogfood-test-plan-2026-10-08.md#stage-1-outcome-disposition-2026-10-13), procedural-versus-strong-custody distinctions and existing held gates remain unchanged. The external article's five-agent suggestion is not local utility evidence or a qualification of this host's blinding.

## Assessment and Counterargument

**[INFERENCE] Best transferable synthesis:** invest in the product's executable/observable surface, then test whether repository knowledge changes what agents do. Let async work reduce the human's interruption burden, not reduce acceptance or permission controls. This is a useful integrated framing even where the constituent rules already exist.

**Strongest counterargument:** an experienced practitioner may rationally prefer a powerful model, lighter formal review and fast production feedback on a well-instrumented, reversible product; requiring every task to carry a heavy process would erase much of the benefit. Decision: agree with risk-scaled workflow and less micro-control, not a universal relaxation. Existing strictness-scaled contracts allow a small workflow while preserving the safety floor.

**What this survey does not judge:** personal writing taste, the team's private code quality, actual Orb security/billing/retention implementation, whether every narrated demo succeeded, and comparative model rankings. These were not audited. The ruling owners are respectively the intended audience/team, Amp maintainers and the separately scoped experiment/deployment owner—not this article survey.

## Evidence vs Inference

- **Verified source binding/text:** official post metadata, mirror-delivered body extraction, and the published earlier presentation/feature descriptions. Full native article authentication and audiovisual verification remain unavailable/unperformed, respectively.
- **Author-reported:** productivity, cheaper-model rework cost, maintainability/clutter experience, successful private tool/evaluation/deployment trajectories, compaction quality and thread-memory value. Their attribution is supported; their generation and generalization were not independently measured.
- **Examples, not measurements or quotas:** percentage analogies, thread lengths, small central-file counts, five agents, twenty variants and four hypotheses.
- **Observed locally:** source/extraction checks and the existence of the cited delivered contracts. Documentation/navigation checks are recorded in the [delivery report](../../review/final-report.md#thorsten-ball-agent-workflow-survey-2026-10-28); they are not evidence that these practices improve agent outcomes.
- **[INFERENCE]:** record-worthy synthesis, no demonstrated new local instruction gap, and no basis here for changing runtime ownership, model defaults, review authority or a standing experiment gate.

## Falsifiability

A different authenticated article body would require correcting the mirror-based claim map. A newer primary source could change current advice, but would not erase what these dated sources said. Keep the October 13 context distinct from the October 25 article.

A reproduced local consumer failure outside the checked delivered instructions reopens its TB-* candidate. A controlled comparison could change the cost/quality, knowledge-utility, compaction or review judgement; it must bind the target task, model/harness/setup, observable outcome and oracle, and preserve incomplete/negative results. A polished demonstration or the same author's repeated assertion alone would not meet that bar.

## Risks / Unknowns and Handoff

This is a source survey, not an Amp installation, production security review, experimental replication or recommendation to deploy without review. No hosted agent experiment, source demo, customer action or scheduled wake-up was run. No raw article or vendor prompt was copied into a portable operating contract; the claim map is paraphrased and source-qualified.

Sufficiency: the supplied object is identified, all returned advice units are covered, decision-bearing qualifications have primary contextual sources, and every recommendation either names checked local coverage or remains an explicit unknown. Further model/product research is unnecessary for the record-only decision.

No skill, core/domain registry, routing fixture, acceptance oracle, memory authority or runtime/campaign gate changed. No commit or push is included. Future admission, experiment or operational changes require their own scope and authority rather than inheriting it from this survey.

## Secondary-reading follow-through — 2026-11-07

The owner asked to survey `paste-14.md`, a capture of Paul Kuo's zh-TW article “Agent 說做完了，你怎麼知道？讀 Thorsten Ball 的十五條 Agent 工作習慣”. It rewrites the October 25 article for non-programmers around two questions: can the agent see the work's actual state, and was “what does not count as evidence” written down before delegation? It adds two evidence lists, permission and notification boundaries and three reservations. **Outcome: `TB-DOC2` reference documentation only.** TB-1–TB-7 and the S1–S4 attributions are unchanged. A secondary reading is not new primary evidence about Amp practice or outcomes. One read-only coverage scout reported to the coordinator, who re-read each cited delivered sentence; no review panel was convened.

### Inputs and identity

| Input | Checked identity (2026-11-07) | Limit |
| --- | --- | --- |
| `paste-14.md` | SHA-256 `54134104f14039790b47ba5bd5300606e99ce4c94a2299b38373e16d31df0eec` | Reader-mode capture. Sentence-level comparison with the live page found every body sentence. The summary box and four-question FAQ are also in the live HTML and `FAQPage` JSON-LD; only the site's Markdown variant (SHA-256 `4dc9e1e16b4c5657a24f46c0fe49709018e569c27761d25af8389adb3c6ff8db`) omits them |
| [Live article](https://paulkuo.tw/articles/delegate-to-agents-what-counts-as-proof/), checked 2026-11-07 | `datePublished` and `dateModified` both 2026-11-07T09:00:00+08:00 | Links the same status as S1 (`2114386050638336082`). A later modification needs a fresh comparison |
| S2 via the [FxTwitter status endpoint](https://api.fxtwitter.com/status/2114386050638336082), checked 2026-11-07 | 16 blocks; article created and modified 2026-10-25T15:58:12Z; snapshot SHA-256 `9a26fbeb7a4bfe9a10562627194b0b9fe673c38335783076827f8fc98b888a93` | Same digest as October 28, so the A1–A15 claim map stands on unchanged text. The mirror reported 1,129,776 views, consistent with the secondary's “about 1.1 million”; a mirror counter is not authenticated X analytics |
| Author identity: [thorstenball.com](https://thorstenball.com/), [interpreter book](https://interpreterbook.com/) and [compiler book](https://compilerbook.com/), checked 2026-11-07 | Self-described Amp co-founder and author of both books | Supports the secondary's biography; not an independent corporate record |
| Cited incident: [Paul Kuo, 2026-10-12](https://paulkuo.tw/articles/ai-team-one-works-others-check/), checked 2026-11-07 | Names Google Antigravity as the reviewer that labeled pasted content as a file read, with an invented path and line numbers counted from the paste | Also reports a silent fallback to a default model and a second write attempt after a denied write. Author-reported; nothing reproduced |

### Fidelity of the secondary reading

| Secondary claim | Verdict | Evidence / qualification |
| --- | --- | --- |
| Fifteen-row table, A1–A13 | faithful paraphrase | Omissions are illustrative: the hiring analogy and model jab (A1), a second example (A3), `scripts` (A6), TTFT and “be more ambitious” (A10), “knowledge multiplies” (A13). No inversion found |
| A9: put “this is not evidence” in AGENTS.md | verified (verbatim) | The two lists that follow are the secondary's own extension, and it labels them as such |
| A14 exception and rationale | qualified | The table drops “some docs” and the stated criterion, “mechanical stuff where human on other end doesn't matter that much”. The secondary reads the concern as forwarding unread text; the stated criterion is the reader's stake, so its reason for not following A14 answers a different concern. Its practice—the human owns structure, viewpoint and every retained sentence—fits TB-7 |
| A15: fewer than five central files, database migrations and four questions | faithful; slight over-reading | “四題都過，他才可能去看程式碼” adds “only then” to the terse “If yes, might review code” |
| A2 and A15 state no preconditions | qualified | True of A2. A15 states four checks, which the secondary itself uses as conditions. TB-DOC1's A15 reading of S3 (14:01, 25:30) supplies the senior-team, end-to-end, dogfooding, flag and recoverability context that the secondary infers without citing |
| “His list lets agents deploy and email customers; I am more conservative” | qualified | Accurate for A4's wording. TB-DOC1's reading of S3 at 18:44, 20:28 and 32:45 records risk-based read-only access, manually granted production access and human flag approval ([Legibility and autonomy do not transfer authority](#legibility-and-autonomy-do-not-transfer-authority)) |
| Date, “as of October 2026” lead, view count, biography | verified | Identity table above |

### Additions mapped to delivered contracts

Correction retained: a delegated coverage summary said the secondary relies on prompt instructions for outward actions. The supplied text (lines 65–67) prefers removing permissions in tool configuration over a chat instruction, so the corresponding row records alignment.

| Secondary addition | Coverage | Delivered text |
| --- | --- | --- |
| Not evidence: completion declarations; summaries or numbers without an openable source | covered | “Do not claim completion until the tool result or other evidence supports the claim” (`04-agent/runtime-trust-boundary.md:114`); “A summary's citation is the summary's claim about a source” (`skills/reflective-research/SKILL.md:107`); “the agent's own summary of it is not” evidence (`:137`) |
| Not evidence: a file or URL the agent says it read that cannot be opened | covered (claimant and reviewer) | “Do not claim execution, tests, source review, or verification that did not happen” (`skills/reflective-dispatch/SKILL.md:48`); never “invent logs, benchmarks, or tool results” (`06-repo/AGENTS.md:132`); Existence includes “fabricated citation”, and `verified` requires “examining the evidence yourself” (`skills/reflective-review/SKILL.md:87`, `:78`). A pasted excerpt labeled as a file read is an instance of these rules, not a separate class |
| Not evidence: the same AI re-checking its own answer | covered | Same-model, same-context review “is one epistemic channel, not independent verification”; a high-risk PASS needs a non-model channel (`skills/reflective-review/SKILL.md:99`); re-running the generator “is not a check” (`skills/reflective-research/SKILL.md:109`) |
| Evidence: resolvable source link, before/after comparison, repeatable steps | covered | Existence and number/text dimensions (`skills/reflective-review/SKILL.md:87-88`); “test output, diffs, reproduction, measurements” (`:69`). A screenshot or before/after view supports only the observable claim it shows. On its own it does not establish causality, behavior on unsampled paths (Extrapolation, `:90`) or acceptance (`skills/governed-delivery/SKILL.md:106`) |
| Evidence: an uninvolved reviewer whose report itself carries such evidence | covered; stricter for high risk | Evidence ranking and channel declaration (`skills/reflective-review/SKILL.md:98-101`); “Self-report is not attestation” (`skills/governed-delivery/SKILL.md:108`). Cross-vendor review remains model judgment: it may block or warn, but cannot by itself pass a high-risk claim |
| Pre-declare the not-evidence list in the delegation | partial | The classes already exist as standing rules (rows above; `skills/governed-delivery/SKILL.md:106-110`; `06-repo/AGENTS.md:131-133`). The brief offers `Failure Conditions`, `Acceptance Criteria` and `Falsifiability` (`skills/reflective-brief/SKILL.md:34`), but no per-task not-evidence slot |
| Limit read scope; untrusted mailbox text can act as instructions | covered | `04-agent/runtime-trust-boundary.md:92`, `:97`; `skills/reflective-dispatch/SKILL.md:165` |
| Chat instruction versus permission removed in tool configuration | covered (aligned) | “prompt rules cannot isolate a sink; the host must” (`04-agent/runtime-trust-boundary.md:97`); `skills/reflective-risk/SKILL.md:42` |
| Irreversible send, delete or payment: draft first, then human confirmation | covered | Outward-action authorization gate (`skills/reflective-risk/SKILL.md:121`); must-approve classes (`skills/agent-governance-scaffold/SKILL.md:82`) |
| A notification calls the human back; it neither approves nor accepts | covered | Human Review is “Not a notification, not a courtesy CC” (`GLOSSARY.md:79-81`); “Closing execution is not closing acceptance” (`skills/governed-delivery/SKILL.md:106`) |
| Strongest model first on the most failure-prone class, then watch retries | qualified | A before/after retry count is at best directional: time, workload and model all change. TB-6 requires controlled task-cost/quality evidence before reopening (`skills/golden-benchmark-runner/SKILL.md:55-56`) |

### Local observations

Two same-week local events match the secondary's not-evidence items. On 2026-11-06, the coordinator's own [lieflat delivery receipt](../../review/final-report.md#lieflat-ai-tone-source-survey-publication-2026-11-06) asserted a clean result from a nonexistent `update_record_hygiene.py` before the hygiene check had run. It was published in `cea0f00` and corrected in `debd002`. During CP-DOC2, a delegated report stated an unverified inference as fact; coordinator re-verification refuted it before publication ([retained correction](agent-control-plane-comparison-survey-2026-11-04.md#executed-delta-probe)). Both breached existing rules—“Do not claim checks passed unless they were run and read” (`skills/reflective-implement/SKILL.md:43`; `06-repo/AGENTS.md:131-132`)—rather than exposing missing wording. A per-task not-evidence list would not have stopped a receipt written before its checks; the remedy is to derive the report from executed results, as `skills/reflective-implement/SKILL.md:113` already requires for `Acceptance Criteria Status`.

### Dispositions

| ID | Candidate | Disposition | Evidence / reopen trigger |
| --- | --- | --- | --- |
| TB-DOC2 | This dated follow-through, catalogue discovery and delivery report | **Adopted — reference documentation only** | Owner's survey request; the unchanged-primary recheck and secondary fidelity verdicts need a durable record |
| TB-8 | Per-task not-evidence slot in `reflective-brief` or the ticket template (the secondary's two lists) | Deferred | Standing rules already name the classes. Reopen if a local delegated task is accepted on a listed not-evidence item while its acceptance criteria are silent, or if the owner decides to add the slot |
| TB-9 | Special-case wording for pasted content presented as a file read | No change | Instance of `skills/reflective-dispatch/SKILL.md:48`, `06-repo/AGENTS.md:132` and the review Existence dimension; an external anecdote, not a missing local rule |
| TB-1–TB-7 | Earlier candidates | Unchanged | As recorded above |

### Falsifiability

- A different S2 digest or a modified secondary page invalidates the corresponding fidelity rows; re-check the new text instead of editing these results.
- An authenticated native-X body, or an author statement on A14/A15 conditions, could change the qualified verdicts.
- A local delegated task accepted on a declaration, an unopenable citation or self-review, while its brief was silent, reopens TB-8 as an in-place brief or template repair. A repeat of the receipt-ordering failure is a compliance problem for the existing rule, not by itself evidence for new wording.
