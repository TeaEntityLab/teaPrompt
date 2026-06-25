# Routing Contract

## Purpose

Define fairness and observability requirements for task routing so equivalent user intent receives equivalent quality.

## Core Rule

```text
Same intent, same route; same risk, same rigor; uncertain route must be visible, not silent.
```

## Contract Scope

This contract applies to:

- Skill/workflow routing.
- Rigor and enhancement selection.
- Low-confidence fallback behavior.
- User-visible route trace output.

## Normative Terms

- Intent signal: semantic evidence of user goal; not an exact keyword match.
- Canonical route: normalized workflow target selected by the router.
- Rigor: depth level of validation and review for the routed task.
- Enhancement: optional checks such as tests, security review, or performance review.
- Silent downgrade: equivalent intent routed to lower quality without explicit visibility.

## Requirements

### R1: Intent Normalization

- The router must normalize user phrasing to a canonical intent before applying trigger cues.
- Trigger cues are examples, not required wording.

### R2: Fairness by Phrasing

- Equivalent intent should map to the same canonical route.
- Keyword fast paths are allowed but cannot be the sole route decision signal.

### R3: Rigor Consistency

- Equivalent risk and intent should receive equivalent rigor.
- If rigor differs, the route trace must explain why.

### R4: Risk-based Default-up

- If confidence is low and risk is low, prefer a visible default-up over silent downgrade.
- If confidence is low and risk or cost is high, run a lightweight intent probe before execution.
- High-risk or irreversible work must route through Human Review gates.

### R5: Route Observability

- Every uncertain route must include a route trace:
  - Canonical intent
  - Selected workflow
  - Confidence level
  - Enabled enhancements
  - Available but disabled enhancements
  - Reason for downgrade or escalation

### R6: Cost Governance

- Cost controls may change depth, but must not silently reduce baseline quality for equivalent intent.
- Cost-based fallback decisions must be explicit in route trace.
### R7: Context Load Deferral

- Skills declare `context_load: low|medium|high` in frontmatter.
- At Strictness `L1`–`L2`, hosts may defer `high` context_load skills when a smaller workflow still satisfies intent.
- Deferred skills must appear in route trace under available enhancements with rationale.
- Deferral is not a silent downgrade: equivalent high-rigor intent must still receive equivalent outcomes or an explicit escalation path.


### R8: Holdout-before-tune

- Add fresh ROUTE-002 holdout and ROUTE-003 adversarial phrases **before** tuning
  `route_paraphrase_eval.py` keyword or boundary rules.
- `validate_route_fixture.py` enforces minimum group and phrase counts in CI.
- Holdout expansion is maintenance, not proof of broad semantic routing.

### R10: Brief-before-plan

- Phrases that scope goals, assumptions, or stakeholder alignment **before** PRD/ticket artifacts route to `reflective-brief`, not `reflective-spec-plan`.
- Skill-catalog questions (which skill handles X) route to `reflective-dispatch`, not execution workflows.

### R9: Production-negation and plan-only boundaries

- Phrases that **negate** production risk (e.g. "not production deploy", 不是正式環境風險)
  must not auto-route to `reflective-risk` when the user requests plain code review.
- Planning-only requests with explicit no-code context route to `reflective-spec-plan`,
  even when incidental words like "change" appear in "code changes".
- Add holdout cases for these boundaries before tuning router keyword lists.

### R11: Approved-spec delivery

- Phrases that request **implementing or landing an approved spec in the repository**
  route to `reflective-implement`, not `reflective-spec-plan`, even when the word `spec` appears.
- Plan-only variants (tickets, rollout, or acceptance criteria with explicit no-code context)
  still route to `reflective-spec-plan`.
- Add ROUTE-003 `implement_not_plan_trap` holdout phrases (including mixed zh-TW + English approved-spec delivery) before tuning this boundary.


## Router Output Contract

Use this minimal output shape for routing responses:

```markdown
Mode:
Strictness:
Goal:
Assumptions:
Workflow:
Route Confidence:
Enhancements Enabled:
Enhancements Available:
Human Review:
Next Action:
```

## Failure Modes

- Intent routing failure: equivalent intent maps to different canonical routes.
- Quality enhancement failure: equivalent rigor requests get different enhancement stacks.
- Observability failure: route decisions or downgraded capabilities are hidden.
- Default policy failure: low confidence silently defaults to lower quality.

## Acceptance Criteria

- Route consistency: aspirational target ≥95%; Phase-1 threshold: ≥70%; current measured: 100.0% on ROUTE-001 (see QUALITY_GATES_SUMMARY.md).
- All low-confidence routes emit route trace fields.
- No silent downgrade events in sampled routing runs.

## Related Artifacts

- `plans/code-followups-plan.md` (`ROUTE-001`)
- `plans/route-001-paraphrase-eval.yaml`
- `skills/reflective-dispatch/SKILL.md`
- `skills/SKILL_TRIGGER_CHEATSHEET.md`
