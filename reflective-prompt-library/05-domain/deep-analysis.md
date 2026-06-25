# Claude / ChatGPT Deep Analysis Prompt

Use this for deeper conceptual, architectural, or critical-thinking analysis.

## Purpose

Deep conceptual, architectural, and critical-thinking analysis beyond quick answers. Primary workflow surfaces: `reflective-research` and `reflective-spec-plan`. Pairs with `01-thinking/critical-thinking-check.md`, `01-thinking/counterargument.md`, and `01-thinking/socratic-reviewer.md`.

## Scope

- In scope: problem reframing, assumptions, counterarguments, minimal vs full options.
- Out of scope: unreviewed delivery (`reflective-implement`) on high-blast-radius conclusions.

## Acceptance Criteria

- Counterarguments and weak points surfaced before recommendation.
- Acceptance criteria stated for both minimal and full solution paths.

## Falsifiability

Name one counterargument that would flip the recommended decision.

```markdown
請以架構師 + 批判性思考教練的角度分析以下問題。

## 問題
{貼上問題}

請輸出：

1. 問題重構
2. 核心概念
3. 隱含假設
4. 強論點
5. 弱論點
6. 反方論點
7. 工程實作含義
8. 成本 / 風險
9. 最小可行方案
10. 完整方案
11. 驗收標準
12. 建議決策

請避免：
- 只迎合我的想法
- 堆砌術語
- 沒有可驗收標準
- 沒有反方
- 沒有風險
```

