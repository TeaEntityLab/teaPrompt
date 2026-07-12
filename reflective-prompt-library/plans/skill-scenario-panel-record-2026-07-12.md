# Skill Scenario/Usage Panel — 2026-07-12

> **Status: decided (non-authoritative); panel record.** Parallel Lens Review
> over the skill layer, asking which user scenarios the 9 core skills + 2 domain
> packs serve poorly and which updates follow. Authority chain unchanged:
> `06-repo/AGENTS.md` and the invoked `SKILL.md` contracts govern; this record is
> evidence, not an operating rule. If it and a governed surface disagree, the
> governed surface wins.

## Purpose

User-directed review ("think about different usages and users' scenarios/scenes,
find out possible updates about skills"). Seven persona lenses walked concrete
journeys through the routing and skill surfaces at commit `8fda8c8` (clean tree,
`make all` green: 899 pytest, all validators, ROUTE-001/002/003 at 100%).

## Execution mode (honesty note)

Method contract: `04-agent/workflow-recipes.md` §Parallel Lens Review. A shared
packet (`review-packet-skill-scenarios-2026-07-12.md`, transient, deleted after
synthesis) was written first. Two parallel fan-out attempts (7 lenses, then a
1-lens probe) failed with provider `resource_exhausted`; per §Packet-and-verdict
contract the lenses were then executed **sequentially by one agent** as explicit
persona passes. Role labels below are review perspectives; no external model or
separate agent was invoked. Consensus here is therefore advisory single-host
multi-pass evidence, one tier below true multi-agent consensus.

## Panel Consensus

- Decision: **AGREE WITH CHANGES** (7/7 lenses).
- Use-case recommendation: **adopt** (wording-level skill/doc updates only; no
  runtime claims, no new core skill — the frozen-nine boundary was respected by
  every lens).
- Adopted same-day as a user-directed wave (recurrence `unknown`), consistent
  with `plans/dormant-items-user-directed-adoption-2026-07-12.md`.

## Required Wording Changes (mandated by lens verdicts; all applied)

1. `reflective-implement`: trigger/description include repository documentation
   and content edits; new `## Small-Change Fast Path` section (single-file,
   low-risk, no bloat signals → collapsed restatement/report; verification never
   collapses).
2. `reflective-dispatch`: Strictness Ladder note — L3's spec-plan stage is for
   plan-artifact work; small clear changes route directly to implement.
3. `reflective-risk`: data-egress trigger bullet referencing
   `04-agent/external-adoption-review.md` §2a as the packet-handling lens (plus
   that prompt's Primary-surfaces line and `AGENT_SKILL_LINKS` registry gain
   `reflective-risk`).
4. `reflective-brief`: spike/exploration framing (falsifiable question +
   timebox + disposable-artifact label; promotion via review/risk).
5. `reflective-handoff-retro`: ledger bridge — attach/summarize implement,
   research, or loop ledgers under `Files / Artifacts` instead of re-deriving.
6. Both cheatsheets: two new boundary quick cues — "Doc edit not review" and
   "Prototype/spike (criteria emerge by building)" (EN + zh-TW co-landed).
7. `SKILL_INSTALLATION.md`: "No Agent Skills support?" prompt-layer fallback.

## Shared Findings

- **Proportionality gap at the implement surface.** Dispatch preaches smallest
  workflow and has an L1 fast path, but implement — where trivial tasks land via
  host auto-triggering — had fixed ceremony (8-heading report; ledger wording
  that literally captured any multi-file step). Observed text, all lenses.
- **Doc work half-covered.** `reflective-review` accepts articles; implement's
  vocabulary excluded prose edits — yet this repo's own daily workload is
  Markdown edits run under implement conventions. Observed repo practice; the
  strongest-evidence finding of the panel.
- **Cross-reference coherence.** New 2026-07-12 stanzas (M7 redaction) and the
  three ledger conventions (implement / research / loop-harness) lacked inbound
  links at the surfaces where users need them (risk gate; handoff template).
  Observed structural gaps.
- **Exploration unnameable.** Implement requires verifiable criteria; brief
  blocked planning before criteria are usable; no surface named the spike
  framing that resolves the tension. Observed text; user demand [INFERENCE].
- **zh-TW parity is structural, not literal, by policy** (EN authoritative; zh
  cheatsheet is an L1–L2 router). ROUTE-002 already fixture-guards zh phrases.
  Deeper localization stays gated: this panel added no user evidence.
- **Install surface is fresh** (verified 2026-07-11) with pack `compatibility:`
  prerequisites; only genuine gap was the no-skill-host degradation path.

## Per-lens summaries

### SoloRapidFix — solo developer, 10-minute window
Findings: ladder L3 read as spec-plan-always (`dispatch` §Strictness Ladder) vs
route table and cheatsheet sending trivial fixes straight to implement; ledger
duty captured 2-step patches; only dispatch had a fast path, invisible from
implement. Socratic: is in-skill proportionality redundant if dispatch fronts
routing? (No — hosts auto-trigger by description.) Does a fast path license
skipped verification? (Only if worded so; it is not.) Is the ladder prescriptive?
(Nothing marked it illustrative.) Strongest objection: the library's own
"smallest workflow" purpose failed at its highest-frequency surface. Verdict:
AGREE WITH CHANGES (SOLO-2, SOLO-3).

### NonEngineerUser — PM/writer/analyst, non-code deliverables
Findings: prose revision had a review route but no revision route; TeaPrompt's
own Markdown governance work is the recurrence evidence; no doc-edit boundary
cue. Socratic: is doc work in scope? (Repo practice says yes.) Do added cues
dilute ROUTE fixtures? (Fixtures pin existing phrases; additive.) Should doc
production route to spec-plan? (It already does; revision was the gap.)
Strongest objection: a library that cannot route its own maintenance work
misdescribes itself. Verdict: AGREE WITH CHANGES (DOC-1, DOC-2).

### BilingualOperator — zh-TW mixed-language routing
Findings: structural parity held (8→10 boundary cues, 快速順序, L1 快速路徑,
pack appendix); many zh sections quote EN cues untranslated — by declared
policy; ROUTE-002 carries zh holdouts. No observed zh-user routing failure →
no new evidence for the localization gate. Socratic: is zh parity load-bearing
under EN authority? (Yes, for L1–L2 routing, per the zh banner itself.) Would
more zh cues help or only inflate fixtures? (Unknown; no telemetry.) What
prevents drift? (Co-landing rule + parity tests.) Strongest objection:
adopting EN-only cues from this panel would create exactly the drift the parity
tests catch. Verdict: AGREE WITH CHANGES (ZH-1 co-landing, applied; deeper
localization stays gated).

### MultiHostInstaller — Claude Code / Codex / Cursor / bare hosts
Findings: install guide fresh and per-host validated; packs declare bash 3.2+/
POSIX/headless prerequisites and macOS `timeout(1)` absence handling; missing
piece was the paste-as-prompt fallback for hosts without Agent Skills.
Socratic: do hosts tolerate the nonstandard `compatibility:` key? (Local
validator does; external hosts author-claimed.) Is paste-as-prompt safe to
document? (It is the library's original architecture.) Any observed install
failure? (None; [INFERENCE].) Strongest objection: install docs verified against
docs, not live hosts — the fallback paragraph is the cheap hedge. Verdict:
AGREE WITH CHANGES (HOST-1).

### HighStakesEnterprise — regulated, audited environments
Findings: risk's output contract is audit-shaped (Audit Log Plan, Human
Approval Gate, Bounded Execution) — strong; no egress trigger existed and the
M7 redaction stanza had no inbound link from the risk gate; incident response
(urgent + high-risk) has no break-glass wording. Socratic: does an egress bullet
expand scope? (It names an instance of existing scope.) Break-glass: library or
org policy? (Org policy; the library can only mark the seam.) Was §2a reachable?
(Not from risk.) Strongest objection: a redaction methodology invisible from
the risk gate is skipped exactly when it matters. Verdict: AGREE WITH CHANGES
(ENT-2 applied; ENT-1 deferred to Human Review by design — it would weaken a
safety gate).

### GreenfieldIterator — fast-cycle exploratory builder
Findings: implement demanded verifiable criteria while nothing told users how
to phrase exploratory criteria; spec-plan's formalization ladder and purpose
already lean anti-ceremony; packs correctly stay verifier-bound (explore loops
without deterministic verifiers are out of pack scope — boundary kept).
Socratic: new mode or wording of brief? (Wording; no new skill.) Does a
disposability label let spike code slip to production? (Promotion routes
through review/risk.) Evidence? ([INFERENCE]; textual tension observed.)
Strongest objection: the library reads as if all work starts with known
criteria; exploration is a top real scenario and was unnameable. Verdict:
AGREE WITH CHANGES (GREEN-1, GREEN-2).

### LongSessionOperator — multi-day autonomous sessions
Findings: handoff template genuinely resumable; three ledger conventions
coexisted with zero bridging text (silent state loss at the seam); mid-task
re-route had no dispatch cue. Socratic: are three formats drift? (No — different
jobs; the gap was the bridge.) Embed ledgers verbatim? (Attach or summarize;
never re-derive.) Does a re-route cue duplicate dispatch's trigger? (Partially —
which is why it defers.) Strongest objection: handoff is the library's whole
continuity story; losing ledger state there is silent data loss. Verdict:
AGREE WITH CHANGES (LONG-1 applied; LONG-2 deferred).

## Disagreements / Residual Risks

- **Fast path vs gate safety (preserved dissent).** SoloRapidFix wanted
  collapsed reporting; HighStakesEnterprise objected that "trivial" labels are
  how risky changes bypass gates. Resolution: fast-path preconditions
  (single-file, low-risk, no bloat signals) + verification never collapses +
  any risk signal exits to the full contract. The tension stands recorded.
- **Spike mode vs bureaucracy-minimalism.** Adding exploration wording for a
  hypothesized user brushes against "do not manufacture lessons." Resolution:
  one stanza + one cue, no new skill, recurrence `unknown` in the ledger.
- **Single-host execution.** This consensus lacks genuinely independent
  reviewers; treat any one-lens-only claim as weaker than its wording suggests.
- ROUTE fixtures still prove regression-guard coverage, not live user routing;
  every "scenario" here remains hypothesis until real usage evidence exists.

## Evidence Actually Checked

- Read in full this session: all nine core `SKILL.md` bodies, both cheatsheets,
  `skill-map.md`, `SKILL_INSTALLATION.md` (per-host sections), pack
  `compatibility:`/config surfaces, `workflow-recipes.md` §Parallel Lens Review,
  `validate_record_hygiene.py`, parity/contract test mechanics
  (`test_cheatsheet_*`, `test_prompt_cross_links.py`, `test_dormant_item_watch.py`,
  `test_skill_module_contract.py`).
- Executed today at `8fda8c8`: `make all` (899 passed; 147 files 0 errors lint +
  links; 11/11 governance; record hygiene green; ROUTE-001/002/003 100%).
- Not executed: any live-host install, any real-user routing session, any
  provider-parallel review (quota-blocked; see Execution mode). Claims resting
  on those are tagged [INFERENCE] above.

## Candidate Adoption Ledger

| ID | Candidate | Status | Evidence | Next action / trigger |
| --- | --- | --- | --- | --- |
| SOLO-2 | implement Small-Change Fast Path | **adopted 2026-07-12** | observed ceremony/purpose contradiction; recurrence `unknown` | guard: fast-path heading + verification-never-collapses line |
| SOLO-3 | dispatch ladder direct-to-implement note | **adopted 2026-07-12** | observed ladder-vs-route-table tension | guard: ladder note line |
| DOC-1 | implement covers repo doc/content edits | **adopted 2026-07-12** | observed repo practice (Markdown governance edits) | guard: trigger wording |
| DOC-2 | "Doc edit not review" boundary cue (EN+zh) | **adopted 2026-07-12** | same as DOC-1 | guard: cue in both cheatsheets |
| ZH-1 | zh co-landing of adopted cues | **adopted 2026-07-12** | parity policy + tests | enforced by cheatsheet parity guards |
| ENT-2 | risk egress trigger + §2a cross-link | **adopted 2026-07-12** | observed missing inbound link to M7 stanza | guard: egress bullet + surfaces line + registry |
| GREEN-1 | brief spike/exploration framing | **adopted 2026-07-12** | textual tension observed; demand [INFERENCE] | guard: spike stanza |
| GREEN-2 | spike boundary cue (EN+zh) | **adopted 2026-07-12** | same as GREEN-1 | guard: cue in both cheatsheets |
| LONG-1 | handoff ledger bridge | **adopted 2026-07-12** | observed three unbridged ledger conventions | guard: bridge sentence |
| HOST-1 | install fallback for no-skill hosts | **adopted 2026-07-12** | observed doc gap; failure evidence none | guard: fallback heading |
| ENT-1 | incident/break-glass clause in risk | **deferred** | would weaken a safety gate; [INFERENCE] demand | re-open on a real incident-response deadlock + explicit Human Review |
| LONG-2 | dispatch mid-task re-route cue | **deferred** | partially duplicates existing trigger; [INFERENCE] | re-open on observed mid-session re-route confusion |
| ZH-2 | per-skill zh localization beyond cheatsheet | **deferred** | existing roadmap gate unchanged; no new evidence | re-open on zh-user routing-failure evidence |

Deterministic guards for adopted rows:
`plans/tests/test_skill_scenario_panel_adoption_state.py`.

## Falsifiability

Wrong if: an adopted surface is absent while its ledger row claims adoption
(guard test contradiction → `make all` red); if the fast path is observed used
to skip verification (then SOLO-2's wording failed and must tighten); if real
usage evidence shows doc edits routing to review-for-revision anyway (then
DOC-1/DOC-2 cues are dead text and should be re-litigated); if deferred rows
(ENT-1, LONG-2, ZH-2) are adopted later without their named triggers or
re-litigation (ledger discipline failure); or if a future panel reproduces this
review with true parallel lenses and overturns a consensus item (single-host
execution bias made material).
