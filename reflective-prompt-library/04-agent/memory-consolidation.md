# Memory / Knowledge Consolidation Prompt

Use this to turn repeated task experience into reusable knowledge.

## Purpose

Consolidate repeated lessons into maintainable knowledge. Primary workflow surface: `reflective-handoff-retro`. Pairs with `01-thinking/falsifiability.md`.

## Scope

- In scope: pattern extraction, promotion candidates, anti-regression tests, trust-boundary lessons.
- Out of scope: silent promotion into `AGENTS.md` or `SKILL.md` without human approval.

## Acceptance Criteria

- Each pattern has recurrence evidence or explicit project decision pointer.
- Promotion destination classified (principle, lesson, decision index, skill candidate).
- Authority class separated: project-design judgement vs agent operating rule.

## Falsifiability

State what would disprove a pattern's claimed recurrence.

## Human Review

Require human approval before promoting executable knowledge (skills, hooks, runners).


```markdown
請將以下多次任務經驗整理成可重用知識。

## Logs / Retros
{貼上內容}

請輸出：

1. Repeated Patterns
2. Repeated Failures
3. Root Causes
4. New Rules
5. New Checklists
6. New Skills Needed
7. New Scripts Needed
8. Anti-regression Tests
9. Prompt Updates
10. Workflow Updates

請區分：
- 一次性事件
- 重複模式
- 應該制度化的規則
- 不值得制度化的偶發問題
```

