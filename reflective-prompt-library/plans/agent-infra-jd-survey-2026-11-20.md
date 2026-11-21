# Agent Infrastructure JD Survey — Fidelity and Contract Map (2026-11-20)

Language: English

> **Status:** source-qualified reference record (`AID-DOC1`); no Skill, prompt-body, operating-rule, or runtime change. The owner supplied a structured zh-TW analysis of a real job description — Xiaohongshu RAI Studio "AI Agent Infra Engineer" (REDstar 2027 campus track, Beijing/Shanghai/Hangzhou) — plus a personal assessment that agent-side design space (harness evolution, long-horizon runtime) is less settled than training infra. Verified here: one employer posting exists at the cited URL with the cited title, track, and locations. The six module names are the owner's plausible interpretation, checked against published taxonomies as industry analogy — not six employer-stated modules and not a verified internal architecture. No installs, model calls, Skill changes, commits, or pushes are authorized.

## Research Question

Which parts of the owner's six-module analysis are the employer's own posting, which are interpretation or industry analogy, and does any part expose a missing TeaPrompt surface?

## Direct Recommendation

**Adopt the record only.** Verified: one employer posting at the cited URL (title, track, locations). The six-module split (Harness Kernel, Managed Runtime, Context & Memory, Tool & Sandbox, Control Plane, Eval & Evolution) is the owner's plausible reading, compatible with published agent-runtime guidance (Alibaba Cloud Agent Infra, AgentScope 2.0, Agent Harness deep-dives) — industry analogy, not employer text. Each module's contract-level requirements map to a named repo-owned clause below; durable execution itself (checkpoint/resume, sandboxing, telemetry collection) is host-executed, and this record supplies no execution proof. The JD is a requirements inventory, not a novel mechanism. The personal assessment — agent infra design space > training infra design space — is defensible and consistent with industry trend reporting, but is opinion, not a contract.

## Evidence Used

| Source | Class | What it supplies |
| --- | --- | --- |
| Owner-supplied zh-TW JD analysis | **Record basis** — structured decomposition | Establishes the owner's module names and readings, not the employer's architecture |
| [job.xiaohongshu.com/campus/position/21899](https://job.xiaohongshu.com/campus/position/21899) | **Primary** — live JD | Confirms RAI Studio / REDstar / "AI Agent Infra 工程师" exists; location and track match |
| [offerseek.ai/jobs/167781](https://offerseek.ai/jobs/167781) | Secondary mirror | Same JD text, reposted |
| Agent Infra guidance (Alibaba Cloud, AgentScope 2.0, Agent Harness deep-dive, InfoQ AICon) | Secondary | Shows the owner's module names are compatible with published taxonomies (industry analogy, not employer confirmation) |
| TeaPrompt surface grep (`skills/`, `00-core`–`06-repo`) | Repository evidence | Locates the cited surfaces for the mappings below; dispositions remain inference |

## Fidelity Ledger — Posting Verbs vs Owner Interpretation vs Industry Analogy

**How to read the verdicts:** only the posting's existence, title, track, and locations are verified against the employer source. `owner reading` = the owner's interpretation of the posting. `analogy-compatible` = compatible with published taxonomies or standard practice — compatibility is not employer confirmation.

| # | Analysis claim (owner's) | Check | Verdict |
| --- | --- | --- | --- |
| 1 | Six modules: Harness Kernel, Managed Runtime, Context & Memory, Tool & Sandbox, Control Plane, Eval & Evolution | Posting exists; module names fit published taxonomy shapes | **owner reading; analogy-compatible** — not employer-stated modules, not a verified internal architecture |
| 2 | "Model + Harness + Context + Tool + Data + Execution Architecture" jointly determine performance | Compatible with compound-AI-systems framing | **owner synthesis; framing-compatible** — not an employer quote |
| 3 | Build → Evaluate → Gate → Release → Run → Observe → Evolve lifecycle | Standard release/eval loop | **owner synthesis; framing-compatible** — not an employer quote |
| 4 | Cloud-native / distributed-systems concepts ported to agent runtime (state machine, idempotency, control/data plane split, observability) | Compatible with AgentScope, Temporal, E2B practice | **owner synthesis; framing-compatible** — not an employer quote |
| 5 | MCP + Skill standardization as first-class citizens | A current industry trend | **owner reading; trend-compatible** — trend compatibility is not employer text |
| 6 | Context engineering replacing prompt engineering | A current industry trend | **owner reading; trend-compatible** — trend compatibility is not employer text |
| 7 | Practice paths (micro-kernel with kill-resume + idempotency keys; gVisor/Firecracker sandbox; OpenTelemetry trajectories; LangGraph/Temporal/E2B references) | Standard-compatible suggestions; stack names illustrative, not JD-required | **owner reading; practice-compatible** — reasonableness is not verification |
| 8 | Personal claim: "agent harness/runtime design space is larger than training infra design space" | Consistent with industry reporting; defensible but opinion | **owner opinion; trend-compatible** — not a contract |

## TeaPrompt Contract Map — Repo-Owned Clauses vs Host-Executed Behavior

TeaPrompt ships the written clauses below. The host supplies execution, durable state, isolation and telemetry. In particular, `agents-sdk`, `durable-objects`, `checkpoint` and `workers-best-practices` are not Skills in the repository's distribution.

| JD module (owner's reading) | Repo-owned clause + host-executed remainder | Disposition |
| --- | --- | --- |
| Harness Kernel (loop, decoupled, ReAct/planner/multi-agent, HITL, telemetry) | Repo: `flow-loop-harness` + `flow-control-generator` (loop/HITL/verifier generation contracts). Host: any `agents-sdk`-style execution bindings — no such skill is shipped | Contract present; execution host-owned |
| Managed Runtime (Session/Event/Turn state, checkpoint/resume, idempotency) | Repo: `04-agent/runtime-trust-boundary.md` §4a (record identity/authority/sink-contract/recovery/acceptance; dispatch without a receipt is `OUTCOME_UNKNOWN`). Host: session/checkpoint/resume execution and sink idempotency enforcement — no shipped `durable-objects` or `checkpoint` skill | Evidence contract present; durable execution host-owned, no execution proof in this record |
| Context & Memory (context engineering, layered memory, grounding, RAG) | [Context Handoff](../03-context/context-handoff.md) records what a successor needs; [Memory Consolidation](../04-agent/memory-consolidation.md) distinguishes reusable lessons from live task state | Guidance for keeping context, not a shipped store, retrieval index or RAG service |
| Tool & Sandbox (MCP, skill registry, identity, delegated auth, isolation) | Repo: `04-agent/runtime-trust-boundary.md` tool/action gates + `agent-governance-scaffold` (authority split, approval gates, receipt/acceptance contract templates). Host: MCP/sandbox isolation and delegated-auth enforcement — no shipped `workers-best-practices` surface | Gate contracts present; isolation/auth enforcement host-owned |
| Control Plane (artifact model, lifecycle protocol, BYO agent, cost) | Repo: `flow-control-generator` DAG + `04-agent/runtime-trust-boundary.md` + `verification-map-generator` (generation and evidence contracts) | Already present as generation/evidence contracts; lifecycle enforcement host-owned |
| Eval & Evolution (deterministic eval, regression, gate, bad-case flywheel) | Repo: `golden-benchmark-runner` + `verification-map-generator` + incident→rule admission gates | Already present |
| "Kill-resume + idempotency key" practice | Repo: `flow-loop-harness` (loop position/retry-rule generation; a resume ledger is a host-honored convention, never crash-safety) + `04-agent/runtime-trust-boundary.md` §4a (idempotency-key scope, recovery, acceptance evidence rules). Host: kill-resume execution and sink enforcement — no shipped `checkpoint`/`durable-objects` skill | Contract present; execution proof host-owned |
| OpenTelemetry trajectory eval | Repo: `golden-benchmark-runner` (eval methodology) + `04-agent/runtime-trust-boundary.md` (receipt/audit evidence rules). Host: trajectory/OTEL collection | Eval-and-receipt rules present; collection host-executed |

## Candidate Adoption Ledger

| ID | Candidate | Decision | Reopen condition |
| --- | --- | --- | --- |
| AID-DOC1 | This dated record + catalogue navigation | **Adopted — reference documentation only** | A corrected JD, a retraction, or a local consumer failure |
| AID-DOC2 | Optional worked reference: the owner's six-module reading as an architecture checklist inside `verification-map-generator` or `governed-delivery` (checklist only — the employer's internal architecture stays unverified) | **Deferred — second recurrence not met** | A second independent JD/source or a local need for the checklist |
| AID-SK1 | Skill/prompt-body change encoding JD modules | **No change** | A demonstrated gap in a named existing surface |
| AID-RUN1 | Applying to the JD or reproducing its architecture | **Not adopted** | Separate decision; not authorized by this record |
| AID-RULE1 | "Agent infra design space > training infra" as an operating rule | **Rejected** | A defensible trend claim is not an invariant |

## Evidence vs Inference

- **Verified:** one employer posting exists at the cited URL with the cited title, track, and locations (live JD + mirror). Module-name compatibility with published taxonomies holds as industry analogy only.
- **Owner-supplied, not employer-verified:** the six module names and readings; the practice-path suggestions; the "agent infra design space > training" assessment.
- **Inference (mine):** contract-map dispositions; the repo-vs-host split; the "no local gap" verdict; AID-DOC2 deferral.
- **Unknown:** the JD's actual internal architecture vs its public text; whether the modules are one team's framing or company-standard; hiring specifics beyond the posting.

## Falsifiability, Risks, and Handoff

- The six-module split is the owner's reading of a hiring document, not the employer's stated architecture and not a measured system; it must not be adopted as a canonical spec.
- The JD's named technologies (LangGraph, Temporal, E2B, MCP) are references, not required stack; treat them as illustrative.
- The "agent infra > training infra" framing is defensible trend analysis but is opinion; no contract should depend on it.
- Checkpoint/resume, sandbox isolation, delegated-auth enforcement, and trajectory collection execute on the host; this record supplies contract wording, not execution proof.
- Delivered scope: this record, the external-adoption catalogue, and regenerated `index.json`. No prompt-body, Skill, routing, governance, or runtime changes.
