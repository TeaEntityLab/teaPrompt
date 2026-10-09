# acceptance-join-validator — Examples

## Example 1 — clean join (exit 0)

Input:

```text
Repo root: /tmp/shop-demo
Requirement sources: VERIFY.md (defines REQ-101, AC-101.1), features/checkout.md (defines REQ-102)
Locked artifact: acceptance.yaml (locked: true, 2 checks)
```

`VERIFY.md` excerpt (one definition seat per ID):

```markdown
# REQ-101 — Cart totals

- AC-101.1: guest checkout totals include tax.
```

`features/checkout.md` excerpt (definition seat plus legitimate references):

```markdown
## Checkout — REQ-102

Drive: `make test-checkout` — exercises AC-101.1 guest path (covers REQ-102).
```

AC-101.1 appears twice here — once as a definition in `VERIFY.md`, once as a
prose reference in `features/checkout.md` — and REQ-102's heading definition
is repeated by its parenthetical reference. Multiple mentions are not
duplicates: only a second definition seat would be.

`acceptance.yaml` excerpt:

```yaml
locked: true
checks:
  - id: REQ-101
    verify: make test-cart
    expect_exit: 0
    covers: [REQ-101, AC-101.1]
  - id: REQ-102
    verify: cd scripts && ./test-checkout.sh
    expect_exit: 0
```

The `REQ-102` check's second segment resolves against `scripts/` because the
leading `cd scripts` segment moves the resolution directory; the `covers:`
entries are coverage references, not second definitions of `REQ-101`/`AC-101.1`.

Expected output shape:

```text
REQ-101   ok   acceptance.yaml:4 (covers REQ-101)
AC-101.1  ok   acceptance.yaml:4 (via covers)
REQ-102   ok   acceptance.yaml:8 (cd scripts → ./test-checkout.sh)
lock: locked=true  artifact sha256:9f2c…  HEAD:a1b2c3d
summary: 3 ok, 0 dangling, 0 duplicate, 0 unrunnable → exit 0
```

## Example 2 — dangling ID (exit 1)

Input: same repo, but the `REQ-102` check is removed from `acceptance.yaml`.

Expected output shape:

```text
REQ-101   ok        acceptance.yaml:4
AC-101.1  ok        acceptance.yaml:4 (via covers)
REQ-102   dangling   features/checkout.md:1 — no check covers it
lock: locked=true  artifact sha256:71bd…  HEAD:a1b2c3d
summary: 2 ok, 1 dangling, 0 duplicate, 0 unrunnable → exit 1
```

The validator names the exact dangling ID (`REQ-102` with file and line);
adding the missing check returns the run to exit `0`.

## Example 3 — negative controls (each exit 1, none executes anything)

```text
Control A — genuine double definition: `## REQ-101` in VERIFY.md and a second
  `- REQ-101: …` definition row in features/cart.md
  → row `REQ-101 duplicate VERIFY.md:3, features/cart.md:7` → exit 1
Control B — repeated reference is NOT a duplicate: one `- AC-101.1: …`
  definition plus prose/`covers:` mentions of AC-101.1 elsewhere
  → rows stay `ok`, exit 0 (contrast control; proves the duplicate rule)
Control C — unlocked: acceptance.yaml sets `locked: false`
  → row `lock: UNLOCKED — join failure, not a pass` → exit 1
Control D — unrunnable: one check has `verify: ./scripts/missing.sh`
  → row `REQ-102 unrunnable: ./scripts/missing.sh not found relative to root` → exit 1
Control E — leading assignment: `verify: FOO=1 make test-cart`
  → resolves `make` via PATH, not `FOO=1` as an executable
Control F — cd context: `verify: cd scripts && ./test-checkout.sh`
  → resolves `./test-checkout.sh` against `<root>/scripts`, not `<root>`
```

In all six controls the validator only resolves command paths statically
(leading assignments stripped, quotes unwrapped, `cd` moves the resolution
directory for later segments, slash paths checked relative to that directory,
bare names via `PATH`) — it never runs the `verify` commands; execution
belongs to the feature-map driver.

## Example 4 — unsupported shell forms refuse without running (exit 2)

```text
Refusal A — `verify: make test || make fallback` (alternation)
Refusal B — `verify: cd $WORKDIR && make test` (variable expansion)
Refusal C — `verify: ./scripts/*.sh` (glob expansion)
```

Each reports `usage/refusal: unsupported shell form — <form> is outside the
static grammar` with exit `2`. Unsupported syntax is never treated as resolved
and never executed; the author must rewrite the check as supported
`&&`-separated simple commands or route the design question to
`reflective-spec-plan`.

## Example 5 — vacuous self-run shape (exit 0, zero IDs)

Input:

```text
Repo root: <tea-prompt-checkout> (no REQ-/AC- IDs in VERIFY.md, features/, or acceptance.yaml)
```

Expected output shape:

```text
0 requirement IDs in scope — join vacuously holds
lock: locked=true  artifact sha256:<digest>  HEAD:<sha>
runnable checks: 5/5 resolve
summary: 0 ok, 0 dangling, 0 duplicate, 0 unrunnable → exit 0
```

This claims nothing about requirement coverage the repo does not assert;
introducing IDs later requires a re-run.
