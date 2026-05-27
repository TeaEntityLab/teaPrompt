---
name: reflective-risk
description: Use this before high-risk work involving security, privacy, auth, permissions, data deletion, migrations, production, billing, legal/medical/financial stakes, or irreversible decisions. It creates a dry-run, rollback, and Human Review gate before execution.
license: MIT
---

# Reflective Risk

## Purpose

Prevent irreversible mistakes. This skill is a gate, not an implementation plan.

## Trigger Conditions

Use before:

- Auth or permission changes
- Security-sensitive code
- Privacy-sensitive data handling
- Destructive file or database operations
- Database migrations
- Billing, ad spend, or financial actions
- Public API breaking changes
- Production deployment
- Legal, medical, or financial high-stakes advice

## Output

```markdown
## Goal

## Stakeholders

## Assets at Risk

## Threat Model

## Assumption Audit

## Evidence Check

## Failure Modes

## Worst-case Scenario

## Safe Dry-run Plan

## Rollback Plan

## Bounded Execution

## Audit Log Plan

## Human Review Required

## Human Approval Gate

## Acceptance Criteria

## Go / No-go Decision
```

## Rules

- Do not recommend direct production changes.
- Do not skip backup, dry-run, or rollback analysis.
- Do not assume permissions, data correctness, or safety.
- If the risk cannot be bounded, recommend no-go or human review.
- Define explicit execution boundaries (tools, scope, timebox, blast radius) before any action.
- Ensure an auditable record exists for high-risk steps and approvals.

## Prompt Sources

- `05-domain/high-risk.md`
- `02-engineering/local-feedback.md`
- `01-thinking/critical-thinking-check.md`
