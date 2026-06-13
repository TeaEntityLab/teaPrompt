# Medium Context Window Prompt

Use this for 32K-128K context windows and ordinary ChatGPT / Claude / Codex tasks.

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

