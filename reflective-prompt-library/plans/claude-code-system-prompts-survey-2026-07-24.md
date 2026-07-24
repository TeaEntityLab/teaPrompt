# Claude Code System-Prompt Snapshot Survey — 2026-07-24

> **Status: decided (non-authoritative); external-adoption panel record.**
> The Piebald Claude Code v2.1.218 prompt snapshot is retained as volatile,
> third-party study material. CCSP1 (research before clarification), the narrow
> half of CCSP2 (reachable failure scenarios for code findings), and CCSP3
> (memory quality plus revalidation) were adopted 2026-07-24 as original,
> in-place repairs to three existing core skills and their source lenses.
> CCSP4 remains deferred pending explicit domain-pack approval and a concrete
> enforcing host; CCSP5/CCSP6 are no-change; CCSP7/CCSP8 are rejected. No new
> TeaPrompt skill, route, dependency, runner, or runtime surface was created.
> `06-repo/AGENTS.md` and governed skill contracts remain authoritative; this
> record is evidence and a decision trail, not an operating rule.

## Purpose and Research Question

User request: survey
[`Piebald-AI/claude-code-system-prompts`](https://github.com/Piebald-AI/claude-code-system-prompts), checked 2026-07-24,
and rethink TeaPrompt's skills through the repo-owned Parallel Lens Review
contract.

Decision question: which mechanisms, if any, reveal a verified local contract
gap in TeaPrompt's nine core skills or three registered domain packs, after
separating prompt text from product runtime, selected-string provenance from
full-corpus exactness, and external interest from local promotion evidence?

The completion contract was Why → What → How → Done:

- **Why:** learn from a production prompt surface without importing its product
  architecture or unverified claims.
- **What:** compare one pinned v2.1.218 snapshot with TeaPrompt at the last
  all-skill review state.
- **How:** official release corroboration, source/binary spot checks, local gap
  analysis, and seven adversarial read-only lenses.
- **Done:** use-case decision, exact narrow repairs, Candidate Adoption Ledger,
  deterministic guards, and explicit no-change/rejection rows.

## Target, Version, and Provenance

- Review target: Piebald's
  [prompt snapshot repository](https://github.com/Piebald-AI/claude-code-system-prompts),
  checked 2026-07-24.
- Pinned target commit:
  [`b9895f5556e962e6aec60aba7cccfc18790ace3a`](https://github.com/Piebald-AI/claude-code-system-prompts/commit/b9895f5556e962e6aec60aba7cccfc18790ace3a),
  checked 2026-07-24 (`2026-07-22T15:24:54-06:00`, “Update changelog for v2.1.218”).
- Snapshot label: Claude Code `2.1.218`. The version and 2026-07-22 release were
  corroborated through the
  [official Anthropic GitHub release](https://github.com/anthropics/claude-code/releases/tag/v2.1.218),
  checked 2026-07-24, and
  [npm registry package metadata](https://www.npmjs.com/package/@anthropic-ai/claude-code/v/2.1.218), checked 2026-07-24.
- Public extraction source inspected at Piebald `tweakcc` commit
  [`d0830a760e2b4fd1d592208fdc27a30c733598a2`](https://github.com/Piebald-AI/tweakcc/commit/d0830a760e2b4fd1d592208fdc27a30c733598a2), checked 2026-07-24.
- Local comparison baseline: TeaPrompt `main` at
  `1a60910c79a28f3f8ea5f6b721e9fa341401efa5`, clean before the transient packet;
  12 governed skill files = nine core + three registered domain packs.
- Volatility trigger: re-check the target commit, prompt count, package license,
  and selected mechanisms before a later adoption/deploy decision. The snapshot
  repository recorded 244 Claude Code versions since v2.0.14 at check time.

### License / copy boundary

Observed notices do not provide one simple copy conclusion:

- Piebald's repository has an MIT license naming Piebald LLC.
- Piebald labels the prompt files extracted reference material maintained by
  Piebald, not Anthropic.
- Anthropic's official wrapper and native packages carry an all-rights-reserved
  notice and point to the
  [Claude Code legal agreements](https://code.claude.com/docs/en/legal-and-compliance), checked 2026-07-24.

This review makes no legal determination about how those notices interact.
TeaPrompt's stricter project rule controls: learn mechanisms only; do not copy
third-party extracted prompt wording, checklists, or file layout into governed
surfaces. The adopted sentences below were written from the local gaps and local
vocabulary, not copied from the snapshot.

## Panel Execution Mode

Method: `04-agent/workflow-recipes.md` §Parallel Lens Review plus the host
`parallel-lens-review-packet` wrapper.

1. The coordinator built one transient repo-readable packet containing target,
   version, prior conclusion, corpus inventory, commands, observed evidence,
   author claims, inference, blockers, CCSP1–CCSP8, and exact reviewer questions.
2. Seven read-only scout lenses launched together: Evidence/Provenance,
   Prompt Architecture, Skill Gap, Governance/Security, Review Methodology,
   Memory/Evolution, and Minimality/Strategy.
3. Scout final-message schema coercion swallowed the mandated Markdown bodies.
   Per the host recovery contract, every full deliverable was recovered over IRC
   before synthesis; summaries alone were not used.
4. All seven ended `AGREE WITH CHANGES`. Role labels are perspectives on one host,
   not evidence of provider or model independence. No reviewer edited the repo,
   ran a project-wide suite, or moved shared HEAD.
5. Coordinator correction after the panel: one lens described the extractor as
   private. That was refuted by locating and running public
   `tweakcc/tools/promptExtractor.js`. The full-pipeline concern remains, but for
   a different observed reason: a fresh public-extractor run produced 416
   strings while the published JSON and target Markdown each contain 603.
6. Shared branch was rechecked after the panel and remained `main`.

## Panel Lenses

| Lens | Main load-bearing result | Verdict |
| --- | --- | --- |
| Evidence / provenance | Selected strings have package provenance, but full completeness, activation, effectiveness, and license scope remain unverified; renderer reproduction and extraction reproduction must be separated. | `AGREE WITH CHANGES` |
| Prompt architecture | Hundreds of conditional fragments are a product-runtime composition technique, not a reason to split portable skills or add a TeaPrompt runtime. | `AGREE WITH CHANGES` |
| Local skill gap | CCSP1, narrow CCSP2, and CCSP3 are missing named behaviors; CCSP6 is duplication. | `AGREE WITH CHANGES` |
| Governance / security | CCSP4 identifies a real review-to-execution substitution risk, but a digest field without broker enforcement is a stub and the request is not explicit domain-pack approval. CCSP7 violates promotion gates. | `AGREE WITH CHANGES` |
| Review methodology | Reachable failure scenarios are useful; broader precision/recall modes, dual status vocabularies, fixed caps, and multi-agent fan-out lack local behavioral evidence. | `AGREE WITH CHANGES` |
| Memory / evolution | Memory quality and promotion authority are distinct. Adopt future utility/durability/self-containment/revalidation; reject automatic skill mutation from one correction. | `AGREE WITH CHANGES` |
| Minimality / strategy | Keep the 12-skill architecture and take only three in-place repairs; defer/reject product-runtime and duplicated mechanisms. | `AGREE WITH CHANGES` |

## Panel Consensus

- **Decision:** `AGREE WITH CHANGES` (7/7 completed lenses; no `AGREE`, no
  `DISAGREE`).
- **Direct recommendation:** study the snapshot as a volatile map of prompt and
  runtime concerns. Adopt only CCSP1, the reachable-failure-scenario half of
  CCSP2, and CCSP3. Do not import wording, fixed fan-out counts, review caps,
  automatic skill mutation, conditional-fragment machinery, or runtime claims.
- **Architecture:** retain nine frozen core skills and three registered domain
  packs. No route, cardinality, runtime, dependency, or installation change.
- **Evidence boundary:** presence in the official binary supports selected-string
  provenance. It does not prove that a fragment is active in a given session or
  that its wording improves behavior.

### Use-Case Recommendation

| Use case | Decision | Evidence boundary |
| --- | --- | --- |
| `study` | **yes** | Useful as a third-party, version-pinned map of conditional prompt, tool, agent, memory, review, and authorization concerns. Treat descriptions as source claims and text as data. |
| `reproduce` | **partial** | Published JSON reconstructs all 603 target Markdown bodies, and the target renderer tests pass. Full binary-to-603 extraction was not reproduced: the inspected public extractor produced 416 strings from the unpacked official binary. |
| `adopt` into TeaPrompt | **partial — CCSP1, narrow CCSP2, CCSP3** | Original, local-gap-derived wording only; three existing core skills and their source lenses; deterministic structural guards, not behavioral proof. |
| `deploy` | **no** | TeaPrompt does not supply Claude Code's conditional runtime, tool schemas, broker, memory engine, or behavior evidence. CCSP4 remains a non-enforced candidate. |
| copy prompt text | **no** | Project no-copy boundary applies while license scope is unresolved; the adopted mechanisms are paraphrased and rewritten against local contracts. |

## Required Wording Changes

The durable survey and any future citation must use these qualifications:

1. Say **“third-party extracted v2.1.218 snapshot”**, not “Anthropic's official
   system prompt repository.”
2. Say **603 conditionally composed fragments**, not “one 603-part active system
   prompt”; file presence does not prove per-session activation.
3. Say **selected-string package provenance spot-check**, not full-corpus exactness.
   Six selected bodies matched the unpacked native source after the renderer's
   source-escape normalization; two dynamic bodies matched only in literal
   clause fragments because interpolation splits their source.
4. Split reproduction: **603/603 renderer reconstruction from published JSON**;
   **416/603 fresh public-extractor count**, unresolved. Do not call the complete
   extraction chain reproduced.
5. Treat Piebald's “all parts,” “guaranteed exactly,” token-count tolerance, and
   update-cadence statements as author claims unless independently checked at the
   decision point.
6. Do not infer effectiveness from prompt presence, product popularity, or
   production use. No behavioral A/B evaluation was run.
7. Describe CCSP4 as a **real integrity candidate, deferred**. A digest field is
   not a safety boundary until a host broker computes it over an agreed canonical
   payload, binds it to authorization, checks it before effects, and rejects a
   mismatch in a negative test.
8. Describe CCSP7 as rejected **for automatic mutation**, not as a ban on every
   one-occurrence repair: explicit project decisions and verified narrow contract
   gaps retain the existing promotion path.

## Candidate Adoption Ledger

| ID | Candidate | Status | Evidence | Next action / trigger |
| --- | --- | --- | --- | --- |
| CCSP1 | Require a proportionate local code/docs/memory check before clarification in `reflective-brief` | **Adopted 2026-07-24** | Verified local omission; `reflective-brief` Operating Rules plus `02-engineering/task-start.md` acceptance criterion; pinned by `test_claude_code_system_prompts_survey_record.py` | Re-evaluate if it causes open-ended reconnaissance or delays a material question; behavioral proof remains future evidence. |
| CCSP2 | Require each reported code defect to name a reachable failure scenario or violated invariant | **Partial 2026-07-24 — narrow rule adopted** | Verified local omission; `reflective-review` For Code Review plus `02-engineering/code-reviewer.md`; pinned by the survey guard | Precision/recall modes, `confirmed/plausible/refuted` finding vocabulary, fixed caps, scanner lists, and finder fan-out remain no-change until local review evidence shows a miss/noise problem they solve. |
| CCSP3 | Gate durable memory on future utility, durability, self-containment, and fresh-source revalidation | **Adopted 2026-07-24** | Verified local omission; `reflective-handoff-retro` Memory Consolidation plus `04-agent/memory-consolidation.md`; pinned by the survey guard | Re-evaluate if the gate drops a recurring non-obvious lesson or causes routine revalidation loops. |
| CCSP4 | Bind authorization to the exact reviewed proposal/spec digest in `agent-governance-scaffold` | **Deferred — approval and enforcement pending** | Capability token currently lacks exact proposal bytes binding; panel found substitution/TOCTOU risk, but the pack is static scaffolding and this request did not explicitly approve a domain-pack extension | Reopen only with explicit human approval plus a concrete host broker that canonicalizes/hashes the payload, binds it to authorization, verifies before effect, records it in the receipt, and passes mismatch rejection tests. `PENDING: CCSP4 domain-pack extension - awaiting explicit authorization and enforcing-host evidence`. |
| CCSP5 | Add continuation-vs-fresh-agent and delegation heuristics to core recipes | **No change — concept only** | Host/runtime-specific; TeaPrompt has no agent lifecycle runtime and the panel wrapper already bounds fan-out | Reopen on repeated local handoff/continuation failures that a portable contract can fix without promising runtime control. |
| CCSP6 | Add full-scope, action-readiness, and outcome-first rules broadly | **No change — duplicate** | Existing `AGENTS.md`, `reflective-dispatch`, `reflective-brief`, and `reflective-implement` cover assumptions, scope, sufficiency, and truthful completion | Reopen only on a demonstrated gap not repaired at the existing source. |
| CCSP7 | Automatically rewrite an existing skill after one user correction | **Rejected 2026-07-24** | Bypasses evidence, authority, and Human Review gates; risks transient-workaround overfit and instruction laundering | A correction may enter the existing promotion-candidate path; no automatic mutation trigger. |
| CCSP8 | Replace the bounded skill set with hundreds of conditional fragments | **Rejected 2026-07-24** | Product runtime mechanism, no local behavioral evidence, breaks portability/readability, conflicts with current non-goals | Reopen only if TeaPrompt explicitly becomes a runtime product and measured context failures survive existing modular loading. |

## Shared Findings

### Corpus and extraction

- A local inventory observed 603 Markdown files: 132 system prompts, 84 system
  reminders, 65 agent prompts, 147 tool descriptions, 7 tool-parameter notes,
  80 skills, and 88 data/template fragments.
- All 603 files carry a `ccVersion`; 95 distinct origin versions appear. This is
  a mixed-age assembled snapshot, not 603 strings newly authored in v2.1.218.
- Target formatter tests passed 7/7. They cover name/path/metadata/source-escape
  mechanics, not completeness or activation.
- Published `prompts-2.1.218.json` reconstructed 603 unique target Markdown bodies
  exactly in a coordinator comparison.
- The official darwin-arm64 native package was unpacked through `tweakcc@4.3.2`.
  Six of eight selected bodies were found as complete source strings after
  source-escape normalization; the two dynamic bodies exposed literal clause
  matches but not one complete rendered body.
- Public `tweakcc/tools/promptExtractor.js` is heuristic (including a default
  length floor plus include/exclude rules). A fresh run over the unpacked
  v2.1.218 JavaScript returned 416 strings, not the published 603. The delta was
  not resolved, so full extraction reproduction remains unknown.

### Mechanism vs. local gap

| Mechanism | Existing coverage | Decision |
| --- | --- | --- |
| Research before asking | Safe assumptions and low-question rule exist, but no proportionate local evidence check | CCSP1 adopt |
| Full-scope autonomy | Dispatch, brief, implement, and harness policy | CCSP6 no change |
| Anti-bloat / no speculative fallback | Minimality and implement | no new candidate |
| Delegation cost/context heuristics | Host wrapper and runtime concern | CCSP5 no change |
| Review calibration | Claims ledger exists; reachable scenario absent | narrow CCSP2 adopt; broader modes no-change |
| Durable memory quality | Recurrence/promotion exists; quality/revalidation criteria incomplete | CCSP3 adopt |
| Exact proposal digest | Governance schema lacks it; no enforcing host in TeaPrompt | CCSP4 defer |
| Automatic skill upkeep | Existing promotion authority conflicts | CCSP7 reject |
| Conditional prompt compiler | TeaPrompt already separates source lenses, skills, and host enforcement | CCSP8 reject |

## Evidence vs Inference

| Claim / item | Status | Basis / constraint |
| --- | --- | --- |
| Claude Code v2.1.218 existed and was released 2026-07-22 | `verified` | Official Anthropic release + npm registry metadata checked 2026-07-24. |
| Pinned Piebald target has 603 categorized Markdown fragments | `verified` | Local pinned clone and programmatic inventory. |
| Published JSON reconstructs all target Markdown bodies | `verified` | Coordinator comparison: 603/603 unique bodies. Covers renderer output only. |
| Selected prompt bodies originate in the official native artifact | `verified-with-scope` | Eight selected checks: six complete after escape normalization, two dynamic bodies only clause-level; not a corpus claim. |
| Piebald's full corpus is complete/exact/active | `author-claimed` | No 603-body binary extraction match; conditional activation not instrumented. |
| Public extractor alone reproduces the published corpus | `refuted for this run` | Fresh run returned 416 vs published 603; cause unresolved. |
| CCSP1–CCSP3 wording improves agent behavior | `[INFERENCE]` | Local contract gaps and panel agreement; no A/B behavioral run. Structural guards prove presence, not effect. |
| CCSP4 would close review/apply substitution | `[INFERENCE]` until host proof | Cryptographic binding is a plausible mechanism; no host broker/negative test exists here. |
| Prompt text may be copied under Piebald MIT | `unknown` | Dual notices; no legal determination. Project policy therefore keeps a no-copy boundary. |

## Disagreements / Residual Risks

1. **CCSP2 breadth.** ReviewMethodology favored precision/recall objectives,
   tri-state candidate vocabulary, fixed caps, and scanner angles. Four lenses
   favored only the reachable-failure rule. Merge decision: adopt the common
   narrow gap. Broader additions lack local noise/miss evidence, duplicate the
   Claims Ledger, and import host-specific fan-out/cap choices.
2. **CCSP3 surface breadth.** MemoryEvolution proposed an additional automatic
   skill-upkeep prohibition in `artifact-promotion.md`. Merge decision: do not add
   it. Existing authority/recurrence rules already block silent promotion, while
   an absolute one-occurrence ban would contradict the established narrow-repair
   and explicit-project-decision paths.
3. **CCSP4 urgency.** GovernanceSecurity called the missing digest a real
   integrity gap and steelmanned immediate template repair. Merge decision:
   preserve it as a high-value deferred candidate. The domain-pack rule requires
   explicit human approval, and a field without an enforcing host can be mistaken
   for a guarantee.
4. **Extraction reproducibility.** EvidenceProvenance called the extractor
   private. Coordinator inspection refuted that wording: source is public. The
   stronger observed residual is count divergence (416 fresh vs 603 published),
   so complete reproduction is still not established.
5. **Behavioral uncertainty.** Structural wording guards can prevent drift, not
   prove fewer questions, better findings, or better memory. The adopted changes
   remain falsifiable hypotheses at behavior tier.
6. **License uncertainty.** The record uses a precautionary no-copy boundary and
   is not legal advice.

## Evidence Actually Checked

### Executed

- Pinned clone identity via `git log`.
- Programmatic corpus inventory: 603 files, seven families, 95 `ccVersion` values.
- `node --test tools/promptMarkdownUtils.test.mjs`: 7 passed, 0 failed.
- Official npm wrapper/native artifact retrieval through `npm pack`.
- Native package unpack through `npx --yes tweakcc@4.3.2 unpack`: v2.1.218,
  21,317,617 JavaScript characters.
- Selected byte/string checks against the official native artifact.
- Public extractor run with `@babel/parser`: 416 strings emitted.
- Published JSON ↔ target Markdown body comparison: 603/603 unique bodies.
- TeaPrompt focused baseline:
  - `validate_governance.py`: 12 valid, 0 invalid.
  - `validate_skill_examples.py`: all nine core + three domain-pack examples.
  - `lint_skills.py`: 158 files, 0 errors, one known governance-pack length warning.
- Post-adoption verification:
  - three one-shot smoke scenarios exercised the changed contracts: Brief used available repository evidence instead of asking; Review refused to confirm an unsupported null-dereference claim; Handoff retained the durable root-command lesson while excluding live branch state and a lookup-recoverable version.
  - affected prompt/guard tests: 260 passed.
  - repository `make all`: 1000 tests passed; link, governance, project-knowledge, record-hygiene, benchmark, skill-example, and ROUTE-001/002/003 gates passed; the pre-existing governance-pack length warning remained the only lint warning.
- Seven parallel read-only lenses; all complete deliverables recovered before
  synthesis.

### Read

- Pinned target README, CLAUDE note, license, changelog, selected prompt files,
  Markdown updater, and formatter tests.
- Public `tweakcc` extractor implementation and merge/filter behavior.
- Anthropic release metadata, npm metadata, package license pointer, and legal
  page.
- Current TeaPrompt harness policy, project knowledge, skill map, external
  adoption/promotion lenses, all-skill panel, the affected core skills/source
  lenses, governance token schema, and comparable survey/guard records.

### Not executed / unknown

- No live Claude Code session captured the final composed prompt or conditional
  activation set.
- No exhaustive semantic review or binary match of all 603 fragments.
- No behavioral A/B test of old vs adopted TeaPrompt wording.
- No host implementation of CCSP4 digest binding.
- No legal analysis of license ownership or reuse rights.
- No model/provider-independence claim for the seven lenses.

## Falsifiability

This decision is wrong if any of the following occurs:

- CCSP1 causes disproportionate reconnaissance or fails to make clarification
  questions more specific; remove or narrow the rule.
- CCSP2 suppresses actionable code defects because a concise reachable scenario
  cannot yet be constructed; amend it to permit explicitly labeled uncertainty,
  then gather local review noise/miss evidence before adding a second vocabulary.
- CCSP3 rejects a recurring non-obvious lesson or triggers routine open-ended
  revalidation; narrow the exclusions or scope revalidation to changeable facts.
- A documented, reproducible public extraction command yields all 603 published
  fragments from the pinned binary; upgrade the reproduction status and retire
  the 416/603 blocker.
- A concrete host broker needs exact proposal binding and has deterministic
  mismatch-rejection tests; seek explicit approval and re-litigate CCSP4.
- The adopted sentences disappear from a named skill/source surface while the
  survey guard still passes; the guard is inadequate.
- A new core skill, route, runtime, dependency, or verbatim upstream wording is
  attributed to this survey; that contradicts the decision.

Guard: `plans/tests/test_claude_code_system_prompts_survey_record.py`.
