# router-trace-linter — Examples

Companion examples for the domain-pack skill. These show expected verdict
and diff-row shapes, not proof that any route was semantically correct.

## Example 1 — Complete trace (must pass)

Input: a ten-field route trace for a low-risk wording task:

- `Mode: dispatch`
- `Strictness: L1`
- `Goal: reword the onboarding banner to match the style guide`
- `Assumptions: banner text only; no auth, billing, or production surface`
- `Workflow: reflective-minimality`
- `Route Confidence: medium`
- `Enhancements Enabled: none`
- `Enhancements Available: style-guide sweep after this edit (deferred: single string, no logic change)`
- `Human Review: not required — L1 wording change, reversible in one edit`
- `Next Action: run reflective-minimality on the banner copy`

Expected output shape:

- Verdict: `pass`, zero failing rows.
- Diff table: 10 rows, all `ok` with the raw line quoted per row
  (rationale reported as found in `Enhancements Available`).

## Example 2 — Missing downgrade rationale (must fail)

Input: same shape, but `Enhancements Available: performance review`
with `Assumptions:` blank and no `Rationale`/`Reason` line anywhere in
the trace.

Expected output shape:

- Verdict: `fail`.
- Failing row: `Enhancements Available: rationale-missing (R5/R7)` —
  a deferred skill is named but no ≥1-sentence (>20-character,
  non-placeholder) rationale is present; `Assumptions: missing
  (presence)` also fails.

## Example 3 — Blank confidence (must fail)

Input: a fully filled trace except `Route Confidence:` is blank.

Expected output shape:

- Verdict: `fail`.
- Failing row: `Route Confidence: unparseable (presence/parse)` — blank
  is never accepted; accepted values are `high | medium | low`
  (case-insensitive) or a numeric `0..1` float. Values like `maybe`,
  `confident`, `80%`, or a prose sentence also fail this row.

## Example 4 — High-risk route without review (must fail)

Input: a trace with `Strictness: L4`, `Goal: deploy the auth-service
migration to production`, `Workflow: reflective-risk`, and
`Human Review: none`.

Expected output shape:

- Verdict: `fail`.
- Failing row: `Human Review: review-missing (R4)` — `none` is a
  negation, not a review. The fix is a named reviewer sign-off, after
  which the underlying task still routes through `reflective-risk`
  before execution.

## Example 5 — Alias six-field form (must pass with warnings; hazard still fails)

Input: only the six machine keys, low-risk wording, and a rationale
sentence. No un-negated hazard keyword. `Mode`, `Strictness`, and
`Next Action` are absent.

```text
canonical_intent: reword the onboarding banner to match the style guide
workflow: reflective-minimality
confidence: medium
enhancements_enabled: none
enhancements_available: style-guide sweep after this edit (deferred: single string, no logic change)
rationale: the banner is copy only, so a wider workflow would not change the result
```

Expected output shape:

- Verdict: `pass`, warnings for absent `Mode`, `Strictness`, and
  `Next Action`. Absent `Human Review` is a warning because no
  high-risk signal fired.
- The same trace with `canonical_intent` containing `production` and
  no `Human Review` — verdict `fail`, row
  `Human Review: review-missing (R4)`.
