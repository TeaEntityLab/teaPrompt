# MiniMax Code Trace-Map Survey — pasted zh-TW entry-point/engine map (2026-09-19)

> **Status: decided — record-only; no installed change, no wording adopted.** The object is a pasted Traditional-Chinese code-trace map of `MiniMax-AI/minimax-code`: seven traces (TUI launch, headless exec, ACP server, account login, BYOK provider add, the in-process service layer, and the vendored engine boundary), decomposed into 35 claims, **every one anchored to a `file:line` plus a one-line code excerpt**. All 35 anchors were verified mechanically against the pinned revision `e3724a13d72d` — the same pin as the 2026-09-19 repository survey, unchanged upstream at verification time: 29 land verbatim at the exact claimed line, 4 land within ±2 (a single systematic +2 offset on the three README table rows; one double-hit that corroborates the map's own "two equivalent login subcommands" note), 1 lands at +4, and 1 is a paraphrase at the exactly-correct line (a two-branch ternary normalized into one statement). **Zero fabricated claims; every trace narrative holds.** This is the fifth pasted-synthesis survey, the second fully-holding one, and a new sub-genre — the source-anchored code map — whose verification cost one script. It also upgrades a slice of the prior survey's docs-tier claims to code-corroborated at the same pin. Clean-room throughout; this project's vocabulary is guarded off installed surfaces by the prior survey's guard.

## Research Question

User instruction: "survey according this: local://paste-11.md". Three questions: (1) do the map's `file:line` anchors and excerpts hold against the repository at a pinned revision; (2) do its trace narratives (delegation, boundaries, engine layering) hold semantically; (3) does any concept expose a verified gap on an installed TeaPrompt surface. A bare "survey" carries no adoption direction.

## Direct Recommendation (as of 2026-09-19)

- **Study: as a genre specimen.** A synthesis whose every claim carries a `file:line` and an excerpt is the cheapest kind to verify — one deterministic script settled all 35 — and the error profile it produced (systematic small offsets, one normalization, no fabrication) is exactly the profile that distinguishes an honest generator with a counting quirk from a confabulated map.
- **Reproduce: done, in effect.** The verification *is* the reproduction: seven files fetched at the pin, every anchor checked for excerpt presence, exact line, and drift; both boundary comments read in context.
- **Adopt: nothing.** The map's method (anchored claims) is how TeaPrompt records and guards already work; its content (CLI delegation, lazy imports, in-process service, zero-IO contract core, lease-brokered tool subprocesses) is runtime engineering — host territory — with two lines recorded as corroboration of installed architecture stances.
- **For citers:** the map's README line numbers carry a uniform +2 offset at this pin; its `program.ts:205` is at 209; its item 6d normalizes `return options ? …sendMessage(ctx, req, options) : …sendMessage(ctx, req);` (lines 289–291) into a single `return …sendMessage(ctx, req);` — line and semantics right, bytes not verbatim.

## Method

Coordinator verification (2026-09-19), no scouts, no panel: upstream HEAD re-checked (still `e3724a13d72d`, so line numbers compare against the identical revision the repository survey pinned); the two files the map cites without paths located via the Git tree API (`packages/local-runtime-v2/src/local/{cli-service,app}.ts`); seven files fetched raw at the pin (`README.md`, `packages/tui/src/cli/{main,program}.ts`, `docs/architecture.md`, the two local-runtime files, `packages/agent-core/src/index.ts`); a single Python table checked all 35 anchors (excerpt present? at the claimed line? within ±3? elsewhere? absent?) and printed the two boundary-comment contexts for semantic reading. Raw bytes were fetched directly — the known URL-reader line-drift caveat is why no reader-mode line numbers were trusted.

**Scope / acceptance:** verify every anchor at the pin; classify every deviation; map the concept set against installed surfaces; land nothing without a verified gap; run `make all` from the repository root.

## Verification Results

| Class | Count | Items | Reading |
| --- | --- | --- | --- |
| Exact line, verbatim excerpt | 29 | all others | held |
| Near (±2), verbatim excerpt | 4 | 1a/2a/3a (README rows, uniform +2: claimed 118/119/120, actual 120/121/122); 4b (claimed 128, hits at 117 **and** 129 — the map itself says the login subcommand exists twice) | held; one systematic offset, one corroborating double-hit |
| Far (+4), verbatim excerpt, unique hit | 1 | 5b (`program.ts` claimed 205, actual 209) | held with drift |
| Exact line, paraphrased excerpt | 1 | 6d (`cli-service.ts:291`: ternary's else-branch fused with line 289's `return`) | semantics held, bytes normalized |
| Absent / fabricated | 0 | — | — |

Semantic spot-reads, both verbatim at the pin: the in-process boundary comment sits directly above the class the map cites — `/** In-process CLI entry point: call local Application directly, without HTTP or RPC envelopes. */` (line 106; class at 107 exact) — and the engine-contract header reads `Pure TypeScript core for Mavis agent-loop contracts.` followed by `**Zero IO.** This package contains no filesystem access, no process spawning, no SQLite, no HTTP server.` with IO assigned to host packages, exactly the map's item 7b. The four `architecture.md` lines the map quotes (layering, vendored engine, lease broker, private-package resolution) match the file read in the repository survey.

## Concept Map

| ID | Concept (clean-room) | TeaPrompt coverage | Disposition |
| --- | --- | --- | --- |
| C1 | Source-anchored claim maps: every synthesis claim carries `file:line` + excerpt, making verification mechanical | Records cite file:line; guards pin exact strings; the intake rule (a summary's citation is the summary's claim until the page is read) — here the "page read" is one script | No change — installed method |
| C2 | Deviation classes are diagnostic: systematic small offsets and normalizations vs fabrication — an honest generator drifts uniformly; a confabulator invents | Verdict-scope family; the line-drift caveat (reader-vs-raw numbering) already recorded as a tool lesson | No change — specimen recorded |
| C3 | CLI delegation pattern: parser → injected callback (`dependencies.X ?? defaultX`) → lazy dynamic import per command | Runtime engineering | No change — host territory |
| C4 | Boundary self-documentation at the boundary: the no-HTTP/no-RPC rule lives as a comment on the class that enforces it | Loop/DAG packs co-locate contract prose with the template bytes; the 2026-09-05 lesson (template drifts from distant prose) is the same force | No change — corroboration |
| C5 | Zero-IO contract core: pure types/contracts package, IO pushed to host packages | TeaPrompt's own stance at policy level (P7: natural-language policy, no owned runtime; hosts own IO) | Noted — architecture corroboration, record-only |
| C6 | Lease-brokered short-lived tokens for tool subprocesses | `agent-governance-scaffold` capability tokens + broker receipts | No change — covered; production corroboration |

## Candidate Adoption Ledger

| ID | Candidate | Status | Evidence | Next action / trigger |
| --- | --- | --- | --- | --- |
| TM-1 | "Anchor every synthesis claim to file:line + excerpt" as an installed research rule | No change 2026-09-19 | C1 row: records and guards already work this way; the intake rule covers unanchored summaries — the harder case | Reopen only if a TeaPrompt record is found citing a source without a checkable anchor where one existed |
| TM-2 | Deviation-class taxonomy (offset vs normalization vs fabrication) as wording | No change 2026-09-19 | C2 row: verdict-scope family covers it; this record is the specimen | None |
| TM-3 | Runtime patterns (delegation, lazy import, in-process service) | No change 2026-09-19 | C3 row: host territory | None |
| TM-4 | Co-located boundary documentation sentence | No change 2026-09-19 | C4 row: packs already co-locate contract prose with templates | None |
| TM-5 | Cross-record evidence upgrade: the repository survey's docs-tier architecture claims (layering line, in-process boundary, vendored engine roles) are now code-corroborated at the same pin — its "docs-to-code fidelity was not audited" bound is narrowed for the architecture slice, not for the verify pipeline | Noted 2026-09-19 (record-only) | Verification Results; the prior record's own text stays correct as written (its bound described that survey's checks) | The remaining unaudited slice (scripts/verify.mjs, workflows, CI) reopens per the prior record's Falsifiability |
| TM-6 | Genre ledger: fifth pasted synthesis; second fully-holding; first source-anchored code map — mechanical verification, one script | Noted 2026-09-19 (record-only) | This record; the GE-1 symmetric-value finding gains a second held instance and its cheapest verification yet | GE-1 lands per its own gate on user direction |

Deterministic guard: `plans/tests/test_minimax_code_trace_map_survey_record.py` (identity and tallies, dispositions, deviation pins, index links; this project's clean-room vocabulary is enforced by `test_minimax_code_survey_record.py` — duplicating the same regex against the same surfaces would be weightless).

## Evidence vs Inference

| Claim | Status | Basis |
| --- | --- | --- |
| Upstream HEAD unchanged at verification time | Observed | Commits API, 2026-09-19 |
| All 35 anchor verdicts and the tally (29/4/1/1/0) | Observed / executed | Verifier script over raw files fetched at the pin, 2026-09-19 |
| Both boundary comments verbatim | Observed | Context prints from the same fetches |
| The map's trace narratives (delegation, DI, lazy imports, forwarding) | Observed at the cited lines; full call-graph not traced | Excerpt + context checks; no build, no execution |
| The README +2 offset's cause (generator counting quirk) | `[INFERENCE]` | Uniformity of the offset; the generator was not inspected |
| Zero fabrication | Observed for these 35 claims | The table; a different map from the same source could differ |

## Evidence Actually Checked

- Commits API re-pin; Git tree API path resolution — 2026-09-19.
- Seven files fetched raw at `e3724a13d72d`; 35-anchor verifier script run; `sendMessage` context read (lines 282–300) — 2026-09-19.
- The pasted map itself (`local://paste-11.md`, 191 lines, zh-TW).
- Not done: build, execution, call-graph tracing beyond the cited lines, inspection of whatever generated the map.

## Falsifiability

- The tally is wrong if re-running the verifier at the pin produces different classes (the script's table is in the session record; the pin is immutable).
- The "zero fabrication" verdict is bounded to these 35 claims at this pin — it says nothing about other maps from the same generator.
- TM-5's upgrade is wrong if the cited lines were reached by coincidence of text rather than the claimed structures; the context reads (class body, ternary, header comment) make that implausible for the checked items.
- C4's corroboration reading is wrong if the boundary comment postdates the boundary's violations rather than guarding them — history was not read.

## Completion Ledger

| Item | Status | Evidence |
| --- | --- | --- |
| All 35 anchors verified at the pin; deviations classified | done | Verification Results |
| Six concepts mapped; six candidates decided | done | Concept Map; Candidate Adoption Ledger |
| Cross-record upgrade recorded without editing the prior record | done | TM-5 |
| Guard written | done | `plans/tests/test_minimax_code_trace_map_survey_record.py` |
| Decision Index row (at head), case-studies row, `index.json` | done | `PROJECT_KNOWLEDGE.md`; `external-adoption-case-studies-2026-06-20.md` |
| Full repository gate | done | `make all` from the repository root |
