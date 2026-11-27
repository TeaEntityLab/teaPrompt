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

## Optional Worked Reference

[Anthropic's performance sprint](https://claude.dev/blog/how-we-made-claude-ai-faster/)
used instruction counts as CI guards on two hot paths after confirming that
reducing the counts also reduced elapsed time. The team measured user-journey
latency separately. [Vercel's Turborepo case](https://vercel.com/blog/making-turborepo-ninety-six-percent-faster-with-agents-sandboxes-and-humans)
reports a 97% microbenchmark improvement that translated into only a 0.02%
real-world gain.

For a slow-startup fix, compare time to the first usable screen before and
after under the same workload. If only the cheap benchmark improves, record
the proxy gain but leave the user-facing fix unverified. These team reports
do not set performance thresholds or establish the causal effect of an agent.
