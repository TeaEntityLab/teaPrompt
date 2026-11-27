# Reliability Panel Follow-Through (2026-11-27)

Language: English
> **Status:** in progress. Owner direction, 2026-11-27: "1、2、3 先做 然後其它接著作" — carry out all five proposals from the 2026-11-27 reliability panel, items 1–3 first. Item 1 is preregistered below and was committed before its first model call.

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

## Candidate Adoption Ledger

| ID | Candidate | Disposition | Next decision |
| --- | --- | --- | --- |
| RFT-1 | State-observable twin-sweep cell | Preregistered 2026-11-27 | Canary, ten runs, blind scoring under the rule above |
| RFT-2 | Commit-pinned skill installs plus installed-state verifier | In progress 2026-11-27 | Tooling tests, then converting host installs |
| RFT-3 | Route-eval `>=` minimums, cheatsheet de-leak, independent ROUTE-004 holdout | In progress 2026-11-27 | Guard, de-leak and holdout integration |
| RFT-4 | Precedence between global user rules and skills | Owner-approved, pending | Dispatch wording and guard |
| RFT-5 | Decision Index split and entry-length cap | Owner-approved, pending | Split entry and validator guard |

## Standing Non-Goals

- No new skill, pack, runtime or route. Core stays nine and the registry stays ten.
- No unit deletion or skill-text change follows from RFT-1 without a separate owner decision.
- No push follows from this record; a push needs its own authorization.
