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
| 2026-08-25 | Heddle / SlideX product-runtime ownership article and appended analysis | Unpinned local Medium snapshot (`d2e50ad...`) + TeaPrompt contract comparison + 7-lens read-only review; no pinned source repository, package, license, hosted deployment, or executable reproduction | yes, narrow wording gap — existing effect/ownership-liveness contracts did not explicitly separate runtime completion from host product acceptance, record-specific durability, or subscriber disconnect from cancellation; no authorized runtime gap | Study the architecture; adopt OW-1–OW-4 and OW-8 as guarded in-place wording; partially adopt only the lowest-sufficient-promise heuristic and distilled failure conditions; defer Heddle packages, named ladder/checklist, and SlideX efficacy claims | [panel record](product-runtime-ownership-panel-2026-08-25.md) |
| 2026-09-03 | Governable autonomous delivery corpus (3 planes, K/W ladders, G0–G6, P1–P12, context compiler, evidence ledger, meta-governance) | Unpinned pasted corpus (`36e09db9...`) + coordinator `read` of 20 cited primary sources (Anthropic, OpenAI, NIST, arXiv, Chroma, ADK, METR, OWASP) + nine read-only mapping scouts + 7-lens review; no benchmark reproduction, no host harness | yes, narrow wording gaps — oracle vs developer tests, mid-task spec invalidation, transcript ≠ source of record, repeated-failure exit, explicit evidence ranking, attester discipline, non-zero-miss sink containment, skill compatibility bounds, irreversible-assumption trigger; no runtime gap | Study the architecture; adopt GA-1–GA-9 as guarded clean-room wording; reject ladders, universal retry caps, live fault-injection CI, wholesale checklists, and the unattended anti-pattern claim; drift and context rot recorded as bounded, not solved | [survey](governable-autonomy-survey-2026-09-03.md) |
| 2026-09-03 | All 12 TeaPrompt skills vs governable-autonomy possibilities | Same corpus + 12 `SKILL.md` contracts + 7-lens coverage panel (architecture lens crashed; `GSArchitecture2` refan); no extra-skill license pin, no live harness | yes, two installed-skill Never gaps — handoff transcript-as-record and risk prompt-as-sink-isolation; no unique extra-skill Trigger | Study; adopt two Never sentences; reject extra core/pack skills; tenth-core gate not waived; deploy still blocked on host containment | [panel record](ga-skills-coverage-panel-2026-09-03.md) |
| 2026-09-03 | Governable-autonomy feature set at feature depth (user-directed coverage objective) | Same corpus restated clean-room + twelve `SKILL.md` contracts + pack admission precedent (`agent-governance-scaffold` G1–G9); no host run, no refuter execution | yes, by direction — phase-local features missing at feature depth in nine core skills; no home for gate sequence, contract set, envelope, refuters | Adopt layered: anchors in nine core skills + fourth domain pack `governed-delivery`; reject tenth core, runtime, ladders; refuters `unknown` until a host runs them | [adoption record](governed-delivery-adoption-2026-09-03.md) |
| 2026-09-05 | LLM-as-a-Judge lifecycle article (Netflix Technology Blog + arXiv:2608.18300v3): rationale-annotated benchmark, reasoning-aligned rubric tuning, judge as gate and critic, rater-spread drift band, human-gated rubric rollback | Blog listing and arXiv abstract verified 2026-09-05; body read from paste only; licence is arXiv distribution-only; no code, data, or prompts; 7-lens review after a scout-backend crash and task-backend refan | panel: no verified load-bearing gap, one observed example-list omission (writer-critic rubric path); post-panel user direction plus one observed local instance of concordant verdicts with discordant reasons in the panel itself | Panel record-only (`AGREE` 4/7); then adopted by user direction three clean-room sentences (rubric as verifier with drift spot-check on the loop pack; reason tally in panel synthesis; reason audit in review) and a compression durable lesson; no numbers, judge runtime, fixture schema, ladder, or tenth skill | [survey](llm-judge-lifecycle-survey-2026-09-05.md) |
| 2026-09-05 | agentflow (agfnow/agentflow @ `b2935f5`): devlog notebook protocol, on-demand pipeline, external-runner-v1 no-remote clones, Stop-hook/pre-commit referees, looper live gate, 73-entry incident ledger; same-day entry-point addendum (zh-TW walkthrough of the same pin) | Pinned clone; coordinator `node --test` 898/889/9 (9 fail on unshipped `release/` and `eval/` paths); 7-lens review, 7/7 delivered; addendum: coordinator executed `init`, intake, and settings validation in a scratch repository, second 7-lens review 7/7 delivered; no `godev` round, hooks on a live host, or provider dispatch; private source repo and evals unreachable | panel: no — every methodology invariant already held; remaining mechanisms are operationalization (Standing Non-Goal); inline citations cover 18/73 incidents; recurrence `unknown`. Post-panel user direction found one textual loophole ("without a reason") and two missing checks. Addendum: one textual absence (activation order) and one permissive qualifier ("manual verification") with no local recurrence — deferred by the panel, then adopted by user direction | Panel record-only, `AGREE` 7/7; peer methodology + host harness, not a competitor or host; reject fixed three-start ceiling (ATT-7) and adoption as dependency; then three clean-room sentences by user direction (finding ≠ scope authorization; compaction fidelity check; origin-before-cut). Addendum record-only for skills (by reason 5/7): EP-1/EP-6 deferred with triggers, no-lighter-route lock rejected (R5/R7), no AF row moved; then EP-1 (resume reads the packet before discovery, on dispatch) and EP-6 (manual verification exercises the surface, on implement) adopted by user direction; concept addendum over docs and references (coordinator + three extractors; 73 incidents classified, 31 execution-layer): CX-1–CX-6 adopted by user direction (red-first tests; revision-bound review decisions; gates on the Safety Floor; observed-evidence spikes; spec examples run through their mechanism; hostile-instruction reporting), CX-11 rejected, the rest kept or held; author-talk addendum (three ASR transcripts + three syntheses, seven lenses 7/7): relation and AF-14/AF-9/AF-17 confirmed, skills unchanged, TK-1 deferred with trigger, Durable Lesson on synthesis grounding adopted; sibling-session reconciliation (SS-1–SS-9: contract-literal non-proof, test-count parameter, L1 ≠ pit of success, guards ≠ referees; host lists reconciled toward the READMEs (Gemini CLI retired, guide sections cut); recipe record-vs-answer sentence; post-panel implementation C1a/C2/C6/C7/C7b/C8/C9; session-outlines addendum O-1/O-2: concept map consolidated, one transcript correction, one open divergence) | [survey](agentflow-survey-2026-09-05.md) |
| 2026-09-10 | Context-efficiency instruction profile (`sh58702e/astra-efficiency-rules` @ `5576ceb`): scaffold fragment merged into an authority file; per-call and current-state character targets, locate-then-read, recover-from-packet after compaction, viewer preview vs original truncation, evidence-reuse validity, honest measurement | README, raw rules file, and commits API fetched 2026-09-10; MIT; one unsigned commit dated 2026-09-08; no clone, nothing executed; eight-lens review, 8/8 delivered | panel: no — every rule section already installed, forbidden (fixed caps), host-owned, or sharing I-1's single occurrence; one genuinely absent concept (preview ≠ return ≠ source) deferred beside I-1; A-7a gap real (external-change evidence reuse) | study yes; reproduce not applicable; adopt A-7a (user-directed); deploy no; A-5 deferred beside I-1 | [survey record](astra-efficiency-rules-survey-2026-09-10.md) |
| 2026-09-10 | Evaluation/release methodology of `MDX-Tom/gpt-instruct` @ `0ad8ec5`; documented harness and configuration installer, payload excluded | Exact-commit methodology docs, CI, ignore rules, license, and metadata checked 2026-09-10; eight complete lens reviews; no payload/tool execution | No qualifying local failure found; acceptance-record visibility is a deferred clarification, not a demonstrated runtime defect | Study only; no installed adoption; results author-claimed; filename/title and purpose/metric claims narrowed after the panel; four candidate triggers recorded | [survey record](gpt-instruct-survey-2026-09-10.md) |
| 2026-09-10 | OpenAI developer model guidance (nine models: GPT-4.1 through GPT-6 Astra): prompting best practices, reasoning effort defaults, tool calling evolution, autonomy calibration, verification calibration, stopping conditions | Nine per-model Markdown pages fetched from `developers.openai.com` 2026-09-10; public docs; no API calls, no execution; five-lens Socratic panel, 5/5 delivered | panel: four real gaps confirmed (prompt-text repetition, outcome-vs-process shape, test-depth calibration, re-search anti-pattern); one rejected (absolute-vs-conditional convention already implicit); two rejected (style, model-specific) | OG-1–OG-4 adopted by user direction; OG-5 rejected; OG-6/OG-7 rejected | [survey record](openai-model-guidance-survey-2026-09-10.md) |
| 2026-09-13 | Agentflow 8.2.0 public delta (`b2935f5` → `fcb6878`), config schema 7 | API identities + pinned source delta; coordinator audit CLI and 28/28 selected fixture tests; three read-only source slices plus a coordinator second pass over the unowned top-level contract with a 21-run fixture probe | Two same-surface wording clarifications, not demonstrated behavioral gaps (four paired synthetic cases unchanged); one question-versus-authorization text gap whose probe showed no behavioral gain for the prohibition but a stall of authorized work when its continuation duty sat inside the prohibition bullet | AF82-1 conflict resolution on dispatch, AF82-2 protected remedy replacement on minimality, AF82-9 question-is-not-authorization (Never) and AF82-14 mid-task question does not pause work (During Editing) on implement adopted by user direction; AF82-10–13 no change/record-only; no runtime/install or gate change | [survey](agentflow-8.2-delta-survey-2026-09-13.md) |
| 2026-09-05 | 84 installed skills on the workstation (harness-generated general subset, third-party workflow packs, vendor routers, lifecycle/locale/CLI wrappers) — sources by functional descriptor only | seven read-only extractors, allowlisted; 4/4 coordinator spot-checks; 26 project-bound skills never opened | ten concrete rules implied by principles but absent as text on the acting surface | GL-1–GL-10 adopted by user direction (brief, implement ×4, review, risk, research, flow generator ×2 plus template merged-result gate with observed dry-run); H-1–H-6 held; host-owned lessons not applicable | [installed-skills](installed-skills-general-lessons-2026-09-05.md) |
| 2026-09-16 | RSIAgent (`AetherLabsAI/RSIAgent` @ `dcd4e58`, Apache-2.0, arXiv 2609.15364): training-free self-improvement harness — actor/verifier/curriculum roles, verifier isolation with rollback, wave memory barrier, sealed evaluation with a leakage fence, infra-error-is-not-a-verdict, no-overwrite batches | GitHub API + five docs + arXiv abstract read 2026-09-16; two read-only scouts (source-mechanism tiering: nine of ten concepts code+test; TeaPrompt coverage map); three coordinator spot-checks 3/3; no clone, nothing executed from the repository | no wording gap — every concept covered or a learning-loop non-goal; **two local template defects in the source's C2/C8 failure families**, found by coordinator rigs: the fix loop's no-progress exit was dead with `STATE=./state` inside an un-ignored worktree; the DAG quorum gate accepted a sink left by a prior run | Study; RS-1 (DAG gate requires this run's sink) and RS-2 (progress count excludes `state/`) landed as in-place template repairs with dry-run guards failing on `9a756e5`; RS-3/4/5 rejected (snapshot rule, oracle-content fence, run-keyed state); RS-9 deferred on an observed oscillation; no surveyed text, skill, lens, dependency, or runtime adopted | [survey](rsiagent-survey-2026-09-16.md) |
| 2026-09-16 | Pasted "Graph Engineering / Agentic RAG" vendor-consensus synthesis (zh-TW, thirteen links attributing a 2026 H2 paradigm to Anthropic, Microsoft, LangChain, OpenAI) | Every vendor page the synthesis cites fetched 2026-09-16 plus the primary pages its third-party citations rest on (Anthropic 2024 guidance, Claude Code announcement, Agents SDK handoffs, LangGraph recursion limit, anthropic.com engineering index); one read-only coverage scout, three coordinator spot-checks 3/3; two third-party pages unreachable or unread | no concept gap — G1–G8 covered (topology selection, orchestrator-workers, sufficiency gate + OG-4, L0–L4 contracts, handoff-as-routing) or decided non-goals (runtime, swarm, retriever incl. knowledge graph, MCP runtime); **the synthesis genre itself is the finding**: a third-party blog's framing presented as an official Anthropic July 2026 article that the inspected official sources do not substantiate (separately, Claude Code is 2025-02, not July 2026), a real OpenAI post cited for graph/handoff content it does not contain, LangChain's "not a new idea / when not to use graphs" post inverted, a 2025-07 article's *envisioned* MCP interface presented as built; control-flow and knowledge graphs merged into one wave | Third synthesis-genre occurrence fired the 2026-09-05 Durable Lesson's *consideration* trigger: GE-1 (a `reflective-research` State Ledger sentence — a summary's citation is the summary's claim; the summary stays in the Source column until the cited page is read) drafted, measured against the bar, and **held pending user direction**; a first landing that read the trigger as authorization was reverted the same day (project judgement grants no agent authority). GE-5 rejected (second negative example on the loop pack); GE-10 "industry consensus" refuted record-only; seven no-change; no installed surface changed | [survey](graph-engineering-synthesis-survey-2026-09-16.md) |

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
10. **Own every changed file family.** When a survey fans out by file family,
    the top-level contract becomes everyone's pointer and nobody's deliverable;
    the coordinator owns that diff or names its owner, and the record lists each
    changed family with an owner or "unreviewed" (2026-09-13: the release's
    highest-yield rules sat in the unowned top-level contract).
11. **Probe drafted wording against state, not statements, before landing.** A
    reply is stated intent; a working tree read by the coordinator is behavior.
    Iterate the draft with the probe as the oracle — the 2026-09-13 pass found a
    stall, an exploitable escape clause, and a seating error in four cheap
    rounds that reading the text did not show.

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

## 2026-09-15 Landing-Review and Tune-Rule Promotion

User instruction: *"Update docs and skills if worth it"*, after a read-back of the
month's surveys. The three September landing passes — the 2026-09-10 model-guidance
adoption, the 2026-09-13 Agentflow 8.2 delta, and the 2026-09-14 governance pass —
each violated a rule they later stated, and each rule now sits only in a
non-authoritative Lesson or a dated record rather than on the surface the next
coordinator reads. This is recurrence in TeaPrompt's own method, not local demand
for any upstream mechanism; the direction authorizes narrow in-place repairs and
fires no named survey trigger.

### Candidate Adoption Ledger

| ID | Candidate | Status | Evidence | Next action or trigger |
| --- | --- | --- | --- | --- |
| XM-6 | Landing reviewed as landed bytes; every figure bound to its measured revision (Parallel Lens Review packet contract) | Adopted in place 2026-09-15 | Three consecutive landing reviews each found defects the landing session had recorded as done: 4 in panel-approved text on 2026-09-10 (a step placed after the workflow's stop carrying a 7-word verbatim run, a risk-scoped prohibition readable as licence to skip a behavior lock, a 9-word verbatim run, three rules fused into one paragraph); an unowned top-level contract on 2026-09-13 whose probe then found a stall, an exploitable escape clause, and a seating error; 13 on 2026-09-14 (five dropped clauses recorded as "same clauses", two example claims the templates did not implement, a vacuous guard, wrong tallies, a pre-tune figure attributed to the wrong fixture revision). No packet-contract bullet said a landed commit is read against its record; step 11 probes a sentence *before* landing and does not check counts, seats, figures, or examples after | Guard `04-agent/workflow-recipes.md`; retire if three consecutive landing reviews find nothing, in which case the bullet is ceremony |
| XM-7 | R8 gains the two tune duties GW-1 violated: one adversarial group per *other* workflow sharing a tuned token; failing probes fixture-backed or recorded, never swapped | Adopted in place 2026-09-15 | The bare-`verify` tune passed its target trap and all three evals at 100% while moving review/risk/test-plan phrases into implement; two failing probes were replaced by passing ones, producing a 100% pre-tune figure that measured nothing. Both duties lived only in the Durable Lesson's review trigger while `PROJECT_KNOWLEDGE.md` says router tuning follows R8 | Guard `plans/ROUTING_CONTRACT.md` R8; the Lesson keeps the pattern and evidence, R8 the rule |
| XM-8 | "Own the front door" promoted from procedure step 10 into the Parallel Lens Review recipe stanza | Held — named gate | The 2026-09-13 reflections gate promotion on a second occurrence; the 2026-09-14 fan-out (by concern, coordinator-owned execute slice) reported no unowned family | Fires on a second survey whose highest-yield rules sat in an unowned slice |
| XM-9 | "Ask approval only after preparing a concrete reviewable result; no unsolicited approval flows" (vendor autonomy guidance) | No change 2026-09-15 | Already held: `reflective-brief` step 4 classifies an unknown before it becomes a question and Never asks before a targeted check; `reflective-implement` presents an implied change as a proposal (AF82-9); `reflective-risk` gates approval on a dry-run, which is the reviewable result | A local case where an agent asked before looking or without a dry-run |
| XM-10 | Per-source yield rule ("after wording yield falls below one clarification per pass, go delta-only, no panel") | No change / record-only 2026-09-15 | Source-specific procedure note in the 2026-09-13 reflections; a generic threshold would be the universal number ATT-7 rejects | Stays with the Agentflow record |

Rejected alternative: a tenth Durable Lesson for the landing-review pattern — it
would restate XM-6 on a second surface, and the three Decision Index entries
already carry the defect counts. Deterministic guard:
`plans/tests/test_managed_skill_promotion_adoption_state.py`. Falsifier: XM-6 is
ceremony if three consecutive landing reviews find nothing; XM-7 is wrong if a
tune that followed both duties still regressed a sibling workflow, in which case
the duty is incomplete, not excessive.

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
| Product/runtime ownership panel outcome and guarded adoption recorded | done | `product-runtime-ownership-panel-2026-08-25.md` + Case Comparison row + `test_product_runtime_ownership_panel_record.py` |
| Governable autonomous delivery survey outcome and guarded adoption recorded | done | `governable-autonomy-survey-2026-09-03.md` + Case Comparison row + `test_governable_autonomy_survey_record.py` |
| Governable autonomy × all skills panel outcome and guarded adoption recorded | done | `ga-skills-coverage-panel-2026-09-03.md` + Case Comparison row + `test_ga_skills_coverage_panel_record.py` |
| Governed delivery feature adoption recorded with pack admission and guards | done | `governed-delivery-adoption-2026-09-03.md` + Case Comparison row + `test_governed_delivery_adoption_state.py` |
| LLM-as-a-Judge lifecycle survey recorded; three sentences adopted by user direction with reflection | done | `llm-judge-lifecycle-survey-2026-09-05.md` + Case Comparison row + `test_llm_judge_lifecycle_survey_record.py` |
| agentflow survey recorded; three sentences adopted post-panel by user direction; entry-point addendum recorded; EP-1/EP-6 adopted by user direction; concept addendum recorded with CX-1–CX-6 adopted; author-talk addendum recorded, skills unchanged, synthesis-grounding Durable Lesson adopted; sibling-session reconciliation recorded (SS-1–SS-9) and implemented by user direction; session-outlines addendum recorded (O-1/O-2) | done | `agentflow-survey-2026-09-05.md` (+ addendum) + Case Comparison row + `test_agentflow_survey_record.py` (five adopted sentences pinned at single surfaces; loophole qualifier absent; EP dispositions; no lighter-route lock) |
| installed-skills general-lessons survey recorded; GL-1–GL-10 adopted by user direction | done | `installed-skills-general-lessons-2026-09-05.md` + Case Comparison row + guard `plans/tests/test_installed_skills_general_lessons_record.py` (ten sentences pinned at single surfaces; fan-out template merged-gate dry-run) |
| Harness and intent-drift rethink recorded; two glossary terms, one Closure clause, one Durable Lesson, one recipe frame-test adopted; tool-status rule deferred | done | `harness-intent-drift-rethink-2026-09-06.md` + Decision Index entry + guard `plans/tests/test_harness_intent_drift_rethink_record.py` |
| Context-efficiency instruction-profile survey recorded; A-7a adopted (user-directed, external-change evidence reuse on `reflective-implement`); A-5 still deferred beside I-1; six rejected; one permanently held | done | `astra-efficiency-rules-survey-2026-09-10.md` + Decision Index entry + guard `plans/tests/test_astra_efficiency_rules_survey_record.py` (survey tokens and cap literals absent from skills, install guide, GLOSSARY, `04-agent/`; A-7a adopted, A-5 reserved wording record-only) |
| Evaluation/release methodology survey recorded; no installed adoption; four candidate triggers and deferred acceptance-record clause retained | done | `gpt-instruct-survey-2026-09-10.md` + Decision Index entry + `plans/tests/test_gpt_instruct_survey_record.py` (source identity, panel completeness, ledger states, clean-room boundary, and index links) |
| OpenAI model guidance survey recorded; OG-1–OG-4 adopted (prompt-text repetition on minimality, outcome-first on spec-plan, verification calibration on implement, re-search anti-pattern on research); OG-5 rejected (already implicit); OG-6/OG-7 rejected (style/model-specific) | done | `openai-model-guidance-survey-2026-09-10.md` + Decision Index entry + guard `plans/tests/test_openai_model_guidance_survey_record.py` (four adopted sentences pinned at single surfaces; vendor tokens absent from skills) |
| Skill correctness and logical-consistency pass recorded; fixes landed in twelve skills; flow packs back under the size budget | done | `skill-verification-panel-2026-09-05.md` + Decision Index entry + guard `plans/tests/test_skill_verification_panel_record.py` (landed sentences pinned per skill; both flow packs ≤ 20,000 chars; DAG quorum-path merged-gate dry-run) |
| Agentflow 8.2.0 delta recorded; four paragraphs adopted on three skills (two with source-review dissent and no measured efficacy claim; AF82-9/AF82-14 from a second pass whose fixture probe set their wording and seating) | done | `agentflow-8.2-delta-survey-2026-09-13.md` + Decision Index + Durable Lesson on seating + `test_agentflow_v82_delta_record.py` (identity, fourteen dispositions, named-section and single-surface record parity) |
| Landing-review bullet on the packet contract and two tune duties on R8 adopted from the September passes; front-door promotion held at its second-occurrence gate; approval-shape and per-source yield no-change; tenth Lesson rejected as restatement | done | `04-agent/workflow-recipes.md` + `plans/ROUTING_CONTRACT.md` R8 + §2026-09-15 above + `test_managed_skill_promotion_adoption_state.py` |
| RSIAgent survey recorded; two template repairs landed (DAG quorum sink gate, fix-loop progress count excluding `state/`); three candidates rejected, one deferred, six no-change | done | `rsiagent-survey-2026-09-16.md` + Decision Index entry + `plans/tests/test_rsiagent_survey_record.py` (identity, twelve dispositions, clean-room boundary, index links, fix-loop dry run) + DAG stale-sink dry run in `test_skill_verification_panel_record.py` |
| Graph-engineering synthesis survey recorded; four vendor attributions read against their pages (one not substantiated by the inspected sources, one absent, one inverted, one overclaimed); GE-1 drafted at the fired third-occurrence consideration gate and held pending user direction (first landing reverted same day); Lesson evidence and trigger rewritten; GE-5 rejected; GE-10 refuted record-only; seven no-change; no installed surface changed | done | `graph-engineering-synthesis-survey-2026-09-16.md` + Decision Index entry + `plans/tests/test_graph_engineering_synthesis_survey_record.py` (shape and source verdicts, ten dispositions, reserved GE-1 wording absent from every installed surface, fired-but-held trigger, clean-room boundary, index links) |
| Decision-model survey recorded (`dsif2012/Qwen3-4B-Instruct-2507-Decision` @ `88e9198`, Apache-2.0; inspirations: TypeSafe Jev/System One post, `harshatheg/Qwen-2.5-1B-RLCD` card): logit-scored typed decisions (BOOLEAN/CHOICE) over dynamic candidate sets, confidence+margin+ranking, programmatic assembly, prefix-cache serving | GitHub API + HF cards + TypeSafe post read 2026-09-18; no clone, nothing executed | no wording gap — C1–C8 covered (verdict contracts, candidate data, packet amortization, batching) or runtime non-goals (logits, KV-cache, calibration, heads); DM-5 self-reported margin rejected as self-report; DM-6 calibration rejected; two record corrections (RLCD acronym conflation; 1B vs 1.5B base) | `plans/decision-model-survey-2026-09-18.md` + `plans/tests/test_decision_model_survey_record.py` |
| Dream-RSI survey recorded (`zhengkid/Dream-RSI` @ `4149ea9`, paper-only, no LICENSE; dream-rsi.com + PDF; arXiv 2609.14858 claimed): discovery history as exact replay simulator, off-policy evaluation of exploration-policy code, incumbent-in-candidate-set monotonicity on recorded history, growing simulator pool, semantic-guidance-underperforms-replay finding | site + PDF + GitHub API read 2026-09-18; nothing executable exists to audit | no wording gap — C1–C10 covered (dry-run rigs, holdout-before-tune, no-change disposition, multi-form matrices, flow packs as programmable exploration) or learning-loop non-goals; DR-5 adopted same day under user direction (caution sentence pinned once on `04-agent/workflow-recipes.md`); DR-8/DR-9 record-only scope corrections | `plans/dream-rsi-survey-2026-09-18.md` + `plans/tests/test_dream_rsi_survey_record.py` |
| Jev architecture-analysis synthesis survey recorded (pasted thread, 2026-09-18; probe essay 2026-09-17; direct scorer pinned `b9cb32537e78`; classification config fetched raw): encoder-vs-no-loop-decoder hypotheses under stated underdetermination, feasibility-is-not-identity, negative probes scoped to the unchanged hypothesis, calibration independent of architecture | thread + essay + two reimplementations + vendor docs + two arXiv abstracts read 2026-09-19; canonical papers tiered standard-not-refetched | no wording gap — all eight concepts are installed epistemic rules; all attributions held (first fully-held pasted synthesis; GE-1 rule value symmetric); JA-7/8/9 dated record-only notes | `plans/jev-architecture-synthesis-survey-2026-09-19.md` + `plans/tests/test_jev_architecture_survey_record.py` |
| MiniMax Code survey recorded (`MiniMax-AI/minimax-code` @ `e3724a13d72d`, MIT default, Pi-lineage vendored core): public-projection governance — inventory-as-boundary, candidate quarantine, single-source registries, self-erratic audits, red-gate-published verification — plus five co-located repo skills (drift sweep, runtime sinks, retro, testing, CLI guide) | GitHub API + 7 docs + all 5 SKILL.md files read 2026-09-19; nothing executed, docs-to-code fidelity not audited | no wording gap — nine concepts covered or host territory; independent convergence on retro-authority and promotion gates recorded as corroboration; MC-5 tri-state consumer map adopted same day under user direction (additive Verification bullet on `reflective-implement`, pinned once) | `plans/minimax-code-survey-2026-09-19.md` + `plans/tests/test_minimax_code_survey_record.py` |
