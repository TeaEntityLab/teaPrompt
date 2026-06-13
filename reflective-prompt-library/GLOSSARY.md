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
