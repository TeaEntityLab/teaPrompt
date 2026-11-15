# Agent Trust Pyramid Survey — Lauren Tan "All Code Is Slop (Except Mine)" (2026-11-15)
Language: English

> **Status: reference documentation and navigation adopted (`ATP-DOC1/2`); no Skill, operating-rule, or runtime change.** The owner supplied a Chinese digest of the talk plus a summarized set of reader comments and asked for a survey and doc update. This record preserves the primary source (official machine transcript), checks the digest's fidelity, and separates verifiable talk claims from supplier-summarized comments. It does not authorize a new Skill, a lint rule, or any claim that these numbers generalize.

## Research Question and Direct Recommendation

Does the trust-pyramid talk — deterministic layers first, prose last — expose a missing delivered TeaPrompt contract?

**Record the source-qualified map; leave Skills unchanged.** The thesis is the strongest external restatement yet of a rule the library already enforces: *corrections become executable checks, not prompt prose*. Every layer of her pyramid maps to an existing contract. The genuinely new operational detail is that the deterministic layers are **host-side assets** (lint rules, API bans, dependency-graph analyzers) — TeaPrompt's natural-language contracts already treat them as out of scope for prompts.

## Version and Source Identity

Checked 2026-11-15.

| Item | Identity | Reuse / accuracy boundary |
| --- | --- | --- |
| [AI Engineer CODE 2026 talk](https://ai.engineer/code/2026/talks/lauren-tan) + [official machine transcript](https://ai.engineer/api/code/reading-download/transcripts/lauren-tan.md) | Lauren Tan ("Potato" / @poteto), Grok Bot team at **SpaceX Super Intelligence** (SpaceXSI; transcript's "SpaceXsi/Grabbot/Grockbot" are ASR variants of "SpaceX SI / Grok Bot"). November 11, 2026 main stage; video premiered 2026-11-14, ~17 min. | Machine-generated transcript; name spellings verified against the [event page](https://ai.engineer/code/2026/talks/lauren-tan) and speaker bio. |
| [YouTube video](https://www.youtube.com/watch?v=O_zcc6Xl12g) | Premiered 2026-11-14; ~102K views at check time. | Transcript's `Source:` line points to a different watch id (`ZZ19zhYnDKY`); both resolve to the same talk content — retained, not reconciled. |
| Speaker background | Ex-Cursor (joined SpaceXSI via acquisition 2026-08); previously Meta React core / React compiler work per her AI Engineer bio. | Self-reported via LinkedIn/bio; not independently verified. |
| Supplied zh digest + comment summary (owner-provided) | Socratic-critical notes; attributed comments from Vishal Singh, Minglei (Uber), Rigario; YouTube skepticism about PR reviewability. | **Unverified paraphrase** — comment threads not independently readable; treated as leads. |

No upstream code is copied into TeaPrompt's operational assets.

## Fidelity Check: Digest vs Transcript

| Digest claim | Transcript | Verdict |
| --- | --- | --- |
| 3,000–11,000 PRs/month | Personal: "I shipped 3,000 pull requests to production" last month; team: "11,000 pull requests" | faithful |
| ~227 contributors | "in October we had about 227 people who contributed at least one pull request" | faithful |
| Revert ~0.5% | "steady at about half a percent" on a relative basis | faithful |
| Stable client ~once a day | "we cut a new stable version about once a day" | faithful |
| Performance improved (startup, typing, chat switching) | Same, with her own caveat "still an Electron app … there is a ceiling" | faithful (caveat retained) |
| Inverse pyramid: deterministic code+controls → verification → prose | "The first two layers are deterministic … Verification … and then" prose last | faithful |
| `useEffect` banned | "ban it in product code … only allowed in some places inside of Dune APIs" — because it "requires a lot of nuance … agents are not good at using it" | faithful |
| `electron-renderer`/`electron-main` dirs + dependency-graph analyzer + lint | Same, verbatim structure | faithful |
| 99% comments banned | "ban 99% of comments … they go stale easily … an escape hatch to justify not doing the right thing … they're not enforceable" | faithful |
| Feature map / site map, custom CLIs, Chrome DevTools Protocol | Same | faithful |
| TLA+ model checking (notifications across devices), Lean proofs (custom virtualization lib), Bombadil UI property testing | Same | faithful |
| Review shifted to artifacts (videos, screenshots, diagrams, state charts) | "code review … shrunk into looking at verification artifacts … videos, screenshots, diagrams, formal verification"; her `state chart` skill in `pstack` plugin pack | faithful |
| "Write a lint rule … structurally impossible" per correction | "every time we correct our agents, it turns into one of these deterministic checks or we … categorically eliminate that problem in the code" | faithful |
| Autonomous post-release fuzz loops auto-merging fix PRs | Same — viable "because our code base is good enough" | faithful |
| "Dune" = client framework, "Grok Bot" = product | "Dune is a client framework … like Next.js for Electron" | faithful |
| NOT in digest | She needed **six months** to reach thousands-of-PRs capability; "it will take you much less time than I did" | omission — the Vishal Singh comment ("months cleaning before automating") compensates, but that detail is her own framing |
| NOT in digest | "70% of her daily tokens go into verification" was **Cindy's** tweet she quotes; Tan says "most of my token usage goes to verification" | the digest's "majority of tokens" is right, attribution was to a peer |
| YouTube-digest extras | "AI Engineer CODE 2026", Nov 11 main stage | verified via event page |

## What the Source Adds vs Existing Contracts

| Idea | Existing TeaPrompt coverage | Gap? |
| --- | --- | --- |
| Corrections → deterministic checks (lint/API ban), not prompt prose | `flow-control-generator` fail-closed checks; `verification-map-generator` executable VERIFY entries; library's own bias to `validate_*.py` over wording | None — same rule; this talk is its strongest external proof-point |
| Automating a low-trust inner loop scales slop | `flow-loop-harness` "never trust model-declared done"; external verifier requirement | None |
| Banned-API pattern (`useEffect`, comments) as architecture | Host-side constraint; prompts don't carry it. Repo precedent: router fail-closed `*)` arm, casefold rejection | None — validates the pattern |
| Verification artifacts as review surface (video/screenshot/state-chart) | `reflective-review` verdict lanes; record discipline | None — new evidence *type*, same contract |
| Autonomous loops gated by revert-rate telemetry | `flow-loop-harness` budget + stall detection; `reflective-risk` for promotion | None — her auto-merge is an *earned* permission, same shape |
| Tokens → verification share (~70% cited) | Verification-first posture | Anecdotal datapoint, retained as author-reported |
| Codebase garden: pristine corpus → agents copy clean patterns | Methodology's "adopted sentence" discipline; corpus hygiene | None — metaphor matches |

## Optional Worked Reference — Corrections Become Checks

Lauren Tan's loop is the existing rule at production scale: **every agent correction is promoted to a deterministic check or a categorical API change — never to a comment, rule file, or prompt line.** Her two concrete examples:

- `useEffect` is banned in product code because nuance-heavy APIs are where agents produce slop; the API surface itself was redesigned (Dune) so the misuse is structurally impossible.
- 99% of comments are banned because they are *unenforceable* prose that agents use to justify patches; lint rules with actionable error messages replace them — telling the agent to fix the root cause instead.

Applied to the library: this is exactly why `flow-control-generator` demands fail-closed checks and `verification-map-generator` requires executable VERIFY entries — a sentence an agent can ignore is a slop source at scale. Her "first two layers are deterministic" ordering is the same precedence TeaPrompt applies: executable check > structural constraint > prose instruction.

This is a source-qualified example from one team's self-reported metrics (11K PRs/month, 0.5% revert), not evidence the numbers transfer to other codebases — she herself spent six months reaching that point.

## Candidate Adoption Ledger

| ID | Candidate | Disposition | Evidence / reopen trigger |
| --- | --- | --- | --- |
| ATP-DOC1 | This source-bound record and its catalogue row | Adopted; documentation only | Owner asked to survey and update docs. Refresh if transcript/talk is revised or metrics are publicly audited. |
| ATP-DOC2 | Optional worked-reference links appended under `runtime-trust-boundary.md`'s and `workflow-acquisition.md`'s existing Optional Worked Reference sections, outside both prompt fences | Adopted; navigation only | Keeps the corrections→checks example discoverable without changing prompt contracts. |
| ATP-SK1 | New Skill or edits encoding the trust pyramid | No change | Every layer already maps to an existing contract; the pyramid is a portfolio-ordering heuristic, not a runnable contract. |
| ATP-RUN1 | Adopt Dune/Bombadil/TLA+/Lean tooling or auto-merge loops | Not adopted | Host-tooling choices; nothing to copy into the library. Auto-merge would first need the local revert telemetry she cites as a precondition. |
| ATP-RULE1 | Ban comments/`useEffect`-class APIs, or promote the pyramid ordering, as a TeaPrompt rule | Rejected | Specific bans are per-codebase host decisions; the ordering rule already exists in executable form. |

## Falsifiability

- If the transcript proves materially different from the talk (ASR garbling a number), the affected row is corrected; dispositions do not depend on the metrics.
- If a local lint-rule-vs-prompt experiment showed prose corrections outperforming deterministic checks at TeaPrompt's scale, ATP-SK1's "no gap" verdict would reopen.
- The 0.5% revert and 11K PRs are self-reported and unaudited; treat them as a directionally plausible datapoint from a team that sells the workflow, not a transferable benchmark.

## Standing Non-Goals

No Skill edit, no prompt edit beyond the cited surfaces, no lint/tool adoption, no model call, no claim that Grok Bot's metrics generalize. Comment attributions (Vishal Singh, Minglei, Rigario) stay unverified. Commit/push remain unperformed pending owner direction.
