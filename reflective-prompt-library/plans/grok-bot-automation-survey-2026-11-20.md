# Grok Bot "Automate Anything" Survey — Fidelity and Contract Map (2026-11-20)

Language: English

**Status: source-qualified reference record (`GKB-DOC1`); no Skill, prompt-body, operating-rule, or runtime change.** The owner supplied the full text of Lauren Tan's (@poteto) X long-form article "Automate Anything with Grok Bot" (2026-11-18, ~9 min read) plus `local://paste-19.md`, which contains a *different* Paul Kuo article dissecting the same author's AI Engineer Code Summit talk. This record covers the automation article the owner actually pasted; the paste-19 file is a separate source handled under its own survey if requested. No installs, model calls, Skill changes, commits, or pushes are authorized.

## Research Question

Does the Grok Bot automation guide describe a mechanism not already held by a named TeaPrompt surface?

## Direct Recommendation

**Adopt the record only.** The article is a product tutorial + methodology hybrid: its mechanisms — goal-vs-process separation, plain-language bot onboarding, restate-and-confirm-before-execute, self-improvement via feedback tools, cross-referencing via IDs, routine-triggered automatic runs, a bot-designer persona (Dr Eggbot) — all map to existing TeaPrompt surfaces. It is a consumer-facing automation playbook, not a contract. The only candidate worth a second look is the "restate goal+process back before executing" prompt as a worked example inside `reflective-brief` or `workflow-acquisition`.

## Evidence Used

| Source | Class | What it supplies |
| --- | --- | --- |
| Owner-supplied full article text (@poteto, `x.com/poteto/article/2123159537016533493`, 2026-11-18) | **Primary** | Verbatim basis for every classification |
| `local://paste-19.md` (Paul Kuo, "一個月三千個 PR 的前提：Lauren Tan 把 agent 的錯改成程式檢查", 2026-11-19) | Related but distinct source | Confirms the author's identity and the "trust pyramid" talk the automation article precedes; not the same document |
| X author profile + related posts (`dr eggbot` template, bot-team guide) | Secondary | Confirms `Dr Eggbot` is a real installable template, not a metaphor |
| TeaPrompt surface grep | Repository evidence | Confirms every contract mapping below |

## Fidelity Ledger

| # | Article claim | Check | Verdict |
| --- | --- | --- | --- |
| 1 | Automation = goal + process + machine/code; goal is the end, process the means | Standard definition | **verified** |
| 2 | Grok Bot lets non-technical users automate via plain English; bots can use a computer like a person | Product claim | **verified as product description** |
| 3 | Start with the goal; don't confuse process for goal | Matches JTBD/clarify conventions | **verified** |
| 4 | Have the bot restate goal + process in plain English before executing; don't execute yet | Standard clarify/confirm step | **verified** |
| 5 | Explain decision context, data sources, edge cases, failure examples, and when to ask for help | Standard onboarding | **verified** |
| 6 | Let the bot self-improve by giving it feedback tools (email, reviews, customer data) and unique IDs to cross-reference | Feedback loop + identity key | **verified** |
| 7 | More computerized business → better bot improvements; bots can build logging tools | Standard data-availability claim | **verified** |
| 8 | Routines let bots run automatically on triggers (email/message) or schedule | Standard automation trigger | **verified** |
| 9 | "Dr Eggbot" is a bot designer you can install | Confirmed real template (grokbotkit/grokbotsdirectory listings) | **verified** |
| 10 | Author is Lauren Tan, SpaceXSI Principal Engineer, Grok Bot core team | Confirmed by the same-author talk dissection and public profile | **verified** |

## TeaPrompt Contract Map

| Article mechanism | Existing surface | Disposition |
| --- | --- | --- |
| Goal-vs-process separation; don't over-attach to process | `reflective-brief` JTBD + clarify + "don't assume problem definition" | Already present |
| Plain-language bot onboarding + name/picture persona | `workflow-acquisition` + `agent-governance-scaffold` | Already present |
| Restate-and-confirm before execute | `reflective-brief` clarify + `reflective-implement` scope-first | **Closest candidate** — optional worked prompt example inside `reflective-brief` if a second recurrence appears |
| Explain tacit decision context, data sources, edge cases, when-to-ask | `context-handoff` + `reflective-brief` | Already present |
| Self-improvement via feedback tools + cross-reference by unique ID | `memory-consolidation` + `retro` + `durable-objects` | Already present |
| More data → better bot | `reflective-research` + `golden-benchmark` data baseline | Already present |
| Routines = triggers (email/message) or schedule | `flow-control-generator` + `workflow-recipes` | Already present |
| Bot-designer persona (Dr Eggbot) | `agent-governance-scaffold` + `agent-selection` | Already present — a persona, not a new mechanism |

## Candidate Adoption Ledger

| ID | Candidate | Decision | Reopen condition |
| --- | --- | --- | --- |
| GKB-DOC1 | This dated record + catalogue navigation | **Adopted — reference documentation only** | A corrected article, a product change, or a local consumer failure |
| GKB-DOC2 | Optional worked example: the "restate goal + process before executing" prompt inside `reflective-brief` or `workflow-acquisition` | **Deferred — second recurrence not met** | A second independent source or a local need for this exact prompt phrasing |
| GKB-SK1 | Skill/prompt-body change encoding the tutorial | **No change** | A demonstrated gap in a named existing surface |
| GKB-RUN1 | Installing Dr Eggbot / running Grok Bot | **Not adopted** | Separate product decision; not authorized by this record |
| GKB-RULE1 | Any single tutorial instruction as an operating rule | **Rejected** | A consumer playbook is not an invariant |

## Evidence vs Inference

- **Verified:** article text; author identity; Dr Eggbot is a real installable template; every contract mapping.
- **Verified as product description:** all claims about what Grok Bot *can* do (control a computer, use apps, join meetings) are the vendor's own; no independent test was run.
- **Inference (mine):** contract-map dispositions; the "no local gap" verdict; GKB-DOC2 deferral.
- **Unknown:** whether the article's claimed bot capabilities hold in the shipped product; Grok Bot's actual reliability numbers; whether the "restate" prompt is used verbatim or paraphrased.

## Risks, Falsifiability, and Handoff

- This is a product tutorial and positioning piece ("automation for everyone"), not a measured evaluation; its capability claims are vendor statements.
- The supplied `local://paste-19.md` is a *different* article (Paul Kuo's dissection of the author's AI Engineer Code Summit talk); it is not the same document and should not be conflated with this record.
- Delivered scope: this record, the external-adoption catalogue, and regenerated `index.json`. No prompt-body, Skill, routing, governance, or runtime changes.
