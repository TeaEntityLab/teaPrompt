# Goal Engineering Survey — Chase × Actively AI Article and Reader Comments (2026-11-15)
Language: English

> **Status: reference documentation and navigation adopted (`GE-DOC1/2`); no Skill, operating-rule, or runtime change.** The owner supplied a Chinese digest of the Goal Engineering discussion plus a summarized set of X comments, and asked for a survey. This record preserves the primary source, checks the digest's fidelity, and separates verifiable article claims from supplier-summarized comments. It does not authorize a new Skill, a scope rule, or any claim that goal engineering supersedes prompt/context work.

## Research Question and Direct Recommendation

Does the Goal Engineering article — and the comment refinements summarized in the supplied digest — expose a missing delivered TeaPrompt contract?

**Record the source-qualified map; leave Skills unchanged.** The core heuristic (scope agents around what is easiest to give feedback on) is new as an explicit rule but already expressed inside existing contracts. The strongest attributed comment refinement — Kaya's "the same kind of judgment each time" (unverified summary) — is a candidate hypothesis for scope splits, recorded here as a transfer test rather than wired into a Skill as a criterion: the informative signal is whether a persisted correction reuses correctly on a comparable later item, while recurrence frequency alone, high or low, is inconclusive. One headline claim is narrower than the digest suggests.

## Version and Source Identity

Checked 2026-11-15.

| Item | Identity | Reuse / accuracy boundary |
| --- | --- | --- |
| [LangChain blog: “Goal Engineering: How to Design Goals”](https://www.langchain.com/blog/goal-engineering) | Harrison Chase, Mihir Garimella (Actively AI), Anshul Gupta (Actively AI); published 2026-11-14, last-modified 2026-11-15T08:15:16Z. Fetched body SHA-256 `d68c7906…ee254c`. | Primary source; vendor-published, Actively AI is a co-author with a product interest. |
| [Harrison Chase X post](https://x.com/hwchase17/status/2121635683999883577) | Announcement thread; a second post adds "design goals around what you can give feedback on more easily". | og:tags readable; comment bodies behind login — not fetched. |
| Supplied zh digest + comment summary (owner-provided) | Covers @Xudong07452910's reading plus attributed comments from @jacksunny18 (Kaya), @KevinWeb3Nomad, @raysnote, @open_is_free, @JTL19971224, @cybersec, @GuyGoldenberg, @KimYx0207. | **Unverified paraphrase.** Handles exist (@jacksunny18 is a real, substantive technical account); the specific quoted replies were not independently confirmed. Treated as leads, not evidence. |

No upstream code or prompt body is copied into TeaPrompt's operational assets.

## Fidelity Check: Digest vs Primary Article

| Digest claim | Article text | Verdict |
| --- | --- | --- |
| 核心價值：design scope so feedback is easiest to give; unwritten tacit knowledge is the hard part | "design the scope of an agent such that it makes it as easy as possible to give feedback"; trickiest context "is not written down anywhere already" | faithful |
| 戰略：account-agent → motion-agent split; reviewer batches similar tasks; feedback transfers across accounts | Actively case study, same story; motion = "a particular job to be done … like outbounding or early-stage deal progression" | faithful |
| 整體：「Goal Engineering 將取代 Prompt 與 Context Engineering」 | "**Prompt engineering and context engineering will disappear, but goal engineering will remain.**" | overstated: the article predicts the job titles/layers disappear as separate concerns while goal design remains — the digest's 「取代」 reads stronger than the original's framing; Kaya's comment (they become downstream artifacts of the goal) is closer to the spirit |
| Missing from digest | Account context "is often already written down and much more objective"; context-gathering agents still assemble it; motions pull account context as needed | omission retained here — this is exactly the tacit-vs-written split the digest compresses |
| Missing from digest | "Invest a lot in an intuitive and delightful UX for reviewing agent work" | omission — the review-UX investment is half the article's practical advice |

## Comment Refinements (as supplied; unverified but coherent)

| Attributed comment | Content | Assessment |
| --- | --- | --- |
| @jacksunny18 (Kaya) | Scope quality ≠ ease of feedback; = **same judgment each time**. Measurable: ratio of repeated correction sentences per reviewer over a week; high repeat = scope right, low = model quality. Motion split **relocates** cross-account inconsistency; needs a cross-motion account identity. Boundary test: "does moving an item from A to B need judgment or just lookup?" If judgment → don't split. Prompt/context titles become downstream of the goal. | Strongest refinement; consistent with the article, proposes a reuse test and names a failure mode — but frequency alone is inconclusive: low repeat may mean the first correction already worked, so only reuse on a comparable later item is informative |
| @KevinWeb3Nomad | Each stage needs "what it may do and when to pause for confirmation" | Matches existing Human Review trigger pattern |
| @raysnote | Keep an ADR per scope/goal split (goal + trade-off) | Matches the repo's own record discipline |
| @open_is_free | Tacit judgments (brand voice, sales aggression) are the hardest to calibrate | Restates article's point |
| @JTL19971224 | Granularity question: how fine should goals be? | Open question; Kaya's comment proposes a reuse test for it — frequency alone, including low, is inconclusive |
| @cybersec/@GuyGoldenberg | Explicit stop conditions to prevent false positives / infinite loops | Already covered by loop-harness budgets |
| @KimYx0207 | Batch same-type work for review, but annotate the applicability range of feedback | Sound caveat: reused feedback without a stated scope over-generalizes |

## What the Source Adds vs Existing Contracts

| Idea | Existing TeaPrompt coverage | Gap? |
| --- | --- | --- |
| Scope the agent around feedback ease | `reflective-brief` "Scope split" + in/out; `reflective-dispatch` task classification | Partial — no stated **transfer test** for a good split; Kaya's reuse-after-correction hypothesis and judgment-vs-lookup boundary question are candidates, recorded not adopted |
| Tacit knowledge extracted via repeated human feedback | `flow-loop-harness` human-verifier pattern; `reflective-review` adjudication | None |
| Review UX as the bottleneck investment | None (host/product concern) | Host scope, not a Skill gap |
| Motion-vs-account split; cross-motion identity | `03-context/context-handoff` continuity guidance (library); identity enforcement is a host-runtime concern — no shipped `durable-objects` Skill in the git tree/registry | None — same problem class; host identity is not a Skill gap |
| ADR for goal boundaries | Repo convention: adoption ledgers, survey records, `docs/retrospective/06-action-register.md` | None — practiced |
| Stop conditions | `flow-loop-harness` MAX_ITER/verifier; `reflective-risk` gates | None |
| "Pause and ask" points | `reflective-brief` Human Review triggers; missing-data audit | None |
| Goal > context > prompt layering | Library's own ordering: classify → strictness → compose smallest prompt (teaprompt-primer) | Consistent; the "disappear" claim stays a prediction, not a rule |

## Optional Worked Reference — Scope by Reusable Judgment

Actively's co-authors describe two ways they assigned work and what happened to reviewer feedback:

- **v1 — one agent per account** failed not because account context was wrong, but because a reviewer could not give *reusable* feedback: each review was one-off account judgment.
- **v2 — one agent per motion** grouped similar tasks under one reviewer; one correction ("how aggressive to outbound") applied across every account the motion touched.

The supplied comment summary attributes this question to Kaya: does moving an item require fresh *judgment*, or just a *lookup*? The reply itself was not verified. One way to test the idea is to record a correction, then see whether a reviewer can apply it correctly to the next comparable item. Repeated corrections might mean earlier feedback did not stick; a single correction might have worked. The count alone does not decide where to split the work.

This is a source-qualified example, not a measured result: Actively's outcome is author-reported by a co-author with a product interest, and the comment refinements are unverified summaries.

## Candidate Adoption Ledger

| ID | Candidate | Disposition | Evidence / reopen trigger |
| --- | --- | --- | --- |
| GE-DOC1 | This source-bound record and its catalogue row | Adopted; documentation only | Owner asked to survey the digest. Refresh if the article is revised or the comment thread becomes independently readable. |
| GE-DOC2 | Optional worked-reference link appended under `workflow-acquisition.md`'s Optional Worked Reference section, outside its prompt fence | Adopted; navigation only | Keeps the scope-by-reusable-judgment hypothesis discoverable as a transfer test, without changing the prompt's output contract. |
| GE-SK1 | New Skill or edits to `reflective-brief` scope criteria | No change | The hypothesis is a one-paragraph proposal without measured backing; a reuse-on-comparable-item transfer test would be needed first. |
| GE-RUN1 | Any runtime, UX investment, or vendor tooling | Not adopted | Source is an essay + comments; nothing to run. |
| GE-RULE1 | Adopt "goal engineering replaces prompt/context engineering" or motion-splits as a rule | Rejected | Original says the layers become downstream of goals, not that they stop mattering; motion-split is one company's fit, not a universal scope rule (and Kaya shows its relocated failure mode). |

## Falsifiability

- A transfer test showing whether a persisted correction under TeaPrompt's current scope-split guidance reuses correctly on comparable later items would reopen GE-SK1. A bare repeat-correction frequency — low or otherwise — would not: low frequency may mean the first correction already fixed the scope.
- If the comment summary proves fabricated (X thread readable and shows no such replies), the comment table is corrected but the article-level dispositions stand.
- Author-product interest (Actively AI co-authored) is retained as a qualifier, not a disqualifier.

## Standing Non-Goals

No Skill edit, no prompt edit beyond the cited surface, no scope rule, no model call, no efficacy claim about goal engineering. Comment attributions stay unverified. Commit/push remain unperformed pending owner direction.
