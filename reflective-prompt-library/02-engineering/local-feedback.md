# LOCAL_FEEDBACK Prompt

Use this when something fails.

## Purpose

Structured LOCAL_FEEDBACK loop for failures during implementation. Primary workflow surface: `reflective-implement`. Pairs with `01-thinking/critical-thinking-check.md` for evidence and assumption audits.

## Scope

- In scope: step, evidence, root cause, correction, verification, anti-regression rule.
- Escalate: route to `reflective-review` when the failure implicates spec or test adequacy.
- Out of scope: spec rewriting (`reflective-spec-plan`), formal blast-radius gating (`reflective-risk`).

## Acceptance Criteria

- Root cause separated from symptom.
- Verification step names an observable pass signal.
- Rollback decision explicit.

## Falsifiability

If the proposed correction cannot be verified with a named command or observation, treat it as hypothesis not fix.

## Human Review

Escalate to `reflective-risk` when rollback or correction implies trust-boundary or data-loss blast radius.

```markdown
請用 LOCAL_FEEDBACK 流程分析錯誤。

## 錯誤描述
{貼上錯誤}

## 請輸出

1. Step：錯在哪一步
2. Evidence：根據什麼判斷
3. Error Type：錯誤類型
4. Root Cause：根本原因
5. Correction：修正方式
6. Next Action：下一步
7. Verification：如何驗證修正成功
8. Anti-regression Rule：如何避免再發生
9. Should we rollback?：是否需要回滾
10. Human Review Required?：是否需要人工審查
```

