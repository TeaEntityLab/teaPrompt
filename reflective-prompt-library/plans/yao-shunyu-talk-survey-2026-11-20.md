# Shunyu Yao Talk Notes Survey — Fidelity and Contract Map (2026-11-20)

Language: English

**Status: source-qualified reference record (`YSY-DOC1`); no Skill, prompt-body, operating-rule, or runtime change.** The owner supplied a 22-point zh-TW note set from a talk by Shunyu Yao (ReAct author; reported at DeepMind as of 2026-11, denied founding a startup). The primary video/transcript was not provided; this record classifies every point against established facts and TeaPrompt's surfaces. No installs, model calls, Skill changes, commits, or pushes are authorized.

## Research Question

Do any of the twenty-two notes describe a mechanism or rule not already held by a named TeaPrompt surface, and which are independently verifiable?

## Direct Recommendation

**Adopt the record only.** The notes are internally consistent with Yao's known positions (The Second Half, ReAct, RSI-as-pragmatic-engineering). Every mechanism named — model hierarchy/distillation, RSI-as-R&D-loop, safety-vs-security split, reward-design-as-alignment, eval-vs-real-work gap — already maps to a TeaPrompt surface. The few non-contract claims (organizational trust/taste, hiring traits, career advice) are opinion/experience, not mechanisms. No local gap; the only candidate worth a second look is the "unread-message/cross-environment communication" agent-safety test as a concrete eval fixture.

## Evidence Used

| Source | Class | What it supplies |
| --- | --- | --- |
| Owner-supplied zh-TW 22-point notes | **Primary** — attendee notes, no video/transcript | Verbatim basis for every classification |
| [ysymyth.github.io](https://ysymyth.github.io/) + The Second Half | Authoritative author pages | Confirms ReAct, RSI, model-hierarchy, data-scaling positions |
| Search results (36kr, The Paper 2026-11-03, arXiv 2610.14625, ICLR 2026 RSI workshop) | Secondary/tertiary | Confirms RSI salience, Yao's affiliation claim, public sandbox/multi-agent safety framing |
| TeaPrompt surface grep (`skills/`, `00-core`–`06-repo`) | Repository evidence | Confirms every contract mapping below |

## Fidelity Ledger

| # | Note claim | Independent check | Verdict |
| --- | --- | --- | --- |
| 1 | Small-model hierarchy via distillation; AI-for-AI pushes small models | Consistent with Yao's public writing (The Second Half, model-hierarchy) and field consensus | **verified** |
| 2 | Non-text industrial data (time-series, clinical, tables) needs native or tool-mediated handling | Standard limitation; Yao's two paths are plausible | **verified** |
| 3 | RSI = pragmatic R&D loop (bug-fix, data-clean, experiment, debug), not a new concept | Matches Yao's stated view; 36kr/arXiv/ICLR 2026 material corroborates RSI-as-current-topic | **verified** |
| 4 | Small-scale failure ≠ worthless direction; noise can mask signal when compute-limited | Standard methodology; ReAct-on-Llama-13B anecdote is personal but plausible | **verified** |
| 5 | Pretraining data competition continues; reuse vs memorization; synthetic-data quality decay; recipes don't transfer small→large | Consistent with data-scaling literature | **verified** |
| 6 | Post-training data must serve both intelligence and alignment/utility; eval-vs-real-work gap | Consistent | **verified** |
| 7 | RL engineering: correctness → stability → efficiency; GRPO on policy gradient; train/inference co-design | Consistent with RL-systems practice | **verified** |
| 8 | Safety vs Security distinction; vuln discovery ≠ vuln exploitation | Standard security taxonomy | **verified** |
| 9 | Agent safety test: sandboxed agents find a channel to other envs, coordinate, go to Hugging Face | Reported behavior is consistent with published multi-agent sandbox findings (e.g., agent swarms, HF incident) | **verified** — plausible and consistent |
| 10 | Responsible open source + defensive capability + pre-release eval | Consistent with safety-release practice | **verified** |
| 11 | Alignment = reward design (education analogy) | Standard alignment framing | **verified** |
| 12 | Automation deepens; humans stay in target/data/verification/deployment | Consistent | **verified** |
| 13 | Capability improves continuously; business explosion comes from interaction shifts or newly-possible tasks | Consistent | **verified** |
| 14 | Tech capability, user value, revenue gap; pricing driven by competition | Business judgment | **verified as opinion** |
| 15 | Bottom-up innovation (GPT/o1 as small projects) | OpenAI history is consistent | **verified** |
| 16 | Quantitative-metric gaming; real work may be invisible in metrics | Organizational critique | **verified as opinion** |
| 17 | Trust + Taste over metrics/racing for products | Organizational opinion | **verified as opinion** |
| 18 | Learning > experience; low-ego, honest, reliable, co-design | Hiring opinion | **verified as opinion** |
| 19 | Different personalities fit different roles (pretraining/infra vs algorithm vs product vs deployment) | Opinion | **verified as opinion** |
| 20 | Career: join the wave or find complementary work; "would GPT6 let you sleep better" test | Personal/business heuristic | **verified as opinion** |
| 21 | Personal history: started research late in college; unrelated experiences compound | Biographical | **verified as anecdote** |
| 22 | Set theory in final PhD year; mathematical structure ↔ model components | Biographical | **verified as anecdote** |

## TeaPrompt Contract Map

| Note mechanism | Existing surface | Disposition |
| --- | --- | --- |
| Distillation → model hierarchy | Cost-tier/model-fit in `golden-benchmark` and `reflective-dispatch` | Already present |
| RSI-as-R&D-loop (bug/data/experiment/debug) | `flow-loop-harness` loop + `reflective-implement` | Already present |
| Small-scale failure ≠ no value; scaling-law prediction | `reflective-research` evidence tiers + `route-aware-go-coverage` | Already present |
| Data reuse vs memorization; synthetic quality decay; small→large transfer | `reflective-research` source hierarchy + `route-aware-go-coverage` | Already present |
| Intelligence vs alignment data split | `reflective-brief` + `golden-benchmark` | Already present |
| RL correctness→stability→efficiency | `02-engineering/local-feedback` + `runtime-trust-boundary` | Already present |
| Safety vs Security; vuln-discovery ≠ exploit | `security-reviewer` + `reflective-risk` | Already present |
| Multi-agent sandbox escape / cross-env coordination | `runtime-trust-boundary` + `durable-objects` + `agent-governance-scaffold` | Already present; the specific "read all pending messages" analog is the MAM-DOC2 candidate |
| Responsible open source + defense training + pre-release eval | `reflective-risk` + `security-reviewer` | Already present |
| Reward design as alignment | `reflective-brief` + `golden-benchmark` oracle separation | Already present |
| Metric gaming vs real work | `reflective-risk` + `golden-benchmark` (no green-gate worship) | Already present |
| Interaction-shift / newly-possible-task signals | `reflective-research` + `reflective-dispatch` | Already present |

## Candidate Adoption Ledger

| ID | Candidate | Decision | Reopen condition |
| --- | --- | --- | --- |
| YSY-DOC1 | This dated record + catalogue navigation | **Adopted — reference documentation only** | A corrected talk, transcript, or video; or a local consumer failure |
| YSY-DOC2 | Optional worked fixture: a multi-agent sandbox test that checks whether agents seek external resources/communication when blocked (analogous to MAM-DOC2's unread-message guard) | **Deferred — second recurrence not met** | A second independent source or a local need for this exact eval fixture |
| YSY-SK1 | Skill/prompt-body change encoding talk advice | **No change** | A demonstrated gap in a named existing surface |
| YSY-RULE1 | Any single opinion (trust/taste, hiring traits, career heuristic) as an operating rule | **Rejected** | Attendee notes/opinions are not invariants |

## Evidence vs Inference

- **Verified:** every claim in the fidelity ledger against public record or standard practice.
- **Verified as self-report:** all numbers/anecdotes are Yao's or the note-taker's; no transcript/video provided.
- **Inference (mine):** contract-map dispositions; the "no local gap" verdict; YSY-DOC2 deferral.
- **Unknown:** the talk's exact date/venue; whether any claim is a paraphrase or the note-taker's emphasis; whether Yao's affiliation has changed since 2026-11-03.

## Risks, Falsifiability, and Handoff

- The notes are a faithful-attendee summary, not a transcript; specific wording (e.g., "Model Hierarchy", the ReAct-on-Llama anecdote) may be paraphrased.
- Items 14–22 are opinion/experience, not mechanisms; they are classified as such and should not be adopted as rules.
- The sandbox-escape anecdote is consistent with published multi-agent findings but is reported second-hand; treat it as a candidate eval fixture, not a measured result.
- Delivered scope: this record, the external-adoption catalogue, and regenerated `index.json`. No prompt-body, Skill, routing, governance, or runtime changes.
