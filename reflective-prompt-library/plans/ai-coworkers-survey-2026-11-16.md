# AI Coworkers Survey — YC Light Cone: Lauren Tan × Roman Ugarte (2026-11-16)
Language: English

> **Status: reference documentation and navigation adopted (`AIC-DOC1/2`); no Skill, operating-rule, or runtime change.** The owner supplied a structured zh-TW digest of the one-hour interview and asked for a survey. This record preserves the source chain, checks the digest against three independent secondary write-ups plus quoted transcript fragments, and maps the claims to existing TeaPrompt contracts. It does not authorize a new Skill, a permission model, or product adoption.

## Research Question and Direct Recommendation

Does the AI-coworker interview — trust ladder, outer-loop bots, everything-factory ambition — expose a missing delivered TeaPrompt contract beyond what the prior [trust-pyramid record](agent-trust-pyramid-survey-2026-11-15.md) already covered?

**Record the source-qualified map; leave Skills unchanged.** The trust ladder is the existing graduated-authority principle restated for non-coding domains; the outer loop and org model are host/product concerns; the one genuinely new recorded nuance is that adversarial multi-model review **overfits without product intent** — a caveat that matches the library's existing skepticism of review theatre. The source itself supplies the strongest counter-claim: outcome-owning bots are "still quite far away."

## Version and Source Identity

Checked 2026-11-16. The caption track could not be fetched directly (YouTube PO-token gate; mirrors behind Cloudflare). Fidelity below is established by triangulating three independent write-ups plus verbatim quotes they preserve.

| Item | Identity | Reuse / accuracy boundary |
| --- | --- | --- |
| [Y Combinator / The Light Cone: "The Rise Of AI Coworkers"](https://www.youtube.com/watch?v=y1-9yeYLJUo) | Garry Tan hosts Lauren Tan + Roman Ugarte (Grok Bot team, SpaceX SI); published 2026-11-14; 1 hr. | Primary source; full transcript not machine-fetched — see limits. |
| [Teamday write-up](https://www.teamday.ai/ai/roman-ugarte-lauren-tan-grok-bot-ai-coworkers-trust-ladder) | Independent summary with verbatim quotes ("still quite far away", credential-scoping quote, 200-message Slack demo). | Secondary; wording preserved where quoted. |
| [Newsfilter interview brief](https://newsfilter.io/interviews/the-rise-of-ai-coworkers-3f5fea27d6505e63a509511d7066be99) | Structured brief: identities incl. phone numbers/credit cards, 7-week build, trust ladder, org model, Quartermaster, Moltbook, abliterated models. | Secondary aggregator. |
| [Followed episode page](https://usefollowed.com/episodes/y-combinator-the-rise-of-ai-coworkers) | Timestamped mentions: GrokBot 1:09, ads logins 4:21, Quartermaster 17:03, Moltbook 18:58, abliterated models 20:33, Cappy 29:07, Slack 32:50. | Confirms segment topics and speakers. |
| [ZeroNoise brief](https://zeronoise.ai/posts/grockbots-ai-teammate-bet-and-dan-shay-on-why-success-never-feels-like-enough-yhe5npbpxapojy2t) | Independent notes: 3 principles, trust ladder, CPU-trace loop, lint-over-review, dogfood/PMF gate, "when execution is cheap, the failure is probably not execution". | Secondary. |
| Supplied zh-TW digest (owner-provided) | Structured summary incl. Socratic critique section. | Digest claims below checked against the above; its critique section is the digest author's own analysis, marked as such. |

Name variants retained, not reconciled: "Grok Bot" / "Grokbot" / "Grockbot" all circulate; "P-Stack"/"pstack" (open-source engineering-skills pack, inspired by "G-Stack"). "Databot" and "Sandy" are product/bot names reported by secondaries; "Potato" is Tan's own engineering bot.

## Fidelity Check: Digest vs Independent Sources

| Digest claim | Independent sources | Verdict |
| --- | --- | --- |
| Grokbot, first line → launch in ~7 weeks | Teamday, newsfilter, zeronoise | faithful |
| Bot-centric primitive: identities, own computer, phone, credit card; always-on proactive | newsfilter ("telephone numbers, credit cards"), teamday (3 principles), zeronoise | faithful |
| Outer loop: bots live in Slack/X where work happens; kills copy-paste friction | Followed quote at 32:50 ("ergonomic to just add the bot in the Slack thread"); zeronoise | faithful |
| Trust ladder: read-only (Databot on warehouse in Slack) → end-to-end (support bot reproduces issues, takes tickets) → outcome ownership (marketing bot w/ ads logins + budget, A/B tests with design bot) | Teamday (three steps + "still quite far away"), zeronoise, newsfilter | faithful, incl. the caveat |
| Inverse pyramid: refactor/static analysis/lint > AGENTS.md/skills > minimal review | zeronoise ("refactoring, static analysis and lint rules … adversarial multi-model review can overfit"), matches [ATP talk](agent-trust-pyramid-survey-2026-11-15.md) | faithful |
| Electron main↔renderer lint rule via dependency-graph checker | zeronoise, ATP transcript | faithful |
| ~4,000 PRs/month personal; overnight auto-fix loops for low-risk bugs only | teamday ("merges about 4,000"), zeronoise ("small bugs … ship overnight"; UX changes dogfooded; no internal PMF → no ship) | faithful, with the low-risk bound preserved |
| Owner/Manager/Collaborator team bots; hire-like-a-person credential scoping | teamday (quote + "team bots launched ~2 weeks earlier"), newsfilter (Quartermaster) | faithful |
| IC / DRI / player-coach org model | newsfilter | faithful |
| Execution→intent bottleneck; objective function/KPI; "Frankensteiny" product risk | zeronoise, teamday (bottleneck = agreeing what the product should be) | faithful |
| "Zero EQ": bot doesn't know who to listen to in group threads | teamday verbatim | faithful |
| Pstack/Gstack skills; Cappy (Garry Tan's factory, captain over 10–15 threads learning preferences from transcripts); Quartermaster; Moltbook ("5% eerie"); abliterated models | newsfilter, Followed timestamps, zeronoise | faithful |
| CPU traces / app-run self-verification loop | zeronoise | faithful |
| Digest's critique: compiler exists for code but not for marketing (verifiability gap) | Consistent with the source's own step-3 caveat; the explicit framing is the digest's analysis | digest-authored inference — sound, labeled |
| Digest's "unlimited-token" critique | Not addressed in source; plausible environment qualifier | digest-authored inference — retained, flagged |
| Digest's prompt-injection / irreversible-write risk | Source acknowledges abliterated-model risk + explicit visible channels + read-before-write; the catastrophic scenario framing is the digest's | digest-authored inference — retained, flagged |
| "Sandy" feedback pipeline name | Pipeline confirmed ("thousands of pieces of customer feedback a day"); the name appears in secondaries inconsistently | name retained as reported, unverified |
| Digest self-check "未引用時間戳記" — timestamps exist in Followed | — | neutral |

## What the Source Adds vs Existing Contracts

| Idea | Existing TeaPrompt coverage | Gap? |
| --- | --- | --- |
| Trust ladder read→act→own = graduated authority | `agent-governance-scaffold` approval tiers; `reflective-risk` gates; same "earned autonomy" as [ATP auto-merge](agent-trust-pyramid-survey-2026-11-15.md) | None — principle extended to non-code domains |
| Credential scoping "like onboarding a person" | `agent-governance-scaffold` named-accountability + issued-out-of-band approvals | None |
| Outer loop: deploy bots where work already happens | Host/product deployment decision | None — out of prompt scope |
| Adversarial multi-model review overfits without product intent | [Parallel Lens Review](../04-agent/workflow-recipes.md#parallel-lens-review) has reviewers share the question and evidence; the host decides how to run them | A review caveat, not evidence that extra models recover missing intent |
| Everything-factory boundary: verifiable vs subjective work | `reflective-risk` Human Review triggers; `reflective-brief` falsifiability requirement | None — source's own step-3 caveat is the contract |
| Zero-EQ social arbitration in group threads | None — open industry problem; no contract claims to solve it | Honest shared gap, recorded |
| Intent/alignment becomes the bottleneck when execution is cheap | `reflective-brief` JTBD; [GE scope-by-reusable-judgment](goal-engineering-survey-2026-11-15.md) | None — third independent restatement this week |
| Overnight auto-fix loops bounded to low-risk surface, dogfood+PMF gate for UX | `flow-loop-harness` bounded autonomy + `reflective-risk` high-risk lane | None — same partitioning |

## Optional Worked Reference — The Trust Ladder Is the Promotion Gate

The interview restates the promotion gate in identity terms: a bot earns the next rung only after the previous one produced evidence.

- **Read-only** (Databot answering analytics in Slack) builds the shared vocabulary and the review record — the equivalent of a replay plan before promotion.
- **End-to-end action** (support bot reproducing and resolving a ticket) is permitted only inside a bounded surface — low-risk bugs auto-merge; UX changes are dogfooded and require internal product-market fit.
- **Outcome ownership** (a bot with its own ad account and budget) is named as "still quite far away" — the authors do not pretend the ladder is climbed.

Applied to the library: `agent-governance-scaffold`'s approval tiers and `reflective-risk`'s gates already require exactly this graduated evidence; `runtime-trust-boundary` keeps write authority behind checks. The source adds one concrete calibration worth keeping: **the rung a bot holds should match the verifiability of its domain** — code has CI; marketing has no compiler, so marketing bots sit lower on the ladder by necessity, not by caution.

This is a source-qualified example from the product's own builders (a YC-backed launch narrative), not independent telemetry.

## Candidate Adoption Ledger

| ID | Candidate | Disposition | Evidence / reopen trigger |
| --- | --- | --- | --- |
| AIC-DOC1 | This source-bound record and its catalogue row | Adopted; documentation only | Owner asked to survey the digest. Refresh when a readable full transcript appears or the product's public docs change. |
| AIC-DOC2 | Optional worked-reference link appended under `runtime-trust-boundary.md`'s Optional Worked Reference section, outside its prompt fence | Adopted; navigation only | Keeps the ladder/verifiability calibration discoverable without changing the prompt contract. |
| AIC-SK1 | New Skill or edits encoding the trust ladder | No change | Graduated authority is already the governance/risk contract; the ladder is a restatement, not a new rule. |
| AIC-RUN1 | Adopt Grokbot / team-bot deployment or the Cappy-style transcript-learning factory | Not adopted | Product/host decision; nothing to copy into the library. Transcript-learned preferences raise the same provenance questions the boundary prompt already covers. |
| AIC-RULE1 | Promote "everything factory" or bot-per-domain org model as a rule | Rejected | Authors themselves bound it ("still quite far away"; no compiler for subjective work); adopting it would overclaim. |

## Evidence vs Inference

- **Verified (triangulated):** digest claims checked against three independent secondary write-ups plus quoted transcript fragments — launch timing, bot primitive (identities/computer/phone/card), trust ladder, inverse pyramid, ~4,000 PRs/month with low-risk overnight bound, Owner/Manager/Collaborator team bots.
- **Digest-authored inference (retained, flagged):** the compiler-exists-for-code-not-marketing framing, the unlimited-token critique, the catastrophic prompt-injection scenario — all labeled as the digest's analysis, not the source's.
- **Speaker-reported:** PR volume and overnight auto-fix claims are Tan's own numbers.
- **Inference (this record):** contract-map dispositions; the "beyond ATP" coverage verdict; AIC-DOC1/2 adoptions.
- **Unknown:** the "Sandy" pipeline name (inconsistent across secondaries); whether a readable full transcript would correct any triangulated claim.

## Falsifiability

- If a readable full transcript contradicts a triangulated claim (e.g., the step-3 caveat, the 4,000-PR figure), the affected row is corrected; dispositions do not depend on the metrics.
- If a local review round showed adversarial multi-model review producing intent-corrected (not just overfit) output at low cost, the "overfit" caveat note is weakened — it stays a recorded caution, not a rule.
- The "Sandy" bot name and all digest-only specifics are retained as reported, flagged for correction when the transcript is readable.

## Standing Non-Goals

No Skill edit, no prompt edit beyond the cited surface, no product/runtime adoption, no model call, no claim that Grokbot's internal results generalize. Full-transcript verification is deferred, not waived — it is marked inside the fidelity table. Commit/push remain unperformed pending owner direction.
