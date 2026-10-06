---
name: router-trace-linter
description: Use when a router emits a route trace and you need to check it against the Router Output Contract before accepting the route — required fields present, confidence parseable, downgrade/defer claims carrying explicit rationale (R5), and high-risk routes carrying Human Review (R4/R7). Outputs pass/fail plus a field-level diff.
license: MIT
metadata:
  risk_level: low
  human_review_required: false
  external_io: false
  context_load: low
---

# Router Trace Linter (Proposal)

**Status:** ADOPTED 2026-10-06 — registered domain pack; live contract at `skills/router-trace-linter/SKILL.md`. This file is the admission record.

**Type:** Domain-pack proposal (verification artifact) — NOT a registered skill, NOT one of the nine frozen core workflow skills, NOT selected by `reflective-dispatch` route rows. Inert until admission review; do not add to `skill-map.md` or `plans/validate_skill_examples.py` `DOMAIN_PACK_SKILLS` without passing the promotion gates.

## Purpose

Give hosts and reviewers a small deterministic checker that lints a router's emitted route trace against the Router Output Contract, so silent downgrades and missing rationale are caught as lint failures instead of shipped as accepted routes. Evidence: `reflective-prompt-library/plans/ROUTING_CONTRACT.md` §Router Output Contract (ten-field trace shape) with R5 route observability (downgrade/escalation rationale required) and R7 context-load deferral (deferred skills listed under available enhancements with rationale); machine-readable precedent in `plans/route-001-paraphrase-eval.yaml` `trace_required_fields` and `plans/validate_route_fixture.py` `REQUIRED_TRACE_FIELDS`; dry-run receipt pattern (record shape + preflight gate exit 0/4/4) observed at `/tmp/teaprompt-dryrun/host-task/` (`binding.json`, `run-note.json`, `checks/preflight.py`) per `reflective-prompt-library/plans/runtime-skills-task001-ticket-2026-10-06.md`.

## Module Contract

Trigger:

- A router (model, template, or host harness) has emitted a route trace and someone must decide whether to accept the route, release the work, or record the routing run.
- A review, eval sweep, or preflight-style gate needs a pass/fail verdict on trace completeness rather than a judgment on whether the chosen workflow was semantically right.

Methods:

- Field-presence check: normalize trace keys (case/whitespace/punctuation-insensitive: `Route Confidence` ≡ `confidence`) and require all ten contract fields — `Mode`, `Strictness`, `Goal`, `Assumptions`, `Workflow`, `Route Confidence`, `Enhancements Enabled`, `Enhancements Available`, `Human Review`, `Next Action`. Missing or blank field = fail with per-field row.
- Confidence-parse check: accept exactly `high | medium | low` (case-insensitive) or a numeric `0..1` float; anything else (blank, `maybe`, `confident`, `80%`, prose sentence) = fail. Rationale: TeaPrompt's standing rule is "evidence over confidence" — the linter checks the value is well-formed and therefore comparable, never that it is calibrated.
- Downgrade/defer-rationale check (R5/R7): when the trace signals reduced rigor, require explicit rationale text (≥1 non-placeholder sentence, >20 characters, not `n/a`/`none`/`tbd`). Signals: `Enhancements Available` non-empty (a deferred skill exists); `Workflow: prompt-only` or Fast Path taken where a workflow was in scope; `Strictness` below the risk-implied floor; or any line matching `downgrade|defer|fallback|default-up|instead of|skipped`. Rationale may live in `Assumptions` or a `Rationale`/`Reason` line — the linter reports where it found it.
- High-risk-review check (R4): when the trace signals high risk or irreversible impact — `Workflow` contains `reflective-risk`, `Strictness` is `L4`/`L5`, or `Goal`/`Assumptions` match `production|auth|billing|credential|secret|permission|privacy|pii|delet|destruct|irreversib|third-part` — require `Human Review` to be present, non-blank, and not a negation (`none`, `not required`, `n/a`). Anything weaker = fail.
- Diff output: emit one row per field (`ok | missing | unparseable | rationale-missing | review-missing`) plus the offending raw line or `<absent>`, so a reviewer can fix the trace without re-reading the contract.

Output:

- Single verdict `pass` or `fail`, followed by the field-level diff table (10 rows, one per contract field) and a one-line reason per failing row naming the rule (R5/R7/R4/presence/parse).
- No routing judgment: the linter never says which workflow *should* have been chosen — only whether the emitted trace satisfies the contract.

Escalation:

- Failing trace on low-risk work → return the diff to the router author for a one-line fix (usually add rationale or fill a blank field); do not escalate the task itself.
- Failing trace on high-risk work, or a second consecutive fail → route the underlying task through `reflective-risk` before execution; the lint failure is evidence, not a release.
- Dispute about whether the route was semantically correct → `reflective-review` of the artifact; dispute about whether the work should exist → `reflective-minimality`. The linter does not resolve either.

Inputs:

- One route trace as markdown text, YAML block, or key/value lines (the ten contract fields, in any order/casing). Machine `trace_required_fields` form (`canonical_intent, workflow, confidence, enhancements_enabled, enhancements_available, rationale`) is accepted as an alias subset — missing display-only fields (`Mode`, `Next Action`) are reported as warnings, not failures, in alias mode.
- Optional: the pre-route request text (one paragraph), used only to detect claimed-but-unexplained downgrades (e.g. request names tests, trace defers them silently). Never required; absence never fails the lint.

Failure signals:

- Linter passes a trace with a blank `Route Confidence` or a missing downgrade rationale (the two named must-fail fixtures regress).
- Linter fails a complete trace (the named must-pass fixture regresses).
- Two reviewers disagree on whether a verdict was correct given the same trace text (rule ambiguity — fix the rule wording, not the trace).

Verification: three self-contained fixtures, runnable without network or model calls —

1. `complete-trace` (must pass): all ten fields filled, `Route Confidence: medium`, `Enhancements Available: security review after bounded patch (deferred: L2 scope, no auth surface)` — verdict `pass`, zero failing rows.
2. `missing-rationale-downgrade` (must fail): `Enhancements Available: performance review` with `Assumptions` blank and no rationale sentence — verdict `fail`, row `Enhancements Available: rationale-missing (R5/R7)`.
3. `missing-confidence` (must fail): `Route Confidence:` blank — verdict `fail`, row `Route Confidence: unparseable (presence/parse)`. Optional fourth fixture: high-risk route (`Strictness: L4`, production deploy) with `Human Review: none` → `fail`, row `Human Review: review-missing (R4)`.

## Evidence Citation

- Contract shape: `reflective-prompt-library/plans/ROUTING_CONTRACT.md` §Router Output Contract — the ten-field markdown block (`Mode` … `Next Action`); R5 (uncertain routes carry confidence + downgrade/escalation reason), R7 (deferred high-load skills listed with rationale), R4 (high-risk work routes through Human Review gates).
- Machine precedent: `plans/route-001-paraphrase-eval.yaml` `trace_required_fields` + eval rules (`low_confidence_visibility`, `enhancement_visibility`, `no_silent_downgrade`); enforced by `plans/validate_route_fixture.py` (`REQUIRED_TRACE_FIELDS`, `REQUIRED_EVAL_RULES`); confidence vocabulary (`high`/`medium`) as emitted in `skills/examples/reflective-dispatch.examples.md`.
- Receipt pattern: `/tmp/teaprompt-dryrun/host-task/` — `binding.json` (pinned artifact hashes), `run-note.json` (evidence rows with precondition/result/exit_code), `checks/preflight.py` gate observed ready/stale/hold → exit 0/4/4; ticket `reflective-prompt-library/plans/runtime-skills-task001-ticket-2026-10-06.md` (TASK-003 wiring, GDR-4/5/6 refuters). The linter copies the *record shape* (pinned inputs, per-check rows, single exit verdict), not any enforcement claim.

## Honest Limits

- Syntax, not semantics: the linter proves the trace *says* something well-formed, not that the rationale is true or the workflow choice is right. A coherent invented rationale passes — cf. GDR-5's lesson that coherent invention does not release.
- Confidence is uncalibrated by design: `high` from a chat model is self-report with no calibration evidence (see decision-model survey DM-5/DM-6 rejection in repo history). The linter checks comparability only.
- High-risk keyword list is heuristic English-first (`production|auth|billing|…`); non-English or novel hazard phrasing can miss the review check. Misses are linter gaps, not route approvals — the underlying R4 duty still binds the router.
- Alias mode (machine six-field form) is leniency by construction: display-only gaps warn instead of fail. Gates that need strictness should require the full ten-field form.
- No recurrence evidence yet: this proposal has zero observed misroute catches. Admission needs ≥2 real failing traces caught pre-release plus a no-false-positive run over the existing `reflective-dispatch.examples.md` traces before registry consideration.
