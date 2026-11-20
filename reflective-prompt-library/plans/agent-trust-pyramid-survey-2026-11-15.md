# Agent Trust Pyramid Survey — Lauren Tan "All Code Is Slop (Except Mine)" (2026-11-15)
Language: English

> **Status: reference documentation and navigation adopted (`ATP-DOC1/2`); no Skill, operating-rule, or runtime change.** The owner supplied a Chinese digest of the talk plus a summarized set of reader comments and asked for a survey and doc update. This record preserves the primary source (official machine transcript), checks the digest's fidelity, and separates verifiable talk claims from supplier-summarized comments. It does not authorize a new Skill, a lint rule, or any claim that these numbers generalize.

## Research Question and Direct Recommendation

Does the trust-pyramid talk — deterministic layers first, prose last — expose a missing delivered TeaPrompt contract?

**Keep the example; leave Skills unchanged.** When the same mistake recurs, first ask whether the host can make it impossible or catch it. A lint rule, an API boundary and a behavior test can enforce different things. Written guidance still has a place when a person or agent must exercise judgment.

## Version and Source Identity

Checked 2026-11-15.

| Item | Identity | Reuse / accuracy boundary |
| --- | --- | --- |
| [AI Engineer CODE 2026 talk](https://ai.engineer/code/2026/talks/lauren-tan) + [official machine transcript](https://ai.engineer/api/code/reading-download/transcripts/lauren-tan.md) | Lauren Tan ("Potato" / @poteto), Grok Bot team at **SpaceX Super Intelligence** (SpaceXSI; transcript's "SpaceXsi/Grabbot/Grockbot" are ASR variants of "SpaceX SI / Grok Bot"). November 11, 2026 main stage; video premiered 2026-11-14, ~17 min. | Machine-generated transcript; name spellings verified against the [event page](https://ai.engineer/code/2026/talks/lauren-tan) and speaker bio. |
| [Standalone video](https://www.youtube.com/watch?v=O_zcc6Xl12g) | AI Engineer, uploaded 2026-11-14, 17:31. | The organizer's transcript uses the [long recording](https://www.youtube.com/watch?v=ZZ19zhYnDKY&t=3662s), starting at 1:01:02. Use the clock for the recording being cited, not a clip timestamp on the long recording. |
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
| A recurring mistake that can be prevented or tested should not depend on remembering prose | `flow-control-generator` fail-closed checks; `verification-map-generator` executable VERIFY entries | No missing contract. Judgment guidance is distinct from enforcement. |
| Automating a low-trust inner loop scales slop | `flow-loop-harness` "never trust model-declared done"; external verifier requirement | None |
| Banned-API pattern (`useEffect`, comments) as architecture | Host-side constraint; prompts don't carry it. Repo precedent: router fail-closed `*)` arm, casefold rejection | None — validates the pattern |
| Verification artifacts as review surface (video/screenshot/state-chart) | `reflective-review` verdict lanes; record discipline | None — new evidence *type*, same contract |
| Improving verification before leaving work unattended | `flow-loop-harness` external verifier and stop conditions; `reflective-risk` for consequential actions | No missing contract. The talk reports a revert rate; it does not specify a rate that grants merge authority. |
| Tokens spent on verification | Verification-first posture | Tan says *most* of her usage; the specific 70% was Cindy's report. Neither is a budget target. |
| Codebase garden: pristine corpus → agents copy clean patterns | Methodology's "adopted sentence" discipline; corpus hygiene | None — metaphor matches |

## Optional Worked Reference — Corrections Become Checks

Tan describes turning repeated corrections into changes to the environment. The point is **not to rely on a reminder for a mistake the system could prevent**. Her talk explicitly reserves prose for judgment. Two examples from her team:

- Product code cannot use React's `useEffect` directly; selected Dune framework APIs can. The boundary gives contributors a supported alternative rather than asking each one to recognize the risky case.
- Tan reports banning about 99% of code comments. An actionable lint error can tell the contributor what to change at the point of misuse. This is not a ban on documenting decisions or preserving constraints that the code cannot express.

In TeaPrompt, a fail-closed route rejects an unknown label whether or not the model remembers the rule. A verification map, by contrast, tells an agent *how to test* a feature; the observed result, not the map, supplies the evidence.

This is a source-qualified example from one team's self-reported metrics (11K PRs/month, 0.5% revert), not evidence the numbers transfer to other codebases — she herself spent six months reaching that point.

## Candidate Adoption Ledger

| ID | Candidate | Disposition | Evidence / reopen trigger |
| --- | --- | --- | --- |
| ATP-DOC1 | This source-bound record and its catalogue row | Adopted; documentation only | Owner asked to survey and update docs. Refresh if transcript/talk is revised or metrics are publicly audited. |
| ATP-DOC2 | Optional worked-reference links appended under `runtime-trust-boundary.md`'s and `workflow-acquisition.md`'s existing Optional Worked Reference sections, outside both prompt fences | Adopted; navigation only | Keeps the corrections→checks example discoverable without changing prompt contracts. |
| ATP-SK1 | New Skill or edits encoding the trust pyramid | No change | Every layer already maps to an existing contract; the pyramid is a portfolio-ordering heuristic, not a runnable contract. |
| ATP-RUN1 | Adopt Dune/Bombadil/TLA+/Lean tooling or auto-merge loops | Not adopted | A host would need its own scoped authorization, verifier and recovery path. Another team's telemetry supplies none of these. |
| ATP-RULE1 | Ban comments/`useEffect`-class APIs, or promote the pyramid ordering, as a TeaPrompt rule | Rejected | Specific bans are codebase decisions. The cost of routine review does not move required Human Review to the end of a high-risk action. |

## Falsifiability

- If the transcript proves materially different from the talk (ASR garbling a number), the affected row is corrected; dispositions do not depend on the metrics.
- If a local lint-rule-vs-prompt experiment showed prose corrections outperforming deterministic checks at TeaPrompt's scale, ATP-SK1's "no gap" verdict would reopen.
- The 0.5% revert and 11K PRs are self-reported and unaudited; treat them as a directionally plausible datapoint from a team that sells the workflow, not a transferable benchmark.

## Standing Non-Goals

No Skill edit, no prompt edit beyond the cited surfaces, no lint/tool adoption, no model call, no claim that Grok Bot's metrics generalize. Comment attributions (Vishal Singh, Minglei, Rigario) stay unverified. Commit/push remain unperformed pending owner direction.

## CabLate guide (2026-11-20)

The supplied `paste-24` is Cab's *讓 AI 值得放手*, not a second report from Tan. The [26-page PDF](https://cablate.com/downloads/lauren-tan-let-ai-work.pdf) is dated Nov 18; Cab [published it Nov 19](https://cablate.com/articles/lauren-tan-ai-trust-pdf/) and explicitly says Tan did not participate or endorse it. PDF checked: SHA-256 `02d2815dc68162032a7712b4043cb36c8ed6f8c5a25ea8f71161adcccfbee255`.

### Who proposed what

| Guide claim | What the source supports | What transfers |
| --- | --- | --- |
| Five ways to stop a mistake (pp. 4–5) | Cab joined two sources. Pinned [`/correct`](https://github.com/cursor/plugins/blob/2f87c854fe3e2fcda44ca86b46ede35aad3c46b7/pstack/skills/correct/SKILL.md) tries architecture, types/lint/CI, behavior tests, then docs for judgment. It groups a class after two occurrences and asks to see a new check fail on a real past mistake. [Guide ch. 9](https://github.com/cursor/plugins/blob/2f87c854fe3e2fcda44ca86b46ede35aad3c46b7/pstack/docs/guide/09-make-it-yours.md) explicitly excludes human review from that list; the costly human tip comes from [Tan's trust pyramid](https://ai.engineer/code/2026/talks/lauren-tan). | Useful for deciding *where* to fix a repeat. Neither waiting for a second occurrence nor putting people last is appropriate when an action already requires approval. |
| Trust, verification, environment, correction, design and autonomy (pp. 6–10) | These are Cab's six groups. Tan's [May article](https://x.com/poteto/status/2058975157503570132) argues for depth before parallelism; [Loops You Can Trust](https://x.com/poteto/status/2069824386283319343) identifies verification as a bottleneck. Her [January article](https://x.com/poteto/status/2014257661035094246) uses plan mode to supply context; [September's Pt. 2](https://x.com/poteto/status/2097732320606507506) uses prototypes to settle design questions. [`/interrogate`](https://github.com/cursor/plugins/blob/2f87c854fe3e2fcda44ca86b46ede35aad3c46b7/pstack/skills/interrogate/SKILL.md) permits a prototype or probe of the current code for a plan. | Start with a finish condition and an inspectable result; neither “never plan” nor “review every change with a panel” follows. |
| Give the agent a reusable way to verify | [Guide ch. 6](https://github.com/cursor/plugins/blob/2f87c854fe3e2fcda44ca86b46ede35aad3c46b7/pstack/docs/guide/06-verify-and-ship.md) requires driving a real feature, collecting evidence, cleaning up, and checking the evidence survived. [Pt. 1](https://x.com/poteto/status/2094457600259842065) recommends daily map upkeep. | TeaPrompt's [verification-map generator](../skills/verification-map-generator/SKILL.md) already calls for a fresh agent and an unlabeled seeded fault; upkeep is **event-driven**, not daily. A successful drive covers the observed path, not all behavior or product quality. |
| Unattended work, independent review and landing | [Guide ch. 7](https://github.com/cursor/plugins/blob/2f87c854fe3e2fcda44ca86b46ede35aad3c46b7/pstack/docs/guide/07-overnight.md) requires a previously observed task, equivalent tools/signals, evidence and a stop at each stage, and reviewed prior runs. Its [`worker.md`](https://github.com/cursor/plugins/blob/2f87c854fe3e2fcda44ca86b46ede35aad3c46b7/pstack/skills/poteto-mode/worker.md) lists four stops: deploy, delete data, force-push a shared branch, message outside the run. [Shipping](https://github.com/cursor/plugins/blob/2f87c854fe3e2fcda44ca86b46ede35aad3c46b7/pstack/skills/poteto-mode/playbooks/shipping.md) binds a non-author's verdict to the **patch**, not just a SHA; an equivalent patch can retain it. [Autopilot](https://github.com/cursor/plugins/blob/2f87c854fe3e2fcda44ca86b46ede35aad3c46b7/pstack/skills/poteto-mode/playbooks/autopilot-full.md) also requires a scoped grant and green CI on the current head. | Evidence that a patch works is not permission to land it. The four worker stops are not a complete permission policy. TeaPrompt retains its own privacy, credential, billing and third-party [review boundaries](../04-agent/workflow-acquisition.md). |
| Decision logs and blind evaluation | [`/show-me-your-work`](https://github.com/cursor/plugins/blob/2f87c854fe3e2fcda44ca86b46ede35aad3c46b7/pstack/skills/show-me-your-work/SKILL.md) specifies append-only TSV, evidence pointers, a transcript check, and an ending *Attention* section after another vendor's review. The [eval playbook](https://github.com/cursor/plugins/blob/2f87c854fe3e2fcda44ca86b46ede35aad3c46b7/pstack/skills/poteto-mode/playbooks/eval.md) hides the rubric from candidates, gives the judge outputs without model names, and checks which files each candidate actually read. | These are written procedures, not receipts of a run. Cab's cheaper one- or two-task before/after check with a disclosed self-judge is a smoke check, not independent evaluation. |

Cab, not Tan, organizes the practices into four maturity stages (0–3) and thirteen rules (0–12). Cab adds the two entry questions (“can it be undone?” / “can it be checked?”) and token/time stops for a small team. The non-code examples on p. 18 are also Cab's: rendering a slide can establish that text fits; it cannot establish that a cited figure is true. A model reader's wrong answer is a lead for a human, not a measured reader outcome.

### What changed in public pstack

Cab gives a date, not a SHA. [`cursor/plugins@2f87c85`](https://github.com/cursor/plugins/commit/2f87c854fe3e2fcda44ca86b46ede35aad3c46b7) is the Nov 16 pstack change (`0.15.43`); its `pstack/` tree matches the Nov 18 snapshot `35a9094`. It contains **22** direct playbook files (not “十幾份”), **24** principle skills among **58** skill directories with a `SKILL.md`, and **10** numbered guide chapters. The [adapter generator](https://github.com/cursor/plugins/blob/2f87c854fe3e2fcda44ca86b46ede35aad3c46b7/scripts/generate-pstack-harness-trees.mjs) derives the Claude Code tree from the Cursor source. Later `main` at [`aaeb0ea`](https://github.com/cursor/plugins/commit/aaeb0ea3a0584995aa8f55ce44c6c5259414b896) has manifest `0.15.46`; the cited correction, worker, shipping, audit and eval files were unchanged across those two pins.

Cab reports that `architect` shrank from about 7,700 to 900 characters. The direction reproduces, **not that pair of counts**. `git cat-file -s REV:PATH` gives the following whole-file lengths, including frontmatter and newlines. All four blobs are ASCII, so bytes and Unicode characters agree. Companion files are not counted.

| `architect/SKILL.md` distribution | Before: `b63c29f` (parent) | After: `2f87c85` |
| --- | ---: | ---: |
| [Cursor source](https://github.com/cursor/plugins/blob/2f87c854fe3e2fcda44ca86b46ede35aad3c46b7/pstack/skills/architect/SKILL.md) | 5,443 | 722 |
| [Generated Claude Code copy](https://github.com/cursor/plugins/blob/2f87c854fe3e2fcda44ca86b46ede35aad3c46b7/harness/pstack/claude-code/skills/architect/SKILL.md) | 5,631 | 910 |

The [Sept 23 change](https://github.com/cursor/plugins/commit/b0b9c7a0baf8b6aa1d00bf77d4101e577d4ba411) does say it cut 19 instructions for Opus 5.5. That verifies the change and its stated reason, not equivalent behavior after removal. The Nov 16 change also removed `check-plan.mjs` and its test: the [Nov 4 checker results](pstack-matt-lauren-survey-2026-10-03.md) remain evidence for those old bytes, not a check available at Cab's pin.

### What the numbers establish

- Tan's [August post](https://x.com/poteto/status/2090141955695198633) says 1,000 personal PRs and her [September post](https://x.com/poteto/status/2102050467505430555) says 2,500, each for the preceding month. The [September talk repost](https://www.youtube.com/watch?v=NjoZoUm85x0) says 2,000. Keep the reports separate. The November talk reports 3,000 personal PRs, about 11,000 team PRs and roughly 0.5% reverted. A fix delivered in a later PR need not be a revert; there is no defect count, cost comparison or independent merge log here.
- Cab lists 11 X items plus a LinkedIn entry, five recordings, and 155 version records. The [Maven event](https://maven.com/p/e23d9c/how-cursor-turned-ai-agents-into-better-engineers) confirms the workshop and chapters. The [Matt Pocock](https://www.youtube.com/watch?v=MN9dGgmLyso) and [MTS](https://www.youtube.com/watch?v=A63sedG-p5Q) pages confirm the recordings; they did not expose captions in this check. Cab's interview timestamps are therefore not verified quotations. Cab also identifies a paywalled interview and an unavailable podcast. `git rev-list --count 2f87c85 -- pstack/` returns 171 commits; Cab does not identify which 155 records were read.
- Cab reports five model vendors, four editorial rounds and 107 second-round comments. The PDF is evidence of that account, not the individual reviews or an independent quality evaluation. Selected original X posts were read via their public JSON mirrors (e.g. [Pt. 2](https://api.fxtwitter.com/status/2097732320606507506)); no private framework, model trial or live merge was tested.

**Decision:** `ATP-DOC1/2` remain reference and navigation only. Correct the earlier “never prose” wording, including its worked-reference link description; do not add a Skill, a review threshold or a runtime. Reopen if a repeatable local task exposes a missing check, or if a dated artifact changes a specific source claim. Another retelling of Tan's work is not independent evidence that her outcomes transfer.
