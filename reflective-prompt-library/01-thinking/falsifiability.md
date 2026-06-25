# Falsifiability Prompt

Use this for scientific thinking, product experiments, AI workflows, and business models.

## Purpose

Turn vague ideas into testable hypotheses before experiments or delivery commitments. Primary workflow surfaces: `reflective-brief` for early framing; `reflective-spec-plan` when the hypothesis becomes a test plan.

## Scope

- In scope: scientific thinking, product experiments, AI workflow checks, business model bets.
- Out of scope: full implementation, formal-environment rollout, or external source surveys without a stated hypothesis.

## Acceptance Criteria

- Hypothesis is binary and observable.
- Prediction and falsifier are distinct.
- Minimum test, metrics, and timebox are concrete (no "feels better").
- Decision rule maps outcomes to next action.

## Falsifiability

Every output must include an explicit falsifier and a minimum test; if none can be stated, the idea is not ready for execution.

## Human Review

Escalate to `reflective-risk` with an explicit Human Review gate when the work implies irreversible or high-blast-radius action.


```markdown
請把以下想法改寫成可證偽假說。

## 想法
{貼上想法}

請輸出：

1. Hypothesis：可測假說
2. Prediction：若假說正確，應該觀察到什麼
3. Falsifier：什麼結果會推翻它
4. Minimum Test：最小測試
5. Metrics：觀察指標
6. Timebox：測試期限
7. Confounders：混淆因素
8. Decision Rule：根據結果如何決策
9. Next Iteration：下一輪如何修正

請避免空泛指標，例如「感覺更好」。請盡量轉成可觀察、可比較、可重複的證據。
```
