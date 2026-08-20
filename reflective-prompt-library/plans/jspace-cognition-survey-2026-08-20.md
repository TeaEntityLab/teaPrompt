# J-Space Cognition Suite Survey — 2026-08-20

> **Status: decided (non-authoritative); external-survey panel record, no
> adoption.** J-Space Cognition Suite v3.6.1 is retained as study material. Four
> neutral mechanisms remain study-only candidates with explicit local triggers;
> its activation-level framing, benchmark claims, scripts, installed module
> suite, and deployment surface are not adopted. No TeaPrompt skill, lens,
> verifier, dependency, runtime, or project-knowledge rule was created or
> changed. `06-repo/AGENTS.md` and governed skill contracts remain authoritative;
> this record is evidence and a decision, not an operating rule.

## Purpose

Preserve the completed seven-lens survey of J-Space Cognition Suite so its
adoption question is not re-litigated from popularity or chat memory: what the
bundle implements, which scientific and benchmark claims survive source checks,
which runtime properties survive adversarial probes, and whether TeaPrompt
should study, reproduce, adopt, or deploy any part of it.

## Target and Version

- Review target: [`Tiger3807861189/J-Space-Cognition-Suite-V3.6`](https://github.com/Tiger3807861189/J-Space-Cognition-Suite-V3.6),
  checked 2026-08-20.
- Pinned release: `v3.6.1`; pinned commit
  `feac3df52d702ced67dda217f7a5167e1935d442` (2026-08-19). The lightweight tag
  and commit are unsigned. The GitHub release has no assets, signatures, or
  attestations.
- Latest immutable archive checked 2026-08-20: Zenodo
  [`10.5281/zenodo.22004675`](https://doi.org/10.5281/zenodo.22004675), published
  2026-08-19, file checksum
  `md5:316deab7d66b2a9f10fa7e13607dafec`, with a Software Heritage directory ID.
- Repository shape at the pin: 25 tracked files; 5,399 lines across the Python
  and Markdown survey surface; one 2,749-word skill entry; nine modules totaling
  16,934 words; three references totaling 10,966 words; an 840-line controller;
  a 273-line integrity verifier; and 18 controller tests.
- License boundary: root code and suite-authored text are Apache-2.0; external
  excerpts retain source terms under `THIRD_PARTY_NOTICES.md`. The separate
  companion benchmark report is CC BY-ND 4.0 and contains only README,
  `CITATION.cff`, and license text.
- Volatility trigger: re-pin and re-run the benchmark-artifact, scientific
  framing, containment, concurrency, scanner, citation, install-identity, and
  test checks before relying on a later revision.

## Architecture and Feature Map

| Layer | Shipped surface | Observed behavior |
| --- | --- | --- |
| Entry / routing | `j-space/SKILL.md` | Establishes a first-person J-space premise and five-step awakening; re-encodes non-trivial requirements; selects `fast`, `full`, or `loop`; routes nine task/failure signals; defines seams, register boundaries, and eight invariants |
| Selective modules | nine Markdown modules | Introspection, directed focus, bridge-before-conclusion reasoning, broadcast consistency, capacity/ledger state, self-monitoring, shorthand, marker→move→settle recovery, and empirical differential testing |
| References | science digest, induction playbook, exemplars | Mixes official activation-level findings, third-party reasoning traces, suite inferences, psychological analogies, and suite-authored drills/examples |
| State | `.jspace/WORKSPACE.md`, `.jspace/history.json` | Stores Goal, Core, Verified, Open, Next; keeps 20 seam snapshots; no content encryption, explicit restrictive permissions, or concurrent transaction control |
| Controller | `note`, `seam`, `resume`, `ship` | Records/reloads state and reports output-register heuristics; decides nothing; `ship` is advisory and returns 0 even when findings exist |
| Integrity | `verify_suite.py` | Checks one entry, exact premise/invariant anchors, module/reference presence/routes, drill headings, backbone order, and version-talk phrases; not protocol semantics or package inventory |
| Regression | `tests/test_jspace.py`, three-OS CI | Exercises 18 controller/source-shape contracts on Ubuntu, macOS, and Windows; no agent-host integration or behavioral-efficacy eval |
| Claims | README and companion prose | Reports nine DeepSeek score pairs, 2.53× speed, 2.21× token-cost improvement, and cross-model reproduction without retained raw evaluation artifacts |

## Panel Execution Mode

Method contract: `04-agent/workflow-recipes.md` §Parallel Lens Review with the
host `parallel-lens-review-packet` wrapper.

1. The merge owner cloned the pinned tag, mapped every entry/module/reference/
   script/test surface, checked official Anthropic sources, release/archive/
   issue metadata, companion-report contents, TeaPrompt overlap, and licensing.
2. The merge owner executed the deterministic and adversarial checks listed
   below, then wrote one shared packet inside the transient clone. Packet
   SHA-256:
   `94f4cb955e2d60d64382a02f20d83e4a82b3db178f6bf820398b66f9cf21311e`.
3. Seven read-only lenses fanned out in one batch: evidence, architecture,
   reproducibility, security/provenance, code correctness, usability, and
   strategic fit. All seven completed. Five scout yields were schema-coerced;
   their complete deliverables were recovered from the agent artifact or by
   tier-1 DM-wake over IRC. Reviewer and security-reviewer evidence arrived in
   structured artifacts and was completed into the required panel shape by IRC.
4. The merge owner, not the read-only lenses, executed the reproduction and
   mutation slice. No lens edited TeaPrompt or upstream files.
5. Role labels are review perspectives. No claim is made that named provider
   models or personas were invoked.

## Lenses

| Lens | Load-bearing question | Main result | Verdict |
| --- | --- | --- | --- |
| Evidence | Which scientific, benchmark, and portability claims survive primary-source checks? | Activation-defined J-space is official research; prompt-to-activation causality, score gains, efficiency, and cross-model effects remain unverified; community reports are contradictory testimony, not raw-artifact refutations | AGREE WITH CHANGES |
| Architecture | Is the prompt/module/controller design cohesive, proportionate, and distinct from ordinary context engineering? | Useful workflow pieces, but a 29.6k-word pedagogical surface, duplicated premises, hidden-register rituals, and a fragile controller create context pressure and compliance theater; TeaPrompt overlap is near-total | DISAGREE |
| Reproducibility | What verification tier does the project actually reach? | Source shape, 18 controller regressions, and three-OS compatibility reproduce; host integration, semantic protocol conformance, benchmark outcomes, and activation effects do not | AGREE WITH CHANGES |
| Security and provenance | Are install identity, storage, logs, licenses, and release chain safe? | No direct script network/process launch, but mutable unsigned acquisition, symlink escape, concurrent loss, plaintext/log exposure, citation drift, and no lifecycle block adoption/deployment | AGREE WITH CHANGES |
| Code correctness | Do controller and verifier meet their documented trust claims? | Single-writer well-formed behavior is tested; seven coordinator findings and seven additional malformed/concurrent/semantic gaps were source-confirmed | AGREE WITH CHANGES |
| Usability | Does selective loading reduce burden across operators and hosts? | `fast` is a useful escape hatch and single-thread recovery has value; long-session ceremony, manual packaging, language-specific regexes, hidden-register auditing, privacy, and concurrency undermine broad use | AGREE WITH CHANGES |
| Strategic fit | Is any mechanism a verified TeaPrompt structural gap? | Existing workflows already cover nearly all neutral mechanisms; four candidates remain study-only; activation ontology and runtime are rejected | AGREE WITH CHANGES |

## Panel Consensus

- **Decision:** `AGREE WITH CHANGES`, majority **6 of 7 lens verdicts**; the
  architecture lens returned `DISAGREE`. The dissent is about verdict strength,
  not use-case disposition: all seven reject unchanged adoption and deployment.
- **Study:** yes—study the neutral workflow mechanisms: explicit seams,
  marker→move→settle, state externalization, output-register leakage checks,
  bridge-before-conclusion, independent verification, and recovery.
- **Reproduce:** partial—the source-shape verifier, 18 controller tests, and
  single-writer controller lifecycle reproduce. Benchmark, efficiency,
  cross-model, host-integration, and activation-level claims do not reproduce
  from shipped assets.
- **Adopt:** no current TeaPrompt change. The method layer almost entirely
  overlaps risk-scaled routing, state/evidence ledgers, local feedback, context
  handoff, verification, and anti-bloat. External popularity is not local
  recurrence.
- **Deploy:** blocked at this revision. Mutable/unsigned acquisition, symlink
  escape, lost concurrent updates, plaintext/logging boundaries, heuristic
  false clearances, parser data loss, citation drift, and missing update/
  rollback/uninstall are unresolved.

### Use-Case Recommendation

| Use case | Recommendation |
| --- | --- |
| `study` | **yes** — study neutral state, seam, recovery, and verifier concepts; keep activation terminology at evidence tier |
| `reproduce` source/controller behavior | **yes, pinned sandbox only** — isolated, non-sensitive, single-writer workspace at the pinned commit/archive |
| `reproduce` benchmark/efficiency/cross-model effects | **blocked** — no complete harness, task manifests, prompts, seeds, raw outputs, grader records, retries, timings, or token traces |
| `adopt` selected mechanisms into TeaPrompt | **no current change** — JS-1 through JS-4 remain study-only with local-evidence triggers |
| `adopt` skill/modules/controller | **no** — duplicated local coverage, context cost, unsupported ontology, and unsafe unchanged runtime |
| `deploy` in shared, concurrent, sensitive, or untrusted workspaces | **blocked at this revision** |

## Required Wording Changes

These are upstream-facing corrections consolidated from the panel. None was
applied to TeaPrompt or the upstream repository.

1. **Separate mechanism from metaphor.** Describe the package as “an agentic
   context-management and metacognitive prompting framework inspired by
   Anthropic’s J-space research.” State that it does not read activations,
   compute Jacobians, use the J-lens, intervene on model weights, or establish
   that prompt self-description writes to the activation-defined J-space.
2. **Split official findings from suite inference.** Label counterfactual
   reflection training as a weight/training intervention and prompt-level
   induction as an unverified transfer hypothesis. Do not call a model’s
   prompted self-report mechanistic measurement.
3. **Calibrate benchmarks.** Label all DeepSeek score/efficiency entries
   author-reported and disputed. Publish the full pinned evaluation bundle:
   harness revision, task IDs/manifests, exact system/developer/user context,
   module loading, parameters, seeds/repeats, tool/environment boundary,
   per-task outputs, grader records, retries, timing/token traces, and
   aggregation scripts. Do not claim cross-model reproduction from vendor
   comparison columns.
4. **Name integrity accurately.** Describe `verify_suite.py` as a source-shape
   and anchor checker. It does not authenticate origin, inventory executables,
   prove semantic protocol meaning, verify behavioral compliance, or validate
   benchmarks.
5. **Make state trustworthy or narrow its contract.** Reject symlinked/junction
   state paths; bind real paths beneath the intended workspace; serialize or
   compare-and-swap complete read-modify-write transactions; protect history
   too; detect duplicate/unknown headings before rewriting; reject reserved
   closure-like suffixes in user fields; and state single-writer limitations
   until fixed.
6. **Repair `ship` without upgrading it to proof.** Keep advisory exit semantics
   explicit; require concrete coverage phrases rather than bare common words;
   detect unclosed fences; evaluate claims individually rather than granting
   paragraph-wide coverage; and describe the scanner as a heuristic, never a
   verifier.
7. **Add a privacy and data-flow contract.** State that `.jspace` is plaintext;
   prohibit secrets, credentials, regulated data, and private source excerpts;
   verify ignore rules and restrictive permissions; explain that `seam`/
   `resume` print state; bound and root `ship FILE`; distinguish “scripts have no
   direct network/subprocess calls” from “the host has no egress or logging.”
8. **Make acquisition reproducible and reversible.** Install an immutable
   archive/commit, verify a published digest, record source identity, reject
   collisions, clean-replace complete directories, preserve reviewed notices,
   and document update, rollback, uninstall, local modifications, and task-state
   handling. Pin GitHub Actions and Python where reproducibility is claimed.
9. **Fix citation identity.** Update `CITATION.cff` to `v3.6.1`, release date
   `2026-08-19`, version DOI `10.5281/zenodo.22004675`, and retain concept DOI
   `10.5281/zenodo.21971181` separately. Remove “link to be added” unless a paper
   exists.
10. **Clarify redistribution.** Ship `LICENSE` and `THIRD_PARTY_NOTICES.md` with
    standalone copies, inventory retained third-party excerpts at point of use,
    and keep the separate CC BY-ND companion report unmodified and outside the
    Apache-licensed work absent separate permission.
11. **Scale pedagogy to runtime.** Move awakening drills, extensive research
    grounding, and exemplar training out of default active modules; expose a
    compact neutral operational contract. Treat 731-character trigger text,
    verbatim premise recurrence, dense private notation, language-specific
    validation, and every-seam ritual as opt-in until measured against neutral
    equivalents.

## Candidate Adoption Ledger

| ID | Candidate | Status | Evidence | Next action or trigger |
| --- | --- | --- | --- | --- |
| JS-1 | Three-arm neutral-framing ablation: J-space ontology vs identical neutral workflow vs base | Deferred / study-only 2026-08-20 — no artifact change | Official research establishes activation-level J-space, not prompt-to-activation transfer; issue #28 names the category error; no local TeaPrompt need or upstream ablation exists | Reconsider only before adopting activation-framed wording or if a local neutral workflow repeatedly fails. Require pinned tasks, repeated runs, blinded grading, cost/latency, and same operational content. Falsifier: ontology and neutral conditions are indistinguishable or both lose to existing TeaPrompt |
| JS-2 | Marker→move→settle state-transition pairs | Deferred / study-only 2026-08-20 — no artifact change | The pairing is concrete and action-oriented, but local feedback, checkpoints, and retry-with-diagnosis already cover the function; no local marker-idling incident was established | Reconsider after repeated local recovery failures where agents name a state but do not execute/settle the correction. First add a narrow behavioral fixture to an existing skill. Falsifier: markers add theater/tokens without reducing recurrence |
| JS-3 | Output-register leakage heuristic | Deferred / study-only 2026-08-20 — no artifact change | `ship` demonstrates a useful boundary concept but has broad-regex, unclosed-fence, paragraph-coverage, advisory, and file-boundary gaps; runtime trust boundary already covers egress conceptually | Reconsider after a documented local leak existing guards miss. Implement a narrow deterministic scanner at the named surface with hostile fixtures; never import the pinned script. Falsifier: false positives/negatives exceed operator value |
| JS-4 | Five-field task-state controller / seam history | Deferred / study-only 2026-08-20 — no artifact change | State externalization is useful in single-writer tests, but TeaPrompt already has state ledgers/handoff methods and deliberately does not own a runtime; upstream loses concurrent updates and follows symlinks | Reconsider only if repeated local workflows need prompt-impossible persistence/reentry and host-native state is insufficient. Require containment, locking/CAS, schema/versioning, privacy, cancellation, and replay tests. Falsifier: existing host/todo/handoff state makes the controller redundant |
| JS-5 | Activation ontology, awakening, narrative identity, dense private register as governed TeaPrompt instructions | Rejected 2026-08-20 | No activation interface or neutral ablation; high context/pedagogical burden; hidden compliance is not auditable; mechanism overlaps neutral local contracts | Re-litigate only with direct activation evidence or a rigorous neutral-framing ablation on local tasks. External benchmark summaries do not satisfy the trigger |
| JS-6 | Import/deploy the nine modules, controller, verifier, install route, or benchmark claims unchanged | Rejected; deployment blocked 2026-08-20 | Near-total methodology overlap; unsigned/mutable install; no benchmark bundle; symlink/concurrency/privacy/parser/scanner/citation/lifecycle gaps | Reconsider only if TeaPrompt changes scope and a later pinned release fixes all P0/P1 runtime/provenance issues, publishes raw evaluations, and demonstrates a verified local structural gap |

No candidate created or changed a TeaPrompt skill, lens, verifier, dependency,
runtime, or project-knowledge rule. Deterministic guard for this record:
`plans/tests/test_jspace_cognition_survey_record.py`.

## Shared Findings

### What is strong

1. **Coherent neutral workflow mechanisms.** Requirement re-encoding,
   bridge-before-conclusion, explicit unknowns, independent references,
   differential tests, stated coverage, retry with diagnosis, and read-back
   completion checks are sound engineering practices.
2. **Selective fast path.** `fast` explicitly avoids unnecessary machinery, and
   the entry admits escalation rather than forcing one fixed process.
3. **Useful state vocabulary.** Goal/Core/Verified/Open/Next, stable question
   IDs, explicit swaps, and checkpoint closure provide legible single-writer
   state.
4. **Honest advisory boundaries in code.** The controller says it decides and
   blocks nothing; `ship` is explicitly a report, not a gate.
5. **Real regression work.** Eighteen standard-library tests cover controller
   lifecycle, recovery, decoding, selected malformed inputs, and verifier
   mutations; all three CI operating systems passed at the pin.
6. **Responsible source labeling in places.** The suite distinguishes access
   from phenomenal consciousness, identifies teaching examples, states some
   inferences, and carries Apache/third-party notices.
7. **Narrow executable surface.** Shipped scripts use the standard library and
   contain no direct network or subprocess calls.

### Load-bearing gaps

1. **Scientific category error:** official J-space is activation-defined;
   prompting a self-report is not a J-lens measurement or intervention.
2. **Benchmark non-reproducibility:** no raw/pinned evaluation bundle supports
   score, speed, token-cost, or cross-model claims.
3. **Contradictory community evidence:** issue #6 reports a lower-score,
   higher-cost 87-task subset; issue #10 reports no completion gain with 17–36%
   time overhead and up to 3.15× input tokens in a small A/B; issue #26 reports
   77.5% TB2.1 versus claimed 87.1%. None publishes enough raw material to be a
   definitive refutation, but all block treating author summaries as settled.
4. **Context/proportionality:** the installed text totals roughly 29.6k words;
   modules repeat premise, research grounding, drills, protocol, failures, and
   handoff. Selective loading reduces simultaneous load but not pedagogical
   weight or install complexity.
5. **Containment:** a pre-existing `.jspace` symlink redirects successful state
   writes outside the task workspace.
6. **Concurrent durability:** 20 successful writers preserved only 14 entries;
   history has the same read-modify-replace race.
7. **Scanner false clearances:** bare coverage words, unclosed fences, and
   paragraph joining can clear unsupported claims; `ship` is advisory by design.
8. **Malformed-ledger data loss:** duplicate scalar headings merge then collapse;
   unknown headings/content disappear on rewrite; reserved-looking closure text
   can pollute open rows.
9. **Verifier scope mismatch:** semantic inversions and extra executable files
   pass a verifier whose success wording sounds broader than source-shape checks.
10. **Privacy/logging:** task state is plaintext and printed to stdout without a
    sensitivity, permission, ignore, or host-retention contract.
11. **Install/provenance:** documented acquisition is mutable; tag/commit are
    unsigned; no attestation, digest-bound installer, collision-safe lifecycle,
    update, rollback, or uninstall exists.
12. **Citation drift:** machine-readable metadata names the previous v3.6
    archive rather than the reviewed v3.6.1 release.
13. **Localization:** English/Chinese claim/coverage regexes and byte-identical
    English premise recurrence constrain other languages and customized forks.

## Mechanism vs. TeaPrompt Fit

| Mechanism | Existing TeaPrompt coverage | Verified local gap? |
| --- | --- | --- |
| Fast/full/loop task classification | `reflective-dispatch` L1–L6 strictness and smallest-workflow rule | No |
| Requirement re-encoding and completion line read-back | Why/What/How/Done, `reflective-brief`, `reflective-implement` verification | No |
| Selective module/context loading | context engineering, strictness-based context budgets | No |
| Goal/Core/Verified/Open/Next ledger | research/implementation state ledgers, decision artifacts, handoff | No; persistence remains a standing non-goal |
| Bridge-before-conclusion and `?` claims | critical-thinking, evidence-vs-inference, falsifiability | No |
| Empirical escape / independent reference | local feedback, behavioral checks, test design, claim audit | No |
| Confidence→trust/retry/reconcile | confidence looper vocabulary and retry-with-diagnosis | No |
| Marker→move→settle | local feedback and checkpoints | Adjacent; recurrence unknown |
| Output register scanner | runtime trust boundary and evidence discipline | Adjacent; no documented local leak |
| Prompt activation ontology / awakening | none | No verified need; unsupported and rejected |
| Persisted CLI state/runtime | standing non-goal unless prompt-impossible guarantee and local recurrence | Out of scope today |

## Evidence vs Inference

| Claim | Status | Basis |
| --- | --- | --- |
| Pin, repository shape, license, archive, CI, citation fields | Observed / verified | GitHub/Zenodo APIs and pinned clone; checked 2026-08-20 |
| Integrity check and 18 tests pass locally | Observed / executed | Local Python 3.13 commands; upstream three-OS CI-read evidence at pin |
| Controller lifecycle works for tested single-writer well-formed inputs | Observed / executed | Unit tests and direct source review |
| Symlink escape, 14/20 concurrent retention, semantic/inventory blind spots, scanner and parser probes | Observed / executed | Coordinator mutation/probe matrix plus correctness/security source review |
| Anthropic J-space is activation/Jacobian-defined | Observed / verified | Official paper/blog checked 2026-08-20 |
| This suite accesses or writes activation-defined J-space | Unsupported | No activation interface or prompt-vs-neutral causal experiment |
| README benchmark, efficiency, and cross-model effects | Author-claimed / unverified | Summary prose/tables; retained raw evaluation bundle absent |
| Issues #6/#10/#26 refute the author benchmarks | Contradictory testimony, not verified refutation | Community reports checked 2026-08-20; raw logs/artifacts not public |
| Pedagogical surface increases cost | `[INFERENCE]` plus contradictory reports | 29.6k-word surface observed; local controlled cost not measured; community reports claim overhead |
| A later release repairs blockers | Unknown / volatile | Must re-pin and re-run checks |

## Disagreements / Residual Risks

- **Verdict wording:** six lenses chose `AGREE WITH CHANGES`; architecture chose
  `DISAGREE`. Preserve both. Architecture treats unsupported activation framing,
  context weight, compliance theater, and unsafe runtime as categorical. Other
  lenses preserve “agree” for the neutral method and tested source quality while
  rejecting claims/adoption/deployment. The use-case outcome is unanimous.
- **Prompt ontology as behavioral prime:** the strongest steelman is that a
  scientifically imprecise first-person ontology might produce better model
  behavior than neutral instructions. No neutral-framing ablation exists, so the
  possibility remains unknown—not evidence for adoption.
- **Runtime threat model:** upstream presents an optional local helper, not a
  concurrent datastore or security boundary. This lowers severity for trusted
  single-writer study; it does not satisfy TeaPrompt adoption/deployment needs or
  the script’s own “trusted ledger” rhetoric.
- **Community accusations:** issue #26 alleges fabricated scores; issue #20
  comments allege deleted criticism. This record does not adopt those
  accusations. Observable fact: author claims lack raw artifacts and multiple
  public reports disagree. Fraud remains unproven.
- **Official-research transfer:** Anthropic’s causal activation findings are
  strong for tested models and interventions. The transfer from training/
  activation interventions to prompt induction is the unsupported step.
- **Privacy finding is bounded:** scripts make no direct network/process calls;
  hosts, install retrieval, terminal/agent logs, and operator-selected file reads
  are distinct trust surfaces.
- **No PROJECT_KNOWLEDGE promotion:** one external survey adds no new durable
  local lesson; existing mechanism-vs-product, evidence-over-confidence, and
  prompt-vs-runtime lessons already govern it.
- Not executed: clean Claude/Codex/OpenCode/DSH discovery/install/update/
  uninstall; Windows locally; behavioral agent benchmark; branch protection;
  archive-byte comparison against the Git tree; third-party legal permission
  audit beyond notices.

## Evidence Actually Checked

- Pinned clone, GitHub repository/tree/commit/tag/release/contributor/community/
  Actions APIs, issue #1/#6/#10/#20/#26/#28 records, and Zenodo v3.6/v3.6.1
  metadata—checked 2026-08-20.
- Official Anthropic blog and technical paper—activation/Jacobian definition,
  causal interventions, model scope, limitations, and consciousness boundary;
  checked 2026-08-20.
- Full/targeted reads: README/Chinese README; `SKILL.md`; all nine modules; all
  three references; controller; integrity verifier; ledger template; all 18
  tests; CI; license/notices/contribution/citation metadata; companion report.
- `python3 j-space/scripts/verify_suite.py`—exit 0, clean.
- `python3 -m unittest discover -s tests -v`—18 tests passed.
- `python3 -m compileall -q j-space/scripts tests`—exit 0.
- Optional unconfigured diagnostics: `ruff` found one E741; `mypy` found one
  missing annotation. Neither is an upstream-required runtime failure.
- Upstream Actions run `32206406331`: Ubuntu, macOS, and Windows jobs passed
  integrity and regression steps at the pin.
- Adversarial execution: semantic inversion and extra executable both passed
  integrity; `.jspace` symlink wrote externally; 20 concurrent successful notes
  retained 14; broad coverage phrase and unclosed fence returned `clean`;
  duplicate/unknown headings lost data; reserved closure-like text entered an
  Open row.
- Not executed or unavailable: upstream benchmark harness/data/logs, independent
  report raw traces, live model activation inspection, neutral-framing ablation,
  all host installs, sensitive-data scenario, signed/attested release.

## Falsifiability

- The scientific-framing verdict is repaired if a pinned study demonstrates
  that prompt induction changes activation-defined J-space differently from an
  operationally identical neutral prompt under controlled J-lens measurement.
- The benchmark verdict is wrong if upstream publishes a complete immutable
  evaluation bundle whose results reproduce across repeated independent runs and
  reconcile issues #6/#10/#26.
- The no-local-gap disposition is wrong if TeaPrompt records a concrete recovery,
  marker-idling, output-leak, or prompt-impossible persistence failure that
  existing governed/host surfaces cannot address. That triggers the relevant
  JS-1 through JS-4 row; it does not automatically justify a new skill/runtime.
- Deployment can be reconsidered after a later pinned release proves real-path
  containment, concurrent transaction safety, malformed-ledger preservation,
  scanner hostile fixtures, privacy/logging controls, immutable acquisition, and
  update/rollback/uninstall.
- This ledger is dead text if a trigger fires and no re-evaluation occurs, or if
  a rejected candidate ships without changing its recorded status and guard.
