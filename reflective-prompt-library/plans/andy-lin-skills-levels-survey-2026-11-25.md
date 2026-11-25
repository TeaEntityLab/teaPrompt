# Andy Lin "Skills 六個層級" Video Survey — Source Fidelity and Contract Map (2026-11-25)

Language: English
> **Status:** source-qualified reference record (`ALV-DOC1`); no Skill, prompt-body, operating-rule, or runtime change.**

The owner asked to survey this video's original source and content, and to consider Doc or Skill updates. The video is a **third-hand source**: Andy Lin's zh-TW adaptation (2026-11-24, 8:42) of Jay E | RoboNuggets' "Anthropic's Engineers Stopped Building AI Agents" (2026-11-23, 16:34), itself summarizing Anthropic's engineering post and a Boris Cherny interview. This record separates the video's claims from the owner's supplied reflection, checks each against primary sources, and maps them onto existing TeaPrompt contracts. It does not call a model, install tooling, or authorize a runtime.

## Research Question and Direct Recommendation

Which claims survive source-checking, and does the skills-over-agents framing expose a TeaPrompt Docs or Skill gap?

**Record the boundaries; the framing largely restates TeaPrompt's own architecture.** Anthropic's primary post does *not* say "stop building agents" — it says general-purpose agents already exist and **skills make them composable/specialized** ("instead of building fragmented, custom-designed agents for each use case, specialize your agents with composable capabilities"). The video's headline is a simplification. The owner's core inference — invest in the skill layer over per-task agents or per-model routing — is defensible for a one-person cost/effort budget and is literally TeaPrompt's architecture (one harness, prompt-layer skills). The brain-science analogy is rhetorical, not evidence.

## Evidence Used and Date Context

Checked 2026-11-25. The target video has no captions; a local Whisper `tiny` transcript (noisy, zh-TW) was generated for content verification. The owner supplied a zh-TW reflection alongside the link.

| Item | Identity | What this check covers |
| --- | --- | --- |
| Andy Lin video | `C9XzsJF-FNY`, 2026-11-24, 8:42 | Title, description, six-level ladder, claims; Whisper tiny transcript |
| Source video | `IMSYKloMFrE`, RoboNuggets, 2026-11-23, 16:34 | Provenance of the "engineers stopped building agents" framing |
| Anthropic engineering post | "Equipping agents for the real world with Agent Skills" (Zhang/Lazuka/Murag, 2025-10-16) | What Anthropic actually claimed vs. the video's retelling |
| Boris Cherny quote | YC Startup School interview, ~2026-07 | "Every 6 months delete your CLAUDE.md, skills, hooks — the model might not need them" — corroborated by independent search |

## What the Video Claims (via transcript + description)

- **Framing:** Anthropic engineers "stopped building an agent per task"; model = CPU, agent = OS, skill = app. One general agent + skills > a fleet of agents.
- **Architecture:** model → harness (system prompts) → skills directory; skills are "an open standard… over 70 AI platforms adopted the same format."
- **Six levels** (creator's ladder, partially garbled in transcription):
  - L1: describe the job, let the official skill creator generate the skill.
  - L2: do the task once with the agent, then "skillify" the session — *"level 2 is how I recommend most people create their skills."*
  - L3: screen-record the task while narrating; the agent proposes a skill from the recording.
  - L4–L5: partially garbled — L4 appears to cover skills teaching tool/API use without connectors; L5 unclear.
  - L6: **periodic skill deletion** — Boris Cherny's advice to delete CLAUDE.md/skills/hooks and see what newer models do, because detailed accumulated instructions "can actually end up holding the model back."

## The Owner's Reflection — Checked Separately

| Claim | Verdict |
| --- | --- |
| Skill-routing across skills is more practical than model-routing across providers | Defensible heuristic for a personal workload; restates TeaPrompt's architecture (prompt-layer skills, one harness). Not a general law — the video and this reflection argue from one cost/convenience frame |
| "Others paying for subscriptions and switching models were just busy work" | Value judgment on others' workflows; unverifiable and out of scope for adoption |
| The brain analogy ("生物大腦也是這樣運作") | Rhetorical reinforcement, not mechanistic evidence; biological routing is not shown to map onto skill selection |
| Historical claim: McCulloch–Pitts 1943 neuron model; Hebb "fires together, wires together"; early AI researchers and neuroscientists were the same circle | Accurate as history (1943 paper, Hebb 1949); but historical genealogy does not validate the design argument — kept as context, not support |
| "我原先一直以爲,所有的模型本該都是這樣子玩的" (owner's prior assumption) | Personal calibration note; TeaPrompt's existence as a skill library already embodies the assumption |

## Evidence vs Inference


- **Verified:** video identity/duration; source-video identity; the Anthropic post's actual claims (read in full); `agentskills.io` open-standard status (confirmed live in the 2026-11-24 survey); the Cherny deletion quote corroborated by an independent search (YC interview, July 2026); the six-level structure exists in the video (L1/L2/L3/L6 verified in transcript).
- **Supplier-summarized (unverified):** "70+ platforms" adoption count (vendor claim via the video); the RoboNuggets retelling's characterization of "Anthropic engineers"; Whisper transcription of L4/L5 levels (garbled, not relied on).
- **Inference (this record):** that the skills-over-agents framing restates TeaPrompt's existing architecture; that the owner's model-vs-skill routing heuristic is budget-sensible but not universal; that the Cherny quote is a *second independent source* for skill ablation, strengthening the deferred UAS-DOC2 note.
- **Unknown:** whether Anthropic engineers literally said "stopped building agents" in any single primary source (the engineering post does not); whether the 70-platform count is current; L4/L5 ladder content.

## TeaPrompt Contract Map and Disposition

| Finding | Existing surface | Disposition |
| --- | --- | --- |
| One general agent + composable skills > agent-per-task | TeaPrompt north star: nine frozen workflow skills as natural-language policy, no agent runtime | Restated; the video is third-party validation of the architecture, not new mechanism |
| Progressive disclosure (metadata → SKILL.md body → bundled files) | All TeaPrompt skills use frontmatter + body; `teaprompt-artifact-promotion` keeps invocation cheap | Identical mechanism |
| L2 "do it once, then skillify the session" | `teaprompt-artifact-promotion` (successful repeated process → skill candidate); `reflective-handoff-retro` (capture lessons) | Same promotion pattern already required |
| L3 "record yourself doing it, agent proposes the skill" | Host-side capture feature; `teaprompt-artifact-promotion` covers the output, not the input modality | Reference only — capture is a host feature, promotion is TeaPrompt's covered half |
| L6 periodic skill deletion / retirement test | **Corroborates UAS-DOC2 deferred note** (Uber ablation + now Cherny, two independent sources) | Still deferred — TeaPrompt has no eval runtime to run ablations; the note now records two-source corroboration in the ledger |
| "70+ platforms adopted the format" | `agentskills.io` verified as an open standard | Platform count remains a vendor claim; format openness already recorded |
| "Stop building agents" headline | Anthropic post says specialize one agent via skills, not stop building them | Framing flagged as simplification in the record; no contract impact |

## Candidate Adoption Ledger

| ID | Candidate | Disposition | Evidence / reopen trigger |
| --- | --- | --- | --- |
| ALV-DOC1 | This source-bound record and its catalogue row | Adopted; documentation only | Refresh if the primary source (Anthropic post, Cherny interview) or the open-standard adoption data changes |
| ALV-DOC2 | Promote the deferred skill-retirement/ablation note: periodic "delete and see" as a Skill-maintenance practice | Deferred (strengthened) | Two independent sources now endorse it (Uber ablation, Cherny advice); reopen if TeaPrompt ever gains an eval surface or a skill's staleness is questioned with evidence |
| ALV-SK1 | New skill-authoring or skill-retirement Skill | Not adopted | `teaprompt-artifact-promotion` covers authoring; retirement has no eval runtime to execute against |
| ALV-RUN1 | Adopt screen-recording skill capture or any host feature | Not adopted | Host/product surfaces; a TeaPrompt runtime is a standing non-goal |
| ALV-RULE1 | Treat the video's "Anthropic stopped building agents" framing or the brain analogy as evidence for adoption | Rejected | The primary source contradicts the headline's strong form; the analogy is rhetorical, not mechanistic |

## Owner Reflection (Verbatim, Recorded 2026-11-25)

The owner supplied the following reflection alongside the survey request. Recorded verbatim; the analysis table above evaluates each clause. The historical paragraph is accurate and retained as context; the routing heuristic is the defensible kernel.

> 我原先一直以爲,所有的模型本該都是這樣子玩的,但這樣最後整個前因後果看下來,是我自己對這件事的認知有誤了。
>
> 因為我自己從Gemini內建的Gems功能開始,到近期上線取代Gems的Skills,就已經預設默認採取這樣的模式了,而同一時間,其他的用戶們,則默認選擇持續投入大量資金訂閱、持續不斷切換更多的預設模型服務來做比較,就整個結果來說,根本就只是窮忙一場。
>
> 與其同時對多個獨立模型進行路由機制,還不如同時對多個獨立的skills進行路由機制還比較實際,因為生物大腦的運作方式也是如此,這原理連一篇論文都不用去翻就能知道了。這也是過去總有人追問:「為什麼你使用的Google Gemini版本,感覺比我們多數人使用的Google Gemini更顯聰明?」的根本差異,這也僅只是用跨領域知識的角度觀點,去達成這件事的成效結論,因為「既身為人,卻不懂於人」,也是一件很耐人尋味的事,因為我自己本身就已經有一顆活生生、無時無刻都在上線服役中的「生物大腦」了,為何我還需要去翻學術資料研究生物大腦本身的「智慧」是如何運作?在過去我常說:「人工智慧一開始的研究目標,就是在於努力還原重現生物大腦的運作架構。」神經網路的概念可以追溯到 1940 年代,第一個人工神經網路模型由 Warren McCulloch 和 Walter Pitts 在 1943 年開發。他們的工作《A Logical Calculus of Ideas Immanent in Nervous Activity》提出了一個人工神經元的數學模型,靈感直接來自大腦中的生物神經元。McCulloch 和 Pitts 在 1943 年形式化了「整合與放電」(integrate and fire)神經元的概念,而 Hebb 在 1940 年代末首次提出了神經元聯想學習的思想——「一起放電的神經元會連接在一起」(what fires together, wires together)。在那個時代,「想要理解大腦如何運作的人」和「想要建造人工大腦或人工智慧的人」,要嘛是同一批人,要嘛是密切的同事和合作者。換言之——AI 研究者和神經科學家,一開始根本就是同一群人。

**Position distilled:** for a one-person workload, prefer investment in the skill layer (composable knowledge a single agent can route across) over investment in additional model subscriptions or model-level routing. This is a budget/effort heuristic, consistent with TeaPrompt's architecture; it is not a claim that model choice never matters.

## Falsifiability

- A reproduced local failure where a TeaPrompt skill demonstrably holds back current models (measurable regression vs. running without it) would promote ALV-DOC2 into an actionable maintenance practice.
- An Anthropic primary statement matching the video's strong "stopped building agents" claim would upgrade the framing from simplification to verified; none was found — the engineering post says the opposite.

## Standing Non-Goals

- No runtime, Skill, prompt-body, routing, or governance change.
- No model call, notebook, install, commit, or push beyond this record and its catalogue row.
- The owner's brain-analogy and AI-history context are recorded as supplied reflection, not as evidence adopted by this survey.
