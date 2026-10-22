# Agentic SOP Workflow Reflection

Date: 2026-06-13

## Research Question

Should TeaPrompt adjust after reviewing `agentic-sop-to-work`, or is the current prompt-and-skill library already sufficient?

## Direct Recommendation

Make a small conceptual adjustment. Do not import a full deterministic runner, Claude Code plugin surface, or new core skill yet.

TeaPrompt already has the right direction: compact skills, Why / What / How / Done gates, runtime trust boundaries, workflow-engine prompts, and quality gates. The missing concept is sharper: a repeatable human process can be treated as source material for a `SOP compiler` that decides whether to remain a prompt, become an artifact, become a skill, or eventually become a code-backed workflow kit.

## Evidence Ledger

| Claim / Item | Source | Status | Open Constraint |
| --- | --- | --- | --- |
| `agentic-sop-to-work` presents itself as turning human SOPs into deterministic, gated, human-approved agentic workflows. | https://github.com/s0912758806p/agentic-sop-to-work | verified | GitHub README is the upstream project surface, not independent validation of runtime quality. |
| Its workflow shape is Human SOP -> single-tool skills -> orchestrated flow -> per-step gates -> DRAFT -> human approval, guarded by Stop-hook regression. | https://github.com/s0912758806p/agentic-sop-to-work | verified | This is the repo's stated architecture. |
| The kit uses hard gates such as command, schema, trace, and recompute gates, with deterministic control flow in code rather than model-selected free loops. | https://github.com/s0912758806p/agentic-sop-to-work and kit/SOP.md | verified | We did not run the external project locally. |
| v1.5.4 added smart intake and capped auto-fix loop behavior. | https://raw.githubusercontent.com/s0912758806p/agentic-sop-to-work/main/CHANGELOG.md | verified | Changelog is upstream-maintained but still not execution evidence. |
| TeaPrompt already contains workflow engine planning, Why / What / How / Done gates, runtime trust boundaries, benchmark tasks, and eight compact workflow skills. | Local repo files under `reflective-prompt-library/` | verified | Current implementation is mostly prompt/artifact-level, not a runner. |
| Threads post was provided as context. | https://www.threads.com/@wgi327119/post/DZc2gTUlHu4 | unverified | Current retrieval did not expose usable content, so it should not carry load-bearing evidence. |

## Project Fit

TeaPrompt should not become an `agentic-sop-to-work` clone. The current repo is a portable reflective prompt and skill library, not a Claude Code plugin runtime. Importing runner code, hooks, and plugin commands now would change the project class and raise maintenance cost before there is enough local evidence.

TeaPrompt should learn the abstraction:

```text
Human know-how
-> SOP
-> Skill or workflow stage
-> Artifact contract
-> Gate
-> Human approval boundary
-> Optional verifier / runner / hook
```

This belongs in `04-agent/` as source material and in `reflective-spec-plan` as a planning lens.

## Socratic Critique

1. Are we trying to make the model smarter, or make the workflow less dependent on model judgment?
2. Which part of the process is actually repeated enough to justify formalization?
3. Which checks can be moved out of model self-review and into deterministic validation?
4. If a human approves the wrong SOP, which downstream gate would catch it? If none, where must the human review boundary move?
5. Are we optimizing single-run token cost, or total cost across repeated runs, corrections, audits, and handoffs?
6. What artifact would let another run resume without rereading the whole conversation?
7. What is the smallest useful level: prompt-only, SOP artifact, skill + artifact contract, verifier, or full runner?
8. What would become worse if TeaPrompt adopted a full plugin/runtime now?

## Critical Findings

### 1. The external project solves a narrower and harder problem than generic loop engineering.

It is best described as a Human SOP compiler for agentic workflows. The important move is not adding stages or loops. It is moving responsibility into artifacts, deterministic gates, and human approval boundaries.

### 2. TeaPrompt already covers the reasoning layer but under-specifies the compiler layer.

`workflow-engine.md` asks for steps, state, gates, recovery, and human review. It does not make SOP intake classification, typed artifact contracts, deterministic-vs-model-drafted fields, or promotion levels explicit enough.

### 3. Pure text skills are not enough for high-risk repeatable workflows.

For low-risk tasks, TeaPrompt's current skill layer is sufficient. For high-risk or repeatedly executed workflows, a text skill can describe discipline but cannot enforce schema, trace, recomputation, command success, fix-loop caps, or regression hooks.

### 4. A full runner would be premature.

TeaPrompt currently lacks enough repeated workflow cases showing that users need local runnable orchestration. Adding a runtime now would increase surface area, testing burden, and installation complexity.

## Decision

Adopt the SOP compiler concept at the prompt/spec layer now.

Reject for now:

- A ninth core workflow skill.
- A copied Claude Code plugin structure.
- A bundled runner, hook, or command system.
- Mandatory single-tool decomposition for all workflows.
- Treating token minimization as the primary objective.

Add now:

- `04-agent/sop-compiler.md`
- `reflective-spec-plan` prompt-source linkage.
- README and methodology documentation.
- A benchmark task for SOP compiler routing.

## Future Promotion Gate

Consider a code-backed workflow kit only if at least three real TeaPrompt workflows meet all criteria:

- repeated at least five times,
- objective artifact schema exists,
- at least two deterministic gates are obvious,
- conversation-only execution caused repeated drift or rework,
- human approval boundaries are stable,
- a small verifier would reduce total review cost.

Until then, keep this as source material.

## Implementation Plan

1. Add SOP Compiler prompt under `04-agent/`.
2. Update `reflective-spec-plan` to treat SOP compiler design as a planning lens.
3. Update README, methodology map, and skill map.
4. Add one benchmark case.
5. Regenerate index and run validation.

## Residual Risks

- The external project may be better or worse in practice than its README suggests; this reflection did not execute it.
- The SOP compiler concept can over-formalize low-risk creative or exploratory work.
- Typed artifact contracts can become bureaucracy unless tied to actual reuse, audit, or failure reduction.

## Latest-version refresh — 2026-10-22

Scope: latest default-branch and release/tag identities for `s0912758806p/agentic-sop-to-work`. Source/ref inspection only; no builds, tests, smokes, installs, commits, or adoption changes. The 2026-06-13 decision (adopt the SOP-compiler concept at the prompt/spec layer; reject a copied runner/plugin surface) and the future-promotion gate stand.

| Identity | Observation |
| --- | --- |
| Prior baseline in this record | v1.5.4 era (smart intake + capped auto-fix loop), unpinned commit, via README/CHANGELOG reads 2026-06-13 |
| Latest tag (core kit) | `v1.9.0` → tag object `6a3707ec2b3e3566d00b63304f68f7b3c242b10d` → commit `248a01f580553e2b4c2b2f43b589a463222bfe05` (2026-06-23); ancestor of `main`; published [release](https://github.com/s0912758806p/agentic-sop-to-work/releases/tag/v1.9.0) |
| Latest checked `main` | `246d96638305722306160b4be0fc0cfd368d13e0` (2026-09-08, "Merge pull request #9 ... feat/graph-engineering") via `git ls-remote` |
| Version split | CHANGELOG on `main` already documents **[1.10.0] — 2026-09-08** (Graph Engineering), but **no `v1.10.0` tag or release exists** (`git ls-remote` tag query empty; releases feed newest core entry is v1.9.0). So: latest tag v1.9.0; latest documented version 1.10.0; latest code `main` @ `246d966`. License MIT, unchanged |
| Delta since v1.5.4 | 189 files (+9105/−187) across `main` = v1.5.4 → v1.9.0 → main |

Change families since the baseline (changelog + release notes + diff stats; no execution in this refresh): (a) **Loop Engineering triad** (v1.6.0–v1.8.0, released in v1.9.0): stall detection (deterministic idle/thrash early-stop + re-run refusal), runtime health monitoring (coverage-shrink hard gate via `verify.py` exit 3, slowdown/flaky advisory), bounded run-state (`verify.py` log rotation, human-authorized `run.py --prune`); (b) **six-rung-ladder decision skill** (v1.9.0, docs-only: decide → build → audit trio); (c) **three new companion plugins** with their own tags/releases: `second-opinion-honesty` v0.1.0/v0.2.0 (domain-neutral honesty reviewer + opt-in enforced acknowledgement Stop-hook gate), `alcoa-guard` v0.1.0 (deterministic ALCOA+ data-integrity linter; enforcing Stop-hook deferred), `plugin-forge` v0.1.0 (plugin linter + scaffolder; `lint --all --strict` replaces `validate_manifests.py` in CI); (d) **Graph Engineering** (main-only, documented 1.10.0, untagged): bounded-graph composition of loops — typed handoff edges (`schema_ref` now actually validated), static topology validation (`graph.analyze()` single authority, runtime enforces what `--plan` reports), bounded back-edges (replacing the forward-only prohibition), state-as-declaration (`reads`/`writes`, one writer per field), `residual_gate` (scans own output for the unfilled-gap marker), `run.py --graph` Mermaid rendering, demo graph + three demo skills, first docs-freshness test. One breaking change: illegal topologies (in practice: unreachable steps) now refuse to run instead of warning. The stdlib-only invariant stays machine-enforced; opt-in rule: flows declaring no graph features produce byte-identical artifacts to v1.9.0.

Effect on prior findings: the external project moved substantially further in exactly the direction this record described (deterministic gates, bounded loops, human approval boundaries) — three companion plugins plus a graph tier — while staying a Claude Code plugin/kit surface, not a TeaPrompt dependency. The "full runner premature" rejection and the six-criterion promotion gate are unaffected: no local recurrence evidence was gathered here. Inspected immutable links: [v1.9.0 release](https://github.com/s0912758806p/agentic-sop-to-work/releases/tag/v1.9.0), [main commit](https://github.com/s0912758806p/agentic-sop-to-work/commit/246d96638305722306160b4be0fc0cfd368d13e0), [CHANGELOG @ main](https://github.com/s0912758806p/agentic-sop-to-work/blob/246d96638305722306160b4be0fc0cfd368d13e0/CHANGELOG.md), [releases feed](https://github.com/s0912758806p/agentic-sop-to-work/releases) (checked 2026-10-22; GitHub API releases endpoint returned 403, feed used instead). Untested: all runtime behavior; gate/determinism claims are author-reported plus source-read.
