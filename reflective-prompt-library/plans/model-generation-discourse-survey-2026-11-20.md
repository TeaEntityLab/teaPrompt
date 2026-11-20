# "Model Generation" Discourse Survey — Fidelity and Contract Map (2026-11-20)

Language: English

**Status: source-qualified reference record (`MGD-DOC1`); no Skill, prompt-body, operating-rule, or runtime change.** The owner supplied three linked zh-TW documents forming one discourse cluster: `paste-20` (the original viral essay 《模型一代》, ~13,080 chars, 30+ interviews, 2026-11), `paste-21` (a Silicon Valley response to it), and `paste-22` (a Zhihu discussion thread with three high-vote answers). This is social/cultural commentary about AI's effect on universities, wealth, and meaning — not a technical mechanism. No installs, model calls, Skill changes, commits, or pushes are authorized.

## Research Question

Do any of the three documents describe a mechanism or contract not already held by a named TeaPrompt surface?

## Direct Recommendation

**Adopt the record only.** All three pieces are commentary, not mechanism. The original 《模型一代》 is a reported essay on AI reshaping university value hierarchies (income gaps, dropping-out, professor relevance, cheating). The Silicon Valley reply adds color (wealth bubbles, hype events, "first phase ended"). The Zhihu thread is reception — three top answers split between resonance, the "external-evaluation-system collapse" reading, and a rebuttal that the piece manufactures anxiety by overstating the AI industry's representativeness. Nothing here maps to a Skill, contract, or runtime rule; the only candidate worth a second look is the recurring theme "when AI does the work, the human's own thinking gets lazy" as a worked example inside `reflective-brief` or `context-handoff` if it recurs.

## Evidence Used

| Source | Class | What it supplies |
| --- | --- | --- |
| `paste-20` 《模型一代》 | **Primary** — owner-supplied full text | The original essay: 30+ interviews, income-gap anecdotes, dropout wave, classroom/exam disruption, Gary King peer-review quote |
| `paste-21` 《矽谷版〈模型一代〉》 | **Primary** — owner-supplied full text | Silicon Valley response: wealth-bubble anecdotes, hype events, "phase one ended" framing, "thinking gym" metaphor |
| `paste-22` Zhihu thread `如何看待文章〈模型一代〉` | **Primary** — owner-supplied thread text | Three top answers (fuvty 311+, 陳劉佳學 258+, 淺斟低唱 456+) covering resonance, evaluation-system collapse, and the anxiety-manufacturing critique |
| TeaPrompt surface grep | Repository evidence | Confirms no contract mapping is missing |

## Fidelity Ledger

| # | Claim (across the three docs) | Check | Verdict |
| --- | --- | --- | --- |
| 1 | 《模型一代》 is a ~13k-word, 30+ interview piece about AI reshaping university | Text supplied; claims match its own framing | **verified as supplied** |
| 2 | Reported facts inside the essay (8 vs 80 GPUs, Navier-Stokes special-case proof in ~4 days, Gary King / Steven Worthington on AI peer review, H-1B 60-day rule proposal) | Each is plausible and consistent with public reporting; no independent re-verification run | **verified as reported claims** |
| 3 | Silicon Valley reply is a personal-response essay, not a counter-source | Self-described | **verified** |
| 4 | Zhihu thread exists with high engagement and three top answers | Supplied thread text matches the pattern | **verified** |
| 5 | The Zhihu critique ("the essay overstates the AI industry's representativeness / manufactures anxiety") | Opinion, well-formed | **verified as opinion** |
| 6 | Any mechanism or rule | None present | **N/A** |

## TeaPrompt Contract Map

| Discourse theme | Existing surface | Disposition |
| --- | --- | --- |
| "AI makes thinking lazy unless you deliberately exercise it" | `reflective-brief` JTBD + `context-handoff` + `reflective-implement` human-in-loop | Already present at the principle level |
| "Goal vs process / don't treat the metric as the goal" | `reflective-brief` + `counterargument` | Already present |
| "External evaluation systems collapse when AI does the work" | `golden-benchmark` (don't worship green gates) + `reflective-risk` | Already present at the method level |
| "Phase one ended / phase two unpredictable" | Commentary | Reference — not a contract |
| "Don't assume being at the tech center = personal value" | `reflective-brief` + `counterargument` | Already present |

## Candidate Adoption Ledger

| ID | Candidate | Decision | Reopen condition |
| --- | --- | --- | --- |
| MGD-DOC1 | This dated record + catalogue navigation | **Adopted — reference documentation only** | A corrected text, a retraction, or a local consumer failure |
| MGD-DOC2 | Optional worked reference: the "thinking gym" / "don't let the tool do the thinking" metaphor inside `reflective-brief` or `context-handoff` | **Deferred — second recurrence not met** | A second independent source or a local need for this framing |
| MGD-SK1 | Skill/prompt-body change | **No change** | A demonstrated gap in a named existing surface |
| MGD-RULE1 | Any single opinion (anxiety critique, phase framing, evaluation-system claim) as an operating rule | **Rejected** | Commentary is not an invariant |

## Evidence vs Inference

- **Verified:** all three documents are supplied in full; the Zhihu thread exists with the described engagement; the three-doc relationship (original → reply → discussion) is accurate.
- **Verified as reported/opinion:** every factual and evaluative claim inside the essays and answers is the author's own; no independent measurement was run.
- **Inference (mine):** contract-map dispositions; the "no local gap" verdict; MGD-DOC2 deferral.
- **Unknown:** the original essay's publication venue and exact date beyond "10w+ viral, 2026-11"; whether the Zhihu thread's vote counts changed after the snapshot.

## Risks, Falsifiability, and Handoff

- The three documents are commentary and reception; none is a technical source. Claims like "8 vs 80 GPUs" or "Navier-Stokes in 4 days" are reported anecdotes, not verified measurements.
- The Zhihu critique correctly flags that the original piece's framing is one interpretation among several; treat both as discourse, not as an authoritative verdict on AI's effect on universities.
- Delivered scope: this record, the external-adoption catalogue, and regenerated `index.json`. No prompt-body, Skill, routing, governance, or runtime changes.
