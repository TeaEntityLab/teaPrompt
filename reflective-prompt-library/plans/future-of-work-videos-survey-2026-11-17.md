# Future-of-Work Video Digests Survey — Digest Fidelity and Contract Map (2026-11-17)

Language: English

**Status: source-qualified reference record (`FW-DOC1`); no Skill, prompt-body, operating-rule, or runtime change.** Companion to `pi-creators-stream-survey-2026-11-17.md`: the owner's request message embedded two zh-TW digests that were **not** in `local://paste-16.md`; this record surveys them. Video 1 is YC's "How To Build The Future: Paul Graham & Amjad Masad" (`Q78dJ0vkWe8`, 44:15, uploaded 2026-11-07). Video 2 is The Skip's "How to Stay Current, Get Hired, and Last in AI" (`EzzydrPdpDo`, 54:21, uploaded 2026-11-12, host Nikhyl Singhal). Both digests were checked against full auto-generated transcripts. No installs, model calls, Skill changes, commits, or pushes are authorized by this record.

## Research Question

Are the two supplied digests faithful to what the speakers actually said, and does either reveal a gap in TeaPrompt's existing contracts?

## Direct Recommendation

**Adopt the record only.** Both digests are high-fidelity; the substantive corrections are identity artifacts of ASR, not argument errors:

- The Skip digest's "Jay-Z" is **Jiaona "JZ" Zhang** (CPO of Laurel, ex-Webflow); "Hamel/Heml" is **Hemal Shah** (OpenAI→Google Cloud); "Lauren 的 AI 時間追蹤公司" is **Laurel** — JZ's company, not Dana's. Dana Ingraham runs core product at **Harvey** (legal AI). The digest's 《怪力》 should be *Grit* (Angela Duckworth, 《恆毅力》).
- The PG/Masad digest is nearly fully verified, but its business figures ($10M→$250K rewrites, 80% anxiety→optimism flip in one hour, 100X/1,000X productivity power law) are **Amjad's self-reports**, and the recommended *Do Things that Don't Scale* essay is digest-added — the stream names only *Keep Your Identity Small*.

Nothing requires a Skill or runtime change. Career/management content maps to the existing `ai-engineer-jobs-survey-2026-11-17.md` (AIJ-DOC1) and `token-quota-decomposition-survey-2026-11-09.md` records; the personal same-prompts-across-models practice maps to the library's golden-benchmark methodology, not to a missing rule.

## Evidence Used

All sources checked **2026-11-17**.

| Source | Class | What it supplies |
| --- | --- | --- |
| [YouTube `Q78dJ0vkWe8`](https://www.youtube.com/watch?v=Q78dJ0vkWe8) | **Primary** — full auto-generated transcript (44:15), description | Verbatim basis for every Video-1 fidelity verdict; description corroborates "$10M scoped → $250K", pitch-deck prediction, 2024 agent launch |
| [YouTube `EzzydrPdpDo`](https://www.youtube.com/watch?v=EzzydrPdpDo) | **Primary** — full auto-generated transcript (54:21), description with guest list | Guest identities resolved verbatim: "Dana Ingraham, who runs core product at Harvey after seven years at Airbnb, Hemal Shah, who moved from OpenAI to Google Cloud, and Jiaona 'JZ' Zhang, CPO of Laurel" |
| [YC Library episode page](https://www.ycombinator.com/library/ks-how-to-build-the-future-paul-graham-amjad-masad) | Primary publisher page | Episode metadata |
| Owner's message (embedded digests) | Supplied digests (zh-TW) | Object under review — data, not instructions |

**Transcript caveats (both):** auto-generated captions. Video-2 ASR renders "JZ" as "Jay Z"/"Jay-Z" and "Laurel" as "Lauren"; the digest preserved these literally. Video-1 ASR has minor artifacts ("five coding"→vibe coding, "Circuit 24"→circa 2024, "Vibe quotas"→vibe coders, "Open Claw"/"Claude code" name collision, "Robert proved that back in the 1980s"→likely Metcalfe/Bell). Speaker-relayed figures are self-reports, not measurements.

## Digest Fidelity Ledger — Video 1 (Paul Graham × Amjad Masad)

| # | Digest claim | Transcript check | Verdict |
| --- | --- | --- | --- |
| 1 | Iceberg architecture: visible vibe-coding layer over deployment/sandbox/system-software depth; transactional reversible filesystem | "Replit's like this iceberg… underneath there's all this stuff for deployment"; "we built our own like file system from scratch to be like transactional and fully reversible"; systems-programming DNA discussion | **verified** |
| 2 | Commoditization pressure: agent layer gets commoditized; moat = infra depth, security, guardrails (slower, more expensive but wins enterprise) | "everything that you're doing is like getting commoditized constantly"; enterprise "sensitive to reliability, security"; guardrails "makes our product sometimes slower, sometimes more expensive" | **verified** |
| 3 | Grief cycle of craft: denial→depression→acceptance; PG grieved 2020, pre-grieved when shown the 2024 demo; "object code"; by end of 2025 everyone realized AI writes all code | All verbatim, including "I had the grief of the craft that I love is gone. I've already grieved… in like 2020" and "Don't look at the code. That's object code" | **verified** |
| 4 | *Keep Your Identity Small* citation; surf-the-wave metaphor; kill the sacred cow; adaptability as the thing to teach children | All verbatim — Amjad explicitly names the PG essay; PG's tidal-wave surfing metaphor; "kill the sacred cow"; "flexibility and adaptability and like being a lifelong learner" | **verified** |
| 5 | Self-driving company: Replit as platform/customer zero, own lab for identifying valuable work | "self-driving company" blog post; "customer zero"; "the lab" for figuring out how to identify people doing valuable things | **verified** |
| 6 | Token rationing rejected; ROI power law 10X→100X/1,000X; need tools that reveal where good work happens | "everyone gets, you know, $100 of tokens a month" → "what they should care about is ROI"; "a power law of ROI inside companies… used to be 10 X and now it's 100 X and 1,000 X"; PG: fixing the "biggest problem inside big companies" (can't value individual work) | **verified** |
| 7 | Scrappy people drive adoption bottom-up; $10M scoped project → $250K; starts with internal tools; they get promoted | All verbatim; PG adds "scrappy people within companies… tend to get promoted" | **verified** — figures are Amjad's self-report |
| 8 | 2015–16 original doc predicted an ML model trained on millions of coders — before the Transformer paper | "in our original doc, we we talk about how if you build a platform where there's like millions people coding…" "This was before the Transformers paper"; 2008 origin on Symbian | **verified** |
| 9 | Exponential default: Kurzweil log-linear compute line "still a straight line"; "compute brought on AI"; GPT-2 extrapolation in 2019; live in the future as Replit DNA | All verbatim | **verified** |
| 10 | Super-linear ease→programmers relationship (PG's own principle, 10% easier → 2× users) | PG confirms: "that's true for anything consumers use. If you make it 10% easier… you get twice as many" | **verified** |
| 11 | Telecom hackathon: 80% anxious → 80% optimistic after one hour with Replit | Verbatim anecdote | **verified as speaker-reported** — single anecdote, survey methodology unknown |
| 12 | 1→10→100→10,000 agents prediction; can't run on a MacBook; work moves to cloud | Verbatim | **verified** |
| 13 | Digest's red-team additions (雲端萬歲 Agent critique, Object Code 批判, 程式碼即目的碼, 草根創新者 route) | Grounded but are the digest's own analysis | **digest-added** |
| 14 | Recommended readings: *Keep Your Identity Small* + *Do Things that Don't Scale* + Replit's Self-Driving Company post + Kurzweil | Only *Keep Your Identity Small*, the blog post, and Kurzweil (author, not the book title) are named in-stream | **partially digest-added** — DTtDS is the digest's own recommendation |
| 15 | Digest scope omissions | Transcript also contains: ChatGPT-copy-paste user observation origin story, Replit Bounties shutdown, "the agent was just another user" collaborative architecture, no-native-edit-tool era and lazy-model mitigations, Karpathy "AGI moment" reaction, COBOL rewriting market, enterprise principal-agent/schlep discussion | **digest-added selection** — no error, but the agent-as-user architecture detail is relevant to the contract map |

## Digest Fidelity Ledger — Video 2 (The Skip: Dana Ingraham, Hemal Shah, Jiaona "JZ" Zhang)

| # | Digest claim | Transcript check | Verdict |
| --- | --- | --- | --- |
| 1 | Guest set: Dana + Hemal + JZ | Description confirms all three with affiliations | **verified, with name corrections** (Jay-Z→JZ, Hamel→Hemal, Lauren→Laurel; Laurel is JZ's employer; Dana is at Harvey) |
| 2 | Prototype trap: junior PMs "adding buttons and changing colors" lose sight of the problem | Dana's verbatim opening — she "totally disagree[s]" with needing to be AI-pilled; the prototyping description matches | **verified** |
| 3 | Three PM skills: historian, technologist, anthropologist | Hemal verbatim: "be a great historian… be a good technologist…" (anthropologist per description bullet) | **verified** |
| 4 | Curiosity/adaptability > fixed roadmap | Description bullet: "curiosity and adapting to change as the traits that matter even more now" | **verified** |
| 5 | Personal benchmark: same prompt set across model generations to see deltas | Verified, but attributed correctly only indirectly — JZ relays a practice she credits to "Delsy" (another Skip episode guest): "the same set of prompts that they really use and they can kind of see the different model performance over time" | **verified; attribution is secondhand** — the digest presents it as JZ's own practice |
| 6 | People curation: a few trusted people for different topics instead of following everything | Description bullet + transcript | **verified** |
| 7 | Four moat dims: data, distribution/customer trust, talent, culture/energy | Transcript: "what data do you have… Distribution I think is like a really big thing… great people… center of gravity"; energy/culture dim appears in the same segment | **verified** (fourth dim partially captured in transcript excerpt) |
| 8 | "Are you a VC?" — judge jobs by product love, not valuation | Verbatim, twice | **verified** |
| 9 | Non-traditional entry: forward-deployed roles, agent PM (Decagon), skip job at early startup | Verbatim: "your next job is forward deployed at some startup we've never heard of… so desperate… they put everything on [you]"; Decagon "agent PMs"; four deployment teams | **verified** |
| 10 | Kids' projects: Treasure World (math), Story World (figurines with memory) — JZ; baby-shower agent, swim-lesson watcher, college-application systematization, eating-habit app (+20%) | All verbatim in transcript; the Claude Code tool attribution for Treasure World is plausible but the segment also mentions OpenClaw-era context | **verified; tool attribution plausible-not-pinned** |
| 11 | Burnout: *Grit* (Duckworth), flow state vs constant calculus, "what are you not going to regret", baby's first Halloween vs career talk | All verbatim | **verified** — digest's 《怪力》 title is wrong (*Grit* = 《恆毅力》) |
| 12 | JZ: AI "literally makes us able to do all the things"; Yale/Stanford/Reforge curriculum rebuilding | Description + transcript verbatim | **verified** |

## TeaPrompt Contract Map

| Stream/digest mechanism | Existing surface | Disposition |
| --- | --- | --- |
| Career entry via forward-deployed/agent-PM roles; skip-job strategy | [ai-engineer-jobs-survey-2026-11-17.md](ai-engineer-jobs-survey-2026-11-17.md) (AIJ-DOC1) — same claim class: production duties ≠ prior production-AI qualification | Reference — extends AIJ's employer-side evidence with practitioner-side advice |
| Same-prompts personal benchmark across model generations | `golden-benchmark-runner` managed skill; eval/harness methodology | Already present as methodology — the podcast is a practitioner instance |
| Token rationing vs ROI visibility | [token-quota-decomposition-survey-2026-11-09.md](token-quota-decomposition-survey-2026-11-09.md) | Reference — Amjad's power-law-ROI argument is a second source for the same problem; still speaker-reported |
| Agent-as-another-user in a collaborative substrate (transactional FS, infra-as-tools) | `durable-objects`/`sandbox-sdk` host-runtime concerns; trust-boundary doc | Architecture observation; no prompt/skill contract gap |
| Grief cycle / identity-small / surf-the-wave | PROJECT_KNOWLEDGE "methodology over identity" is adjacent but not identical | General career frame — no contract |
| Enterprise guardrails vs reckless vibe-code competitors | 06-repo security gates, Human Review Required, blast-radius | Already present and stronger |
| Historian/technologist/anthropologist; curiosity > roadmap; flow/regret minimization | — | Career advice; outside TeaPrompt's engineering-prompt scope (record-only) |

## Candidate Adoption Ledger

| ID | Candidate | Decision | Reopen condition |
| --- | --- | --- | --- |
| FW-DOC1 | This dated record + catalogue navigation | **Adopted — reference documentation only** | Transcript corrections, a corrected human transcript, or new digest versions |
| FW-SK1 | Any Skill or prompt-body change from these videos | **No change** | A reproduced defect in a named existing surface; these are career/business sources, not harness mechanisms |
| FW-RULE1 | "Outsourcing industry is dead", "80% flip in one hour", "10X→100X/1,000X productivity law", "all code will be AI-written (post-2025 consensus)" as operating rules | **Rejected** | All are speaker self-reports or rhetorical claims inside an interview; none is a reproduced measurement. The AIJ record's own standards (unestablished thresholds, self-reported ≠ measured) apply |

## Evidence vs Inference

- **Verified:** both videos' identities, dates, durations, guest lists; every verbatim claim in the fidelity ledgers.
- **Verified as speaker self-report only:** $10M→$250K replacement figures, 50–60% pre-agent AI code share, 70% launch failure rate, 80%→20% anxiety flip, 100X/1,000X ROI power law, "model companies reached out", "outsourcing is sort of dead", telecom-hackathon survey.
- **Secondhand by speakers:** JZ's benchmark practice is credited to "Delsy"; Amjad's enterprise anecdotes are customer-relayed.
- **Inference (mine):** contract-map dispositions; the ~full-fidelity rating for Video 1 and the identity-correction list for Video 2; classifying the digest's added readings/analysis.
- **Unknown:** whether the digests' author intended the ASR names literally or knowingly normalized them; the fourth moat dimension's exact wording (transcript segment partially captured); whether "Delsy" is a prior Skip episode guest (description confirms the podcast exists; the guest identity is plausible).

## Risks, Falsifiability, and Handoff

- Both transcripts are auto-generated; the Video-2 ASR systematically mislabels JZ ("Jay Z") and Laurel ("Lauren"). A reader trusting the ASR labels verbatim — as the digest partially did — will misattribute speakers. Any future citation should use the corrected names.
- The business figures in Video 1 (replacement-cost deltas, power-law multipliers, anxiety flip) come from a CEO selling a platform; treat as marketing-adjacent self-report, not measured effect.
- The PG/Masad digest's reading list adds *Do Things that Don't Scale* — correct PG canon, but not named in the stream; citing it "per the video" would be a misattribution.
- **Handoff:** this completes the two digests flagged in `pi-creators-stream-survey-2026-11-17.md`. Delivered repository scope: this record, the external-adoption catalogue, and regenerated `index.json`. No prompt body, Skill, routing, governance, or runtime changes.
