# FlashProve Source Survey — Proof-of-Inference Reference (2026-11-04)

Language: English

> **Status: reference documentation adopted (`FP-DOC1`); no Skill, operating-rule or runtime change.** The owner asked to survey `anthropics/FlashProve` and update docs or skills if worth it. The outcome is a source-bound record plus catalogue row; every transferable method it demonstrates is already covered by existing TeaPrompt contracts. No installation, credential use, model weight access, GPU work, commit or push is authorized by this record.

## Research Question and Direct Recommendation

Does FlashProve contain a mechanism worth adopting into TeaPrompt's prompt-library scope?

**No.** FlashProve is a cryptographic research prototype — zero-knowledge proofs that an AI provider's reply came from committed model weights — not a prompt/workflow mechanism. Its genuinely careful evidence-separation discipline (proved theorems vs tested programs vs paper arguments) is already covered by TeaPrompt's existing contracts. Adoption of any part of its runtime would additionally be a Standing Non-Goal (no agent runtime, let alone a ZK prover).

The one artifact worth noting for future reference is its **exhaustive limits registry** — a single table enumerating every known limit, with row IDs that other docs cite. TeaPrompt does not need an equivalent registry today: our limits live in per-record state ledgers and a released-product surface does not exist. If a machine-readable limits table is ever proposed, `docs/limits-all-rows.tsv` is the model.

## Evidence Used and Date Context

Source checked **2026-11-04**:

| Item | Identity | Scope read |
| --- | --- | --- |
| Repository | `anthropics/FlashProve`, HEAD `9e2bdd8ff5bf9c62f18263d7dac189b0400b260c` (`main`), Version 0.16.0, Apache-2.0 | Created and last pushed 2026-10-30; repo description: "A research prototype for zero-knowledge proofs of AI inference. Not maintained." No tags, no releases. ~611 stars at check time. Language: Lean (+ C++/CUDA). |
| README.md, AGENTS.md, SECURITY.md | pinned commit | Full text — routes, agent rules, reporting format, exit-code table |
| guide/what-is-proved.md, guide/known-limits.md, guide/weight-hiding.md, guide/verify-a-proof.md | pinned commit | Substantial sections — theorem/tested/paper argument boundaries |
| verifier/build.sh + verifier/ tree, examples/accepted-proof/ | pinned commit via sparse checkout (19 MB) | Build script read; bounded build attempted (below) |
| Not read in full | SUITE.md (96 KB), PUBLISHED-WORKS.md (295 KB), paper/paper.pdf, prover/, lean/ (~majority of tree) | Limits table and Lean files identified, not audited |

## What It Actually Is — Evidence vs Inference

Verified from source:

- **Claim**: prove which committed model produced a reply, weights hidden. Runs Llama 4 Maverick shape, 1,024-token context, one H100; prover ~110 tok/s prefill at batch 24 (author-reported).
- **Soundness is proved in Lean** for a verifier *written in Lean*: false accept ≤ ~q/2^124 + 2^-101 after q hash queries, random-oracle model, exact-match policy only. The shipped `cp_verify` (C++) and `cp_prove` (CUDA) "follow the same protocol and are tested against it, not themselves proved."
- **The repo's own known-limits doc is unusually honest**: `WITHIN LIMITS` (clipped-gap policy) "does not say the reply is the model's"; printed "bits" are the programs' own accounting, not the theorem's; tests ran partly on "other sources" (test builds), not the released programs; proofs cover only named output positions; the commitment ID must come from a trusted party, never from proof-adjacent files; weight hiding is "expected, not known" — few attacks sought, no test hunts for leaks.
- **Not maintained, not accepting contributions.** Two open issues at check time. A single release-day artifact.

The transferable pattern — **three-tier evidence separation** (machine-proved / tested / argued-on-paper, stated per claim, with the shipped binary explicitly on the weaker tier) — is a strong implementation of a discipline TeaPrompt already mandates: the methodology-vs-operationalization layer caveat ("a spec covering a capability is not the capability"), "self-test or green CI verifies only tested assertions" (Recurring Evaluation Procedure item 3), and exit-code-plus-output reporting (reflective-implement: "read the exit status and the actual output: a log line that says success while the process failed is not a pass").

## Bounded Execution

Sparse checkout at the pin (verifier, accepted-proof example, README); then `verifier/build.sh --clang - <dir>` twice on this host (Darwin arm64, Apple clang 21.0.0, BSD userland). Both attempts exited 2 at `open_above()` — the output-directory containment check — because it invokes GNU `stat -c '%u %a %F'` and `readlink -z`, which BSD userland lacks. **This matches the documented requirement (Linux, g++ 13+, GNU coreutils/findutils), not a defect**: the supported platform check fails closed. No GNU toolchain was installed to work around it; installing packages is out of scope. Nothing was built; no proof was verified locally.

`[INFERENCE]` The same check pattern — refuse output paths any other account can write, walking every path component — is the containment discipline already prescribed by TeaPrompt's external-adoption procedure (probe parent-symlink containment, per-install ownership). No local gap.

## Candidate Adoption Ledger

| ID | Candidate | Disposition | Evidence / reopen trigger |
| --- | --- | --- | --- |
| FP-DOC1 | This source-bound record + catalogue row | Adopted: documentation only | Owner's survey request; prevents re-litigating a release-day research artifact |
| FP-1 | Adopt any FlashProve mechanism (commitment/proof protocol, verifier binary, agent-route packaging) | Rejected | Cryptographic runtime, not a prompt-layer mechanism; operational adoption is a Standing Non-Goal. Reopen only as another record if a named product decision explicitly scopes it |
| FP-2 | Mirror its machine-readable limits registry (`limits-all-rows.tsv`) as a TeaPrompt convention | No change | No released-product surface exists for TeaPrompt to warrant a limits table; per-record state ledgers already carry limits. Reopen if a durable artifact gains enough limits that prose ledgers are demonstrably losing them |
| FP-3 | Borrow its agent-route packaging (route table with hardware/time requirements, "report exit code + full last line" contract) for skill docs | No change | Skills already carry execution contracts and exit/output reporting rules; no consumer failure demonstrated |
| FP-4 | Three-tier evidence vocabulary (proved / tested / argued) as a new glossary rule | No change | `Evidence vs Inference`, `[INFERENCE]` tags and the layer caveat already enforce the distinction; adding a third tier would duplicate, not sharpen |

## Falsifiability

- A concrete local consumer failure against an existing TeaPrompt verification/reporting contract could justify an in-place repair citing this record — external popularity alone cannot.
- A later maintained version, security audit, or independent replication changes freshness, not this pin's findings; re-pin before citing again.
- If a TeaPrompt artifact accumulates enough operational limits that per-record ledgers demonstrably lose them, FP-2 reopens with a named missing-limit incident.
- Unknowns: unaudited Lean tree, prover correctness, real weight-hiding, performance claims, and whether the proof protocol survives the two cited unexamined Fiat–Shamir attacks (ePrint 2025/118, 2026/1838). This survey audits none of those.
