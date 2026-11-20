# Agent Infrastructure JD Survey — Fidelity and Contract Map (2026-11-20)

Language: English

**Status: source-qualified reference record (`AID-DOC1`); no Skill, prompt-body, operating-rule, or runtime change.** The owner supplied a structured zh-TW analysis of a real job description — Xiaohongshu RAI Studio "AI Agent Infra Engineer" (REDstar 2027 campus track, Beijing/Shanghai/Hangzhou) — plus a personal assessment that agent-side design space (harness evolution, long-horizon runtime) is less settled than training infra. This record classifies every claim against the live JD and TeaPrompt's surfaces. No installs, model calls, Skill changes, commits, or pushes are authorized.

## Research Question

Is the JD analysis's six-module decomposition accurate and does it expose any missing TeaPrompt surface?

## Direct Recommendation

**Adopt the record only.** The six-module split (Harness Kernel, Managed Runtime, Context & Memory, Tool & Sandbox, Control Plane, Eval & Evolution) is a faithful decomposition of the JD and consistent with published agent-runtime guidance (Alibaba Cloud Agent Infra, AgentScope 2.0, Agent Harness deep-dives). Every module already maps to a TeaPrompt surface; the JD is a requirements inventory, not a novel mechanism. The personal assessment — agent infra design space > training infra design space — is defensible and consistent with industry trend reporting, but is opinion, not a contract.

## Evidence Used

| Source | Class | What it supplies |
| --- | --- | --- |
| Owner-supplied zh-TW JD analysis | **Primary** — structured decomposition | Verbatim basis for every classification |
| [job.xiaohongshu.com/campus/position/21899](https://job.xiaohongshu.com/campus/position/21899) | **Primary** — live JD | Confirms RAI Studio / REDstar / "AI Agent Infra 工程师" exists; location and track match |
| [offerseek.ai/jobs/167781](https://offerseek.ai/jobs/167781) | Secondary mirror | Same JD text, reposted |
| Agent Infra guidance (Alibaba Cloud, AgentScope 2.0, Agent Harness deep-dive, InfoQ AICon) | Secondary | Confirms the six-module decomposition matches published taxonomies |
| TeaPrompt surface grep (`skills/`, `00-core`–`06-repo`) | Repository evidence | Confirms every module maps below |

## Fidelity Ledger

| # | JD-analysis claim | Check | Verdict |
| --- | --- | --- | --- |
| 1 | Six modules: Harness Kernel, Managed Runtime, Context & Memory, Tool & Sandbox, Control Plane, Eval & Evolution | Matches JD structure and published agent-infra taxonomies | **verified** |
| 2 | "Model + Harness + Context + Tool + Data + Execution Architecture" jointly determine performance | Consistent with compound-AI-systems framing | **verified** |
| 3 | Build → Evaluate → Gate → Release → Run → Observe → Evolve lifecycle | Standard release/eval loop | **verified** |
| 4 | Cloud-native / distributed-systems concepts ported to agent runtime (state machine, idempotency, control/data plane split, observability) | Consistent with AgentScope, Temporal, E2B practice | **verified** |
| 5 | MCP + Skill standardization as first-class citizens | Confirmed trend | **verified** |
| 6 | Context engineering replacing prompt engineering | Confirmed trend | **verified** |
| 7 | Practice paths (micro-kernel with kill-resume + idempotency keys; gVisor/Firecracker sandbox; OpenTelemetry trajectories; LangGraph/Temporal/E2B references) | Reasonable and standard | **verified** |
| 8 | Personal claim: "agent harness/runtime design space is larger than training infra design space" | Consistent with industry reporting; defensible but opinion | **verified as opinion** |

## TeaPrompt Contract Map

| JD module | Existing surface | Disposition |
| --- | --- | --- |
| Harness Kernel (loop, decoupled, ReAct/planner/multi-agent, HITL, telemetry) | `flow-loop-harness` + `flow-control-generator` + `agents-sdk` | Already present |
| Managed Runtime (Session/Event/Turn state, checkpoint/resume, idempotency) | `durable-objects` + `checkpoint` + `runtime-trust-boundary` | Already present |
| Context & Memory (context engineering, layered memory, grounding, RAG) | `reflective-research` + `03-context/context-handoff` + `memory-consolidation` | Already present |
| Tool & Sandbox (MCP, skill registry, identity, delegated auth, isolation) | `workers-best-practices` + `runtime-trust-boundary` + `agent-governance-scaffold` | Already present |
| Control Plane (artifact model, lifecycle protocol, BYO agent, cost) | `flow-control-generator` DAG + `runtime-trust-boundary` + `verification-map-generator` | Already present |
| Eval & Evolution (deterministic eval, regression, gate, bad-case flywheel) | `golden-benchmark` + `verification-map-generator` + incident→rule admission | Already present |
| "Kill-resume + idempotency key" practice | `checkpoint` + `durable-objects` + `flow-loop-harness` | Already present |
| OpenTelemetry trajectory eval | `golden-benchmark` + `runtime-trust-boundary` observability | Already present |

## Candidate Adoption Ledger

| ID | Candidate | Decision | Reopen condition |
| --- | --- | --- | --- |
| AID-DOC1 | This dated record + catalogue navigation | **Adopted — reference documentation only** | A corrected JD, a retraction, or a local consumer failure |
| AID-DOC2 | Optional worked reference: the six-module decomposition as an architecture checklist inside `verification-map-generator` or `governed-delivery` | **Deferred — second recurrence not met** | A second independent JD/source or a local need for the checklist |
| AID-SK1 | Skill/prompt-body change encoding JD modules | **No change** | A demonstrated gap in a named existing surface |
| AID-RUN1 | Applying to the JD or reproducing its architecture | **Not adopted** | Separate decision; not authorized by this record |
| AID-RULE1 | "Agent infra design space > training infra" as an operating rule | **Rejected** | A defensible trend claim is not an invariant |

## Evidence vs Inference

- **Verified:** JD existence and location; six-module decomposition matches the live posting and published taxonomies; every contract mapping.
- **Verified as opinion:** the "agent infra design space > training" assessment; the personal commentary.
- **Inference (mine):** contract-map dispositions; the "no local gap" verdict; AID-DOC2 deferral.
- **Unknown:** the JD's actual internal architecture vs its public text; whether the modules are one team's framing or company-standard; hiring specifics beyond the posting.

## Risks, Falsifiability, and Handoff

- The six-module split is a hiring-document decomposition, not a measured architecture; it should not be adopted as a canonical spec.
- The JD's named technologies (LangGraph, Temporal, E2B, MCP) are references, not required stack; treat them as illustrative.
- The "agent infra > training infra" framing is defensible trend analysis but is opinion; no contract should depend on it.
- Delivered scope: this record, the external-adoption catalogue, and regenerated `index.json`. No prompt-body, Skill, routing, governance, or runtime changes.
