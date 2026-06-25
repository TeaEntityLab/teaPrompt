# Medium Context Window Prompt

Use this for 32K-128K context windows and ordinary ChatGPT / Claude / Codex tasks.

## Purpose

Balance completeness and context cost for 32K–128K windows. Primary workflow surfaces: `reflective-spec-plan` and `reflective-brief`. Pairs with `01-thinking/why-what-how-done.md` and `01-thinking/falsifiability.md`.

## Scope

- In scope: goal through self-check with cited evidence, not full input duplication.
- Out of scope: repository edits without `reflective-implement`.

## Acceptance Criteria

- Uncertainty is explicitly marked.
- Composable with `02-engineering/task-start.md` as noted below.

## Falsifiability

Name one acceptance criterion that would fail if evidence were misquoted.

```markdown
你在中型 context window 中工作。請平衡完整性與節省 context。

任務：
{貼上任務}

請輸出：
1. Goal
2. Assumptions
3. Scope
4. Key Evidence / Inputs
5. Options
6. Trade-offs
7. Recommendation
8. Plan
9. Acceptance Criteria
10. Failure Conditions
11. Risks
12. Self-check

規則：
- 不要全文複製輸入。
- 引用重點即可。
- 對不確定處標記 uncertainty。
- 給出可執行 artifact。
```

> **Composition note:** When composed with `02-engineering/task-start.md`, `task-start.md` serves as the primary output template and this prompt provides window-size guidance for 32K-128K contexts.

