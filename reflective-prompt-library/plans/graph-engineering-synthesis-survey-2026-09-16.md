# "Graph Engineering" Vendor-Consensus Synthesis — Survey Record (2026-09-16)

> **Status: decided — one sentence (GE-1) adopted in a 2026-09-19 follow-up under user direction; otherwise record-only. GE-1 was drafted at a fired Durable-Lesson consideration gate, held pending user direction, and landed on `reflective-research` three days later (Landing Addendum below); every other surveyed concept already covered or a decided non-goal.** The object is a pasted zh-TW synthesis claiming that Anthropic, Microsoft, LangChain, and OpenAI converged in 2026 H2 on "Graph Engineering" and "Agentic RAG" as the standard paradigm, with thirteen citations. Each vendor-attributed claim was read against its cited page: one attribution is not substantiated by any inspected official source, one real page is cited for content it does not contain, one real post's thesis is inverted, one 2025 article is presented as new and its "envisioned" interface as built, and two different graphs (control-flow, knowledge) are merged into one wave. The concepts themselves (G1–G8) map onto installed TeaPrompt surfaces or Standing Non-Goals with no gap. The artifact is the third synthesis-genre occurrence the 2026-09-05 Durable Lesson set as its consideration trigger; the consideration was made, the sentence drafted and measured against the bar, and held — project judgement cannot authorize an installed change, and a first landing that treated the trigger as direction was reverted the same day. Verification state lives in the Completion Ledger.

## Research Question

User instruction: "Survey these concepts", followed by a pasted synthesis (Traditional Chinese, thirteen numbered links, a closing offer to "拆解其核心程式碼邏輯"). Two questions: (1) does the synthesis describe its sources; (2) does any concept expose a gap on an installed TeaPrompt surface. A bare "survey" carries no adoption direction. A named gate in `PROJECT_KNOWLEDGE.md` (Lesson: a pasted synthesis is a claim about its source) set a third genre occurrence as the point to *consider* a `reflective-research` sentence; that consideration is GE-1 below. Considering is the gate's whole authority: `PROJECT_KNOWLEDGE.md` is non-authoritative by its own header and `06-repo/AGENTS.md` §PROJECT_KNOWLEDGE states it never grants agent authority, so the drafted sentence lands only on user direction.

## Direct Recommendation (as of 2026-09-16)

- **Study: the sources, not the synthesis.** Three of the four vendor pages are worth reading for what they say: LangChain's post is a measured "graph engineering is the latest name for a three-year-old approach, and here is when not to use graphs"; Anthropic's guidance is the December 2024 "simplest solution possible" piece with five workflow patterns; the LangGraph tutorial is a clean grade-and-rewrite loop. None says what the synthesis says they say.
- **Adopt: GE-1, on direction (landed 2026-09-19; addendum below).** GE-1, an intake sentence for `reflective-research`, was drafted and held here, then installed under user direction; the eight concepts need no sentence. G1–G8 are covered (topology selection, orchestrator-workers template, sufficiency gate with the OG-4 bound, formalization L0–L4 contracts, handoff-as-routing) or decided non-goals (owned runtime, swarm, retriever or vector store — knowledge-graph retrieval included, MCP runtime).
- **Reject the synthesis's headline.** "業界共識" is not supported: one vendor calls the term a buzzword, one wrote nothing about graphs, one's inspected material is 2024–2025 and framework-sceptical, one's is a retrieval technique from 2024 with no 2026 post.
- **Deploy: not applicable.** No artifact to run.

## Method

Coordinator fetched every vendor page the synthesis cites and the three primary pages the third-party citations rest on (Anthropic "Building effective agents", the Claude Code announcement, the OpenAI Agents SDK handoffs page), plus the LangGraph Graph API section on recursion limits and the anthropic.com engineering index; two third-party pages were unreachable or not fetched (see Evidence Actually Checked). One read-only scout mapped G1–G8 against every installed skill, the `04-agent` lenses, `PROJECT_KNOWLEDGE.md`, `GLOSSARY.md`, and nine prior records; three of its citations were re-read by the coordinator and held. No panel: no surveyed wording was proposed for adoption. The landing was reviewed as landed bytes by an independent pass before commit (packet contract, 2026-09-15); two same-day advisories then corrected it — see Post-Landing Corrections.

**Scope / acceptance:** verify each of the four vendor attributions against the cited page; map eight concepts with coverage and prior decision; make the consideration the fired trigger asks for, against the standard bar (verified gap on an installed surface, named failure, smaller alternative rejected, deterministic guard), and hold the result for direction; keep survey vocabulary and the reserved wording out of installed surfaces; run `make all`.

## What the Artifact Is

A generated synthesis in the genre the 2026-09-05 lesson describes: instruction-shaped, citation-dense, ending in an offer to go deeper. Its vendor attributions, read against the cited pages on 2026-09-16:

| Synthesis claim | Cited | What the page is | Finding |
| --- | --- | --- | --- |
| Anthropic "officially released" a *Graph Engineering Methodologies* article in July 2026 "with the launch of Claude Code"; context windows do not remove the need for graphs; orchestrator + worker agents; chaining is a linear graph, routing is conditional edges | [1] aibuilderclub.com (course blog, 2026-07-24); [2] blog.csdn.net (2026-07-28) | [1] is a third-party course-marketing post that itself says Anthropic "already shipped the pattern under a plainer name", citing Anthropic's *Building effective agents* (2024-12-19). [2] relays two X posts (unreachable) about an "Anthropic two-hour workshop" and a "12-page PDF" on *knowledge-graph* engineering; nothing with that title appears on the anthropic.com engineering index (checked 2026-09-16; the multi-agent post there is 2025-06-13). Claude Code launched 2025-02-24. | **Not substantiated by the inspected sources.** The five patterns are Anthropic's 2024 text, which recommends "the simplest solution possible" and warns that frameworks "make it tempting to add complexity"; the "graph" framing is [1]'s. Only the engineering index was searched, so a July 2026 Anthropic publication elsewhere is `unknown`, as are the workshop and PDF [2] relays (X posts not read). Separately and independently verified: Claude Code launched 2025-02-24, so the "with the launch of Claude Code" dating is wrong whatever the publication's status. |
| Microsoft Research's GraphRAG page "long updated"; the "latest" Data Science at Microsoft article details how GraphRAG + MCP builds an agentic root-cause interface | [3] microsoft.com project page; [4] GraphRAG blog index; [6] medium.com Data Science at Microsoft | [3] lists posts through 2025-08-05 (page modified 2026-07-31; no 2026 post); [4] lists posts through 2024-12-16. [6] is dated **2025-07-10**; its agentic interface is "envisioned to be powered by an MCP server", the prototype "exposed the graph-powered retrieval via a lightweight REST API … rather than building a full agentic interface", results are three qualitative cases, "still actively in the advance research stages". | **Real sources, overclaimed.** A 2025 article is presented as new; an envisioned interface as built; a research prototype as a detailed method. |
| LangChain's July 2026 milestone post "defined true graph engineering": 2023 nodes were code or single calls, 2026 nodes are full autonomous agents; agentic RAG loops back when retrieval is insufficient | [7] langchain.com blog (2026-07-22, Runkle & Chase); [8] docs.langchain.com agentic-rag | [7] opens with the term surfacing "this weekend" from a tweet, "the latest term to come out of X's AI content factory", states "Graph engineering isn't a new idea", has a section "When not to use graphs" (their own deep research moved from a predefined graph to an agent harness), and offers the agent-in-a-node point as "a generous interpretation". [8] is a tutorial: grade retrieved documents, rewrite the question, loop back; the loop has no cap in the tutorial and is bounded only by the runtime's default recursion limit (1000 super-steps since 1.0.6). | **Thesis inverted.** The post argues the opposite of "確立為標準範式". The loop-back description is accurate. |
| OpenAI's September 2026 *Research Acceleration* post reveals internal graph agents; OpenAI's agent guide frames handoffs as edges of an implicit workflow graph | [11] openai.com (2026-09-06); [10] ai.plainenglish.io | [11] is about coding-agent usage metrics inside the research organisation and RSI pacing; the words handoff, node, edge, orchestrator do not occur, and "graph" occurs once as a plot caption ("Graph excludes classifications where the outcome was uncertain") — the landing review caught the coordinator's case-sensitive grep claiming zero. Its one matching fragment — agents "excel at troubleshooting internal research infrastructure" — is real. [10] returned HTTP 403. The OpenAI Agents SDK handoffs page says handoffs "are represented as tools to the LLM"; no graph framing. | **Real page, claim absent.** The graph/handoff framing is [10]'s or the synthesizer's. |
| "業界共識": all vendor articles "without exception" convey one message | [10], [12], [13] medium/plainenglish | Third-party essays; [10] unreachable, [12]/[13] not fetched. | **Unsupported by the vendor pages** it names. |

Two graphs are merged: a control-flow graph (LangGraph nodes/edges, orchestrator-workers) and a knowledge graph for retrieval (GraphRAG, the [2] pipeline). They solve different problems and TeaPrompt decided them separately (flow packs; retriever non-goal).

## Concept Map

Coverage names the installed sentence; decision names the record that settled it.

| ID | Concept (clean-room) | Installed coverage | Prior decision | Disposition |
| --- | --- | --- | --- | --- |
| G1 | Graph as the design unit: nodes are agents, calls, or code; edges are control flow; chaining is a line, routing a conditional edge | `flow-control-generator` Topology Selection (pick the smallest topology; "if no row fits, the task is probably a single agent call"), Never "choose topology from platform prestige"; `reflective-spec-plan` "Do not start by drawing a graph. First choose the lowest formalization level" | 2026-07-11 flow research P12 (DAG template, user-directed); flow-coverage panel §Rejected | No change (GE-2) |
| G2 | Orchestrator + bounded workers + synthesis | `flow-control-generator` Orchestrator-Workers template (task is data, not authority; merged-result gate) | 2026-07-11 P8; PAN-CHG-02 kept the name | No change (GE-3) |
| G3 | A node that is a full agent versus a single call or code | generator `run_agent` abstraction; `reflective-spec-plan` transition ownership (code, rule, model, human); scaffold "subagent report is untrusted" | 2026-06-25 panel: swarm runtime rejected (row AY); Standing Non-Goal | No change (GE-3) |
| G4 | Grade retrieved context; loop back to re-query when insufficient | `reflective-research` Sufficiency Gate ("if the gate fails, name the missing evidence and keep searching") bounded by OG-4 ("a passed gate is not reopened for polish") | 2026-09-10 OG-4; retriever non-goal (case-studies procedure step 6) | No change (GE-4) |
| G5 | Persistent graph state and checkpoints as the loop substrate | loop pack Anatomy #3 ledger and `RESUMED`, Never "claim crash-safety"; `reflective-spec-plan` L4 control-state / effect / ownership contracts; `04-agent/workflow-engine.md` state model | 2026-07-11 §Rejected memory backends; 2026-08-25 AH-10/13 runtime engine rejected | No change (GE-6) |
| G6 | Knowledge graph + community summaries for global and multi-hop questions; MCP server for agent-driven root cause | `reflective-research` Source Priority and DeepWiki-as-map; `reflective-implement` root cause before edits | Retriever / vector-store non-goal covers knowledge-graph retrieval (procedure step 2 "reject … retrievers"; CR-3); MCP runtime CR-5, AH-15 | No change (GE-7) |
| G7 | Handoffs as implicit edges | generator Conditional Router; `reflective-handoff-retro` continuation packet | 2026-07-11 research: "handoff … is OpenAI/Microsoft vocabulary … The skills treat handoff as a routing variant" | No change (GE-8) |
| G8 | Build multi-agent systems with distributed-systems / state-machine rigor | `reflective-spec-plan` four contracts; `reflective-risk` `OUTCOME_UNKNOWN`, fencing; generator Never crash-safety claims | 2026-08-25 AH-18/19 adopted the contracts, AH-10 rejected the engine | No change (GE-9) |

## Candidate Adoption Ledger

| ID | Candidate | Status | Evidence | Next action / trigger |
| --- | --- | --- | --- | --- |
| GE-1 | `reflective-research` State Ledger rule: a summary's citation is the summary's claim; a claim that arrived through a summary keeps the summary as its Source until the cited page is read; then record page beside summary | Adopted 2026-09-19 (user direction; installed once on `reflective-research` §State Ledger) | Gap: the installed skill governed only the `verified` mark ("not a summary of one") and ranked summaries as supplemental context; no sentence said what Source an unverified summary claim carries at intake. The tier rule lived only in `PROJECT_KNOWLEDGE.md`, which an installed agent does not read. Failure defended: today's artifact — four real-looking citations whose pages say other things; an agent copying "Anthropic says …" into its Source column would carry a fabricated consensus forward. Smaller alternatives rejected: leave it in the Lesson (not on the acting surface, the same reason the Lesson set this trigger); rely on line 104 (fires at `verified`, after the damage); seat it in `reflective-review`'s four dimensions (review runs after the evidence set exists) | Lands on user direction, once, with the State Ledger rules after "not a summary of one"; reserved wording: "A summary's citation is the summary's claim about a source, not the source's evidence: a claim that arrived through a summary keeps the summary in its Source column until the cited page is read, however real the link; then record what the page says beside what the summary said it says." Guard keeps the wording out of every installed surface until then and pins the deferred status → Landed 2026-09-19: Landing Addendum below; the guard now pins the sentence once on the skill. |
| GE-2 | Graph-first design vocabulary / topology table entry | No change 2026-09-16 | G1 row | — |
| GE-3 | Orchestrator-workers, agent-in-a-node | No change 2026-09-16 | G2, G3 rows | — |
| GE-4 | Retrieval grade-and-loop-back as a research rule | No change 2026-09-16 | G4 row; the loop already exists as the Sufficiency Gate with OG-4 as its bound | — |
| GE-5 | LangGraph's documented "graceful degradation" pattern (a fallback node returns a "best effort answer" when the step budget nears its limit) as a second negative example beside the loop pack's cap rule | Rejected 2026-09-16 | The pack already forbids returning the last unverified output on cap exhaustion and names one negative example; a second citation adds no rule and the packs sit at 19,984 / 19,979 of 20,000 characters | Reopen if a TeaPrompt-generated loop is observed doing this |
| GE-6 | Persistent graph state / checkpoint substrate | No change 2026-09-16 | G5 row | — |
| GE-7 | Knowledge-graph retrieval, community summaries, MCP-served root-cause exploration | No change 2026-09-16 | G6 row; a knowledge graph is a retriever and the non-goal names retrievers, not embeddings | Reopen only if the retriever non-goal is re-litigated |
| GE-8 | Handoffs as edges | No change 2026-09-16 | G7 row | — |
| GE-9 | Distributed-systems rigor as meta-principle | No change 2026-09-16 | G8 row | — |
| GE-10 | "Industry consensus on graph engineering" as a recordable fact | Refuted 2026-09-16 (record-only) | What the Artifact Is: one vendor calls it a buzzword, one wrote nothing about it, one's material is 2024, one's is a retrieval technique; the 2026-08-25 finding recurs — family resemblance is not consensus | — |

Deterministic guard: `plans/tests/test_graph_engineering_synthesis_survey_record.py` (reserved wording absent from installed surfaces; statuses; fired-but-held trigger; index links).

## Shared Findings

1. **Real links are the new laundering channel.** Every vendor citation resolved to a live page; three of the four pages do not say what they were cited for. Existence checks pass; attribution fails. This is the split `reflective-review`'s four dimensions already make; GE-1 would apply it at research intake.
2. **The deflationary source became the hype.** LangChain's post exists to say the term is old and to list when *not* to use graphs; the synthesis quotes its "what's new" paragraph and drops its frame. A summary's selection is a claim about the source too.
3. **Two graphs, one word.** Control-flow graphs and knowledge graphs were decided on different days for different reasons (flow packs; retriever non-goal). Merging them under one "wave" is how a settled non-goal gets re-litigated as a new paradigm.
4. **The one accurate vendor fragment** — OpenAI's researchers using coding agents to troubleshoot research infrastructure — is what remains once the graph framing is removed, and it matches nothing the synthesis concludes.
5. **Third occurrence, gate fired, candidate held.** The 2026-09-05 lesson was adopted on a second occurrence with an explicit third-occurrence trigger; today's artifact is the third. The trigger's verb is *consider*: the sentence it anticipated was drafted and measured, and it waits for direction. A first landing installed it on the strength of the trigger and was reverted the same day — project judgement records why the project believes something; it does not authorize an agent to change an installed surface.
6. **A verdict is bounded by the check that produced it.** "Attribution refuted" was written after searching one index; the honest status is "not substantiated by the inspected sources", with the independently verified date error kept separate. The same over-reach the synthesis committed, one level down.

## Evidence vs Inference

| Claim | Status | Basis |
| --- | --- | --- |
| LangChain post identity, date, authors, thesis, "When not to use graphs" section | Observed | Page fetched 2026-09-16 |
| OpenAI post identity, date, subject; no occurrence of handoff / node / edge / orchestrator; "graph" once, in a plot caption | Observed | Page fetched and grepped 2026-09-16; corrected by the landing review (case-insensitive re-grep) |
| Anthropic engineering index carries no graph-engineering post; multi-agent post 2025-06-13; Managed Agents 2026-04-08 | Observed | Index grepped 2026-09-16 |
| Anthropic *Building effective agents* content and date | Observed | Page fetched 2026-09-16 (page carries a note that tooling has changed since; not relied on) |
| Claude Code announced 2025-02-24 | Observed | Announcement page fetched 2026-09-16 |
| Microsoft project page last post 2025-08-05, modified 2026-07-31; blog index last post 2024-12-16 | Observed | Pages fetched 2026-09-16 |
| Medium article date 2025-07-10; MCP "envisioned"; REST prototype; qualitative results | Observed | Page fetched 2026-09-16 |
| LangGraph tutorial loop shape; default recursion limit 1000 since 1.0.6 | Observed | Tutorial and Graph API pages fetched 2026-09-16 |
| OpenAI Agents SDK handoffs "represented as tools"; no graph framing on that page | Observed | Page fetched 2026-09-16 |
| [1] is a course blog attributing the pattern to Anthropic's 2024 post | Observed | Page fetched 2026-09-16 |
| A July 2026 Anthropic graph-engineering publication exists | `unknown` — not substantiated by the inspected sources | Only the anthropic.com engineering index was searched; [2]'s "two-hour workshop" and "12-page PDF" X posts not fetched |
| [10], [12], [13] content | `unknown` | 403 / not fetched; third-party |
| G1–G8 coverage and prior decisions | Scout-read; three coordinator spot-checks held (`agent-flow-control-research-2026-07-11.md:50`, `reflective-spec-plan/SKILL.md:155`, `flow-loop-harness/SKILL.md:50`) | Local grep; local line numbers are exact |
| GE-1's gap on the installed skill | Observed | `reflective-research/SKILL.md` grepped for summary / provenance / attribution rules; lines 43, 62, 104 read |
| GE-1's authorization | Corrected | The fired trigger authorizes consideration only (`PROJECT_KNOWLEDGE.md` header; `06-repo/AGENTS.md` §PROJECT_KNOWLEDGE); a survey instruction supplied no adoption direction |
| An agent would have recorded the synthesis's attributions as author-claimed | `[INFERENCE]` | The failure is drawn from the artifact's shape and the 09-05 occurrences, not from a fixture run |

## Evidence Actually Checked

All fetched 2026-09-16 with the `read` tool; no clone, nothing executed.

- https://www.langchain.com/blog/3-years-of-graph-engineering-with-langgraph (accessed 2026-09-16)
- https://docs.langchain.com/oss/python/langgraph/agentic-rag and the Graph API page's recursion-limit section (accessed 2026-09-16)
- https://openai.com/index/research-acceleration-view-inside-openai/ (accessed 2026-09-16; full text read and grepped)
- https://openai.github.io/openai-agents-python/handoffs/ (accessed 2026-09-16)
- https://www.microsoft.com/en-us/research/project/graphrag/ and https://microsoft.github.io/graphrag/blog_posts/ (accessed 2026-09-16)
- https://medium.com/data-science-at-microsoft/graphrag-powered-ai-agent-interfaces-real-world-applications-in-incident-and-change-management-01f489ccac93 (accessed 2026-09-16; first 241 of 364 lines)
- https://www.aibuilderclub.com/blog/graph-engineering-with-claude-code (accessed 2026-09-16)
- https://blog.csdn.net/weixin_58753619/article/details/163281948 (accessed 2026-09-16; first 300 of 532 lines)
- https://www.anthropic.com/engineering/building-effective-agents, https://www.anthropic.com/engineering (index), https://www.anthropic.com/news/claude-3-7-sonnet (accessed 2026-09-16)
- Not read: https://ai.plainenglish.io/graph-engineering-the-next-evolution-in-ai-agent-systems-95a04cf6e577 (HTTP 403, 2026-09-16); the three remaining medium.com essays; the two X posts [2] relays.
- Local: scout coverage map over thirteen `SKILL.md`, `04-agent/`, `PROJECT_KNOWLEDGE.md`, `GLOSSARY.md`, nine prior records; coordinator greps of `reflective-research/SKILL.md`, `flow-loop-harness/SKILL.md`, `reflective-spec-plan/SKILL.md`, `agent-flow-control-research-2026-07-11.md`, the Durable Lesson and its guard (`test_agentflow_survey_record.py:489-492`).

## Falsifiability

- The Anthropic finding moves from "not substantiated" to "substantiated" if an Anthropic-authored graph-engineering publication dated July 2026 is found off the engineering index; the Claude Code date correction is independent of that search, and GE-1's case would still stand on the OpenAI and LangChain rows.
- The OpenAI finding is wrong if the page's rendered text differs from the fetched text (the fetch returned the full article and its appendix), or if a reader counts the plot caption's "Graph" as graph-engineering content.
- GE-1's draft is wrong if it would produce ledgers that never resolve — a summary claim that stays attributed to the summary after the page was read. The wording requires the page to be read and recorded beside the summary; a ledger that stops at "pasted summary" is a failure of the workflow, not of the rule.
- GE-1's deferral is wrong if user direction lands it and the guard still forbids the wording on `reflective-research`; the guard must then flip from reserved-absent to pinned-once.
- The concept map is wrong if an installed skill lacks a rule a row credits to it; every row cites the sentence, re-grep it.
- This record is wrong if a fourth synthesis-genre survey records a summary's attribution as the cited source's before reading the page; that is the Lesson's rewritten trigger.

## Post-Landing Corrections (same day)

Two advisories on the first landing (`69fbd81`), both accepted:

1. **Authorization.** The first landing installed GE-1 on `reflective-research` and presented the fired Lesson trigger as its authorization. `PROJECT_KNOWLEDGE.md` is non-authoritative by its own header and `06-repo/AGENTS.md` §PROJECT_KNOWLEDGE says project judgement never grants agent authority; the trigger's verb is *consider*, and the survey instruction carried no adoption direction. The bullet was removed (the skill is byte-identical to its pre-landing state), GE-1 became a deferred candidate with reserved wording, the Lesson's trigger line was rewritten to say what happened, and the guard flipped from pinned-once to reserved-absent.
2. **Verdict scope.** "Attribution refuted" / "no such publication" for the Anthropic row exceeded the check performed (one index searched; two X-post leads unread). The verdict is now "not substantiated by the inspected sources", with the Claude Code date correction — independently verified — kept separate.

## Completion Ledger

| Item | Status | Evidence |
| --- | --- | --- |
| Four vendor attributions read against their cited pages | done | What the Artifact Is |
| Eight concepts mapped with coverage and prior decision | done | Concept Map; three scout citations spot-checked |
| Fired gate considered with the standard bar; candidate drafted and held | done | GE-1 row |
| No installed surface changed; reserved wording absent everywhere but this record; Lesson evidence and trigger rewritten with the agentflow guard's pins intact | done | `test_graph_engineering_synthesis_survey_record.py`; `test_agentflow_survey_record.py`; `git diff 69fbd81^ -- skills/reflective-research/SKILL.md` empty |
| Survey vocabulary absent from installed surfaces | done | `test_survey_vocabulary_stays_out_of_installed_surfaces` |
| Independent landing review before the first commit | done | `AGREE WITH CHANGES` in substance: every attribution, date, local citation, count, test result, and clean-room check reproduced; one literal claim corrected ("zero occurrences of graph" on the OpenAI page — a case-sensitive grep missed a plot caption) |
| Same-day corrections after two advisories (authorization; verdict scope) | done | Post-Landing Corrections; second commit |
| Decision Index, Case Comparison row, State Ledger row, `index.json` | done | `PROJECT_KNOWLEDGE.md`, `external-adoption-case-studies-2026-06-20.md` |
| Full repository gate | done | `make all` from the repository root |
| GE-1 landed under 2026-09-19 user direction; guard flipped reserved-absent → pinned-once; gap re-verified at landing; scoped ledgers re-read unchanged | done | Landing Addendum; `test_ge1_landed_wording_pinned_once`; post-landing `make all` |

## Landing Addendum (2026-09-19, user direction)

GE-1 landed three days after deferral. Direction: "according to recent JEV-like decision and MiniMax Code CLI, rethink about any skills or docs worth updated" — adoption direction naming the survey families whose 2026-09-19 ledgers carried GE-1 as their one live user-direction-gated candidate (`jev-architecture-synthesis-survey-2026-09-19.md` JA-8 and `minimax-code-trace-map-survey-2026-09-19.md` TM-6, each with next action "GE-1 lands per its own gate on user direction"). This is the DR-5 precedent shape — direction naming the carrying family — not the MC-5-addendum shape, where a generic same-day "if worth then update skills" fired no named gates.

- **Gap re-verified at landing.** The skill's State Ledger bullets still governed only the `verified` mark; no sentence assigned what Source an unverified summary-derived claim carries at intake.
- **Landing site.** One bullet on `skills/reflective-research/SKILL.md` §State Ledger, directly after "not a summary of one" — the seat and form the GE-1 row specified — byte-identical to the reserved wording.
- **Guard flip per Falsifiability.** `test_ge1_reserved_wording_stays_out_of_installed_surfaces` became `test_ge1_landed_wording_pinned_once`: the sentence stays in this record's ledger, appears exactly once on the skill, and stays absent from every other durable surface; the status cell, header regex, and the Lesson's trigger line flipped to landed wording.
- **Scope check.** Every other row in the scoped ledgers was re-read under this direction and left unchanged: DM-1..DM-9 (DM-5's reopen names structural scores exposed to a TeaPrompt-run step — host integration, still unfired), JA-1..JA-9, TM-1..TM-6, MV-1..MV-6 (MV-6 defers to DM-5's trigger), and the already-settled MC and DR ledgers.
