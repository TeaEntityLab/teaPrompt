# Agent Selection Prompt

Use this to decide whether a task should use prompting, artifacts, coding agents, workflow engines, or a full agent system.

## Purpose

Choose the smallest sufficient execution layer for a task. Primary workflow surface: `reflective-dispatch`. Pairs with `01-thinking/socratic-reviewer.md` and `01-thinking/why-what-how-done.md`.

## Scope

- In scope: complexity, tooling, state, risk, cost, and repeatability comparison across layers.
- Out of scope: implementation (`reflective-implement`), formal blast-radius gating (`reflective-risk`).

## Acceptance Criteria

- Each layer (prompt-only, artifact, agentic coding, workflow engine, full agent system) rated with rationale.
- Recommended layer maps to a frozen workflow skill where applicable.
- Failure cost and repeatability inform the recommendation.

## Falsifiability

State what observation would prove the recommended layer is over- or under-powered for the task.

## Human Review

Escalate to `reflective-risk` when the task implies irreversible side effects regardless of selected layer.


```markdown
請判斷以下任務應該用 Prompting、文件 workflow、Agentic Coding、Workflow Engine，還是完整 Agent System。

## 任務
{貼上任務}

請根據以下因素評估：

1. 任務複雜度
2. 是否需要工具
3. 是否需要讀寫檔案
4. 是否需要測試
5. 是否需要多輪執行
6. 是否需要狀態保存
7. 是否需要 resume
8. 是否涉及風險
9. Token 成本
10. 人類時間成本
11. 失敗代價
12. 是否高頻重複

請輸出：

| 層級 | 是否適合 | 理由 |
|---|---|---|

層級：
- Prompt-only
- Prompt + Artifact
- Agentic Coding
- Workflow Engine
- Full Agent System

層級對照（以下是候選搭配，不是固定路由；先依任務選 Strictness 與主要 workflow，以已安裝的 `reflective-dispatch` 契約為準。執行層是 host 能力，路由是 TeaPrompt skill，兩者是不同軸）：
- Prompt-only → `reflective-brief` 或直接回答
- Prompt + Artifact → `reflective-brief` / `reflective-spec-plan`
- Agentic Coding → `reflective-implement` + `reflective-review`
- Workflow Engine → `reflective-spec-plan`（無碼 workflow 規格）；可執行的 engine 由 host 提供，TeaPrompt 不交付 runtime
- Full Agent System → 先由 `reflective-dispatch` 選 Strictness 與路由；實際執行屬 host，須經 host 授權

最後給：
- 建議層級（含對應 skill / gate 與 host 執行歸屬）
- 最小可行做法
- 不應該過度工程的部分

規則：層級標籤不授權副作用——涉及不可逆行動時，一律先走 `reflective-risk` 並取得 Human Review。
```

