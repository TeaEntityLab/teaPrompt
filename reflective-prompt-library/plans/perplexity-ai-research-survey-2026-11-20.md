# Perplexity "AI Research" Survey — Content Fidelity and Contract Map (2026-11-20)

Language: English

> **Status:** source-qualified reference record (`PAR-DOC1`); no Skill, prompt-body, operating-rule, or runtime change. The owner supplied `perplexity.ai/hub/blog/ai-research`. This record reads the full article via an accessible mirror and checks its claims; it is a vendor-published consumer guide, not a research-mechanism disclosure. No installs, model calls, Skill changes, commits, or pushes are authorized.

## Research Question

Does the article contain transferable mechanisms or claims missing from TeaPrompt, or is it a conventional evergreen explainer whose substance maps to existing contracts?

## Direct Recommendation

**Adopt the record only.** The article is a conventional evergreen guide — a milestone timeline, an institution/tool taxonomy, a four-way task map, and a seven-step usage framework — with no novel mechanism beyond what `reflective-research` and the external-verifier rules already require. Its factual anchors (timeline entries, the 257,890-publications figure, the "GPT 6.1-Sol" model name) are either standard history or vendor product naming, not survey-grade evidence of anything new. No local gap; no adoption.

## Evidence Used

| Source | Class | What it supplies |
| --- | --- | --- |
| [Perplexity article](https://www.perplexity.ai/hub/blog/ai-research) via `r.jina.ai` mirror | **Primary text** (full markdown retrieved; direct fetch blocked by Cloudflare) | Verbatim basis for every claim classification |
| Wayback lookups, 2026-11-20 | For `perplexity.ai/hub/blog/ai-research`, the [availability query](https://archive.org/wayback/available?url=perplexity.ai/hub/blog/ai-research) returned `archived_snapshots: {}` and the [CDX query](https://web.archive.org/cdx/search/cdx?url=perplexity.ai/hub/blog/ai-research&output=json&limit=5) returned `[]` | Neither query returned a capture; this does not rule out captures outside those results |
| Owner-supplied URL | Target | Confirms the intended page, not the newer "Frontier Research" post (`/introducing-perplexity-frontier-research`, 2026-11-16) |

**Access notes:** direct fetch returns HTTP 403 (Cloudflare). The mirror supplies complete article text including image captions and the seven-step framework; rendering artifacts (e.g., the institution table's flattened layout) are cosmetic, not content gaps. Publication date is not stamped on the page; search indexing puts it ~1 month old (mid-October 2026).

## Claim Classification

| # | Article claim | Check | Verdict |
| --- | --- | --- | --- |
| 1 | Milestone timeline 1943–2022 (McCulloch-Pitts, Turing, Dartmouth, perceptron, backprop, LSTM, ImageNet, GAN, AlphaGo, Transformer, few-shot, ChatGPT) | Standard published history; citations supplied to DOI/publisher pages | **verified** — conventional, correct |
| 2 | Six "important recent developments" 2025–2026 (DeepSeek-R1, s1, AlphaEvolve, Genie 3, AlphaGenome, Co-Scientist) | All real publications with correct venues (arXiv, Nature, DeepMind blog) | **verified** — selection is editorial, not exhaustive |
| 3 | "257,890 AI publications in 2024 (Stanford 2026 AI Index)" | Figure is the report's self-published count; the article cites it without independent verification | **verified as cited** — single-source metric |
| 4 | Four task categories (information retrieval, analysis, decision-making, evaluation/diagnosis) | Matches the Microsoft Copilot-sessions study it cites | **verified as cited** — taxonomy is the study's, not the article's |
| 5 | Tool taxonomy (Perplexity/ChatGPT/Claude/Gemini; Semantic Scholar; Elicit/SciSpace; ResearchRabbit/Connected Papers; Scite/Consensus) | Real tools, accurate capability descriptions | **verified** |
| 6 | "GPT 6.1-Sol" product name in the example | Internal Perplexity naming for a routed model; not independently verifiable | **vendor naming** — recorded, not fact-checked |
| 7 | Benefits/drawbacks (automation, non-specialist access, hypothesis testing, hallucination, oversimplification, skill erosion, incompleteness) | All standard, sourced claims | **verified** — no novel mechanism |
| 8 | Seven-step framework (time calculation → tool choice → T&Cs → legal data → prompt practice → fact-check → disclose) | Matches `reflective-research`'s source hierarchy, primary-source rule, external-verifier rule and disclosure duty | **verified** — all already present in TeaPrompt contracts |

## TeaPrompt Contract Map

| Article element | Existing surface | Disposition |
| --- | --- | --- |
| Source hierarchy and fact-check duty | `reflective-research` source hierarchy, primary-source rule | Already present and stricter (article is a vendor guide; our rules are evidence-bound) |
| T&Cs / data-confidentiality / legal-constraint check | `teaprompt-project-primer` supply-chain + trust-boundary docs | Already present |
| Prompt practice (clear question, context, output format, citations) | `reflective-brief` + `reflective-research` method sections | Already present |
| Disclosure of AI use | `teaprompt-project-primer` AI-transparency convention | Already present |
| Tool taxonomy (general vs dedicated research tools) | `find-skills`/external-survey precedent | Reference content, not a contract |
| "AI as supplement, not replacement" | PROJECT_KNOWLEDGE methodology principle | Already present |

## Candidate Adoption Ledger

| ID | Candidate | Decision | Reopen condition |
| --- | --- | --- | --- |
| PAR-DOC1 | This dated record + catalogue navigation | **Adopted — reference documentation only** | A corrected article, a different edition, or a local consumer failure |
| PAR-SK1 | Any Skill/prompt-body change from this article | **No change** | A demonstrated gap in `reflective-research` or `reflective-review`; the article restates both |
| PAR-RULE1 | The four-task taxonomy or seven-step framework as an operating rule | **Rejected** | A consumer-guide checklist is not an invariant; adopting it would add a second convention |

## Evidence vs Inference

- **Verified:** article text (full markdown via mirror); all timeline entries; the four-task taxonomy; tool names and capability descriptions; the seven steps.
- **Verified as cited only:** 257,890 publications (single-report figure), Copilot-sessions study existence.
- **Inference (mine):** the "conventional evergreen guide" verdict; the no-gap contract call; the "no adoption" disposition.
- **Unknown:** exact publication date (not stamped); whether “GPT 6.1-Sol” is a model alias or marketing shorthand; whether the mirror preserved every figure and caption (direct fetch was blocked); whether other archive captures exist.

## Falsifiability, Risks, and Handoff

- A later-edited version of the article (Perplexity rewrites evergreen guides) could change the claims; the mirror fetched 2026-11-20 is the authoritative copy for this record.
- The linked "Frontier Research" post (`introducing-perplexity-frontier-research`, 2026-11-16) is a separate announcement about autonomous discovery — deliberately out of scope; if the owner intended that post, it is a separate survey.
- Delivered scope: this record, the external-adoption catalogue, and regenerated `index.json`. No prompt-body, Skill, routing, governance, or runtime changes.
