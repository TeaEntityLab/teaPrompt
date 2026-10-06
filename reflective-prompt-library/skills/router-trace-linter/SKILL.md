---
name: router-trace-linter
description: Use when a router emits a route trace and you need to check it against the Router Output Contract before accepting the route — required fields present, confidence parseable, downgrade/defer claims carrying explicit rationale (R5), and high-risk routes carrying Human Review (R4/R7). Outputs pass/fail plus a field-level diff.
license: MIT
compatibility: Requires router route-trace artifacts conforming to the Router Output Contract; checks declaration completeness (fields, parseable confidence, downgrade rationale, high-risk Human Review) — cannot judge whether a deferral was justified.
metadata:
  risk_level: low
  human_review_required: false
  external_io: false
  context_load: low
---

# Router Trace Linter

**Type:** Domain-pack skill (verification artifact) — registered in the TeaPrompt source repo's domain-pack registry (`plans/validate_skill_examples.py` `DOMAIN_PACK_SKILLS`), not one of the nine frozen core workflow skills, and not selected by `reflective-dispatch` route rows; the host harness may invoke it directly.

## Purpose

Give hosts and reviewers a small deterministic checker that lints a router's emitted route trace against the Router Output Contract, so silent downgrades and missing rationale are caught as lint failures instead of shipped as accepted routes. Evidence: `reflective-prompt-library/plans/ROUTING_CONTRACT.md` §Router Output Contract (ten-field trace shape) with R5 route observability (downgrade/escalation rationale required) and R7 context-load deferral (deferred skills listed under available enhancements with rationale); machine-readable precedent in `plans/route-001-paraphrase-eval.yaml` `trace_required_fields` and `plans/validate_route_fixture.py` `REQUIRED_TRACE_FIELDS`.

## Module Contract

### Trigger

- A router (model, template, or host harness) has emitted a route trace and someone must decide whether to accept the route, release the work, or record the routing run.
- A review, eval sweep, or preflight-style gate needs a pass/fail verdict on trace completeness rather than a judgment on whether the chosen workflow was semantically right.

### Inputs

- One route trace as markdown text, YAML block, or key/value lines (the ten contract fields, in any order/casing). Machine `trace_required_fields` form (`canonical_intent, workflow, confidence, enhancements_enabled, enhancements_available, rationale`) is accepted as an alias subset — missing display-only fields (`Mode`, `Next Action`) are reported as warnings, not failures, in alias mode.
- Optional: the pre-route request text (one paragraph), used only to detect claimed-but-unexplained downgrades (e.g. request names tests, trace defers them silently). Never required; absence never fails the lint.

### Methods

1. **Field-presence check:** normalize trace keys (case/whitespace/punctuation-insensitive: `Route Confidence` ≡ `confidence`) and require all ten contract fields — `Mode`, `Strictness`, `Goal`, `Assumptions`, `Workflow`, `Route Confidence`, `Enhancements Enabled`, `Enhancements Available`, `Human Review`, `Next Action`. Missing or blank field = fail with per-field row.
2. **Confidence-parse check:** accept exactly `high | medium | low` (case-insensitive) or a numeric `0..1` float; anything else (blank, `maybe`, `confident`, `80%`, prose sentence) = fail. Rationale: TeaPrompt's standing rule is "evidence over confidence" — the linter checks the value is well-formed and therefore comparable, never that it is calibrated.
3. **Downgrade/defer-rationale check (R5/R7):** when the trace signals reduced rigor, require explicit rationale text (≥1 non-placeholder sentence, >20 characters, not `n/a`/`none`/`tbd`). Signals: `Enhancements Available` non-empty (a deferred skill exists); `Workflow: prompt-only` or Fast Path taken where a workflow was in scope; `Strictness` below the risk-implied floor; or any line matching `downgrade|defer|fallback|default-up|instead of|skipped`. Rationale may live in `Assumptions` or a `Rationale`/`Reason` line — the linter reports where it found it.
4. **High-risk-review check (R4):** when the trace signals high risk or irreversible impact — `Workflow` contains `reflective-risk`, `Strictness` is `L4`/`L5`, or `Goal`/`Assumptions` match `production|auth|billing|credential|secret|permission|privacy|pii|delet|destruct|irreversib|third-part` — require `Human Review` to be present, non-blank, and not a negation (`none`, `not required`, `n/a`). Anything weaker = fail.
5. **Diff output:** emit one row per field (`ok | missing | unparseable | rationale-missing | review-missing`) plus the offending raw line or `<absent>`, so a reviewer can fix the trace without re-reading the contract.

### Output

- Single verdict `pass` or `fail`, followed by the field-level diff table (10 rows, one per contract field) and a one-line reason per failing row naming the rule (R5/R7/R4/presence/parse).
- No routing judgment: the linter never says which workflow *should* have been chosen — only whether the emitted trace satisfies the contract.

### Never

- Never pass a trace with a blank `Route Confidence` or a missing downgrade rationale (the two named must-fail fixtures regress if this happens).
- Never fail a trace that fills all ten fields with well-formed values (the named must-pass fixture regresses if this happens).
- Never state which workflow *should* have been chosen — report only whether the emitted trace satisfies the contract.
- Never present a `pass` as evidence the rationale is true, the confidence is calibrated, or the workflow choice was right: a coherent invented rationale passes the syntax check.
- Never treat a high-risk-keyword miss as a route approval — the underlying R4 duty still binds the router when the heuristic list misses.
- Never fail alias-mode (machine six-field) traces on display-only gaps (`Mode`, `Next Action`) — warnings only; gates that need strictness must require the full ten-field form.
- Never invent rationale, confidence, or review text to turn a fail into a pass — return the diff to the router author for a one-line fix.
- Never adjudicate whether the route was semantically correct or whether the work should exist — escalate instead (see Escalation).

### Escalation

- Failing trace on low-risk work → return the diff to the router author for a one-line fix (usually add rationale or fill a blank field); do not escalate the task itself.
- Failing trace on high-risk work, or a second consecutive fail → route the underlying task through `reflective-risk` before execution; the lint failure is evidence, not a release.
- Dispute about whether the route was semantically correct → `reflective-review` of the artifact; dispute about whether the work should exist → `reflective-minimality`. The linter does not resolve either.

### Failure signals

- Linter passes a trace with a blank `Route Confidence` or a missing downgrade rationale (the two named must-fail fixtures regress).
- Linter fails a complete trace (the named must-pass fixture regresses).
- Two reviewers disagree on whether a verdict was correct given the same trace text (rule ambiguity — fix the rule wording, not the trace).

### Verification

Three self-contained fixtures, runnable without network or model calls —

1. `complete-trace` (must pass): all ten fields filled, `Route Confidence: medium`, `Enhancements Available: security review after bounded patch (deferred: L2 scope, no auth surface)` — verdict `pass`, zero failing rows.
2. `missing-rationale-downgrade` (must fail): `Enhancements Available: performance review` with `Assumptions` blank and no rationale sentence — verdict `fail`, row `Enhancements Available: rationale-missing (R5/R7)`.
3. `missing-confidence` (must fail): `Route Confidence:` blank — verdict `fail`, row `Route Confidence: unparseable (presence/parse)`. Optional fourth fixture: high-risk route (`Strictness: L4`, production deploy) with `Human Review: none` → `fail`, row `Human Review: review-missing (R4)`.

## Honest Limits

- Syntax, not semantics: the linter proves the trace *says* something well-formed, not that the rationale is true or the workflow choice is right. A coherent invented rationale passes.
- Confidence is uncalibrated by design: `high` from a chat model is self-report with no calibration evidence. The linter checks comparability only.
- High-risk keyword list is heuristic English-first (`production|auth|billing|…`); non-English or novel hazard phrasing can miss the review check. Misses are linter gaps, not route approvals — the underlying R4 duty still binds the router.
- Alias mode (machine six-field form) is leniency by construction: display-only gaps warn instead of fail. Gates that need strictness should require the full ten-field form.
- Recurrence evidence is still thin: at registration the linter had zero observed misroute catches. Record real failing traces caught pre-release, plus a no-false-positive run over the existing `reflective-dispatch.examples.md` traces, before treating early passes as established practice.

## Examples

Companion examples live at `<skills-root>/examples/router-trace-linter.examples.md` when co-installed. They show pass/fail verdict shapes and field-level diff rows, not a judgment that any route was semantically correct.

## Prompt Sources

*Provenance: TeaPrompt source-repository paths (`reflective-prompt-library/`), not runtime dependencies — the installed skill is self-contained.*

- `reflective-prompt-library/plans/ROUTING_CONTRACT.md` (§Router Output Contract ten-field shape; R4/R5/R7 duties)
- `reflective-prompt-library/plans/route-001-paraphrase-eval.yaml` (`trace_required_fields` + eval rules `low_confidence_visibility`, `enhancement_visibility`, `no_silent_downgrade`)
- `reflective-prompt-library/plans/validate_route_fixture.py` (`REQUIRED_TRACE_FIELDS`, `REQUIRED_EVAL_RULES`)
- `reflective-prompt-library/skills/examples/reflective-dispatch.examples.md` (confidence vocabulary as emitted; no-false-positive corpus)
