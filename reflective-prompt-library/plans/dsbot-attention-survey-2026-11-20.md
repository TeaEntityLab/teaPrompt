# DS Bot Survey — Fewer Inboxes, Not Fewer Sessions (2026-11-20)

Language: English

> **Status:** reference case (`DSB-DOC1`); no Skill, runtime, scheduler or merge automation. Decision: try a stable point of contact for recurring, independently verifiable work; do not turn it into a ban on direct sessions. DS Bot lets a person give out work and receive decisions in one conversation while other bots work elsewhere. That changes who has to follow each session. It does not make the work correct, a checkbox a merge receipt, or an optimal team size known.

## What FeiZ actually reported

[FeiZ's November 15 post](https://x.com/Fei2411/status/2121930284048478462) was recovered in full through [FxTwitter](https://api.fxtwitter.com/status/2121930284048478462); the direct X reader was unavailable. It concerns development of [Fei2411/DS-Bot](https://github.com/Fei2411/DS-Bot), a community project built on DeepSeek Harness, not DeepSeek's separate Super-agent prototype. FeiZ also [links the repository under its current name](https://x.com/Fei2411/status/2114372356080869821).

- The assistant handles *about 60% of communication*, not 60% of jobs. FeiZ also names an issue/bug handler, an improvement-ideas handler and a separate goal-alignment bot. “Two or three” describes regular contacts, not the total roster. About twenty worker bots are reported; the post does not say twenty ran concurrently.
- Scheduled tasks run in batches. The author describes returning to an interactive card, choosing PRs to merge and discarding the rest. The post supplies neither the earlier demonstration's link nor per-PR receipts, attention logs, a comparison period or a sample of the developers consulted. The account verifies what the author said, not the volume of work, a measured saving or developer consensus.
- [A same-day quote post by @libukai](https://x.com/libukai/status/2121967585935937585) ([text and quote relationship](https://api.fxtwitter.com/status/2121967585935937585)) gives a useful counterexample from one user: schedule recurring reports, but use Classic for course material that takes repeated discussion and revision. It is a preference, not an independent efficacy study.

## What the software supports

The [November 12 release, v0.3.6](https://github.com/Fei2411/DS-Bot/releases/tag/v0.3.6), preceded the post; the public [`main` snapshot at posting time](https://github.com/Fei2411/DS-Bot/tree/ab3316e847f9fda3629d7942a4a862c518eb2abc) need not be the author's installed build. On November 20, `git ls-remote`, the GitHub tag and the [latest published release, v0.3.8](https://github.com/Fei2411/DS-Bot/releases/tag/v0.3.8) agreed on `5e9b7da8882da3b68d8a0624342708c2150a9156` (November 16). The implementation checks below use that later revision unless stated otherwise.

| Question | What the pinned implementation does | Limit |
| --- | --- | --- |
| Is one bot one endless session? | No. [Thread state](https://github.com/Fei2411/DS-Bot/blob/5e9b7da8882da3b68d8a0624342708c2150a9156/ds-bot/src/host/threads.js#L1-L84) separates bot ID, foreground session, live background parts and per-thread history. | Keeping a familiar contact is not keeping every conversation in one model context. The parallel-parts implementation is evidence about v0.3.8, not FeiZ's private setup on November 15. |
| Who gets the worker's answer? | A [direct request](https://github.com/Fei2411/DS-Bot/blob/5e9b7da8882da3b68d8a0624342708c2150a9156/ds-bot/src/host/tools.js#L323-L379) can queue; the [later reply](https://github.com/Fei2411/DS-Bot/blob/5e9b7da8882da3b68d8a0624342708c2150a9156/ds-bot/src/host/turns.js#L58-L102) refers to the original exchange. The caller can instead request `reply_to: 'user'`, which directs the person to the worker's own chat. | A dispatch acknowledgment is not a result. One inbox is a routing choice, not a guarantee. |
| What does a schedule target? | The [schedule adapter](https://github.com/Fei2411/DS-Bot/blob/5e9b7da8882da3b68d8a0624342708c2150a9156/ds-bot/src/host/schedules.js#L115-L150) resolves a bot or group to a session and passes the prompt and timing to DSH. It refuses creation when that service is off. | Registering a daily task is not proof it ran, ran once, or produced an acceptable PR. No live scheduler was exercised. |
| Was Classic removed? | The [v0.3.0 change](https://github.com/Fei2411/DS-Bot/pull/933) removed the account-menu shortcut but kept Settings → General → Mode. [v0.3.5 restored the shortcut](https://github.com/Fei2411/DS-Bot/pull/1385) where switching is available. | This was a discoverability change, not removal and reinstatement of the agent engine. |

## What a PR checkbox returns

At v0.3.8, [`show_view`](https://github.com/Fei2411/DS-Bot/blob/5e9b7da8882da3b68d8a0624342708c2150a9156/ds-bot/src/host/tools.js#L895-L926) can open an interactive card in the bot's own chat; this tool refuses group sessions. The [submission handler](https://github.com/Fei2411/DS-Bot/blob/5e9b7da8882da3b68d8a0624342708c2150a9156/ds-bot/src/host/channel.js#L671-L694) checks that the card is still pending, validates the selection and sends it as a user follow-up. The [pre-post handler](https://github.com/Fei2411/DS-Bot/blob/ab3316e847f9fda3629d7942a4a862c518eb2abc/ds-bot/src/host/channel.js#L651-L674) also delivered a message. A current card ID does not establish that a PR's head is still current.

**Offline checks, no accounts or models:**

- Ran the [upstream thread fixture](https://github.com/Fei2411/DS-Bot/blob/5e9b7da8882da3b68d8a0624342708c2150a9156/ds-bot/test/threads.test.js) with Node 25.1.0: `node --test --test-isolation=none ds-bot/test/threads.test.js` → 7 passed. The cases include keeping a busy part in the background and moving a part without mixing its history with another thread's. This tests state transitions, not worker performance.
- Checked the `deep-view@0.1.2` tarball against [DS Bot's lockfile SHA-512](https://github.com/Fei2411/DS-Bot/blob/5e9b7da8882da3b68d8a0624342708c2150a9156/ds-bot/package-lock.json#L581-L585). Ran the actual [`viewReply` encoder](https://github.com/Fei2411/deep-view/blob/dab178d026332bdb2016afe71e57eddf0747b850/src/core/reply.js#L30-L44) with network and writes denied. A multi-select `options` card offered fictional `PR #17` and `PR #21`. Selecting only `PR #17` returned `answer_to_pending_view`, `action: "pick"`, `selected: ["PR #17"]`, `outcome: "answered"`. Empty selection returned `values.selected: select at least one option` from the validator. No PR was merged or closed. For this card shape, “accept none” needs an explicit choice if it is to be submitted as a decision.

DS Bot lists a [separately authenticated GitHub connector](https://github.com/Fei2411/DS-Bot/blob/5e9b7da8882da3b68d8a0624342708c2150a9156/ds-bot/src/host/connectors/catalog.js#L20-L28); the repository's own [issue-triage workflow](https://github.com/Fei2411/DS-Bot/blob/5e9b7da8882da3b68d8a0624342708c2150a9156/.agents/skills/issue-triage/SKILL.md#L7-L12) explicitly excludes merging PRs. Neither identifies the tool FeiZ used. For a real review, show the repo, PR, reviewed head, diff and checks; distinguish **merge**, **defer** and **close**. An unchecked row is not by itself an instruction to close. GitHub's [merge API](https://docs.github.com/en/rest/pulls/pulls#merge-a-pull-request) accepts an expected head `sha` and returns `409` on mismatch. If the head changes, review the new revision; if a submitted merge has no response, check GitHub's state before retrying. These are recommendations, not guarantees provided by the card.

## Does it save attention?

The closest comparison found was [Long et al., *ParallelPilot*, arXiv v1](https://arxiv.org/html/2609.33113v1). Sixteen developers tried both their baseline Copilot setup and a combined planning, logging and monitoring interface in counterbalanced order. Each condition allowed 20 minutes for six short coding tickets. The authors report 0.272 versus 0.445 tickets per minute (63% higher with ParallelPilot) and lower **self-reported** tracking and switching burden. Perceived control and success redirecting agents did not improve significantly. There was no required systematic code review; verification accuracy was not measured. This supports making parallel work easier to supervise. It does not isolate the UI from planning assistance, test DS Bot, or establish durable gains for a twenty-worker team.

Batching is a different intervention. [Mark et al., CHI 2016](https://www.microsoft.com/en-us/research/publication/email-duration-batching-and-self-interruption-patterns-of-email-use-on-productivity-and-stress/) observed 40 information workers over about 12 workdays. Under longer email use, people who batched reported higher productivity, but the study found no evidence of lower stress from batching. Email is not PR review; neither paper measures the maintainer's claimed energy savings.

## When to try it, and when to go direct

Use a fixed inbox for repeatable work with a clear acceptance check. Keep routine successes quiet until the review window; surface blockers, conflicting edits, authorization requests and time-sensitive failures early. A short card should let the reviewer open the underlying diff, checks and session rather than trust the bot's summary. Prefer a direct session when discovering the goal, reproducing an unfamiliar failure or making a tightly coupled design change: the next useful question depends on the intermediate result.

**A local comparison, not a result:** alternate matched task batches between direct sessions and one assistant inbox. Keep model, worker limit, permissions and acceptance criteria the same. Count all attempts, including deferred, failed and discarded work. Track human minutes spent assigning, inspecting and repairing per accepted change, interruptions requiring action, time a blocker waits, and regressions or useful changes incorrectly discarded. Record perceived effort separately. Fewer open windows with longer blocker delays or more missed defects is not a win.

TeaPrompt's [attention measurement guidance](agent-control-plane-comparison-survey-2026-11-04.md#measuring-attention-without-hiding-failure) and [external-effect boundary](../04-agent/runtime-trust-boundary.md#4a-external-effect-recovery-boundary) already cover the relevant decisions. `DSB-DOC1` is a reference case only: no worker quota, Skill, scheduler, dashboard or merge automation. Revisit efficacy with comparable DS Bot task data; revisit the action path with a card tied to an authorized operation and its actual GitHub result.

## Evidence vs Inference

- **Verified (sources):** the FeiZ launch post and its repository link; the DS-Bot repo's separately authenticated GitHub connector and its issue-triage exclusion of PR merges; the GitHub merge API's expected-head `sha`/`409` behavior; the Long et al. ParallelPilot figures and Mark et al. batching results as reported.
- **Author-reported:** FeiZ's "~60% of communication" share and personal workflow description.
- **Inference (this record):** the attention comparison; whether a fixed inbox outperforms direct sessions for a given maintainer.
- **Unknown:** the tool FeiZ used for reviews; whether either cited study generalizes to DS Bot's audience.

## Falsifiability

`DSB-DOC1` fails if a matched task batch shows the inbox raises interruptions, blocker wait or missed defects versus direct sessions, or if a card tied to an authorized operation returns a GitHub result inconsistent with the reported merge state.
