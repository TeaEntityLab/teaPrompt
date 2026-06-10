# Plan: Code Follow-ups for Prompt Library

## Goal

Identify future work that would require writing code, scripts, tests, or generated artifacts beyond the Markdown library.

## Why Code May Be Needed

The prompt library can be used manually today. Code becomes useful only if the library must be searched, validated, composed, exported, evaluated, or served repeatedly.

## Candidate Code Artifacts

### CODE-001: Prompt Index Generator

- Goal: Generate a machine-readable index of all prompts.
- Inputs: Markdown files under `reflective-prompt-library/`.
- Outputs: `index.json` or `index.yaml`.
- Acceptance:
  - Every prompt file appears in the index.
  - Each entry includes path, title, category, intended use, and tags.
  - The generator fails on missing title or duplicate slug.
- Tests:
  - Empty directory.
  - Duplicate title.
  - Missing heading.
  - Non-prompt Markdown file.

### CODE-002: Prompt Composer ✅

- Goal: Compose core prompt + task prompt + context prompt + validation prompt.
- Inputs: prompt slugs and optional task text.
- Outputs: a composed Markdown prompt.
- Acceptance:
  - Preserves prompt boundaries.
  - Rejects unknown slugs.
  - Supports low-token mode.
  - Does not silently drop required sections.
- Tests:
  - Valid composition.
  - Missing slug.
  - Conflicting context modes.
  - Empty task.

### CODE-003: Prompt Linter

- Goal: Detect weak or risky prompt patterns.
- Checks:
  - Missing acceptance criteria.
  - Missing falsifiability.
  - Missing human review triggers in high-risk prompts.
  - Claims that ask for hidden chain-of-thought.
  - Undefined placeholders.
- Acceptance:
  - Produces actionable diagnostics with file and line.
  - Supports warnings and errors.
  - Exits non-zero on errors.

### CODE-004: Eval Harness ✅

- Goal: Evaluate prompt outputs against rubric-based test cases.
- Inputs:
  - Prompt file.
  - Scenario fixture.
  - Expected rubric.
- Outputs:
  - Score report.
  - Failure analysis.
  - Regression history.
- Acceptance:
  - Detects missing goal, assumptions, scope, acceptance criteria, and validation.
  - Detects overconfident unsupported claims.
  - Keeps hidden eval answers separate from implementation prompts.

### CODE-005: Static Site or Dashboard ✅

- Goal: Browse, search, tag, and compose prompts visually.
- Acceptance:
  - Category navigation.
  - Search by use case.
  - Copyable prompt blocks.
  - Plan/workflow pages visible but separated from prompt files.

### ROUTE-001: Paraphrase Routing Eval

- Goal: Verify routing fairness across equivalent phrasings.
- Inputs:
  - Intent groups and paraphrase sets.
  - Router config and enhancement policies.
- Outputs:
  - Route consistency report.
  - Confidence and fallback report.
  - Silent downgrade detection report.
- Acceptance:
  - Same intent group routes to the same canonical workflow for at least 95% of paraphrases.
  - Equivalent high-rigor requests receive equivalent enhancement options or execution.
  - Low-confidence routes always emit a visible route trace.
- Tests:
  - Native technical phrasing.
  - Non-native and plain phrasing.
  - PM and novice phrasing.
  - Literal translation phrasing.
  - Cost-aware and high-risk edge cases.
- Seed artifacts:
  - `plans/ROUTING_CONTRACT.md`
  - `plans/route-001-paraphrase-eval.yaml`

## Human Review Triggers

- Publishing the prompt library publicly.
- Adding telemetry or analytics.
- Sending prompt contents to third-party services.
- Introducing dependencies or a hosted dashboard.

## Recommended Sequence

1. ✅ Start with Prompt Index Generator.
2. ✅ Add Prompt Linter.
3. ✅ Add Prompt Composer.
4. ✅ Add Eval Harness.
5. ✅ Add Static Site/Dashboard.

## Stop Conditions

- The library is only used occasionally and manual navigation is sufficient.
- The maintenance cost of tooling exceeds the time saved.
- Prompt evaluation cannot be made reliable enough to justify automation.
