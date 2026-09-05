# agentflow — Survey and Comparison Record — 2026-09-05

> **Status: decided (record-only), guarded, and verified.** Seven-lens Parallel Lens Review of `agfnow/agentflow` pinned at `b2935f5381d6469243440e080b43d0092a591663` (2026-09-04) against TeaPrompt's skills and doctrine. Outcome: **no in-place wording adopted**; findings and comparisons recorded; nothing installed or depended upon. Authority chain unchanged: `06-repo/AGENTS.md` and the invoked `SKILL.md` contracts govern; this record is evidence and design judgement, not an operating rule. TeaPrompt operates no notebook protocol, Stop hook, pre-commit guard, external runner, or looper.

## Research Question

User instruction: *"Survey this project https://github.com/agfnow/agentflow — record your findings and comparisons."* (repository checked 2026-09-05). What is agentflow, what may a reader rely on, how does it compare with TeaPrompt axis by axis, and does any of it expose a verified local gap that warrants wording?

## Direct Recommendation (as of 2026-09-05)

**Study yes; reproduce partial (unit tests) / blocked (everything else); adopt no; deploy blocked.**

agentflow is a **peer methodology with an attached host harness** — not a TeaPrompt competitor and not a TeaPrompt host. It fuses in one skill what TeaPrompt deliberately splits: the methodology (route, evidence discipline, human authority, minimality) and the operationalization (a `devlog.md` notebook as the owner conversation and recovery surface, Stop-hook and pre-commit referees, an `external-runner-v1` that runs every delegated task in an independent no-remote Git clone with bounded output, a looper with a real-provider live gate, worktree streams). Its methodology is convergent with TeaPrompt's on every axis checked: the transcript is not the record; a model or worker verdict is a proposal, never acceptance; humans own irreversible decisions; "exit zero is not acceptance"; reject concepts that name no owner outcome or reproduced failure.

What agentflow has that TeaPrompt does not is the operational layer, and it is honest about that layer's limits ("the clone is not an OS sandbox"; inherited credentials, network, and absolute-path writes remain). What TeaPrompt has that agentflow does not is a mechanically guarded provenance model: ledger IDs, deterministic adoption-state tests, and Adoption Guard Closure. agentflow's inline `— I-NNN` incident citations are a different encoding of the same need, and the public tree shows the encoding is incomplete (18 of 73 incidents cited inline). Neither side's mechanism is a gap in the other; they are two products.

The single most useful thing in the repository for a TeaPrompt reader is the **incident ledger as a cost accounting of operationalization**: 73 failures in three weeks (2026-08-14 → 2026-09-04) that TeaPrompt has only asserted — a terminal one-liner rule that produced twenty false statements (I-028), a compression pass that dropped a load-bearing count (I-038), reviewers spawning reviewers (I-072), worker numbers as non-evidence (I-008, I-047), a false "sandboxed by design" claim (I-033). Read as evidence for the Durable Lesson "prompt wording cannot fix execution-layer failures", not as a template.

## Panel Consensus

- **Decision:** `AGREE` **7 of 7** (record-only). No `AGREE WITH CHANGES`, no `DISAGREE`. Unanimous on: no in-place wording; AF-9 and AF-14 rejected; AF-6/7/8/11 record-only; AF-1–AF-5 narrowed from the coordinator's "absorb" priors to record-only or no-change.
- **Reason tally (per the 2026-09-05 reason-concordance rule):** all seven `AGREE` verdicts rested on the same two reasons — (a) every transferable invariant is already held by a named TeaPrompt surface, and (b) the remaining agentflow mechanisms are operationalization that a policy library must name, never own. No lens agreed for a divergent reason; the verdict split and reason split coincide.
- **Recovery disclosure:** all seven lenses were run on the `task` backend directly (the `scout` backend crashed at startup in the previous panel); **7/7 delivered complete §-shape reviews over the hub**; structured yields were again coerced to short JSON. Same-host role labels; no provider persona or model routing is claimed.
- **Use-case recommendation:**
  - `study` — **yes**: the notebook protocol, runner, and incident ledger as a host-harness case study.
  - `reproduce` — **partial**: unit tests and clone-independence mechanics reproduced by the coordinator; hooks, looper live gate, providers, and `npx` install need a host; the private source repo, `eval/`, and `release/` are unreachable.
  - `adopt` — **no**: no verified load-bearing local gap; recurrence `unknown`.
  - `deploy` — **blocked**: Standing Non-Goal; supply-chain shape (unpinned `npx skills add`, auto-updating plugin channel, hook and git-hook writes on first use).

## Required Wording Changes (final)

**None.** No TeaPrompt skill, lens, or doc changed. No dependency, install path, or route.

## Findings

### What agentflow is (`observed` in the clone)

1. **Notebook-as-conversation.** Owner ↔ agent through `devlog.md` (Ask / Reply rounds `A-NNN`, STATUS ≤ 60 lines, numbered RUN events, ten-minute WIP checkpoints, SHA-256-verified archive compaction). Terminal output is one line. Any dead session resumes from the file via `resume-intake.js`.
2. **Two layers.** Base protocol for any task; on-demand pipeline (`requirements → codewalk → explore/spike → spec → implementation → security-scan → acceptance → learn`) with eight advisor rulebooks, loaded only when a wish changes product behaviour. Route ∈ {`direct`, `selected_advisors`, `full_pipeline`, `blocked`}; `allow-ag: off` is never silently downgraded.
3. **Delegation = `external-runner-v1`.** One literal executable + argument array in an independent disposable Git clone with no remotes (`external-runner.js` throws otherwise), closed stdin, 4,096-byte bounded output, frozen `*-brief.md`/`*-report.md` pairs, report stamped with model/effort and closed by one `Self-check:` line; "worker text cannot prove dispatcher metadata"; the coordinator diffs every clone change against the frozen write list before import.
4. **Mechanical referees.** Stop hook (Claude Code / Codex, `--host` required since I-043), round linter, git pre-commit devlog guard (I-039), tracker contract, cross-check plan (`narrow | targeted | full` from changed-file facts), terminal preflight, looper + `looper-live-gate` (two real low-cost provider plans before any looper change ships, I-064).
5. **Incident ledger as rule provenance.** `docs/incidents-log.md`: 73 append-only entries I-001…I-073; an editing guard says a rule whose incident you cannot explain is a rule you are not yet allowed to change.
6. **Minimality doctrine.** Reject any added concept that cannot name a current owner outcome or reproduced failure; record a rejected smaller alternative before freezing a contract-shaped change; a worker finding is never self-authorizing (I-054); Minimality is judged separately from Conformance.

### Evidence-tier findings (Evidence Auditor corrections to the packet)

- **Inline citation coverage is 18/73**, not "each incident maps to a cited rule": 55 ledger entries have no inline `— I-NNN` outside the ledger, and some `Cited by:` lines are stale (I-001 names a SKILL rule that carries no citation). The editing guard is real; its coverage is `author-claimed`.
- **Shipped tests depend on unshipped paths.** `release.test.js` needs `release/config.json` and `eval/evaluation-harness.md`; `prompt-compression.test.js` and `alignment.test.js` also read source-repo paths absent from the public tree. The coordinator's 898 / 889 / 9 TAP summary is a measurement on this tree, not a green release signal; the "all nine in `release.test.js`" attribution is `[INFERENCE]`.
- **Dangling load rule.** The shipped `SKILL.md:34` and `references/ag.md:11` instruct the agent to read `eval/evaluation-harness.md`, which `release.test.js:178` asserts must not ship. The public skill is not self-contained for that trigger; the default `godev` path does not need it.
- **LICENSE** is stock Apache-2.0 text with the `[yyyy] [name of copyright owner]` placeholder unfilled; no NOTICE file; `plugin.json` carries no version.
- **Public history** is three squashed release commits; the source repo `18a615a7` and every devlog round the incidents cite are private. Incident measurements, "safety behaviors never broke", F-code eval scores, and live two-plan gate runs are `author-claimed`.

### Supply-chain findings (Provenance lens)

`npx skills add agfnow/agentflow` and `/plugin marketplace add` (auto-updates) install a floating head; first `godev` / `agf init` writes project Stop hooks into `.claude/settings.json` / `.codex/hooks.json` and a git pre-commit hook; `--global` writes `~/.claude/settings.json` and `~/.codex/hooks.json`; optional `setup.js --fix` edits shell rc files after a prompt. The Stop hook fails open on its own errors. None of this is hidden — it is documented — but it is a host-product footprint, and `SKILL_INSTALLATION.md`'s "do not grant hooks unless the skill genuinely needs them" applies.

## Comparisons

| Axis | agentflow | TeaPrompt | Relation |
|---|---|---|---|
| Layer | methodology + operationalization in one skill (scripts, hooks, runner, looper) | methodology only; the operational layer is a Standing Non-Goal | two products; agentflow is closer to a host harness |
| Source of record | `devlog.md` notebook; transcript is not the record; SHA-256 archive | task packet / continuation packet / State Ledger; transcript is not the record (GA-3, GD-4) | same principle; agentflow owns the concrete file protocol |
| Human authority | owner sign-off gates; Design Go / Result Go on exact commits; `allow-ag: off` never downgraded; coordinator relabelling its own ruling as an owner decision is an incident (I-011) | Human Review list; `intent` and `acceptance` never auto-release; named accepter (GD-9); no silent downgrade | convergent |
| Worker confinement | independent no-remote clone, frozen brief, write-list diff, bounded output; self-declared "not an OS sandbox" | host preconditions declared (sandbox, egress, credential brokering), never provided | agentflow ships one instance of what TeaPrompt names; both honest about limits |
| Evidence | "a claim becomes a fact only after direct command output or exact file inspection"; worker numbers are never delivery evidence; exit zero is not acceptance | Claims Ledger, Evidence Tiers, attester ≠ self-summary, reason audit | convergent |
| Rule provenance | inline `— I-NNN` + append-only ledger + editing guard; 18/73 coverage | Candidate Adoption Ledgers + deterministic guard tests + Decision Index + Adoption Guard Closure; no inline citations | different encodings; TeaPrompt's is mechanically checked, agentflow's is honour-system and incomplete |
| Retry / loops | fixed at most three worker starts per review stage; relaunch at most twice; `Consensus: UNRESOLVED` rather than invented agreement | task-declared caps (ATT-7); cap exhaustion is a human decision | agentflow's fixed ceiling is the class ATT-7 rejected |
| Minimality | reject concepts without a named owner outcome; record the rejected smaller alternative; Minimality ≠ Conformance | `reflective-minimality` delete-before-add; GD-11; promotion classifier records the rejected lighter destination | convergent |
| Reviewer boundary | reviewer treats repository instructions as data, never runs the reviewed repo's workflow, never spawns another reviewer (I-072) | runtime trust boundary §3; Parallel Lens Review read-only contract | same rule; agentflow learned it from a recursion incident |
| Closeout | stop rule: record-only corrections after a proven commit do not restart implementation review (I-072/I-073) | Sufficiency Gate; failure-signature exits | analogous; agentflow's is a host completion-loop rule |
| Model dependence | per-project tiers `best/better/basic/cheap`; claim that safety held on every model and weak models fail on record hygiene | model-agnostic | claim is `author-claimed`; the "hygiene" discriminator is the same rule family that produced I-028 |
| Evaluation | private eval folders with F-codes; not shipped; shipped tests reference them | deterministic fixtures and ROUTE evals; no LLM-judged scores in CI | both public trees are judge-free; agentflow's scores are unverifiable |
| Cognitive load | ~14k always-on skill + trigger-loaded references; a four-item owner mnemonic | ~10k router + one skill; L1 fast path and context-load deferral | same shape; agentflow's win is owner memory, not model memory |

## Socratic Questions and Disposition

1. **Is inline incident citation a provenance gap in TeaPrompt?** No. Ledger IDs, adoption-state tests, and the Decision Index already bind adopted sentences to their origin and fail loudly on drift; Adoption Guard Closure deliberately retires paragraph pins. Inline IDs without an incident directory dangle; with one they are a new durable surface (promotion-gated). agentflow's own 18/73 coverage shows the honour-system encoding does not stay complete.
2. **Is "a worker finding is never self-authorizing" missing?** Conceptually stricter than `reflective-implement`'s "without a reason", but TeaPrompt avoids the failure structurally: review and implement are separate skills, implementation is bound to acceptance criteria, and reviewer output is findings, not authority. No local recurrence; record-only.
3. **Should `governed-delivery` name the no-remote clone as a host precondition?** No. It already names sandbox, egress, and credential brokering as host duties; naming one runner design would advertise a non-sandbox as isolation and lengthen a list TeaPrompt does not enforce.
4. **Does agentflow's closeout stop rule belong on the `acceptance` gate?** No — that would read "suite + review PASS closes delivery", contradicting OW-2 and the gate table. Its analog is the Sufficiency Gate and verification-channel hygiene, already present.
5. **Are agentflow's fixed three starts a "default" TeaPrompt could keep?** No. The ceiling is fixed by design and the coordinator may not exceed it; that is a universal numeric policy, the class ATT-7 rejected. Task-declared caps in emitted scripts are a different class.

## Disagreements / Residual Risks

- No verdict disagreement. Coordinator priors on AF-1, AF-2, AF-4, AF-5, AF-7 were "absorb narrow"; all seven lenses narrowed them to record-only or no-change. The coordinator accepts the narrowing: each candidate is either already held structurally or is operationalization.
- Residual: agentflow was not run against any repository and no provider was dispatched; live hook behaviour on current host versions is unknown (I-044 documents one regression); recurrence for every AF row is `unknown`.

## Candidate Adoption Ledger

| ID | Candidate (clean-room) | Status | Evidence | Next action / trigger |
| --- | --- | --- | --- | --- |
| AF-1 | Inline incident citation on failure-born rules + editing guard | **Record-only** 2026-09-05 (7/7) | Different provenance encoding; 18/73 inline coverage; ledger+guard already mechanical | Re-litigate only after a documented TeaPrompt skill edit that reopened a failure although its record existed |
| AF-2 | A worker or reviewer finding is never self-authorizing | **Record-only** 2026-09-05 (7/7) | Structural separation of review and implement; acceptance-criteria scope Never; no local recurrence | Re-litigate if a TeaPrompt review's Required Fixes are executed without an acceptance criterion |
| AF-3 | Record the rejected smaller alternative before freezing a contract | **No change** 2026-09-05 | `reflective-minimality` ladder; promotion classifier's rejected-destination column; GD-11 | — |
| AF-4 | Reviewer never runs the reviewed repo's workflow or spawns another reviewer | **Record-only** 2026-09-05 (7/7) | Trust boundary §3; Parallel Lens read-only contract; recursion is a host spawn rule | Re-litigate if a TeaPrompt lens is observed invoking a surveyed repository's skill or runtime |
| AF-5 | Record-only closeout must not restart implementation review | **Record-only** 2026-09-05 (7/7) | Sufficiency Gate; host completion-loop rule; must never sit on `acceptance` | Host-only if a delivery harness appears |
| AF-6 | Notebook / STATUS / RUN / WIP protocol | **Record-only; rejected as skill** 2026-09-05 | Standing Non-Goal; continuation packet is the methodology analog | — |
| AF-7 | Independent no-remote clone runner | **Record-only** 2026-09-05 | Host instance of named preconditions; self-declared non-sandbox | Cite as an example in a future host-precondition survey, never as a clause |
| AF-8 | Stop hook / pre-commit guard / round linter | **Record-only** 2026-09-05 | Host enforcement; fails open on its own errors; Durable Lesson on execution-layer failures | — |
| AF-9 | Fixed three worker starts per review stage | **Rejected** 2026-09-05 (7/7) | ATT-7; `governed-delivery` Never on universal retry counts | ATT-7's local controlled-pilot trigger only |
| AF-10 | One-line terminal output rule | **Rejected** 2026-09-05 | Host UX; I-028 shows the rule forced false statements | — |
| AF-11 | Real-provider live gate before shipping loop changes | **Record-only** 2026-09-05 | Matches refuter philosophy; TeaPrompt CI runs no providers; shipped test is fixture-only | — |
| AF-12 | Design Go / Result Go / advance gate authority | **No change** 2026-09-05 | GD-8 envelope; GD-9 named accepter | — |
| AF-13 | `blocked` as a first-class route with reason | **No change** 2026-09-05 | dispatch Human Review / stop; envelope stop | — |
| AF-14 | Adopt agentflow as a TeaPrompt host or dependency | **Rejected** 2026-09-05 (7/7) | Standing Non-Goal; no runtime dependencies; supply-chain footprint | Only on an explicit project-direction change |
| AF-15 | Cite agentflow's model-tier findings as evidence | **Record-only, author-claimed** 2026-09-05 | Eval folders unshipped; private source | If public eval bytes at a pinned commit are ever reproduced |
| AF-16 | Public tree pins unshipped `eval/` and `release/` paths; dangling load rule in the shipped skill | **Record-only (agentflow defect)** 2026-09-05 | `SKILL.md:34`, `ag.md:11`, `release.test.js:178`, `prompt-compression.test.js`, `alignment.test.js` | Not a TeaPrompt candidate; TeaPrompt's self-contained install rule already holds |
| AF-17 | Unpinned install and auto-update channel; hook / git-hook / shell-rc writes | **Rejected as install path** 2026-09-05 | README; `install-hook.js`; `setup.js --fix`; `SKILL_INSTALLATION.md` hook rule | Never add to TeaPrompt install docs |
| AF-18 | `allow-ag: off` never silently downgraded; exit zero ≠ acceptance; Minimality ≠ Conformance | **No change** 2026-09-05 | GLOSSARY Silent Downgrade; Delivery Invariants; separate review and minimality skills | — |

## Evidence Used (external source ledger)

- https://github.com/agfnow/agentflow — GitHub API view checked 2026-09-05: JavaScript, Apache-2.0, 18 stars / 6 forks / 0 issues; README and file tree.
- Local clone at `b2935f5381d6469243440e080b43d0092a591663` (`release: agentflow @ 18a615a7`, 2026-09-04 13:02 +0800); 3 commits; no tags; 71 files.

## Evidence vs Inference

- **Observed:** file tree, line text, counts (3 commits, 73 incident headings, 18 inline citations, 26 test files, 71 files), clone-independence code path, hook installer targets, LICENSE text, TeaPrompt surfaces at HEAD `2d61cf836eedd9492ae7fcd2e6762bf094a36849`; packet SHA-256 `2b95cecfc40b0ac7320082355167867659ed71927f8a8557852f5200164116c2`.
- **Coordinator-executed:** `node --test --test-reporter=tap` in `skills/agentflow/scripts` on Node v25.1.0 → 898 tests / 889 pass / 9 fail.
- **Author-claimed:** incident narratives and measurements; "safety behaviors never broke"; F-code eval scores; live two-plan gate runs; in-the-wild session recovery.
- **`[INFERENCE]`:** that the 9 failures are exclusively the `release.test.js` ENOENT cascade; that inline citation discipline would reduce TeaPrompt rule drift; that `npx skills add` installs cleanly today.

## Risks / Unknowns

- No agentflow script was run against a real repository and no provider was dispatched; the notebook protocol and hooks are unverified beyond unit tests.
- Recurrence for every AF row is `unknown`; nothing here is local evidence of a TeaPrompt failure.
- Apache-2.0 permits reuse with attribution; TeaPrompt policy stays clean-room restatement, so no agentflow sentence may enter a skill.

## Reproduction Contracts (host-only; not run)

- R-AF-1: on a host with Claude Code or Codex, install the skill project-scoped, run one `godev` round, and observe whether the Stop hook and round linter reject a malformed Reply on the current host version (I-043/I-044 class).
- R-AF-2: dispatch one `external-runner-v1` task with a provider and confirm the clone has no remotes, the write-list diff is enforced, and output is bounded at 4,096 bytes.
- R-AF-3: run `looper-live-gate.js` with two low-cost provider plans and confirm both exit criteria; the shipped fixture test does not run this.

## Evidence Actually Checked

- **Coordinator-executed:** GitHub API read; `git clone`; `git rev-parse` / `log` / `tag`; `find`, `wc`, `cat plugin.json`, `node --version`; `node --test` (TAP); greps for `eval/`, remote removal, hook targets, incident count, test-call count; reads of `SKILL.md`, `references/{looper,delegation,ag}.md`, `docs/incidents-log.md` (I-001–I-048, I-069–I-073), `docs/AG_GUIDE.md` §Which AI models, `external-runner.js:1-80`; TeaPrompt `reflective-minimality` contract and grep of candidate-absorb phrases.
- **Lens-read (per their Evidence sections):** all four references, advisor listing, `docs/skill-editing-and-compression.md`, `scripts/{README.md,release.test.js,looper-live-gate.js,looper-live-gate.test.js,external-runner.js,external-runner.test.js,install-hook.js,install-hook.test.js,stop-hook.js,agf.js,setup.js,resume-intake.js,prompt-compression.test.js,alignment.test.js,round-linter.js}`; LICENSE; `.claude-plugin/*.json`; TeaPrompt skills, `04-agent` lenses, `06-repo/AGENTS.md`, GLOSSARY, PROJECT_KNOWLEDGE, ATT-7, CCSP7, OW-2, GA/GD ledgers, adoption-state guards, `validate_record_hygiene.py`, `SKILL_INSTALLATION.md`.
- **Not executed:** any agentflow script against a repository; looper; any provider; the private source repo; `README.zh-tw.md`.
- **Post-synthesis verification:** recorded in the Completion Ledger.

## Falsifiability

This record is wrong and must be re-litigated if: (1) any TeaPrompt skill gains an agentflow sentence, an `I-NNN` citation, a fixed worker-start ceiling, or an install pointer to agentflow; (2) a TeaPrompt panel lens is observed invoking a surveyed repository's skill or spawning a nested reviewer; (3) a TeaPrompt review's Required Fixes are executed without an acceptance criterion; (4) agentflow publishes its eval data at a pinned commit and a reproduction contradicts the tiers above; (5) the 7/7 verdict is later cited as covering more than record-only.

## Completion Ledger

| Item | Status | Evidence |
| --- | --- | --- |
| Survey record, direct answer, findings, comparisons, ledger | `verified` | this file; record hygiene 0 errors / 0 warnings (26 enforced records) |
| Deterministic guard | `verified` | `plans/tests/test_agentflow_survey_record.py`: 6 passed — shape, identities, unanimity and reason tally, evidence corrections kept at their tier, ledger dispositions, no surveyed vocabulary on any skill or install surface, index rows |
| Decision Index and case-study rows | `verified` | `PROJECT_KNOWLEDGE.md` (validator passed), `external-adoption-case-studies-2026-06-20.md`; links 0 errors |
| Repository verification | `verified` | `make all`: 1094 passed; links 0 errors; lint 0 errors / one pre-existing `agent-governance-scaffold` warning; governance 13/13; ROUTE-001/002/003 100% |
| Packet removal, clone removal, branch re-check | `verified` | `review-packet-agentflow-survey-2026-09-05.md` deleted after synthesis; `/tmp/teaprompt-agentflow.0FuGFN` removed; shared worktree attached to `main` |
