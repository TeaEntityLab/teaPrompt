# DevOps and Agentic AI Architecture Trends Survey — August–September 2026 Shift (2026-09-28)

> **Status: decided — one sentence adopted; the other six candidates stay no-change.** The object is a comprehensive industry survey paste (`local://paste-1.md`, accessed 2026-09-28) detailing the late August to late September 2026 DevOps paradigm shift from raw coding-agent generation velocity to verification bottlenecks, runtime trust, and agent governance. All 14 primary references across 6 core themes and 1 background economic study were verified on 2026-09-28. A later user instruction, "Verify and think about updating skills if worthy," re-read the sentences an agent actually follows. Six candidates were already written there, or sit on the host side of Principle P7. One was not: invariant #11 was a bare name on `agent-governance-scaffold`, while "scope is the intersection, prohibitions the union, you cannot delegate a capability you do not hold" lived only in `plans/agent-governance-four-power-concepts-2026-07-17.md`. That sentence now sits on the capability-token block. Guard: `plans/tests/test_devops_agentic_trends_survey_record.py`.

## Research Question

User instruction: "Survey: local://paste-1.md". The pasted text outlines a major paradigm shift in DevOps and AI Coding Agents between late August and late September 2026: moving from "Vibe Coding" generation velocity to solving "Verification Bottlenecks" (absorbing velocity) and establishing "Runtime Trust".

Questions:
1. Does the paste accurately reflect verified industry publications, engineering leadership analyses, and technical releases from late August to late September 2026?
2. Does any identified concept expose a genuine architectural gap or missing invariant on TeaPrompt's installed skills, governance docs, or prompts?
3. What is the disposition of each candidate under TeaPrompt's core principles (especially P7: no owned runtime; and the requirement for observable runtime evidence)?

## Direct Recommendation (as of 2026-09-28)

- **Adopt one sentence, on the capability-token block of `agent-governance-scaffold`.** Invariant #11 was already the canonical name. The acting constraint — a delegate's allowed scope is the intersection, its prohibitions the union, and it cannot receive a capability the delegator does not hold — was only in the 2026-07-17 concepts plan. The token template is where an agent emits `delegated_to`.
- **Leave the other six candidates unchanged.**
  - Verification absorption, outer-loop verdicts, and "self-report is not a pass" are already on `reflective-implement`, `reflective-review`, and `governed-delivery`.
  - Credential handling is already a Never on `reflective-risk` (do not place a credential in a command line, transcript, or source file) plus a host precondition (`credential brokering`) on `governed-delivery`. Reading a secret into model context is already "placing it in a transcript."
  - MicroVM isolation, binary scanning, and System-One logit runtimes stay on the host side of Principle P7.

## Method

1. **Source verification (2026-09-28):** All 14 cited publications and references across 6 core technical themes and 1 macro-economic background report were verified against primary sources via web search and documentation checks.
2. **Surface mapping (2026-09-28):** Each concept was mapped against TeaPrompt's installed surfaces:
   - `reflective-prompt-library/04-agent/runtime-trust-boundary.md`
   - `reflective-prompt-library/06-repo/AGENTS.md`
   - `reflective-prompt-library/PROJECT_KNOWLEDGE.md`
   - `reflective-prompt-library/skills/agent-governance-scaffold/SKILL.md`
   - `reflective-prompt-library/skills/governed-delivery/SKILL.md`
   - `reflective-prompt-library/skills/flow-loop-harness/SKILL.md`
   - Prior decision-model surveys (`decision-model-survey-2026-09-18.md`, `jev-architecture-synthesis-survey-2026-09-19.md`, `pi-warden-survey-2026-09-20.md`)
3. **Dispositions assigned:** Under standing rules, every candidate was evaluated against local failure evidence and runtime boundaries.

## Source Identity and Claim Verification

| Topic / Item | Cited Work & Authors | Venue & Date | URL (checked 2026-09-28) | Claim Verification Status |
| --- | --- | --- | --- | --- |
| **Background** | *Why Isn't AI Adoption Showing Up in Your P&L?* (Leah Brown on Rodo Abad, Jason Cox, Jeff Gallimore et al.) | IT Revolution / Enterprise Technology Leadership Journal (2026) | [IT Revolution Article](https://itrevolution.com/articles/why-isnt-ai-adoption-showing-up-in-your-pl/) (checked 2026-09-28) | **Verified.** Reports ~441% review-time rise and ~243% incidents-per-PR rise for **one bank team**, separately citing the Faros AI 22,000-developer/4,000-team study population. Bottleneck shifted from generation to absorption. (Corrected 2026-10-02: the population metrics belong to the primary Faros report — see *Evidence vs Inference*; earlier wording attributed population-level claims to this article.) |
| **Theme 1.1** | *Docker Cloud Sandboxes Provide a Consistent Sandbox Abstraction Across Laptop and Cloud* (Sergio De Simone) | InfoQ (2026-09-27) | [InfoQ Article](https://www.infoq.com/news/2026/09/docker-cloud-sandboxes/) (checked 2026-09-28) | **Verified.** Hardware-level microVM sandboxes replacing standard containers for AI agents; seamless laptop-to-cloud handoff (`sbx --cloud`). |
| **Theme 1.2** | *Smoothing the Never-Ending Road to Modernization* (Anne Plese reporting on Mark Cavage) | DevOps.com (2026) | [DevOps.com Article](https://devops.com/smoothing-the-never-ending-road-to-modernization/) (checked 2026-09-28) | **Verified.** Discusses Docker Sandboxes, Kits specification, and why traditional containers cannot safely constrain autonomous agents. |
| **Theme 1.3** | *6 Benefits of Sandbox Environments* (Kevin Wittek / Tom Smith) | Docker Blog / DevOps.com (2026) | [Docker Blog Post](https://www.docker.com/blog/benefits-of-sandbox-environments/) (checked 2026-09-28) | **Verified.** Details 6 sandbox benefits: hardware boundary, runtime network/filesystem restrictions, disposable environments, credential isolation. |
| **Theme 2.1** | *The Agent Never Sees the Key / MCP Gateway for AI Agents* (Anish Singh Walia) | DigitalOcean Community Tutorials (2026-09) | [DigitalOcean Tutorial](https://www.digitalocean.com/community/tutorials/credential-brokering-action-gateway) (checked 2026-09-28) | **Verified.** DigitalOcean Action Gateway & Harness Runtime credential brokering: tokens never enter model context or logs; dynamically injected at gateway. |
| **Theme 2.2** | *Below the Harness: Governing a Multi-Model, Multi-Harness World* (Srini Sekaran / Tushar Jain) | Docker Blog (2026) | [Docker Blog Article](https://www.docker.com/blog/below-the-harness-governing-a-multi-model-multi-harness-world/) (checked 2026-09-28) | **Verified.** Confused Deputy problem in AI agents; security rules and permission isolation must move below the harness into runtime. |
| **Theme 3.1** | *AI agents that pass authentication can still drift, expose data, or get memory-poisoned* (Nik Kale) | VentureBeat (2026-08) | [VentureBeat Article](https://venturebeat.com/security/ai-agents-that-pass-authentication-can-still-drift-expose-data-or-get-memory-poisoned) (checked 2026-09-28) | **Verified.** Proposes Monotonic Delegation (privilege can only stay equal or decrease) and 6-stage dependency gates for AI agent deployment. |
| **Theme 3.2** | *AI agents need their own identity before they need a gateway* (Ravindra Annam) | VentureBeat (2026) | [VentureBeat Post](https://venturebeat.com/security/ai-agents-need-their-own-identity-before-they-need-a-gateway) (checked 2026-09-28) | **Verified.** "Authentication establishes identity, not trust." Introduces Runtime Trust framework (intent verification, behavior monitoring, kill switch). |
| **Theme 3.3** | *Identity and permissions aren't enough to govern AI agent behavior* (Heather Ceylan / Box CISO) | VentureBeat (2026) | [VentureBeat Interview](https://venturebeat.com/security/identity-and-permissions-arent-enough-to-govern-ai-agent-behavior) (checked 2026-09-28) | **Verified.** Shift from static access permission management to runtime execution supervision with 3-tier risk-based approval. |
| **Theme 4.1** | *The AI-Native SDLC Playbook* (Louis Claxton) | Anthropic / Claude Academy / DevOps.com / The New Stack (2026-08/09) | [Claude Academy Course](https://academy.claude.com/courses/ai-native-sdlc-playbook) (checked 2026-09-28) | **Verified.** Artifact-driven continuous loop: `intent.md → spec.md → plan.md → code/tests → evidence → incident`. Demands objective runtime evidence over blind test pass claims. |
| **Theme 4.2** | *Own the Outer Loop* (Addy Osmani) | Addy Osmani Blog / Substack / AI Engineer World's Fair (2026) | [Addy Osmani Post](https://daily.dev/posts/own-the-outer-loop-jdc7i9zwl) (checked 2026-09-28) | **Verified.** Inner Loop (agent coding, testing, self-repair) vs Outer Loop (human engineer owning Quality, Verdict, Answerability). Tackling cognitive debt. |
| **Theme 5.1** | *Make the agent and its authority reproducible (Docker Sandbox Kits)* (Mark Cavage) | DevOps.com (2026) | [DevOps.com Kit Report](https://devops.com/smoothing-the-never-ending-road-to-modernization/) (checked 2026-09-28) | **Verified.** Packaging agent tools and guardrails into standard OCI images for reproducible execution and CNCF open governance. |
| **Theme 5.2** | *BigID Debuts AgentIQ for Agent-Run Data Security and Compliance* (Miles Okada) | Unite.AI (2026-09-21) | [Unite.AI Article](https://www.unite.ai/zh-cn/bigid-debuts-agentiq-for-agent-run-data-security-and-compliance/) (checked 2026-09-28) | **Verified.** Security and compliance governance for agent data access, credential boundary scanning, and runtime posture remediation. |
| **Theme 5.3** | *UN AI Panel Invokes Precautionary Principle on Loss-of-Control Risk* | Unite.AI (2026-09-21) | [Unite.AI Report](https://www.unite.ai/un-ai-panel-invokes-precautionary-principle-on-loss-of-control-risk/) (checked 2026-09-28) | **Verified.** Policy briefing on loss-of-control risks from autonomous agents, citing supply-chain and alignment failures; calls for precautionary isolation. |
| **Theme 6.1** | *20 Agentic Use Cases of TypeSafe AI's Jev* | MarkTechPost (2026-09-27) | [MarkTechPost Article](https://www.marktechpost.com/2026/09/27/20-agentic-use-cases-of-typesafe-ais-jev/) (checked 2026-09-28) | **Verified.** System-One fast decision model (Jev 1.13.0) for tool gating, triage, and routing in <100ms without natural-language text generation. |
| **Theme 6.2** | *TypeSafe AI Releases Jev: A System One Model That Returns Typed Decisions* | MarkTechPost (2026-09-19) | [MarkTechPost Release](https://www.marktechpost.com/2026/09/19/typesafe-ai-releases-jev/) (checked 2026-09-28) | **Verified.** Architecture details: typed candidate scoring, calibrated probabilities, eliminates hallucinations via schema-bound logits. |
| **Theme 6.3** | *A Coding Guide to TypeSafe AI Jev* | MarkTechPost (2026-09-23) | [MarkTechPost Guide](https://www.marktechpost.com/2026/09/23/a-coding-guide-to-typesafe-ai-jev/) (checked 2026-09-28) | **Verified.** Implementation guide for speculative fan-out, action gating, and fast pipeline triage. |

## Concept Map

| ID | Concept | Source Tier | TeaPrompt Surface & Coverage | Disposition |
| --- | --- | --- | --- | --- |
| C1 | **Absorbing Velocity & The Verification Bottleneck:** AI accelerates code generation, but reported review time surges ~441% (median PR-review time) and incidents per PR spike ~243%; organizational capacity is bound by safe absorption speed. | Industry Study (Faros AI / IT Revolution) | `reflective-review`, `reflective-minimality`, `reflective-implement` Verification ("Tests alone are not proof; UI verify actual surface; Bug reproduce before/confirm after"), `06-repo/AGENTS.md`. | **Covered.** TeaPrompt was conceived specifically to address review collapse and cognitive debt through structured verification. No change. |
| C2 | **MicroVM & Cloud Sandboxes:** Hardware-level microVM isolation (Firecracker, Docker Cloud Sandboxes) replacing prompt guardrails and weak container boundaries; seamless local-to-cloud handoff. | Runtime / Infra (Docker, DigitalOcean) | `reflective-prompt-library/04-agent/runtime-trust-boundary.md` ("Runtime guarantees separated from prompt or skill claims: host runtime must enforce them"); `reflective-risk`. | **Host Boundary (P7).** Methodology specifies isolation boundaries; physical microVMs belong to host runtimes. No change. |
| C3 | **Action Gateways & Credential Brokering:** Tokens never reach the agent's context or logs; raw credentials dynamically attached at the gateway; mitigates Confused Deputy attacks. | Tool / Gateway (DigitalOcean, Arcade.dev, Docker) | `runtime-trust-boundary.md` §2a ("Product/Runtime Ownership Boundary: Host product owns authentication and tenant scope; secrets never in prompt context"); `reflective-risk`. | **Covered / Host Boundary.** Perfectly matches TeaPrompt's secret-isolation rules. Gateways enforce at host tier. No change. |
| C4 | **Non-Human Identity & Monotonic Delegation:** Explicit machine identities (Entra Agent ID); authority delegation strictly monotonic (≤ delegator privilege; never privilege escalation); 6-stage dependency gates. | Identity & Governance (VentureBeat, Nik Kale, Ravindra Annam) | `skills/agent-governance-scaffold/SKILL.md` names invariant #11 and emits `delegated_to`. The operational rule was only in `plans/agent-governance-four-power-concepts-2026-07-17.md` §Composition. | **Adopted.** One sentence on the capability-token block. The six-stage gate list and vendor identity products stay out. |
| C5 | **AI-Native SDLC & Outer Loop Governance:** Inner loop (agent: explore, code, self-test) vs. Outer loop (human engineer: Intent, Architecture Constraints, Quality, Verdict, Answerability); artifact-driven pipeline (`intent → spec → plan → code/evidence → incident`). | SDLC Architecture (Anthropic Louis Claxton, Addy Osmani) | TeaPrompt core workflow: `reflective-brief` (Intent) → `reflective-spec-plan` (Spec/Plan) → `reflective-implement` (Inner Loop Code) → `reflective-review` / `governed-delivery` (Outer Loop Evidence/Verdict) → `reflective-handoff-retro` (Retro/Incident). | **Covered.** Complete 1:1 structural convergence. TeaPrompt is an operational implementation of the outer-loop artifact pipeline. No change. |
| C6 | **Supply Chain Security Left-Shift to Binaries & MCP Catalog Admission:** Hardened base images, automated binary scanning/APM, and pre-execution admission vetting of MCP servers and Skill catalogs. | Security / Packaging (Docker Sandbox Kits, BigID, CNCF) | `04-agent/artifact-promotion.md` (strict promotion gates from discussion/memory into skills); `plans/lint_skills.py` & `validate_governance.py`. Binary scanning is host-side. | **Covered / Host Boundary.** Skill catalog admission is guarded locally; binary infrastructure scanning is host-side. No change. |
| C7 | **System-One Fast Decision Models in Pipelines:** Sub-100ms typed classification models (e.g. Jev 1.13.0) for gating, CI triage, and routing without text generation. | Model / Serving (TypeSafe AI, DigitalOcean Serverless) | Prior surveys: `plans/decision-model-survey-2026-09-18.md` (DM-1..DM-9), `plans/jev-architecture-synthesis-survey-2026-09-19.md`, `plans/pi-warden-survey-2026-09-20.md`. Prompt-level typed verdicts installed. | **Covered.** Prompt-level contracts installed; logit-scoring engine is host runtime. No change. |

## Candidate Adoption Ledger

| ID | Candidate | Status | Evidence | Reopen Trigger |
| --- | --- | --- | --- | --- |
| DT-1 | Preserving review capacity & cognitive debt guardrails (Velocity Absorption) | No change (Covered) 2026-09-28 | `reflective-minimality`, `reflective-implement` Verification, `reflective-review`. | A TeaPrompt workflow that generates high PR volume without required verification evidence. |
| DT-2 | MicroVM sandbox runtime requirement in prompts | No change (Host Boundary) 2026-09-28 | `runtime-trust-boundary.md` line 21: "TeaPrompt can specify required gates, but a host runtime or accepted module must enforce and test them." Principle P7 forbids owning runtimes. | If TeaPrompt ever bundles a native execution harness or container runner. |
| DT-3 | Credential brokering protocol (Action Gateways) | No change (Host Boundary) 2026-09-28 | `runtime-trust-boundary.md` §2a & §4: secrets stripped from prompt context, dynamic injection at execution time. | A TeaPrompt skill that accepts or stores raw third-party API tokens in prompt context. |
| DT-4 | Monotonic delegation invariant in agent governance | Adopted 2026-09-28 — one sentence | Re-read under "update skills if worthy": the skill listed `authority-monotone-down-the-chain` and a `delegated_to` field, but did not say scope is the intersection and prohibitions the union. That sentence is now under the capability-token template. Broker enforcement stays a host precondition. | A second seat stating the same rule, or a prompt that claims the broker check already ran. |
| DT-5 | Outer Loop governance & artifact chain (`intent → spec → plan → evidence`) | No change (Covered) 2026-09-28 | Core skill chain (`reflective-brief` → `spec-plan` → `implement` → `review` / `governed-delivery` → `handoff-retro`). Outer loop human verdict invariant is inviolable. | An automated workflow attempting to self-approve production releases without human outer-loop verdict. |
| DT-6 | Binary scanning & hardened image left-shift | No change (Host Boundary) 2026-09-28 | `artifact-promotion.md` governs skill promotion; binary scanning belongs to CI/CD infrastructure. | An artifact promotion workflow that accepts unverified executable binaries into the repository. |
| DT-7 | System-One fast decision model integration | No change (Covered) 2026-09-28 | Prior survey `decision-model-survey-2026-09-18.md` (DM-1..DM-9) and `pi-warden-survey-2026-09-20.md`. Typed verdict contracts installed. | A host runtime exposing raw logit margins to TeaPrompt skill steps. |

## Evidence vs Inference

| Claim | Status | Basis |
| --- | --- | --- |
| All 14 articles and reports exist with verified authors, dates, and venues | Observed | Primary web sources fetched and verified on 2026-09-28. |
| Faros AI reports a large review-time/incident surge for AI-assisted teams | Observed (primary report re-checked 2026-10-02) | The primary [Faros AI Engineering Report 2026](https://pages.faros.ai/hubfs/AI_Engineering_Report_2026_The_Acceleration_Whiplash_Faros.pdf) reports +441.5% **median** PR-review time, +242.7% incidents **per PR**, and +57.9% monthly incidents, from observational within-company/within-team comparisons (≥6 companies per metric, Spearman p<.05) — not causal inference or verified raw telemetry. The IT Revolution article (checked 2026-09-28) reports the rounded ~441%/~243% per-PR figures for **one bank team**; the original wording conflated the anecdote with the 22,000-developer study population. |
| Docker Cloud Sandboxes provide hardware-enforced microVM isolation across laptop and cloud | Observed | InfoQ reporting by Sergio De Simone (2026-09-27) and Docker blog announcements. |
| DigitalOcean Action Gateway dynamically brokers credentials without entering agent context | Observed | DigitalOcean Managed Agents documentation and Anish Singh Walia tutorial (2026-09). |
| Monotonic Delegation is proposed by Nik Kale as a 6-stage dependency gate | Observed | VentureBeat publication (2026-08). |
| Anthropic SDLC Playbook structures artifact flow as `intent → spec → plan → code/evidence → incident` | Observed | Anthropic Claude Academy course materials and analysis on DevOps.com (2026). |
| Addy Osmani keynote defines Outer Loop as Quality, Verdict, and Answerability | Observed | Addy Osmani blog and AI Engineer World's Fair address. |
| TeaPrompt already implements the conceptual requirements of the Outer Loop and Runtime Trust | `[INFERENCE]` | Based on direct 1:1 structural comparison between published frameworks and installed TeaPrompt skills/contracts. |
| Invariant #11's acting constraint was missing from the skill | Observed | Before this pass the skill listed the name and a `delegated_to` field; the intersection/union rule was only in `plans/agent-governance-four-power-concepts-2026-07-17.md`. The sentence is now on the capability-token block. |

## Evidence Actually Checked

- `local://paste-1.md` read in full on 2026-09-28.
- Primary source checks via web search (2026-09-28):
  - IT Revolution: *Why Isn't AI Adoption Showing Up in Your P&L?*
  - InfoQ: *Docker Cloud Sandboxes Provide a Consistent Sandbox Abstraction Across Laptop and Cloud*
  - Docker Blog: *Below the Harness: Governing a Multi-Model, Multi-Harness World* & *6 Benefits of Sandbox Environments*
  - DigitalOcean: *Action Gateway & Credential Brokering* documentation
  - VentureBeat: Articles by Nik Kale, Ravindra Annam, and Heather Ceylan
  - Anthropic Claude Academy: *The AI-Native SDLC Playbook*
  - Addy Osmani: *Own the Outer Loop*
  - MarkTechPost: Articles on TypeSafe AI Jev (2026-09-19, 2026-09-23, 2026-09-27)
- TeaPrompt installed files re-read and audited:
  - `reflective-prompt-library/04-agent/runtime-trust-boundary.md`
  - `reflective-prompt-library/skills/agent-governance-scaffold/SKILL.md`
  - `reflective-prompt-library/skills/governed-delivery/SKILL.md`
  - `reflective-prompt-library/06-repo/AGENTS.md`
  - `reflective-prompt-library/PROJECT_KNOWLEDGE.md`

## Falsifiability

1. **Falsifier for Source Verification:** The survey's source claims are falsified if any of the 14 cited works, authors, or key reported statistics (e.g. Faros AI 441% review increase) are proven to be fictitious or misattributed.
2. **Falsifier for Candidate Dispositions:** DT-4 is falsified if the capability-token block no longer states that a `delegated_to` grant takes the intersection of allowed scope and the union of prohibitions, or if that sentence claims the prompt itself enforces the broker check. The no-change rows (DT-1, DT-2, DT-3, DT-5, DT-6, DT-7) are falsified if the acting sentence cited for them is absent: credentials may be placed in a command line or transcript (`reflective-risk`), a gate may auto-release on self-report (`governed-delivery`), or a high-risk pass may rest on model judgment alone (`reflective-review`).
3. **Falsifier for Host Boundary Distinction:** The distinction between prompt methodology and host runtime (P7) is falsified if microVM isolation or dynamic secret injection can be deterministically guaranteed solely through prompt text instructions without underlying host runtime infrastructure.

## Shared Findings and Architectural Synthesis

1. **The Verification Bottleneck is the Defining Failure of Uncontrolled Agent Velocity:**
   The industry data reported by Faros AI (~441% rise in median PR-review time, ~243% rise in incidents per PR — observational within-company/team comparisons, not a causal finding) is consistent with what TeaPrompt has maintained from its inception: generating code is trivial; safely absorbing code into production systems is the real bottleneck. Teams that treat AI agents as unconstrained code producers simply convert syntactic debt into cognitive debt and operational instability.


2. **The "Inner Loop / Outer Loop" Consensus Validates TeaPrompt's Structure:**
   The convergent frameworks from Anthropic (Claxton) and Addy Osmani draw an unmistakable boundary:
   - **The Inner Loop (Machine Domain):** Fast, iterative investigation, drafting, and local regression testing.
   - **The Outer Loop (Human Engineering Domain):** Ground truth intent, architectural invariants, evidence evaluation, release verdicts, and legal/ethical answerability.
   TeaPrompt's core pipeline (`reflective-brief` → `reflective-spec-plan` → `reflective-implement` → `reflective-review` / `governed-delivery`) directly instantiates this model. The rule "Tests alone are not proof. Ground every claim in observable runtime evidence" is the exact mechanism preventing outer-loop collapse.

3. **Runtime Trust Must Replace Static Authentication:**
   Static credentials (API keys, service tokens) are fundamentally unsafe inside autonomous agent contexts. As demonstrated by DigitalOcean's Action Gateway and Docker's runtime governance, credentials must be brokered out-of-band by the execution platform. Prompt systems should manage intent, authority scopes, and task contracts, while execution gateways manage secrets and enforce monotonic delegation.

---

## Corrections (2026-10-02)

Post-review audit (`review/final-report.md`, finding Factory-4) corrected the Faros citation/denominator at :39, :61, :86 and :123. The IT Revolution article attributes its rounded ~441% review-time / ~243% incidents-per-PR figures to **one bank team**; the population metrics come from the primary [Faros AI Engineering Report 2026](https://pages.faros.ai/hubfs/AI_Engineering_Report_2026_The_Acceleration_Whiplash_Faros.pdf): +441.5% median PR-review time, +242.7% incidents per PR, +57.9% monthly incidents, under an observational within-company/within-team design (≥6 companies per metric, Spearman p<.05). The figures are corroborated — narrowed by citation and denominator, not alleged fabricated. Primary report checked 2026-10-02, separate from the historical 2026-09-28 checks. Settled DT-1..DT-7 dispositions and the adopted capability-token sentence are unchanged.
