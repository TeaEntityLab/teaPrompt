# External-Adoption Case Studies — 2026-06-20

## Dispatch

Synthesize the recent "should TeaPrompt adopt this external tool/method?"
evaluations into one case study, and capture the recurring evaluation procedure
so future sessions do not re-derive it from scratch or re-litigate settled
outcomes.

## Why This Record Exists

Each individual evaluation correctly produced a small or null change. This record
is not a duplicate of them: it captures the pattern *across* them — the same
evaluation method, re-run each session, plus the fact that three outcomes had no
record and would otherwise be re-litigated. The synthesis crosses the project's
own promotion gate (≥3 cross-session recurrences); the individual tools did not.

## Case Comparison

| Date | External item | One-hand source verified | Verified local gap? | Outcome | Record |
| --- | --- | --- | --- | --- | --- |
| 2026-06-13 | agentic-sop-to-work | repo + CHANGELOG | concept under-specified | Adopt SOP-compiler concept at prompt layer; defer runner | [agentic-sop](agentic-sop-workflow-reflection-2026-06-13.md) |
| 2026-06-17 | Knowie | repo | no project-rationale layer | Adopt minimal project-knowledge contract; reject full toolchain | [knowie](knowie-project-knowledge-reflection-2026-06-17.md) |
| 2026-06-18 | STORM / Co-STORM | README + NAACL/EMNLP papers | **yes** — no question-space expansion | Fold optional perspective-discovery into `reflective-research` | [storm](storm-perspective-discovery-reflection-2026-06-18.md) |
| 2026-06-20 | Loop-Skill | GitHub API (created 2026-06-17, no LICENSE, 19★, single-day) | no | No change — methodology complete, runtime is a non-goal, gate unmet | this file |
| 2026-06-20 | preflight-checker | GitHub API (created 2026-06-19, no LICENSE, 0★, 0.1.0) | no | No change — UX patterns already in `reflective-review`; missing items out of scope | this file |
| 2026-06-20 | Codex Record & Replay | OpenAI official docs | operational, not methodological | No change *to TeaPrompt* — the gap is real but operational (acquisition / persistence / replay), which is a standing non-goal; R&R is vendor-locked and uncopyable. Worth using as an external acquisition front-end | this file |
| 2026-06-21 | Hyperplan / multi-agent adversarial planning (OMO) | GitHub repo (code-yeongyu/oh-my-openagent) SKILL.md | no — runtime hits non-goals; methodology mostly covered | No change — Hyperplan runtime is agent swarm + runtime engine (both non-goals); methodology layer overlaps existing lenses; three possible gaps (Defend/Refine/Concede, Evidence Grade, Assumption Ledger) not promoted | this file |
| 2026-06-25 | OpenFugu | GitHub repo + arXiv + HF APIs + local clone | no — mechanism useful, runtime/adoption blocked by artifact, license, and egress risks | No runtime adoption; reference-only; TRINITY hands-on deferred until `model_iter_60.npy` / safetensors boundary fixed | [research](openfugu-research-record-2026-06-25.md), [brief](openfugu-technical-brief-2026-06-25.md), [plan](openfugu-reference-plan-2026-06-25.md) |
| 2026-06-25 | Skills, memory, and agent tooling survey | upstream repos/docs for Superpowers, Spec Kit, Karpathy skills/autoresearch, mem0, ChatGPT Memory, LLM Wiki, MemPalace, Hermes Agent, Oh My Pi, Oh My OpenAgent | mostly no — methodology already covered; memory/runtime surfaces are non-goals unless a local app/runtime gap appears | No new core skill, runtime, or memory dependency; keep as references and reuse existing `reflective-*` workflows plus Markdown project knowledge | [skills](skills-and-spec-systems-research-2026-06-25.md), [memory](memory-mechanisms-research-2026-06-25.md), [tooling](agent-tooling-research-2026-06-25.md) |
| 2026-07-13 | Baton / `baton-dispatch` v0.1.1 | GitHub repository/API + pinned skill/reference files + Anthropic official article | no — methodology present/adjacent; consolidated-checklist recurrence `unknown` | Study/reference only; no TeaPrompt skill, lens, verifier, dependency, or runtime adoption; empirical reproduction deferred | [survey](baton-dispatch-survey-2026-07-13.md) |
| 2026-07-13 | DilinAI Nuwa + Jiyao / team memory officer | five public share/API snapshots + platform terms + NASA, Anthropic, and Claude official sources | no — methodology present/adjacent; source-lineage recurrence `unknown`; runtime is a non-goal | Study traceability and artifact separation; no TeaPrompt prompt, skill, role, verifier, dependency, or runtime adoption; outcome reproduction and installation blocked | [survey](dilinai-nuwa-jiyao-survey-2026-07-13.md) |
| 2026-07-16 | fable-method v1.4.0 | GitHub repo/API + pinned clone + arXiv + upstream issue #3 | yes, narrow — forced-artifact gates absent from `reflective-implement`/`reflective-risk`; demonstrated by same-day deterministic reproduction (capable-tier control ran the unauthorized deploy 3/3; treatment 0/3) | Study strongly; FM1/FM2 adopted 2026-07-16 as narrow wording repairs to `reflective-implement` / `reflective-risk`; FM3 deferred; FM4 rejected; no new TeaPrompt skill, lens, verifier, dependency, or runtime surface | [survey](fable-method-survey-2026-07-16.md) |
| 2026-07-24 | Claude Code v2.1.218 prompt snapshot | Piebald pinned repo + public extractor/updater + official npm/native package spot-check | yes, three narrow contract gaps; runtime/product mechanisms remain out of scope | Study; partially adopt original CCSP1–CCSP3 wording repairs; defer digest binding; reject auto-mutation/micro-fragment architecture; no new skill, route, dependency, or runtime | [survey](claude-code-system-prompts-survey-2026-07-24.md) |
| 2026-08-04 | agnix v0.45.0 + agent-skills-hook | GitHub repos + pinned clones + local build/test/self-lint/eval reproduction + lens web checks | no — agnix concepts already covered or concept-only (AX1/AX2), binary gate rejected (AX3); skills-hook blocked by observed license violations, unpinned supply chain, and destructive installers | Study only; agnix additionally recommended user-side as a version-pinned personal linter outside repo governance; no TeaPrompt skill, lens, verifier, dependency, or runtime adoption | [survey](agnix-agent-skills-hook-survey-2026-08-04.md) |
| 2026-08-06 | Prime Agent v0.7.0 | GitHub repo + pinned clone + local Python-runtime test reproduction + 7-lens source reads | patterns only — structured state ledger (PA-1) and auto-refine gate (PA-2) deferred with triggers; runtime rejected (PA-4); deployment blocked by extension auto-load RCE and harness wipe risk (PA-5) | Study & reproduce patterns; no TeaPrompt skill, lens, verifier, dependency, or runtime adoption | [survey](prime-agent-survey-2026-08-06.md) |
| 2026-08-12 | AI-assisted team throughput / unlimited-token discussion | original X post + user-provided capture + DORA, Microsoft Research, MIT Media Lab, METR, and Leroy source checks + 7-lens review | no governed-surface gap — cost, bounded flow, evidence gates, handoff, review, and Human Review are already covered; local recurrence for proposed refinements is `unknown` | Study the warning signal; adopt only the English record, cross-link, and guard; reject hard session/retry limits, AI-only proof, new skill/coordinator/runtime, and humans-only-at-the-edges policy | [review](ai-assisted-team-throughput-review-2026-08-12.md) |
| 2026-08-20 | 3xa-harness bundle-v0.1.0 | GitHub repo/API + pinned clone + local self-check/manifests/audit runs + adversarial verifier mutations + 7-lens source review | no — methodology already covered; 3XA-1/2 remain study-only with local triggers; executable tools are weaker than their protocol and unsafe unchanged | Study and reproduce pinned mechanisms only; no TeaPrompt skill, lens, verifier, dependency, or runtime adoption; deployment blocked by containment, provenance, verifier, CI, and install-lifecycle gaps | [survey](3xa-harness-survey-2026-08-20.md) |
| 2026-08-20 | J-Space Cognition Suite v3.6.1 | official Anthropic paper/blog + GitHub/Zenodo APIs + pinned clone + local integrity/tests/adversarial controller probes + disputed public issue reports + 7-lens review | no — neutral mechanisms already covered; JS-1/2/3/4 remain study-only with local triggers; activation ontology unsupported; runtime is unsafe unchanged and outside current scope | Study neutral mechanisms and reproduce source/controller behavior only in a pinned sandbox; no TeaPrompt skill, lens, verifier, dependency, or runtime adoption; benchmark reproduction and deployment blocked | [survey](jspace-cognition-survey-2026-08-20.md) |
| 2026-08-20 | Code Recall `@erikhuang/coderecall` 2.10.0 (master `116512be`) | GitHub/npm APIs + pinned clone + executed selftest/bench/CI-read + adversarial containment/cleanup/MCP/ledger probes + 7-lens source review | no — methodology already covered; CR-1/2 remain study-only with local triggers; persistent-memory runtime is a standing non-goal and unsafe unchanged | Study patterns and reproduce source/controller behavior only in a pinned single-project sandbox; no TeaPrompt skill, lens, verifier, dependency, or runtime adoption; deployment blocked by containment, cleanup-ownership, MCP, ledger-grammar, provenance, and privacy gaps | [survey](code-recall-survey-2026-08-20.md) |
| 2026-08-25 | Pi / Maka / Amplio / Ankole durable harness concepts | GitHub/API exact-commit pins + pinned clones + primary DB/distributed-systems sources + local Pi/Maka/Amplio targeted builds/tests + 6-lens base review; official live Temporal/LangGraph/DBOS/Restate/Orleans/OTP docs + 7-lens lineage addendum | no — runtime enforcement remains a standing non-goal; existing trust/risk surfaces already classify missing evidence as unknown/no-go | Study the shared pattern, not industry consensus or genealogy; keep the qualified technical lineage as a scoped addendum; reproduce only named local crash contracts against a concrete host; no TeaPrompt skill, lens, dependency, runtime, or project-knowledge adoption; deployment requires sink idempotency/query reconciliation and external-effect evidence | [survey](agent-harness-convergence-survey-2026-08-25.md) |

## The Recurring Evaluation Procedure

This is the transferable output. When evaluating a new external tool or method:

1. **Verify from the one-hand source** (repo API, official docs), not the
   circulating summary or "N-prompts" re-telling. Pin the exact commit or
   artifact digest actually checked. If a tag, registry revision, and reviewed
   branch diverge, record each identity and scope every claim/test to the checked
   bytes; identity difference alone is not behavioral divergence.
2. **Separate transferable mechanism from product form.** Adopt mechanisms;
   reject runtimes, retrievers, citation pipelines, dashboards, and quotas.
3. **Tier repository-owned checks correctly.** A self-test or green CI run
   establishes only its tested assertions at that revision; it is not general
   safety, end-to-end correctness, or agent-outcome efficacy evidence.
4. **Probe state mutation, not just happy paths.** For tools that write files or
   shared configuration, test canonical-root containment through parent
   symlinks/junctions, per-install ownership receipts before cleanup, and
   concurrent writers.
5. **Gate any change on a verified *local* structural gap.** STORM had one and
   warranted a change; Loop-Skill, preflight, and Record & Replay did not, so
   they warranted none. "Interesting" is not a gap. When desired usage data
   cannot be observed, record it as `unknown`; absence of data is not zero
   demand and cannot become a permanent veto. Use the best available local
   structural evidence and prefer a bounded, reversible repair when it is
   directly testable.
6. **Check against standing non-goals** (runtime engine, vendor lock-in,
   RAG/vector store). An out-of-scope capability is not a missing capability.
7. **Apply the promotion gate only to new durable surface area** (≥3
   cross-session recurrences before a new skill, directory, runner, or similar
   surface). Prefer folding into an existing skill or a supporting lens. The
   gate does not block a narrow repair to an existing skill's declared contract.
8. **Record the outcome — including "no change"** — so the next session does not
   re-evaluate a settled item.
9. **No-copy boundary:** until an upstream repo carries a license, learn the
   concept only; do not copy text, checklists, or code.

## Signal Accounting (do not miscount)

Two external tools now point at the same deferred runtime: agentic-sop-to-work
and Loop-Skill. These are **external signals**. They do **not** advance the
**local** promotion gate for a runner, which counts at least three real local
workflows (each repeated ~5×, with observed drift or rework). Keep the two counts
separate: external interest is not local evidence. The runner stays deferred.
See the runner gate in [agentic-sop](agentic-sop-workflow-reflection-2026-06-13.md).

## Decision-Rule Correction

The earlier rule overreached in two ways: it treated unavailable local usage
data as if it proved no demand, and it applied a promotion gate for new surface
area to an in-place repair. The corrected rule is proportional and traceable:

1. Local project authority and verified repository evidence come first.
2. Current external or official evidence is required when the claim depends on
   changing facts, unfamiliar technology, standards, comparisons, or high-risk
   guidance; it is not mandatory ceremony for self-contained repo-local facts.
3. Logic, Socratic questioning, counterargument, and critical thinking test the
   evidence and expose assumptions. They do not create evidence.
4. Unmeasurable or unavailable evidence remains `unknown` and is documented.
5. Reversibility, blast radius, cost of delay, and testability determine whether
   to implement a bounded repair, defer, or reject.
6. Every material decision records a falsifier and the check that would verify
   or overturn it.

This follows mixed-evidence guidance from
[Google Research](https://research.google/pubs/bridging-the-gap-from-research-to-practical-advice/)
and NIST's guidance to combine qualitative and quantitative methods, document
uncertainty and unmeasurable risks, and prioritize by impact, likelihood, and
available resources in the
[AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/).

### Applied Counterexample: Test Plan Routing

The source prompt `02-engineering/test-designer.md` declares test design without
implementation, while its only operational mapping was an implementation skill
whose trigger requires edits. Installation copies `SKILL.md`, so a Prompt
Sources pointer alone does not provide the mode to installed users. This is a
verified local structural gap. Adding a conditional no-code Test Plan mode to
`reflective-spec-plan` is a narrow, reversible, route-tested repair; it does not
create a new skill or runtime and therefore does not require three observed
sessions.

## Methodology Layer vs Operationalization Layer

Correction (2026-06-20): an earlier framing treated "the SOP Compiler spec
exists" as equivalent to "the capability exists." It is not. Two distinct layers:

- **Methodology layer** — prompts, design lenses, triggerable skills
  ([sop-compiler.md](../04-agent/sop-compiler.md),
  [reflective-review](../skills/reflective-review/SKILL.md)). TeaPrompt is
  effectively complete here.
- **Operationalization layer** — a recorder that captures a real workflow, a
  skill generator, persisted execution state, and replay verification (what
  Record & Replay does; what immutable iteration / event log / feedback reopen
  would *guarantee*). TeaPrompt deliberately does not provide this.

So "complete" is true only of the methodology layer. A source-agnostic *prompt*
does not become an acquisition or persistence *capability* by being
source-agnostic — that earlier reasoning was an overclaim. This does not flip the
decision: the operational/runtime layer stays a standing non-goal (not an
oversight), the local promotion gate is unmet, and Record & Replay is
vendor-locked and uncopyable. "Learn it" therefore means *use it externally* — its
output feeds `sop-compiler` review → `reflective-review` — not *build it in*.

## Decision

The external-adoption decision remains unchanged for Loop-Skill,
preflight-checker, and Record & Replay: do not add their runtime or a new skill.
The corrected rule does require one separate in-place repair: operationalize a
conditional no-code Test Plan mode in `reflective-spec-plan` and test its route.
Keep the adoption procedure as a lesson, not a new skill, because it is a
specialization of existing
[reflective-research](../skills/reflective-research/SKILL.md),
[reflective-minimality](../skills/reflective-minimality/SKILL.md), and
[reflective-dispatch](../skills/reflective-dispatch/SKILL.md).

The 2026-07-13 Baton survey applies the same rule: its dispatch brake and
ownership/verification vocabulary are useful reference material, but no verified
local gap or recurrence warrants a new or repaired TeaPrompt surface. The
candidate dispositions and re-evaluation triggers are recorded in the
[Baton survey](baton-dispatch-survey-2026-07-13.md).

The 2026-07-24 Claude Code prompt snapshot survey also applies the corrected
rule: selected prompt mechanisms are study evidence, not local promotion
evidence. Three verified omissions warranted narrow repairs to existing skills;
conditional runtime composition, agent lifecycle heuristics, automatic skill
mutation, and unenforced digest fields did not warrant new surfaces. Full
extraction reproduction remains partial (603 published bodies, 416 in a fresh
public-extractor run); see the
[survey](claude-code-system-prompts-survey-2026-07-24.md).

## 2026-08-20 Cross-Survey Method Promotion

The 3xa-harness, J-Space Cognition Suite, and Code Recall surveys independently
exposed the same four review-method gaps. This is recurrence in TeaPrompt's own
evaluation workflow, not local demand for any upstream runtime or mechanism.
The user's direction to update skills authorizes these narrow in-place repairs;
it does not fire any named 3XA, JS, or CR adoption trigger.

### Candidate Adoption Ledger

| ID | Candidate | Status | Evidence | Next action or trigger |
| --- | --- | --- | --- | --- |
| XM-1 | Exact revision/digest identity and claim scoping | Adopted in place 2026-08-20 | All three surveys needed commit-level pins; Code Recall's `2.10.0` label resolved to distinct tag, npm `gitHead`, and master identities without material runtime divergence | Guard `reflective-research`, `external-adoption-review`, and Parallel Lens Review packet fields; retire only if later reviews show revision identity never affects evidence scope |
| XM-2 | Repository-owned self-test/CI evidence tier | Adopted in place 2026-08-20 | Green or repository-owned checks coexisted with adversarial false passes, boundary defects, and absent baseline/treatment efficacy evidence across the three surveys | Keep repository checks `observed` only for tested assertions; require boundary probes or reproducible outcome evaluation before safety/efficacy claims |
| XM-3 | State-mutating-tool boundary probes | Adopted in place 2026-08-20 | The three reproductions exposed containment, shared-configuration ownership, or concurrent-write gaps not established by happy paths | Guard the existing research skill and adoption lens; widen only after a repeated failure class escapes these probes |
| XM-4 | Complete lens deliverable before terminal verdict | Adopted in place 2026-08-20 | Five scout yields were schema-coerced in every survey; Code Recall also had a reviewer schema failure, with full deliverables recovered before synthesis | Canonical recipe marks incomplete yields unavailable rather than inferring verdicts; host manual retains recovery mechanics |
| XM-5 | Flip 3XA/JS/CR mechanism candidates because skills were requested | No change 2026-08-20 | Every survey records candidate-specific local triggers that remain unfired; generic method-update approval is not per-candidate adoption evidence | Re-open only the named row after its recorded trigger fires or explicit candidate-specific Human Review changes its status |

Deterministic guard: `plans/tests/test_managed_skill_promotion_adoption_state.py`.

## Rejected Alternatives

- A new `reflective-adopt` skill or `evaluation/` directory: rejected —
  promotion gate met for *recording the procedure*, not for new surface area;
  the Durable Lesson "prefer a source doc or lens over a new core skill" applies.
- A dispatch route for "external-tool evaluation": rejected — it is research +
  minimality, already routable today.
- Per-tool reflection files for the three no-change cases: rejected — they would
  near-duplicate the agentic-sop runner-defer logic; one consolidated case study
  carries the only non-duplicate content (the procedure and signal accounting).

## Falsifiability

This record is wrong if later external reviews scope evidence safely without
exact identities, repository-check tiering, state-mutation probes, or complete
lens deliverables; remove any repair that adds ceremony without changing a
decision or catching drift. It is too weak if a repeated failure class still
escapes these checks; repair the existing lens before proposing another skill.
No method repair is evidence that any 3XA, JS, or CR trigger fired.

## State Ledger

| Item | Status | Evidence |
| --- | --- | --- |
| Four no-change outcomes recorded | done | Case Comparison table |
| Recurring procedure captured | done | this file + PROJECT_KNOWLEDGE Durable Lesson |
| Durable Lesson + Decision Index added | done | PROJECT_KNOWLEDGE.md |
| No new skill or directory created | done | Rejected Alternatives |
| Evidence/promotion rule corrected | done | Decision-Rule Correction |
| No-code Test Plan route repaired | done | `reflective-spec-plan` + ROUTE fixtures |
| Baton no-change outcome recorded | done | `baton-dispatch-survey-2026-07-13.md` + Case Comparison table |
| DilinAI Nuwa/Jiyao no-change outcome recorded | done | `dilinai-nuwa-jiyao-survey-2026-07-13.md` + Case Comparison table |
| fable-method survey outcome recorded | done | `fable-method-survey-2026-07-16.md` + Case Comparison table |
| fable-method FM1/FM2 reproduction and adoption recorded | done | `fable-method-survey-2026-07-16.md` §Local Reproduction + wording pins in `test_fable_method_survey_record.py` |
| Claude Code prompt snapshot outcome recorded | done | `claude-code-system-prompts-survey-2026-07-24.md` + wording pins in `test_claude_code_system_prompts_survey_record.py` |
| agnix + agent-skills-hook survey outcome recorded | done | `agnix-agent-skills-hook-survey-2026-08-04.md` + Case Comparison table |
| Prime Agent survey outcome recorded | done | `prime-agent-survey-2026-08-06.md` + Case Comparison table + pins in `test_prime_agent_survey_record.py` |
| AI-assisted team throughput review recorded | done | `ai-assisted-team-throughput-review-2026-08-12.md` + Case Comparison table + pins in `test_ai_assisted_team_throughput_review.py` |
| 3xa-harness survey outcome recorded | done | `3xa-harness-survey-2026-08-20.md` + Case Comparison table + pins in `test_3xa_harness_survey_record.py` |
| J-Space Cognition Suite survey outcome recorded | done | `jspace-cognition-survey-2026-08-20.md` + Case Comparison table + pins in `test_jspace_cognition_survey_record.py` |
| Code Recall survey outcome recorded | done | `code-recall-survey-2026-08-20.md` + Case Comparison table + pins in `test_code_recall_survey_record.py` |
| Cross-survey method promotion recorded | done | XM-1–XM-5 Candidate Adoption Ledger |
| Research skill and adoption lens repaired | done | exact identity + evidence tier + state-mutation probes |
| Parallel Lens Review completeness gate repaired | done | `04-agent/workflow-recipes.md` + host-manual recovery note |
| Survey candidate statuses preserved | done | `test_managed_skill_promotion_adoption_state.py` guards 3XA/JS/CR ledger rows |
| Agent harness convergence survey outcome recorded | done | `agent-harness-convergence-survey-2026-08-25.md` + Case Comparison table + pins in `test_agent_harness_convergence_survey_record.py` |
| Agent harness technical-lineage addendum recorded | done | `agent-harness-convergence-survey-2026-08-25.md` §Technical Lineage Addendum + Case Comparison table + addendum pins in `test_agent_harness_convergence_survey_record.py` |
