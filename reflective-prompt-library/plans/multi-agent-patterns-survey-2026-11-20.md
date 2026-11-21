# Multi-Agent Design Patterns Survey — Fidelity and Contract Map (2026-11-20)

Language: English

**Status: source-qualified reference record (`MAD-DOC1`); no Skill, prompt-body, operating-rule, or runtime change.** The owner supplied `local://paste-18.md`, which pairs a zh-TW commentary with an unattributed English "MULTI-AGENT DESIGN PATTERNS — A COST-VALUE BREAKDOWN" post. This record checks the taxonomy against established agentic-pattern sources and maps the claims to TeaPrompt contracts. No installs, model calls, Skill changes, commits, or pushes are authorized.

## Research Question

Is the six-pattern breakdown accurate and faithful to the source, and does it contain mechanisms missing from TeaPrompt's contracts?

## Direct Recommendation

**Adopt the record only.** The taxonomy is a conventional, correct restatement of the standard agentic-pattern set — sequential, parallel, hierarchical, generator–critic, human-in-the-loop, composite — matching Google ADK's workflow patterns, the Google Cloud architecture guide, and published multi-agent surveys. The cost-tier labels ($–$$$$) and MCP/A2A separation are the post's own editorial additions, and the paste's zh-TW commentary is faithful to both the original and its own reasoning. The load-bearing advice — "more agents don't automatically mean better results; start simple; add orchestration only when it delivers measurable value" — is already TeaPrompt's minimality-gate and smallest-topology rules. No local gap; no adoption. TeaPrompt supplies the methods and templates methodology-side; the host executes them — this record claims no shipped runtime team.

## Evidence Used

| Source | Class | What it supplies |
| --- | --- | --- |
| `local://paste-18.md` | **Primary** — supplied zh-TW commentary + embedded original post | Verbatim object under review |
| [Google ADK workflow patterns](https://adk.dev/workflows/patterns) | Established taxonomy reference | Confirms the six patterns are canonical, not original |
| [Google Cloud agentic-design-pattern guide](https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system) | Established taxonomy reference | Confirms pattern selection is a documented engineering concern, not a novel insight |
| [Google Developers multi-agent patterns (ADK)](https://developers.googleblog.com/en/developers-guide-to-multi-agent-patterns-in-adk/) | Secondary implementation guide | Confirms Parser/Critic/Dispatcher role decomposition as standard practice |
| [MDPI multi-agent orchestration survey](https://www.mdpi.com/1999-5903/18/6/326) | Secondary survey | Confirms MCP/A2A/ANP protocol-layer separation is a settled distinction |

**Attribution:** the embedded English post carries no author line; the paste's zh-TW commentary is the supplied analysis. The post's style (bold-Unicode headings, $–$$$$ tiers, checklist bullets) is characteristic of LinkedIn/X engineering listicles rather than a formal publication — consistent with the "social-media pattern explainer" class.

## Fidelity and Substance Ledger

| # | Post/paste claim | Check | Verdict |
| --- | --- | --- | --- |
| 1 | Six patterns: Sequential, Parallel, Hierarchical, Generator–Critic, Human-in-the-Loop, Composite | All six are the standard decomposition; matches ADK/Cloud/MDPI sources | **verified** |
| 2 | Cost tiers ($, $$, $$$, $$$$) and "hidden cost" per pattern | Editorial shorthand, not a measured model; directionally correct | **verified as editorial** — ordinal, not cardinal |
| 3 | "Best For" guidance per pattern | Matches ADK/Cloud guidance | **verified** |
| 4 | Hierarchical's management overhead (task understanding, delegation, context passing, result checking adds error surface) | Sound engineering point; consistent with ADK's "supervisor" caveat and multi-agent wiki | **verified** |
| 5 | Generator–Critic's "two agents agreeing doesn't make it right" | The post's own qualification; matches the verification literature | **verified** — same caution as TeaPrompt's oracle-separation |
| 6 | HITL for legal/safety/billing/critical decisions | Standard practice | **verified** |
| 7 | MCP = tool connectivity layer; A2A = agent coordination layer; "protocols solve interaction standards, business reliability still needs the system itself" | Accurate distinction; matches MCP/A2A documentation and MDPI survey | **verified** |
| 8 | Key lesson: start simple, add agents only for measurable value | Matches TeaPrompt's minimal-composition and blast-radius rules | **verified** |
| 9 | Paste's own additions: hiring-agent worked example, token/latency/debuggability failure modes, "complexity is not technical progress" | The paste's commentary, correctly framed as its own analysis | **digest-added analysis** — sound, not misattributed |
| 10 | Cost labels as measured economics | Not measured; no data behind $–$$$$ or hidden-cost figures | **editorial** — do not cite as measurements |

## TeaPrompt Contract Map

| Pattern/post mechanism | Existing surface | Disposition |
| --- | --- | --- |
| Sequential (deterministic dependencies) | Shipped: `flow-control-generator` DAG template (host-executed script generation) + `reflective-dispatch` Strictness Ladder | Method present — default topology the templates emit; the host executes |
| Parallel (independent tasks, merge) | Shipped method: `flow-control-generator` parallel fan-out/fan-in template (host-executed); `task` fan-out and `workpool` are host-runtime concerns — no shipped `workpool` pack | Method present — TeaPrompt emits the merge-gate script; it runs no team |
| Hierarchical (manager delegation, context passing) | Shipped method: `flow-control-generator` orchestrator-worker template + `governed-delivery` supervisor/gate contract (both methodology-side, host-executed); `task`/`agent` invocation is host-runtime | Method present — with explicit authority boundaries the post lacks; TeaPrompt runs no team |
| Generator–Critic | Shipped: `reflective-review` core skill + `01-thinking/socratic-reviewer.md`; a `reviewer` role is host-assigned, not a shipped agent | Method present — TeaPrompt adds oracle-separation the post only gestures at |
| Human-in-the-Loop | Written requirement: Human Review gate ([04-agent/runtime-trust-boundary.md](../04-agent/runtime-trust-boundary.md):111) + skill `human_review_required` metadata; the `ask` channel is host-provided | Written-rule present — enforcement is host-owned, not demonstrated here |
| Composite | Composable prompt/workflow library | Already present — composition is the library's own design |
| MCP vs A2A protocol distinction | Host-only — no shipped `agents-sdk` or `durable-objects` packs; MCP bindings are host-runtime | Reference — host-runtime concern, not a prompt contract |
| "More agents ≠ better; add for measurable value" | `reflective-minimality` gate + smallest-topology rule (`flow-control-generator`) + blast-radius gating (`reflective-risk`) | Method present — same claim |

## Candidate Adoption Ledger

| ID | Candidate | Decision | Reopen condition |
| --- | --- | --- | --- |
| MAD-DOC1 | This dated record + catalogue navigation | **Adopted — reference documentation only** | A corrected post, an attributable author, or a local consumer failure |
| MAD-SK1 | Skill/prompt-body change from the pattern taxonomy | **No change** | A demonstrated gap in an existing surface; the taxonomy is canonical and already instantiated |
| MAD-RULE1 | Cost-tier labels, "more agents ≠ better", MCP/A2A layer split as operating rules | **Rejected** | Editorial shorthand and protocol trivia are not invariants |

## Evidence vs Inference

- **Verified:** the six patterns, their `best-for`/`hidden-cost` descriptions, the MCP/A2A distinction, and the "start simple" lesson all match established published references; the paste's commentary is faithful.
- **Verified as editorial:** cost tiers, "hidden cost" figures, and the $–$$$$ scale — ordinal, not measured.
- **Inference (mine):** contract-map dispositions; the "no gap" call; classifying the post as a listicle rather than a primary research source.
- **Unknown:** the post's original author/platform (not signed); whether the paste author is the same person as the original poster.

## Risks, Falsifiability, and Handoff

- The post is a listicle, not a measured study; the cost tiers should never be cited as economics. If the owner wants cost evidence, the source-of-record is a benchmark, not this post.
- The zh-TW commentary's worked hiring-agent example is a useful concrete instantiation; it is the paste's own analysis and is recorded as such.
- Delivered scope: this record, the external-adoption catalogue, and regenerated `index.json`. No prompt-body, Skill, routing, governance, or runtime changes.
