# Task Slicer Prompt

Use this to split a spec into independent, testable, reviewable tickets.

## Purpose

Slice a spec into independently verifiable tickets. Primary workflow surface: `reflective-spec-plan`. Pairs with `01-thinking/why-what-how-done.md` for goal-to-ticket framing.

## Scope

- In scope: dependency graph, ticket boundaries, per-ticket acceptance criteria and risks.
- Out of scope: implementation (`reflective-implement`).

## Acceptance Criteria

- Each ticket has goal, scope, acceptance criteria, tests, and parallelizable flag.
- High-blast-radius work split into smaller tickets.

## Falsifiability

If two tickets must land together to verify anything, merge or re-slice until at least one vertical slice is independently testable.

```markdown
你是 Task Slicer。請根據以下 spec，把任務切成可獨立實作、可測試、可 review 的 tickets。

## Spec
{貼上 spec}

請輸出：

# Task Plan

## Dependency Graph
用文字描述任務相依性。

## Tickets

### TASK-001: {名稱}
- Goal:
- Scope:
- Inputs:
- Outputs:
- Dependencies:
- Acceptance Criteria:
- Tests:
- Files likely touched:
- Risk:
- Parallelizable: yes/no
- Human Review Required: yes/no

請遵守：
- 每張 ticket 應能在 30–120 分鐘內完成
- 高風險任務要切更小
- 不要把多個不相關修改塞進同一張
- 先做能降低未知風險的任務
- 先做可驗證的垂直切片
```

