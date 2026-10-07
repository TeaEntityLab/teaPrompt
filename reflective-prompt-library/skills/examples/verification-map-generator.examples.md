# verification-map-generator — Examples

Companion examples for the domain-pack skill. These show expected output
shapes, not proof that code was executed.

## Example 1 — HTTP server product (wsgiLite.js shape)

Input: "do experiments on this repo" over an Express-like demo app.

Generated surface:

- `VERIFY.md` — launch `node demo/simple-routing.js`, doctor
  `curl localhost:PORT/heartbeat`, drive = curl per route in feature files,
  evidence = response bodies to scratch dir, the four-way failure
  classification table (product regression / doc drift / spec-oracle error /
  harness failure), cleanup = stop the demo server and remove the scratch dir.
- `features/README.md` — index of the feature files below.
- `features/routing.md`, `features/csrf-upload.md`, `features/errors.md` —
  each with `source_commit` + `last_verified_at` + `verification_status`
  metadata, entry points (route table), drive (curl commands), observable
  outcomes (expected bodies/statuses), failure paths, evidence.
- Environment quirk recorded verbatim: launch directory changes what
  `/file/../` traversal serves — cwd-dependent, documented not hidden.

Fresh-agent result: 15/15 routes verified; a seeded `/heartbeat` → `pong`
bug classified product regression; a stale map classified doc drift; a
locked spec claiming `pong` classified spec-oracle error.

## Example 2 — Library product (fpGo/fpEs/fpRust shape)

Input: "do experiments on @~/dev/fpGo/" over a Go library.

Generated surface:

- `VERIFY.md` — launch `go test -mod=mod ./...` (the `-mod=mod` flag is the
  recorded environment quirk: stale `vendor/` vs `go.mod`), doctor =
  `go vet` + smoke `-run` regex, drive = per-feature `-run` regexes,
  evidence = `go test -json` output to scratch dir, the four-way failure
  classification table, cleanup = remove scratch drivers.
- `features/README.md` — index of the feature files below.
- `features/core.md`, `collections.md`, `queues.md`, `concurrency.md`,
  `integrations.md` — each carries `source_commit` + `last_verified_at` +
  `verification_status` metadata; the product's own test suite is the
  oracle; the map routes feature areas to test regexes.

Fresh-agent result: 1013/1013 baseline; unlabeled `Distinct` bug classified
product regression; wrong spec classified spec-oracle error. Same shape
replicated on npm (mocha `--grep`) and cargo (`cargo test <module>::`).

## Example 3 — Wrong-spec arm

Input: healthy product + docs + LOCKED `acceptance.yaml` claiming
`Maybe.just(null).isPresent() == true` (product returns false).

Expected fresh-agent output: FAIL on that check, classified
**spec-oracle error** — citing the implementation line, the feature map's
observable outcome, and existing tests as ground truth; the locked spec is
indicted, not the product.
