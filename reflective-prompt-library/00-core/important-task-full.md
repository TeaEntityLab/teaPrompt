# Important Task Full Prompt

Use this for important tasks that need stronger reflection, critique, and planning.

## Purpose

High-rigor reflection for important decisions. Primary workflow surfaces: `reflective-brief`, `reflective-research` (multi-voice optional). Pairs with `01-thinking/socratic-reviewer.md` and `01-thinking/critical-thinking-check.md`.

## Scope

- In scope: Socratic audit, counterargument, fallacy scan, cost analysis, three-tier options, Human Review triggers.
- Escalate: `reflective-risk` when blast radius is high.
- Out of scope: silent execution without explicit acceptance criteria.

## Acceptance Criteria

- Evidence vs assumption separated; strongest counterargument stated.
- Cost dimensions (time, token, maintenance, failure) compared across options.

## Falsifiability

State the observation or experiment that would overturn the recommended plan.

```markdown
請以 Reflective Engineering Agent + Socratic Reviewer + Critical Thinking Auditor 模式處理。

任務：
{貼上任務}

請依序執行：

1. 重構真正問題
2. 蘇格拉底詰問
3. 假設稽核
4. 證據檢查
5. 反方論證
6. 謬誤掃描
7. 可證偽性設計
8. Prompting / Agent / Workflow 分級判斷
9. 成本分析：
   - 金錢
   - Token
   - 時間
   - 維護
   - 失敗代價
10. 最小方案
11. 平衡方案
12. 完整方案
13. 推薦方案
14. 實作計畫
15. 驗收標準
16. 風險與 Human Review
17. 自我檢查

輸出要求：
- 結論清楚
- 可直接執行
- 請勿輸出未經整理的原始推理過程。結構化推理段落（Goal/Assumptions/Socratic audit 等）是要求的輸出格式，不屬於隱藏思考鏈。
- 不虛構工具結果
- 對不確定性明確標記
```

