# Critical Thinking Review Prompt

Use this to review articles, strategies, product ideas, technical choices, or AI-generated claims.

## Purpose

Audit claims, assumptions, and evidence quality before accepting a plan, article, or AI output. Primary workflow surfaces: `reflective-review` for diff/plan critique; `reflective-implement` for evidence before material commits; `reflective-risk` for high-blast-radius checks; pair with `reflective-research` when external sources are required.

## Scope

- In scope: articles, strategies, product ideas, technical choices, AI-generated claims, diff/plan review prep.
- Out of scope: writing first-draft specs (`reflective-spec-plan`), repository implementation (`reflective-implement`), formal-environment gating (`reflective-risk`).

## Acceptance Criteria

- Major and minor claims listed separately.
- Assumption audit distinguishes explicit vs implicit risks.
- Strongest counterargument stated (not a strawman).
- Each conclusion tagged: supported, plausible-but-unproven, or unsupported.

## Falsifiability

Name at least one observation, dataset, or experiment that would overturn the strongest supported conclusion.

## Human Review

Escalate to `reflective-risk` with an explicit Human Review gate when the work implies irreversible or high-blast-radius action.


```markdown
請用 Critical Thinking Review 嚴格審查以下內容：

## 待審查內容
{貼上內容}

## 請依序分析

### 1. Claim Extraction
列出主要主張與次要主張。

### 2. Assumption Audit
列出：
- 明示假設
- 隱含假設
- 高風險假設
- 需要證據的假設

### 3. Evidence Check
檢查：
- 有哪些證據？
- 證據品質如何？
- 是否有資料缺口？
- 是否有過度推論？

### 4. Counterargument
提出最強反方論點，而不是稻草人反駁。

### 5. Fallacy Scan
檢查是否存在：
- False dichotomy
- Strawman
- Appeal to authority
- Hasty generalization
- Survivorship bias
- Confirmation bias
- Motte-and-bailey
- Slippery slope
- Goodhart's Law
- Reward hacking

### 6. Falsifiability
什麼觀察、資料或實驗會推翻此主張？

### 7. Decision
請分類：
- Strong conclusion
- Weak conclusion
- Plausible but unproven
- Unsupported
- Dangerous assumption

### 8. Recommendation
最後給：
- 可採納部分
- 必須修正部分
- 需要更多證據部分
- 不建議採用部分
```
