# High-risk Review Prompt

Use this for security, privacy, money, destructive operations, and production-sensitive work.

## Purpose

Gate security, privacy, billing, destructive, and production-sensitive work before irreversible action. Primary workflow surfaces: `reflective-risk` and `reflective-review`. Pairs with `01-thinking/critical-thinking-check.md`, `01-thinking/counterargument.md`, and `01-thinking/falsifiability.md`.

## Scope

- In scope: threat model, assumption audit, rollback/dry-run plan, go/no-go framing.
- Out of scope: silent execution of irreversible changes (`reflective-implement` without review).

## Acceptance Criteria

- Human confirmation required before irreversible or high-blast-radius recommendations.
- Rollback and dry-run paths explicit when delivery is contemplated.

## Falsifiability

Name one threat or failure mode that would change the go/no-go decision.

## Human Review

Require human approval before any irreversible recommendation or production-facing change.

```markdown
這是高風險任務。請啟用 High-risk Review Mode。

## 任務
{貼上任務}

請先不要執行任何不可逆建議。請輸出：

1. Goal
2. Stakeholders
3. Assets at Risk
4. Threat Model
5. Assumption Audit
6. Evidence Check
7. Failure Modes
8. Worst-case Scenario
9. Rollback Plan
10. Human Review Required
11. Safe Dry-run Plan
12. Acceptance Criteria
13. Go / No-go Decision

規則：
- 不得建議直接上 production。
- 不得略過備份、rollback、dry-run。
- 不得假設權限、安全、資料正確。
- 涉及金錢、資料刪除、auth、隱私，一律要求人工確認。
```

