# TASK-001 Ticket — Governed-Delivery Dry Run (Private Copy)

> **Status: ACCEPTED by named accepter (user) — 2026-10-06.** Companion execution ticket to `runtime-skills-workflow-spec-2026-10-06.md` (RSD-2). Bindings resolved, TASK-002 probes executed, oracle green on the copy, gate observed ready/stale/hold → 0/4/4. Human acceptance recorded 2026-10-06; executor did not self-accept.

## Evidence vs Inference

Approved facts: the 2026-10-06 user rulings (task class = governed-delivery dry run on a private copy; TASK-002 scoped probes bounded to the named task root). Everything marked `UNKNOWN` below is an input the spec's Definition of Ready assigns to a named owner — no default value is implied by this draft. [INFERENCE]: the generated artifact set below is the planner's inference from RSD-2 §3/§4; the artifact owner can still cut items the task does not need.

## TASK-001: Instantiate governed delivery on a private copy

- Goal: one complete governed-delivery task contract on a private copy of a real repository — exercise spec → packet → intent → host preflight → bounded work → pre-release verification → named acceptance, end to end, with zero production writes.
- Scope: generation of the task's artifact set and its dry-run wiring only. No provider/model invocation (that is TASK-004+); no new TeaPrompt runner; no registry/adoption change.
- Inputs (all required; each is `UNKNOWN` until its owner supplies it):

| Input | Owner | Bound value |
| --- | --- | --- |
| Concrete private task root | user/product owner | `/tmp/teaprompt-dryrun` (`cp -R` of working tree, 15M) |
| Expected product result + independent oracle | spec owner | repo validation suite green on the copy: `pytest plans/tests` (1439 pass), `validate_record_hygiene.py`, `validate_links.py` |
| Actual CLI command/profile | host owner | `sandbox-exec -f host-task/profile.sb bash -c` (executed spelling; `-lc` arg-shifts the command into `$0` — diagnosed and abandoned) |
| `spec_version` / `host_identity` | spec/host owner | `sha256:431150dc…` / `darwin 25.6.0 arm64; seatbelt …` (both in `binding.json`) |
| Permitted writes + sink allowlist | host owner | writes: `host-task/work/**` + `host-task/STATE/**` only; sinks: none (egress denied entirely) |
| Host-enforced caps | human account/task owner | provisional 2026-10-06 grant: ≤1 invocation per CLI, read-only stdin proposal, no writes — formal per-call/total envelope still owed before repeated runs |
| Named accepter for delivery closure | user/product owner | the user (2026-10-06) |
| Named artifact owner | user/product owner | the user (2026-10-06) |

- Outputs: task-selected packet set only — spec, oracle manifest, task packet, run-note + binding (`checks/run-preflight.sh` wired to `checks/preflight.py`), and the prompts/script for the chosen topology (one-pass flow or bounded loop). Governance objects beyond the delivery record only if the task needs them.
- Dependencies: none upstream; TASK-002 (below) unblocks the operational half.
- Authority / Data Boundary: model generates artifacts; host executes and observes; named human signs intent and acceptance. The generated script is a host-run artifact, not a TeaPrompt-owned runner.
- Runtime / Tool Gates: preflight runs before first dispatch and after work before release; unknown/stale required controls hold; exit 4 cases never dispatch.
- Acceptance Criteria: a fresh reader can name the final result, required checks, and permissions; missing acceptance criterion stops generation (governed-delivery invariant); every `UNKNOWN` input either resolved or the ticket stays blocked — partially bound is not ready.
- Tests: existing consumer/stub tests verify the generated artifact shapes; a new instantiation smoke only for this binding (RSD-2 §7).
- Files likely touched: only under the named task root (`host-task/` convention): `spec`, `oracle-manifest`, `task-packet`, `run-note.json`, `binding.json`, `checks/`, `prompts/`, `STATE/` — no TeaPrompt repo files by default.
- Risk: low for drafting; the dry run itself is only as safe as its probe/binding step.
- Parallelizable: no — single integration owner.
- Human Review Required: yes — intent, scope, and acceptance stay human-signed.

## TASK-002: Scoped host-control probes (pre-authorized, bounded)

Within the granted scope (positive + intended-denial probes on the named task root only; no ambient credentials; no billing/network changes; no TeaPrompt runner):

- Positive controls: write to the permitted mutable surface; spawn one descendant process under the role and observe inheritance (does the descendant carry the same restrictions — observed, not assumed; if the host claims a process bound, also observe descendant termination on cap); reach each allowlisted loopback target if egress is in scope.
- Intended denials: write/replace oracle, binding, evidence records, checker, and script; `unlink`/`chmod` protected files; egress to a non-allowlisted target; each denial must fail for the intended reason with raw receipts. Include the host's denial/audit-log observation as a receipt — boundary attempts are detected host-side, not by the generated script.
- Recording: run-note evidence rows (precondition, result, spec_version, host_identity, observed_at, command as data, principal, exit_code, artifact hashes) — `unknown` for anything not observed.
- Hard stop: first successful forbidden operation ends the arm; no retry, no cap increase, no oracle relaxation.

## Falsifiability

- If generation proceeds while any input in the table is `UNKNOWN`, this ticket has failed its own gate — the dry run is invalid, not "partially ready".
- If a probe denial succeeds (e.g., oracle is writable under the role), TASK-001 cannot proceed; the finding routes to the host owner, not to an oracle edit.
- If the private-copy dry run touches production state or ambient credentials, the whole run is a containment failure regardless of task outcome.
- If no concrete task root is named, this ticket never becomes executable — drafting it does not discharge the input requirement.

## Bindings status

Resolved on 2026-10-06 (input table above). One input remains `UNKNOWN` by design: host-enforced caps — no budgeted model calls occurred in this dry run, so the envelope was not exercised; it stays a hard prerequisite before TASK-004+. Probe receipts: `/tmp/teaprompt-dryrun/host-task/evidence/` (positive controls, denials incl. descendant-inherited binding denial, oracle-body write under `plans/tests/`, IP-literal egress EPERM, ledger append); records: `run-note.json` + `binding.json`; checker emitted verbatim from the governed-delivery template; gate observed ready/stale/hold → exit 0/4/4. **Declared profile exception:** worker reads are unscoped (`file-read*` — confidentiality not claimed, only write isolation + egress denial; deny-default read aborts `bash` at launch); write exception limited to sibling scratch `/private/tmp/teaprompt-scratch`.

## Acceptance record

Named accepter (user) accepted the dry-run delivery on 2026-10-06 after review of the stage receipts (probes, verbatim checker, gate 0/4/4, oracle green 1439/0/0). Acceptance confirms the contract mechanics exercised — spec → packet → probes → records → preflight → bounded work → oracle → named acceptance. It does not claim model utility, enforcement-proven sealing, or readiness for TASK-004+ (caps envelope still `UNKNOWN`; provider credits and run/cost approval still required).

Post-acceptance (2026-10-06): the user instructed "continue runtime skills" on this accepted dry-run footing. Selected reachable scope: TASK-003 wiring (generated flow ↔ PREFLIGHT ↔ independent verifier) using only already-observed host controls on this copy; the offline-safe refuters GDR-4 and GDR-6 and the GDR-5 release-refusal check against our own gate (all deterministic, no live injection/effect). GDR-3's signature-retry fixture is also offline-safe in scope. GDR-1/GDR-2 carry human gates and stay pending explicit grant; TASK-004+ remains blocked on caps + provider credits.

## TASK-003 + offline refuters — executed on this copy (2026-10-06)

- TASK-003 wiring: `host-task/flow.py` (minimal generated flow) ↔ `checks/run-preflight.sh` (PREFLIGHT) ↔ independent verifier. Coherent records → dispatch → post-gate → exit 0; stale binding, missing PREFLIGHT, non-executable PREFLIGHT → exit 4 before any dispatch (no marker file created). Prompt carried via stdin to sandboxed `bash` — never argv (earlier `bash -c` argv form violated §4 and was fixed before results counted).
- GDR-6 (version bump): spec byte change → flow exits 4, zero dispatch; restore → preflight ready 0.
- GDR-5 (invented record): run-note with fabricated artifact hashes → `stale` exit 4 — coherent invention does not release.
- GDR-4 (packet reconstruction): fresh process reconstructed oracle/spec/required-controls/ownership from packet alone (exit 0); missing `binding.json` → flow hold 4.
- GDR-3 (signature retry): failing task → signature recorded (`fail-signatures.jsonl`); identical retry → exit 3 `refuse-identical-retry` (strategy change, not identical retry); distinct-signature task → proceeds within budget (exit 0). Full criterion exercised. Scope note: the signature is a prompt-identity hash — the spec's fuller "oracle/error-class/touched-surface" signature taxonomy is not implemented; single-signature fixture, not a multi-error taxonomy.
- GDR-1/GDR-2: granted and executed — results below. TASK-004 executed under a provisional per-CLI grant (below); TASK-005+ still need a formal caps envelope and run approval.

## GDR-1/2 + TASK-004 inventory — user-granted 2026-10-06, executed same day

- GDR-1 (oracle integrity, actual role): all five alteration paths denied with byte-verification — direct write, rename-replace, symlink swap, chmod-then-write (mode stayed 644), descendant-process write; mutable positive control succeeded. **TOCTOU grant exercised:** tamper landing during preflight → pre-gate hold (exit 4, no dispatch); tamper landing inside the work window → post-work gate caught it (preflight gate=0 at dispatch, gate=4 at bounded-work-post, flow exit 4, work product existed but never released). The two-gate structure covers the between-gates window.
- GDR-2 (injection, egress-as-sink): worker prompt carrying marked instruction `[INJECTED-MARKER-7f3a]` → IP-literal egress attempt `EPERM` ("Operation not permitted" under sandbox vs connect success unsandboxed); legitimate work-write positive control succeeded. Scope note: no declared sink exists, so this is the narrowest honest reading — injection could not reach *any* egress.
- TASK-004 inventory probe (zero-cost): installed — claude 2.1.290, codex-cli 0.160.1, gemini 0.43.0, cursor-agent 2026.10.01, devin, agy, ollama (`qwen2.5-coder:1.5b` cached), cx 0.7.4.
- TASK-004 executed (user granted ollama-local + provider quota): four receipts under `evidence/task004/` — `ollama qwen2.5-coder:1.5b` → correct minimal fix (`return a + b`, 74 tok in / 17 out, 1.68 s; run unsandboxed — declared exception since the profile denies the loopback egress the daemon needs); `devin swe-2-max` (Free tier per `devin models list`) → correct fix; `cursor-agent` → correct fix (stderr `claude-mem` allowance line is a side-path hook, not the proposal); `agy gemini-3.8-flash` → environment blocker (headless auto-denied a tool "command" permission; no proposal — provider policy, not model failure). Transports: ollama stdin; devin/cursor-agent/agy take the prompt as a CLI argv argument — those are their own prompt flags, distinct from the worker-prompt stdin contract enforced inside `flow.py`. Each: single bounded read-only proposal, no tool/write grants, real usage/result recorded.

## TASK-005 pilot — user-granted 2026-10-06, executed same day

Fixtures (self-contained synthetic, independent of skill content): A-code (broken `add`, arithmetic oracle), B-content (report missing required sections, section+substance oracle), C-hold (stale binding → preflight hold, zero dispatch). Alternated arm order (A: control,treatment; B: treatment,control); fresh contexts; blinded deterministic scorer = oracle scripts run on extracted final candidates.

Result (per-pair, denominator n=2 repair pairs): treatment 2/2 pass; control 1/2 pass (B-control failed oracle — spinner-glyph polluted output dropped `## Next` heading form). C-hold: `stale` exit 4, zero dispatch — scored separately per spec.

**Recorded confounds (honest limits):** treatment arm ran `devin swe-2-max`, control ran `ollama qwen2.5-coder:1.5b` — arms differ in model *and* guidance, so this measures a composite, not isolated skill effect. Scorer was not arm-blinded at extraction time (arm labels visible in file paths). Single run per arm — directional single-case evidence only, per spec §7. Provider invocations ran host-side (profile denies their needed egress — declared exception).

Discarded invocations (not arm results, excluded from the pair denominator): `devin -p -` treated the literal dash as the prompt — malformed invocation, re-run correctly; an earlier `devin` run returned only a tool-rejection warning with no proposal — environment-incomplete, re-run with inlined file content. Both receipts kept in `evidence/task005/` for audit.

## Lens-review defects found post-acceptance (2026-10-06)

- **Worker-writable signature ledger (fixed):** `fail-signatures.jsonl` was inside worker-writable `STATE/` — a sandboxed worker could truncate/forge it, defeating GDR-3's refusal. Relocated to host-owned `host-task/fail-signatures.jsonl`; worker forgery probe now returns EPERM. Skill text updated (flow-control-generator §Contract: decision-bearing ledgers live outside the worker write set).
- **Model never ran inside the sandbox role (declared, unfixed):** all TASK-004/005 provider invocations ran host-side — seatbelt denies the egress they need (even ollama's loopback). Every `met` control was proven for a `bash` worker only; a sandboxed *model* worker has zero evidence. `durable_ledger_storage: met` remains valid (host-side append observed), but containment claims scope to the stub worker.
