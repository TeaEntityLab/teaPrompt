# Context Handoff Prompt

Use this when switching models, tools, agents, or sessions.

## Purpose

Produce session handoff summaries when switching models, tools, agents, or sessions. Primary workflow surface: `reflective-handoff-retro`. Pairs with `01-thinking/why-what-how-done.md` and `01-thinking/socratic-reviewer.md`.

## Scope

- In scope: goal, state, decisions, artifacts, risks, blockers, and next action for a successor agent.
- Out of scope: full retrospective synthesis or repository edits (`reflective-implement`).

## Acceptance Criteria

- Output follows the handoff field structure without narrative drift.
- Do-not-do guidance explicit when blast-radius warrants `reflective-risk`.

## Falsifiability

Name one handoff field that would be wrong if the successor could not resume work.

## Human Review

Require human confirmation before handoff when irreversible or high-blast-radius work remains open.

```markdown
請將目前任務整理成 Context Handoff Summary，供下一個 Agent 接手。

請輸出：

1. Goal
2. Current State
3. Decisions Made
4. Assumptions
5. Files / Artifacts
6. Completed Work
7. Remaining Work
8. Risks
9. Blockers
10. Acceptance Criteria
11. Commands / Tests Run
12. Next Recommended Action
13. Do Not Do
14. Human Review Required

請只保留接手必要資訊，不要寫流水帳。
```

