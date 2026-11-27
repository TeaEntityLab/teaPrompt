# Reliability Panel Follow-Through (2026-11-27)

Language: English
> **Status:** delivered. Owner direction, 2026-11-27: "1、2、3 先做 然後其它接著作" — carry out all five proposals from the 2026-11-27 reliability panel, items 1–3 first. The state-observable cell completed under its preregistered rule with amendment A1; items 2–5 are implemented and verified below. Local commits only; no push.

## Source

On 2026-11-27, a five-lens read-only panel assessed the project's tests and Skills: methodologist, test-oracle engineer, practitioner, runtime-trust reviewer and skeptic. All five lenses came from one model family, so they form a single epistemic channel. The coordinator verified the load-bearing claims with deterministic scripts:

- Only 7 of 114 test modules (153 of 953 static test functions) execute behavior; about 770 assertions pin wording or record state.
- ROUTE-002/003 minimum-count guards used `==`.
- 46 of 374 route-fixture phrases appeared verbatim in the English cheatsheet.
- Four host skill roots held live symlinks into the working tree, and no test observed installed state.
- Global user rules (`[cx]` mandates, host routing hooks) had no stated precedence relative to the skills.
- The 2026-11-26 Decision Index entry had grown into one multi-topic paragraph.

One lens claim was refuted: the injected skill list did not carry X4b's deleted units (0 of 12 appear in skill descriptions).

## Item 1: State-Observable Twin-Sweep Cell (Preregistered 2026-11-27)

**Question.** Does `reflective-implement`'s twin-sweep bullet (X4b unit U05) change what an agent *does*, not only what it writes? X4b separated its arms only at the wording level (C 3/3 versus T 0/3 on a `TWINS:` predicate), and its fixtures were text-only. This cell uses a file-state observable instead: hidden tests run against the workspace the agent leaves behind.

**Arms.** C is the current `reflective-implement/SKILL.md` (SHA-256 `bb93faf71378747bd769787b20277ad5bf5bbaa93a586959921b99e608a79d18`). T is the same text minus exactly the 514-character twin-sweep line, the frozen X4b U05 text. The two prompts differ only by that line, and T contains no other twin-sweep cue.

**Fixture.** A six-file Python package, `shop`. `ISSUE.md` reports one bug: `unit_price_cents` truncates instead of rounding to the nearest cent, as `docs/finance.md` requires. The same money-truncation construct appears in `tax_cents` and `per_item_shipping_cents` (in-scope twins under the finance rule). A decoy, `full_boxes`, truncates correctly, because a partial box is not a box. The task names only the reported bug and states that shell commands cannot run.

**Primary endpoint.** Hidden tests H1–H5 all pass on the final workspace:

- H1: reported function fixed.
- H2, H3: both twins fixed.
- H4: decoy intact.
- H5: unchanged helpers still behave.

The scorer rebuilds the package in memory from a workspace snapshot under the frozen read-only scorer sandbox. Candidates are scored through the unchanged arm-blinded scaffold.

**Calibration before any run.** Six hand-written snapshots scored as intended:

- Original fixture, reported-only fix, decoy over-fix and syntax error fail.
- Full fix and refactor into a shared rounding helper pass.

**Secondary endpoints** (descriptive): per-check passes, runs with any search tool call, runs searching for the `int(` construct, runs whose final report has a `TWINS:` line, changed-file count, and protocol deviations.

**Recipe and boundary.**

- Recipe: `cursor-agent` 2026.11.22-e9042b2 with `grok-4.7-medium` in agent mode (no `--mode ask`, so it can edit), `--sandbox disabled`, `--trust`, stream-json. It is launched through the pinned shell-free launcher.
- The per-job `sandbox-exec` profile keeps the X4b continuation boundary with two deliberate changes: the fixture workspace is writable, and every skill root is unreadable, so no injected skill list can carry the unit.
- No shell, no binary outside the CLI install except the keychain helper, no localhost, and no reads of user files outside CLI state.
- Shell, web, MCP and task tool calls are protocol deviations: recorded, not invalidating.

**Envelope.** At most 11 model requests: one tool-using qualification canary plus 2 arms × 5 runs in a seeded shuffle (`state-cell-2026-11-27`), run sequentially, with no automatic retry and a 900 s timeout per run. No credits, overage or paid add-on.

**Validity and stops.**

- Invalid: timeout, nonzero exit, no successful result, empty final text, or the model not reported as `Grok 4.7 … Medium`.
- Stop: quota signal, model drift, harness failure, or any kernel sandbox denial outside the expected set frozen after the canary.

**Decision rule.** Only complete pairs are analyzed. With c and t the primary passes and n the complete pairs:

- fewer than 4 complete pairs, or invalid counts differing between arms by 2 or more: **inconclusive (missingness)**
- two-sided Fisher exact p ≤ 0.05 with c > t: **behavioral effect detected** on this fixture and model
- p ≤ 0.05 with t > c: **reverse effect detected**
- otherwise, both arms ≥ n−1: **ceiling** (fixture insensitive)
- otherwise, both arms ≤ 1: **floor**
- otherwise: **inconclusive at this n**

At n=5 only large differences can reach p ≤ 0.05: 5 versus 0 (p≈0.008), and 5 versus 1 or 4 versus 0 (p≈0.048). No skill change follows automatically from any outcome.

**Frozen artifacts.**

- Session-private `state-cell-2026-11-27/manifest.json`, SHA-256 `f3de661b49be53186347790119236e714290260906fef37af6e83bd243233cf0`.
- It pins the fixture, scorer, scorer launcher and sandbox, scaffold, both contracts, all prompts, runner, analysis and boundary builder, plus the pinned launcher, original pilot runner and CLI bundles.

**Sequencing rule.** No further text-only efficacy cohort runs before this cell reports. A text-only cohort can show only that wording changes emitted text.

### Amendment A1 (owner-approved 2026-11-27, before any scored run)

**Trigger.** Canary `cell-canary-1` reached the model, which was reported as `Grok 4.7 256K Medium`. It made glob, read and edit calls, and its edit landed: `note.txt` became `status: final`. The CLI then hung until the 960 s kill. After each write, the CLI records AI-code tracking in `~/.cursor/ai-tracking/ai-code-tracking.db`, which the boundary keeps unreadable. The SQLite open failure surfaced as an uncaught exception, so the write tool's tracking promise never settled. The preregistered stop rule (harness failure) fired after 1 of 11 requests, before any run was dispatched.

**Owner answer** (form, 2026-11-27): `redirect`. Changes:

- A `NODE_OPTIONS` preload, `tracking_redirect.cjs`, rewrites only paths under `~/.cursor/ai-tracking` into the job temp dir. A zero-inference check inside the boundary showed three things: the redirected database opened, wrote and closed; the real database still returned `EPERM`; unrelated paths were unchanged. A network-denied dry run with the preload hit the same denial classes as the original dry run.
- The stream parser counts only `*ToolCall` keys as tool kinds. Keys such as `toolCallId`, `startedAtMs` and hook contexts are recorded separately as metadata. Only descriptive counts are affected.
- One replacement canary raises the request cap to 12. If it fails, the cell stops and is recorded as held.
- Correction to the envelope above: the runner's hard timeout is 960 s, a 900 s budget plus 60 s grace.

The manifest was re-frozen as SHA-256 `67cd250aaadc8d7c7889e321c319cbc97aa8372b23a5c2e147293c38ce992491` (30 files). Its amendment entry keeps the prior hash.

**Replacement canary.** `cell-canary-2` qualified. It exited 0 in 13.2 s, was reported as `Grok 4.7 256K Medium`, and made glob, read and edit calls. `note.txt` changed, and the tracking database appeared in the redirected directory. The expected-denial set was then frozen: 14 rules (SHA-256 `b521426f9e962002370edc9fde833200b3c212fd48b7a050f8fc20f2aab363bd`). They cover every canary-2 denial and every canary-1 class except the tracking-database read, which stays unexpected so a failed redirect stops the series. The manifest was re-frozen as `961c2cab8935cc6ec1e0e0148eb58b84ae916d6347f275e6de711b07ee1a7e4e` (31 files).

### Completed Cell Outcome (2026-11-27)

All ten seeded runs were valid, with five complete pairs, the same reported `Grok 4.7 256K Medium` model and no unexpected sandbox denials. The frozen scaffold scored ten label-stripped workspace snapshots. All primary labels were identical, so the two candidates selected by the frozen blind stage were read in full and an audit was sealed before opening the arm map. Their unchanged tax and shipping truncation supported the failing twin checks; the scorer, fixtures and scores were not changed.

The preregistered disposition is **floor (fixture too hard or recipe defect)**: C 0/5, T 0/5; two-sided Fisher p = 1.0. Each arm's Wilson 95% interval is [0, 0.434].

| Endpoint | C: full skill | T: twin-sweep line deleted |
| --- | --- | --- |
| Valid runs | 5/5 | 5/5 |
| Primary: H1–H5 all pass | 0/5 | 0/5 |
| H1: reported bug fixed | 5/5 | 5/5 |
| H2: tax twin fixed | 0/5 | 0/5 |
| H3: shipping twin fixed | 0/5 | 0/5 |
| H4: packing decoy intact | 5/5 | 5/5 |
| H5: unchanged helpers pass | 5/5 | 5/5 |
| Any search call | 5/5 | 5/5 |
| Search for the `int(` construct | 4/5 | 0/5 |
| Final text has `TWINS:` | 5/5 | 0/5 |
| Runs with protocol deviation | 2/5 | 4/5 |
| Median changed-file count | 2 | 2 |

Every run changed only `shop/pricing.py` and `tests/test_pricing.py`. Deviations were `getMcpToolsToolCall` queries; they were retained as prescribed, not removed after seeing outcomes. The search and report differences are descriptive secondary outcomes, not a selected efficacy claim. The primary result does not establish that the line is inert, justify its deletion, or generalize beyond this fixture, recipe and model.

There were 12 model-bearing CLI invocations, including the failed first canary and the qualified replacement, with no automatic retry. The opaque CLI's provider-internal request counts and quota debits were not independently audited. Frozen-file verification checked 31 local and five external files with zero mismatches. Session-private receipts remain under `state-cell-2026-11-27/`; the delivery evidence ledger pins every run receipt.

| Artifact | SHA-256 |
| --- | --- |
| Final manifest | `961c2cab8935cc6ec1e0e0148eb58b84ae916d6347f275e6de711b07ee1a7e4e` |
| Blind audit, sealed before unblinding | `b033b7177910f63e47e74f82959ed968f2ee3066bcfc734a18c0bf7186efe5fd` |
| Blinded score receipts | `32b5152336aa361fcc734fb10b272e721b1327e7f869ec2fd131dd9dd1746c74` |
| Unblinded result | `d9ea68efade30b04cc1006966021c73135ad4618450d9d97f8571829a67bac0d` |

## Item 2: Commit-Pinned Installs

`SKILL_INSTALLATION.md` keeps one maintained shell helper, `install_skills_pinned <destination> <rev> <entry>...`. It extracts committed bytes, never working-tree bytes, and stamps each entry in `.teaprompt-pins.tsv`. Unknown entries and unpinned real paths are refused before replacement. Each replacement stages the entry and restores its predecessor if the manifest update fails.

`plans/verify_installed_skills.py` is a read-only, stdlib-only verifier. It checks stamped entries against their recorded commit for tampering and against `HEAD`'s entry tree for staleness. It follows aliases to pinned entries; live or dangling TeaPrompt links fail. Unstamped real copies and unrelated entries are not identifiable as TeaPrompt installs and are ignored. This is installed-byte provenance, not evidence that a host obeyed the skill.

The installer/verifier consumer tests passed (23 tests). Tooling and delivered skill bytes were committed as `b50706993f385f694cf9859037539d3c178644cf`, then 111 direct repository symlinks were replaced with copies pinned to that commit. Unrelated entries and aliases to shared install roots stayed untouched. `make verify-installed` exited 0: 118 entries verified, including seven aliases, with no failures.

| Install root | Direct replacements | Verified entries |
| --- | --- | --- |
| `~/.agents/skills` | 23 | 23 |
| `~/.cursor/skills` | 23 | 23 |
| `~/.claude/skills` | 23 | 23 |
| `~/.codex/skills` | 23 | 23 |
| `~/.gemini/antigravity/skills` | 18 | 18 |
| `~/.gemini/skills` | 1 | 8 |
| `~/.grok/skills` | 0 | 0 |

The verifier ignored 143 non-TeaPrompt or unstamped entries. The session-private conversion inventory preserves every original direct link for rollback; a separate receipt records each root's successful helper exit. None of the 118 verified TeaPrompt entries resolves into the working tree. These receipts do not show host-agent compliance.

## Item 3: Routing Measurement Repair

- ROUTE-002/003 count guards now use `>=`, preserving minimum coverage without forbidding expansion. ROUTE-001's existing count contract is unchanged.
- The English cheatsheet had 46 verbatim matches against the 374 ROUTE-001/002/003 phrases; zh-TW had 9. Both now have 0. Boundary guidance remains, without requiring the eval phrases themselves. R8 and its anti-leak checks also cover every `skills/*/SKILL.md`.
- ROUTE-004 was written from only the nine core skill descriptions and independently labeled by a second agent. All 63 labels agreed; both agents belong to the same model family, so this is procedural separation, not independent epistemic evidence.
- The unchanged router matched 35/63 (55.6%). No router keyword, fixture phrase or label was changed to improve it. `make route-holdout` exposes the measurement outside `all`; pytest guards the pre-tuning floor and keeps its phrases out of routed surfaces, router code and other fixtures. Once used to tune a router, it is no longer an untouched holdout.
- Actual CLI observation: the 55.6% score exceeds its configured 55% threshold and trace coverage is 100%, but the evaluator classified ten mismatches as `silent_downgrade_incidents`. That separate hard gate makes the underlying evaluator exit 1. The report-only Makefile target intentionally ignores that exit; it is not a passing ROUTE-004 acceptance result. The CLI's generic failure line incorrectly describes the cause as score below threshold. These policy-gate findings are retained without tuning the router, weakening the gate or changing the held-out phrases.

## Items 4–5: Precedence and Index Growth

- `reflective-dispatch/SKILL.md` now states that higher-authority instructions and applicable global user rules/host routing take precedence, while non-conflicting duties remain. The yielding clause is named in a trace or report. Standing rules and host routing still do not grant outward-action authorization. No exact-paragraph adoption pin was added: this is prompt guidance, not demonstrated host enforcement.
- The overloaded November Decision Index entry was split into X4b, skills × survey rethink, and survey-series pointers. Existing facts and links remain in the owning records.
- `validate_project_knowledge.py` caps entries dated from 2026-11-01 at 1,000 characters. Earlier entries are grandfathered. Tests cover an oversized current entry failing, an oversized older entry passing, and a current in-cap entry passing.

## Verification Ledger

| Consumer class | Status | Evidence / boundary |
| --- | --- | --- |
| Installer and installed-state verifier | Verified | 23 isolated consumer tests; 111 direct links converted; 118 installed entries verified |
| Routing floors, cheatsheets and skill surfaces | Verified | Included in the 140-test focused pass; seeded ROUTE-001/002/003 remain 100% |
| Independent holdout | Verified, bounded | 35/63 without router tuning; guard and anti-leak tests passed |
| Dispatch precedence | Delivered wording | No live-host precedence or compliance claim |
| Decision Index and validator | Verified | Split entries and cap behavior included in the focused pass |
| Generated metadata and publication gates | Code gate verified | Index regenerated (280 files); `make all` passed with 1,802 tests; the final doc-only publication receipt is retained in the session delivery ledger |

The 140-test focused pass used Python 3.13. The first full pytest attempt stopped on documentation drift: 1,802 tests were collected but `QUALITY_GATES_SUMMARY.md` still stated a 1,776 floor. The documented floor was corrected to 1,802; no oracle was weakened.

After the floor correction, `PYENV_VERSION=3.13.0 PYTHONDONTWRITEBYTECODE=1 make all` exited 0: 1,802 passed in 166.13 s, 340 files link-checked with zero errors, all validators passed, and ROUTE-001/002/003 remained 100%. Record hygiene retained its pre-existing 373 warnings. The final documentation edits receive a focused publication check rather than another full suite.

## Evidence vs Inference

- **Verified:** the panel counts under Source were re-derived by deterministic scripts. All six calibration snapshots scored as intended. The A1 zero-inference checks, qualified replacement, ten valid run receipts and frozen blind scoring were observed. Installed-state verification passed after conversion.
- **[INFERENCE]:** the A1 hang mechanism is read from the CLI bundle and the canary session log: an uncaught `SQLITE_CANTOPEN`, while the write path awaits tracking. The qualified replacement supports the diagnosis. A redirected tracking database is assumed not to change model-visible behavior, because tracking is post-write bookkeeping the model never sees.
- **Unknown:** whether the primary floor is fixture difficulty, another recipe effect or a broader repair-scope limitation; whether either primary or secondary result transfers to another fixture, host or model. Provider-internal request counts and quota debits remain unaudited.

## Falsifiability

- A1 is refuted if the replacement canary hangs again, or if its edit leaves no database in the redirected directory.
- Every RFT-1 disposition is fixed by the decision rule before data. Only the primary endpoint can establish the preregistered repair-state effect; secondary search/report differences remain descriptive. A floor does not show the line is inert elsewhere.
- RFT-3's ROUTE-004 score is meaningful only while no router change is tuned against it.
- RFT-5 fails if a Decision Index entry dated from 2026-11-01 exceeds the cap and the validator still passes.

## Candidate Adoption Ledger

| ID | Candidate | Disposition | Next decision |
| --- | --- | --- | --- |
| RFT-1 | State-observable twin-sweep cell | Completed: five complete pairs; primary C 0/5, T 0/5; preregistered floor | No line deletion, new cohort or broader efficacy claim follows |
| RFT-2 | Commit-pinned skill installs plus installed-state verifier | Delivered and verified; 111 direct links converted to `b50706993f` | Re-pin deliberately when skill bytes change; verifier detects stale or tampered entries |
| RFT-3 | Route-eval `>=` minimums, cheatsheet de-leak, independent ROUTE-004 holdout | Delivered and verified | Keep ROUTE-004 untuned; 35/63 is a bounded measurement |
| RFT-4 | Precedence between global user rules and skills | Delivered in dispatch | No host-enforcement or methodology-efficacy claim |
| RFT-5 | Decision Index split and entry-length cap | Delivered and verified | Keep dated entries map-sized |

## Standing Non-Goals

- No new skill, pack, runtime or route. Core stays nine and the registry stays ten.
- No unit deletion or skill-text change follows from RFT-1 without a separate owner decision.
- No push follows from this record; a push needs its own authorization.
