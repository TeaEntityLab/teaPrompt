# Code Recall Survey — 2026-08-20

> **Status: decided (non-authoritative); external-survey panel record, no
> adoption.** Code Recall is retained as study material. Its decision-lifecycle
> and re-anchor mechanisms are useful reference patterns; its persistent-memory
> runtime (hooks, MCP server, installers, CLI ledger), authority framing, and
> cleanup routines are not adopted. No TeaPrompt skill, lens, verifier,
> dependency, runtime, or project-knowledge rule was created or changed.
> `06-repo/AGENTS.md` and governed skill contracts remain authoritative; this
> record is evidence and a decision, not an operating rule.

## Purpose

Preserve the completed seven-lens survey of Code Recall so its adoption question
is not re-litigated from chat memory: what the tool implements, which claims
survive execution and adversarial probing, which trust boundaries fail on
ordinary local inputs, and whether TeaPrompt should study, reproduce, adopt, or
deploy any part of it.

## Target and Version

- Review target: [`erikhuang76821/code-recall`](https://github.com/erikhuang76821/code-recall),
  checked 2026-08-20. Default branch `master`.
- Survey pin: current `master` commit
  `116512be98ce6ee8b8a4ba190ca229e99b42515b` (2026-08-14), chosen because the
  upstream URL points at the live repository and current code differs from the
  tagged release.
- **Version-identity split (ambiguity, not disjoint runtime).** The label
  `2.10.0` maps to three revisions: the lightweight, unsigned GitHub tag
  `v2.10.0` at `03f09e7ad45783f13dc23c0a434d0f222a8a3b34` (2026-06-26); the
  published npm package `@erikhuang/coderecall@2.10.0` whose registry `gitHead`
  is `81f0bb188c03ea06629e64656faa015606d08cbc`; and current `master`
  (`116512be…`), 15 commits after the tag but still reporting `2.10.0` in
  `package.json` and the CLI. Executed `git diff` shows the functional runtime
  is nearly identical across all three: current-vs-tag `coderecall.js` differs
  by only 4 added / 3 removed install/help strings, and current-vs-npm-`gitHead`
  by 2/2 install strings. The published npm `coderecall.js`/`package.json`
  matched their declared `gitHead` exactly after CRLF→LF normalization. So the
  concern is reproducible-install identity and provenance, not divergent
  behavior or a demonstrated exploit delta between channels.
- License: MIT. Two listed contributors; young, single-maintainer-led project.
- Provenance surface: npm supplies SHA-512 integrity and a registry signature
  for its artifact; the GitHub tag is unsigned and there is no signed annotated
  release, cross-channel release hash, SBOM, or provenance attestation. CI
  Actions are pinned only to mutable major tags (`@v4`). `SECURITY.md` is
  excluded from the npm `files` allowlist, so npm installers do not receive it.
- Volatility trigger: re-pin the commit and re-run the containment, cleanup-
  ownership, MCP-failure, ledger-grammar, expiry, sanitizer, provenance, and
  install-lifecycle checks before relying on a later revision or on any tagged
  release that resolves the version split.

## Architecture and Feature Map

| Layer | Shipped surface | Observed behavior |
| --- | --- | --- |
| CLI core | one 3,459-line, zero-runtime-dependency `coderecall.js` | init/sync/status/doctor/digest/snapshot/consolidate/search/decisions/affected/decision/resolve-lesson/reconfirm/graduate/precommit/githook/deinit/score/mcp/selftest |
| State | `.ai/memory/TASK.md` (local), `DECISIONS.md`/`LESSONS.md` (committed), `archive/`, `sessions.md`, heartbeat/reminder/lock | plain-Markdown ledger; hybrid `.gitignore` splits volatile working state from durable team knowledge |
| Lifecycle hooks | `sessionstart.js`, `precompact.js`, `stop.js`, optional `userpromptsubmit.js` | Claude Code SessionStart digest injection, PreCompact transcript-tail snapshot + auto-consolidate, Stop heartbeat/timeline; other hosts are instruction-driven stubs (PARTIAL) |
| Retrieval | zero-dep BM25 status/confidence/recency-weighted search; resident digest index capped at 12 decision + 8 lesson titles; current-vs-history split | search/decisions/digest surface current truth by default |
| Lifecycle governance | status (proposed/accepted/superseded/deprecated/resolved/obsolete), `expires:`, supersede chains, `reconfirm`, `graduate` to `docs/adr` and optional `~/.coderecall` | code-maintained, mark-over-delete |
| MCP | stdio JSON-RPC tools: read/update/write/resolve/reconfirm/search/list | binds ledger paths once at launch CWD |
| Assurance | inline `selftest`, `bench/bench.js`, three-OS × Node 18/20 CI | source-shape + controller regression; synthetic context-hygiene/write-back benchmarks |
| Claims | README/SPEC/SECURITY/COMPATIBILITY | compaction survival CI-proven for Claude hooks; explicit "advisory, not enforcement"; no shipped live-agent efficacy numbers |

## Panel Execution Mode

Method contract: `04-agent/workflow-recipes.md` §Parallel Lens Review with the
host `parallel-lens-review-packet` wrapper.

1. The merge owner cloned the pinned commit, mapped every CLI/hook/template/
   installer/doc surface, read the tag/npm/CI/issue metadata, and diffed the
   three `2.10.0` revisions.
2. The merge owner executed the deterministic and adversarial checks below, then
   wrote one shared packet inside the transient clone. Packet SHA-256:
   `277f6e544ade938170463b7eae5bb1dddaf1a731b1763f2e4ed1394d8afc4c95`.
   It separated observed, author-claimed, `[INFERENCE]`, and unknown claims and
   carried a tailored load-bearing question per lens.
3. Seven read-only lenses fanned out in one batch: evidence, architecture,
   reproducibility, security/provenance, code correctness, usability, and
   strategic fit. All seven completed. Five scout yields were schema-coerced and
   the reviewer yield failed structured-schema validation; every complete
   deliverable was recovered by tier-1 DM-wake over IRC while the woken agents
   still held full context.
4. The merge owner, not the read-only lenses, executed all reproduction and
   mutation slices. No lens edited TeaPrompt or upstream files.
5. Role labels are review perspectives. No claim is made that distinct model
   providers or personas were invoked.

## Lenses

| Lens | Load-bearing question | Main result | Verdict |
| --- | --- | --- | --- |
| Evidence | Which claims are executed, fixture-only, or unsupported? | Selftest/bench/CI are real and reproduce; live-agent efficacy is unshipped; SECURITY/containment/fencing claims exceed verified behavior; version label is ambiguous | AGREE WITH CHANGES |
| Architecture | Is the plain-Markdown state + lifecycle design cohesive and proportionate? | Elegant hybrid state split and status lifecycle, but a 3,459-line monolith concentrates change risk and the parser/authority/containment layers are fragile | AGREE WITH CHANGES |
| Reproducibility | What tier does assurance actually reach? | Syntax/unit/fixture/subprocess-integration and synthetic benchmarks reproduce; host integration, install.ps1, non-Node-18/20, and live efficacy are untested; identity split complicates reproducible install | AGREE WITH CHANGES |
| Security/provenance | What executes, writes, escapes, or loses identity? | No shipped network egress, but P1 symlink-parent containment escape, receipt-less cleanup deletion of user config, heuristic transcript redaction, MCP mis-binding/false-success, and unsigned/ambiguous release identity | AGREE WITH CHANGES |
| Code correctness | Are the probes real contract defects? | All eight packet probes confirmed against source; nine further defects found, incl. an unlocked `graduate --global` cross-project race; last-writer-wins timeline and graduated-stays-active are documented tradeoffs, not defects | AGREE WITH CHANGES |
| Usability | Does it reduce burden across operators/hosts? | Practical for solo long-session Claude Code work; continuous recitation cost, `sync --all` workspace clutter, single-file `DECISIONS.md` merge conflicts, silent MCP CWD binding, and 2h dirty-staleness blind spot hurt team/short-task/regulated use | AGREE WITH CHANGES |
| Strategic fit | Is any mechanism a verified TeaPrompt gap? | Methodology overlaps existing risk-scaled workflows/ledgers; persistent runtime is a standing non-goal; three concepts remain study-only; runtime import rejected | AGREE WITH CHANGES |

## Panel Consensus

- **Decision:** `AGREE WITH CHANGES` — unanimous, **7 of 7 lens verdicts**; no
  terminal `DISAGREE`. The usability lens additionally dissents on *general*
  adopt/deploy while keeping its terminal verdict at AGREE WITH CHANGES; that
  dissent is preserved below and does not change the unanimous use-case outcome.
- **Method quality:** the hybrid local/committed state split, status/expiry/
  supersede lifecycle, current-vs-history retrieval, resident title index,
  compaction re-anchor, `code:`-link advisory, and candid "advisory, not
  enforcement" framing are genuinely useful study material. The tool is unusually
  honest about several of its own limits (Claude-only automation, heuristic
  redaction, disclosed MCP deviations, non-destructive graduation).
- **Executable quality:** real 93-check selftest and deterministic benchmarks
  pass, but the checks smoke source shape and controller lifecycle on fixtures,
  not live-host integration or agent efficacy. Reproduced defects — parent-
  symlink containment escape, receipt-less cleanup deletion, MCP false-success/
  server-termination, Markdown-grammar record forgery, unfenced model-facing
  MCP/CLI output, expiry off-by-one, and an unlocked cross-project global-lessons
  race — are contract or safety failures on ordinary local inputs.
- **Evidence quality:** no live baseline/treatment agent evaluation shows Code
  Recall reduces re-litigation, dead-end retries, context-loss restarts, or token
  cost. The deterministic benchmarks measure only context hygiene and write-back-
  gap detection, and say so.
- **Local fit:** TeaPrompt already covers the methodology through risk-scaled
  routing, decision archives, review triggers, handoff, and evidence ledgers.
  External existence is not a verified local structural gap, and a persistent
  memory runtime is a standing non-goal.

### Use-Case Recommendation

| Use case | Recommendation |
| --- | --- |
| `study` | **yes** — study the local/committed state split, status/expiry/supersede lifecycle, current-vs-history retrieval, resident title index, compaction re-anchor, and the candid benchmark scoping |
| `reproduce` source/controller behavior | **yes, pinned sandbox only** — isolated, non-sensitive, single-project workspace at commit `116512be…`; run `selftest`/`bench`; never inside a workspace with a symlinked `.ai/` or pre-existing hooks/config that reference `coderecall`/`stop.js`; do not register real global hooks |
| `reproduce` live-agent efficacy | **blocked** — no shipped harness, tasks, prompts, seeds, transcripts, grader, or token traces exist |
| `adopt` selected patterns into TeaPrompt | **no current change** — CR-1 through CR-3 remain study-only with local-evidence triggers |
| `adopt` the runtime (hooks/MCP/installers/ledger) | **no** — duplicated local coverage, standing runtime non-goal, and unsafe unchanged |
| `deploy` in shared, concurrent, sensitive, regulated, untrusted, or multi-project MCP environments | **blocked at this revision** — containment, cleanup ownership, MCP identity/failure/output, ledger grammar, provenance, and privacy boundaries are unresolved |

## Required Wording Changes

These are upstream-facing corrections consolidated from the panel. None was
applied to TeaPrompt or the upstream repository.

1. **Correct the "never touches anything else" claim.** `SECURITY.md`'s touched-
   surface table omits `CLAUDE.md`, `.gemini/settings.json`, `.cursor/hooks.json`,
   `.gitignore`, `docs/adr/`, and `~/.coderecall/GLOBAL-LESSONS.md`. List every
   surface and drop the absolute "never touches anything else."
2. **Correct the subprocess claim.** State that `doctor` executes the exact
   settings-provided SessionStart command through the host shell during its
   health check, in addition to `git` and the selftest self-invocation.
3. **Correct the fencing claim.** Only the SessionStart digest and PreCompact
   snapshot fence ledger/transcript text; `search_memory`, `list_decisions`, and
   raw CLI `search`/`decisions` output are unfenced model-facing project data.
4. **Disclose cleanup ownership limits and stop claiming precision.** Replace
   installer "removes ONLY our entries" / "existing entries are never modified or
   removed" and the deinit byte-for-byte-preservation claim with the truth: a
   pre-existing hook whose command merely contains `coderecall`, any command
   matching `/coderecall|stop\.js/i`, a pre-existing `@AGENTS.md` import, or a
   pre-existing `AGENTS.md` Gemini `contextFileName` entry is removed on
   uninstall/deinit. Ship per-install ownership receipts (exact object + hash +
   pre-existence) and remove only receipt-owned unchanged additions; otherwise
   preserve and warn.
5. **Enforce filesystem containment.** Canonicalize the project root, walk each
   existing ancestor with `lstat`, reject symlink/junction traversal below the
   root, and revalidate before any destructive `deinit` apply; abort on ambiguity
   and print canonical targets.
6. **Fix MCP failure and output semantics.** Check `setTaskField`'s return before
   reporting success; replace library `process.exit`/`fail()` paths with thrown
   errors surfaced as `isError`; validate an explicit per-call project identity
   (MCP roots or a required `--project`) and refuse ambiguous binding; fence all
   model-facing tool output.
7. **Reject or encode ledger structure.** Strip CR/LF and reserved `## `/metadata
   prefixes from authored titles and bodies, or store a typed record rendered to
   Markdown, so one write parses back to exactly one entry.
8. **Fix the expiry contract.** Either compare `<=` today or change the docs
   from "auto-forget on/after this date" to "after this date"; today the entry
   stays current on its own expiry date.
9. **Make `doctor` inspection-only by default.** Move hook execution behind an
   explicit `doctor --execute-hooks`, show the exact command first, and stop
   selecting it by broad substring match.
10. **Lock or scope the global-lessons write.** `graduate --global` performs an
    unlocked read-modify-write on `~/.coderecall/GLOBAL-LESSONS.md`; two projects
    running it concurrently lose one project's lessons. Add a global-file lock or
    append-only merge.
11. **Resolve the release identity.** Increment the master version, publish only
    from CI at a signed annotated tag whose commit matches `package.json`, npm
    `gitHead`, and a published SHA-512; add SBOM/provenance; pin Actions by SHA;
    include `SECURITY.md` in `package.json.files`.
12. **Calibrate efficacy language and host coverage.** Keep "advisory / structures
    and surfaces" wording until a baseline/treatment agent evaluation exists, and
    state that non-Claude hosts, `install.ps1`, Node outside 18/20, and network
    filesystems are untested.

## Candidate Adoption Ledger

| ID | Candidate | Status | Evidence | Next action or trigger |
| --- | --- | --- | --- | --- |
| CR-1 | `code:`-backlinked file→decision advisory (`affected`): surface current decisions/lessons governing changed files | Deferred / study-only 2026-08-20 — no artifact change | Useful anti-rot concept, but it is file-level advisory only, omits untracked files, and TeaPrompt already links decisions to evidence via plans/adoption ledgers; no local decision-vs-code-drift incident was established | Reconsider after a documented local case where a code change silently invalidated a recorded decision that existing review triggers missed. First extend an existing ledger/lens, not a new runtime. Falsifier: file→decision links add token/upkeep cost without reducing local regressions |
| CR-2 | Expiry / `reconfirm` staleness lifecycle for durable knowledge | Deferred / study-only 2026-08-20 — no artifact change | `reflective-handoff-retro` and PROJECT_KNOWLEDGE review triggers already govern staleness; no local incident where a dated auto-forget would have prevented a stale-constant error; upstream expiry is off-by-one | Reconsider if `PROJECT_KNOWLEDGE.md` accumulates stale constants that repeatedly mislead. Falsifier: explicit expiry forces needless re-validation of slow-moving constants |
| CR-3 | Current-vs-history status-weighted retrieval + resident title index | No change 2026-08-20 | TeaPrompt search/retrieval is host-provided and owning a retrieval runtime is a standing non-goal; the current-truth-by-default and anti-fragmentation title-index ideas are already expressed by decision archives and review-before-propose discipline | Revisit only if a host-independent retrieval guarantee becomes a prompt-impossible local need. Falsifier: the pattern duplicates existing archive/search behavior without changing decisions |
| CR-4 | Cleanup-ownership receipt discipline (learned as an anti-pattern) | Deferred / study-only 2026-08-20 — no artifact change | Reproduced deletion of pre-existing user hooks/config via substring/regex/value matching is a concrete caution, but TeaPrompt ships no installer that mutates shared user config today | Reconsider only if TeaPrompt ever ships a local installer/uninstaller; then require per-install receipts and refuse deletion without one. Falsifier: strict receipts add ceremony without preventing real drift |
| CR-5 | Import the persistent-memory runtime (hooks, MCP server, installers, CLI ledger) into TeaPrompt | Rejected; deployment blocked 2026-08-20 | Standing runtime non-goal; near-total methodology overlap; reproduced P1 containment escape, receipt-less cleanup deletion, MCP false-success/termination, ledger-grammar forgery, unfenced model output, expiry off-by-one, global-lessons race, and ambiguous unsigned release identity | Reconsider only if TeaPrompt changes scope to own a memory runtime and a later pinned, signed release fixes all P0/P1 defects, publishes reproducible provenance, and demonstrates a verified local structural gap |
| CR-6 | Adopt the generated "the ledger wins / re-anchor from the ledger" authority protocol as a governed instruction | Rejected 2026-08-20 | The suite installs an instruction-authority surface sourced from agent-written Markdown and untrusted transcripts; TeaPrompt's canonical authority chain and runtime-trust-boundary already govern instruction/data separation and forbid promoting retrieved/agent-written content to authority | Re-litigate only with a runtime that cryptographically separates trusted instruction from ledger data. Falsifier: none needed — this conflicts with the standing authority boundary |

No candidate created or changed a TeaPrompt skill, lens, verifier, dependency,
runtime, or project-knowledge rule. Deterministic guard for this record:
`plans/tests/test_code_recall_survey_record.py`.

## Shared Findings

### What is strong

1. **Hybrid state split.** Local-only `TASK.md`/`sessions.md` versus committed
   `DECISIONS.md`/`LESSONS.md` avoids multi-developer working-state merge noise
   while keeping durable knowledge team-shared.
2. **Honest lifecycle governance.** Status/expiry/supersede/`reconfirm` with
   mark-over-delete keeps decision evolution visible and current-truth-first.
3. **Attention discipline.** Current-vs-history default, status/confidence/recency
   weighting, and a resident title index capped at 12/8 keep the injected digest
   bounded and anti-fragmenting.
4. **Candid boundaries.** README/SPEC/SECURITY repeatedly distinguish advisory
   surfacing from enforcement, disclose the MCP deviations, and refuse to ship
   faked agent numbers.
5. **Narrow executable surface.** Zero runtime dependencies; user-facing scripts
   import no `http`/`https`/`net`/`tls`/`dgram`; no `install`/`postinstall` hook.
6. **Real regression work.** A 93-check selftest drives the actual hook scripts
   and controller lifecycle; three-OS × Node 18/20 CI ran green at the pin; the
   published npm artifact independently passed the same 93 checks and benchmarks.

### Load-bearing gaps

1. **Containment escape:** `MEM_DIR` is a textual `path.join(CWD, '.ai',
   'memory')`; `rmrf` lstat-checks only the final component. A pre-existing `.ai`
   parent symlink made `init` write externally and `deinit --yes` recursively
   delete the external target plus an unrelated sentinel. (A final `memory`
   symlink is unlinked, not traversed — the parent-symlink case is the escape.)
2. **Receipt-less cleanup deletion:** global uninstall removed a pre-existing user
   SessionStart hook solely because its command contained `coderecall`; `deinit`
   removed a pre-existing `@AGENTS.md` import, an `AGENTS.md` Gemini
   `contextFileName` entry, and a `/user/custom/stop.js` Cursor hook via
   `/coderecall|stop\.js/i` — contradicting "removes ONLY our entries" and
   byte-for-byte-preservation claims. Not disclosed anywhere.
3. **MCP failure/output semantics:** `update_task` returns success with no
   `TASK.md`; a missing `DECISIONS.md` terminates the long-lived server via
   `fail()`; `search_memory`/`list_decisions` return unfenced project text.
   Disclosed in SPEC but still contract violations.
4. **Ledger-grammar forgery:** one `decision`/MCP write with a newline title or a
   `## ` body line serializes into multiple parsed entries; `doctor` accepted the
   forged well-formed entry.
5. **Expiry off-by-one:** `expires < today` keeps an entry current on its own
   expiry date, contradicting "auto-forget on/after."
6. **Global-lessons race:** `graduate --global` does an unlocked read-modify-write
   on `~/.coderecall/GLOBAL-LESSONS.md`; concurrent projects lose one project's
   lessons (source-confirmed by the correctness lens; not coordinator-executed).
7. **Heuristic redaction:** the transcript sanitizer persisted a `mysql://` URL
   with credentials and an `rk_live_…` value verbatim; it is defense-in-depth, not
   a privacy boundary.
8. **`affected` blind spot:** the default working-tree diff omits untracked files,
   so a new file governed by a `code:` link is invisible (advisory, disclosed as
   "not proof," but the untracked omission is undocumented).
9. **Version identity:** one `2.10.0` label spans three unsigned/ambiguous
   revisions; npm integrity does not bind bytes to the GitHub tag.
10. **No efficacy evidence:** nothing measures whether the tool changes agent
    outcomes; benchmarks are synthetic context-hygiene/detection only.

## Mechanism vs. TeaPrompt Fit

| Mechanism | Existing TeaPrompt coverage | Verified local gap? |
| --- | --- | --- |
| Local vs committed state split | handoff/state ledgers; plans vs working notes | No |
| GOAL/NOW/NEXT + checklist | Why/What/How/Done, `reflective-brief`, `reflective-implement` | No |
| Decision status/supersede/expiry lifecycle | plans decision archive, PROJECT_KNOWLEDGE review triggers, adoption ledgers | No; persistence is a standing non-goal |
| Compaction re-anchor + transcript snapshot | host context/checkpoint/handoff surfaces | Operational/runtime, standing non-goal |
| Current-vs-history BM25 retrieval + resident index | context engineering; host retrieval tools | No local recurrence; runtime non-goal |
| `code:`-link file→decision advisory | adoption guards, source pointers | Adjacent; no documented local drift incident |
| MCP/hooks/installers/CLI runtime | standing runtime/integration non-goal | Out of scope and unsafe unchanged |
| Generated "ledger wins" authority protocol | canonical authority chain + runtime-trust-boundary | Conflict, not a gap |

## Evidence vs Inference

| Claim | Status | Basis |
| --- | --- | --- |
| Pin, three-way version split, tiny runtime diffs, license, npm/tag/CI metadata | Observed / verified | GitHub/npm APIs, pinned clone, executed `git diff`/`shasum`; checked 2026-08-20 |
| Selftest 93/93 and benchmarks pass on current master and published npm | Observed / executed | Local Node 24.3 runs; upstream three-OS × Node 18/20 CI-read at the pin |
| Parent-symlink containment escape and external `deinit` deletion | Observed / executed | Isolated symlink probe + `rmrf`/`cmdDeinit` source |
| Receipt-less cleanup deleted pre-existing user hook/import/config | Observed / executed | Isolated global-uninstall and `deinit` probes + installer/deinit source |
| MCP false-success and server termination | Observed / executed | stdio probes against missing `TASK.md`/`DECISIONS.md` + source |
| Ledger-grammar record forgery; unfenced MCP/CLI output | Observed / executed | `decision`/MCP write probes + `parseEntries`/tool source |
| Expiry off-by-one; `affected` untracked omission; sanitizer misses | Observed / executed | Dated-entry, untracked-file, and secret-string probes + source |
| `graduate --global` cross-project race | Source-confirmed (not executed) | Correctness-lens source review of the unlocked global RMW |
| Live-agent efficacy (drift/dead-ends/cost) | Unverified / unavailable | No shipped harness, tasks, or transcripts |
| Recitation/context operator cost | `[INFERENCE]` | Protocol requires per-step write-back; local cost not measured |
| A later release repairs blockers | Unknown / volatile | Must re-pin and re-run checks |

## Disagreements / Residual Risks

- **Terminal unanimity vs adopt/deploy dissent:** all seven lenses returned
  terminal AGREE WITH CHANGES. The usability lens separately argues general
  adoption/deployment is a `DISAGREE`; the architecture and security lenses treat
  the containment/cleanup/injection defects as categorical deploy blockers. The
  use-case outcome (study yes, reproduce sandbox-only, no adoption, deploy
  blocked) is unanimous, so the record keeps the AGREE WITH CHANGES consensus and
  preserves the adopt/deploy dissent explicitly.
- **Advisory-by-design steelman:** the strongest counterargument is that Code
  Recall scopes itself as an advisory layer and is unusually candid, so several
  findings are accepted tradeoffs. Counter: the cleanup-ownership deletions are
  *not* disclosed and directly contradict the installers' "removes ONLY our
  entries," so they are undocumented data loss, not a disclosed tradeoff.
- **Doctor execution is user-trusted, not remote RCE:** `doctor` runs a command
  from the user's own settings, invoked deliberately; it is a boundary/claim
  mismatch, not an untrusted-repository code-execution path.
- **Symlink precondition:** the containment escape requires a pre-existing
  symlinked `.ai/`; unusual, but destructive when present and unguarded, and
  Windows junction/reparse behavior is untested (`unknown`).
- **Version split is identity, not behavior:** corrected from an initial
  "three disjoint runtimes" framing; runtime is nearly identical across channels.
- **No PROJECT_KNOWLEDGE promotion:** one external survey adds no new durable
  local lesson; existing mechanism-vs-product, evidence-over-confidence, and
  prompt-vs-runtime lessons already govern it.
- Not executed: `install.ps1` on Windows; junction/reparse containment; live-agent
  benchmark; non-Claude host discovery/compaction; network-filesystem lock
  behavior; Node outside 18/20/24.3; the `graduate --global` concurrency race.

## Evidence Actually Checked

- GitHub repository/tree/commit/tag/release/contributor/issue/Actions APIs; npm
  registry metadata for `@erikhuang/coderecall@2.10.0`; pinned clone at
  `116512be…` — checked 2026-08-20.
- `git diff`/`rev-list` across tag `03f09e…`, npm `gitHead` `81f0bb…`, and master
  `116512be…`; `shasum` + LF normalization confirming npm bytes match `gitHead`.
- Full/targeted reads: `coderecall.js`; four hooks; `bench/bench.js`;
  `docs/launch/demo.js`; templates; both READMEs; SPEC/SECURITY/COMPATIBILITY/
  CHANGELOG/ROADMAP; `package.json`; `.github/workflows/ci.yml`; installers.
- `node coderecall.js selftest` — 93/93 on Node 24.3 (current master and the
  extracted published npm artifact); `node bench/bench.js` — deterministic
  context-hygiene and write-back benchmarks; `node -c` on all scripts; `npm pack
  --dry-run` (22 files, `SECURITY.md` excluded); upstream CI run `31792233469`
  (four green jobs).
- Adversarial execution (isolated temp projects): parent-symlink `init` wrote
  externally and `deinit --yes` deleted the external target + sentinel; global
  uninstall deleted a pre-existing `coderecall`-substring hook; `deinit` removed a
  pre-existing `@AGENTS.md` import, `AGENTS.md` Gemini context entry, and
  `/user/custom/stop.js` hook; MCP `update_task` false success without `TASK.md`;
  MCP `write_decision` terminated the server with no `DECISIONS.md`; MCP
  search/list returned unfenced `IGNORE ALL SAFETY` text; `decision` newline/`##`
  titles and bodies forged extra entries; `expires: today` stayed current;
  default `affected --json` omitted an untracked governed file; PreCompact
  persisted `mysql://…:hunter2@…` and `rk_live_…` verbatim; 40 concurrent
  `decision` writes all persisted; 40 concurrent Stop hooks left 1 timeline entry
  (documented last-writer-wins); POSIX installer install/install/uninstall
  round-trip preserved unrelated settings; normal `sync --all`→`deinit` preserved
  unrelated user content.
- Not executed or unavailable: `install.ps1`/Windows junctions; live-agent
  efficacy; non-Claude host runs; `graduate --global` race; network-filesystem
  locks; signed-release verification beyond observed absence.

## Falsifiability

- The containment verdict is repaired, not refuted, if a later pinned release
  canonicalizes the project root, rejects symlink/junction traversal, and proves
  it with parent-symlink and Windows-junction tests.
- The cleanup-ownership verdict is wrong if a release adds per-install receipts
  and preserves-and-warns on every reproduced collision.
- The MCP verdict is wrong if a release checks mutation returns, surfaces errors
  as `isError` without process exit, validates per-call project identity, and
  fences model-facing output.
- The no-local-gap disposition is wrong if TeaPrompt records a concrete decision-
  vs-code drift, staleness, or handoff failure that existing governed surfaces
  cannot address; that triggers CR-1 or CR-2, and does not by itself justify a new
  skill or runtime.
- The no-efficacy finding is wrong if upstream publishes a reproducible
  baseline/treatment agent evaluation tying the tool to task outcomes.
- This ledger is dead text if a trigger fires and no re-evaluation occurs, or if a
  rejected candidate is adopted without changing its recorded status and guard.
