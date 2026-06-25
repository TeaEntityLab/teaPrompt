# Workflow Engine Planning Prompt

Use this when a task is too stateful or repeatable for prompt-only work and needs an explicit workflow engine.

## Purpose

Design a stateful, resumable workflow specification. Primary workflow surface: `reflective-spec-plan` (Workflow Design mode). Pairs with `01-thinking/falsifiability.md`.

## Scope

- In scope: state model, transitions, checkpoints, recovery, observability events.
- Out of scope: writing orchestration runtime code (`reflective-implement`).

## Acceptance Criteria

- State fields, transition owners, and gate conditions documented.
- Resume, cancel, and failure recovery paths named.
- Persistence/replay guarantees marked unproven until implementation tests exist.

## Falsifiability

Name one failure mode the workflow cannot recover from under the proposed state model.


```markdown
你是 Workflow Engine Architect。請把以下任務轉成可保存狀態、可恢復、可驗證、可審查的 workflow。

## 任務
{貼上任務}

請輸出：

## 1. Workflow Goal
真正要穩定產生的結果是什麼？

## 2. Trigger
這個 workflow 何時啟動？

## 3. Inputs
列出必要輸入、可選輸入、輸入格式與驗證規則。

## 4. State Model
定義：
- state fields
- persisted artifacts
- checkpoint points
- resume behavior
- cancellation behavior

## 5. Steps
用可執行階段描述：
- Step ID
- Owner / Agent
- Inputs
- Action
- Outputs
- Acceptance
- Failure handling

## 6. Agent Roles
列出需要的 agent 或 pass：
- analyst / spec writer
- implementation agent
- reviewer
- test designer
- verifier
- human reviewer

## 7. Tools
需要哪些工具、檔案、指令、API 或測試？

## 8. Verification Gates
每個 gate 要用什麼 evidence 放行？

## 9. Recovery / Rollback
失敗、部分完成、工具中斷、資料損壞時如何恢復？

## 10. Human Review Gates
哪些狀況必須停止等待人工審查？

## 11. Observability
要記錄哪些 logs、metrics、artifacts、decision records？

## 12. Anti Reward-Hacking
如何防止弱化測試、跳過驗收、假通過或把錯誤藏到狀態裡？

## 13. Minimal Implementation Plan
列出最小可行實作，不要過度工程。
```

