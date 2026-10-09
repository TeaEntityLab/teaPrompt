---
name: acceptance-join-validator
description: Lint a repo's acceptance surface — every REQ/AC ID in VERIFY.md/features must resolve to a locked runnable acceptance check; duplicates and dangling IDs flagged, every check command verified statically runnable.
license: MIT
compatibility: Requires a repo exposing a REQ/AC acceptance surface (VERIFY.md/features/ or acceptance.yaml); static resolvability checks only — never executes the checks it lists.
metadata:
  risk_level: low
  human_review_required: false
  external_io: false
  context_load: low
---

# Acceptance Join Validator

**Type:** Domain-pack skill (acceptance lint) — registered in the TeaPrompt source repo's domain-pack registry (`plans/validate_skill_examples.py` `DOMAIN_PACK_SKILLS`), not one of the nine frozen core workflow skills, and not selected by `reflective-dispatch` route rows; the host harness may invoke it directly.

## Purpose

Close the held AEAT-4 gap with a linter, not a new map or schema: given a product repo that already has a verification surface (`VERIFY.md` + `features/` map + a locked acceptance artifact), prove the requirement leg — every in-scope `REQ-`/`AC-` ID named in the docs resolves to a locked, runnable acceptance check — or fail loudly with the exact dangling ID. Evidence: `plans/agent-execution-assurance-taxonomy-survey-2026-09-30.md` AEAT-4 row ("acceptance-oracle join" held: each in-scope REQ/AC ID must reach a locked acceptance check, or an oracle-manifest entry resolving to such a check, exercised by a driver with recorded observation) and `plans/3xa-harness-survey-2026-08-20.md` 3XA-1 row (reviewed-batch hash binding deferred because `sensory-gate` specified hashes `verify_closeout.py` never compared — this validator performs the comparison its report enables).

## Module Contract

### Trigger

- A named product requests requirements-based verification and its repo carries `REQ-`/`AC-` IDs in `VERIFY.md` or `features/*.md`.
- A map sweep is green but nobody has shown the requirement leg is joined — the AEAT-4 reopen trigger (missing, ambiguous, stale, or skipped REQ/AC→check→driver→evidence binding plus authorization to assess).

### Inputs

1. Product repo root (read-only; default: cwd).
2. Requirement sources (default: `VERIFY.md`, `features/*.md`); ID pattern override (default `REQ`/`AC`, pattern `\b(?:REQ|AC)-[A-Za-z0-9][\w.-]*`).
3. Locked artifact path (default: `acceptance.yaml`; equivalent manifest accepted when it carries an immutability flag).

### Methods

1. **Extract requirement IDs.** Scan the requirement sources (default: `VERIFY.md` + `features/*.md`) for the ID pattern. Record each occurrence with file, line, and classification: a *definition* is an ID in a definition seat — a Markdown ATX heading naming the ID, a list item or table row whose first token is the ID, or an explicit `Requirement:`/`ID:` declaration line; every other occurrence — prose, inline code, parenthetical `(covers REQ-…)`, `exercises`/`drives`/`tests` mentions, and any `covers:` list entry — is a *reference* (a coverage reference when inside `covers:`). Only definitions participate in duplicate detection; references never create a definition.
2. **Extract check bindings.** Parse the locked artifact (default `acceptance.yaml`: `locked: true` + `checks:` entries with `id`, `verify`, `expect`/`expect_exit`). Accept an equivalent locked artifact — per AEAT-4, an oracle-manifest entry resolving to a check (observed shape: an oracle-manifest with `oracle_id`, `owner`, `commands`, `immutable: true`). Refuse unlocked artifacts: `locked: false`/missing, or `immutable: false`/missing, is a join failure, not a pass. A check `id:` is a check-side definition; its `covers:` list entries are coverage references, never check-side definitions.
3. **Join.** Every defined requirement ID must resolve to ≥1 check whose `id` equals the requirement ID or whose `covers:` list names it. Flag duplicates (same ID in two definition seats across requirement sources, or the same check `id:` twice in check sources) and dangling IDs (defined requirement ID with no check). One definition seat plus any number of reference mentions — including `covers:` references — is a clean multiple mention, not a duplicate. Orphan checks (check with no requirement ID) are reported as info only — checks may cover non-REQ invariants — and do not fail the run.
4. **Runnable check (static shell grammar, never executed).** The supported grammar is a `&&`-separated sequence of *simple commands*; `;`, `||`, `|`, `&`, command substitution, process substitution, glob expansion, and control keywords (`if`, `for`, `while`, subshells) are unsupported and classify the check as usage/refusal (`exit 2`), never as resolved or silently passed. Each segment supports: optional leading `NAME=value` assignments (stripped, never treated as the executable — so `FOO=1 make test` resolves `make`, not `FOO=1`); a single- or double-quoted first word (quotes removed after tokenizing; unmatched quotes are usage/refusal); then the executable word plus arguments. A bare `cd <dir>` segment changes the resolution directory for later segments only (`cd sub && ./test.sh` resolves `./test.sh` against `<root>/sub`); `cd` with no target, with flags, or into an absolute path is usage/refusal. Resolution per segment: a word containing `/` must exist as an executable file relative to the current resolution directory (starting at the repo root); a bare name must resolve via `PATH` (shell builtins other than `cd` are usage/refusal — only `cd` is supported). Tilde expansion, parameter/variable expansion (`$VAR`, `${VAR}`), and quoting that spans a `&&` boundary are unsupported and classify the segment as usage/refusal. This is static resolvability only — the validator never executes checks; execution belongs to the feature-map driver, whose observation is recorded as evidence elsewhere.
5. **Digest-bound report.** The report records `sha256` of the locked artifact and the repo `HEAD` (or `source_commit`), so a later closeout can deterministically compare reviewed-vs-shipped bytes — the 3XA-1 repair applied to the acceptance surface itself.

### Never

- Never treat an unlocked artifact (`locked: false`/missing, `immutable: false`/missing) as joined — it is a join failure, exit `1`.
- Never execute a check command itself; static resolvability only — runtime proof belongs to the driver sweep.
- Never invent checks for a repo that has requirement IDs but no locked artifact — report the AEAT-4 gap and route to `reflective-spec-plan`.
- Never accept a `covers:` claim as semantic proof — coverage declaration is trust-based; whether the check actually exercises the requirement stays a human review judgment.
- Never treat a repeated reference as a duplicate definition — one definition seat plus any number of reference mentions (prose, inline code, `covers:` entries) is a clean multiple mention; only a second definition seat (heading/list-row/declaration, or a second check `id:`) is a duplicate.
- Never let a dangling, duplicate, or unrunnable check pass silently — any of them fails the run with exit `1`.
- Never resolve an unsupported shell form as runnable — `;`, `||`, pipes, substitution, globs, variable/tilde expansion, or control keywords are usage/refusal (`exit 2`), not a pass and not a runnable failure.
- Never claim requirement coverage from a vacuous self-run — zero requirement IDs in scope means the join holds vacuously, nothing more.

### Output

- Human-readable join report on stdout plus `--json` machine form: per-ID rows (`ok` / `dangling` / `duplicate`), unrunnable-check rows, artifact lock status, artifact digest, repo HEAD, summary counts.
- Exit `0` on a clean join; exit `1` on any dangling ID, duplicate ID, unlocked artifact, or unrunnable check; exit `2` on usage error (missing sources, unparseable artifact).

### Escalation

- Repo has requirement IDs but no locked artifact at all → report the AEAT-4 gap (missing binding) and exit `1`; do NOT invent checks — route to `reflective-spec-plan` for a test-design pass first, mirroring the verification-map-generator escalation.
- Auth, permissions, security-sensitive, or destructive check commands → route to `reflective-risk` before anyone executes them; this validator only resolves their paths, never runs them.

### Failure signals

- A synthetic repo with one dangling AC passes the validator.
- A genuine double definition (second definition seat) passes silently.
- A repeated reference mention is misreported as a duplicate.
- `cd sub && ./test.sh` resolves the second segment against the repo root instead of `sub`.
- `FOO=1 make test` resolves `FOO=1` as the executable instead of `make`.
- An unsupported form (`;`, `||`, pipe, substitution, expansion) is treated as runnable or silently passed.
- A duplicate or unrunnable check passes silently.
- An unlocked artifact is treated as joined.
- The validator executes a check command itself.

### Verification

Build a synthetic repo (three requirement IDs across two `features/` files, `acceptance.yaml` with checks covering two) → validator must exit `1` naming the exact dangling ID; add the missing check → exit `0`. Negative controls: duplicate one ID with a second definition seat → exit `1`; repeat an ID only as prose/`covers:` references → still exit `0`; set `locked: false` → exit `1`; point one `verify` at a nonexistent script → exit `1`. Static-grammar controls: `cd sub && ./scripts/t.sh` resolves against `sub`; `FOO=1 make test` resolves `make`; `make test || make fallback` refuses with exit `2` without executing anything. Then run on TeaPrompt itself: it must pass or flag honestly (see Honest Limits).

## Honest Limits

- **TeaPrompt self-run is vacuous on the requirement leg.** No `REQ-`/`AC-` ID currently appears in root `VERIFY.md`, `features/`, or `acceptance.yaml` (verified by grep at admission time); the honest self-run result is `exit 0` with "0 requirement IDs in scope — join vacuously holds" plus the runnable-check pass over the existing checks. That does not demonstrate requirement coverage TeaPrompt does not claim; if IDs are introduced later, the validator must be re-run.
- **Static resolvability ≠ runnable in practice.** A command that resolves (`make`, `python3`, a repo script) can still fail at runtime (missing dep, wrong cwd, toolchain breakage). Runtime proof belongs to the driver sweep, not this linter.
- **`covers:` indirection is trust-based.** A check claiming to cover an ID is accepted on declaration; the validator does not semantically verify the check actually exercises the requirement. Semantic adequacy stays a human review judgment.
- **No execution, no evidence.** This validator produces a join report, not verification evidence; observation-with-spec/version/freshness binding is still the driver's and the run-note's job.
- **Single-repo, stdlib-only scope.** No cross-repo ID resolution, no network, no model calls. Suggested implementation: one Python standard-library script; deterministic; no writes outside the report.

## Examples

Companion examples live at `<skills-root>/examples/acceptance-join-validator.examples.md` when co-installed. They show the join-report shape, the dangling-ID failure, and the unlocked-artifact negative control — report shapes, not executed verification.

## Prompt Sources

*Provenance: TeaPrompt source-repository paths (`reflective-prompt-library/`), not runtime dependencies — the installed skill is self-contained.*

- `reflective-prompt-library/plans/agent-execution-assurance-taxonomy-survey-2026-09-30.md` (AEAT-4 held text and falsifier)
- `reflective-prompt-library/plans/3xa-harness-survey-2026-08-20.md` (3XA-1 deferred text; digest comparison repair)
- `reflective-prompt-library/plans/runtime-skills-task001-ticket-2026-10-06.md` (oracle-manifest shape reference)
- `reflective-prompt-library/skills/verification-map-generator/SKILL.md` (contract shape this skill follows)
