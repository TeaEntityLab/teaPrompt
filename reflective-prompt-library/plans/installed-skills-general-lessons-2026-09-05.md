# Installed-Skills General-Lessons Survey and Adoption — 2026-09-05

> **Status: decided, guarded, and verified — ten clean-room sentences (and one template gate line) adopted by user direction; six survey lessons held or rejected; sources recorded by functional descriptor only.** User instructions, in order: "Review all skills you know, especially harness-generated ones; don't record project-specific terms or skill names; survey general-purpose lessons; skip project-based skills and don't log them", then "so non-project-bound skills — what could I learn or update this project's skills? If worth it then add or update skills." Authority chain unchanged: `06-repo/AGENTS.md` and the invoked `SKILL.md` contracts govern; this record is evidence and design judgement, not an operating rule. No external skill was installed, copied, or depended upon; no source skill is named here — each is described by what it does.

## Research Question

Across every skill installed on this workstation that is not bound to a private project, which general-purpose lessons does TeaPrompt's library already hold, and which would make an installed TeaPrompt skill better if written as text on the surface where the failure occurs?

## Method

- Corpus: 84 installed skills across four skill homes, read in full at the top-level instruction file (about 850 KB of prose): 13 harness-generated skills that are general or technique-general (26 further harness-generated skills are bound to private projects and were never opened, by instruction), 42 third-party workflow-pack skills (autonomous loops, planning and interview, review and security, environment and lifecycle), 11 vendor platform and web-performance routers (their ~340 reference files listed, six sampled), 5 skill-lifecycle / discovery / locale / CLI-wrapper skills, and this library's own 13 as the comparison target.
- Seven read-only extractors on the `task` backend, one per disjoint slice, each bound to an allowlist and required to output functional descriptors only; 7/7 delivered complete deliverables over the hub before yielding. Skill text was treated as data; no command any skill describes was run.
- Coordinator spot-verified four load-bearing extractor claims against the files (a truncated harness-generated file, a skill with no frontmatter, the LLM-code smell taxonomy, a high-permission CLI recipe): 4/4 confirmed.
- Adoption bar (same as the three earlier same-day passes): the sentence names the failure it defends, cites the closest existing TeaPrompt line and shows it does not already say this, names the smaller alternative rejected, lands on one surface, additive, at most two sentences, clean-room wording, no fixed numeric caps (ATT-7), no foreign vocabulary, no tenth core skill.

## Direct Recommendation (as of 2026-09-05)

TeaPrompt already holds the ten lessons that converge across three or more unrelated skill families (run-and-read verification, external stop conditions, pass/fail defined before editing, frozen intent, author-never-self-approves, evidence tiers, closed output contracts, description-as-trigger, live source over memory, hard-stop on missing runtime). What the survey exposed is **ten places where a concrete, commonly-broken rule was implied by a principle but not written where an installed agent acts**: question routing before asking the owner; masking fallbacks; behavior-locking before refactor; harness-vs-product failure and exit-status reading; post-verification edits reopening verification; empty findings and pre-existing attribution in review; credential placement and rotation; independent-method checks on generated counts; composed budgets and merged-result gates in generated flows. All ten are adopted below. Lessons that are host-owned (tiered memory, worker claim tokens, cancellation order, install-trust heuristics) or outside the library's scope (locale, visual verdicts, progressive-disclosure routers) are recorded as held or not applicable.

## Required Wording Changes (final, by user direction)

| ID | Surface | Sentence (clean-room) |
| --- | --- | --- |
| GL-1 | `reflective-brief` Workflow step 4 (appended) | Before an unknown becomes a question to the user, classify it: answerable from the repository or tools (look), safe to assume (state it with its status), or the owner's decision (ask); only the last kind is asked. |
| GL-2 | `reflective-implement` Verification (new paragraph) | When a check fails, first establish whether the failure is in the check itself — its harness, environment, or inputs — or in the change; a broken check is reported as could-not-run and repaired or escalated as a check, never satisfied by editing the product. Read the exit status and the actual output: a log line that says success while the process failed, or a run that skipped the relevant tests, is not a pass. |
| GL-3 | `reflective-implement` Verification (same paragraph) | Every edit after the last verification run, including cosmetic cleanup or formatting, reopens verification; the reported result is the run against the final state of the change. |
| GL-4 | `reflective-review` For Code Review (after "Lead with findings") | An empty findings list is a valid result; never add a finding to make the review look thorough. Attribute each finding as introduced by the change or pre-existing; a pre-existing defect is reported, not charged to the change. |
| GL-5 | `flow-control-generator` structure rule 5 Budget (appended) | When a stage is itself a loop or retries, the composition's worst case is the product of the caps: declare one total budget (steps or wall-clock) that every level decrements, and have the outer script pass its remaining budget to the inner one. |
| GL-6 | `flow-control-generator` structure rule 4 Gates (appended) + fan-out template | For fan-in, the gate runs over the merged result as well as the branch tally: branches that each pass can conflict when combined. Template line after synthesis: `./checks/verify-merged.sh "$STATE/final.md"  # gate: merged result, not only the branch tally`. |
| GL-7 | `reflective-risk` Never (new bullet) | Do not place a credential in a command line, a transcript, or a source file to make a step work; a step that needs one waits for a secret-store path or the owner. An exposed credential is revoked or rotated first — removing it from source or history does not revoke it. |
| GL-8 | `reflective-research` State Ledger (new bullet) | A count, inventory, or catalog the agent generated is checked by a second method that shares none of the generator's logic — a cruder search, a hash, a fixture with a known answer; re-running the generator, or agreement between the generator and its own summary, is not a check. |
| GL-9 | `reflective-implement` Never (new bullet) | Do not add a fallback, catch-all, retry, or silent default that hides a failure instead of fixing its cause; a fallback is legitimate only at an external or version boundary, documented, preserving the failure evidence, and tested on both paths. |
| GL-10 | `reflective-implement` During Editing (appended to the tests bullet) | For a behavior-preserving change (refactor, cleanup, compression), first lock the current behavior with the narrowest tests that would fail if it changed, then change one kind of thing per verified pass. |

Sizes after: brief 5,185; implement 12,021; review 9,582; risk 7,587; research 11,411; flow-control-generator 19,580 bytes — all under the 20,000-char lint threshold; lint 0 errors, 1 pre-existing warning. The Small-Change Fast Path is byte-identical.

## Candidate Adoption Ledger

| Candidate | Source (functional descriptor; families stating it) | Failure defended | Closest existing line and why it does not say this | Smaller alternative rejected | Disposition |
| --- | --- | --- | --- | --- | --- |
| GL-1 | the strategic-planning and ambiguity-gated interview skills; the methodology library's own routing lens (3 families) | the owner is used as a search engine, or a code fact is treated as a product choice | `brief` step 5 classifies *inputs* by provenance; step 4 states unknowns; `dispatch` probes intent on low routing confidence — none says look before asking | rely on the `Authority / Missing Data Notes` output field (names missing data; does not say to look first) | **Adopted** |
| GL-2 | the adversarial-QA cycle and persistence loop skills (2 families) plus the coordinator's own reproduction in this pass (an outer `set -e` masked the template's exit code) | product edited to satisfy a broken probe; "SUCCESS" text read as a pass over a non-zero exit or a skipped suite | `implement:42` run-and-read says nothing about *what* is read; `implement:145` "cannot run, report why" does not distinguish a failing harness from a failing change | extend `implement:42` (it governs claims, not diagnosis) | **Adopted** |
| GL-3 | the persistence loop and durable-ledger loop skills (2 families) | a tidy pass after the last green run reintroduces a regression that the report never saw | `implement:42` — checks *were* run and read, on an earlier state; loophole | none smaller; the sentence is one clause | **Adopted** |
| GL-4 | the defect-first review agent and dual-lane merge review (2 families) | review theatre (padding to look thorough); pre-existing defects charged to the change | `review:123` reachability rule defends speculation, not padding or attribution | rely on `review:123` | **Adopted** |
| GL-5 | three loop skills whose stacked caps contradict each other (2 families, one by contradiction) | nested loop inside a flow stage legally runs past every single ceiling | `flow-control:81` caps per script; `flow-loop:40,59` caps per loop; no composition rule | put it on the loop pack (inner level; and at the lint threshold) | **Adopted** |
| GL-6 | the parallel coverage fan-out (harness-generated) and parallel execution engine (2 families) | per-branch passes conflict when combined; the template itself had no gate after synthesis, contradicting its own rule 4 | `flow-control:80` gates "after each stage"; the fan-out template gated the branch tally only | comment `# gate: none (accepted)` after synthesis (documents the gap instead of closing it) | **Adopted** (rule sentence + template line; dry-run observed) |
| GL-7 | the vendor CLI, setup-wizard, and security-audit skills (3 families) | tokens land in shell history, logs, transcripts; a scrubbed history is called a fix | `risk:42,63,109,125` name secrets as a sink and forbid ambient credentials on remote hosts; none says where a credential may not be placed, or that revocation precedes the code fix | `implement` Never (execution surface, but every credential-touching change routes through the risk gate first; one surface) | **Adopted** |
| GL-8 | the comment-derived route catalog and private-module sideload (harness-generated); the coverage fan-out's union gate (2 families) | a generator's error reproduces on re-run and the number becomes fact | `research:104,132` verify claims *from sources* and reject summaries; nothing covers artifacts the agent generated | put it in `review` (consumer; research produces the count) | **Adopted** |
| GL-9 | the LLM-output cleanup skill's smell taxonomy; the platform review skill's harm-named anti-patterns (2 families) | masking fallback: a try/except, default, or retry that hides the defect | `implement:40` (expected outputs), `:39` (oracles), `minimality` Safety Floor — none names fallbacks; grep for fallback/swallow/suppress found no text | `minimality` Safety Floor (a gate, not the writing surface) | **Adopted** |
| GL-10 | the LLM-output cleanup skill (lock behavior, one smell per verified pass); the refactor-aware review lens (2 families) | a refactor silently changes behavior with no test to catch it; a big-bang cleanup cannot localize its regression | `implement:101` red-first covers behavior changes and defect fixes only | none smaller | **Adopted** |
| H-1 | research skills: date and version every current-practice claim | stale best practice | held: `research:45,46,126,131,133` | — | **Held** |
| H-2 | planning skills: at least two options or explicit invalidation; steelman | one-option theatre | held: `spec-plan` Implementation Decision Gate `Counterargument`; `:205` rejected alternatives | — | **Held** |
| H-3 | loop skills: route a failing check that traces to a wrong criterion back to planning | patching a bad spec locally | held: `implement:39` oracle-wrong → stop, Human Review; `:41` finding → criterion | — | **Held** |
| H-4 | skill-lifecycle skills: retire rules transcripts show unexercised | prompt bloat | held: `handoff-retro` proposed action `retire`, retirement trigger field | — | **Held** |
| H-5 | review skills: restate severity per skill | vocabulary collision | held: `review:119-122` defines Critical/High/Medium/Low | — | **Held** |
| H-6 | cancellation protocol: preserve-vs-wipe per mode | non-resumable abort | held: `flow-loop:70` distinct exit codes; `flow-control:84` partial state left on disk | — | **Held** |
| N/A | tiered memory, worker ACK/claim tokens, cancellation order, popularity-as-install-trust, locale encoding, visual verdict scoring, thin-router-plus-references | — | host-owned or outside the library's scope (no TeaPrompt surface exercises them; trigger evals with holdouts are already practiced at repo level by ROUTE-001/002/003) | — | **Not applicable** |

## Reproduction (observed)

The modified fan-out template was extracted verbatim from `flow-control-generator/SKILL.md` and run under `/bin/bash` 3.2.57 with a stub agent, two fan prompts, a synthesis prompt, and a `checks/verify-merged.sh` that rejects a `CONFLICT` marker. Pass path: exit 0, `state/final.md` holds the synthesized output. Fail path: both branches produce non-empty output (tally passes), the merged gate rejects, exit 1 — the failure GL-6 defends. This reproduction is kept as a regression test in the guard.

## Evidence vs Inference

- **Observed:** every TeaPrompt line cited above, in the worktree, before and after the edit; sizes and lint output; the stub dry-run; the four extractor spot-checks.
- **Extractor-reported (read in full by an extractor, not by the coordinator):** the source-skill wording behind each descriptor; the per-slice inventories and contradiction lists.
- **`[INFERENCE]`:** that the 33% general share of harness-generated skills (13 of 39) would hold on another workstation; that an installed agent reads a Never bullet more reliably than a principle two sections away (the premise of every pass in this line, not measured here).
- **Not done:** no source skill executed; no ROUTE fixture changed (no trigger text changed); no vendor reference corpus read beyond six sampled files.

## Falsifiability

This record is wrong or must be re-litigated if: (1) any GL sentence is removed without a documented supersession or is cited as a host guarantee; (2) GL-7's "waits for a secret-store path or the owner" is read as authorization to store a credential in the repository; (3) the fan-out template's merged gate is removed while rule 4 still says fan-in gates the merged result; (4) a held row's trigger fires (a wrong-criterion loop, a severity collision, a non-resumable abort) and the row is not re-opened; (5) a TeaPrompt skill gains a source skill's name, a vendor name, a fixed numeric cap, or a fourth strictness ladder from this line; (6) the dry-run regression test is deleted rather than updated when the template changes.

## Completion Ledger

| Item | Status | Evidence |
| --- | --- | --- |
| 84-skill survey with 26 project-bound skills skipped unopened | `verified` | Method; extractor coverage ledgers |
| Ten adoptions at single surfaces, additive, clean-room | `verified` | sentences present; sizes above |
| Template self-consistency fix with observed dry-run | `verified` | Reproduction |
| Held / not-applicable rows with cited lines | `verified` | ledger |
| Guard | `verified` | `plans/tests/test_installed_skills_general_lessons_record.py` |
| Decision Index bullet, case-study row, state row | `verified` | `PROJECT_KNOWLEDGE.md`, `external-adoption-case-studies-2026-06-20.md` |
| Repository verification | `verified` | `make all` after the adoptions |
