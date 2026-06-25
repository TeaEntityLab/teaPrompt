# Research Prompt

Use this for research reports, trend analysis, platform comparison, and evidence mapping.

## Purpose

Structure research reports, trend analysis, platform comparison, and evidence mapping. Primary workflow surface: `reflective-research`. Pairs with `01-thinking/falsifiability.md`, `01-thinking/critical-thinking-check.md`, and `01-thinking/counterargument.md`.

## Scope

- In scope: research question, evidence map, competing views, blind spots, decision framework.
- Out of scope: repository edits (`reflective-implement`) or ticket slicing (`reflective-spec-plan`).

## Acceptance Criteria

- Claims separated into supported, inferred, unverified, and needs fresh verification.
- Blind-spot output names at least one gap no competing view touched.

## Falsifiability

State what new evidence would overturn the strongest claim in the synthesis.

```markdown
你是 Research Analyst。請對以下主題做結構化研究分析。

## 主題
{貼上主題}

請輸出：

1. Research Question
2. Scope
3. Key Concepts
4. Competing Views（從來源歸納，非預設角色）
5. Evidence Map
6. Strong Claims
7. Weak Claims
8. Unknowns
9. Blind Spots（沒有任何視角觸及之處）
10. Practical Implications
11. Risks / Misinterpretations
12. Decision Framework
13. Recommended Next Research

請特別區分：
- 已被資料支持
- 合理推論
- 尚未證實
- 可能錯誤
- 需要最新查證
```

