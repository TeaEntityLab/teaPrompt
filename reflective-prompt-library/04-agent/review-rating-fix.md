# Review -> Rating -> Fix Prompt

Use this as the small Review -> Rating -> Fix loop for improving an artifact.

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
若在複審修正，用原本的呼叫方式檢查修正後的版本，並註明實際驗了哪一版；尚未驗證就保留為待驗。若照建議修改反而會破壞需求，說明為何不應改，不要把「審查意見消失」當成修好了。

## Step 6: Gate Decision
- Pass
- Fix required
- Human review required
- Reject

> **Note:** The Gate Decision is an LLM self-assessment and is advisory, not a hard enforcement gate. For production or high-risk artifacts, the Gate should be independently verified by a human or deterministic check.
```

## Optional Worked Reference

In [Anthropic's randomized study of expert judgment](https://www.anthropic.com/research/agents-judgment-calls),
50 professional analysts worked on one task. Across their analytical
decisions, they matched the agent's assigned preference 86% of the time.
The study strengthened those preferences on purpose; 86% is not an error rate.
In [OpenAI's SWE-bench Pro audit](https://openai.com/index/separating-signal-from-noise-coding-evaluations/),
reviewers made an initial judgment from the task, tests, and reference patch
before consulting the agent's findings. The audit did not measure whether
that sequence reduced bias.

**Example:** A reviewer is deciding whether a test is right to require a
particular output order. To provide an independent check, they read the task
and test before seeing the agent's verdict. Their initial note: "Undecided.
I'd call the test too strict if it rejects a different order that satisfies
the stated requirement." After seeing the agent's reasoning, they can revise
their decision and record the evidence that changed it. A matching sign-off
alone does not show that the reviewer reached the decision independently.
