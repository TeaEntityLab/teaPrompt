# Methodology-Only Posture Rethink — Parallel Lens Panel (2026-10-01)

> **Status: decided — AGREE WITH CHANGES 3/3; posture retained, boundary
> sharpened.** User asked whether TeaPrompt's deliberate non-goal on
> operationalization/runtime is still necessary. Panel answer: yes — it is
> load-bearing scope discipline, but it needed (a) an honest falsifier,
> (b) an authority rule for lifting non-goals, and (c) explicit codification
> that in-repo consumer-test execution is a developer-only CI fixture, not a
> shadow runtime.

## Packet

`review-packet-methodology-only-2026-10-01.md` (repo root, deleted after
synthesis per packet protocol). Two packet citation errors were found by the
evidence lens and are corrected in this record (see Required Wording
Changes).

## Panel composition

Five `task` lenses were fanned out first; the `task` backend returned hard
quota 429 for all five (retry-after ~38h). Refanned on the `scout` backend
with three merged lenses; all three delivered complete §-shape reviews.

| Lens | Verdict |
| --- | --- |
| Evidence + Governance (scout) | AGREE WITH CHANGES |
| Scope / Product (scout) | AGREE WITH CHANGES |
| Adversary / strongest-counterargument (scout) | AGREE WITH CHANGES |

No lens argued for owning a runtime; the adversary lens, tasked to steel-man
adoption, itself concluded TeaPrompt must not ship a runner.

## Shared Findings

1. **OmO 5.x strengthens, not weakens, the non-goal.** OmO built a real DAG
   scheduler/WAL/safety gates yet left its flagship `ultrawork` verification
   as prompt text — proof that owning a runtime does not convert methodology
   into enforced verification, and that runtime investment crowds out the
   methodology layer. (Evidence: `plans/oh-my-openagent-survey-2026-10-01.md`.)
2. **TeaPrompt already operates a "shadow runtime" in tests.**
   `plans/tests/test_flow_generator_consumers.py` and
   `test_flow_loop_consumers.py` extract SKILL.md templates and execute them
   under subprocess stubs — a developer-only verification oracle. The posture
   was dishonest only in not naming this; it is now codified as a bounded
   fixture class (see adopted changes).
3. **The adoption bar was operationally unfalsifiable.** External runtime
   tools were rejected as "host layer," prompt-level tools as "already
   covered," and a *reproduced local failure* could never occur because
   TeaPrompt runs no runtime and collects no telemetry — eight consecutive
   surveys landed record-only. A reachable falsifier is now written into the
   non-goal itself.
4. **A rethink prompt is not an owner sentence.** The user's question
   authorized evaluation only; lifting a Standing Non-Goal still requires an
   explicit human direction change plus a reproduced local defect (precedent:
   2026-09-03 governable-autonomy user instruction; 2026-09-19 GE-1 reverted
   triggered-consideration landing).
5. **User-facing thin lane rejected; author-side fixture bridge accepted.**
   A shipped `teaprompt-exec`-style runner was judged a loophole that drifts
   into the panel-rejected swarm/runtime; in-repo test helpers bounded to
   `plans/tests/` (offline, no egress, no user-facing interface) are the
   legitimate bridge and already exist.

## Disagreements / Residual Risks

- Unverified residual failure modes an owned runner *might* catch remain
  marked [INFERENCE]: signal/process-group isolation, real host-CLI protocol
  impedance (ANSI/stderr/permissions), cross-platform POSIX portability
  beyond macOS bash 3.2, mid-stream crash state corruption. These are now
  reachable by the new falsifier clause if they manifest as reproduced
  defects.
- ScopeLens flagged that no in-repo test currently exercises
  signal/process-group cleanup (`os.killpg`); a `plans/tests/`-only helper
  may be added when a reproduced defect justifies it — not preemptively.

## Required Wording Changes (applied)

1. `PROJECT_KNOWLEDGE.md` Standing Non-Goals bullet 1 — extended with: the
   owner-sentence condition, the in-repo test-harness boundary, and the
   falsifier (≥3 documented real-world host executions failing on
   script-structure defects unreproducible by stub tests).
2. `PROJECT_KNOWLEDGE.md` adoption lesson — appended the authority rule
   (inquiry ≠ revision; external recurrence ≠ local promotion evidence).
3. `06-repo/AGENTS.md` out-of-scope line — "multi-agent runtime or any
   distributed/user-facing runner (author-side extracted-template test
   harnesses stay developer-only CI fixtures)".
4. Packet corrections recorded: "host owns execution" was a packet
   misquote — the Module Contract pin is "the host owns durability"
   (`flow-loop-harness/SKILL.md:47`); the durable-WAL sentence lives at
   `04-agent/workflow-recipes.md:109`, not in the loop skill; and consumer
   tests do execute templates (the "verified = wording presence" claim holds
   for routing/governance pins only).

## Candidate Adoption Ledger

| ID | Candidate | Status | Evidence | Next action / trigger |
| --- | --- | --- | --- | --- |
| MR-1 | Keep methodology-only, reject shipped runtime/runner | Adopted 2026-10-01 | 3/3 lenses; OmO prompt-only-verification evidence | Falsifier in non-goal bullet; re-litigate on trigger |
| MR-2 | Codify consumer tests as bounded CI fixtures | Adopted 2026-10-01 | `*_consumers.py` subprocess harnesses; AdversaryLens + ScopeLens + EvidenceLens | Guard test pins boundary wording; any promotion attempt to skills/ or packages requires owner sentence |
| MR-3 | Falsifier clause in Standing Non-Goals | Adopted 2026-10-01 | Unfalsifiability finding | If falsifier fires: ≥3 documented real-host failures on script-structure defects not reproducible by stubs |
| MR-4 | Authority rule for lifting non-goals | Adopted 2026-10-01 | Governance precedents (2026-09-03 owner sentence; GE-1 revert) | Applies to all future rethink prompts |
| MR-5 | `plans/tests/` signal/process-group cleanup helper | Deferred | ScopeLens [INFERENCE] gap; no reproduced defect yet | Promote only when a reproduced defect in template execution needs it |
| MR-6 | User-facing reference runner (`teaprompt-exec`) | Rejected 2026-10-01 | Adversary + Scope verdicts; OmO scope-creep lesson; 2026-06-25 swarm rejection stands | Re-litigate only if MR-3 falsifier fires AND owner sentence changes direction |

## Guard

`plans/tests/test_methodology_only_panel_record.py` pins this record's
headings, the amended non-goal/authority-rule wording, and the ledger IDs.

## Evidence Actually Checked

- Coordinator: packet written; authority lines read verbatim
  (`PROJECT_KNOWLEDGE.md` 52-54/83-89, `06-repo/AGENTS.md` 9-10);
  settled-pin files re-read post-repair; lens reports synthesized.
- EvidenceLens independently verified every load-bearing quote at HEAD and
  confirmed consumer tests subprocess-execute extracted templates.
- No runtime built, installed, or invoked; no external repo touched.

## Falsifiability

This record is wrong if: the amended non-goal wording is absent or diluted;
a runtime/runner ships without an owner sentence + reproduced defect; the
MR-3 falsifier fires and no re-litigation is opened; or a consumer-test
harness is promoted into `skills/` or a distributed package without recorded
owner authorization.
