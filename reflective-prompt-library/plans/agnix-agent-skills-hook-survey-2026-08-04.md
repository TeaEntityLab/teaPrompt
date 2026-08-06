# agnix + agent-skills-hook Survey — 2026-08-04

> **Status: decided (non-authoritative); external-survey panel record, no
> adoption.** Both targets are retained as study material only. agnix is
> additionally recommended to the user as an optional personal-workstation
> tool (pinned version), outside repository governance. No TeaPrompt skill,
> lens, verifier, dependency, or runtime surface was created or changed.
> `06-repo/AGENTS.md` and governed skill contracts remain authoritative; this
> record is evidence and a decision, not an operating rule.

## Purpose

Preserve the completed 7-lens survey of two external repositories so the
adoption questions are not re-litigated from chat memory: (1) whether agnix's
"444 evidence-backed rules" claim survives independent verification and what,
if anything, its provenance model teaches TeaPrompt; (2) whether
agent-skills-hook's tri-runtime skill distribution is safe to adopt, copy
from, or imitate.

## Target and Version

- Review target A: [`agent-sh/agnix`](https://github.com/agent-sh/agnix), checked 2026-08-04.
  Pinned: v0.45.0, commit `572a860971a18c48c7a830eb00cb411d5b87dd3f`
  (2026-08-01). Rust workspace (edition 2024, MSRV 1.91), six crates
  (core/rules/cli/lsp/mcp/wasm), 1159 commits, single primary author
  (Avi Fenesh). Dual-licensed MIT OR Apache-2.0, verified in root LICENSE
  files and every crate manifest (`license.workspace = true`) on 2026-08-04.
- Review target B: [`docevilOck/agent-skills-hook`](https://github.com/docevilOck/agent-skills-hook), checked 2026-08-04.
  Pinned: commit `116e26b85768277026e1b9646d3207451f21344b` (2026-08-04),
  untagged (0 releases), 348 commits. Chinese-language personal
  configuration + skills distribution repo for Claude Code / Codex CLI /
  OpenCode. **No top-level LICENSE**; 8 of 63 skill directories carry
  per-skill license files.
- Volatility trigger: both repos were active within 3 days of the check date;
  re-pin commit and re-verify rule counts, deploy-script behavior, and license
  posture before relying on any later revision.

## Panel Execution Mode

Method contract: `04-agent/workflow-recipes.md` §Parallel Lens Review with the
host `parallel-lens-review-packet` wrapper.

1. The merge owner ran a pre-panel verification pass: cloned both repos,
   captured commit/tag metadata, parsed `rules.json` (444 entries confirmed on
   disk), located the deploy scripts' backup logic, and identified the
   `npx -y context-mode` MCP dependency before writing the packet.
2. One shared packet was written to a repo-root transient path readable by
   subagents; it was deleted after synthesis. It separated observed /
   author-claimed / `[INFERENCE]` tiers and carried questions Q1–Q8.
3. The first fan-out of seven default-worker lenses all failed with provider
   `resource_exhausted` after ~10-minute retry spirals producing zero
   assistant output. Per the wrapper's quota-fallback guardrail the batch was
   refanned on the scout backend, which succeeded (task and scout run on
   different backends; five sibling workers were mid-flight when the first
   batch died, confirming burst-limit rather than hard quota).
4. Scout yields were schema-coerced into `{summary, files, architecture}`;
   full deliverables were recovered by DM-wake over IRC (4 of 6), transcript
   salvage of an in-transcript deliverable (1 of 6, strategy lens), and — for
   the provenance lens, which crashed twice without a verdict — raw session
   JSONL salvage of its 67 tool payloads (license texts, per-directory scans,
   web origin hunts) synthesized by the merge owner. Scouts also hit `EPERM`
   writing fallback files even under `/tmp`: scout sandboxes are read-only,
   so file-drop recovery paths are unavailable for that agent type.
5. The build/test reproduction slice was executed by the merge owner directly
   (coordinator-run commands, fable-method precedent): deterministic command
   evidence, not a judgment lens.
6. Two load-bearing provenance claims were hardened by the merge owner with
   local diffs against the user's own installed OMX skills (see Evidence
   Actually Checked). Role labels are review perspectives; no claim is made
   that distinct model providers were used. No reviewer edited the TeaPrompt
   repository or the clones.

## Lenses

| Lens | Load-bearing question | Main result | Verdict |
| --- | --- | --- | --- |
| Evidence auditor | Do the 444-rule claim, per-rule evidence URLs, and the Vercel citation hold? | 444 confirmed; 7 sampled rules across families all SUPPORTED with resolving URLs; README's flagship Vercel framing is a misrepresentation (0pp-improvement conflated with 0%-invocation); skills-hook has 63 skills on disk vs 61 claimed, all with SKILL.md | AGREE WITH CHANGES |
| Rust architecture | Is the data-driven rule engine sound? | rules.json → build.rs codegen → validator registry is compiler-enforced; parity tests pin rules.json↔implementation↔fixtures; zero production `unsafe`; fix confidence tiers (≥0.95 safe / ≥0.75 medium / <0.75 low); one systematic FP risk in CC-HK-008 script-path extraction | AGREE |
| Reproducibility (merge owner) | Does it build, test, self-lint, and eval as shipped? | All green: build exit 0; 5121 tests passed / 0 failed; self-lint "No issues found"; eval harness 61/61 cases, 100% P/R (self-regression fixtures, not an independent benchmark); cross-lint flagged 38 errors / 45 warnings / 11 info on agent-skills-hook | evidence only |
| Supply-chain & security | What executes on an adopter's machine? | agnix: SHA-pinned actions, sha256-verified npm installer, strict deny/audit, telemetry off by default (author-claimed). skills-hook: unpinned `npx -y context-mode` + `@tarquinen/opencode-dcp@latest`, unofficial `rayplus` proxy models in opencode.json, destroy-before-privilege-check on Windows, Linux claude block omits `~/.claude/agents` from backup and link | AGREE WITH CHANGES |
| Provenance & licensing | Original vs vendored; is redistribution clean? | Crashed twice; no independent verdict. Merge-owner synthesis of its salvaged evidence: Anthropic-proprietary LICENSE.txt (carried in 6 skills) expressly forbids redistribution; AGPL-3.0 and non-commercial licenses mixed in; OMX skills rebranded with markers stripped; repo itself unlicensed | (salvaged, no lens verdict) |
| Config & skill quality | Is the operating regime sound? | "Hook" is a misnomer — zero programmatic hooks, all prompt-text; per-turn forced skill evaluation and ctx_*-only execution deadlock when the unpinned MCP server is unavailable; ddev pipeline is well-formed but heavyweight; several agnix stylistic rules over-severe (CC-MEM-005 HIGH, CC-MEM-014/PE-006 MEDIUM) | AGREE WITH CHANGES |
| Strategic synthesis | What should TeaPrompt learn, per use case? | agnix: study yes, local personal deploy yes, repo adoption no (dependency boundary). skills-hook: concepts-only study; adopt/deploy never (license + supply chain + destructive installers). Steal-list reduced to concepts with falsifiers | AGREE WITH CHANGES |

## Panel Consensus

- **Decision:** `AGREE WITH CHANGES` (5 of 6 delivered lens verdicts; 1 clean
  AGREE; no DISAGREE; provenance lens crashed without a verdict and is
  represented by merge-owner synthesis over its salvaged raw evidence).
- **agnix:** mechanically what it claims — 444 rules confirmed on disk with
  per-rule `evidence{source_type, source_urls[], verified_on}` blocks,
  compiler-enforced parity, a green 5121-test suite, clean self-lint, and a
  working labeled eval harness. Its trust surface has the same failure mode
  the fable-method survey found: the README headline misrepresents its
  flagship citation while the underlying artifact is honest. `[INFERENCE]`
  The per-rule evidence model is the most transferable idea and directly
  rhymes with TeaPrompt's falsifier + "checked date" discipline.
- **agent-skills-hook:** a personal dotfiles-style distribution, not a
  product. Facially non-compliant redistribution: six skills carry Anthropic's
  proprietary LICENSE.txt whose own text forbids distribution and derivative
  works; `visual-verdict` and `ddev-clean` are OMX skills with the `[OMX]`
  origin markers stripped (ddev-clean additionally renamed into the repo's
  in-house ddev- family); the repo has no top-level license. Supply chain and
  installers add material risk (unpinned npx, `rayplus` proxy models,
  destroy-before-privilege-check). Under
  `04-agent/external-adoption-review.md` the boundary is strict: concepts
  only; never copy text, code, checklists, or file structure.
- **Panel-corrected packet fact:** the packet's observed "64 skill dirs" was
  wrong (a `README.md` miscount); ground truth is **63 skill directories**,
  each containing a SKILL.md, vs the README's claimed 61.

### Use-Case Recommendation

| Use case | agnix | agent-skills-hook |
| --- | --- | --- |
| `study` | **yes** — the rule-evidence schema, parity tests, and eval harness are reference-grade | **concepts only** — tri-runtime single-source layout and pre-deploy backup discipline; never copy content |
| `reproduce` | **yes** — build/test/self-lint/eval all reproduced locally in this survey | **no** — nothing to reproduce; deploy scripts are the artifact and they are the risk |
| `adopt` into TeaPrompt | **no** — a Rust binary gate violates the dependency-free methodology boundary; ledger AX3 rejected | **no** — unlicensed repo ⇒ no-copy rule; license violations observed in its own tree |
| `adopt` in user environment | **conditional yes** — as a personal, version-pinned config linter; treat stylistic severities skeptically (see Required Wording Changes 4) | **no** — destructive installers, unpinned supply chain, proxy-routed models |
| `deploy` (CI / fleet) | **conditional** — general audiences may gate agent-config repos on it; pin the version, triage severities, expect CC-HK-008-class false positives | **never** |

## Required Wording Changes

Upstream-facing candidates consolidated from the lenses. None was applied to
TeaPrompt or to either upstream repository by this review.

1. **agnix README Vercel row:** "Vercel's research found skills invoke at 0%
   without correct syntax. One wrong field and your skill is invisible" must
   become wording of the form "Vercel found default-configured skills
   produced 0pp improvement over baseline because the agent never invoked
   them in 56% of cases; correct syntax is a prerequisite for
   discoverability, not the failure Vercel measured." The blog attributes
   non-invocation to model tool-selection limits; the words "syntax",
   "wrong field", and "invisible" do not appear in it (checked 2026-08-04).
2. **agnix severity calibration:** CC-MEM-005 (generic-instruction detection)
   HIGH→LOW; CC-MEM-014 (CLAUDE.md line limit) MEDIUM→LOW; PE-006
   (negative-only instructions) MEDIUM→LOW. Stylistic lints at structural
   severities train users to ignore the linter.
3. **agnix CC-HK-008:** restrict script-path extraction to executable
   positions instead of any extension-matching token; `grep 'main.py' log`
   currently manufactures a missing-script diagnostic.
4. **skills-hook README:** "61 个技能" → 63; and rename or re-describe the
   repo — it ships zero hooks; enforcement is prompt-text only.
5. **skills-hook licensing:** add a top-level LICENSE; remove or obtain
   authorization for the six Anthropic-proprietary skill copies; restore
   upstream attribution on the OMX-derived `visual-verdict` and `ddev-clean`;
   surface the AGPL-3.0 (guizang-ppt-skill) and non-commercial (mediacrawler)
   grants in the README so consumers see the mixed obligations.
6. **skills-hook installers:** pre-flight privilege check before any
   destructive operation in `windows/deploy.ps1`; add `~/.claude/agents` to
   the Linux backup+link path to match the Windows block; pin `context-mode`
   and `@tarquinen/opencode-dcp` versions; disclose the `rayplus` proxy
   routing.

## Candidate Adoption Ledger

| ID | Candidate | Status | Evidence | Next action / trigger |
| --- | --- | --- | --- | --- |
| AX1 | Per-rule machine-checkable provenance (`evidence{source_urls, verified_on}`) mirrored into TeaPrompt skill/prompt contracts | Concept-only 2026-08-04 — no artifact change | agnix rules.json observed; TeaPrompt already enforces record-level "checked <date>" via `validate_record_hygiene.py` and link liveness via `validate_links.py`; no verified per-contract gap | Reconsider if a TeaPrompt lens/rule is found citing an external behavior claim with no checkable date, or a quarterly link pass finds systemic drift; falsifier: the fields rot into unmaintained boilerplate |
| AX2 | Labeled expected-vs-actual eval manifests (agnix `eval`) for TeaPrompt routing/skill checks | No-change 2026-08-04 | TeaPrompt ROUTE-002/003 fixtures + `validate_route_fixture.py` already implement expected-vs-actual labeling; external concordance is pressure, not local recurrence (`external-adoption-review.md` §5) | Revisit only if a new eval class (e.g. per-skill fixture efficacy) emerges that ROUTE fixtures cannot express |
| AX3 | agnix binary as a TeaPrompt repository CI gate or dependency | Rejected 2026-08-04 | Violates the dependency-free, host-agnostic methodology boundary; TeaPrompt skills are method contracts, not host configs; user-side use stays personal and outside governance | Re-litigate only if TeaPrompt ever ships host-specific config artifacts as first-class deliverables |
| SH1 | Tri-runtime single-source symlink distribution to replace `SKILL_INSTALLATION.md` manual copies | Deferred — current no-change | skills-hook layout observed working for three runtimes; risk: live-linked files leak local edits/credentials into the tracked repo (strategy-lens falsifier); no observed local drift failure from manual copies yet | Reconsider on first observed stale-copy failure attributable to manual installation; falsifier: a leak or accidental commit through a live link |
| SH2 | Timestamped pre-deploy backup discipline for any future TeaPrompt install tooling | Concept-only 2026-08-04 | skills-hook `deploy.sh` backs up each target to `~/.<runtime>-backups/<stamp>` before destructive linking (observed); TeaPrompt ships no installer today | Apply if TeaPrompt ever ships install automation; falsifier: an installer lands without backup-before-destroy and nobody objects |

No candidate created a new TeaPrompt skill, lens, verifier, dependency, or
runtime surface. Deterministic guard for this record:
`plans/tests/test_agnix_agent_skills_hook_survey_record.py`.

## Shared Findings

### What agnix does well

1. **Evidence-per-rule as a first-class schema.** Every rule carries
   `source_type`, `source_urls[]`, and `verified_on`; all 7 sampled rules'
   URLs resolved and supported the rule as written (checked 2026-08-04).
2. **Compiler-enforced rule parity.** `build.rs` validates and codegens the
   rule DB; `parity.rs` pins the two rules.json copies and counts;
   `rule_parity.rs` scans source for every rule ID and requires a fixture per
   rule — an undocumented or unimplemented rule fails the build/tests.
3. **Reproducibility as shipped.** Build exit 0; 5121/0 tests; self-lint
   clean; eval 61/61. The panel's exact commands are in Evidence Actually
   Checked.
4. **Supply-chain hygiene.** SHA-pinned GitHub Actions, sha256-verified npm
   installer, `deny.toml` multiple-versions deny, zero production `unsafe`.
5. **Working editor/CI surface area** (author-claimed beyond the CLI): LSP,
   MCP server, WASM playground, four editor extensions, GitHub Action.

### Load-bearing gaps (agnix)

1. The README's flagship citation is marketing drift over an honest artifact
   (same asymmetry the fable-method survey found in its README table).
2. Severity calibration treats style as structure (CC-MEM-005 et al.).
3. CC-HK-008 extension-scraping produces systematic false positives.
4. `learn.chatgpt.com`, cited as an authority for several AGM-*/XP-* rules,
   is not an official OpenAI domain; authority status unverified (checked
   2026-08-04).
5. The eval harness's 100% P/R is self-referential (its own labeled
   fixtures) — a regression floor, not an external benchmark.

### What agent-skills-hook does well

1. **Single-source, three-runtime distribution** with per-target timestamped
   backups before destructive linking (Linux block, observed).
2. **A coherent, opinionated spec-driven pipeline** (ddev-*: arch → spec →
   detail → plan → exec → gate) with concrete artifacts and phase gates.
3. **An honest engineering culture in prose**: root-cause-not-symptom rules,
   `ponytail:` known-ceiling markers, verification-before-completion norms.

### Load-bearing gaps (agent-skills-hook)

1. **License posture is disqualifying for reuse.** No top-level LICENSE; six
   Anthropic-proprietary skills whose carried license forbids redistribution
   and derivatives; AGPL-3.0 and non-commercial grants mixed in silently;
   OMX skills de-branded (`[OMX]` markers stripped; `ddev-clean` renamed from
   `ai-slop-cleaner` into the in-house family).
2. **Supply chain is load-bearing and unpinned:** every deployed session
   depends on `npx -y context-mode` (Elastic License 2.0, single-author npm
   package) because the config forbids most Bash; `@tarquinen/opencode-dcp@latest`;
   `rayplus/gpt-5.4*` proxy models route prompts through an unofficial
   gateway (`[INFERENCE]` on endpoint behavior — config observed, traffic not
   tested).
3. **Installers can destroy data:** Windows deletes configs before the
   privilege check that link creation needs; Linux omits `~/.claude/agents`
   from both backup and link, silently diverging from the Windows block.
4. **The name is a misnomer:** zero hook-based enforcement exists; the entire
   regime is prompt text, so every "强制" (forced) rule is advisory under
   pressure and deadlocks when the mandated MCP tools are absent.

## Evidence vs Inference

| Claim | Status | Basis |
| --- | --- | --- |
| agnix 444 rules; per-rule evidence schema; v0.45.0 identity | Observed / verified | rules.json parsed locally; git metadata from pinned clone, checked 2026-08-04 |
| agnix builds, tests pass (5121/0), self-lint clean, eval 61/61 | Observed / executed | Merge-owner commands, this survey, 2026-08-04 |
| 7 sampled rule evidence URLs resolve and support their rules | Observed / verified | Evidence-lens fetches, checked 2026-08-04 |
| agnix README misrepresents the Vercel result | Observed / verified | Blog text vs README text compared; quotes in lens deliverable, checked 2026-08-04 |
| skills-hook: 63 skills, all with SKILL.md; README claims 61 | Observed / verified | Directory scan (two independent lenses + salvaged payload) |
| Anthropic LICENSE.txt in docx/pdf/pptx/xlsx forbids redistribution | Observed / verified | Full license text salvaged from provenance-lens session log; also present in clone |
| `visual-verdict` = OMX skill with `[OMX]` stripped; `ddev-clean` = OMX `ai-slop-cleaner` renamed | Observed / verified | Merge-owner `diff` against the user's installed `~/.codex/skills` copies, 2026-08-04 |
| `rayplus` proxy exposes prompts/keys to an intermediary | `[INFERENCE]` | opencode.json model entries observed; endpoint behavior not exercised |
| context-mode/codegraph package metadata (authors, licenses) | Observed via web lookups | Supply-chain lens, checked 2026-08-04; registry state is volatile |
| Whether upstream Anthropic re-licensed these skills elsewhere permissively | Unknown | Not determinable from the vendored copies; carried text governs the copies as shipped |
| skills-hook forced-eval regime burns tokens and deadlocks without ctx_* | `[INFERENCE]` | Config text observed; runtime behavior not measured |

## Disagreements / Residual Risks

- One lens returned clean AGREE (Rust architecture) vs five AGREE WITH
  CHANGES; no material contradiction — its scope simply had no wording stake.
- The provenance slice carries no independent lens verdict (double crash);
  its facts above are merge-owner-synthesized from salvaged raw payloads and
  two local diffs. Residual risk: classification counts for all 63 skills
  (original vs vendored) were not completed to a full table; the six
  Anthropic copies, two OMX copies, AGPL and non-commercial grants are
  individually verified, the remainder is spot-checked only.
- Severity-calibration recommendations are judgment-tier, not defects.
- The `rayplus` privacy risk and the forced-eval token-cost claim remain
  inference; both are falsifiable by instrumenting a deployed session.
- Requested lens routing: the first batch's provider identity is evidenced
  only by failure symmetry (7/7 `resource_exhausted`); no provider identity
  claims are made for either backend.

## Evidence Actually Checked

- `git clone` both repos; `git log -1 --format='%H %ci %s'`, `git tag` — pins
  above (2026-08-04).
- `python3` parse of `crates/agnix-rules/rules.json` — 444 entries,
  schema keys, sample rule AGM-001.
- `cargo build --workspace` (exit 0); `cargo test --workspace` — **5121
  passed, 0 failed** (re-run confirmed); `./target/debug/agnix .` — "No
  issues found", exit 0; `./target/debug/agnix <skills-hook clone>` — 38
  errors / 45 warnings / 11 info, 33 auto-fixable; `agnix eval
  tests/eval.yaml` — "SUCCESS All 61 cases passed", exit 0. All on the pinned
  clones, 2026-08-04.
- `diff ~/.codex/skills/visual-verdict/SKILL.md <clone>/agents/skills/visual-verdict/SKILL.md`
  — 2 hunks: `[OMX]` stripped, `.omx/state/...` path genericized; 76 lines
  both. Same procedure for `ai-slop-cleaner` → `ddev-clean` (renamed,
  de-branded, lightly edited).
- Salvaged provenance payloads (67 tool outputs from the crashed lens's
  session log): full Anthropic LICENSE.txt text, AGPL-3.0 (guizang-ppt-skill),
  NON-COMMERCIAL LEARNING LICENSE 1.1 (mediacrawler), per-directory
  SKILL.md/license scan, agnix per-crate license fields (all
  `MIT OR Apache-2.0`), no NOTICE/vendored-content hits, empty
  `agent-knowledge` submodule.
- Lens web fetches (evidence + supply-chain): 7 rule-evidence URL checks, the
  Vercel blog, npm metadata for `context-mode` and `@colbymchenry/codegraph`
  (all checked 2026-08-04).
- Not verified: editor extensions and WASM playground behavior; npm wrapper
  end-to-end install; `rayplus` endpoint traffic; Windows deploy execution
  (static read only); full 63-skill origin table.

## Falsifiability

- The agnix verdict is wrong if a later pinned revision shows the parity
  tests do not actually gate unimplemented rules, if the sampled evidence
  URLs were unrepresentative (a fuller audit finds systemic dead or
  unsupportive citations), or if the misrepresented Vercel row is shown to be
  an accurate paraphrase of a different Vercel publication.
- The agent-skills-hook verdict is wrong if the repository produces
  authorization for the Anthropic-proprietary copies and restores upstream
  attribution (the license finding would then be repaired, not refuted), or
  if the carried Anthropic LICENSE.txt is shown to be superseded by a
  permissive upstream grant covering exactly these files.
- The ledger is dead text if AX1/SH1 triggers fire and no re-evaluation
  happens, or if a candidate ships without its recorded trigger — that is the
  drift this record's guard exists to catch.

Guard: `plans/tests/test_agnix_agent_skills_hook_survey_record.py`.
