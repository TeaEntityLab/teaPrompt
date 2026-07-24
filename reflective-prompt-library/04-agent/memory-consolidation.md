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
- Each retained memory is future-useful, durable beyond the current task, self-contained for a reader without the original session, and identifies changeable facts that require fresh-source revalidation.
- Live task state and lookup-recoverable facts are excluded.

## Falsifiability

State what would disprove a pattern's claimed recurrence.

## Human Review

Escalate to `reflective-risk` before promoting executable knowledge (skills, hooks, runners).


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

請另外套用記憶品質檢查：
- 只保留未來仍可重用、跨任務仍有效，而且脫離原始工作階段也能獨立理解的內容。
- 排除即時任務狀態，以及可直接從目前原始資料查得的事實。
- 把記憶視為有日期的線索；會變動的內容在使用前要對照最新權威來源重新驗證。
```

