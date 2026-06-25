# Why / What / How / Done Prompt

Use this as the core gate prompt before committing to a direction.

## Purpose

Gate a task through Why / What / How / Done before choosing strictness or workflow depth. Primary workflow surfaces: `reflective-brief` for pre-commitment gating; `reflective-spec-plan` when framing becomes ticket or spec work.

## Scope

- In scope: pre-commitment checks on goal, scope, method, and completion evidence for a single task or feature.
- Out of scope: post-hoc code review (`reflective-review`), handoff retros (`reflective-handoff-retro`), or detailed test implementation.
- Adjacent: after brief framing, `reflective-dispatch` selects orchestration level before deeper spec or implement work.

## Acceptance Criteria

- Why gate answers cost of doing nothing and doing wrong.
- What gate lists scope in/out, outputs, and acceptance criteria.
- How gate names minimal method, risks, and human review triggers.
- Done gate ties completion to observable evidence.

## Falsifiability

Done gate must name evidence that would prove the task should not proceed or should be rolled back.

## Human Review

Escalate to `reflective-risk` with an explicit Human Review gate when the work implies irreversible or high-blast-radius action.

```markdown
請把任務通過 Why / What / How / Done 四層檢查。

## 任務
{貼上任務}

# 1. Why Gate
請回答：
- 真正目的
- 背景脈絡
- 不做的代價
- 做錯的代價
- 成功後的價值
- 是否值得做

# 2. What Gate
請定義：
- 範圍內
- 範圍外
- 主要使用者
- 輸入
- 輸出
- 約束
- 驗收標準
- 失敗條件

# 3. How Gate
請提出：
- 最小可行方法
- 替代方法
- 工具選擇
- 風險
- 測試策略
- 回復策略
- 人工審查點

# 4. Done Gate
請定義：
- 完成定義
- 證據
- 測試
- review checklist
- residual risks
- 下一步

最後請給：
- 是否應該現在做
- 應該做到哪個層級
- Prompting 即可，還是需要 Agent / Workflow / 程式
```
