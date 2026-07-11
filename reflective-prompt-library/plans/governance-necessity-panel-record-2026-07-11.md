# Governance Necessity Panel Record — 2026-07-11

## Purpose

Record the adversarial review requested as: **"The necessary reasons of nine frozen core + two registered domain packs, if not why keep these rules. Fully exam all the rules and constraints of this project."**

This remains a governance/methodology judgment artifact, not an agent operating rule by itself. After the review, the user explicitly directed **"Do the consensus now"**, satisfying Human Review for actionable candidates N2–N7, N9, and N10. Their authority comes from the amended canonical policy, consumer surfaces, validators, and guards named below—not from this record alone.

## Scope and packet

The review used `04-agent/workflow-recipes.md` § Parallel Lens Review and the host-side `parallel-lens-review-packet` execution manual. A temporary repo-root packet, `review-packet-governance-necessity-2026-07-11.md`, enumerated 33 rules (A1–G3), prior decisions, observed state, and eight named tensions:

- exception versus promotion-gate integrity;
- whether the domain-pack tier is necessary;
- evidence-chain circularity;
- why the core count is exactly nine;
- adoption-guard phrase-pin creep;
- falsifier discharge versus exception bypass;
- governance cost;
- two-tier wording and installation drift.

Claims below retain the packet's evidence classes:

- `observed`: read or executed in this session;
- `author-claimed`: present in a prior record but not reproduced;
- `[INFERENCE]`: panel reasoning, not observed fact.

## State at review time

- `observed`: branch `main`, HEAD `13fcc16`, clean worktree before the temporary packet.
- `observed`: `make all` from the repository root passed: 772 pytest tests plus all validators and ROUTE-001/002/003 at 100% consistency. The route result is regression-fixture evidence, not semantic-routing proof.
- `observed`: 11 `skills/*/SKILL.md` directories: nine names in `CORE_SKILLS` and two names in `DOMAIN_PACK_SKILLS` (`flow-control-generator`, `flow-loop-harness`).
- `observed`: registry membership, core count, required governance metadata, domain-pack self-label, and example presence are mechanically checked. Domain-pack exclusion from the live `reflective-dispatch` route table, panel approval, recurrence, and Human Review are not fully machine-enforced.

## Panel lenses

Six distinct same-host reviewer lenses were used; these are review roles, not claims that six named provider models were invoked:

1. constitutional necessity / first-principles auditor;
2. two-tier registry and wording-drift auditor;
3. evidence genealogy / falsifiability auditor;
4. governance cost accountant;
5. rival-constitution architect;
6. rule-to-enforcement trace auditor.

The initial task backend returned complete reports for four lenses but `resource_exhausted` for two. The two empty lenses were retried as the skill requires; the retry also exhausted. They were recovered through alternative in-harness task agents. One recovery returned terse JSON and one reported a file; continuation agents expanded the former, and the reported file was verified in the main worktree before use. This recovery history lowers confidence in those two lenses relative to the four original reports. All six final verdicts were `AGREE WITH CHANGES`.

## Panel Consensus

### Decision

**`AGREE WITH CHANGES`.** Keep the current bounded core routing surface and keep the two packs outside core routing for now, but stop treating the integer nine or the current count two as intrinsically necessary.

### Direct answer: nine frozen core + two registered domain packs

| Claim | Verdict | Why keep it now | What would falsify or change it |
| --- | --- | --- | --- |
| A bounded, mechanically registered **core routing surface** | **Necessary** for the current architecture | `reflective-dispatch`, cheatsheets, canonical `context_load`, route fixtures, examples, and benchmark coverage assume a closed route set. An unbounded set creates silent trigger overlap and parity drift. | A replacement registry/router that safely discovers arbitrary skills with measured routing parity and no consumer confusion. |
| The exact core cardinality **nine** | **Useful-not-necessary; historical** | The nine names cover the present task lifecycle and no tenth core candidate has met the gate. Keeping the current set avoids gratuitous routing churn. The June panel froze the set that existed; it did not derive nine as an optimal number. | A verified recurring core workflow gap that cannot fold into the nine, plus Human Review and holdout evidence; or evidence that two existing core skills should merge. |
| A three-recurrence gate for a tenth core skill | **Useful conservative evidence floor, not a law of nature** | Cheap anti-bloat control; forces a durable local-gap argument before expanding every routing/governance surface. The threshold itself is not empirically derived. | Evidence that the gate repeatedly blocks valid core workflows, or a superior measurable promotion rule. User direction alone does not prove recurrence. |
| A separate registered **domain-pack tier** | **Useful-not-necessary as a design; load-bearing once packs ship** | It acts as a routing firewall: installable script-generation contracts stay outside the fairness-tested core route table. The registry prevents hidden/unregistered `SKILL.md` directories. | A flat registry with enforced tier metadata and host filtering; demotion of packs to recipes/host-side skills; or routing holdouts that justify honest core admission. |
| The exact number **two** domain-pack skills | **Not a rule; current inventory only** | Generator and loop harness have different host-risk metadata (`human_review_required: false` versus `true`) and different control-flow contracts. | Existing P6 trigger: if either sees zero solo use by 2026-10-11, re-litigate merge/demotion. No current usage telemetry proves lasting demand. |
| The 2026-07-11 user-directed exception as a general admission channel | **Not established** | The flow-pack record documents one explicit exception with recurrence `unknown`, guards, and demotion triggers. A non-authoritative record cannot silently create a universal policy. | Explicit Human Review adopting a binding domain-pack admission rule in `06-repo/AGENTS.md`. Until then, future additions cannot cite this one record as automatic permission. |

### Bottom line

The **cap and routing boundary** are the necessary parts. **Nine and two are current design state**, not sacred constants. The domain-pack tier should be kept provisionally because removing it now requires either routing the packs as core skills or demoting them; neither has supporting usage/routing evidence. Its admission rule must be made explicit before the pattern is reused.

## Full rule-and-constraint examination

Verdict vocabulary:

- **Necessary**: removal exposes a concrete failure mode in the current architecture.
- **Useful-not-necessary**: cheap, proportionate insurance or clarity; alternatives exist.
- **Ceremonial/duplicate**: no independent failure mode; retain only as a pointer or remove when authorized.

### A. Skill-surface rules

| ID | Rule | Verdict | Evidence and failure mechanism |
| --- | --- | --- | --- |
| A1 | Nine frozen core skills; gated-not-never | **Necessary cap / useful-not-necessary number** | `observed`: registry and count guards failed when the flow packs first appeared outside the accepted set. `author-claimed`: June froze the set without a cardinality proof. |
| A2 | Tenth core needs three recurrences + Human Review | **Useful-not-necessary threshold; Human Review necessary** | Prevents one-session/external-interest promotion. The recurrence count is prose-only and not empirically calibrated; it applies to core promotion, not automatically to packs. |
| A3 | Registered domain-pack tier, outside core routing | **Useful-not-necessary architecture; necessary integrity mechanism while packs exist** | Registry/self-label/examples are checked. Panel approval, dispatch exclusion, and demotion semantics are partly prose. The binding admission channel is missing. |
| A4 | Frontmatter governance metadata | **Necessary** | Hosts/validators need name, description, risk, review, I/O, and context-load metadata. New finding: `CONTRIBUTING.md` calls `license` required while validators only recommend it; this must be reconciled. |
| A5 | Module Contract (Trigger/Methods/Output/Never/Escalation) | **Necessary** | Stable invocation/output/risk contract. Strict subsection checks cover core skills; domain packs rely partly on non-failing lint warnings. |
| A6 | Worked example of at least 200 characters | **Useful-not-necessary** | Cheap protection against empty/non-actionable skill contracts. Length is only a proxy for quality. |

### B. Routing rules

| ID | Rule | Verdict | Evidence and failure mechanism |
| --- | --- | --- | --- |
| B1 | Strictness L1–L6 before skill choice | **Necessary** | Prevents L3/L4 ceremony on trivial work and silent under-review on high-risk work. |
| B2 | Equivalent intent routes equivalently with visible trace | **Necessary** | Prevents hidden rigor downgrade and inconsistent canonical routes. Fixtures prove regression consistency only; R1–R12 are not all behaviorally proven. |
| B3 | Holdout-before-tune; fixtures are not semantic proof | **Necessary** | `observed` history records verifier-artifact phrases misrouting before tuning and passing after holdouts + tuning. |
| B4 | Multi-voice panel is optional research method, not core skill | **Useful-not-necessary, keep** | Avoids another overlapping route; one research/review pass remains the ceremony falsifier. A dedicated skill remains possible only after recurrence and routing evidence. |

### C. Authority and knowledge rules

| ID | Rule | Verdict | Evidence and failure mechanism |
| --- | --- | --- | --- |
| C1 | `PROJECT_KNOWLEDGE.md` is non-authoritative; binding rules migrate | **Necessary** | Prevents a second, stale agent constitution. Mechanically checked with acknowledged semantic limits. |
| C2 | Read relevant PK section before architecture/governance decisions | **Useful-not-necessary** | Reduces re-litigation and non-goal drift; must remain targeted to avoid context bloat. |
| C3 | Root `AGENTS.md` is an authority stub; memory snapshot is historical | **Necessary** | Prevents regenerated/stale memory text from overriding canonical harness policy. |
| C4 | English canonical; zh-TW covers navigation/routing aids | **Useful-not-necessary** | Controls translation drift. Full localization remains a resource/product choice, not a safety theorem. |

### D. Promotion and adoption rules

| ID | Rule | Verdict | Evidence and failure mechanism |
| --- | --- | --- | --- |
| D1 | Local-gap gate; external interest is not local recurrence | **Useful-not-necessary, keep** | Prevents trend-following from becoming durable surface area. It is a judgment rule; a counter would create false assurance. |
| D2 | Fail-closed prompt-injection, supply-chain, and memory-write gates | **Necessary for promotion claims** | Prevents imported/memory-derived instructions from laundering authority. Tests pin selected wording, not operational behavior; TeaPrompt cannot enforce host runtime guarantees. |
| D3 | Candidate Adoption Ledger + guards for adopted changes | **Useful-not-necessary; justified by one observed drift incident** | The 2026-07-06 candidates were partial/untracked until re-litigation. Permanent literal-phrase pins can recreate the doc-echo problem; guard scope needs a closure rule. |
| D4 | `reflective-handoff-retro` owns promotion candidates; Human Review for PK | **Useful single owner / necessary Human Review** | Prevents ambiguous promotion ownership and unauthorized rule elevation. |
| D5 | Acquisition L0–L4 ladder; recurrence before team standard | **Useful-not-necessary** | Separates a note/lens/SOP/skill/verifier/runner and prevents methodology from being mislabeled operationalization. |

### E. Standing non-goals

| ID | Rule | Verdict | Evidence and failure mechanism |
| --- | --- | --- | --- |
| E1 | No TeaPrompt-owned runtime/swarm/recorder/replay/enforcer | **Necessary product boundary** | Keeps a portable prompt/skill library from making runtime guarantees it cannot test or support. |
| E2 | Methodology-complete does not mean operationally complete | **Useful-not-necessary, keep as cheap caveat** | Prevents readers inferring persistence/idempotency/replay from prompt coverage. Overlaps E1/E3 but addresses a recurring category error. |
| E3 | Skills may declare runtime needs; host code/tests must enforce | **Necessary safety boundary** | Prompt text cannot guarantee permissions, isolation, cancellation, or side-effect controls. |
| E4 | No full `SKILL.md` localization by default | **Useful-not-necessary** | Limits drift and maintenance. Revisit on measured consumer demand, not governance identity. |
| E5 | Holdout expansion precedes router tuning | **Duplicate of B3/R8** | No separate mechanism. Keep only as a high-traffic pointer to `ROUTING_CONTRACT.md` R8 rather than an independent rule. |

### F. Execution discipline

| ID | Rule | Verdict | Evidence and failure mechanism |
| --- | --- | --- | --- |
| F1 | Strictness-scaled L1–L4+ Required Workflow | **Useful-not-necessary; correctly scoped** | Prevents both ceremony and under-gating; largely honor-system. |
| F2 | Human Review for nine high-blast-radius categories | **Necessary** | Prevents unauthorized irreversible/security/privacy/public-interface actions. Category detection cannot be fully reduced to text tests. |
| F3 | Anti-cheating rules | **Necessary** | Prevents reward-hacking verification. Prose-only by nature; grep-based enforcement would be false assurance. |
| F4 | Context Engineering | **Useful-not-necessary** | Reduces context exhaustion and stale chat state; overlaps strictness and research state-budget guidance. |
| F5 | `make all` from repo root before governance/routing verification claims | **Necessary** | Only integrated local proof of registry, links, fixtures, routing regression, and tests. Green does not prove semantic correctness. |
| F6 | Eight-section Review Standard | **Useful at L4+/handoff; ceremonial if forced globally** | Preserves risks, traceability, and remaining work. The strictness-scaled workflow must remain the scope authority. |

### G. Record discipline

| ID | Rule | Verdict | Evidence and failure mechanism |
| --- | --- | --- | --- |
| G1 | Disclaimer, evidence tiers, falsifiability | **Useful-not-necessary, keep** | Makes claims auditable. Falsifiers are real only when exception paths and triggers cause re-litigation rather than being narrated after the fact. |
| G2 | Decision Index is a map; historical headers instead of deletion | **Useful-not-necessary** | Preserves causal evidence and links while limiting active-policy confusion. |
| G3 | Parallel-lens packet/verdict/ledger protocol | **Useful-not-necessary; ceremony-gated** | This review found a binding-policy gap, install-scope defect, enforcement overclaims, and metric ambiguity; it was not ceremony here. It remains inappropriate for routine L1–L2 work. |

## Enforcement reality

The rulebook must not imply that 772 tests enforce all governance behavior.

### Mechanically strong

- registered skill-set equality and exact nine-core count;
- canonical core `context_load` table;
- required governance metadata values;
- domain-pack body self-label;
- presence/length of examples;
- core Module Contract structure;
- project-knowledge authority markers;
- link and prompt-corpus registry parity;
- deterministic route-fixture consistency and trace coverage.

### Partial or phrase-level

- domain packs are absent from fixture `VALID_WORKFLOWS`, but no test directly scans the dispatch route table for pack names;
- domain-pack Module Contract subsections are lint warnings/suggestions rather than strict failures;
- domain-pack self-label has production validation but no focused negative pytest;
- the validator checks packs are absent from `CANONICAL_CONTEXT_LOAD`; it does **not** and should not forbid them from using the shared enum values `low|medium|high`;
- M1/M2 and earlier adoption guards validate headings/tokens/selected phrases, not runtime behavior;
- route fixtures cover seeded phrases, not all R1–R12 or real user distributions.

### Prose/judgment rules that should remain prose

- three genuine recurrences;
- explicit Human Review approval;
- strictness choice in a live session;
- local-gap quality;
- anti-cheating intent;
- context relevance.

Mechanical proxies for those would create false confidence.

## New findings beyond the packet

1. **Installation breaks the conceptual tier.** `SKILL_INSTALLATION.md` lists only nine core skills, but repeated `skills/*` copy/symlink commands install all entries under `skills/`, including both domain packs and non-skill files/directories. A consumer cannot currently choose "core only" versus "core + packs" consistently. This is an observable product defect, not merely wording drift.
2. **License schema drift.** `CONTRIBUTING.md` presents `license` as required frontmatter; `validate_links.py` treats it as optional/recommended. Either make it required for portable skill directories or correct the contribution contract.
3. **The cost ratio is not reproducible historically.** Under an explicit narrow formula measured now—product = all Markdown under `skills/` plus `00-core`–`06-repo`; meta = `plans/*.md` plus `plans/tests/*.py`—the counts are 7,092 product lines and 13,081 meta lines, ratio 1.844:1. The prior ~2.45:1 record does not define a matching denominator, so improvement/degradation cannot be claimed. Do not rewrite historical evidence to 1.844.
4. **Adoption guards are mixed, not uniformly defective.** Exact prose pins such as "nine frozen workflow skills" are D1-risky. Structural headings, registry parity, verdict tokens in a Markdown protocol, and executable-template symbols (`MIN_OK`, `RESUMED`) defend real contracts. The three adoption modules cannot honestly be blanket-labeled either behavioral or doc-echo.

## Candidate Adoption Ledger

The review initially deferred policy edits for Human Review. The user's subsequent explicit instruction adopted the actionable consensus; the ledger now distinguishes implemented rows from rejected and still-trigger-gated rows.

| ID | Candidate | Status | Evidence | Next action or trigger |
| --- | --- | --- | --- | --- |
| N1 | Keep a bounded nine-name core registry and keep the two current packs outside core routing | **No-change / keep** | Six-lens consensus; current registry, dispatch, and route fixtures | Re-open only on a verified core gap, pack demotion, or a replacement tier-aware router. |
| N2 | Amend `06-repo/AGENTS.md` with one binding domain-pack admission rule: registered, host-invoked, not dispatch-routed; explicit Human Review + panel ledger + demotion trigger; user direction may establish approval but recurrence remains `unknown` | **Adopted 2026-07-11 — explicit Human Review** | `06-repo/AGENTS.md` item 3; `GLOSSARY.md` Adoption Guard Closure | Future pack additions must satisfy this rule; it never waives tenth-core promotion. |
| N3 | Add one canonical two-tier gloss and pointers in root/library README, `CONTRIBUTING.md`, `METHODOLOGY_MAP.md`, and PK; avoid duplicating the full rule everywhere | **Adopted 2026-07-11** | Public surfaces point to `skills/skill-map.md` or canonical policy | Detailed admission wording remains single-source in `06-repo/AGENTS.md`. |
| N4 | Repair `SKILL_INSTALLATION.md`: core-only default; explicit optional domain-pack install; copy/symlink only directories containing `SKILL.md` | **Adopted 2026-07-11** | Four core/pack copy/symlink helpers; macOS `/bin/bash` smoke matrix produced exactly 9 core + 2 pack directories | Keep default core-only; registry-parity test guards explicit pack names. |
| N5 | Add cheap structural guards: pack names absent from dispatch route rows; domain-pack self-label negative test; pack example pytest mirror; full Module Contract parity for packs | **Adopted 2026-07-11** | Existing `test_validate_governance.py`, `test_validate_skill_examples.py`, `test_skill_module_contract.py`, and `test_readme_governance.py` strengthened | Do not add a meaningless "pack context_load must differ" guard. |
| N6 | Reframe "nine" as current core cardinality, not optimal number | **Adopted 2026-07-11** | Canonical policy, README surfaces, methodology map, PK, skill map, and cheatsheet introductions | Exact registry count remains mechanically guarded while the set stays nine. |
| N7 | Define adoption-guard closure: temporary phrase pins retire or become structural after adoption; permanent guards must defend structure, registry parity, executable behavior, or stable protocol tokens | **Adopted 2026-07-11** | `GLOSSARY.md` § Adoption Guard Closure; adoption tests narrowed; touched governance tests made order-independent | Audit each assertion; do not blanket-delete feature/source-contract checks. |
| N8 | Replace the historical ~2.45 meta:product claim with 1.844 | **Rejected** | Formulas are not comparable; the recovered lens initially measured the wrong denominator | If this metric remains useful, first define and guard a stable numerator/denominator; otherwise retire it. |
| N9 | Fold duplicate E5 wording to a pointer to B3/ROUTING_CONTRACT R8 | **Adopted 2026-07-11** | PK Standing Non-Goals now points to R8 and retains the regression-guard caveat | `ROUTING_CONTRACT.md` remains canonical. |
| N10 | Reconcile `license` frontmatter: required versus recommended | **Adopted 2026-07-11 — license required** | `validate_links.py` requires `name`, `description`, `license`; focused negative pytest | Preserve portable licensing for independently copied skill directories. |
| N11 | Merge/demote one of the two packs now | **Deferred under existing P6** | Distinct Human Review defaults; no usage evidence | Re-litigate 2026-10-11 if either skill has zero solo invocations; instrument evidence manually because TeaPrompt has no telemetry. |
| N12 | Add pack trigger phrases to core router now | **Deferred under existing P7** | Trigger collision is plausible but unmeasured | Holdout-before-tune: first add ROUTE-002/003 groups, then decide whether dispatch should route to packs at all. |
| N13 | Add same-host evidence-tier caveat to every historical panel record | **No mass edit** | Several records already state the same-host/advisory caveat; rewriting history adds churn | This record states it. Add caveat to future records through the existing packet contract. |

## Adoption Update — Explicit Human Review

The adopted scope is deliberately narrower than "change everything":

- N2–N7, N9, and N10 are implemented at their named surfaces.
- N8 remains rejected because the historical ratio is not reproducible under a matching formula.
- N11/P6 remains deferred until the 2026-10-11 solo-invocation trigger.
- N12/P7 remains deferred until fresh ROUTE-002/003 holdouts exist before tuning.
- N13 remains no-mass-edit; future records inherit the evidence-tier contract.
- No pack was merged, promoted into the nine core routes, or added to `reflective-dispatch`.

Focused implementation evidence before the full repository gate:

- macOS `/bin/bash` copy/symlink smoke matrix: exactly nine core directories and two optional pack directories; the first run caught and corrected BSD `cp -R` trailing-slash flattening;
- license validator: 3 focused tests passed;
- domain-pack/Module Contract/README/adoption guards: 76 focused tests passed;
- isolated governance/adoption modules: 55 focused tests passed after removing test-order dependence.

Full repository gate after adoption: `make all` collected and passed 782 tests;
all validators passed; ROUTE-001/002/003 remained at 100% seeded-fixture
consistency (128 / 114 / 66 phrases). This is regression evidence, not semantic
routing proof.

## Falsifiability audit

The five reviewed records have testable clauses, but most are live future conditions rather than "discharged" facts:

| Record | Clause class | Status here |
| --- | --- | --- |
| `workflow-possibilities-constraints-review-2026-07-06.md` | constraints block a qualifying workflow; candidates never adopted/re-litigated | Candidate-drift half was honestly re-litigated. Workflow-blocking half remains live. |
| `governance-rules-rethink-review-2026-07-11.md` | ledger drift, blocked workflow, workflow-toil counterevidence, successful disputed merges | Clause (b) did **not** fire: the flow packs did not meet the recurrence gate and were admitted through a separate user-directed exception. The exception exposes ambiguity, not a logically fired falsifier. |
| `flow-control-pack-panel-record-2026-07-11.md` | unregistered skill ships, adopted surfaces disappear, P6/P7 triggers ignored | Registry/surface guards are currently green; P6/P7 remain live. Green now is not final discharge. |
| `flow-coverage-panel-record-2026-07-11.md` | missed worthy mechanism; P12/P13 triggers ignored | Coverage was reviewed, but both clauses remain falsifiable by future evidence. |
| `managed-skill-promotion-panel-record-2026-07-11.md` | missed recurring skill; M1 ceremony; deferral-trigger drift | All remain live. M1 is not ritual merely because its future ceremony falsifier has not fired. |

The strongest valid circularity criticism is narrower: the **specific nine count** traces to the set that existed in June, and later panels often cite earlier panels. The cap also has independent mechanical rationale; therefore the whole constitution is not circular.

## Rival constitutions considered

| Alternative | Benefit | First concrete loss | Decision |
| --- | --- | --- | --- |
| No freeze; semver/deprecate arbitrary skills | Honest evolution, no sacred count | Expands routing, metadata, fixture, docs, and collision surface without a qualifying gap | Reject now; migration trigger N1. |
| Flat registry with `tier` metadata | One registry, honest 11-count | Current hosts/install docs do not reliably filter tiers; requires a real tier contract | Plausible future replacement; trigger when host filtering is portable or packs grow materially. |
| Treat packs as core skills 10–11 | Disk count equals routing count | Trigger collisions and route fairness are unmeasured; changes product semantics | Reject until P7 holdouts justify it. |
| Keep packs only as `04-agent` recipes | Restores nine-only skill tree | Removes requested installable script-generation contracts and metadata | Demotion option if P6 fires. |
| Keep packs only as host managed skills | No TeaPrompt pack governance | Not portable to library consumers; user-directed repo deliverable disappears | Reject while the repo pack remains used. |
| CI only; no panels/ledgers | Lower meta overhead | Repeats the observed 2026-07-06 candidate-adoption drift; loses decision rationale | Reject wholesale; slim guards under N7 instead. |
| Pure docs; remove validators | Minimal governance code | Silent registry/link/routing/authority drift | Reject while the project claims evidence-backed verification. |

## Shared Findings

1. The necessary invariant is **bounded, explicit routing**, not the number nine.
2. The pack tier is a defensible routing firewall but also a same-day compromise that preserved the nine-core story. Both statements are true.
3. The flow-pack exception did not prove a general pack admission rule. Binding policy is still missing.
4. Most high-stakes rules are judgment/prose rules. The test count must not be sold as behavioral enforcement of recurrence, Human Review, or anti-cheating.
5. Structural validators provide real value. Literal phrase pins provide mixed value and need a closure policy, not blanket deletion.
6. The two-tier model is currently least coherent at installation time.
7. Same-host consensus is advisory/model-vote-tier evidence. The panel's force comes from cited repository evidence and executed checks, not six votes.

## Disagreements / Residual Risks

- **Exact nine:** all lenses retained a bounded core; several called nine historical/ritual. No lens demonstrated that eight or ten would fail after the necessary routing migration. Current no-change is a stability choice, not proof of optimality.
- **Tier architecture:** some lenses called it load-bearing; others called it a pressure-release valve. Synthesis: it is not the only architecture, but it is now load-bearing until packs are rerouted or demoted.
- **Three-recurrence threshold:** no operator dataset validates three specifically. It remains conservative, cheap policy—not scientific law.
- **Cost:** the recovered cost lens initially used an incomplete denominator and invented time estimates. Those claims are rejected. Independently measured line counts are reported only under a named formula; no trend claim is made.
- **Falsifiability:** the recovered circularity lens overcalled several live future falsifiers as discharged and simultaneously called one record discharged/unfalsifiable. The synthesis corrects that contradiction.
- **No usage telemetry:** the 2026-10-11 pack trigger currently depends on manual evidence. `unknown` must not become "zero" or "used" by assumption.

## Evidence Actually Checked

### Executed

- `make all` from repository root: 772 tests passed; validators passed; route fixtures green.
- repository state before packet: `main`, HEAD `13fcc16`, clean.
- structured line-count computation using the harness glob results and file reads:
  - 25 Markdown files under `skills/`: 3,001 lines;
  - 52 Markdown files under `00-core`–`06-repo`: 4,091 lines;
  - 35 `plans/*.md` files: 8,042 lines;
  - 44 Python files under `plans/tests/`, of which 42 are `test_*.py`: 5,039 lines;
  - three adoption-state modules: 314 lines.

### Read directly in the host session

- canonical `06-repo/AGENTS.md`, `PROJECT_KNOWLEDGE.md`, README surfaces, `GLOSSARY.md`, skill map, EN cheatsheet, installation guide, root `CONTRIBUTING.md`;
- skill registries and governance/link/lint validators;
- registry, promotion, coverage, managed-skill, and prior governance panel records;
- the three adoption-state test modules and domain-pack validator tests;
- both domain-pack frontmatter/self-labels.

### Lens-read / reported

- June freeze rounds and source reflections;
- broader route/eval test inventory;
- alternative architecture comparisons against the project's 2026-06 external-tool surveys.

### Not established

- no external provider/model calls were made for this panel;
- no fresh external platform research was needed or performed;
- no real consumer routing distribution, pack invocation telemetry, or operator-toil dataset exists;
- historical ~2.45 meta:product ratio is not reproduced under a documented matching formula.

## Falsifiability

This record is wrong if any of the following occurs and the conclusion is not corrected:

1. a tenth core workflow repeatedly meets the local promotion gate and cannot be represented by the existing nine, but the bounded-core rule still blocks it;
2. domain packs can be safely flattened into a portable tier-aware registry without route/install ambiguity, yet this record's provisional firewall rationale is still cited to prevent migration;
3. P6 or P7 triggers fire and no re-litigation occurs;
4. the installation commands are shown to install exactly the intended tier for every documented host despite the current `skills/*` behavior;
5. a stable, documented cost formula reproduces the historical baseline and demonstrates a trend opposite to this record's agnostic conclusion;
6. a supposedly structural guard passes while its named contract is behaviorally absent, or a phrase pin is removed and the predicted adoption drift does not recur—evidence for revising N7 either way.
