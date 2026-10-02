# Research Prompt

Use this for research reports, trend analysis, platform comparison, and evidence mapping.

## Purpose

Structure research reports, trend analysis, platform comparison, and evidence mapping. Primary workflow surface: `reflective-research`. Pairs with `01-thinking/falsifiability.md`, `01-thinking/critical-thinking-check.md`, and `01-thinking/counterargument.md`.

## Scope

- In scope: research question, evidence map, competing views, blind spots, decision framework.
- Out of scope: repository edits (`reflective-implement`) or ticket slicing (`reflective-spec-plan`).

## Acceptance Criteria

- Claims separated into supported, inferred, unverified, and needs fresh verification.
- Blind-spot output names at least one gap no competing view touched, or explicitly states that none was found — never a fabricated gap.

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
9. Blind Spots（沒有任何視角觸及之處；若確實沒有，請明確說明，不可虛構）
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
- 科學或人類行為主張：優先核對原始研究與相關系統性回顧，註明實際讀到的是全文、原始摘要或二手介紹，不能把摘要的介紹寫成已讀摘要；記錄受試群體、測量結果、比較條件與限制。書籍改寫摘要與機制解釋不是介入效果證據，也不能直接推到 AI。
```

