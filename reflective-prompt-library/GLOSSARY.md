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

## Governance Maintenance Playbook / 治理維護手冊

Ongoing upkeep after panel close (Rounds 1–20). Not agent instructions — operator checklist.

**Operational test:** Before router tuning, add fresh ROUTE-002/003 holdout phrases; run `make validate`; record decisions in `PROJECT_KNOWLEDGE.md` Decision Index when governance surface changes.

1. Run `make all` on every governance/routing change.
2. Add holdout cases **before** tuning `route_paraphrase_eval.py` keyword rules.
3. Watch non-blocking undocumented-decision warnings from `validate_project_knowledge.py`.
4. Keep manual `benchmark_tasks.py` runs optional — fixture gate only in CI.
5. Reject tenth skill / full `SKILL.md` i18n unless promotion gate met (panel A, Q, W, AJ).

