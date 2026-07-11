# Socratic Change Inquiry - 2026-06-11

> **Status: historical record (retired from active guidance, 2026-07-11).** Kept for provenance and as Decision Index / Durable Lesson evidence. Wording may predate the nine-skill surface and current governance; do not cite as current policy — see `PROJECT_KNOWLEDGE.md` Decision Index for live decisions.


## Purpose

Question whether TeaPrompt should change after studying the attached Siri-style agent prompt and Apple-style runtime analysis.

## Intention Differences

| Layer | Intention | Difference That Matters |
| --- | --- | --- |
| User request | Improve TeaPrompt by reflecting on strong external agent patterns. | Wants learning and action, not passive commentary. |
| Siri-style prompt | Specify a device-native assistant with personal data, tools, UI surfaces, citations, and safety rules. | Product/runtime constitution, not a general engineering prompt library. |
| TeaPrompt | Provide composable reflective prompts and workflow skills for engineering work. | Library and workflow substrate, not an OS agent runtime. |
| Proposed adjustment | Add runtime trust-boundary thinking where tools, retrieved data, and side effects enter the workflow. | Adopt governance primitives without importing product identity or UI obligations. |

## Clarify

- Are we trying to make TeaPrompt more like a device assistant, or more capable at reviewing agent runtimes?
- Is the pain point missing prompts, weak routing, weak evaluation, or weak security vocabulary?
- Is "learn from Siri" a request to copy structure, or to extract transferable principles?
- Which current TeaPrompt failures would this change actually prevent?

## Purpose

- Why should TeaPrompt care about entity-first and trust-boundary design?
- Who benefits: prompt authors, coding agents, workflow designers, reviewers, or users installing skills?
- What happens if the project does not add this layer?
- What happens if it over-adds this layer and makes every workflow feel like a security audit?

## Assumptions

- We assume tool-integrated agents will be a normal TeaPrompt use case.
- We assume retrieved files, web pages, attachments, and tool outputs can contain hostile or irrelevant instructions.
- We assume missing data discipline improves correctness in both personal-data and engineering contexts.
- We assume users still value the library's current small-skill architecture.

Most fragile assumption: runtime trust-boundary concerns are common enough to justify a reusable prompt, but not yet common enough to justify a ninth workflow skill.

## Evidence

- Current repo docs already separate prompt source, skills, plans, and quality gates.
- Current risk handling is explicit for high-risk work but less explicit for ordinary tool/result authority boundaries.
- Attachment analysis repeatedly emphasizes Entity-first, Instruction/Data Separation, Missing Means Unknown, Tool Grounding, and Irreversibility Gate.
- Official sources support the same direction: untrusted data by default, least privilege, consent, tool-use evaluation, and feature-specific safety checks.

## Alternatives

1. Do nothing.
   - Rejected because the repo would keep treating runtime trust boundaries as implicit knowledge.
2. Add a ninth core skill.
   - Rejected for now because the current eight-skill system is intentionally compact.
3. Add a large master agent constitution.
   - Rejected because it conflicts with TeaPrompt's compositional architecture.
4. Add a reusable prompt plus plan records.
   - Chosen because it is low-cost, reviewable, and aligned with existing structure.

## Consequences

Best case: TeaPrompt gains a clear bridge between reflective engineering and tool-integrated agent safety.

Worst case: The new prompt becomes unused documentation. This is acceptable because the change is local and reversible.

Most likely case: The prompt becomes a supporting source for future `reflective-risk`, `reflective-review`, and `reflective-spec-plan` improvements.

## Falsifiability

This adjustment is wrong if:

- Future users cannot tell when to use `runtime-trust-boundary.md`.
- It duplicates `reflective-risk` without adding a distinct runtime/data authority lens.
- It causes skill routing confusion.
- It encourages every task to become over-governed.
- It fails prompt-injection and missing-data review scenarios.

## Decision

Make the smallest useful change now: add the prompt source and record the plan. Revisit skill-level promotion only after repeated use cases show that runtime trust-boundary review is a frequent standalone workflow.
