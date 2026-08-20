# 3xa-harness Survey — 2026-08-20

> **Status: decided (non-authoritative); external-survey panel record, no
> adoption.** 3xa-harness is retained as study material. Two mechanisms remain
> study-only candidates with explicit local triggers; its scripts, five-skill
> lifecycle, installation routes, and CI template are not adopted. No TeaPrompt
> skill, lens, verifier, dependency, runtime, or project-knowledge rule was
> created or changed. `06-repo/AGENTS.md` and governed skill contracts remain
> authoritative; this record is evidence and a decision, not an operating rule.

## Purpose

Preserve the completed seven-lens survey of 3xa-harness so its adoption question
is not re-litigated from chat memory: what the bundle actually provides, which
claims survive execution and adversarial mutation, and whether TeaPrompt should
study, reproduce, adopt, or deploy any part of it.

## Target and Version

- Review target: [`3xachris/3xa-harness`](https://github.com/3xachris/3xa-harness),
  checked 2026-08-20.
- Pinned release: `bundle-v0.1.0`; pinned commit
  `bea12d3c0a1b25672fd027f627c148075a7f8ed7` (2026-08-16). The annotated tag
  object is `4c3b19f35bf1a978e096f03a1116b84b3b954dec`; the tag is not
  cryptographically signed. The merge commit is GitHub-verified, which is not a
  maintainer release signature or artifact attestation.
- Component versions: `harness-core` 0.3.0, `harness-debug` 0.2.0, and
  `harness-audit` 0.1.0.
- Repository shape at the pin: 53 tracked files, eight skills, and four Python
  scripts totaling 2,059 lines. The core lifecycle is `workorder` →
  `sensory-gate` → `decision-log` → `handoff` → `honest-closeout`; add-ons are
  `staged-diagnosis`, `claim-audit`, and `repo-audit`.
- License boundary: repository code and documentation are MIT. Bundled Space
  Grotesk and JetBrains Mono assets carry local SIL OFL 1.1 texts and an asset
  provenance ledger. The asset-fetch commit and generated-image recipe are not
  independently attested.
- Volatility trigger: this was a young, single-listed-contributor project at the
  check date. Re-pin the source and re-run containment, hash, status, CI-exit,
  and install-lifecycle checks before relying on a later revision.

## Panel Execution Mode

Method contract: `04-agent/workflow-recipes.md` §Parallel Lens Review with the
host `parallel-lens-review-packet` wrapper.

1. The merge owner cloned the pinned tag, read the core skills, add-ons,
   verifier, self-check, templates, manifests, demo, license surfaces, and
   release metadata, then executed the deterministic checks and adversarial
   mutations listed below.
2. One shared packet was written inside the transient clone. Its corrected
   SHA-256 was
   `b86d3e2faeafcfba513b4f91fa949c166f8b92432037275b56ff3f8a9ac175ac`.
   It separated observed, author-claimed, `[INFERENCE]`, and unverified claims
   and carried one load-bearing question per lens. The packet and clone were
   deleted after synthesis; this record contains the durable evidence.
3. Seven read-only lenses fanned out in one batch: evidence, architecture,
   reproducibility, security/provenance, code correctness, usability, and
   strategic fit. All seven completed. Five scout yields were schema-coerced;
   all five complete deliverables were recovered by tier-1 DM-wake over IRC.
   The reviewer and security-reviewer deliverables arrived directly.
4. The merge owner, not the read-only lenses, executed the reproduction and
   mutation slice. No lens edited TeaPrompt or upstream files.
5. Role labels are review perspectives. No claim is made that distinct model
   providers or named personas were invoked.

## Lenses

| Lens | Load-bearing question | Main result | Verdict |
| --- | --- | --- | --- |
| Evidence auditor | Which claims are executed, fixture-only, or unsupported? | Manifests, self-check, and audit snapshots reproduce; the demo is static, its hash is a placeholder mismatch, and no behavioral efficacy evidence exists | AGREE WITH CHANGES |
| Architecture | Is the five-stage lifecycle cohesive and proportionate? | Coherent method, but duplicated state, unenforced authority, append-only context growth, a universal two-strike rule, and GUI-centric rejection semantics create disproportionate ceremony | AGREE WITH CHANGES |
| Reproducibility | What test tier is actually reached? | Python compile/smoke and the known-good fixture run; zero discovered unit tests, no negative suite, and critical verifier mutations pass | AGREE WITH CHANGES |
| Security and provenance | What executes, writes, or loses source identity? | User-facing scripts have no direct network/process launch, but installs are unpinned and collision-prone; configured paths and symlinked scan inputs can escape root and expose snippets | AGREE WITH CHANGES |
| Code correctness | Are mutation findings real contract defects? | All packet mutations confirmed; additional DONE-substring, gate-disposition, and repo-audit containment gaps found | AGREE WITH CHANGES |
| Usability | Can users apply the workflow without hidden ceremony? | Useful for long multi-party work, but too rigid for small/single-operator tasks; headless sensory review and proportionate verification are missing | AGREE WITH CHANGES |
| Strategic fit | Is any mechanism a verified TeaPrompt gap? | Near-total methodology overlap; two concepts remain study-only, scripts and full lifecycle rejected | AGREE WITH CHANGES |

## Panel Consensus

- **Decision:** `AGREE WITH CHANGES` — unanimous, **7 of 7 lens verdicts**;
  no AGREE and no DISAGREE.
- **Method quality:** the five-stage lifecycle is coherent, explicit, and
  unusually honest that protocol is not enforcement. Pointer-not-copy
  handoffs, a cold-reader test, reviewed-batch identity, fixed closeout states,
  and evidence-first reporting are useful study material.
- **Executable quality:** `verify_closeout.py` is a syntax and linkage check
  script, not a DONE validator. It accepts parseable FAIL/BLOCKED answers under
  DONE, ignores recorded file hashes, accepts duplicate acceptance IDs and
  out-of-root evidence/archive paths, mistakes body text containing `DONE` for
  the status, and does not reconcile approve/reject disposition. The checked-in
  demo proves the hash gap while still passing self-check.
- **Evidence quality:** repository-owned self-check and CI are real and were
  reproduced, but they smoke one known-good static fixture. No negative test
  suite or baseline/treatment agent evaluation shows reduced scope drift,
  better handoffs, or more truthful closeouts.
- **Local fit:** TeaPrompt already covers almost every methodology mechanism
  through risk-scaled workflows and existing validators. External existence is
  not a verified local gap and does not count as local promotion recurrence.

### Use-Case Recommendation

| Use case | Recommendation |
| --- | --- |
| `study` | **yes** — study the lifecycle vocabulary, reviewed-batch identity concept, pointer-not-copy handoff, and cold-reader test |
| `reproduce` | **partial** — the pinned manifests, scripts, self-check, and audit snapshots reproduce; the verifier's intended safety properties do not |
| `adopt` selected patterns into TeaPrompt | **no current change** — 3XA-1 and 3XA-2 remain study-only with local-evidence triggers |
| `adopt` scripts or five-skill lifecycle | **no** — weaker than local validators, disproportionate, and unsafe unchanged on untrusted repositories |
| `deploy` as a governed repository/fleet gate | **blocked at this revision** — containment, status/hash/disposition enforcement, CI exit handling, immutable installation, and clean update/rollback are missing |

## Required Wording Changes

These are upstream-facing corrections consolidated from the panel. None was
applied to TeaPrompt or the upstream repository.

1. **Name the executable accurately.** Describe `verify_closeout.py` as a
   “syntax and linkage check script,” not a closeout/DONE verifier. Enumerate
   that it does not prove independent execution, compare gate hashes, require
   PASS under DONE, or constrain evidence to the project root.
2. **Make DONE parsing and linkage internally consistent.** Parse the declared
   closeout heading rather than searching for the word `DONE`; reject duplicate
   AC IDs; require every AC to be PASS for DONE; and reconcile disposition,
   reviewer, archive, and decision-log pointers.
3. **Implement reviewed-byte binding.** Parse each recorded file/hash pair,
   calculate the current digest, and fail on missing, extra, changed, or
   duplicated entries. Replace the demo's `sha256-demo` placeholder with the
   actual digest and add negative fixtures.
4. **Enforce a filesystem boundary.** Resolve and require configured outputs,
   evidence, archives, baselines, histories, reference ledgers, reports, and
   scan candidates beneath `--root`; reject absolute paths, `..` escapes, and
   external symlink targets. Warn that paths/snippets may enter agent, terminal,
   or CI logs.
5. **Fix CI exit policy.** Remove blanket `continue-on-error: true`; explicitly
   choose whether exit 1 is advisory and fail on exit 2/3 or missing/miswired
   inputs. Fail if copied demo paths remain. Call non-blocking integration
   “Advisory CI.”
6. **Make installation reproducible and reversible.** Document a full-commit
   pin; verify installed source identity; abort on destination collisions;
   clean-replace rather than merge; record inventory; and document update,
   rollback, and uninstall. Do not recommend `@latest` for governed use. Pin
   GitHub Actions by full commit SHA.
7. **Scale ceremony to risk and environment.** Replace the universal
   two-strike stop with a declared retry/hypothesis budget, support a
   single-operator mode without fictional role separation, allow proportionate
   closeout evidence for low-risk work, and provide a headless sensory-gate
   path instead of requiring file dragging.
8. **Calibrate product claims.** Replace “prevents” outcome language with
   “structures and makes inspectable” until a baseline/treatment behavioral
   evaluation exists. State that repository code/docs are MIT while bundled
   fonts remain OFL, and distinguish GitHub commit verification from a signed
   release or attestation.

## Candidate Adoption Ledger

| ID | Candidate | Status | Evidence | Next action or trigger |
| --- | --- | --- | --- | --- |
| 3XA-1 | Reviewed-batch hash binding: bind named reviewer/scope and reviewed asset digests to shipped bytes | Deferred / study-only 2026-08-20 — no artifact change | `sensory-gate` specifies hashes, but `verify_closeout.py` never compares them and the demo's placeholder mismatches; no TeaPrompt local asset-drift incident was established | Reconsider after a documented local reviewed-vs-shipped asset drift or verified contract omission; repair an existing surface and add deterministic digest comparison. Falsifier: digest fields become unmaintained placeholders |
| 3XA-2 | Cold-reader handoff test: a fresh reader must recover one concrete next action from the artifact without chat | Deferred / study-only 2026-08-20 — no artifact change | `handoff/SKILL.md` documents the test; `reflective-handoff-retro` already provides handoff structure, and no local failure was demonstrated | Reconsider after a documented local handoff where next action cannot be recovered without chat; first test whether the existing skill already covers it. Falsifier: the extra pass adds tokens without reducing handoff failure |
| 3XA-3 | Pathfinding-vs-known-road capability tier | No change 2026-08-20 | TeaPrompt already separates task strictness L1–L6 from execution mode and chooses the smallest workflow; another tier vocabulary would duplicate routing | Revisit only if a capability mismatch cannot be expressed by existing strictness and mode fields; falsifier: labels do not change action, budget, or checks |
| 3XA-4 | Import `verify_closeout.py` or a generic closeout form checker into TeaPrompt CI | Rejected 2026-08-20 | Verified FAIL/BLOCKED, hash, duplicate-ID, status, disposition, and containment false passes; TeaPrompt already has narrower deterministic validators | Re-litigate only after repeated local malformed closeouts escape existing checks and a new implementation has adversarial negative tests; never import the pinned script unchanged |
| 3XA-5 | Import `claim_audit.py` / `repo_audit.py` into TeaPrompt | Rejected 2026-08-20 | Existing record-hygiene, link, project-knowledge, governance, and adoption-state validators cover local needs; audits are heuristic, write root state, and have configured-path/symlink boundary gaps | Reconsider only for a measured local blind spot existing validators cannot express, after containment and no-dirty-tree behavior are proved |
| 3XA-6 | Adopt or deploy the complete five-skill bundle and documented install/CI routes | Rejected; deployment blocked 2026-08-20 | Near-total methodology overlap, high ceremony, unpinned/collision-prone installs, unsigned tag, fail-open CI, no outcome eval, and unsafe unchanged filesystem boundaries | Reconsider only if TeaPrompt changes scope to distribute an executable harness and a later pinned release fixes P0 correctness/containment plus reproducible install/update/rollback |

No candidate created or changed a TeaPrompt skill, lens, verifier, dependency,
runtime, or project-knowledge rule. Deterministic guard for this record:
`plans/tests/test_3xa_harness_survey_record.py`.

## Shared Findings

### What 3xa-harness does well

1. **Honest layer boundary.** The README repeatedly distinguishes protocol,
   form checks, and human judgment from runtime enforcement and security.
2. **Coherent lifecycle.** Scope freeze/amendment, named human review, decision
   records, pointer-based handoff, and evidence-first closeout form one method
   rather than a loose prompt collection.
3. **Useful handoff discipline.** The cold-reader test is observable, and
   pointers avoid copying state into divergent handoff summaries.
4. **Portable implementation basics.** User-facing Python scripts are
   standard-library-only and make no direct network calls or process launches;
   plugin manifests validate; the repository self-check runs on Python 3.9.
5. **Transparent heuristic audits.** Claim/repo audit docs identify bypasses,
   distinguish warnings from verdicts, and avoid pretending to be security
   scanners.
6. **Clean licensing basics.** MIT repository licensing, explicit upstream
   credits, and local OFL font notices support study and lawful reuse within
   each grant's boundary.

### Load-bearing gaps

1. **DONE false pass:** a parseable `[FAIL]` or `[BLOCKED]` answer under DONE
   satisfies the acceptance-ID presence check and can exit 0.
2. **Reviewed-byte false pass:** the demo records `approved.txt=sha256-demo`,
   while the actual SHA-256 is
   `f4c25b5b45735b3183381384b47a345ce2262a0301a399855a9dd4fe8d052e9f`;
   verifier and self-check still pass because no hash is compared.
3. **Independence false pass:** descriptive text lacking four blocked keywords
   stands in for independent execution; one acceptable line establishes the
   whole report through `any()` semantics.
4. **Containment failure:** absolute evidence/archive paths pass. Repo-controlled
   audit output paths can escape root through absolute/parent paths or symlinks;
   matching scan symlinks can read external host files and emit snippets to
   terminal, agent, or CI logs.
5. **Linkage gaps:** duplicate AC IDs overwrite, DONE is detected by substring,
   and the report's approve/reject disposition is not cross-validated.
6. **Fail-open CI:** step-wide `continue-on-error` masks exits 1, 2, and 3,
   including missing inputs. The template is advisory evidence, not a gate.
7. **Fixture-only assurance:** CI runs one static known-good demo. The claimed
   independent container/unittest result is text, not a retained test or
   container receipt. `unittest discover` found zero tests.
8. **No efficacy evidence:** no controlled agent run measures scope drift,
   handoff recovery, closeout truthfulness, token cost, or operator burden.
9. **Install/source identity gap:** convenience routes do not preserve the
   reviewed commit identity; direct copies can merge or overwrite existing
   skills and lack inventory, clean update, rollback, or uninstall.
10. **Proportionality gap:** fixed multi-file ceremony, GUI-centric rejects, and
    a universal two-strike stop are poorly matched to small, headless,
    single-operator, or high-uncertainty tasks.

## Mechanism vs. TeaPrompt Fit

| Mechanism | Existing TeaPrompt coverage | Verified local gap? |
| --- | --- | --- |
| Frozen work order, scope, ACs, falsifier | Why/What/How/Done, `reflective-brief`, `reflective-spec-plan` | No |
| Human review gate | `reflective-risk`, `reflective-review`, explicit Human Review triggers | No; hash binding remains study-only |
| Decision log / amendments | plans decision archive, project knowledge, candidate ledgers | No |
| Handoff snapshot | `reflective-handoff-retro`, context-handoff contracts | No; cold-reader test remains study-only |
| Honest closeout | `reflective-implement`, AGENTS verification rules, focused behavioral checks | No |
| Claim/repository audit | record hygiene, links, project-knowledge, governance, adoption guards | No |
| Executable runtime/install surface | Standing non-goal: TeaPrompt ships method contracts, not an agent runtime | Out of scope |

## Evidence vs Inference

| Claim | Status | Basis |
| --- | --- | --- |
| Release/component identity, tree shape, MIT/OFL boundaries | Observed / verified | Pinned clone, GitHub API, manifests, license files; checked 2026-08-20 |
| Self-check succeeds on Python 3.13 and upstream Python 3.9 | Observed / executed + CI-read | Local `python3 ci/self_check.py`; two successful upstream Actions runs at the pin |
| Four Claude manifests validate | Observed / executed | `claude plugin validate` on root, marketplace, debug, and audit manifests |
| Claim/repo audit documented snapshots reproduce | Observed / executed | Local CLI runs at the pin; repo audit wrote two untracked ledgers |
| Verifier false passes listed above | Observed / executed | Throwaway-clone mutation matrix plus direct source review by code/reproducibility/evidence lenses |
| Configured audit paths and symlink scans escape root | Observed / source-verified | Security lens traced read/write paths; generalized external egress beyond emitted logs was not claimed |
| Five-skill loop reduces drift or improves outcomes | Unverified | No behavioral baseline/treatment eval or agent-run corpus |
| Workflow ceremony increases token/operator cost | `[INFERENCE]` | Required artifacts and role steps observed; cost was not measured |
| A later release fixes any blocker | Unknown / volatile | Must re-pin and re-run checks |

## Disagreements / Residual Risks

- **Disclosure versus defect severity:** the code-correctness lens steelmanned
  that upstream explicitly calls the script a form checker. This reduces the
  severity of semantic-judgment gaps, but not defects inside its stated form and
  linkage scope: out-of-root evidence, DONE substring parsing, disposition
  mismatch, duplicate IDs, and the passing placeholder hash demo.
- **Project-knowledge promotion:** the architecture lens proposed a new durable
  lesson and Decision Index entry. The merge decision rejects that change: one
  external survey is not a new local recurrence, and the existing lesson
  “prompt wording cannot fix execution-layer failures” already governs the
  issue. The survey and external-adoption case-study ledger are sufficient.
- **Usability changes are judgment-tier:** proportional retries, single-operator
  mode, and headless sensory gates are sensible upstream proposals, not defects
  proved by outcome data.
- **No-network finding is narrow:** the three user-facing scripts have no direct
  network/process surface; host agents, install tools, terminal output, hooks,
  and CI logs remain separate egress/trust surfaces.
- Windows, marketplace discovery/auto-update, OpenCode discovery, skills.sh,
  branch protection, and Obsidian behavior were not executed. No conclusion
  depends on them succeeding.

## Evidence Actually Checked

- `git clone --depth 1 --branch bundle-v0.1.0`; commit, tag object, release,
  contributor, license, and security-file metadata — pin above, checked
  2026-08-20.
- Full/targeted reads: README/zh-TW README; five core skills; three add-on
  skills; `verify_closeout.py`; both audit scripts; `ci/self_check.py`;
  `.github/workflows/self-check.yml`; CI template; all plugin manifests;
  `.harness-audit.json`; demo order/decision/closeout/evidence/gate files;
  collaboration and audit docs; license/asset provenance files.
- `python3 ci/self_check.py` on Python 3.13.0 — exit 0: five JSON manifests,
  16 declarations / eight unique skill targets, 58 relative links, three
  script syntax/import/CLI smokes, demo exit 0, `SELF_CHECK_OK`.
- GitHub Actions API — two successful Python 3.9 self-check runs at the pinned
  commit.
- `claude plugin validate` on four manifest surfaces — all passed.
- `claim_audit.py --root .` — exit 1 as designed: 22 records, two candidates,
  three restatements. `repo_audit.py --root .` — exit 0: 16 size targets, 61
  pointers, two source files, six tracked docs, no findings; wrote two untracked
  root ledgers.
- `python3 -m unittest discover -v` — exit 5, zero tests.
  `python3 -m compileall -q verify_closeout.py ci addons` — exit 0. Optional
  `ruff` found two E741 style diagnostics; optional `mypy` found 25 diagnostics;
  upstream configures neither, so neither is treated as a runtime failure.
- Eleven verifier mutations: five malformed-linkage cases correctly warned;
  FAIL-under-DONE, fake independence, altered reviewed file, duplicate AC ID,
  absolute evidence, and absolute archive all exited 0. Direct code review found
  additional DONE-substring, disposition, and repo-audit containment gaps.
- Not executed: clean marketplace/Codex/OpenCode/skills.sh install and discovery;
  Windows; Obsidian; behavioral agent evaluation; branch protection; release
  attestation verification beyond the observed absence.

## Falsifiability

- The executable-risk verdict is repaired, not refuted, if a later pinned
  release adds root/symlink containment, PASS/status/disposition/hash checks,
  adversarial negative fixtures, and explicit blocking CI semantics. Re-run the
  mutation matrix before changing the disposition.
- The no-efficacy-evidence finding is wrong if upstream publishes a reproducible
  baseline/treatment evaluation tying the bundle to task outcomes rather than
  form compliance.
- The no-local-gap decision is wrong if TeaPrompt records a concrete
  reviewed-byte drift or cold-reader handoff failure that existing governed
  surfaces cannot address. That triggers 3XA-1 or 3XA-2 re-evaluation; it does
  not automatically justify a new skill.
- This ledger is dead text if a trigger fires and no re-evaluation occurs, or if
  a rejected candidate ships without changing its recorded status and guard.
