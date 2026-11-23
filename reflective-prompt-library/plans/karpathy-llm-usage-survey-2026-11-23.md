# Karpathy “How I use LLMs” Digest Survey — Fidelity Check and Contract Map (2026-11-23)

Language: English

> **Status:** source-qualified reference record (`KLM-DOC1`); no Skill, prompt-body, operating-rule, or runtime change. The owner supplied `local://paste-27.md`, a zh-TW article by Paul Kuo (郭曜郎, `paulkuo.tw`, dated 2026-11-22) digesting Andrej Karpathy's YouTube lecture “How I use LLMs” (`EWvNQjAaOHw`). This record checks the digest against the video's full English transcript and chapter metadata, then maps the article's advice onto existing TeaPrompt contracts. It does not install a tool, adopt a prompt, or authorize a model call.

## Research Question and Direct Recommendation

Is the zh-TW digest faithful to Karpathy's source, and does anything in it expose a TeaPrompt Docs or Skill gap?

**Record the fidelity and the contract map; do not adopt.** The digest is a faithful restructured paraphrase of the source: every checkable example matches the transcript, the arithmetic is correct, and the chapter anchor it names resolves to a real YouTube chapter. Its five-part tool-selection frame (general chat → reasoning → web search → deep research → file upload) is Karpathy's own ordering from the lecture. TeaPrompt already requires the load-bearing habits — identify the missing ingredient before asking, convert claims into checkable gates, verify by recomputing what a tool produced, keep the falsifier — so there is no missing delivered contract to repair.

## Evidence Used and Date Context

Checked 2026-11-23. Video: [Andrej Karpathy, “How I use LLMs”](https://www.youtube.com/watch?v=EWvNQjAaOHw) (accessed 2026-11-23; uploaded 2025-02-27, duration 2:11:12). Digest: `local://paste-27.md` supplied by the owner (zh-TW article dated 2026-11-22; the digest names an X repost by `@tyay2015` as its discovery path).

| Item | Identity | What this check covers |
| --- | --- | --- |
| Video metadata | `EWvNQjAaOHw`, upload_date `20250227`, duration 7872 s | yt-dlp metadata and full chapter list; oembed title/author cross-check |
| Transcript | English auto-generated VTT (en + en-orig, identical), cleaned to 3,475 timestamped lines | Every digest example located and compared below |
| Arithmetic | `423,534 × 3,124` | Independently recomputed |

## Fidelity Check: Digest vs Transcript

The zh article is a restructured paraphrase, not a translation of record. Point-by-point against the cleaned transcript:

| Digest claim | Transcript | Verdict |
| --- | --- | --- |
| 2015 valuation `N/A` became `0.1` in code — “這一填，就多出一億美元” | 01:05:54 “we had na for 2015 … it put in 0.1 … the valuation of 2015 was 100 million” | faithful; the 億 math is correct (0.1 × $1B = $100M = 一億) |
| Karpathy asked ChatGPT to research OpenAI valuations, then plotted | 01:05:02 “let's research openai evaluation … use the search tool … plot this, log scale” | faithful |
| Gradient-check failure → thinking model found the pack/unpack parameter order mismatch; non-thinking GPT-4o listed debugging directions instead | 00:25:31–00:27:39: `o1-pro` “noticed that the parameters are mismatched and how I pack and unpack them”; GPT-4o gave issues but “didn't really solve the problem” | faithful |
| Same code to different models: some listed directions, some found the issue | 00:27:41–00:28:29: Claude 3.5 Sonnet, Gemini, Grok 3 all solved it | faithful |
| White Lotus season 3 next-episode search | 00:31:38–00:35:03 “when are new episodes of white lotus season 3 getting released” | faithful |
| Multi-lab size/funding comparison missed xAI | 00:50:14 “hit and miss … xai is not here … hugging face should probably not be here … EleutherAI shouldn't count” | faithful; digest omits the two extra rows Karpathy also flagged (Hugging Face, EleutherAI) |
| Wealth of Nations: paste the chapter being read, ask about it | 00:55:10–00:56:42: Adam Smith 1776, Project Gutenberg, division of labour chapter pasted | faithful |
| A paper PDF exceeded the context limit → switched interface | 00:52:37–00:53:55: a PDF dropped into Claude hit “the limit of this chat” and he switched tools | faithful |
| `423,534 × 3,124` via Python interpreter, showing formula and output `1,323,120,216` | 00:59:54–01:01:46: multiplication example delegates to the Python interpreter; recomputed: `423534*3124 = 1323120216` — matches | faithful; digits verified independently |
| Start a new chat to change topics | 00:16:34 “always start a new chat”; 00:30:28 “when I start a new conversation” | faithful |
| `1:04:35 資料分析` chapter anchor | Real chapter: `01:04:35 ChatGPT Advanced Data Analysis, figures, plots` | faithful; digest shortens the chapter title |

## What the Digest Adds, Omits, and Reframes

- **Added (author's own, correctly framed):** the five-row zh-TW prompt table (一般對話/推理/搜尋/深度研究/上傳原文) with copyable templates, the weekly-report example (“兩週要比相同天數，缺值留空”), and the “別讓一格空白默默變成零流量” rule. These are the digest author's application, not Karpathy's words, and the article presents them as such.
- **Omitted, not misreported:** the second valuation anomaly (the printed `2027 1.7B` trend-line that implied 20 trillion while claiming 1.7 trillion — 01:06:56–01:07:49), the Hugging Face/EleutherAI inclusion errors beside xAI, the Grok-3 hallucinated multiplication (digit transposition `120`→`060`), Claude Artifacts/Cursor/audio/NotebookLM/image/video/memory chapters (the lecture's second half), and Karpathy's caveat that he “would be hesitant to recommend these tools if people aren't able to read and verify” the generated code.
- **Reframed:** “資料還是推理” is the digest's organizing frame over Karpathy's tool-list; the five tool buckets exist in the video but not as that binary question. The “能回去核對” delivery condition is the author's synthesis, consistent with Karpathy's “scrutinize the code” advice.

## Contract Map

| Digest advice | Nearest TeaPrompt surface | Already required? |
| --- | --- | --- |
| Identify what's missing before asking (data vs reasoning) | `reflective-brief` goal/assumption/acceptance clarification | Yes |
| Convert ambition into checkable gates before acting | `reflective-brief` acceptance criteria + falsifiability; `flow-loop-harness` external verifier | Yes |
| Check the actual code/tool output, recompute a number, read the generated program | `reflective-review` evidence tiers (self-assessment last); `04-agent/runtime-trust-boundary.md` execution-vs-acceptance | Yes |
| Leave missing values missing rather than silently zero-filling | `reflective-review` unverified-vs-refuted distinction; record-hygiene `unknown ≠ zero demand` convention | Yes |
| Scope the comparison before deep research | `reflective-research` source hierarchy and scope-first method | Yes |
| Start a fresh chat when the task changes | `03-context/context-handoff.md` and context-engineering rules | Yes |

## Candidate Adoption Ledger

| ID | Candidate | Disposition | Evidence / reopen trigger |
| --- | --- | --- | --- |
| KLM-DOC1 | This record and its catalogue row | Adopted: documentation only | Bare survey. Refresh if the video's transcript is corrected or the article's claims are updated. |
| KLM-SK1 | New Skill, or an edit to an existing Skill or prompt contract | No change | No verified local structural gap. The five-bucket tool selection is ChatGPT-product UI, already covered at the decision level. |
| KLM-RUN1 | Adopt the digest's zh-TW prompt templates as TeaPrompt prompt bodies | Not adopted | Product-UI templates for ChatGPT's tool picker; TeaPrompt's prompts are harness-level contracts. No local need reproduced. |
| KLM-RULE1 | Require “identify missing data vs reasoning” or “verify the plotted code” as a new TeaPrompt rule | Rejected | Both are weaker restatements of `reflective-brief`/`reflective-review` clauses already in force. |

Missing local usage data remains `unknown`, not zero demand.

## Evidence vs Inference

- **Verified (transcript):** every fidelity row above — the `N/A`→`0.1` code substitution, the 100M/一億 equivalence, gradient-check model behavior, White Lotus, xAI/HuggingFace/EleutherAI omissions, Wealth of Nations, the PDF context-limit switch, the Python-interpreter multiplication, the new-chat advice, and the `1:04:35` chapter anchor.
- **Verified (independent recompute):** `423534 × 3124 = 1323120216` exactly matches the digest's on-screen output.
- **Verified (metadata):** `EWvNQjAaOHw`, title “How I use LLMs”, author Andrej Karpathy, upload 2025-02-27, duration 7872 s, 22 chapters including `01:04:35 ChatGPT Advanced Data Analysis`.
- **Author-reported (unverified):** the `@tyay2015` X repost as discovery path (not fetched); `paulkuo.tw` as the article's canonical host (the paste itself is the checked artifact); the digest's claim the video was “從一則 X 轉貼找到的”.
- **Inference (this record):** contract-map dispositions; the “no missing delivered contract” verdict; KLM-DOC1 adoption.
- **[INFERENCE]** The digest's five templates would work as pasted; not executed — no model call was made.
- **Unknown:** whether the ASR transcript has errors in unquoted spans; whether the zh article was later updated after this paste; whether Kuo's earlier 〈用 AI 整理新聞〉 article supports the “檢索、整理和查核分開做” claim as quoted.

## Falsifiability

- A corrected YouTube transcript showing the `0.1`/`N/A` or multiplication segments differ from the ASR text would correct the matching fidelity rows; the contract dispositions do not depend on them.
- A reproduced local failure of an existing brief/review contract — for example a verification step that accepted a tool's output without inspecting what it computed — would reopen the gap verdict; this survey does not show one.
- If the X repost proves to be a different video or date, the discovery-path note is corrected but no disposition changes.
- A later upload-date or title change on `EWvNQjAaOHw` updates freshness only after a new pin is recorded.

## Standing Non-Goals

No model call, no skill install, no prompt-body adoption, no product or UI evaluation, no claim that the digest's templates produce good output. The lecture's second half (Cursor, voice, image, video, memory, custom GPTs) is recorded as out-of-scope content, not surveyed. Commit/push remain unauthorized by this record.
