# Ambition Prompts Survey — Rieseberg's Altitude/Depth/Range Tutorial (2026-11-14)
Language: English

> **Status: reference documentation and navigation adopted (`AMB-DOC1/2`); no Skill, operating-rule, or runtime change.** The owner shared a Business Weekly syndication link and asked for a survey. This record preserves the source chain, a fidelity check against the primary essay, and the mapping to existing TeaPrompt contracts. It does not authorize a new Skill, prompt edit beyond the two cited surfaces, or any claim that the tactics improve outcomes.

## Research Question and Direct Recommendation

What does the syndicated article add beyond its primary source, is it faithful, and does any tactic expose a missing delivered TeaPrompt contract?

**Record the source-qualified map; leave Skills unchanged.** All three tactics and the enabling precondition map to existing contracts; the strongest single contribution is the four-question depth prompt, which is already covered point-for-point by current rules. The Business Weekly / Business Next (數位時代) version is a faithful paraphrase with one disclosed editor-added prompt, one added biographical detail, and three omissions. It is reference reading, not a mechanism.

## Version and Source Identity

Checked 2026-11-14. The shared short URL `https://share.google/MHPNNrY5eHNgdi5hi` resolves to the Business Weekly page.

| Item | Identity | Reuse / accuracy boundary |
| --- | --- | --- |
| [Business Weekly 商業周刊 article](https://www.businessweekly.com.tw/careers/blog/3023561) | `用同樣的AI成果差幾百倍？Anthropic主管公開3大「野心提示詞」`, author 李先泰, published 2026-11-12, modified 2026-11-12T16:32:51 (NewsArticle JSON-LD). Fetched body SHA-256 `cd298308…a194516a`. | zh-TW syndication of the Business Next article; full text readable without login at fetch time. |
| [Business Next 數位時代 original](https://www.bnext.com.tw/article/92896/claude-ambition-altitude-depth-range) | `別讓AI只做雜事！Anthropic主管公開「野心提示詞」3招`, same author, dated 2026-11-03. | Primary Chinese edition; the BW page carries its text verbatim per the page's own 來源 attribution. |
| [Felix Rieseberg, “How to be more ambitious: A tutorial for humans with models”](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/) | Published 2026-10-13, tagged `claude`, ~8 min. Fetched body SHA-256 `777ffbba…ad6531`; etag `W/"7e22-X9m4KosZvv6xGYGcwDq6kQJdxxc"` observed 2026-11-14. | Primary English source. Author states EM at Anthropic (led engineering for Claude.ai, Cowork, Claude Code Desktop), Electron co-maintainer; self-described, not independently verified. |
| [Gizmodo, “Did Claude Help an Amateur Astronomer Discover a New Planet?”](https://gizmodo.com/did-claude-help-an-amateur-astronomer-discover-a-new-planet-2000824393) | Webb Wright, published 2026-10-09. | Backs the article's hedged exoplanet claim: Pavel Rabtsevich, 28-year-old product manager in Spain, TESS data, candidate TIC 4206066, report submitted for review — **candidate, not confirmed**. |
| [Locke & Latham retrospective](https://med.stanford.edu/content/dam/sm/s-spire/documents/PD.locke-and-latham-retrospective_Paper.pdf) | Goal-setting research review cited by both the essay and the zh article. | Cited, not re-derived; used only as the article's own attribution for the hard-goals claim. |

No upstream code or prompt body is copied into TeaPrompt's operational assets. Refresh on a changed page, a confirmation/refutation of the planet candidate, or a revised Rieseberg essay.

## Fidelity Check: Chinese Article vs Primary Essay

The zh article is a restructured paraphrase, not a translation of record. Checked point-by-point against the English original.

| zh article claim | Original text | Verdict |
| --- | --- | --- |
| Four directions: 速度、高度、深度、廣度 | Speed, Altitude, Depth, **Range** | faithful; English names differ （高度=Altitude, 廣度=Range) |
| Three staged QBR prompts (data → decisions → redesign) | Three escalating QBR asks, quoted verbatim | faithful |
| Crash example: “讓我們的App保持不當機”, plus fetching crash reports, version→commit mapping, three-OS repro machines | Same, including the workflow-enabling precondition | faithful |
| Depth: expert instruments, unreasonable-goal trick, challenge-what-you-know, produce-new-knowledge, outside judge (“in October 2026 … outside validation”) | Same five techniques; original stresses “Do not ask the model to judge itself” | faithful |
| Four-question depth prompt, verbatim | Same prompt, verbatim | faithful |
| Range: nouns→verbs from *The Art of Innovation* (Kelley & Littman); crew incl. short seller + forensic accountant red team; “do what a short seller does”, not role play | Same, including the role-play warning | faithful |
| Range complete prompt block | **None in the original** | editor-added; the article itself discloses this (“原文沒有給這一招的完整提示詞…可整理出參考提示詞”) |
| Precondition: computer that installs software + data access (MCP) | Same closing requirement | faithful |
| Limits: best for outcome-seeking work, weaker for creative; “Claude, go make money” doesn't work in 2026 | Same | faithful |
| Dantzig, self-efficacy, Locke & Latham 2002 | Same, in the original's “We have been here before” section | faithful |
| “一名沒有天文專業背景的產品經理 … 可能發現一顆新的系外行星” | Original says only “it may have helped discover a new planet” | qualified: product-manager detail comes from Gizmodo (verified above); “可能/仍待確認” hedge retained — **not an embellishment, an added citation** |
| — | Michelangelo/Sistine, Bannister four-minute mile, **Sabastian (sic) Sawe** sub-2-hour marathon, *The Inner Game of Tennis*, Linux “just a hobby”, Collison “Fast” list | omitted by the zh article; noted here so the record is not silent |
| — | Original spells the runner “Sabastian Sawe”; the athlete's name is **Sebastian Sawe** | minor typo in the primary source; retained, not corrected |

## What the Source Adds vs Existing Contracts

| Tactic | Existing TeaPrompt coverage | Gap? |
| --- | --- | --- |
| Altitude: hand the outcome, not the task; meetings-worth-discussing as the tell | `reflective-brief` step 1–2 “Identify the real goal / Clarify the intended user outcome (job-to-be-done)”; durable-workflow note matches `flow-control-generator`'s trigger design | None — same move, richer examples |
| Depth question 1–3: what a top professional would do, the **rawest** material, named methods/tools | `reflective-research` source hierarchy / primary-over-digested rule; evidence-first practice | None |
| Depth question 4: “what, other than you or me, would show the result is right” — outside judge; don't let the model judge itself | `flow-loop-harness` external-verifier requirement; `runtime-trust-boundary` acceptance vs producer; verification-map falsifiers | None — explicit restatement |
| Unreasonable-goal insistence (“ask for 200ms”) | None — deliberately **not** adopted: it invites confident unsupported output; the library prefers falsifiable bars | Rejected candidate (AMB-RULE1) |
| Range: nouns→verbs, assemble a cross-field crew incl. an adversarial seat | `reflective-brief` reframes the task; [Parallel Lens Review](../04-agent/workflow-recipes.md#parallel-lens-review) describes how to compare independent perspectives | A review method, not a supplied group of agents |
| Enabling precondition: model needs a computer, software installation and data access | [Runtime Trust Boundary](../04-agent/runtime-trust-boundary.md) separates requested tools and permissions from those the host provides | A host prerequisite; TeaPrompt grants none of this access |
| Creative-work caveat; “go make money” doesn't work in 2026 | Honest limitation, matches library's falsifiability posture | None |

## Optional Worked Reference — Delegating the Outcome, Not the Task

Rieseberg's own progression is the cleanest illustration of an existing TeaPrompt rule: at the start of 2025 he asked Claude to fix individual crashes (a task); later he delegated “keep our apps crash-free” (an outcome). The delegation only worked **after** the workflow was rebuilt so the model could fetch crash reports, map app versions to git commits, and reproduce and verify fixes on Windows, macOS, and Linux machines.

Applied to the library: `reflective-brief`'s step “Identify the real goal … job-to-be-done” plus `flow-control-generator`'s external trigger design already require this move. The source adds one operational detail worth keeping: **raising the altitude of a delegated outcome requires investing in the model's verification loop first** — tools to observe, reproduce, and check — not just a bigger prompt. The QBR ladder (data → decisions → redesign the review itself) is the same shape as `workflow-acquisition`'s promote-only-what-you-can-replay gate.

This is a source-qualified example, not a new workflow or an efficacy claim: every success story in the essay is anecdotal (planet candidate, 3D homepage, crash-free apps), none measured.

## Candidate Adoption Ledger

| ID | Candidate | Disposition | Evidence / reopen trigger |
| --- | --- | --- | --- |
| AMB-DOC1 | This source-bound record and its catalogue row | Adopted; documentation only | Owner asked to survey the link. Refresh when the pages change, the planet candidate is confirmed/refuted, or a v2 essay appears. |
| AMB-DOC2 | Optional worked-reference links appended under `business-strategy.md`'s existing Optional Worked Reference section, outside its prompt fence | Adopted; navigation only | Keeps the outcome-vs-task example discoverable without changing the prompt's output contract. |
| AMB-SK1 | New Skill or edit to `reflective-brief`/`reflective-research` | No change | Every tactic maps to an existing contract; no verified local gap. |
| AMB-RUN1 | Install or wire anything from the article | Not adopted | Source is an essay; nothing to run. |
| AMB-RULE1 | Adopt “set unreasonable goals, insist they're reasonable” or the editor-added Range prompt as a rule | Rejected | Unreasonable-goal insistence invites unsupported confident output; contradicts falsifiability. The Range prompt is editorial, not from the primary source. |

## Evidence vs Inference

- **Verified (primary essay):** the zh syndication is a faithful restructured paraphrase — four directions, staged QBR prompts, crash workflow, depth techniques, Range red-team tactic, closing precondition — checked point-by-point against the English original.
- **Qualified (external check):** the "product manager discovered an exoplanet" detail comes from Gizmodo, not the essay; retained with its hedge. The Range complete prompt block is editor-added and disclosed as such by the zh article itself.
- **Omitted-not-adjudicated:** Michelangelo/Bannister/Sawe/Inner Game/Linux anecdotes dropped by the syndication; "Sabastian" typo in the primary source retained, not corrected.
- **Inference (this record):** contract-map dispositions; the "no missing delivered contract" verdict; AMB-DOC1/2 adoptions.
- **Unknown:** whether the TIC 4206066 candidate is a real discovery; whether the tactics improve outcomes for anyone outside the essay's anecdotes.

## Falsifiability

- A reproduced local failure where `reflective-brief`'s outcome step provably underperforms a task-level ask would demote AMB-SK1's “no gap” verdict; a single anecdote, a model call, or a translation quibble would not.
- If the TIC 4206066 candidate is refuted, the Gizmodo row is corrected but the adoption dispositions stand (they never depended on it).
- The zh article's added biographical detail and omitted anecdotes are recorded, not adjudicated as errors; syndication edits are expected.

## Standing Non-Goals

No Skill edit, no prompt edit beyond the cited surfaces, no model call, no install, no efficacy or safety claim about the tactics. Commit/push remain unperformed pending owner direction.
