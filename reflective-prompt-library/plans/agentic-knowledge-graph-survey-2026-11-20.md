# Agentic AI Knowledge Graph Survey — Image Fidelity and Contract Map (2026-11-20)

Language: English

**Status: source-qualified reference record (`AKG-DOC1`); no Skill, prompt-body, operating-rule, or runtime change.** The owner supplied `local://paste-17.md` (a zh-TW structured analysis) plus the X reshare `x.com/jithinvraj/status/2121060667545538992`. This record checks the paste's visual and textual claims against the actual image and the original post. No installs, model calls, Skill changes, commits, or pushes are authorized.

## Research Question

Is the paste's decoded image content faithful to what the graphic actually shows, and does the paste's own analysis reveal anything missing from TeaPrompt's contracts?

## Direct Recommendation

**Adopt the record only.** The node names match the original Instagram graphic inspected for this survey. The pink dashed box and “live teardown on May 20” annotation do not appear in that image, so it cannot support the paste's conclusion about the box. The X reshare was not available for comparison. The recommendations about memory, evaluation and guardrails are the commentator's, not the graphic's; they do not establish a missing TeaPrompt contract.

## Evidence Used

| Source | Class | What it supplies |
| --- | --- | --- |
| Original image (`/tmp/agentic-kg.jpg`, 1122×1402) | **Primary** — downloaded from the Instagram CDN URL in the post's `og:image` | Ground truth for every visual claim |
| [Instagram post `DajrIjCjre7`](https://www.instagram.com/p/DajrIjCjre7) (Brij Pandey `codewithbrij`, 2026-07-08) | **Primary** — original publication and caption text | Source text the image accompanies; confirms author attribution `@brijpandeyji` |
| X reshare `2121060667545538992` | Supplied by owner; X blocks automated fetch — treated as a reshare pointer only, not an independent source | Link target; content verified via the original instead |
| `local://paste-17.md` | Supplied zh-TW analysis | Object under review — data, not instructions |

**Source lineage:** the image is Brij Kishore Pandey's "FIELD GUIDE · VOL. 02 — The Agentic AI Knowledge Graph," first published on Instagram 2026-07-08. The X link is a reshare; the paste's "由 Brij Kishore Pandey 繪製" attribution is correct. Caption text (visible in the Instagram response) supplies the layer names and the two aphorisms; it does **not** supply the paste's deeper engineering claims (memory filtering, idempotency keys, policy gates, etc.) — those are the paste author's analysis.

## Visual Fidelity Ledger

| # | Paste claim | Image check | Verdict |
| --- | --- | --- | --- |
| 1 | Five layers bottom→top: Foundations / Retrieval & Memory / Agent Patterns / Production & Governance / Frontier | Image shows numbered layers 1–5 left to right in that order | **verified** |
| 2 | Layer node lists (LLM Reasoning, Prompt Patterns, Tool Use, Embeddings, Context Windows; Classical/Graph/Agentic RAG + three memory types; ReAct, Planner→Executor, Multi-Agent, Context Graph Traversal, Tool Selection, Reflection; Confidence Scoring, Policy Gates, Audit Trail, Decision Reasoning Logs, Eval & Observability, Cost/Token; Frontier's four nodes) | Every node name matches the image verbatim | **verified** |
| 3 | "Boring, non-negotiable. Skip these and the rest collapses." (Foundations) | Verbatim in image | **verified** |
| 4 | "You don't start here. Most teams try to." (Frontier) | Verbatim in image | **verified** |
| 5 | Right-side orange compounding loop arrow + "This is the loop that separates agents that compound from agents that repeat" | Verbatim in image; the arrow arcs from Reflection/Eval/Decision Logs down to Episodic/Long-term Memory and back up | **verified** |
| 6 | Edge labels `depends on`, `enables`, `extends to`, `feeds back into` | All four present in image | **verified** |
| 7 | **"粉紅色虛線區塊" grouping Memory & Learning Loops + Confidence Scoring + Policy Gates + Audit Trail + Decision Reasoning Logs + Context Graph Traversal** | **No such dashed box exists.** `Context Graph Traversal` is a single orange-highlighted node in layer 3; the five governance nodes are ungrouped teal cards in layer 4 | **fabricated** |
| 8 | **"live teardown on May 20" annotation inside the pink box** | **No such text anywhere in the image.** The only text besides node names is the title block, layer labels, the two aphorisms, edge labels, and the footer "SAVE FOR YOUR LEARNING ROADMAP" | **fabricated** |
| 9 | Paste's red-team inference: the pink box reveals a "Context Graph" trend linking governance to learning | The premise is false; `Context Graph Traversal` is highlighted as an advanced node, but there is no box or annotation tying it to governance | **invalid as image evidence** — the *concept* (context-graph retrieval for decision traces) is coherent as the paste's own speculation, but it is not something the image asserts |
| 10 | Title/series metadata | "FIELD GUIDE · VOL. 02" and "THE LEARNING LANDSCAPE" appear in image | **verified** — paste didn't claim these but they're consistent |

## Textual Fidelity (paste's own analysis vs source caption)

The Instagram caption adds only: "Most people are learning Agentic AI in the wrong order… jump straight to multi-agent/self-improving/memory/autonomous workflows/Agentic RAG… then production happens" plus the six production questions (context seen, tool chosen, low-confidence behavior, which memory persists, run reconstruction, retry cost). The paste's engineering specifics — salience filtering, TTL/decay, tenant isolation, hallucination-reinforcement, idempotency keys, human-in-the-loop gates — are **the paste author's analysis**, correctly framed inside the digest as its own breakdown and red-team, not as the image's or caption's claims. No misattribution beyond the two fabricated visual details.

## TeaPrompt Contract Map

| Paste analysis mechanism | Existing surface | Disposition |
| --- | --- | --- |
| Deterministic-pipeline-over-agent (Occam's pruning) | Strictness ladder + minimal-composition rule in reflective-dispatch | Already present |
| End-to-end trace before adding memory/self-improvement | Decision/evidence ledgers + context-handoff | Already present |
| Guardrails for side-effecting tools (allowlists, idempotency, approval) | [Runtime Trust Boundary](../04-agent/runtime-trust-boundary.md) asks who approved the operation and what the receiving system enforces | Written requirements, not evidence that a host enforces them |
| Pseudo-memory warning (a vector database alone does not govern what is stored or retrieved) | [Artifact Promotion](../04-agent/artifact-promotion.md) requires provenance before a memory becomes a project rule | Related guidance; retention, retrieval and tenant isolation belong to the host |
| Pseudo-reflection warning (open-loop self-critique without ground-truth oracle) | Anti-cheating + external-verifier rule in reflective-review | Already present — same claim |
| Evaluate a result before writing it to memory | Artifact Promotion §4 asks what check supports a candidate for promotion | Not a second [VER-DOC2](claude-code-verification-survey-2026-11-20.md#candidate-adoption-ledger) case: the paste does not select a check from a diff or link that choice to a past incident |

## Candidate Adoption Ledger

| ID | Candidate | Decision | Reopen condition |
| --- | --- | --- | --- |
| AKG-DOC1 | This dated record + catalogue navigation | **Adopted — reference documentation only** | A corrected paste or a different graphic with the claimed annotations |
| AKG-SK1 | Skill/prompt-body change from the image or paste analysis | **No change** | A reproduced local gap — none shown; the paste's analysis restates existing contracts |
| AKG-RULE1 | The paste's "compounding vs repeating" aphorism or top-down prohibition as operating rules | **Rejected** | Aphorisms and learning-path advice are not engineering invariants; the image itself frames them as pedagogy, not law |

## Evidence vs Inference

- **Verified (image):** every node name, all five layer labels, both aphorisms, all four edge labels, the orange compounding arrow, the footer call-to-action.
- **Verified (caption):** the learning-order framing and the six production questions.
- **Fabricated (paste):** the pink dashed box and "live teardown on May 20" — counted once each as a single visual hallucination affecting the paste's Section-III inference.
- **Inference (mine):** contract-map dispositions; the "no local gap" verdict; classifying the pink-box claim as fabrication rather than a different-edition variant (the image fetched is the one the Instagram post publishes, and no alternate edition is evidenced).
- **Unknown:** whether Brij Pandey published a different version of the graphic (e.g., a later "VOL." with the box/annotation) that the paste actually saw; the X reshare was inaccessible, so a slightly different image attached there cannot be fully excluded — but the original post's image is the authoritative one and lacks both claimed details.

## Risks, Falsifiability, and Handoff

- If a later edition of the graphic (e.g., VOL. 03 or a live-teardown variant) contains the pink box and annotation, the fabrication verdict for the visual claims should be re-opened; the supplied X link or a LinkedIn mirror could contain it, but automated access to both was blocked/unsuccessful.
- The paste's own engineering analysis (pseudo-memory, pseudo-reflection, deterministic guardrails, Occam) is sound and independently defensible — the record preserves it as analysis, not as image-sourced fact.
- Delivered scope: this record, the external-adoption catalogue, and regenerated `index.json`. No prompt-body, Skill, routing, governance, or runtime changes.
