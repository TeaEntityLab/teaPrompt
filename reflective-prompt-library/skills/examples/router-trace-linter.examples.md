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

## Example 6 — R4 contrastive matrix (bypasses deny, controls hold)

Base: the low-risk control trace (`Mode: dispatch`, `Strictness: L2`,
`Goal: rename a local variable`, `Assumptions: Only the actions in Goal
are planned.`, `Workflow: reflective-implement`,
`Route Confidence: medium`, `Enhancements Enabled: none`,
`Enhancements Available: none`, `Human Review: not required`,
`Next Action: execute the named change`), substituting only the named
`Goal`, `Workflow`, or `Human Review` field:

- `Goal: No auth changes, deploy to production, and rotate credentials`
  + `Human Review: not required` → `fail`,
  `Human Review: review-missing (R4)` — the denial covers `auth` only;
  the later `deploy`/`rotate` actions re-open the scope.
- `Goal: deploy to production` + `Human Review: false` → `fail`
  (`review-missing (R4)`).
- `Goal: deploy to production` + `Human Review: not applicable`
  (either spelling) → `fail` (`review-missing (R4)`).
- `Goal: deploy to production` + `Human Review: tbd` → `fail`
  (`review-missing (R4)`).
- `Goal: deploy to production` + `Human Review: **none**`
  (markdown-bold) → `fail` (`review-missing (R4)`).
- `Goal: deploy to production` + `Human Review: "none"` (quoted) →
  `fail` (`review-missing (R4)`).
- `Workflow: Reflective-Risk` (capitalized) on the low-risk rename →
  `fail` (`review-missing (R4)`) — workflow gating is case-insensitive.
- Supported-negation positives (unchanged): low-risk rename +
  `not required` → `pass`; production + `none` → `fail`; production +
  `skipped` → `fail`.

## Example 7 — Quoted confidence (must pass; unparseable still fails)

Input: the low-risk control trace with
`Route Confidence: "medium"` (YAML-style quoted scalar). The same
verdict holds for `'medium'`, `**medium**`, `"high"`, `"low"`, and
`"0.8"` — supported quoting/markdown wrapping is stripped before the
parse check.

Expected output shape:

- Verdict: `pass`, zero failing rows.
- Genuinely unparseable values (`maybe`, `confident`, `80%`, a prose
  sentence) still fail with
  `Route Confidence: unparseable (presence/parse)`.

## Example 8 — Folded/literal block scalars (representation parity)

Input: a high-risk trace whose `Goal` is written as a YAML folded scalar:

```text
Mode: routing
Strictness: L4
Goal: >
  deploy the auth-service migration
  to production
Assumptions: production deploy window
Workflow: reflective-risk
Route Confidence: high
Enhancements Enabled: risk gate
Enhancements Available: none
Human Review: none
Next Action: stop for review
```

Expected output shape:

- Verdict: `fail`.
- Failing row: `Human Review: review-missing (R4)` — the folded
  continuation is part of `Goal`, so `deploy ... production` still
  reaches the risk scan. A literal `|` block behaves identically.
- The same folded form on low-risk wording (e.g. `rename a local
  variable` across two indented lines) passes.
- A field whose value is only an unsupported scalar indicator
  (`Goal: ?`, `Goal: !`, `Goal: >-`, `Goal: |+`, flow `[]`/`{}`) fails
  as `unparseable (unsupported scalar form)` — the marker is refused,
  never read as the field's content.

## Example 9 — Documented low-risk forms (must pass)

Inputs that a correct linter accepts:

- `Goal: credit the original author in the changelog` — `author`,
  `authors`, `authorship`, and `coauthor` never fire the hazard scan;
  `auth`, `authentication`, `authorize`, and `auth-service` still do.
- A six-field alias trace whose `rationale` is short but complete
  (`rationale: copy change only`) — it fills `Assumptions` and passes
  with the usual alias warnings; the >20-character sentence rule
  applies only when a deferral signal is present.
- `Assumptions` carrying a meaningful sentence (`The existing suite
  already covers this surface well`) satisfies a deferred enhancement
  as a rationale seat without inventing keyword requirements.
- `Human Review: skipped` on a low-risk trace with no deferred
  enhancement passes — `skipped` is review status, not a deferral
  claim. (On a genuine high-risk trace it still fails R4.)
