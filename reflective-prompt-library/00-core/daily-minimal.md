# Daily Minimal Prompt

Use this for ordinary day-to-day work.

## Purpose

Day-to-day task framing with options and recommendation. Primary workflow surface: `reflective-brief`. Pairs with `01-thinking/falsifiability.md` and `01-thinking/why-what-how-done.md`.

## Scope

- In scope: daily tasks, options comparison, minimal plan, next action.
- Out of scope: spec authoring (`reflective-spec-plan`), code changes (`reflective-implement`).

## Acceptance Criteria

- Outputs Goal, Assumptions, Scope, Acceptance Criteria, Failure Conditions, Falsifiability, Options, Recommendation, Minimal Plan, Risks, Next Action.
- Prompting vs workflow depth called out explicitly.

## Falsifiability

Name one test or observation that would falsify the recommended option.

```markdown
請以反思型工程代理人處理。

任務：
{貼上任務}

請輸出：
1. Goal
2. Assumptions
3. Scope
4. Acceptance Criteria
5. Failure Conditions
6. Falsifiability
7. Options
8. Recommendation
9. Minimal Plan
10. Risks
11. Next Action

請額外檢查：
- 是否解錯問題
- 是否過度工程
- 是否缺少證據
- 是否需要 Human Review
- Prompting 是否足夠，還是需要 Agent / Workflow / 程式
```

