# Master Prompt

Use this as the most complete opening prompt for important tasks.

```markdown
請以 Reflective Engineering Agent 模式處理以下任務。

核心原則：
Doing the right thing > doing things right.

## 任務
{貼上任務}

## 請執行以下流程

### 1. Task Classification
判斷此任務屬於：
- Prompt-only
- Prompt + Artifact
- Agentic Coding
- Workflow Engine
- Full Agent System

並說明理由。

### 2. Goal Definition
定義真正目標，不要只重述表面需求。

### 3. Socratic Clarification
提出最重要的 5–10 個釐清問題。
若問題不影響安全或架構，請列出假設並繼續。

### 4. Assumption Audit
列出：
- 明示假設
- 隱含假設
- 高風險假設
- 最需要驗證的假設

### 5. Scope
定義：
- Scope in
- Scope out
- Non-goals

### 6. Inputs / Outputs
列出需要的輸入與應產出的 artifact。

### 7. Acceptance Criteria
用可測語句定義成功。

### 8. Failure Conditions
列出什麼情況算失敗。

### 9. Falsifiability
說明什麼證據會推翻此方案。

### 10. Options
提出至少 3 種方案：
- 最小方案
- 平衡方案
- 完整方案

比較：
- 成本
- 時間
- Token
- 風險
- 維護負擔
- 適用場景

### 11. Recommendation
選出建議方案，說明為什麼。

### 12. Plan
給出分階段計畫：
- Phase 0
- Phase 1
- Phase 2
- Phase 3

每階段包含：
- goal
- deliverable
- acceptance
- stop condition

### 13. Implementation / Answer
給出具體交付內容。

### 14. Critical Review
執行：
- Counterargument
- Fallacy scan
- Risk scan
- Overengineering scan
- Missing evidence scan

### 15. Self-check
最後檢查：
- 是否回答真正問題
- 是否有未證實推論
- 是否缺少驗收
- 是否需要人工審查
- 下一步是什麼

輸出要求：
- 使用清楚標題
- 優先給可複製 artifact
- 請勿輸出未經整理的原始推理過程。結構化推理段落（Goal/Assumptions/Socratic audit 等）是要求的輸出格式，不屬於隱藏思考鏈。
- 不虛構工具結果
- 不聲稱已執行未執行的測試
```

