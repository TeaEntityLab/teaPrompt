# Craft Anything Source Survey — Acceptance and Evidence Boundaries (2026-11-10)

Language: English

> **Status: reference documentation adopted (`CFT-DOC1/2`); no Skill, operating-rule or runtime change.** The owner asked to update Docs or Skills where the 2026-11-10 `storytold/craft-anything` survey supports it. The transferable distinctions are already required by existing TeaPrompt contracts. This record preserves the pins, the bounded CLI receipt, and one worked reference. It does not install the engine, register an MCP server, call a model, or authorize a rebuild.

## Research Question and Direct Recommendation

Which mechanisms in Craft Anything are worth borrowing, and do they expose a TeaPrompt Docs or Skill gap?

**Record the boundaries; do not adopt the runtime or add a Skill.** The useful mechanisms are a typed evidence record, first-class unknown questions, staged rebuild state, and a host-checked tool gate. They do not establish that any program can be reconstructed, that a terminal `Ready` status is acceptance, or that a content hash authenticates its producer. No local consumer defect was reproduced against an existing TeaPrompt contract.

## Evidence Used and Date Context

Checked **2026-11-10**. `main` was read and not executed. The release CLI was executed only inside a disposable host sandbox.

| Item | Identity | What this check covers |
| --- | --- | --- |
| `main` source | `30e916536a8adf9fad47602c2a8bcf26bcfa930b` | Code and docs cited below. Not compiled and not run. |
| Release | tag `v0.6.0`, commit `899b4ebd24ca17d4a84af1e1b9ef9c0304de08ab`, published 2026-11-09 | Separate from `main`. Not treated as the same tree. |
| Workspace metadata on `main` | `Cargo.toml` version `0.4.0`, `rust-version` `1.97` | Source package metadata only. It does not identify the executed binary. |
| Executed CLI | `craft-anything-cli-0.6.0-macos-universal.zip` | `--version` printed `craft-anything-cli 0.6.0`. |
| Maturity | upstream README status badge and Status section say **early alpha** | A public release is not production-readiness evidence. |

Download ZIP SHA-256: `29661218b0c293308b4ffbe1623628f2d22ad4074dabeb414dbc8c7f25dcb2a5`, matched to the GitHub release asset digest. Unpacked CLI SHA-256: `e09a40d1939d9a3fca9c4e46d0dd79d3aecd2f840a0ced49d8e13e043e0f5df3`. Those digests identify the downloaded bytes. They are not a reproducible-build attestation or a signature audit.

Permalinks below use the `main` pin: `https://github.com/storytold/craft-anything/blob/30e916536a8adf9fad47602c2a8bcf26bcfa930b/`.

## What Was Executed

The release CLI ran with a temporary `HOME` and config, `CRAFT_ANYTHING_NO_KEYCHAIN=1`, and an external `sandbox-exec` profile that allowed scratch read/write and denied outside-scratch read/write plus socket connect. No MCP registration, engine install, builder, model call, GUI, or upstream test suite.

The first sandbox profile aborted even `/bin/echo` with signal 6 because it could not read the literal path `/`. That was a harness failure, not a product failure and not a passed isolation control. After that profile correction, six host controls passed: launch, scratch read, scratch write, and denial of outside read, outside write, and socket connect. The network control was `nc` to `127.0.0.1:9`, exit 1. Those controls belong to this survey's host profile, not to Craft Anything.

Eleven CLI scenarios then matched their asserted expectations. Refusal scenarios are defined to exit 1:

| Scenario | Exit | Observed boundary |
| --- | --- | --- |
| Clean-room inspection of a fixture `add.wasm` | 1 | `feature_missing`, reason `clean_room` |
| Deep inspection of the same file | 0 | Listed `add` and `(i32, i32) -> (i32)` with the input hash, and retained a `static_only` limitation |
| Evidence export, then import | 0 | One record survived a separate CLI invocation |
| Import after changing `result` but keeping the id | 1 | `evidence_hash_mismatch` |
| Import after changing only the display summary | 0 | Accepted, matching the hash exclusion |
| Import after changing `result` and recomputing the canonical id | 0 | Accepted. The id is not a source signature |
| Unknown add, update, stale update, and reread | 0, 0, 1, 0 | Revision moved 1 to 2; the stale revision was rejected; the stored row stayed revision 2 |

`commands` returned 322 tool objects. An independent count of `"tool"` fields in that output was also 322. On the unread-as-executed `main` tree, `docs/tools.md` has 302 unique engine entries and its section counts sum to 302. The README's "300 in the engine" sentence is a third population. The three counts are not an availability rate and are not one revision.

## Optional Worked Reference: Acceptance Is Narrower Than a Terminal Status

**[INFERENCE] only where marked. This is an application of existing TeaPrompt contracts to one pinned engine, not a new rule and not an end-to-end rebuild.**

| Boundary | What the pinned source does | Do not import |
| --- | --- | --- |
| Terminal status versus acceptance | After the refinement cap, status becomes `Ready` when the last stored check's `passed` field is true. The adjacent comment says a site that builds but is not close enough is still usable. `CheckResult::good()` is stricter: `passed`, no unknowns, every claim passed, and any stored similarity at or above its bar. The Ready summary can still say that only some checks or claims hold. | Do not copy `Ready` as acceptance. Execution success is already not business acceptance. |
| Self-report versus an independent oracle | The game checker launches the artifact with `--self-test` and reads JSON. The required steps are `move`, `act`, and `hud`, and each `passed` boolean is the program's own report. A non-blank screenshot check is also stored as `passed: true` once pixels exist; likeness is a separate field. | A builder-written report is not an observation of play, hits, or HUD behavior. Self-assessment stays the weakest evidence tier. |
| Changed acceptance setting versus reused result | The kept-check key hashes the app fingerprint, reference and capture metadata, project root, target kind, stack, `clean_room`, and plugin ids. It does not hash `picture_good_enough`. The screenshot checker stores a similarity score only when that bar is set. | **[INFERENCE, not reproduced]** Changing only that bar can reuse an older result whose score was never stored, so the new bar has nothing to compare. Reproduce with one fixture and no model before treating it as an upstream defect. |
| Content checksum versus authenticity | The evidence id is SHA-256 of the canonical JSON after removing `summary`, `subject.name`, and `carries_target_content`. The CLI accepted a summary-only edit and a recomputed id, and rejected a changed result that kept the old id. | A matching id shows those covered fields still match. It does not identify the producer or prove the log is complete. |

Sources for the four rows, all at the `main` pin:

- Ready versus `good()`: [`crates/engine/src/workspace.rs`](https://github.com/storytold/craft-anything/blob/30e916536a8adf9fad47602c2a8bcf26bcfa930b/crates/engine/src/workspace.rs#L320-L326), [`crates/ai/src/rebuild/mod.rs`](https://github.com/storytold/craft-anything/blob/30e916536a8adf9fad47602c2a8bcf26bcfa930b/crates/ai/src/rebuild/mod.rs#L1066-L1084), [`crates/ai/src/rebuild/self_check.rs`](https://github.com/storytold/craft-anything/blob/30e916536a8adf9fad47602c2a8bcf26bcfa930b/crates/ai/src/rebuild/self_check.rs#L76-L85).
- Self-test and screenshot `passed`: [`crates/ai/src/rebuild/kinds/self_test.rs`](https://github.com/storytold/craft-anything/blob/30e916536a8adf9fad47602c2a8bcf26bcfa930b/crates/ai/src/rebuild/kinds/self_test.rs#L15-L41), [`crates/ai/src/rebuild/kinds/screenshot.rs`](https://github.com/storytold/craft-anything/blob/30e916536a8adf9fad47602c2a8bcf26bcfa930b/crates/ai/src/rebuild/kinds/screenshot.rs#L90-L109).
- Cache inputs: [`crates/ai/src/rebuild/kept_check.rs`](https://github.com/storytold/craft-anything/blob/30e916536a8adf9fad47602c2a8bcf26bcfa930b/crates/ai/src/rebuild/kept_check.rs#L48-L56), [`crates/engine/src/workspace/progress.rs`](https://github.com/storytold/craft-anything/blob/30e916536a8adf9fad47602c2a8bcf26bcfa930b/crates/engine/src/workspace/progress.rs#L164-L177).
- Evidence id: [`crates/evidence/src/lib.rs`](https://github.com/storytold/craft-anything/blob/30e916536a8adf9fad47602c2a8bcf26bcfa930b/crates/evidence/src/lib.rs#L204-L249).

Clean room is the same class of boundary. Dispatch refuses a tool id before consent when the session is in clean-room mode ([`crates/engine/src/lib.rs`](https://github.com/storytold/craft-anything/blob/30e916536a8adf9fad47602c2a8bcf26bcfa930b/crates/engine/src/lib.rs#L257-L258)). That is an application policy. It is not an OS sandbox, a legal clearance to rebuild someone else's program, or the same isolation as a WASM plugin with an empty linker. The executed clean-room refusal shows the policy exists. It does not certify the builder shell.

## Existing Coverage and Candidate Adoption Ledger

| Concept | Checked delivered surface | Result |
| --- | --- | --- |
| Execution success is not acceptance | [Runtime Trust Boundary](../04-agent/runtime-trust-boundary.md) §2a, rule "Execution Success ≠ Business Acceptance" | Already required. The worked reference shows an external `Ready` status that is intentionally weaker than its own `good()`. |
| Self-assessment is the weakest tier | [Reflective Review](../skills/reflective-review/SKILL.md), Evidence Tiers | Already required. No Skill sentence added. |
| Iteration cap is not success | [Flow Loop Harness](../skills/flow-loop-harness/SKILL.md) | Already requires an external verifier. The loop contract is unchanged. |
| Stale acceptance settings must be rerun | [SOP Compiler](../04-agent/sop-compiler.md) §7; [Context Handoff](../03-context/context-handoff.md) | The duty already exists. The cache-key candidate stays an inference until reproduced. |
| Hash scope is not authority | [Runtime Trust Boundary](../04-agent/runtime-trust-boundary.md) §3–4a | Already separates tool output from commands and host enforcement from prompt text. |
| External engine, GUI, MCP, or checker runtime | [Project Knowledge](../PROJECT_KNOWLEDGE.md) Standing Non-Goals; [External Adoption Review](../04-agent/external-adoption-review.md) | Operationalization, not a missing prompt-layer method. |

### Candidate Adoption Ledger

| ID | Candidate | Disposition | Evidence / reopen trigger |
| --- | --- | --- | --- |
| CFT-DOC1 | This source-bound record and its catalogue row | Adopted: documentation only | Owner asked to update Docs where possible. Refresh when the pin, release, or cited control changes. |
| CFT-DOC2 | Optional reference link from the existing runtime trust boundary, outside the prompt fence | Adopted: navigation only | Makes the four boundaries discoverable without changing the prompt's output contract. |
| CFT-SK1 | New Skill, or an edit to an existing Skill contract | No change | No verified local structural gap. External presence is not local recurrence. Reopen on a reproduced consumer defect. |
| CFT-RUN1 | Install, register, or route work through Craft Anything | Not adopted | Standing Non-Goal for a TeaPrompt runtime. Needs a separate host, purpose, and acceptance record. |
| CFT-RULE1 | Copy `Ready`, self-test JSON, or an excluded-field checksum as a TeaPrompt acceptance rule | Rejected | Each one is weaker than the contract already in force. |

Missing local usage data remains `unknown`, not zero demand.

## Falsifiability

- A reproduced local failure of an existing acceptance, evidence-tier, invalidation, or hash-scope contract can justify an in-place repair. This survey does not.
- Reproducing the likeness-bar reuse with one unchanged fixture and one changed `picture_good_enough`, without a model call, would promote that row from inference to an observed upstream defect. It still would not by itself authorize a Skill edit.
- A later commit, release, or adapter live-test changes freshness only after the new identity is pinned. `v0.6.0` and `main` `30e9165` stay distinct until a diff says otherwise.
- Unknown here: rebuild quality, real-account builder behavior, malicious plugin isolation, parent-symlink and concurrent-write behavior of setup, full rollback, cost, and whether particular assets may legally be rebuilt. Upstream names the project MIT OR Apache-2.0; bundled engines, model services, assets, and brands have separate conditions ([`docs/licences.md`](https://github.com/storytold/craft-anything/blob/30e916536a8adf9fad47602c2a8bcf26bcfa930b/docs/licences.md#L3-L32)).
