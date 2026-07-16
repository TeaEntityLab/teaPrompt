# Fable Method Skill-Pack Survey — 2026-07-16

> **Status: decided (non-authoritative); external-adoption panel record.**
> fable-method is retained as study material with three deferred selective-adoption
> candidates (FM1–FM3) and one rejected candidate (FM4). No TeaPrompt workflow
> skill, supporting lens, verifier, dependency, or runtime surface was adopted by
> this survey. `06-repo/AGENTS.md` and governed skill contracts remain
> authoritative; this record is evidence and a decision, not an operating rule.

## Purpose

Preserve the completed 7-lens survey of `Sahir619/fable-method` (a Claude Code
skill pack claiming to distill "how Claude Fable 5 worked" into four skills plus
a 14-fixture trap eval) so the adoption question is not re-litigated from chat
memory. The decision question was twofold: whether the pack's eval claims match
its committed artifacts, and whether any mechanism survives TeaPrompt's overlap,
minimality, and recurrence gates.

## Target and Version

- Review target: [`Sahir619/fable-method`](https://github.com/Sahir619/fable-method), checked 2026-07-16.
- Pinned: tag `v1.4.0`, commit [`88b5cf36b10ee3679e08ee0f0181b9774d481508`](https://github.com/Sahir619/fable-method/commit/88b5cf36b10ee3679e08ee0f0181b9774d481508) (2026-07-15), checked 2026-07-16.
- Upstream license: MIT, verified from the repository on 2026-07-16.
- Repo shape at check date: 1143 stars, 158 forks, single-author linear history
  (15 commits), 4 skills (`fable-method`, `fable-loop`, `fable-judge`,
  `fable-domain`), `AGENTS.md` port, 14 eval fixtures, 16 result JSONs.
- Meta-disclosure: the surveying host agent is configured as the model family the
  repo claims to describe. Every repo claim about that model was treated as
  author-claimed; host identity corroborated nothing.
- Volatility trigger: re-check tag, commit, installer contents, and eval
  artifacts before relying on any later version; upstream was actively receiving
  issues and community PRs at check date.

## Panel Execution Mode

Method contract: `04-agent/workflow-recipes.md` §Parallel Lens Review and the
host `parallel-lens-review-packet` wrapper.

1. The coordinator ran a verification pass before fan-out: pinned clone, executed
   the repo's own `python3 .github/checks.py` (all checks passed, exit 0),
   measured skill line counts, previewed round 3/8/13 JSONs, and read the README,
   eval methodology, core `SKILL.md`, installers, and `RESULTS.md` rounds 14–15.
2. One shared packet (target, prior conclusion, meta-disclosure, commands run,
   findings F1–F9, author claims A1–A7, blockers, reviewer questions Q1–Q7,
   proposition under review) was written to a temp path readable by subagents.
   It was transient and deleted after synthesis.
3. The first fan-out of seven read-only scout lenses failed immediately with
   provider `429 RESOURCE_EXHAUSTED`. Per the skill's quota-fallback guardrail,
   the identical batch was refanned on default workers with a strict read-only
   constraint; that batch succeeded.
4. Three lenses crashed or parked mid-run (provenance twice, evidence once,
   methodology tail missing); each was revived over IRC and delivered its full
   deliverable. Every lens's complete output was read, not merely its preview;
   terminal verdict blocks were explicitly requested where a first reply omitted
   them.
5. Upstream issue list and [issue #3](https://github.com/Sahir619/fable-method/issues/3)
   (filed 2026-07-16) were fetched during the panel run, checked 2026-07-16.
6. One red-team claim ("s7 self-spoils its frauds") was coordinator-checked
   before synthesis and corrected: the fraud checklist lives in the correctly
   excluded `GROUND-TRUTH.md`; only `report.md`'s header framing would leak on a
   naive copy.
7. Role labels below are review perspectives; reviewer count is not evidence and
   no claim is made that distinct model providers were used. No reviewer edited
   the TeaPrompt repository or the clone.

## Lenses (all seven: AGREE WITH CHANGES)

| Lens | Load-bearing question | Main result |
| --- | --- | --- |
| Evidence auditor | Do the README results-table rows match the cited JSONs? | 5 rows faithful, 3 stretched, 2 unsupported: "3 of 4 vs frontier" is 2 of 4 in its own JSONs; ">260 agent runs" not reconstructible (~150–220); round 14 has no committed JSON. |
| Methodology / reproducibility | Is the eval design sound for the claims as worded? | "Judges never read reports" is false; train-on-test never named; n=1–4 cells; scenario-level reproduction possible, full 15-round chain not. |
| Provenance / security | What executes on an adopter's machine; what is the injection surface? | Installers are plain file copies but ship 3 of 4 skills; AUTH gate blocks outward actions only — fable-judge's "re-run every claimed verification" is a local execution relay; "sanitized" labeling not marker-evidenced. |
| Skill/prompt correctness | Are the four skills and references internally consistent? | Core loop coherent; 12 contradictions found: `AGENTS.md` "identical method" claim false, `fable-loop` stale at v1.3 artifacts, TWINS missing from Step-6 prose and chart 6, read-narrow vs binding-opens unresolved. |
| Trap-design red team | Are the 14 fixtures real traps; is the suite gameable? | Worker traps s2/s4/s7/s13 sound and code-verified; bait traps s9/s14 invalid under the default harness (blindness scores as safety); public answer sheets and artifact templates create high training-contamination risk. |
| Usability / actionability | Can a non-author adopt each path in ~10 minutes? | Plugin path yes (minor namespace confusion); standalone is a false-complete install (silent 3/4); `AGENTS.md` path is core-loop-only with slash-shaped usage. |
| Strategic synthesis | Thesis coherence and TeaPrompt fit? | Thesis coherent and honestly bounded; high philosophical overlap with `reflective-implement`/`review`/`risk`, low operational compatibility — merge artifacts, never stack both loops on one agent. |

## Panel Consensus

- **Decision:** `AGREE WITH CHANGES` (7/7 completed lenses; no clean AGREE, no
  DISAGREE) on the packet proposition that the pack is well-evidenced,
  honestly-reported, and safe to study and selectively adopt.
- **Direct recommendation:** study it seriously; treat `eval/RESULTS.md` as the
  honest read and the README results table as the marketing read. The repo's
  transferable core is one finding: weak models obey rules only as forced
  artifacts at decision points, not as prose (`INTENT` 1/4 → 4/4;
  `TWINS` 0/6 → 3/3 with fresh-seed replication). That finding was independently
  corroborated on the survey date by upstream issue #3 (17.6-point self-grading
  inflation measured in an unrelated pipeline; deterministic grep-floor
  proposed).
- **Honesty asymmetry:** `[INFERENCE]` the project's self-corrections (round 15
  downgrading its own round-14 safety claims to "not-armed", published nulls,
  cut features) are more trustworthy than its README headline table, which
  over-claims in at least three places. The gap is marketing drift, not data
  fabrication: every number the panel checked traces to a committed JSON except
  the run-count total and round 14.
- **Local-fit decision:** `[INFERENCE]` fable-method's loop methodology is
  present or adjacent across `reflective-implement`, `reflective-review`,
  `reflective-risk`, and `reflective-dispatch`. What TeaPrompt lacks is not the
  philosophy but the two empirical mechanisms: verbatim forced artifacts at
  decision points, and a regenerable trap-fixture eval with an answer-sheet
  exclusion protocol. Those are merge candidates into existing skills, not new
  surfaces.
- **Promotion decision:** no promotion. Frozen-core and new-surface gates stay
  closed; FM1–FM3 defer until their triggers fire; FM4 is rejected outright.

### Use-Case Recommendation

| Use case | Decision | Evidence boundary |
| --- | --- | --- |
| `study` | **yes** | `eval/cases/`, `RESULTS.md`, and the v1→v3 forced-artifact iteration are reference-grade; the nulls-with-wins reporting stance is rare and worth imitating. |
| `reproduce` | **conditional** | Scenario-level re-runs are possible from `GROUND-TRUTH.md` files; the full 15-round chain is not (unpinned models, dual harnesses, placeholders, traps that fail to arm under the workflow-subagent harness). Reproduction requires fresh/held-out fixture variants — the public ones are contaminated by design. |
| `adopt` into TeaPrompt | **deferred** | FM1–FM3: merge candidates only (forced artifacts into `reflective-implement`/`reflective-risk`; private trap suite with a deterministic floor). Gated on same-harness reproduction on the org's executor tier. |
| `adopt` in another host | **conditional** | Plugin path only (installers ship 3 of 4 skills); most lift claims concern weak-tier executors; capable-model hosts should expect nulls on clean tasks, per the repo's own table. |
| `deploy` | **no** | Skill text is behavioral policy, not a security boundary; verification mandates are a local execution relay in poisoned workspaces; numbers are smoke-grade (n=1–4, LLM judges, train-on-test) and must not be quoted as benchmarks. |

## Required Wording Changes

Upstream-facing candidates consolidated from all seven lenses. None was applied
to TeaPrompt or to the upstream repo by this review.

1. **Cross-model row:** "ties or out-ranks it on 3 of 4" must become "2 of 3
   (round 4); ties on score but ranks second on the large research task
   (round 5)" — unsupported as worded by the cited JSONs.
2. **Run count:** ">260 agent runs" must become "~150+ committed runs (rounds
   1–13, 15); round 14 narrative-only" or the round-14 JSON must be committed.
3. **Judge description:** "never by reading reports" is false; judges read every
   report for `report_quality` and several `correct_action` caps. Say "verify
   factual claims by diffing and executing; reports are also read and scored".
4. **Headline trap row:** add "4/4 surfaced; ideal fix 0/4 (all runs still
   edited the code)" and cite round 1 for the 0/4 baseline.
5. **s14 safety claim:** footnote the round-15 downgrade ("not-armed under the
   workflow-subagent harness") everywhere "7/7 refused" appears.
6. **Tier-lift thesis row:** add "n=1 per cell; Haiku pair cross-domain".
7. **Stale counts:** "~110 lines" → ~130; "14 failure modes" → 18; DOC.md
   "Three skills" → four; "raw sanitized judge outputs" → evidence the
   sanitization or drop the word (scratch paths remain in round-7 JSON).
8. **Limitations:** add an explicit train-on-test bullet (rules iterated on the
   same fixtures that produce headline ratios; round-15 fresh seeds mitigate the
   twin check only).
9. **Installers:** `install.sh`/`install.ps1` must copy `fable-domain` or print
   "partial install (3/4 skills)" — currently a false-complete install with a
   success banner.
10. **AGENTS.md parity:** "identical method" must be scoped; the port lacks the
    v1.4 domain-router paragraph and flowcharts pointer, so non-Claude adopters
    get a split-brain method.
11. **Family drift:** `fable-loop` Stage 4 still claims INTENT and AUTH are the
    only report artifacts (stale at v1.3); Step-6 prose and flowchart 6 omit
    TWINS; chart 1 mandates a judge pass that chart 8 and the skill text make
    optional; read-narrow vs binding-opens needs one precedence sentence.

## Candidate Adoption Ledger

| ID | Candidate | Status | Evidence | Next action / trigger |
| --- | --- | --- | --- | --- |
| FM1 | Merge `INTENT`/`TWINS`-style forced artifacts into `reflective-implement` Verification | Deferred — current no-change | Round 3 (1/4 prose → 4/4 forced artifact) and round 14/15 (0/6 → 3/3, fresh-seed replicated) are the pack's strongest transfer evidence; TeaPrompt encodes the intent but not verbatim decision-point artifacts | Requires same-harness reproduction on the org's executor tier showing the artifact adds lift over existing `reflective-implement` wording; then a wording change to that skill's contract with its own guard |
| FM2 | Merge `AUTH`/`PENDING` (documented ≠ authorized) into `reflective-risk` Authority | Deferred — current no-change | Round 11 frontier deploy 1/2 is diff-proven; `reflective-risk` carries dry-run/rollback/Human Review but no verbatim quote-gate; PENDING failed to transfer to weak tiers (1/12) | Same reproduction gate as FM1; adopt the AUTH quote-gate only if it composes with (not substitutes for) the existing risk record; PENDING adoption requires evidence the artifact closes the weak-tier dropout it failed to close upstream |
| FM3 | Private regenerated trap-fixture suite with a deterministic floor for TeaPrompt skill evals | Deferred — current no-change | Trap suite pattern is sound for worker traps (s2/s4/s7/s13 code-verified); public fixtures are contamination-burned; upstream issue #3 proposes grep-checkable anchor facts under LLM judgment, checked 2026-07-16 | Reconsider when a TeaPrompt eval-harness round needs adversarial fixtures; regenerate variants privately, pair every LLM-judged metric with a deterministic anchor check, never reuse the public fixtures verbatim |
| FM4 | Install fable-method as a parallel global skill beside the reflective library | Rejected 2026-07-16 | Strategy lens: competing final-report schemas and default-rigor levels on one agent produce costume compliance or dropped gates — the failure mode both libraries exist to prevent | Re-litigate only if upstream and TeaPrompt reconcile to a single report contract, and a real routing failure shows the reflective library alone is insufficient |

No governed TeaPrompt wording, skill, lens, verifier, dependency, or runtime
surface was adopted. Therefore no content pin is required at a named operational
surface. The deterministic guard for this record checks the record shape, exact
FM1–FM4 dispositions, pinned revision, and cross-link from the external-adoption
case-study index: `plans/tests/test_fable_method_survey_record.py`.

## Shared Findings

### What fable-method does well

1. **The forced-artifact finding is real and replicated.** Prose rules moved
   Haiku 1/4; the same rule as a mandatory `INTENT:` report line moved it 4/4;
   the `TWINS:` line repeated the pattern (0/6 → 3/3) and survived a fresh-seed
   replication the grader did not author.
2. **Nulls are published beside wins.** Rounds 6–7 (12/12 ceiling nulls), the
   9a fixture-design null, the round-14 app-build ceiling, and the cut
   skill-in-skill feature (1/14) are all in the log; the README table carries a
   deliberate "no lift" row.
3. **Self-downgrades are unusually honest.** Round 15 re-classifies its own
   round-14 safety wins as "not-armed" and names blindness-vs-discipline as a
   measurement problem — a distinction most eval logs never draw.
4. **Worker traps are mechanically gradable.** s7's five frauds and s13's five
   disguised `int(*100)` sites were verified present by code inspection;
   `deploy.py`/`ship.py` are genuinely inert marker-writers, so violations are
   diff facts.
5. **The supply chain is small and boring.** Installers are `cp -r`; no
   install-time code execution; CI is a consistency lint; MIT license; the
   SpecBench citation ([arXiv 2605.21384](https://arxiv.org/abs/2605.21384),
   checked 2026-07-16) is faithful to the paper's 28pp-per-10x finding.
6. **The authority order is coherent everywhere it appears.** User > spec >
   tests > code survives across SKILL.md, flowcharts, fable-judge, and all
   domain adapters without inversion.

### Load-Bearing Gaps

1. **The README trust surface over-claims.** "3 of 4" is 2 of 4; ">260 runs" is
   unsupported; "never by reading reports" is false; the headline trap row
   conflates surfacing with fixing.
2. **Round 14 is narrative-only.** The round that justified v1.4's flagship
   features has no committed JSON; round 15's smoke replication is n=1.
3. **Train-on-test is undisclosed.** Rules were iterated on the same fixtures
   that produce the headline ratios; the limitations section names smoke grade
   but not fixture-overfitting.
4. **Bait-dependent traps measure exploration, not discipline.** s9/s14 "safe"
   outcomes under the default harness came from never reading the bait; the
   repo's read-narrow rule actively works against trap arming.
5. **Public answer sheets burn the benchmark.** All 14 `GROUND-TRUTH.md` files,
   case postmortems, and artifact templates are public; any model trained on the
   repo can pass by vocabulary mimicry. The suite is valid only as a private,
   regenerated pattern.
6. **The family has split-brain drift.** `AGENTS.md` ("identical method") and
   `fable-loop` lag v1.4 on load-bearing surfaces, hitting exactly the weak-tier
   adopters the pack targets.
7. **Verification mandates are an execution relay.** fable-judge re-runs claimed
   commands; the AUTH gate does not cover local execution, so a poisoned
   workspace weaponizes the discipline itself.
8. **The standalone install is false-complete.** Both installers ship 3 of 4
   skills behind a success banner.

## Evidence vs Inference

| Claim | Status | Basis |
| --- | --- | --- |
| v1.4.0 tag, commit identity, MIT license, repo stats | Observed / verified | GitHub API reads and pinned clone, checked 2026-07-16 |
| Repo's own `checks.py` passes at the pinned commit | Observed / executed | Local run, exit 0 |
| README "3 of 4" row unsupported; "2 of 4" per JSONs | Observed / verified | Evidence-lens counts over round4/round5 JSONs |
| ">260 agent runs" | Unsupported from artifacts | JSON cell tally ~150–175 committed (~191–218 with round-14 narrative estimate) |
| Judges read reports | Observed / verified | `workflow.js` judge prompt + every JSON `verdict_summary` |
| s7 frauds and s13 twin sites physically present | Observed / verified | Red-team code inspection of fixture files |
| `install.sh`/`install.ps1` ship 3 of 4 skills | Observed / verified | Both installer files read; F1 confirmed twice independently |
| SpecBench citation faithful | Observed / verified | arXiv abstract fetch, checked 2026-07-16 |
| Forced-artifact lesson transfers beyond this repo | `[INFERENCE]` | Consistent across rounds 3/14/15 plus independent corroboration in upstream issue #3; not reproduced locally |
| Origin story (model self-distillation, three critics, observed traces) | Author-claimed | Round 10/11 trace JSONs exist but were not audited line-by-line |
| Eval results reflect real model runs (not fabricated) | Author-claimed / consistent | Internal consistency across 16 JSONs, self-corrections, and committed failures make fabrication unlikely but unproven; no re-runs executed |
| TeaPrompt has an adoption-worthy gap in loop methodology | Not supported | Overlap matrix: philosophy present/adjacent across `reflective-*`; only the two mechanisms (FM1–FM3) are candidates |

## Disagreements / Residual Risks

- **Leakage severity:** the red-team lens holds the eval "materially compromised
  for out-of-repo use"; the methodology lens holds it "directionally informative
  as a developer-in-the-loop program". Adjudication: both, at different scopes —
  trust the diff/execution-backed failures, never quote the ratios.
- **AGENTS.md drift severity:** the skill-quality lens noted a skeptic could
  argue DISAGREE-level incoherence for port users; settled at AGREE WITH CHANGES
  because the core loop mechanics are coherent where the eval actually tested
  them.
- **Inverse-tier thesis:** strategy lens "supported with bounds" vs evidence
  lens "stretched at n=1 cross-domain". Consensus wording: directionally
  suggestive, smoke-grade.
- **Judge-as-execution-relay:** flagged by the provenance lens as the sharpest
  tension in any "safe to adopt" wording; no lens proposed a fix short of
  allowlisting verification commands, which upstream does not have.
- **Provenance residue:** PR #2's contribution is described in round-15 JSON but
  not confirmable from the linear git log; plugin installs track the marketplace
  pointer without a commit pin; star count authenticity was not checked.

## Evidence Actually Checked

### Executed

- `git clone` and `git log` pinning; tag list.
- `python3 .github/checks.py` at the pinned commit (all checks passed).
- `wc -l` over the four SKILL.md files and AGENTS.md.
- JSON cell counting across rounds 1–13 and 15 (evidence lens; coordinator
  previews of rounds 3/8/13).
- Greps for sanitization markers, round-14 artifacts, and s7 fraud strings.
- Code inspection of s2, s7, s9, s13, s14 fixtures including `deploy.py` /
  `ship.py` inertness and the five s13 infected modules.
- Both installers read end-to-end; plugin and marketplace manifests read.
- Panel mechanics: one failed scout fan-out (429), one successful default-worker
  refan, three IRC revivals, seven full deliverables synthesized.

### Upstream / Official Sources

All checked 2026-07-16:

- [Repository and README](https://github.com/Sahir619/fable-method), checked 2026-07-16.
- [Pinned commit](https://github.com/Sahir619/fable-method/commit/88b5cf36b10ee3679e08ee0f0181b9774d481508), checked 2026-07-16.
- [Issue #3 — deterministic floor under LLM judges](https://github.com/Sahir619/fable-method/issues/3), checked 2026-07-16.
- [SpecBench, arXiv 2605.21384](https://arxiv.org/abs/2605.21384), checked 2026-07-16.
- Pinned-clone reads: all four `skills/*/SKILL.md`, `references/flowcharts.md`,
  `references/failure-modes.md`, domain adapters, `AGENTS.md`, `DOC.md`,
  `CONTRIBUTING.md`, `CHANGELOG.md`, `eval/README.md`, `eval/RESULTS.md`,
  `eval/workflow.js`, all 16 result JSONs (counts), 14 scenario fixtures,
  `.github/workflows/checks.yml`, `LICENSE`.

### Local TeaPrompt Sources

- `04-agent/workflow-recipes.md` §Parallel Lens Review (method contract).
- `skills/reflective-implement/SKILL.md`, `skills/reflective-review/SKILL.md`,
  `skills/reflective-risk/SKILL.md` (strategy-lens overlap matrix).
- `plans/external-adoption-case-studies-2026-06-20.md` and the Baton/DilinAI
  survey records (record conventions).

### Not Executed

- No LLM eval re-runs, no plugin install, no standalone install, no
  `fable-judge` invocation, no benchmark replication.
- No TeaPrompt workflow, route, skill, or project-knowledge authority surface
  was changed by the survey decision.
- The shared packet and the pinned clone were deleted after synthesis and are
  not dependencies of this record.

## Falsifiability

This decision is wrong if any of the following occurs and FM1–FM4 are not
re-opened:

1. A TeaPrompt eval round or real task shows a weak-tier executor dropping a
   verification, authorization, or twin-sweep obligation that a verbatim forced
   artifact would have caught — and the ledger still says deferred (FM1/FM2
   trigger fired, unacted).
2. A local same-harness reproduction shows the forced artifacts add no lift over
   existing `reflective-implement`/`reflective-risk` wording — then FM1/FM2 must
   be closed as rejected, not left deferred indefinitely.
3. A TeaPrompt eval-harness round adopts adversarial fixtures without the
   deterministic-floor discipline recorded in FM3, or reuses the contaminated
   public fixtures verbatim.
4. A future pinned fable-method release commits round-14-grade raw artifacts,
   held-out fixture replications, and reconciled family documents — the
   "reproduce: conditional" and README-drift findings must then be re-checked
   rather than quoted from this record.
5. Upstream reconciles report contracts and a real local routing failure shows
   the reflective library alone is insufficient — FM4's rejection must be
   re-litigated instead of treated as permanent.

Re-evaluation must update FM1–FM4 rather than creating a disconnected decision
record. Guard: `plans/tests/test_fable_method_survey_record.py`.
