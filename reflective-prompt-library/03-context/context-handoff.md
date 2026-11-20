# Context Handoff Prompt

Use this when switching models, tools, agents, or sessions.

## Purpose

Produce session handoff summaries when switching models, tools, agents, or sessions. Primary workflow surface: `reflective-handoff-retro`. Pairs with `01-thinking/why-what-how-done.md` and `01-thinking/socratic-reviewer.md`.

## Scope

- In scope: goal, state, decisions, artifacts, risks, blockers, and next action for a successor agent.
- Out of scope: full retrospective synthesis or repository edits (`reflective-implement`).

## Acceptance Criteria

- Output follows the handoff field structure without narrative drift; summarized state preserves named invalidations and the decisions or steps they affect, rather than silently retaining withdrawn support as verified.
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

若工作卡在一個決定，先分清楚：哪些事在現有授權內可以查證，哪一步確實要等誰答覆。留下任務與版本、要問的問題、原因和建議；建議不等於核准。若已有決定，附上答覆來源、適用範圍和下一步，讓接手者不必重問。未答覆、已否決或範圍已變時，不要把該步驟寫成可以執行。

請只保留接手必要資訊，不要寫流水帳。
```

## Optional Worked Reference

[What reaches the next worker?](../plans/archdev-factory-attention-survey-2026-11-21.md) distinguishes notifying someone about a blocker from giving the next worker the owner's answer.
