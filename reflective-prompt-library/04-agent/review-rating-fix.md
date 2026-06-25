# Review -> Rating -> Fix Prompt

Use this as the small agentflow loop for improving an artifact.

## Purpose

Run a Review → Rating → Fix loop on an artifact. Primary workflow surface: `reflective-review`. Pairs with `01-thinking/critical-thinking-check.md` and `01-thinking/counterargument.md`.

## Scope

- In scope: rubric scoring, required fixes, residual risks, decision (approve / request changes / reject).
- Out of scope: repository implementation (`reflective-implement`).

## Acceptance Criteria

- Each rubric dimension scored with evidence, not vibes.
- Required fixes are concrete and testable.
- Strongest counterargument stated before final decision.

## Falsifiability

Name one rating change that would flip the approve/reject decision.

## Human Review

Escalate to `reflective-risk` when fixes touch trust boundaries, sensitive data, or irreversible operations.


```markdown
請執行 Review → Rating → Fix 建議流程。

## Artifact
{貼上產物}

## Original Requirement
{貼上需求}

## Rubric
請用 1–10 分評估：

1. Correctness
2. Completeness
3. Testability
4. Clarity
5. Risk Handling
6. Maintainability
7. Alignment with Goal

## Step 1: Review
逐項指出問題。

## Step 2: Rating
給出總分與各項分數。

## Step 3: Why not lower?
請回答：為什麼這個分數不應該再低 2 分？

## Step 4: Path to 10
請列出達到 10 分需要修正的具體項目。

## Step 5: Fix Plan
請給出最小修正計畫。

## Step 6: Gate Decision
- Pass
- Fix required
- Human review required
- Reject

> **Note:** The Gate Decision is an LLM self-assessment and is advisory, not a hard enforcement gate. For production or high-risk artifacts, the Gate should be independently verified by a human or deterministic check.
```

