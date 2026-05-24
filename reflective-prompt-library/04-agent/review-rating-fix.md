# Review -> Rating -> Fix Prompt

Use this as the small agentflow loop for improving an artifact.

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
```

