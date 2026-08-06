# Prime Agent Survey — 2026-08-06

> **Status: decided (non-authoritative); external-survey panel record, no
> adoption.** Prime Agent is retained as study material: two architectural
> patterns (structured state ledger, auto-refine review gate) are deferred
> with explicit triggers; runtime adoption and deployment are rejected. No
> TeaPrompt skill, lens, verifier, dependency, or runtime surface was created
> or changed. `06-repo/AGENTS.md` and governed skill contracts remain
> authoritative; this record is evidence and a decision, not an operating
> rule.

## Purpose

Preserve the completed 7-lens survey of Prime Agent so the adoption questions
are not re-litigated from chat memory: (1) whether the "Self-Improving RLM
Agent" claims survive source-level verification; (2) whether the RLM
(persistent-IPython-as-only-tool) and Continual Harness patterns teach
TeaPrompt anything worth borrowing; (3) whether the runtime is safe to adopt
or deploy.

## Target and Version

- Review target: [`PrimeIntellect-ai/prime-agent`](https://github.com/PrimeIntellect-ai/prime-agent), checked 2026-08-06.
  Pinned: v0.7.0, commit `c22549a37b73cc603c6f0d202517cb0ca856c7d3`
  (2026-08-05). MIT license — Copyright (c) 2025 Mario Zechner, (c) 2026
  Prime Intellect. TypeScript monorepo (910 TS files, npm workspaces:
  agent/ai/coding-agent/tui, all still under the `@earendil-works/pi-*`
  package namespace) plus a separate Python kernel shim
  (`prime-agent-runtime`, 1533 LOC, 4 test files).
- Provenance: a hard fork/extension of Mario Zechner's `pi` codebase
  (earendil-works), acknowledged in the README and LICENSE. License boundary
  verified clean (all four package manifests MIT).
- Volatility trigger: the repo was active the day before the check
  (HEAD dated 2026-08-05); re-pin the commit and re-verify the extension
  auto-load behavior, harness-state atomicity, and CI Python-test coverage
  before relying on any later revision.

## Panel Execution Mode

Method contract: `04-agent/workflow-recipes.md` §Parallel Lens Review with the
host `parallel-lens-review-packet` wrapper.

1. The merge owner ran a pre-panel verification pass: cloned the repo,
   captured commit/license metadata, read the core docs
   (architecture/rlm/rlm-runtime/daemon/long-running-agents/skills/providers),
   read the full Python runtime shim, inspected `install.sh` checksum logic
   and `ci.yml`, and verified every source line reference in the
   user-supplied concept map before writing the packet.
2. One shared packet was written to an absolute path inside the transient
   clone (`/tmp/surveys/prime-agent/review-packet-prime-agent-2026-08-06.md`),
   readable by scout lenses via absolute path; it was deleted after
   synthesis. It separated observed / author-claimed / `[INFERENCE]` tiers
   and carried one load-bearing question per lens.
3. Seven scout lenses fanned out in a single batch; all seven completed on
   the first attempt (no quota fallback needed).
4. All seven scout yields were schema-coerced into
   `{summary, files, architecture}`; all seven full deliverables were
   recovered by tier-1 DM-wake over IRC. This re-proved the recovery path
   after prior field uses on 2026-07-27 and 2026-08-04; this run was 7/7.
5. The build/test reproduction slice was executed by the merge owner
   directly (coordinator-run commands, fable-method precedent):
   `pip install -e .` of `prime-agent-runtime` on Python 3.13, then pytest —
   **62 passed, 2 failed**, both failures `ModuleNotFoundError: No module
   named 'mcp'` (optional dependency required by `test_mcp_base.py` only;
   no code defect). The TS build was not run (repo AGENTS.md forbids
   wholesale `npm run build/test`; native deps libcairo/pango/zeromq).
6. Role labels are review perspectives; no claim is made that distinct model
   providers were used. No reviewer edited the TeaPrompt repository or the
   clone.

## Lenses

| Lens | Load-bearing question | Main result | Verdict |
| --- | --- | --- | --- |
| Evidence auditor | Do the concept map, README, and docs match source? | All cited `main.ts` line refs (171/213/371/445/937) exact; `/refine` judgment located in `refinement.ts` (`planRefinement`:855-947 LLM pass + `reviewAutoRefine`:949-1011 gate); depth default 1, control-channel deadlock avoidance, and HMAC-SHA256 framing all match code; drift: `/refine rollback` implemented but undocumented | AGREE WITH CHANGES |
| Architecture | Is RLM + Continual Harness + daemon topology sound? | RLM is expressive but pays latency/token/complexity tax vs discrete tools; "self-improving" is structured in-context learning, not model improvement; daemon topology right-sized for long-running work, over-engineered for quick edits; 3 failure modes named (sync-blocking kernel deadlock, stale lease lockout, JSON-parse failures silently breaking refinement) | AGREE WITH CHANGES |
| Reproducibility (+ merge owner) | Can a fresh clone build/check/test? | CI real (biome+tsgo+sharded vitest) but **Python runtime tests omitted from CI entirely**; provider integration tests silently skip without API keys; native deps (zeromq/canvas) are local-build friction; merge-owner pytest run: 62/2 (optional-dep only) | AGREE WITH CHANGES |
| Provenance & security | What executes on an adopter's machine? | License boundary clean (MIT, pi fork acknowledged); installer checksums in-band only (no signing/SBOM); telemetry removed in v0.7.0; trust model documented honestly; **critical: project-local extensions under `cwd/.prime/agent/extensions/` auto-execute via `jiti.import` at startup with no confirmation — RCE in untrusted clones** | AGREE WITH CHANGES |
| Code correctness | Is the Python shim + host bridge correct? | **Non-atomic harness writes (`open("w")`, harness.py:285-298) + silent empty-state fallback on parse errors (harness.py:180-184, refinement.ts:291-299) can permanently wipe all harness state**; unlocked `auth.json` reads race TS-side OAuth refresh (`mcp_base.py:61-71`); `refineHarness` utility omits `baselineState` bypassing conflict detection; subagent cancellation race during async setup | AGREE WITH CHANGES |
| Usability | Usable by a non-PrimeIntellect user today? | Yes — onboarding, recovery journals, and doctor/status are solid; but Windows daemon discovery broken (`daemon-ps.ts` uses Unix-only `ss`/`lsof`; default named pipe invisible when no workers tracked) and autonomous quality gates silently lose their unchanged-workspace optimization in non-git directories (token-burn risk) | AGREE WITH CHANGES |
| Strategic synthesis | What should TeaPrompt learn, per use case? | RLM is an ergonomic (compositional) shift, not a paradigm shift; "self-improving" is config-persistence with functional behavioral adaptation; target user is long-running research evals, not daily coding; recommendation: study & reproduce patterns, do not adopt/deploy runtime | AGREE (packet accurate; no wording changes) |

## Panel Consensus

- **Decision:** `AGREE WITH CHANGES` (6 of 7 lens verdicts; 1 clean AGREE; no
  DISAGREE; all 7 lenses delivered full independent verdicts).
- **Prime Agent is what it claims architecturally.** The user-supplied
  concept map and the repo's own docs are faithful to source — every audited
  line reference, invariant (depth default 1, admission-handle-only returns,
  control-channel replies, HMAC framing), and process boundary was verified.
  This is the best doc-to-code fidelity of any surveyed repo to date.
- **The "Self-Improving RLM Agent" branding is overstated.** `/refine` runs
  an LLM planning pass (`planRefinement`) gated by a cheap review call
  (`reviewAutoRefine`) that applies CRUD edits to a supplemental JSON ledger
  (`harness_state.json`) recompiled into the system prompt. It never touches
  model weights or the immutable base prompt. `[INFERENCE]` Functionally it
  is structured, versioned, rollback-capable in-context learning — valuable,
  but "config-persistence with behavioral adaptation", not self-improvement.
- **Two adoption blockers for deployment:** (1) project-local extension
  auto-load RCE — launching the agent inside an untrusted clone executes
  `cwd/.prime/agent/extensions/*.ts` with user permissions, no prompt;
  (2) harness-state wipe — non-atomic kernel-side writes plus dual-sided
  silent empty-state fallback mean one interrupted write permanently erases
  all accumulated prompts/memories/skills at the next save.
- **The reproduction slice passed** where it could run: the Python runtime
  shim installs and tests green (62/2, failures optional-dep-only).

### Use-Case Recommendation

| Use case | Recommendation |
| --- | --- |
| `study` | **yes** — the state-ledger schema, auto-refine gate, host-bridge deadlock analysis, and daemon recovery journals are reference-grade |
| `reproduce` | **partial** — Python runtime shim reproduced locally in this survey; TS build/test not attempted (native deps, repo policy) |
| `adopt` patterns into TeaPrompt | **deferred, two candidates** — PA-1 (state ledger) and PA-2 (auto-refine gate) with explicit triggers; see ledger |
| `adopt` runtime as dependency | **no** — daemon/ZeroMQ/IPython complexity violates the dependency-free methodology boundary; TeaPrompt ships method contracts, not runtimes |
| `deploy` (use as an agent on real work) | **blocked until fixed** — extension auto-load RCE and harness wipe risk; if used anyway: only in trusted repos, with harness state backed up |

## Required Wording Changes

Upstream-facing candidates consolidated from the lenses. None was applied to
TeaPrompt or to the upstream repository by this review.

1. **Extension auto-load (behavioral):** `extensions/loader.ts` must require
   explicit confirmation before executing project-local extensions from
   `cwd/.prime/agent/extensions/`; README's trust warning must state that
   untrusted clones can currently execute code at launch.
2. **Harness atomicity (behavioral):** `harness.py` `save()` must use
   temp-file + `os.replace`; both `harness.py:180-184` and
   `refinement.ts:291-299` must stop degrading parse failures to an empty
   state that the next save persists (recover from backup or surface the
   corruption instead).
3. **`usage.md` `/refine` entry:** document the implemented
   `/refine rollback <refinement-id> [--global]` form.
4. **`rlm-runtime.md` Continual Harness section:** note that local harness
   refinement requires a persisted session directory and throws on ephemeral
   in-memory sessions.
5. **"Self-improving" framing:** README should scope the claim to
   supplemental-state refinement (the docs' own body text already does this
   correctly; the tagline overreaches).
6. **CI:** add the `prime-agent-runtime` Python unit tests to `ci.yml` (they
   are currently never run in CI).
7. **Windows:** `discoverDaemons()` must probe the default named pipe
   directly instead of relying on Unix-only `ss`/`lsof`; autonomous gate
   snapshotting needs a non-git fallback or a visible warning.

## Candidate Adoption Ledger

| ID | Candidate | Status | Evidence | Next action / trigger |
| --- | --- | --- | --- | --- |
| PA-1 | Structured state ledger pattern (typed kinds prompt/memory/skill/subagent + refinement-event history + before/after rollback snapshots) mirrored into any future TeaPrompt persistent-agent-state design | Deferred 2026-08-06 — no artifact change | `harness.py` HarnessState CRUD + RefinementEvent observed; `refinement.ts` applyRefinementProposal:705-802; TeaPrompt currently ships no persistent agent state surface | Reconsider when TeaPrompt first designs a durable agent-state or memory surface; falsifier: a state surface ships without typed kinds/rollback and nobody misses them |
| PA-2 | Auto-refine review gate (cheap LLM pre-pass judging whether trajectory evidence justifies a heavy refinement pass) for any future TeaPrompt refinement loop | Deferred 2026-08-06 | `reviewAutoRefine` (`refinement.ts:949-1011`) + `AUTO_REFINE_REVIEW_SYSTEM_PROMPT` observed | Reconsider when TeaPrompt adds any automated lesson-capture/refinement loop; falsifier: a refinement loop ships that wastes heavy passes on evidence-free trajectories |
| PA-3 | Python-backed skill package contract (`SKILL.md` + `pyproject.toml` + `run()` convention + editable kernel-venv install) | Concept-only 2026-08-06 | `skills.md` + `skill.py` (tyro CLI shim) observed; TeaPrompt skills are markdown method contracts by design | Revisit only if TeaPrompt ever ships executable skills; falsifier: an executable-skill need arises and markdown-only blocks it |
| PA-4 | prime-agent runtime/daemon as a TeaPrompt dependency or execution layer | Rejected 2026-08-06 | Panel consensus: dependency-free methodology boundary; daemon/ZeroMQ/IPython complexity and trust surface mismatch a prompt-library repo | Re-litigate only if TeaPrompt's scope changes to shipping a runtime |
| PA-5 | Deploying prime-agent as a working agent on TeaPrompt or user repos | Blocked 2026-08-06 | Extension auto-load RCE (`extensions/loader.ts`) + harness wipe risk (`harness.py:285-298` / `:180-184`) observed at pinned commit | Re-evaluate after upstream fixes both blockers at a later pinned revision; interim mitigation: trusted repos only, back up `harness_state.json` |

No candidate created a new TeaPrompt skill, lens, verifier, dependency, or
runtime surface. Deterministic guard for this record:
`plans/tests/test_prime_agent_survey_record.py`.

## Shared Findings

### What Prime Agent does well

1. **Doc-to-code fidelity.** Every audited architecture claim, line
   reference, and invariant matched source (checked 2026-08-06). The docs
   state the trust boundary ("not a security sandbox") honestly and
   repeatedly.
2. **A genuinely versioned refinement ledger.** Harness edits are typed,
   evidence-gated (by prompt contract), recorded as RefinementEvents with
   before/after snapshots, and rollback-capable — the discipline TeaPrompt's
   candidate-adoption ledgers enforce socially, implemented mechanically.
3. **Careful concurrency design where it was designed.** The Jupyter
   control-channel host-request path exists specifically to avoid a
   shell-channel deadlock, with `loop.call_soon_threadsafe` for cross-thread
   future completion; frames are HMAC-SHA256 signed; kernel execution is
   serialized while child agents run concurrently.
4. **Recovery engineering.** Idempotent command journals, lease-keyed
   session ownership, claim-before-deliver scheduling (no replayed uncertain
   prompts), coalesced missed ticks, two-phase coordinated updates, and
   visible recovery markers.
5. **Supply-chain hygiene basics.** 7-day `min-release-age` on deps,
   checksum-verified installer and Node download, telemetry removed in
   v0.7.0, 0600 `auth.json`, 0700 config dir.

### Load-bearing gaps

1. **Extension auto-load RCE** (`extensions/loader.ts`): silent
   `jiti.import` of `cwd/.prime/agent/extensions/*.{ts,js}` at startup.
   Undermines the otherwise-honest trust documentation.
2. **Harness state can be wiped by design**: non-atomic Python writes plus
   both sides silently treating corrupt JSON as empty state, persisted on
   next save.
3. **Python runtime shim is untested in CI** despite being the model-facing
   API surface.
4. **Reasoning-model JSON fragility**: `planRefinement`/`reviewAutoRefine`
   depend on strict JSON emission; truncation or verbose thinking output
   silently breaks the refinement loop (defensively handled but
   user-invisible).
5. **Windows support is partially broken** (daemon discovery) and autonomous
   gates degrade silently outside git repos.
6. **No independent evidence for "self-improving"** in-repo: no benchmark or
   eval demonstrates that refined harness state improves task outcomes;
   external repos (`verifiers`, `prime-rl`) are linked but out of scope.

## Evidence vs Inference

| Claim | Status | Basis |
| --- | --- | --- |
| v0.7.0 identity, MIT license, pi-fork provenance | Observed / verified | Pinned clone: LICENSE, package.json manifests, README, checked 2026-08-06 |
| Concept-map line refs exact (main.ts 171/213/371/445/937) | Observed / verified | Coordinator grep + evidence-lens re-verification |
| Python runtime installs and tests green (62 passed, 2 optional-dep failures) | Observed / executed | Merge-owner `pip install -e .` + pytest, Python 3.13, 2026-08-06 |
| `/refine` judgment is an LLM pass gated by a second LLM call | Observed / verified | `refinement.ts:855-947`, `:949-1011`, prompts read |
| Extension auto-load executes without confirmation | Observed / verified | `extensions/loader.ts` read by provenance lens |
| Harness wipe: non-atomic write + silent empty fallback both sides | Observed / verified | `harness.py:285-298`, `:180-184`; `refinement.ts:291-299` |
| Python tests absent from CI | Observed / verified | `ci.yml` read in full by two lenses + coordinator |
| Windows daemon discovery misses default pipe | Observed (static read) | `daemon-ps.ts` read; not executed on Windows |
| Autonomous non-git gate degradation causes token burn | `[INFERENCE]` | `autonomous.ts` snapshot logic observed; runtime behavior not measured |
| Refinement loop breaks silently under reasoning-model JSON drift | `[INFERENCE]` | Defensive parse paths observed; failure rate not measured |
| Refined harness state improves task outcomes ("self-improving") | Unverified | No in-repo benchmark; external repos not audited |
| TS build/check/test suite passes at pinned commit | Unverified locally | CI badge + workflow read only; not executed in this survey |

## Disagreements / Residual Risks

- **Daemon topology framing:** the architecture lens calls it
  over-engineered for interactive use; the usability lens calls its recovery
  logic "extremely robust". Both hold: the design optimizes long-running
  autonomous work at the cost of interactive-use overhead. Recorded as
  positioning, not defect.
- **Blocker ranking:** code-correctness ranks the harness wipe first (hits
  normal use); provenance ranks the extension RCE first (needs an untrusted
  clone). Both are deployment blockers in PA-5; no resolution needed.
- **"Self-improving" severity:** strategic lens grants "functional
  behavioral adaptation" as a fair reading; architecture lens calls the
  branding overstated. Consensus wording: technically-grounded mechanism,
  overreaching tagline.
- Scout lenses could not execute code; all build/test evidence above the
  Python shim is CI-read-only. Residual risk: an undetected TS-side test
  failure at the pinned commit.
- The clone and packet were transient (`/tmp/surveys/prime-agent`); this
  record and its guard are the durable artifacts.

## Evidence Actually Checked

- `git clone --depth 1`; `git log -1 --format='%H %ci %s'` — pin above
  (2026-08-06).
- Coordinator full reads: README, LICENSE, AGENTS.md, root package.json,
  `docs/{architecture,rlm,rlm-runtime,daemon,long-running-agents,skills,providers}.md`,
  `prime-agent-runtime/src/rlm/{__init__,harness,skill}.py` (structural),
  `install.sh` checksum sections, `ci.yml`, `cli.ts`.
- Coordinator executed: `pip3 install -e prime-agent-runtime` (Python
  3.13.0), `python3 -m pytest test/ -q` — **62 passed, 2 failed**
  (`ModuleNotFoundError: No module named 'mcp'` in `test_mcp_base.py` only);
  `grep` verification of all six concept-map line references; license-field
  scan of all four package manifests.
- Lens reads (file:line evidence in lens deliverables): `refinement.ts`
  (plan/review/apply paths), `agent-session.ts` (refine orchestration
  :7571-7678, depth check :9597-9601, child registry :9402, cancellation
  :9718-9844), `rlm-runtime.ts`, `kernel/index.ts` (control-channel replies
  :1274-1280, HMAC :284-386), `slash-commands.ts:35-57`,
  `extensions/loader.ts`, `auth-storage.ts`, `resolve-config-value.ts`,
  `daemon-ps.ts`, `autonomous.ts`, `goals.ts`, `auth-flows.ts`,
  `mcp_base.py:61-71`, `harness.py` (write/read paths), 414 TS test files
  counted, 4 Python test files read.
- Not verified: TS build/test execution; Windows/Termux behavior; installer
  end-to-end; `/refine` outcome quality; external `verifiers`/`prime-rl`
  repos; the Continual Harness arXiv paper (2605.09998) content.

## Falsifiability

- The consensus is wrong if a later audit shows the doc-fidelity finding was
  unrepresentative (systematic doc-vs-code drift elsewhere in the tree), or
  if the extension loader already gates project-local extensions behind a
  confirmation this review missed.
- PA-5's blockers are repaired (not refuted) if upstream lands atomic
  harness writes + corruption surfacing and extension-load confirmation;
  re-pin and re-verify then.
- The "no in-repo self-improvement evidence" finding is wrong if the linked
  external repos contain a reproducible benchmark tying `/refine` state to
  outcome deltas — that audit was explicitly out of scope here.
- This record is wrong if its deferred candidates (PA-1/PA-2) are never
  reconsidered when their triggers fire and never re-litigated — the exact
  drift failure the adoption ledger exists to catch.

Guard: `plans/tests/test_prime_agent_survey_record.py`.
