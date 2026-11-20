# Personal Prompt Inventory Survey — Contract Map (2026-11-20)

Language: English

**Status: source-qualified reference record (`PMP-DOC1`); no Skill, prompt-body, operating-rule, or runtime change.** The owner supplied `local://paste-18.md`-adjacent material — a two-part personal inventory of prompts the author uses with coding agents: ten zh-TW reasoning prompts plus nine English workflow prompts. This is self-authored practice documentation, not an external publication; it is surveyed for coverage against TeaPrompt's existing surfaces. No installs, model calls, Skill changes, commits, or pushes are authorized.

## Research Question

Do any of the nineteen prompts describe a mechanism or trigger not already held by a named TeaPrompt surface?

## Direct Recommendation

**Adopt the record only.** All nineteen prompts map cleanly to existing surfaces — every reasoning prompt is already a named skill or prompt, and every workflow prompt is already a flow/worktree/acquisition pattern. The list is best read as the author's personal trigger inventory: it confirms coverage, not a gap. Nothing to adopt; a few prompts could optionally become one-line usage examples inside an existing skill's examples file if a second recurrence appears.

## Evidence Used

| Source | Class | What it supplies |
| --- | --- | --- |
| `local://paste-18.md` adjacent owner paste | **Primary** — self-authored prompt inventory | Verbatim basis for every classification |
| TeaPrompt surface grep (`skills/`, `00-core`–`06-repo`) | Repository evidence | Confirms every prompt maps to a named surface |

## Contract Map — Part 1 (zh-TW reasoning prompts)

| # | Prompt (paraphrased) | Existing surface | Disposition |
| --- | --- | --- | --- |
| 1 | "From first principles, find the root cause, fix it" | `02-engineering/task-start.md`, `05-domain/deep-analysis.md`, `01-thinking/why-what-how-done.md` | Already present — root-cause-first is the standard implement entry |
| 2 | "Ask unclear questions, align to my preference, then produce three options" | `reflective-brief` JTBD + clarify + options | Already present |
| 3 | "Don't assume my problem definition is right; separate symptom from cause, means from goal" | `reflective-brief` assumption audit + `01-thinking/socratic-reviewer.md` | Already present |
| 4 | "Trace second- and third-order effects on modules, users, complexity, maintenance" | `05-domain/deep-analysis.md` + `reflective-risk` + `02-engineering/local-feedback.md` | Already present |
| 5 | "Cross-domain analogies to find the best solution" | `05-domain/` pack pattern + `reflective-dispatch` domain routing | Already present |
| 6 | "Assume my preferred plan is wrong; argue the strongest opposing case, look for counterexamples, then re-evaluate" | `01-thinking/counterargument.md`, `socratic-reviewer`, `parallel-lens-review-packet` | Already present |
| 7 | "Audit git history / PRs / architecture evolution; separate intentional design from leftover baggage" | `04-agent/retro.md` + `03-context/context-handoff.md` + doc-drift check (AGS delta) | Already present at record level |
| 8 | "Evaluate cognitive cost for a fresh capable engineer; flag bad naming, over-abstraction, unclear ownership" | `03-context/context-handoff.md` onboarding-cost framing + `reflective-minimality` + `02-engineering/local-feedback.md` | Already present — the "new engineer" frame is a readability proxy, not a new mechanism |
| 9 | "Review last XX days of PRs, find the slowest, check for stalls/optimization" | `04-agent/retro.md` + `route-aware-go-coverage` analysis pattern | Already present at method level |
| 10 | "Postmortem on bugs/rework/rollbacks; find shared root causes; sink into rules/automation/Skill" | `04-agent/retro.md` + `teaprompt-artifact-promotion` + durable-lesson admission | Already present — the prompt is a paraphrase of the retro+promotion pipeline |

## Contract Map — Part 2 (English workflow prompts)

| # | Prompt (paraphrased) | Existing surface | Disposition |
| --- | --- | --- | --- |
| 1 | "Don't implement; analyze files, list changes, ask if unclear" | `reflective-implement` scope-first + clarify-before-edit | Already present |
| 2 | "Implement all steps, worktree, one commit, merge to main & push / create PR" | `04-agent/workflow-recipes.md` worktree pattern + `flow-loop-harness` | Already present — plus our commit/PR rules are stricter |
| 3 | "Save as separate zh markdown with mermaid under ~/Downloads" | Output-format convention + `localization-tw` | Already present |
| 4 | "grill me on X" | `01-thinking/socratic-reviewer.md` + requirements advisor (agentflow `go-hunt` parallel) | Already present |
| 5 | "This codebase is yours — keep building" | `flow-loop-harness` + governed-delivery | Already present — plus our human-ownership rule keeps this scoped |
| 6 | "Implement, test, prove with HTML under ~/Downloads" | `reflective-implement` proof-of-work convention | Already present |
| 7 | "Make a motion-graphics video of the product" | Creative-task recipe (Eian video workflow is the catalogued precedent) | Reference — product content, not a contract |
| 8 | "Review PRs one by one in worktree; check bundle size, edge cases, UI/UX; approve & merge or reject with comment; improve if needed" | `reflective-review` + worktree + reviewer agent | Already present — plus our gate keeps acceptance non-self-authorized |
| 9 | "/goal … don't ask, don't stop until done, use workflow, worktree, commit, create PR" | `04-agent/workflow-acquisition.md` `/goal` + `flow-loop-harness` stop-conditions | Already present |

## Candidate Adoption Ledger

| ID | Candidate | Decision | Reopen condition |
| --- | --- | --- | --- |
| PMP-DOC1 | This dated record + catalogue navigation | **Adopted — reference documentation only** | A corrected inventory, an attributable publication source, or a local consumer failure |
| PMP-DOC2 | Optional one-line usage examples: "grill me", "/goal … don't stop", "prove with HTML" inside an existing skill's examples file | **Deferred — second recurrence not met** | A second independent author or a local need for worked trigger examples; the patterns already exist as mechanics |
| PMP-SK1 | New skill or prompt-body change encoding the inventory | **No change** | A reproduced gap in a named existing surface — every prompt maps to one |
| PMP-RULE1 | Any single prompt as an operating rule | **Rejected** | A personal trigger list is not an invariant |

## Evidence vs Inference

- **Verified:** every prompt string classified; every surface match located by name in the repository.
- **Inference (mine):** the "confirms coverage, no gap" verdict; the PMP-DOC2 deferral; the authorship/personal-inventory classification.
- **Unknown:** whether the author (the owner) intends these as personal triggers or as publishable prompt patterns — the survey records them as supplied, without claiming external provenance.

## Risks, Falsifiability, and Handoff

- If any of these prompts is later published under the owner's name, the record remains valid; only the provenance line changes.
- None of the nineteen prompts is a mechanism TeaPrompt lacks; the inventory is a coverage confirmation, not a gap list.
- Delivered scope: this record, the external-adoption catalogue, and regenerated `index.json`. No prompt-body, Skill, routing, governance, or runtime changes.
