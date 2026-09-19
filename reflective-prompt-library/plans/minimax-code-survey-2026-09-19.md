# MiniMax Code Survey — `MiniMax-AI/minimax-code` (2026-09-19)

> **Status: decided — one sentence adopted in a same-day follow-up under user direction (MC-5; Adoption Addendum); otherwise record-only.** The object is an open-source terminal coding agent (TypeScript, MIT default for first-party code, 779 stars; repo created 2026-06-01; HEAD `e3724a13d72d`, 2026-09-18) published as the **reviewed public projection of an internal monorepo**: a machine-readable file inventory is the publication boundary, upstream changes arrive by a three-way merge whose candidates are quarantined as unreviewed internal material, and the release audit publishes its own gaps — including a root-license attribution error caught after the audit and a currently-red typecheck gate. The harness is built on a vendored Pi-lineage agent core (`third_party/pi-mono`) — shared ancestry with the host harness TeaPrompt sessions run on. Its repo ships five co-located agent skills whose rules converge, independently, on TeaPrompt's own: evidence-backed retro lessons with a recurrence gate and an explicit "a retrospective is not authorization", paired old/new token sweeps with a don't-touch-unrelated-matches rule, and a tri-state consumer map with a "never declare complete while a consumer is `unknown`" bar. Ten concepts mapped: nine covered by installed rules or host-territory non-goals; the tri-state consumer map is deferred with an observed-failure trigger. Clean-room throughout.

## Research Question

User instruction: "Survey this https://github.com/MiniMax-AI/minimax-code". Two questions: (1) what the artifact is and what its governance actually does; (2) does any concept expose a verified gap on an installed TeaPrompt surface. A bare "survey" carries no adoption direction; the standing bar applied per candidate.

## Direct Recommendation (as of 2026-09-19)

- **Study: yes — two surfaces.** (a) The public-projection release governance: `release/public-source.json` as the explicit inventory, `release/extraction.json` pinning the source baseline, three-way sync with candidate quarantine, and audits that record their own misses (the root-license follow-up; the visa-PDF provenance case resolved by a history-free snapshot). (b) The five repo-local skills, which are the closest thing yet surveyed to TeaPrompt's own genre — natural-language operating rules for agents working a specific repo, with evidence bars and authority limits.
- **Reproduce: not undertaken.** Nothing executed; no clone; no install. All claims are author-authored repo documents read at the pinned HEAD.
- **Adopt: one sentence, in a same-day follow-up under user direction (MC-5; Adoption Addendum).** The runtime, release pipeline, and CI gates are host territory (P7: TeaPrompt owns no runtime). The epistemic rules its skills encode are already installed — several are point-for-point convergent. The one form sharper than anything installed, the tri-state consumer map, landed as one additive Verification bullet on `reflective-implement`.
- **Deploy: not applicable to TeaPrompt.**
- **For citers:** first-party default license is MIT, but the tree is license-heterogeneous by design (32 package roots: 27 Apache-2.0, 5 MIT per the audit; vendored Pi and sandbox forks keep their own licenses); the audit's own follow-up documents that the root LICENSE was, at extraction, byte-identical to the sandbox fork's file — attribution history matters when reusing this code.

## Method

Coordinator reads (2026-09-19), no scouts, no panel: repository metadata and HEAD pin via the GitHub API; `README.md` (main body); `docs/architecture.md`; `AGENTS.md`; `docs/source-sync.md`; `docs/release-audit.md`; `docs/publication-authorization.md`; `docs/verification.md` (as a converted table); all five `.agents/skills/*/SKILL.md` files. Listed but not read: `docs/telemetry.md`, `docs/open-source-status.md`, `LICENSE-STATUS.md`, `docs/releasing.md`, `docs/maintainers.md`, installation/examples/demo docs, `README_ZH.md`, and the source itself (~4,800 files; only the architecture doc's account of it). Coverage checked by grep against installed TeaPrompt surfaces.

**Scope / acceptance:** identify the artifact and its governance from its own documents; map the concept set against installed surfaces; decide every candidate with evidence and a trigger; land nothing without a verified gap; keep the clean-room boundary; run `make all` from the repository root.

## What the Artifact Is

A terminal coding agent ("MCode": interactive TUI, headless exec, and an editor-protocol adapter) over MiniMax accounts or bring-your-own OpenAI/Anthropic-format providers, with sandboxing, permissions, plugins, MCP, subagents, sessions, and plan/permission modes. Architecture: `TUI / exec / ACP → CliService → local applications → session/turn/agent services → model providers and tools`, with the agent core vendored from a Pi-lineage mono-repo and a forked sandbox runtime; private `@mavis/*` workspace names resolve from source, not a registry.

The governance is the distinctive part:

- **Publication boundary as data.** Every published file is listed in `release/public-source.json`; `check:source` verifies inventory, canonical license text, internal addresses, retired modules, credentials patterns, and workspace exports; `check:standalone` separately verifies the actual build graph. The docs state the rule twice: adding a path to the inventory "does not make it suitable for publication" — listing is not approval.
- **Three-way sync with quarantine.** The internal repo is never a mergeable upstream; a tool reads Git objects only and emits merge candidates into a private review directory that must sit outside both repos; candidates are "unreviewed internal material" never uploaded or bulk-copied; approved files are applied individually; the recorded baseline advances only after all differences are reviewed; no internal authors, messages, or history are carried.
- **Single sources of truth.** A declared-in/consumed-by table (package scope, export maps, per-gate test registries, retired paths, the verification pipeline, docs-only classification) with generated files regenerated, never hand-edited, and a ban on duplicate hard-coded lists.
- **Audits that publish their own misses.** The release audit records: secret-scan false positives excluded only by exact file and matched value; a PDF-skill fixture whose synthetic provenance could not be established, resolved by rewriting to explicitly synthetic data and importing a history-free snapshot; live-service acceptance rows each bounded ("a request that only returned a known official URL was not counted as tool acceptance"; "54 available plugins… does not claim all plugins were installed or tested"); an explicit not-run list; and a dated follow-up admitting the root LICENSE was byte-identical to the sandbox fork's Anthropic-copyright file since the first extraction commit, with the corrected file hash-pinned. `docs/verification.md` currently publishes a red gate (a typecheck FAIL against installed Undici 8, "NOT RUN: the full verifier stopped at typecheck").
- **Five co-located agent skills.** A CLI architecture guide (entry-point map; "trace callers before assuming a fix to one adapter covers the others"; "help output alone is insufficient"); a testing workflow (declared suite registry; per-scope gate table; PASS/FAIL/BLOCKED with "local macOS success does not establish Windows/Linux or live-service acceptance"); a cross-layer drift sweep (change-axis gap table; paired old/new token searches; assert at the final observable layer; "avoid changing unrelated matches merely because they contain the same token"; explain deliberate compatibility remnants); a runtime-sinks verifier (enumerate consumers, mark each `covered` / `not applicable` / `unknown`; "do not declare complete runtime coverage while a relevant consumer is `unknown`"); and a retro skill (Event/Cause/Lesson/Impact evidence rows; "do not turn one-off preferences into repository-wide rules"; a right-home routing table; "prefer correcting an existing instruction over introducing a parallel process"; "do not treat the retrospective as authorization to create issues, send messages, publish changes or modify personal/agent memory").

## Concept Map

Tier is `docs` throughout (author-authored repo documents at the pinned HEAD; nothing executed).

| ID | Concept (clean-room) | TeaPrompt coverage | Disposition |
| --- | --- | --- | --- |
| C1 | Publication boundary as machine-readable inventory; listing is not approval | `04-agent/artifact-promotion.md` §4: promotion needs evidence gates, not registry entry; `governed-delivery` acceptance records | No change — release pipeline is host territory; the rule exists |
| C2 | Unreviewed-candidate quarantine; per-file apply; baseline advances only after full review | `agent-governance-scaffold` proposal/authorization/effect separation | No change — an instance of the installed split |
| C3 | Single-source-of-truth registry with declared-in/consumed-by, regenerate-don't-edit, no duplicate lists | TeaPrompt practice (generated `index.json`; guards as consumers; TODO-catalog drift rules in the harness lineage) | No change — repo-engineering, host-side |
| C4 | Evidence-bounded acceptance: per-row claim limits, PASS/FAIL/BLOCKED, platform-scoped conclusions, current red gates published | `reflective-review` evidence rules; verification-claims-bounded lesson; `OUTCOME_UNKNOWN`; status-banner honesty | No change — installed; convergence noted |
| C5 | Tri-state consumer map before completion: enumerate affected consumers, mark `covered` / `not applicable` / `unknown`, never declare complete while `unknown` remains | `reflective-implement` verification contract and the landing-review bullet cover the substance; no installed sentence requires *enumerating* consumer classes with a tri-state before "done" | **Adopted same day (MC-5)** |
| C6 | Paired old/new token sweep; change-axis gap table; assert at the final observable layer; don't touch unrelated same-token matches | Lived precedent: the fix-loop decoy case (a filter swallowing `run-1/`), the landed-bytes review rule, drift guards | No change — installed by rule and by scar |
| C7 | Retro authority limits: evidence rows, recurrence gate, right-home routing, no parallel process, retro ≠ authorization, memory writes only on explicit ask | `reflective-handoff-retro`; `artifact-promotion.md` §4 memory-write gate; the 2026-09-16 authority-boundary lesson; second-convention prohibition | No change — independent convergence, recorded as corroboration |
| C8 | Repo ships co-located agent skills that cross-reference each other and the harness policy | TeaPrompt's own genre (`skills/` + `06-repo/AGENTS.md`); managed-skill ecosystem | No change |
| C9 | Adapter-coverage tracing: shared implementation is evidence only after tracing how each adapter reaches it | `reflective-review` coverage questions; harness-side references discipline | No change |
| C10 | Vendored-lineage transparency: upstream forks keep licenses, revisions, and modification records; attribution errors corrected with hash pins and documented | `reflective-research` External Adoption Checks (pin identities, record divergence separately); the license-heterogeneity caution is a citer fact | No change — recorded |

## Candidate Adoption Ledger

| ID | Candidate | Status | Evidence | Next action / trigger |
| --- | --- | --- | --- | --- |
| MC-1 | "Listing is not approval" sentence for TeaPrompt surfaces | No change 2026-09-19 | C1 row: §4 promotion gates already require evidence beyond registry entry; TeaPrompt has no publication inventory to govern | Reopen only if TeaPrompt ever ships an inventory-gated surface |
| MC-2 | Candidate-quarantine rule | No change 2026-09-19 | C2 row: proposal/effect separation is the scaffold's core; the quarantine is its release-pipeline instance | None |
| MC-3 | Declared-in/consumed-by registry table as a documented form | No change 2026-09-19 | C3 row: practiced (generated index, guard consumers); a form template would be host repo-engineering advice, outside the nine-skill scope | None |
| MC-4 | Evidence-bounding sentences from the audit ("X returned does not claim Y tested") | No change 2026-09-19 | C4 row: installed rules state the general form; the audit is a good specimen, not a missing rule | None |
| MC-5 | Tri-state consumer map: before declaring an implementation complete, enumerate affected consumer classes and mark each `covered` / `not applicable` / `unknown`; `unknown` blocks completion | Adopted 2026-09-19 (same-day user direction) | Gap re-verified by full read before landing: the State Ledger and Sufficiency Gate govern *listed* items and the Twin sweep enumerates twin defects, but no installed sentence forces enumerating the consumers of a changed contract — a consumer never enumerated never becomes a ledger row, so the gate passes with coverage silently missing. Landed as one additive single-line Verification bullet on `reflective-implement` (after the Twin sweep, its structural sibling), pinned once by the guard; the record-name citation is omitted on the surface per the clean-room precedent | Retire if the bullet leaves `reflective-implement`; the adoption is wrong if the enumeration duty catches nothing the landing reviews would have missed across the next several implementation records |
| MC-6 | Don't-touch-unrelated-same-token-matches sentence | No change 2026-09-19 | C6 row: the decoy-filter scar and the tight-ranges edit discipline already encode it | None |
| MC-7 | Retro-authority convergence | Noted 2026-09-19 (record-only) | Their retro skill independently derives the §4 memory-write gate, the recurrence bar, and the no-parallel-process rule — third-party corroboration of installed governance, from a production harness's own repo | None |
| MC-8 | Co-located-skills pattern | No change 2026-09-19 | C8 row: TeaPrompt is the pattern | None |
| MC-9 | Adapter-tracing sentence | No change 2026-09-19 | C9 row: covered | None |
| MC-10 | Lineage note: the surveyed harness vendors a Pi-lineage agent core — shared ancestry with the host harness TeaPrompt sessions run on | Noted 2026-09-19 (record-only) | Architecture doc names the vendored mono-repo and sandbox fork; the release audit records their licenses, upstream revisions, and modification records | None — host-lineage fact, dated |

Deterministic guard: `plans/tests/test_minimax_code_survey_record.py` (identity, dispositions, MC-5 trigger, clean-room boundary, index links).

## Shared Findings

1. **Independent convergence on TeaPrompt's governance rules, from a production vendor's own repo.** The retro skill's authority limits ("not authorization to… modify personal/agent memory"; explicit-ask memory writes), the recurrence gate, and the prefer-correct-existing-over-parallel-process rule are the §4 memory-write gate, the promotion bar, and the second-convention prohibition — none of which they could have taken from TeaPrompt. Convergent evolution is the strongest external corroboration an installed rule can get short of a measured failure.
2. **The audit genre done with its own errata.** The release audit publishes false-positive scoping (exclusions by exact file and matched value, "not entire test or skill directories"), an unresolvable-provenance fixture handled by rewriting to synthetic data plus a history-free import, and a dated follow-up in which the root LICENSE itself failed attribution review after the audit passed. Publishing the correction with byte hashes is the landed-bytes review rule applied to a legal surface.
3. **"Listing is not approval," stated twice, is the inventory-governance rule TeaPrompt's promotion gates state for skills.** Their boundary is a JSON inventory; TeaPrompt's is a skill registry; both refuse to let registration substitute for review.
4. **The tri-state consumer map is the one form worth watching (MC-5).** "Do not declare complete runtime coverage while a relevant consumer is `unknown`" forces the unknown into the report. TeaPrompt's texts demand bounded verification claims but do not force enumeration; the deferral trigger names the failure that would justify the addition.
5. **A currently-red gate is published as status.** `docs/verification.md` leads with a FAIL (a type error against a newer installed dependency) and "NOT RUN: the full verifier stopped at typecheck" — current-status honesty over release-page polish, the same rule as TeaPrompt's status banners and the QUALITY_GATES floor guard.

## Evidence vs Inference

| Claim | Status | Basis |
| --- | --- | --- |
| Identity: created 2026-06-01, HEAD `e3724a13d72d` (2026-09-18), MIT default, TypeScript, 779 stars | Observed | GitHub API, accessed 2026-09-19 |
| Architecture, execution path, vendored Pi-lineage core and sandbox fork, `@mavis/*` resolution | Observed (docs) | `docs/architecture.md`, read 2026-09-19 |
| Inventory boundary, sync quarantine, single-source registry, verification gates | Observed (docs) | `AGENTS.md`, `docs/source-sync.md`, read 2026-09-19 |
| Audit contents: scan scoping, provenance case, bounded live-service rows, license follow-up with hashes | Observed (docs) | `docs/release-audit.md`, `docs/publication-authorization.md`, read 2026-09-19 |
| Current red typecheck gate and stopped verifier | Observed (docs) | `docs/verification.md` (converted table), read 2026-09-19 |
| All five skills' rules as quoted | Observed | The five `SKILL.md` files, read 2026-09-19 |
| The gates actually run and pass as documented | Author-claimed | Repo documents; no clone, nothing executed, CI not inspected |
| Package-root license split (27 Apache-2.0 / 5 MIT), 503 dependency entries | Author-claimed | Audit figures; inventories not independently counted |
| Convergence is independent (not derived from TeaPrompt) | `[INFERENCE]` | No citation of TeaPrompt anywhere read; independence beyond absence of citation not establishable |

## Evidence Actually Checked

- GitHub API: repo metadata, `commits` (HEAD `e3724a13…`) — 2026-09-19.
- `README.md` (main body), `docs/architecture.md`, `AGENTS.md`, `docs/source-sync.md`, `docs/release-audit.md`, `docs/publication-authorization.md`, `docs/verification.md` — 2026-09-19.
- `.agents/skills/{cli-guide,testing-workflow,cross-layer-drift-sweep,verify-all-runtime-sinks,retro}/SKILL.md` — all five, 2026-09-19.
- Installed-surface greps for the surveyed vocabulary and the coverage citations — 2026-09-19.
- Not read: telemetry, open-source-status, LICENSE-STATUS, releasing, maintainers, installation/examples/demo docs, `README_ZH.md`, the source tree, CI runs. Not executed: anything.

## Falsifiability

- The "no sentence needed" mapping is wrong if an installed skill is later shown to lack a rule the Concept Map credits to it (rows name the surfaces; re-grep them).
- MC-5's adoption is wrong if the enumeration duty suppresses legitimate small changes (the bullet scopes itself to changes other surfaces consume; the Small-Change Fast Path is untouched) or if it catches nothing the landing reviews would have missed across the next several implementation records — the ledger row names the retire condition. The original deferral trigger (a completion declaration where an affected consumer class was never enumerated) is now the failure the installed sentence defends against.
- Finding 1's independence claim is inference; discovery of a citation path from their skills to TeaPrompt's texts would demote it to lineage, not convergence.
- The governance description is docs-tier: reading `scripts/verify.mjs`, the workflows, or CI results could revise the enforcement picture (docs-to-code fidelity was not audited here, unlike the RSIAgent survey).

## Completion Ledger

| Item | Status | Evidence |
| --- | --- | --- |
| Identity pinned; artifact and governance described from primary documents | done | this record |
| Ten concepts mapped; ten candidates decided with evidence and triggers | done | Concept Map; Candidate Adoption Ledger |
| MC-5 adopted under same-day user direction; additive bullet pinned once on `reflective-implement` | done | ledger row; Adoption Addendum; guard pin |
| Clean-room boundary on installed surfaces | done | guard vocabulary test |
| Guard written | done | `plans/tests/test_minimax_code_survey_record.py` |
| Decision Index row (at head), case-studies row, `index.json` | done | `PROJECT_KNOWLEDGE.md`; `external-adoption-case-studies-2026-06-20.md` |
| Full repository gate | done | `make all` from the repository root |

## Adoption Addendum (2026-09-19, same day, user direction)

The user's follow-up ("if worth then update skills") supplied adoption direction of the generic form: it fires no named or dated gates (GE-1, RS-9, the September holds, and DM-5 are untouched — their triggers name their own conditions), and it delegates the worth judgment to the standing bar. Under that bar the survey's ledger was re-read: MC-1–MC-4 and MC-6–MC-9 stay no-change (each is covered; adding any would duplicate an installed rule), MC-7/MC-10 stay record-only notes. MC-5 converted: its deferral had rested on "no verified local gap", and the precise re-read of `reflective-implement` performed under this direction found the gap is textual and real — the ledger tri-state governs items already listed, the Sufficiency Gate stops at the listed criteria, the Twin sweep enumerates twin defects, and "if a check cannot run, report why" covers known checks; nothing forces the consumer classes of a changed contract into the record, which is exactly the silent-unknown failure the surveyed skill exists to prevent in a production harness. One additive single-line bullet landed after the Twin sweep (its structural sibling: enumerate, tri-state, report), scoped to changes other surfaces consume so the Small-Change Fast Path is unaffected; clean-room held (the sentence carries no surveyed vocabulary and the record-name citation is omitted on the surface, per the prior token-conflict precedent); the guard flipped MC-5 to Adopted and pins the bullet exactly once at its surface.
