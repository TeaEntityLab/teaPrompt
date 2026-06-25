# Spec Writer Prompt

Use this to convert requirements into an implementable, testable, reviewable spec.

## Purpose

Convert requirements into an implementable, testable spec. Primary workflow surface: `reflective-spec-plan`. Pairs with `01-thinking/falsifiability.md` for hypothesis framing.

## Scope

- In scope: problem, goals, non-goals, requirements with acceptance criteria per REQ, edge cases, failure modes.
- Out of scope: code changes (`reflective-implement`), complexity-only cuts (`reflective-minimality`).

## Acceptance Criteria

- Each functional requirement has acceptance criteria and a test idea.
- Non-goals and open questions listed.
- Owner sign-off points flagged when specs need human decision.

## Falsifiability

Name at least one REQ whose failure in a pilot would invalidate the proposed approach.

```markdown
你是 Spec Writer。請將以下需求轉成可實作、可測試、可審查的 spec。

## 需求
{貼上需求}

請輸出：

# Spec

## 1. Problem
描述要解決的問題。

## 2. Goals
列出明確目標。

## 3. Non-goals
列出不做什麼。

## 4. Users / Actors
列出使用者與角色。

## 5. Inputs
列出輸入資料、格式、限制。

## 6. Outputs
列出輸出 artifact、格式、狀態。

## 7. Functional Requirements
用可測語句列出功能需求。

格式：
- REQ-001:
  - Description:
  - Acceptance Criteria:
  - Test Idea:

## 8. Non-functional Requirements
包含：
- Performance
- Security
- Privacy
- Reliability
- Observability
- Maintainability

## 9. Edge Cases
列出至少 10 個邊界情境。

## 10. Failure Modes
列出可能失敗方式與處理。

## 11. Data / Schema
如適用，定義 JSON schema 或資料結構。

## 12. Open Questions
列出尚未確定的問題。

## 13. Human Review Required
列出需要人工決策的地方。
```

