# Skill Improvement Plan — `writing-great-skills` Lens — 2026-07-24

> **Status: adopted 2026-07-24 (non-authoritative); plan record — Phases 1–3 executed.**
> Per-skill improvement plan for all 12 registered TeaPrompt skills, derived from the
> external guide `mattpocock/skills` → `writing-great-skills` (SKILL.md + GLOSSARY.md,
> checked 2026-07-24). Authority chain unchanged: `06-repo/AGENTS.md` and the invoked
> `SKILL.md` contracts govern. All ledger rows, including flagged WGS-BRF-1 and
> WGS-REV-2, were approved in-session on 2026-07-24 ("next for all"); Phases 1–3
> executed the same day behind `make all` (see Execution Note). Deferred rows
> (WGS-GOV-1, WGS-SPC-2, WGS-X4a/b) keep their triggers. External-adoption discipline
> applies (PROJECT_KNOWLEDGE.md §Lesson): only verified local gaps got change tickets;
> no-change verdicts are recorded below.

## Why / What / How / Done

- **Why:** The guide names measurable skill-quality levers (predictability via
  descriptions, information hierarchy, completion criteria, pruning, leading words,
  negation discipline). TeaPrompt's 12 skill contracts have never been audited against
  this specific vocabulary; the last all-skill pass (2026-07-18) was
  portability/evidence-tier focused, not prose-economy focused.
- **What:** One improvement plan per skill (9 core + 3 domain packs): concrete findings
  with locations, change tickets, and explicit no-change verdicts.
- **How:** Map guide concepts onto repo constraints first (Adaptation Rules below), then
  audit each `SKILL.md` per lever, then phase the tickets behind `make all`.
- **Done:** Every skill has a verdict per lever; every ticket has acceptance criteria and
  a verification gate; deferred items carry dated or observable triggers; ledger records
  approval state.

## Source and Method

Guide: https://github.com/mattpocock/skills/tree/main/skills/productivity/writing-great-skills (checked 2026-07-24; SKILL.md and GLOSSARY.md read in full via raw.githubusercontent.com).

Levers audited per skill:

1. **Description** — front-load the leading word; one trigger per branch; cut identity restated in the body.
2. **Information hierarchy / completion criteria** — steps vs reference placement; checkable + exhaustive done-conditions; progressive disclosure for branch-only material; co-location.
3. **Splitting** — by invocation or by sequence.
4. **Pruning** — single source of truth, relevance, no-op test, sediment.
5. **Leading words** — collapse restatements into one pretrained token.
6. **Failure modes** — premature completion, duplication, sprawl, negation.

## Adaptation Rules (guide vs. repo constraints)

The guide is advisory; where it collides with governed local decisions, the local
decision wins. These rules are load-bearing for every ticket below:

| # | Guide lever | Local constraint | Resolution |
| --- | --- | --- | --- |
| A1 | Split by invocation (new skills) | Frozen nine + registered-pack admission (`06-repo/AGENTS.md` §Harness Policy) | No new SKILL.md directories. Sprawl is cured by progressive disclosure *within* a skill folder or the examples tree, never by a new skill. |
| A2 | Negation backfires; prefer positive phrasing | `Never:` subsection is test-pinned for all 12 skills (`tests/test_skill_module_contract.py` REQUIRED_SUBSECTIONS) and holds the anti-cheating/anti-overclaim guardrails | `Never` blocks stay — they are exactly the guide's "hard guardrail" carve-out. Negation cure applies as: (a) delete *duplicate* restatements of Never lines elsewhere in the same file, (b) keep the positive counterpart where one exists. |
| A3 | Collapse synonym triggers in descriptions | Routing fairness contract: equivalent intent must route equivalently (`plans/ROUTING_CONTRACT.md`); ROUTE-002 is a paraphrase holdout | Trigger-vocabulary breadth is measured coverage, not duplication. Only *identity tails* (what the skill does, already stated in the body) are trim candidates; trigger synonyms are kept. |
| A4 | Single source of truth | Installed skills are self-contained (AS2, 2026-07-18 panel); cheatsheet/dispatch cues deliberately co-exist | Single source of truth is enforced **within a file**. Cross-file repetition (frozen-nine rule, trust-boundary rule, dispatch cues in cheatsheet) is a recorded portability tradeoff — no-change. |
| A5 | User-invoked skills (`disable-model-invocation`) for zero context load | TeaPrompt ships multi-host; frontmatter is host-portable; domain packs are host-invoked already | Invocation axis is an **installation-layer** option, not a source change. Candidate: document in `SKILL_INSTALLATION.md` that hosts supporting user-invocation may install the three domain packs that way. The cheatsheet already plays the guide's "router skill" role. |
| A6 | Prune aggressively | Several lines are verbatim-pinned by tests (TWINS line in implement, PENDING line in risk, dispatch boundary cues, examples pointers, rig-tier labels) and by adoption records | Guarded lines are unprunable. Every edit phase gates on `make all` (pytest + 8 validators + 3 route evals). |
| A7 | Shrink oversized skills now | AS8 (2026-07-18) defers `agent-governance-scaffold` shrink to the 2026-10-11 checkpoint | This plan pre-stages the disclosure design but does **not** execute it early; findings feed the checkpoint. |
| A8 | No-op test is model-relative; settle by running | Repo lesson: prompt wording cannot fix execution-layer failures; eval harness exists but no-op verdicts need runs | Standalone no-op deletions are deferred (recurrence/eval-gated). Only lines that *also* fail the duplication test are cut in Phase 1. |

## Guarded Surfaces (blast radius)

Any ticket touching these re-verifies the named guard:

| Surface | Guard |
| --- | --- |
| `## Module Contract` + Trigger/Methods/Output/Never/Escalation subsections (all 12) | `test_skill_module_contract.py`, `lint_skills.py` |
| Escalation bullets naming only frozen skills | `test_core_skill_escalation_routes_to_valid_workflow_skills` |
| `<skills-root>/examples/<skill>.examples.md` pointer lines (all 12) | `validate_skill_examples.py` |
| Dispatch inline boundary cues; TWINS verbatim line (implement §Verification); PENDING verbatim line (risk §Rules); rig-tier / evidence-tier labels (flow packs, governance) | port1/fable/adoption-state tests |
| Frontmatter `name`, `description`, `metadata` rows | `lint_skills.py`, `validate_governance.py` |
| Routing behavior after any Trigger/description edit | `route_paraphrase_eval.py` ROUTE-001/002/003 (fixtures do not read SKILL.md — coupling is semantic, so the eval is the regression net, not a blocker) |
| `index.json` | regenerate via `plans/generate_index.py` after any skill text change |

---

## Per-Skill Improvement Plans

Line references are to the 2026-07-24 working tree.

### 1. reflective-dispatch (176 ln / 1,409 w)

Shape: reference-heavy router; flat rule set is a legitimate peer-set per the guide.

| Lever | Verdict |
| --- | --- |
| Description | **Trim identity tail** — "It selects the smallest useful reflective workflow and keeps Doing the right thing > doing things right." duplicates §Purpose (l.18–24). Trigger clauses stay. |
| Duplication | **Cut** Purpose l.24 ("Do not create a large plan, agent swarm, or multi-file process unless…") — verbatim meaning of Never l.46; the positive form ("Use the smallest workflow that can produce a verifiable result") already precedes it. |
| Hierarchy | Route table + boundary cues + strictness ladder inline: **no-change** (AS2 made cues inline-mandatory; disclosure would revert a governed decision). |
| Leading words | Healthy: *smallest useful workflow*, *default-up*, *route trace*, *silent downgrade*. No action. |
| Completion criteria | Output field list is checkable. No action. |

Tickets: **WGS-DIS-1** (Phase 1) delete Purpose duplicate sentence. **WGS-DIS-2** (Phase 2) trim description identity tail.

### 2. reflective-brief (117 ln / 601 w)

Shape: steps + template; smallest core skill; healthiest against the guide.

| Lever | Verdict |
| --- | --- |
| Description | **No-change** — the field enumeration doubles as trigger vocabulary (users ask with "assumptions/scope/acceptance criteria"); second sentence is a genuine branch cue. |
| Duplication | **Cut one** — Never l.39 ("Do not ask a broad questionnaire when one direct question or one reversible assumption is enough") is the negative twin of Operating Rule l.101. Keep the positive rule; this Never line is UX-shaping, not an integrity guardrail. Judgment call — flagged for approval. |
| Hierarchy | Workflow steps 1–11 mirror the Output template by design (derive each field in order): **no-change**; collapsing would trade clarity for tokens. |
| Completion criteria | "All Output fields filled" is checkable. Spike framing carries its own bound (question + timebox). No action. |

Tickets: **WGS-BRF-1** (Phase 1, flagged) drop Never l.39 in favor of the positive rule.

### 3. reflective-spec-plan (244 ln / 1,548 w)

Shape: steps + two large branch modes (Test Plan l.114–143, Workflow Design l.145–187).

| Lever | Verdict |
| --- | --- |
| Duplication | **Strongest core finding.** Operating Rules l.220–227 restates Never l.43–49 nearly verbatim: "workflow engine" (l.222≈l.44), "plan before acceptance criteria" (l.223≈l.45), "pass incomplete artifacts" (l.225≈l.47). Cut the three duplicates; keep l.224 ("Mark unknowns…", positive twin of l.46) and l.226 (unique retrieved-content rule). |
| Hierarchy | Modes are branch-only reference — the guide's cleanest disclosure license. **Deferred**, not fired: 244 ln is under lint bounds, installed skills are single-file today, and disclosure changes the install surface. Trigger to fire: lint length warning, or a documented case of mode content burying the core workflow. |
| Description | **No-change** — nearly all trigger enumeration; earns its length. |
| Completion criteria | Step 6 ("Stop at the smallest plan that can be executed and reviewed") + DoD block are checkable. No action. |

Tickets: **WGS-SPC-1** (Phase 1) dedupe Operating Rules. **WGS-SPC-2** (Phase 3, conditional) mode disclosure design.

### 4. reflective-implement (195 ln / 1,268 w)

Shape: steps with the repo's best completion criterion (Sufficiency Gate — checkable and exhaustive; cite as the house exemplar).

| Lever | Verdict |
| --- | --- |
| Duplication | **Cut** During-Editing l.103–104 ("Do not delete, skip, or weaken tests." / "Do not change expected outputs…") — verbatim copies of Never l.39–40. Never keeps the anti-cheating guardrails (A2); During Editing keeps its positive counterpart ("Add or update tests for each acceptance criterion"). |
| Leading words | Strong set: *State Ledger*, *Twin sweep*, *Sufficiency Gate*, *Fast Path*, *Budget Rule*. Micro-candidate: unify "smallest safe change" (l.18) vs "smallest reviewable change" (l.98) to one token. |
| Description | **Trim identity tail** ("It enforces small safe changes, … without weakening requirements.") — restates Purpose/Never. |
| Guarded | TWINS verbatim line l.136 untouchable (fable FM1 test). |

Tickets: **WGS-IMP-1** (Phase 1) dedupe During Editing + unify the leitwort. **WGS-IMP-2** (Phase 2) trim description tail.

### 5. reflective-review (174 ln / 1,079 w)

Shape: all-reference review skill — the guide explicitly blesses this arrangement; exhaustiveness bar ("every load-bearing claim in the ledger") binds the flat rules.

| Lever | Verdict |
| --- | --- |
| Duplication | **Trim one** — Never l.43 ("re-verified source text…") restates §Four Evidence Dimensions l.88 ("re-verifying a source's text never verifies its underlying data"). Shorten the Never bullet to guardrail form; the section owns the meaning. Never l.42 vs Claims Ledger intro l.65: **no-change** — prohibition + definition pair, the guide-endorsed shape. |
| Description | **Weak trim candidate** — tail enumeration ("critical thinking, counterargument, test integrity, spec traceability…") is part identity, part invocation vocab ("test integrity"). Trim conservatively or skip; flagged for approval. |
| Hierarchy | Six review modes, one line each: co-located, inline-cheap. No action. |

Tickets: **WGS-REV-1** (Phase 1) shorten Never l.43. **WGS-REV-2** (Phase 2, flagged) description tail.

### 6. reflective-minimality (140 ln / 898 w)

Shape: reference skill; apply its own ladder to itself.

| Lever | Verdict |
| --- | --- |
| Duplication | **Thin Methods gloss** — Methods l.34–41 pre-renders the Minimality Ladder l.69–81 (capability-ladder bullet spells all rungs) and Output l.43–52 renders the machine a third time. Compress Methods bullets to name + pointer ("stop at the first sufficient rung — see Minimality Ladder"); Output list stays (it is the deliverable spec). |
| Description | **Trim identity tail** ("It challenges whether code should exist, prefers deletion, … ceiling and upgrade triggers.") — first sentence already carries the trigger set; synonyms (YAGNI, anti-bloat) stay per A3. |
| Leading words | Exemplary: *ladder*, *safety floor*, *ponytail*, *debt marker*. No action. |

Tickets: **WGS-MIN-1** (Phase 1) thin Methods gloss. **WGS-MIN-2** (Phase 2) trim description tail.

### 7. reflective-research (196 ln / 1,439 w)

| Lever | Verdict |
| --- | --- |
| Duplication | **Shorten** Never l.46 (full high-volatility rule with parenthetical list) — §High-Volatility Facts l.119–127 is the source of truth. Never keeps a one-line guardrail naming check-date + tracking point. |
| Hierarchy | DeepWiki / Multi-Voice Panel / External Adoption Checks are branch reference but cheap and clearly gated ("Optional Method", "Skip when…"): **no-change** at current size. |
| Description | **Trim identity tail** ("It separates evidence from inference and avoids dumping raw context."). |
| Completion criteria | Sufficiency Gate is checkable + exhaustive; the "no fixed quota" perspective rule carries its own skip condition. No action. |

Tickets: **WGS-RES-1** (Phase 1) shorten Never l.46. **WGS-RES-2** (Phase 2) trim description tail.

### 8. reflective-risk (124 ln / 648 w)

| Lever | Verdict |
| --- | --- |
| Duplication | **Worst ratio in core.** (a) §Rules l.102–104 duplicates Never l.37–39 verbatim ("direct production changes", "backup/dry-run/rollback", "assume permissions…"): delete the three §Rules copies; §Rules keeps its unique rules (authorization gate, fail-closed verifier gates, memory-write provenance, bounded execution, audit record). (b) The trigger list exists three times: description, Module Contract Trigger l.23, §Trigger Conditions l.48–60. Shorten the Module Contract Trigger to one sentence + pointer to §Trigger Conditions (the superset with egress/injection rows); description stays per A3. |
| Guarded | PENDING verbatim line l.106 untouchable (fable FM2 test). |
| Description | **No-change** — the "gate" tail is routing-relevant (risk-first ordering is a dispatch cue). |
| Completion criteria | 17-heading output is demanding and checkable. No action. |

Tickets: **WGS-RSK-1** (Phase 1) dedupe §Rules + collapse triple trigger list to two surfaces.

### 9. reflective-handoff-retro (156 ln / 849 w)

| Lever | Verdict |
| --- | --- |
| Duplication | **Cut** l.100 ("Do not turn one-off accidents into permanent bureaucracy") — verbatim copy of Never l.40; the positive form ("Only institutionalize repeated patterns", l.91) opens the same section. |
| Hierarchy | Handoff / Retro / Promotion are three branches, each with explicit "Use when" entry conditions — the guide's branch pattern done right. Promotion contract stays inline (load-bearing for the AGENTS.md promotion path). **No-change.** |
| Cross-file | Frozen-nine restatement l.135 is portability duplication per A4. **No-change.** |

Tickets: **WGS-HND-1** (Phase 1) cut l.100.

### 10. flow-control-generator (371 ln / 2,396 w — domain pack)

| Lever | Verdict |
| --- | --- |
| Sprawl | Under lint bounds (500 ln / 20k chars). Templates ARE the deliverable; per-topology inline templates are branch reference, but "delete unused parts before adding" workflow and single-file install favor inline. **No-change**; trigger to revisit: lint length warning. |
| Duplication | Template comments restating the Script Contract are co-location for copy-paste artifacts (generated scripts must carry provenance): **no-change**, deliberate. |
| Description | **No-change** — reach clause to `flow-loop-harness` is exactly the guide's "when another skill needs…" clause; capability enumeration is trigger vocab (chain, pipeline, fan out, route, orchestrate). |
| Negation | Seven Never bullets are all integrity guardrails (secrets, self-edited gates, persistence claims): keep per A2. |

Tickets: none. Recorded no-change.

### 11. flow-loop-harness (326 ln / 2,732 w — domain pack)

| Lever | Verdict |
| --- | --- |
| Completion criteria | Six-part Loop Anatomy + four distinct exit codes is the strongest determinism contract in the repo — cite as exemplar; no action. |
| Description | **Trim identity tail** — "with iteration and budget caps, no-progress detection, human-review gates before unattended or side-effectful runs, and state ledgers as a resume convention the host must honor" is mechanics restated from the body. Trigger vocab (loop until, iterate, retry until green, ralph, burn down, writer-critic) stays. |
| Cross-file | macOS-`timeout(1)` note duplicated with flow-control-generator: portability duplication per A4, **no-change**. |
| Sprawl | Same verdict as flow-control-generator: **no-change**, lint-warning trigger. |

Tickets: **WGS-FLH-1** (Phase 2) trim description tail.

### 12. agent-governance-scaffold (404 ln / 3,060 w — domain pack)

| Lever | Verdict |
| --- | --- |
| Sprawl | Known: only skill tripping the lint char warning; AS8 (2026-07-18) defers shrink to **2026-10-11** — per A7 this plan does not fire early. **Pre-staged disclosure design for the checkpoint:** keep SKILL.md = Module Contract + Four-Power Split + Gate 2.0 + artifact *menu* (name + one line + invariant each); move the YAML/JSON object templates of the Artifact Set into a co-installed sibling reference (e.g. `agent-governance-scaffold/ARTIFACTS.md`) reached by a context pointer, mirroring the guide's own SKILL.md→GLOSSARY.md split. The guide's branch test licenses it: artifacts are emit-on-need ("the Artifact Set is a menu, not a mandatory file count"), so template bodies are branch-only reference. Estimated cut: >180 lines from SKILL.md. Requires: install-helper + `SKILL_INSTALLATION.md` update, pointer-wording test, evidence-tier labels preserved (AS4 guards). |
| Description | **No-change** — capability enumeration is trigger vocab; the "It emits static host-run contract templates; it does not enforce them" tail is an evidence-tier honesty label (AS4), not prunable identity. |
| Negation | Nine Never bullets are the four-power integrity core: keep per A2. |

Tickets: **WGS-GOV-1** (Phase 3, checkpoint-bound) submit the disclosure design to the 2026-10-11 AS8/R10 review.

---

## Cross-Cutting Tickets

| ID | Change | Phase |
| --- | --- | --- |
| WGS-X1 | Execute all Phase-1 within-file dedupe tickets as one reviewable change (DIS-1, SPC-1, IMP-1, REV-1, MIN-1, RES-1, RSK-1, HND-1; flagged: BRF-1). Net-negative diff; no heading removed; no guarded line touched. | 1 |
| WGS-X2 | Description identity-tail trims (DIS-2, IMP-2, MIN-2, RES-2, FLH-1; flagged: REV-2), then regenerate `index.json` (`generate_index.py`). Cheatsheets unaffected (they hold trigger cues, not frontmatter descriptions). | 2 |
| WGS-X3 | `SKILL_INSTALLATION.md`: add host-optional invocation note per A5 — hosts supporting user-invocation (e.g. Claude Code `disable-model-invocation`) may install the three domain packs user-invoked for zero context load; core nine stay model-invoked. zh-TW variant synced per LANGUAGE_POLICY. | 3 |
| WGS-X4 | Deferred experiments, each with an observable trigger: (a) description front-loading rewrite ("Route…", "Review…") — fire only on a documented misroute or routing-metric regression, measured by ROUTE evals; (b) standalone no-op hunt per A8 — fire when the eval harness can A/B a skill wording change; (c) spec-plan mode disclosure (SPC-2) — fire on lint warning or documented burying. | deferred |
| WGS-X5 | Feed this record's sprawl/disclosure findings into the 2026-10-11 governance checkpoint (WGS-GOV-1). | 3 |

## Sequencing and Verification

1. **Phase 0 (this record):** human approval of ledger rows; `make all` green with this file added.
2. **Phase 1 (WGS-X1):** within-file dedupe. Acceptance: net line count strictly decreases in each of the 8–9 edited skills; all five contract subsections still present per skill; `make all` green (782+ tests, 8 validators, ROUTE-001/002/003). Route: `reflective-implement` (doc edit, not review), Small-Change discipline per file.
3. **Phase 2 (WGS-X2):** description trims. Acceptance: frontmatter parses; trigger clauses byte-identical except removed tails; `make all` green; `index.json` regenerated. Any ROUTE eval regression reverts the batch — descriptions are semantically coupled to routing even though fixtures don't read them.
4. **Phase 3 (WGS-X3/X5):** installation note + checkpoint feed. Acceptance: `SKILL_INSTALLATION.md` + zh-TW updated; checkpoint agenda references this record.
5. **Rollback:** every phase is a single revertible commit; no phase changes governance surfaces (`AGENTS.md`, validators, route fixtures).

### Execution Note (2026-07-24)

All proposed rows were approved in-session ("next for all") and Phases 1–3 executed:

- Measured diff (Phases 1+2): 10 `SKILL.md` files, +12/−23 lines (net −11); skill
  layer total 2,623→2,612 lines and 17,927→17,667 words. `make all` green after each
  phase (1000 passed; 8 validators; ROUTE-001/002/003 passed).
- Acceptance deviation, recorded not hidden: Phase 1's "net line count strictly
  decreases in each edited skill" was over-specified — four files (dispatch, review,
  minimality, research) shrank within-line only (one line SWAPped for a shorter one),
  so their line counts are flat while content decreased. The criterion's intent
  (content-only removal, nothing added beyond pointers) held in all nine.
- Phase 3: `SKILL_INSTALLATION.md` §Choose an Install Tier invocation-mode note plus
  the zh-TW equivalent; the 2026-10-11 checkpoint runbook gained Agenda item 6
  (AS8/R10) pointing at WGS-GOV-1.
- `index.json` regenerated after the description trims.

## Candidate Adoption Ledger

| ID | Candidate | Status | Evidence | Next action / trigger |
| --- | --- | --- | --- | --- |
| WGS-X1 | Within-file dedupe across 8 core skills (+1 flagged) | Adopted 2026-07-24 | Duplicate pairs removed in 9 core skills; guarded lines untouched; see Execution Note; `make all` green | none |
| WGS-BRF-1 | Drop brief's Never l.39 for its positive twin | Adopted 2026-07-24 (within WGS-X1) | brief Never bullet removed; positive Operating Rule retained | none |
| WGS-X2 | Description identity-tail trims (5 skills, +1 flagged) | Adopted 2026-07-24 | 6 descriptions trimmed (dispatch, implement, minimality, research, review, flow-loop-harness); `index.json` regenerated; ROUTE-001/002/003 green | Revert trigger stands: documented misroute attributable to a trimmed description |
| WGS-X3 | Installation-layer invocation note for domain packs | Adopted 2026-07-24 | `SKILL_INSTALLATION.md` §Choose an Install Tier note + zh-TW note | none |
| WGS-GOV-1 | Governance-pack disclosure design (SKILL.md + ARTIFACTS.md) | Deferred to 2026-10-11 (AS8/R10) | Guide §Sprawl/§Progressive disclosure; lint char warning; AS8 ruling; checkpoint runbook Agenda item 6 added 2026-07-24 (X5 feed) | Evaluate at checkpoint; do not fire early |
| WGS-SPC-2 | Spec-plan mode disclosure | Deferred — conditional | 244 ln under bounds today | Fire on lint warning or documented burying |
| WGS-X4a | Description front-loading rewrite | Deferred — conditional | No observed misroute; ROUTE evals green | Fire on documented misroute/metric regression |
| WGS-X4b | Standalone no-op hunt | Deferred — evidence-gated | A8: no-op verdicts are model-relative, need runs | Fire when eval harness can A/B wording |
| — | Import guide vocabulary into repo GLOSSARY / new skill for skill-writing | **No change** | Existing GLOSSARY + skill-creator coverage; recurrence gate unmet; PROJECT_KNOWLEDGE lesson (prefer source doc over new skill) | Re-litigate only on third recurrence of skill-authoring guidance need |
| — | Flow-pack template disclosure / restructure | **No change** | Under lint bounds; templates are the deliverable; panel-adopted labels intact | Lint length warning |
| — | Cheatsheet/dispatch cue de-duplication | **No change** | AS2 governed decision; A4 portability tradeoff | New panel decision only |

## Evidence Actually Checked

- Guide SKILL.md + GLOSSARY.md, read in full (raw.githubusercontent.com, checked 2026-07-24).
- All 12 `reflective-prompt-library/skills/*/SKILL.md` (9 read in full; the 3 domain packs read to line 300 with tail sections read via prior structural passes; domain-pack line refs kept at section level).
- `wc -l -w` on all 12 skills (sizes quoted above, 2026-07-24 tree).
- `plans/lint_skills.py` (required sections, 500-line/20k-char bounds), `plans/validate_record_hygiene.py`, `plans/validate_skill_examples.py`, `plans/tests/test_skill_module_contract.py`, root `Makefile` (`make all` = pytest + 8 validators + 3 route evals).
- `plans/all-skills-panel-record-2026-07-18.md` (AS1–AS10, notably AS8 deferral), `06-repo/AGENTS.md`, `PROJECT_KNOWLEDGE.md` §Standing Non-Goals + §Durable Lessons, `skills/SKILL_TRIGGER_CHEATSHEET.md` header + dispatch section.
- Grep of `plans/route_paraphrase_eval.py` for `SKILL.md|description|Trigger`: no matches — fixtures do not read skill files.
- [INFERENCE] Identity-tail trims carry low routing risk because eval fixtures are decoupled and tails restate body content; this stays an inference until a post-edit ROUTE run — hence the Phase-2 revert rule.
- [INFERENCE] Estimated >180-line governance cut is a design estimate, not a measured diff.

## Falsifiability

This plan is wrong, and must be revised or withdrawn, if any of:

- A cited duplicate pair is not actually semantically equivalent when read in context (check the quoted line pairs before Phase 1).
- Phase 1 or Phase 2 turns `make all` red in a way that requires touching a guarded surface to fix — that would mean the "safe dedupe" framing was false.
- A ROUTE-001/002/003 regression follows a description trim — falsifies the decoupling inference; revert per Phase-2 rule.
- The 2026-10-11 checkpoint measures the governance pack's SKILL.md at ≤ the lint bounds without disclosure — WGS-GOV-1's premise (oversize persists) would be false.
- A host is found that cannot install multi-file skill folders — falsifies the ARTIFACTS.md disclosure design and WGS-X3's premise.

## Human Review

Approval for all proposed rows — including flagged WGS-BRF-1 and WGS-REV-2 — was granted in-session on 2026-07-24 ("next for all"). The frozen-core edits were in-place repairs, allowed without the promotion gate per the PROJECT_KNOWLEDGE §Lesson caveat. No auth/production/destructive surface was touched; residual risk is routing/regression only, bounded by `make all` and single-commit rollback per phase.
