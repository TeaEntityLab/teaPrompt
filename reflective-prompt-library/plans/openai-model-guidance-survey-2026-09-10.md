# OpenAI Model Guidance Survey — 2026-09-10

> **Status: decided, guarded, and verified.** Five-lens Socratic panel (5/5 delivered) reviewed seven candidates from nine official OpenAI developer guidance pages (GPT-4.1 through GPT-6 Astra, fetched 2026-09-10). Four clean-room sentences adopted by user direction on four skills; one rejected (already implicit); two rejected (style, model-specific). User instruction: "survey these model guidance differences" plus "if worth it then update docs and skills."

## Source

- URL pattern: `https://developers.openai.com/api/docs/guides/latest-model/<model>.md` (accessed 2026-09-10)
- Models surveyed: `gpt-4.1`, `gpt-5`, `gpt-5.1`, `gpt-5.2`, `gpt-5.3-codex`, `gpt-5.4`, `gpt-5.5`, `gpt-5.6`, `gpt-6-astra`
- Fetch method: `curl` to `/tmp/model_<model>.md`; all nine returned 200 with model-specific content
- Date fetched: 2026-09-10
- License: OpenAI developer documentation (public)
- No clone, no execution, no API calls — static Markdown only

## What Was Surveyed

Official OpenAI developer guidance pages for nine model generations, from GPT-4.1 (non-reasoning) through GPT-6 Astra (latest). Each page prescribes prompting practices, migration steps, API parameters, and behavioral notes for its model.

## Cross-Model Themes (Chronological Arc)

### 1. Prompt Simplification Arc

- **GPT-4.1**: prescriptive reminders (persistence, tool-calling, planning) — three system-prompt sentences increased SWE-bench 20%
- **GPT-5**: eagerness calibration via XML-tagged sections; "remove maximize_ prefixes that cause over-tool-use" (Cursor case study)
- **GPT-5.5**: "avoid carrying over every instruction from an older prompt stack; legacy prompts over-specify process, add noise, narrow the search space"
- **GPT-5.6**: "state each instruction once; removing repeated instructions improved evals 10-15% while cutting tokens 41-66%"
- **GPT-6 Astra**: "more sensitive to information in context; strongly recommend auditing skills and AGENTS.md for instructions that could influence behavior"

### 2. Reasoning Effort Default Oscillation

- GPT-5: `medium` default → GPT-5.1–5.4: `none` default → GPT-5.5: `medium` default → GPT-5.6: `medium` default → GPT-6 Astra: `low` recommended, `none` removed
- Lesson: `none` as default caused quality regressions in agentic workflows; 5.5 reversed to `medium`; 6 Astra dropped `none` entirely

### 3. Outcome-First Prompts (GPT-5.5)

- "Describe the expected outcome, success criteria, allowed side effects, evidence rules, and output shape. Avoid step-by-step process guidance unless the exact path matters."
- "Reduce or remove detailed step-by-step process guidance. Let the model choose the path unless the product requires that path."
- "Avoid unnecessary absolute rules. Use ALWAYS/NEVER/must only for true invariants. For judgment calls, prefer decision rules."

### 4. Instruction Sensitivity Increases

- GPT-4.1: "follows instructions more literally than predecessors"
- GPT-5: "contradictory instructions can be more damaging; expends reasoning tokens searching for reconciliation"
- GPT-5.5: "interprets prompts in a literal and thorough manner"
- GPT-6 Astra: "more sensitive to information in context; unclear or conflicting guidance in a skill file may cause the model to pause and block work early"

### 5. Autonomy Calibration

- GPT-4.1: "keep going until resolved"
- GPT-5: "calibrate eagerness; set stop conditions"
- GPT-5.1: "solution persistence; bias for action"
- GPT-5.3-Codex: "autonomous senior engineer; persist for hours"
- GPT-5.5: "outcome-first; let model choose path"
- GPT-5.6: "define autonomy/approval boundaries compactly; safe local actions vs external/destructive"
- GPT-6 Astra: "bias toward action; ask approval only after preparing a concrete, reviewable result; do not introduce unsolicited approval flows"

### 6. Verification Calibration (GPT-6 Astra)

- "Do not write tests for reversible, low-impact changes that mirror the implementation."
- "If you do choose to verify your work with tests, make sure that the tests are meaningful and necessary."
- "Run tests appropriate to the change and complete required checks. Once those pass, broaden or repeat testing only when new changes, failures, or unresolved concerns justify it."

### 7. Stopping Conditions / Retrieval Budgets (GPT-5.5)

- "After each result, ask: 'Can I answer the user's core request now with useful evidence and citations for the factual claims?' If yes, answer."
- "Do not search again to improve phrasing, add examples, cite nonessential details, or support wording that can safely be made more generic."

### 8. Tool Calling Evolution

- 4.1: API `tools` field → 5: custom tools, preambles → 5.1: named apply_patch, plan tool → 5.2: compaction → 5.3-Codex: AGENTS.md, skills, hosted shell → 5.4: tool search, computer use, phase, allowed_tools → 5.5: tool-specific guidance in descriptions → 5.6: programmatic tool calling (JS), multi-agent → 6 Astra: async tool calling, mid-turn steering

### 9. Writing Style (GPT-6 Astra)

- Avoid slop words: "delve," "foster," "leverage," "it's worth noting," "importantly," "Bottom Line:" "In short:", "The simplest mental model is:"
- "State the intended action directly. Avoid adding what you won't do."
- "Avoid contrastive framing such as 'X, not Y' that introduces an unprompted alternative."

## Candidate Adoption Ledger

### OG-1: Prompt-level minimality — "state each instruction once"

- **Source**: GPT-5.6 guidance: "State each instruction once. Removing repeated instructions and examples and simplifying tool descriptions can improve task performance and token efficiency."
- **Gap**: `reflective-minimality` covers code/artifact bloat and governance ceremony. It does not explicitly cover *prompt-text* repetition — the cost of stating the same instruction multiple times in a system prompt or skill file. The Minimality Ladder says "Does this need to exist?" but the specific anti-pattern (repeated instructions add noise and narrow the model's search space) is not named.
- **Destination**: `reflective-minimality` — add a bullet about prompt-text repetition.
- **Existing text check**: Line 83 says "Governance artifacts face the same delete-before-add test: size gate thickness to risk and remove ceremony that defends no named invariant." This covers governance artifacts but not prompt-text repetition.
- **Smaller alternative rejected**: rely on the existing "Does this need to exist?" rung — rejected because it asks about existence, not repetition; a sentence can exist once and still be duplicated elsewhere.
- **Failure defended**: a skill that repeats the same instruction in multiple sections causes the model to over-weight it or waste reasoning tokens reconciling minor wording differences.
- **Size estimate**: ~1 sentence.

### OG-2: Outcome-first prompts — "describe the destination, not every step"

- **Source**: GPT-5.5 guidance: "Reduce or remove detailed step-by-step process guidance. Let the model choose the path unless the product requires that path."
- **Gap**: `reflective-spec-plan` says "Stop at the smallest plan that can be executed and reviewed" and `reflective-brief` says "Minimal Plan: the smallest How that could satisfy the acceptance criteria." Neither says "prefer outcome description over step-by-step process guidance; let the model choose the path." The GPT-5.5 guidance is a paradigm shift: the plan should describe the destination, not the route.
- **Destination**: `reflective-spec-plan` — add a bullet in the Workflow section.
- **Existing text check**: Line 115 says "Stop at the smallest plan that can be executed and reviewed." This covers size but not shape — a small plan can still be over-specified with process steps.
- **Smaller alternative rejected**: rely on "smallest plan" — rejected because "smallest" is about quantity, not about outcome-vs-process shape.
- **Failure defended**: a spec that prescribes every step prevents the model from choosing a more efficient path and adds noise that narrows the search space.
- **Size estimate**: ~1 sentence.

### OG-3: Verification calibration — "calibrate test depth to change risk"

- **Source**: GPT-6 Astra guidance: "Do not write tests for reversible, low-impact changes that mirror the implementation. If you do choose to verify your work with tests, make sure that the tests are meaningful and necessary."
- **Gap**: `reflective-implement` §Verification says "Run the checks that prove the claim" and lists specific checks. The Small-Change Fast Path collapses the report but says "Never collapse verification itself." Line 102 says "narrowest tests that would fail if it changed." But neither says "calibrate how much testing a change requires; avoid tests that mirror the implementation for reversible low-impact changes."
- **Destination**: `reflective-implement` §Verification.
- **Existing text check**: Line 102 says "narrowest tests" and the Fast Path says "Never collapse verification itself." The system prompt says "NEVER write a test so the change 'has tests'." The gap is the explicit calibration sentence.
- **Smaller alternative rejected**: rely on "narrowest tests" — rejected because "narrowest" is about width, not about whether to test at all; a narrow test that mirrors the implementation is still a wasted test.
- **Failure defended**: writing tests that mirror the implementation for a reversible low-impact change wastes tokens and can create false confidence.
- **Risk**: could be misread as "skip verification for small changes," contradicting "Never collapse verification itself." The sentence must preserve the invariant that verification itself is never skipped.
- **Size estimate**: ~1 sentence.

### OG-4: Stopping conditions for search — "do not search again to improve phrasing"

- **Source**: GPT-5.5 guidance: "Do not search again to improve phrasing, add examples, cite nonessential details, or support wording that can safely be made more generic."
- **Gap**: `reflective-research` Sufficiency Gate says "Once it passes, stop — do not pad the answer with more sources." But it doesn't name the specific anti-patterns (searching again for phrasing, examples, nonessential details).
- **Destination**: `reflective-research` Sufficiency Gate.
- **Existing text check**: Line 118 says "Once it passes, stop — do not pad the answer with more sources." This covers the general principle but not the specific anti-patterns.
- **Smaller alternative rejected**: rely on "do not pad" — rejected because "pad" is about adding sources, not about re-searching for phrasing or examples.
- **Failure defended**: re-searching for phrasing or nonessential details wastes tokens and can introduce conflicting evidence that degrades the answer.
- **Size estimate**: ~1 sentence.

### OG-5: Avoid unnecessary absolute rules — "use ALWAYS/NEVER only for true invariants"

- **Source**: GPT-5.5 guidance: "Avoid unnecessary absolute rules. Use ALWAYS/NEVER/must/only for true invariants. For judgment calls, prefer decision rules."
- **Gap**: TeaPrompt skills use "Never" bullets extensively for true invariants (security, data loss, etc.) and conditional language for judgment calls, but this convention is implicit, not stated as a writing principle. A skill author could add a "Never" for a judgment call, over-constraining the model.
- **Destination**: Durable Lesson in `PROJECT_KNOWLEDGE.md` or a writing convention in `AGENTS.md`.
- **Existing text check**: No existing principle states this convention. The GLOSSARY defines terms but not writing conventions for absolute vs conditional language.
- **Smaller alternative rejected**: rely on the existing "Never" bullets as examples — rejected because examples don't state the principle; a new author could add a "Never" for a judgment call.
- **Failure defended**: an absolute rule on a judgment call over-constrains the model, preventing it from adapting to context where the judgment should differ.
- **Size estimate**: ~1 sentence.
- **Note**: This is a meta-principle about skill writing, not a skill change. It belongs in the project-knowledge layer or AGENTS.md, not in a workflow skill.

### OG-6: Slop word avoidance

- **Source**: GPT-6 Astra guidance: avoid "delve," "foster," "leverage," "Bottom Line:" etc.
- **Gap**: No TeaPrompt skill addresses AI-generated slop words.
- **Assessment**: Slop words are a style issue, not a correctness issue. `reflective-review` is about "what would make the artifact fail in real use." Slop words don't make an artifact fail. Not actionable for TeaPrompt's correctness-focused skills.
- **Status**: Rejected — style, not correctness.

### OG-7: "Drop the current date" — model already knows UTC date

- **Source**: GPT-5.5 guidance: "Drop the current date. The model is already aware of the current UTC date."
- **Gap**: Some system prompts inject the current date.
- **Assessment**: This is model-specific guidance. TeaPrompt is model-agnostic. Adding "the model already knows the date" would be wrong for non-OpenAI models or older models. Not actionable.
- **Status**: Rejected — model-specific.

## Panel Verdicts (Five-Lens Socratic Review, 2026-09-10)

| Candidate | Verdict | Rationale |
|---|---|---|
| OG-1 | **Adopted** | "Does this need to exist?" tests existence, not repetition; real gap in `reflective-minimality` |
| OG-2 | **Adopted** | "Smallest plan" is quantity, not shape; real gap in `reflective-spec-plan` |
| OG-3 | **Adopted** | "Narrowest tests" is width, not whether to test; guarded wording preserves "never collapse verification" |
| OG-4 | **Adopted** | "Do not pad" covers output, not re-search for phrasing; real gap in `reflective-research` |
| OG-5 | **Rejected** | Already implicit in skills (Never for invariants, conditional for judgment calls); wrong surface for Durable Lesson (no recurrence evidence) |
| OG-6 | Rejected | Style, not correctness |
| OG-7 | Rejected | Model-specific, TeaPrompt is model-agnostic |

## Adopted Wording

- **OG-1** (`reflective-minimality` Minimality Ladder, after governance-artifacts bullet): "Apply the same test to prompt text: state each instruction once. A rule repeated across sections adds tokens, invites wording drift between copies, and can over-weight the instruction or spend reasoning reconciling near-duplicates."
- **OG-2** (`reflective-spec-plan` Workflow, after step 6): "Describe the intended outcome and acceptance criteria rather than prescribing each step; let the model choose the path unless a specific path is required for the product."
- **OG-3** (`reflective-implement` §Verification, after A-7a sentence): "Calibrate the depth of verification to the risk and reversibility of the change: do not add tests that merely mirror the implementation for reversible, low-impact edits. The proving check is still run and read; choose the narrowest check that would actually fail if the change were wrong, then stop once the claim is proven."
- **OG-4** (`reflective-research` Sufficiency Gate, after stop rule): "Do not search again to improve phrasing, add examples, or cite nonessential details; if wording can safely be made more generic, make it generic instead of re-searching."

## Evidence Separation

- **Observed**: nine official developer guidance pages fetched 2026-09-10 from `developers.openai.com`; all returned 200 with model-specific content; page text read and compared across nine models.
- **Author-claimed**: all quoted guidance text is OpenAI's published recommendation; vendor-reported benchmark numbers (e.g. "20% SWE-bench improvement", "10-15% eval improvement", "41-66% token reduction") are OpenAI's claims, not independently verified here.
- `[INFERENCE]`: that the cross-model themes (prompt simplification arc, reasoning default oscillation, instruction sensitivity increase) describe a coherent vendor-internal trajectory; that the four adopted sentences generalize beyond OpenAI models to model-agnostic skill text.
- **Not done**: no API calls, no model execution, no behavioral testing of adopted sentences.

## Falsifiability

This record is wrong or must be re-litigated if: (1) any of the four adopted sentences is removed from its named skill surface without a documented supersession; (2) vendor model names (GPT, Astra, OpenAI, Codex) appear on any durable skill surface (clean-room violation); (3) OG-5 is re-opened without new recurrence evidence showing a skill author adding a `Never` for a judgment call; (4) a future model guidance page contradicts the adopted sentences and the contradiction is confirmed locally.
