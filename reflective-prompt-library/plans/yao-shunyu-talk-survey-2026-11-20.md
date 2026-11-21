# Shunyu Yao Attributed-Talk Notes Survey — Fidelity and Contract Map (2026-11-20)

Language: English

> **Status:** source-qualified reference record (`YSY-DOC1`); no Skill, prompt-body, operating-rule, or runtime change. The owner supplied a 22-point zh-TW attendee note set attributed to a talk by Shunyu Yao (ReAct authorship confirmed via author pages; DeepMind affiliation and startup-founding denial as reported in November 2026 coverage). No video or transcript was provided, so this record establishes the note text as recorded, checks it against independently checkable background, and leaves speaker attribution, wording fidelity, and incident truth unverified. No installs, model calls, Skill changes, commits, or pushes are authorized.

## Research Question

Do any of the twenty-two note items describe a mechanism or rule not already held by a named TeaPrompt surface, and for each item, which layer is established: the text as recorded, speaker attribution, background plausibility, or incident truth?

## Direct Recommendation

**Adopt the record only.** Read strictly as an attendee record: the note text is compatible with Yao's published positions (The Second Half, ReAct, RSI-as-pragmatic-engineering), but without a video or transcript neither speaker attribution nor wording fidelity is verified. Every mechanism the notes name — model hierarchy/distillation, RSI-as-R&D-loop, safety-vs-security split, reward-design-as-alignment, eval-vs-real-work gap — maps at method level to a TeaPrompt surface. The few non-contract claims (organizational trust/taste, hiring traits, career advice) are recorded as attributed opinion/experience, not mechanisms. No local gap; the only candidate worth a second look is the "unread-message/cross-environment communication" agent-safety test as a concrete eval fixture — deferred, since the second-hand anecdote does not verify the behavior.

## Evidence Used

| Source | Class | What it supplies |
| --- | --- | --- |
| Owner-supplied zh-TW 22-point notes | **Record basis** — attendee notes, no video/transcript | Establishes what the notes say, not who said it or whether it happened |
| [ysymyth.github.io](https://ysymyth.github.io/) + The Second Half | Authoritative author pages | Confirms ReAct authorship and published positions on RSI, model hierarchy, and data scaling (background only) |
| Search results (36kr, The Paper 2026-11-03, arXiv 2610.14625, ICLR 2026 RSI workshop) | Secondary/tertiary | Reports RSI salience and Yao's affiliation claim; records public sandbox/multi-agent safety framing as background, not the note-9 incident itself |
| TeaPrompt surface grep (`skills/`, `00-core`–`06-repo`) | Repository evidence | Locates the cited surfaces for the mappings below; dispositions remain inference |

## Consistency Ledger

The 22 rows report what the attendee wrote. “Background consistent” means other material is compatible with the note; it does not confirm the speaker's words or that an incident happened. No recording or transcript was available to check attribution.

| # | Note claim (as recorded) | Background check | Verdict |
| --- | --- | --- | --- |
| 1 | Small-model hierarchy via distillation; AI-for-AI pushes small models | Consistent with Yao's public writing (The Second Half, model-hierarchy) and field consensus | **recorded; background consistent** |
| 2 | Non-text industrial data (time-series, clinical, tables) needs native or tool-mediated handling | Standard limitation; the two paths are plausible as positions | **recorded; background consistent** |
| 3 | RSI = pragmatic R&D loop (bug-fix, data-clean, experiment, debug), not a new concept | Matches Yao's published view; 36kr/arXiv/ICLR 2026 material corroborates RSI-as-current-topic | **recorded; background consistent** |
| 4 | Small-scale failure ≠ worthless direction; noise can mask signal when compute-limited | Standard methodology; the ReAct-on-Llama-13B anecdote is unattested beyond the notes | **recorded; background consistent; anecdote unverified** |
| 5 | Pretraining data competition continues; reuse vs memorization; synthetic-data quality decay; recipes don't transfer small→large | Consistent with data-scaling literature | **recorded; background consistent** |
| 6 | Post-training data must serve both intelligence and alignment/utility; eval-vs-real-work gap | Consistent | **recorded; background consistent** |
| 7 | RL engineering: correctness → stability → efficiency; GRPO on policy gradient; train/inference co-design | Consistent with RL-systems practice | **recorded; background consistent** |
| 8 | Safety vs Security distinction; vuln discovery ≠ vuln exploitation | Standard security taxonomy | **recorded; background consistent** |
| 9 | Agent safety test: sandboxed agents find a channel to other envs, coordinate, go to Hugging Face | Consistent with published multi-agent sandbox findings (background only — e.g., agent swarms, HF incident) | **recorded; incident unverified** — background consistency does not verify the reported behavior |
| 10 | Responsible open source + defensive capability + pre-release eval | Consistent with safety-release practice | **recorded; background consistent** |
| 11 | Alignment = reward design (education analogy) | Standard alignment framing | **recorded; background consistent** |
| 12 | Automation deepens; humans stay in target/data/verification/deployment | Consistent | **recorded; background consistent** |
| 13 | Capability improves continuously; business explosion comes from interaction shifts or newly-possible tasks | Consistent | **recorded; background consistent** |
| 14 | Tech capability, user value, revenue gap; pricing driven by competition | Business judgment, recorded as stated | **recorded as attributed opinion** |
| 15 | Bottom-up innovation (GPT/o1 as small projects) | OpenAI history is consistent | **recorded; background consistent** |
| 16 | Quantitative-metric gaming; real work may be invisible in metrics | Organizational critique, recorded as stated | **recorded as attributed opinion** |
| 17 | Trust + Taste over metrics/racing for products | Organizational opinion, recorded as stated | **recorded as attributed opinion** |
| 18 | Learning > experience; low-ego, honest, reliable, co-design | Hiring opinion, recorded as stated | **recorded as attributed opinion** |
| 19 | Different personalities fit different roles (pretraining/infra vs algorithm vs product vs deployment) | Opinion, recorded as stated | **recorded as attributed opinion** |
| 20 | Career: join the wave or find complementary work; "would GPT6 let you sleep better" test | Personal/business heuristic, recorded as stated | **recorded as attributed opinion** |
| 21 | Personal history: started research late in college; unrelated experiences compound | Biographical as recorded; not independently checked | **recorded as attributed self-report** — attribution and factual accuracy unverified |
| 22 | Set theory in final PhD year; mathematical structure ↔ model components | Biographical as recorded; not independently checked | **recorded as attributed self-report** — attribution and factual accuracy unverified |

## TeaPrompt Contract Map

| Note mechanism | Existing surface | Disposition |
| --- | --- | --- |
| Distillation → model hierarchy | `reflective-dispatch` considers cost and task fit when choosing a workflow | An analogy about resource use, not guidance for training or distilling models |
| RSI-as-R&D-loop (bug/data/experiment/debug) | `flow-loop-harness` loop + `reflective-implement` | Already present |
| Small-scale failure ≠ no value; noise-vs-signal reading of small runs | `reflective-research` (repo-owned: State Ledger statuses, source map, `verified`-only-after-upstream-check) | Already present as general research method; local ML-training scaling prediction is not a TeaPrompt contract |
| Training-data regimes: reuse vs memorization; synthetic quality decay; small→large transfer | `reflective-research` (repo-owned: source-backed claims, ledger auditability — cited-source handling, not training runs) | Already present for cited-source handling only; ML training-data regimes are not a TeaPrompt contract, and `route-aware-go-coverage` (a host-managed Go test-coverage skill) does not cover them |
| Intelligence vs alignment data | `reflective-brief` separates the intended outcome from how to measure it | Related question; no training-data split is specified |
| RL correctness → stability → efficiency | [Local Feedback](../02-engineering/local-feedback.md) asks for a failure, correction and verification | A debugging analogy, not a validated ordering for RL training |
| Safety vs security | `reflective-risk` identifies security-sensitive work and its Human Review requirements | A risk-review method, not a shipped security-review agent |
| Multi-agent sandbox escape / cross-env coordination (second-hand anecdote) | `04-agent/runtime-trust-boundary.md` tool/action gates + `agent-governance-scaffold` (repo-owned: authority split, approval gates, broker-receipt/acceptance contract templates — templates only, host enforces) | Method-level analog only; the unverified anecdote neither verifies the behavior nor establishes the MAM-DOC2 unread-message guard, which needs its own evidence; no per-user consent or execution shown |
| Responsible release, defense training and pre-release evaluation | `reflective-risk` identifies who must review security-sensitive changes | Review guidance, not a defense-training or release service |
| Reward design as alignment | `reflective-brief` distinguishes the intended outcome from its acceptance criteria | An analogy; good acceptance criteria are not proof of model alignment |
| Metric gaming vs real work | `golden-benchmark-runner` separates a scored result from evidence of an improvement | A measurement check, not evidence about the talk |
| Interaction-shift / newly-possible-task signals | `reflective-research` + `reflective-dispatch` | Already present |

## Candidate Adoption Ledger

| ID | Candidate | Decision | Reopen condition |
| --- | --- | --- | --- |
| YSY-DOC1 | This dated record + catalogue navigation | **Adopted — reference documentation only** | A corrected talk, transcript, or video; or a local consumer failure |
| YSY-DOC2 | Optional evaluation fixture for the reported cross-environment behavior | **Deferred** | A source that independently documents that behavior, or a local need to evaluate it. MAM's read-before-checkout guard tests a different precondition and does not establish this incident. |
| YSY-SK1 | Skill/prompt-body change encoding talk advice | **No change** | A demonstrated gap in a named existing surface |
| YSY-RULE1 | Any single opinion (trust/taste, hiring traits, career heuristic) as an operating rule | **Rejected** | Attendee notes/opinions are not invariants |

## Evidence vs Inference

- **Recorded (note text):** all 22 items as the owner-supplied notes state them.
- **Verified (background):** ReAct authorship and the cited published positions (author pages); compatibility with standard practice where the ledger cites it. Neither layer verifies speaker attribution, wording fidelity, or incident truth.
- **Recorded as attributed self-report (attribution unverified):** numbers and anecdotes appear in the notes as the speaker's words or experience; without a video/transcript it is unverified whether Yao said them, whether wording is paraphrased, or where the note-taker added emphasis.
- **Inference (mine):** contract-map dispositions; the "no local gap" verdict; YSY-DOC2 deferral.
- **Unknown:** the talk's exact date/venue; whether any claim is a paraphrase or the note-taker's emphasis; whether Yao's affiliation has changed since 2026-11-03; whether the note-9 sandbox behavior occurred as described.

## Falsifiability, Risks, and Handoff

- The notes are an attendee summary of unknown fidelity, not a transcript; specific wording (e.g., "Model Hierarchy", the ReAct-on-Llama anecdote) may be paraphrased, and speaker attribution for every item is unverified.
- Items 14–22 are opinion/experience, not mechanisms; they are classified as such and should not be adopted as rules.
- The sandbox-escape anecdote is second-hand and unverified as an incident; consistency with published multi-agent findings is background compatibility, not confirmation. Treat it as a deferred eval-fixture candidate (YSY-DOC2), not a measured result — and not as evidence establishing MAM-DOC2's unread-message guard.
- Delivered scope: this record, the external-adoption catalogue, and regenerated `index.json`. No prompt-body, Skill, routing, governance, or runtime changes.
