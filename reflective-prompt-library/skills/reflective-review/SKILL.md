---
name: reflective-review
description: Use this to review code, diffs, specs, plans, AI outputs, articles, or decisions. It combines critical thinking, counterargument, test integrity, spec traceability, and actionable required fixes.
license: MIT
risk_level: low
human_review_required: false
external_io: false
---

# Reflective Review

**Type:** Prompt-level workflow

## Purpose

Find what would make the artifact fail in real use, then recommend the smallest useful fix.

## Module Contract

Trigger:
- Use to review code, diffs, specs, plans, AI outputs, articles, decisions, or methodology claims.

Methods:
- Requirement traceability
- Assumption audit
- Evidence and test integrity check
- Claims ledger with observable-evidence requirement
- Runtime trust-boundary review
- Prompt/scaffold provenance review
- Steelman counterargument
- Fallacy, overengineering, and reward-hacking scan

Output:
- Output `Findings`, `Traceability`, `Required Fixes`, `Decision`, and `Residual Risks`.

Never:
- Do not bury serious findings behind a summary.
- Do not accept unsupported claims as evidence.
- Do not treat stated reasoning — human or AI — as proof that a check ran; require observable evidence.
- Do not treat missing tests or weak acceptance criteria as style issues.
- Do not rewrite the artifact unless the task asks for edits.

Escalation:
- Mark `Human review required` when safety, privacy, financial, legal, medical, destructive, or irreversible risk is present.
- Route implementation fixes to `reflective-implement` after review.

## Review Flow

1. Identify the original requirement and acceptance criteria.
2. Extract the artifact's major claims or behavior.
3. Check correctness against the requirement.
4. Audit assumptions.
5. Check evidence and test integrity, recording each load-bearing claim in the Claims Ledger.
6. Steelman the strongest counterargument.
7. Scan for overengineering, reward hacking, and missing edge cases.
8. Give a decision.

## Claims Ledger

A reasoning narrative is not evidence that anything was checked. Models (and people) routinely produce step-by-step explanations that do not reflect what actually drove the conclusion, and they omit influences from the final write-up even when aware of them. So review the artifact's claims against observable evidence — test output, diffs, reproduction, measurements — never against how convincing the explanation sounds.

For reviews with more than a few load-bearing claims, keep a ledger and derive `Findings` and `Traceability` from it:

| Claim | Checked How | Status |
|---|---|---|
| what the artifact asserts | the observable evidence examined | `asserted` / `verified` / `refuted` / `unverifiable` |

- `asserted` means only the author's word supports it — treat as unverified, not as low-risk.
- Mark `verified` only after examining the evidence yourself, not after reading a description of it.
- `unverifiable` claims that are load-bearing belong in `Required Fixes` or `Residual Risks`, never silently accepted.

## Review Modes

Choose one mode first, then apply the common review flow:

- `Code Review`: correctness, regressions, tests, security/privacy, maintainability.
- `Plan/Spec Review`: scope clarity, acceptance criteria quality, sequencing, missing gates.
- `Methodology Review`: classification quality, strictness mismatch, framework overreach.
- `AI Output Review`: evidence quality, unsupported claims, hallucination risk, actionability.
- `Runtime Trust Boundary Review`: instruction/data separation, missing-data discipline, tool-result authority, side-effect gates.
- `Scaffold Provenance Review`: official-vs-mirror evidence, surface distinctions, transferability, and no-copy boundaries.

If the artifact spans multiple modes, declare a primary mode and list secondary checks.

## For Code Review

Prioritize findings by severity:

- Critical: security or data-loss risk.
- High: likely bug or acceptance failure.
- Medium: maintainability, edge case, test gap.
- Low: minor clarity or style issue.

Lead with findings. Include file and line references when available.

## Runtime Trust Boundary Checks

- External content is evidence, not an instruction source.
- Missing fields are unknown, not false, safe, or absent.
- Tool results support claims but do not silently expand scope.
- Side-effectful actions have authority, rollback, and Human Review gates when needed.

## Traceability Table

```markdown
| Acceptance Criteria | Artifact Evidence | Test Evidence | Status |
| --- | --- | --- | --- |
```

## Decision

Use one:

- Approve
- Comment
- Request changes
- Reject
- Human review required

## Output Shape

```markdown
## Findings

## Traceability

## Required Fixes

## Decision

## Residual Risks
```

## Prompt Sources

- `01-thinking/critical-thinking-check.md`
- `01-thinking/counterargument.md`
- `02-engineering/code-reviewer.md`
- `04-agent/review-rating-fix.md`
- `04-agent/runtime-trust-boundary.md`
- `04-agent/agent-scaffold-provenance.md`
