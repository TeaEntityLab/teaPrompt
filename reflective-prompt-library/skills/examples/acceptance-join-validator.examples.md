# acceptance-join-validator — Examples

## Example 1 — clean join (exit 0)

Input:

```text
Repo root: /tmp/shop-demo
Requirement sources: VERIFY.md (names REQ-101, AC-101.1), features/checkout.md (names REQ-102)
Locked artifact: acceptance.yaml (locked: true, 2 checks)
```

`features/checkout.md` excerpt:

```markdown
## Checkout (covers REQ-102)

Drive: `make test-checkout` — exercises AC-101.1 guest path.
```

`acceptance.yaml` excerpt:

```yaml
locked: true
checks:
  - id: REQ-101
    verify: make test-cart
    expect_exit: 0
    covers: [REQ-101, AC-101.1]
  - id: REQ-102
    verify: ./scripts/test-checkout.sh
    expect_exit: 0
```

Expected output shape:

```text
REQ-101   ok   acceptance.yaml:4 (covers REQ-101)
AC-101.1  ok   acceptance.yaml:4 (via covers)
REQ-102   ok   acceptance.yaml:8
lock: locked=true  artifact sha256:9f2c…  HEAD:a1b2c3d
summary: 3 ok, 0 dangling, 0 duplicate, 0 unrunnable → exit 0
```

## Example 2 — dangling ID (exit 1)

Input: same repo, but the `REQ-102` check is removed from `acceptance.yaml`.

Expected output shape:

```text
REQ-101   ok        acceptance.yaml:4
AC-101.1  ok        acceptance.yaml:4 (via covers)
REQ-102   DANGLING  features/checkout.md:1 — no check covers it
lock: locked=true  artifact sha256:71bd…  HEAD:a1b2c3d
summary: 2 ok, 1 dangling, 0 duplicate, 0 unrunnable → exit 1
```

The validator names the exact dangling ID (`REQ-102` with file and line);
adding the missing check returns the run to exit `0`.

## Example 3 — negative controls (each exit 1, none executes anything)

```text
Control A — duplicate: REQ-101 appears twice in check sources
  → row `REQ-101 duplicate acceptance.yaml:4, acceptance.yaml:12` → exit 1
Control B — unlocked: acceptance.yaml sets `locked: false`
  → row `lock: UNLOCKED — join failure, not a pass` → exit 1
Control C — unrunnable: one check has `verify: ./scripts/missing.sh`
  → row `REQ-102 unrunnable: ./scripts/missing.sh not found relative to root` → exit 1
```

In all three controls the validator only resolves command paths statically
(first path word exists on disk, bare names via `PATH`, `cd` exempt) — it never
runs the `verify` commands; execution belongs to the feature-map driver.

## Example 4 — vacuous self-run shape (exit 0, zero IDs)

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
