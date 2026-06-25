# Glossary of Operational Terms

This glossary defines load-bearing terms used across the reflective prompt
library, workflow skills, and validation scripts. Definitions here are
**operational**: they describe observable, testable behavior rather than
abstract intent.

> Individual prompts or skills may use a term in a slightly narrower or
> broader sense. When a definitional question arises, this file is the
> canonical source. If you find a usage that contradicts this glossary,
> update the specific file or raise it as an issue.

---

## Non-trivial

A task that cannot be completed with a single, obvious action. It requires
multiple steps, trade-off decisions, or investigation.

**Operational test:** If the task can be done with one edit or one shell
command and the outcome is obvious before running it, it is trivial.
Otherwise it is non-trivial. A task that needs planning before action is
always non-trivial.

---

## Minimal / 最小

The smallest intervention that satisfies the acceptance criteria. "Minimal"
does not mean "do the minimum work." It means stop at the point where
removing any part would cause an acceptance criterion to fail.

**Operational test:** For each change in the delivered artifact, ask: "If
this change were removed, would a criterion still pass?" If every change
is necessary, the artifact is minimal.

---

## Evidence / 證據

Observable output that confirms or refutes a claim. Evidence is not
reasoning, intent, or explanation. It is data produced by running a check:
a test result, a log line, a diff, a measurement, a linter exit code.

**Operational test:** Can a different agent, starting only from the
delivered artifact and the claim, independently verify the evidence
without re-running the original work? If yes, it is evidence. If it
requires trust in the producer's judgment, it is not.

---

## Risk / 風險

The product of (estimated probability of failure) x (estimated cost of
failure) for a specific task step. Risk is not a general concern or a
vague unease. It attaches to a concrete decision or action.

**Operational test for "high risk":** If the step fails, can it be rolled
back in under five minutes? If no, it is at least medium risk. If the
failure would cause data loss, financial cost, security exposure, or
irreversible state change, it is high risk regardless of rollback time.

---

## Acceptance Criteria / 驗收標準

A set of falsifiable pass / fail conditions that must all be true for the
task to be considered complete. Each criterion must be binary: either it
passes or it fails, with no gray area.

**Operational test:** Each criterion must be verifiable by a different
agent using only the delivered artifact. If the criterion cannot be checked
without asking the original author, it is not specific enough.

---

## Human Review Required / 人工審查

A gate condition that blocks execution or deployment until a named human
has reviewed and approved the artifact. Not a notification, not a courtesy
CC. Automation must stop and wait.

**Operational test:** If no human explicitly approves, the next stage
does not start. No auto-approval timeout, no "assume yes after N days."
The human reviewer must be identifiable by name or handle.

---

## Artifact

A persistent, named output file that carries state across workflow stages.
An artifact is not a conversational message, not a piece of reasoning, and
not a transient tool result.

**Operational test:** A fresh agent session with no prior context can read
the artifact and understand what stage produced it, what it contains, and
what the next stage should do with it. If the session needs the original
conversation history to make sense of the file, it is not an artifact.

---

## Feedback-Gated Engineering Workflow

A work pattern where each stage produces evidence that must pass a quality
gate before the next stage starts. The gates are explicit checks, not
style preferences.

**Operational test:** If the gate rejects the output, the workflow loops
back to the previous stage instead of proceeding. If there is no rejection
path, the workflow is a linear checklist, not feedback-gated.

---

## Hidden Chain-of-Thought (clarified)

Internal reasoning the model generates before producing visible output.
The agent uses this for planning, reflection, and self-correction. It is
called "hidden" because it is not exposed to the user by default.

**Clarification:** Do not expose raw hidden chain-of-thought as an output
artifact. When transparency is needed, provide a concise reasoning summary,
decision record, evidence ledger, checklist, or observable step trace instead.

Structured reasoning sections such as Goal, Assumptions, Socratic audit,
Evidence vs Inference, or Risks are allowed and often required. They are
not raw hidden chain-of-thought when written as deliberate, user-facing
artifacts.

---

## Strictness Level (L1-L6)

A taxonomy of **execution rigor**: how deeply to validate, review, and
gate the work. Defined in `skills/reflective-dispatch/SKILL.md` and
reproduced in METHODOLOGY_MAP.md.

| Level | Use When | Main Surface |
| --- | --- | --- |
| **L1** Daily prompting | Low-risk, short answer, no state | `00-core/daily-minimal.md` |
| **L2** Reflective analysis | Complex reasoning or decision | `reflective-brief` |
| **L3** Engineering task | Code, system design, data flow, tests | `reflective-spec-plan` -> `reflective-implement` |
| **L4** High-risk review | Security, privacy, money, deletion, production | `reflective-risk` |
| **L5** Agent workflow | Long-running, multi-tool, resumable work | `reflective-dispatch` + workflow plans |
| **L6** Strategy overlay | Business, education, organization, long-term systems | `05-domain/` prompts as overlays |

## Formalization Level (L0-L4)

A taxonomy of **automation depth**: how much of a process is codified into
a machine-executable workflow. Defined in `04-agent/sop-compiler.md`.

| Level | Meaning |
| --- | --- |
| **L0** | Prompt-only: low-risk, one-off, cheap to redo. |
| **L1** | SOP artifact: repeated but still human-run. |
| **L2** | Skill + artifact contract: repeated agent-assisted task. |
| **L3** | Skill + verifier: repeatable task with objective checks. |
| **L4** | Runner + gates + hook: high-risk, audited, or frequently repeated workflow. |

## Distinction between Strictness and Formalization

Strictness levels answer **"How carefully should we do this work?"**
Formalization levels answer **"How much of this work should be automated?"**

They are independent. A high-risk task might use Strictness L4 (thorough
review) with Formalization L0 (prompt-only, no runner). A routine ETL
pipeline might use Strictness L1 (low rigor) with Formalization L4 (runner
with deterministic gates). Always qualify bare L-level references with the taxonomy name:
write "Strictness L3" or "Formalization L3", never bare "L3".

---

## Skill (Workflow Skill)

A reusable `SKILL.md` file that encodes a repeatable agent workflow as
natural-language instructions interpreted by the host runtime.

**What it is:** A prompt-level workflow descriptor — a procedure for the
model to follow, not a runtime module with its own process, state,
messaging, or lifecycle.

**Operational test:** A skill can be loaded, read, and followed by any
compatible agent runtime (Claude Code, Codex, OpenCode, Cursor, etc.)
as a text document. If a workflow requires asynchronous messaging between
independent agents, role-specific context isolation, or a persistent
runtime process, a single skill alone is insufficient — those require a
dedicated orchestration layer outside this library's scope. See
`PROJECT_KNOWLEDGE.md` for the full list of non-goals.

---

## Context Load / 上下文負載

Estimated prompt-and-artifact cost of loading and following a workflow skill.
Declared in each `SKILL.md` frontmatter as `low`, `medium`, or `high`.

**Operational test:** A host with tight token budget may defer `high` skills when
Strictness is L1–L2 and route trace shows no need for deep planning or research.

---

## Route Trace / 路由軌跡

User-visible routing record emitted when workflow selection is uncertain or when
`reflective-dispatch` runs. Must include canonical workflow, confidence, and
enabled vs available enhancements.

**Operational test:** A different session can see whether quality was downgraded
and why, without reading hidden reasoning.

---

## Enhancement / 增強檢查

Optional rigor layer beyond the baseline workflow (e.g., security review,
performance check, extra tests). May be disabled for cost, but disabling must
appear in the route trace — not silently.

---

## Minimality Signal Scan / 最小化訊號掃描

A lightweight check inside `reflective-implement`, triggered only when bloat
signals appear (new dependency, extra files, new abstraction, explicit YAGNI ask).
It applies the minimality ladder without requiring a separate `reflective-minimality`
run on every edit.

**Operational test:** If no bloat signal is present, the scan is skipped. If a
signal is present and the smaller path is disputed, route to `reflective-minimality`.

---

## Silent Downgrade / 靜默降級

Routing equivalent intent to lower rigor without making the downgrade visible in
the route trace or output. Prohibited by `plans/ROUTING_CONTRACT.md` R4–R6.

---

## Context Load Deferral / 上下文負載延後

At Strictness L1–L2, hosts may defer skills with `context_load: high` when a
smaller workflow still satisfies intent. Deferred skills must appear in the route
trace under available enhancements with rationale — not as a silent downgrade.

**Operational test:** A cost-sensitive L1 request still names which heavy skills
were deferred and why.



---

## Undocumented Decision Hint / 未記錄決策提示

A **non-blocking** validator warning when git shows governance-surface commits after
the latest `PROJECT_KNOWLEDGE.md` Decision Index date without a decision-record cue in
the commit subject. Mirrors Knowie's drift hint without blocking CI.

**Operational test:** Warning only; exit code stays 0. Add a Decision Index entry or
use a subject cue (`governance`, `panel`, `record`, `route-002`, etc.) to clear it.

---

## Benchmark Fixture Gate / 基準任務固定欄位閘門

Deterministic CI check on `benchmark_tasks.py` golden tasks (workflow mapping,
acceptance criteria, minimum count). Does **not** run LLM benchmark executions.

**Operational test:** `make validate` runs `validate_benchmark_fixture.py`; failures
block merge; manual skill-vs-baseline runs stay optional.

---

## Intent Normalization (zh-TW) / 意圖正規化（繁中）

The deterministic router in `route_paraphrase_eval.py` includes Traditional Chinese
intent keywords alongside English cues. ROUTE-002 holdout groups test zh-TW phrasing
fairness without translating canonical `SKILL.md` contracts.

**Operational test:** A TW phrase in the holdout fixture routes to the same workflow as
its English equivalent intent group.


---


## Plan-Only Without Code / 僅規劃不寫程式

A request for tickets, acceptance criteria, rollout plans, or specs with explicit
no-code context. Routes to `reflective-spec-plan`, not `reflective-implement`.

**Operational test:** Phrase includes planning artifact signals **and** no-code
context (e.g. "plan only", "without touching the repo", 不要改程式).

---

## Plain Review (Non-Production) / 非正式環境審查

Code or diff review for correctness, readability, or regressions **without**
production-risk assessment. Routes to `reflective-review`, not `reflective-risk`.

**Operational test:** Review/diff/PR context plus production negation (e.g.
"not production deploy", 不是正式環境風險) or readability-only scope.

---

## Brief-before-Plan / 規劃前先釐清

Routing boundary: when intent is to narrow scope, assumptions, or stakeholder alignment **before** PRD/ticket breakdown, route to `reflective-brief` — not `reflective-spec-plan`.

**Operational test:** "narrow scope before writing the PRD" routes to brief; "write tickets without code" routes to spec-plan.

---

## Design Comparison (Plan-Only) / 設計比較（僅規劃）

Paper-only API or architecture comparisons without repository changes route to `reflective-spec-plan`, including mixed zh-TW + English phrasing with 不要寫 code cues.

**Operational test:** ROUTE-002 `design_comparison_plan_holdout` phrases route to spec-plan at 100%.

---

## Approved-Spec Delivery / 已核准規格落地

Routing boundary: when intent is to **implement or land an approved spec in the repository**, route to `reflective-implement` — not `reflective-spec-plan`, even when `spec` appears in the phrase.

**Operational test:** ROUTE-003 `implement_not_plan_trap` — "implement the approved spec in the repository", "在 repository 實作已核准 spec", and "落地已核准規格到 codebase" route to implement; "plan the approved spec without repo changes" routes to spec-plan.

---

## Boundary Quick Cues / 邊界速查

Curated top-of-cheatsheet summary of high-confusion routing traps (ROUTE-002 holdout + ROUTE-003 adversarial). Not exhaustive — per-skill trigger cues and holdout fixtures remain authoritative.

**Operational test:** `test_cheatsheet_boundary_quick_cues.py` — marker labels and probe-linked snippets in the quick-cue block; `ROUTING_CONTRACT.md` R12.

---

## Governance Maintenance Playbook / 治理維護手冊

Ongoing upkeep after panel close (Rounds 1–91). Not agent instructions — operator checklist.

**Operational test:** Before router tuning, add fresh ROUTE-002/003 holdout phrases; run `make all`; record decisions in `PROJECT_KNOWLEDGE.md` Decision Index when governance surface changes.

1. Run `make all` on every governance/routing change.
2. Add holdout cases **before** tuning `route_paraphrase_eval.py` keyword rules; `validate_route_fixture.py` blocks accidental shrinkage.
3. Watch non-blocking undocumented-decision warnings from `validate_project_knowledge.py`.
4. Keep manual `benchmark_tasks.py` runs optional — fixture gate only in CI.
5. Reject tenth skill / full `SKILL.md` i18n unless promotion gate met (panel A, Q, W, AJ).
6. When cheatsheet boundary quick cues change, update `BOUNDARY_QUICK_CUE_*` markers and probe snippets in `test_validate_route_fixture.py`; run `test_cheatsheet_boundary_quick_cues.py`.
7. When holdout probe tuples change in `test_validate_route_fixture.py`, mirror cues in EN/zh-TW cheatsheets and run `test_cheatsheet_*_parity.py` (e.g. `test_cheatsheet_dispatch_meta_parity.py`).
8. Keep `CONTRIBUTING.md` Routing Maintenance aligned with `ROUTING_CONTRACT.md` R8–R12 when boundaries or cheatsheet parity steps change.
9. When adding benchmark golden tasks, keep `test_benchmark_covers_all_nine_workflows` green and bump `MIN_TASK_COUNT` in `validate_benchmark_fixture.py` if the floor rises.
10. When changing thinking-lens ↔ skill cross-links, update `SKILL_THINKING_SOURCES` and consumer lists in `01-thinking/` Purpose preambles; run `test_prompt_cross_links.py` (including reciprocal `THINKING_LENS_SKILL_CONSUMERS`).
11. When changing Module Contract subsections on workflow skills, keep `Escalation:` present and run `test_skill_module_contract.py`.
12. When adding or editing `01-thinking/` lenses, keep `## Human Review` in the preamble (routes to `reflective-risk`) and run `test_thinking_prompts_eval_harness.py`.
13. When editing workflow skill Escalation bullets, cite only frozen `reflective-*` skills; run `test_skill_module_contract.py` escalation route guard.
14. When editing `01-thinking/` Purpose preambles, keep `Primary workflow surfaces` aligned exactly with `SKILL_THINKING_SOURCES` via `test_thinking_lens_primary_surfaces_match_consumer_graph`; put escalations and adjacent workflow notes in Scope or Human Review, not on the primary line.
15. When editing composable prompts (`02-engineering`–`06-repo`), keep `Primary workflow surface(s)` aligned with `*_SKILL_LINKS` in `test_prompt_cross_links.py`; use Supporting lens for cross-cutting lenses like `runtime-trust-boundary.md`; put escalate/pair notes in Scope.
16. When editing `00-core/` prompts, keep `Primary workflow surface(s)` aligned with `CORE_SKILL_LINKS` in `test_prompt_cross_links.py`; put pair/escalation skills in Scope or Human Review, not on the primary line.
17. When editing composable prompts (`00-core`–`06-repo`), keep `Primary workflow surface(s)` / Supporting-lens preamble lines and run `test_*_prompts_eval_harness.py` primary-surface guards.
18. When adding or editing composable prompts (`02-engineering`–`06-repo`) with `## Human Review`, keep preamble escalation routed to `reflective-risk` and run Human Review guards in `test_*_prompts_eval_harness.py` (exact heading match via `prompt_eval_helpers.py`).
19. When editing Human Review guards, use `prompt_eval_helpers.assert_human_review_preamble` in all `test_*_prompts_eval_harness.py` files (thinking lenses + composable categories).
20. When adding or editing risk-bearing `00-core/` prompts with `## Human Review`, keep preamble escalation routed to `reflective-risk` and run `test_core_prompts_eval_harness.py` Human Review guards via `prompt_eval_helpers.py`.
21. When editing `00-core/` Human Review coverage, keep `CORE_HUMAN_REVIEW_REQUIRED` and `CORE_HUMAN_REVIEW_EXEMPT` in `test_core_prompts_eval_harness.py` aligned with preamble `## Human Review` sections; run core HR parity tests.
22. When editing Human Review coverage on thinking lenses or composable prompts (`01-thinking`–`06-repo`), keep frozen `*_HUMAN_REVIEW_REQUIRED` / `*_HUMAN_REVIEW_EXEMPT` sets in `test_*_prompts_eval_harness.py` aligned with preamble `## Human Review` sections; use `prompt_eval_helpers.assert_human_review_*` parity helpers and run HR set partition tests.
23. When adding composable prompts or new categories, keep `PROMPT_LIBRARY_CATEGORIES` and `test_human_review_library_registry.py` aligned so frozen HR sets cover every `00-core`–`06-repo` prompt exactly once.
