# Parallel Lens Review: SDLC & Software Factory Entry Points Rethink (2026-09-28)

> **Status: decided — two surfaces updated; new core skill and domain pack rejected; router keyword tuning deferred.** A 4-lens Parallel Lens Review (`MinimalityArchitectureLens`, `RoutingDiscoveryParityLens`, `WorkflowRecipeSynthesisLens`, `AdversarialSkepticLens`) evaluated whether TeaPrompt should introduce a dedicated "Software Factory" or "AI-Native SDLC" skill or entry point, following the survey of `agfnow/agentflow` v8.3.3 and late-2026 DevOps trends. All four lenses unanimously agreed with changes: a new standalone skill is 95% redundant with `governed-delivery` and violates the 9-core freeze and Principle P7; doing nothing leaves a real discovery gap; the optimal solution updates the existing `governed-delivery` bullet in place in both cheatsheets (preserving the 6-bullet invariant T2 and 105 parity tests) and adds the canonical 4-phase composition recipe to `04-agent/workflow-recipes.md`. Router keyword tuning for "factory" is deferred under ROUTING_CONTRACT R8 due to an existing collision with `reflective-minimality`. Guard: `plans/tests/test_software_factory_rethink_panel_record.py`.

## Research Question & Problem Context

User instructions:
1. *"Survey updated agfnow/agentflow v8.3.3"*
2. *"Then rethink about: Should we have a SDLC or Software Factory entry points or skills like it?"*
3. Advisory guidance to check cheatsheet parity tests (`test_cheatsheet_r11_parity.py`, `test_cheatsheet_route003_parity.py`), keep EN and zh-TW in strict lockstep, and preserve the "emits contracts, does not enforce" disclaimer.

Questions addressed by the panel:
1. **Minimality & Redundancy:** Would a new `software-factory` or `ai-native-sdlc` skill provide any procedural contract not already in `governed-delivery` or `reflective-spec-plan`?
2. **Routing & Discovery Risk:** How can "Software Factory" and "AI-Native SDLC" cues be surfaced in cheatsheets without breaking `ROUTE-002`, `ROUTE-003`, or R11 parity, and without colliding with `reflective-minimality`?
3. **Workflow Recipe Utility:** Does an explicit "Autonomous Software Factory" composition recipe in `04-agent/workflow-recipes.md` provide high-leverage architectural guidance without adding runtime bloat?
4. **Adversarial Reality:** What happens to a developer using Claude Code or Cursor asking for a "Software Factory" today, and what is the minimal zero-bloat solution?

---

## Panel Consensus

- **Decision:** **AGREE WITH CHANGES (4/4 Lenses Unanimous).**
  - Reject Option A (New Core Skill: breaks 9-core freeze).
  - Reject Option B (New Domain Pack: 95% redundant with `governed-delivery`).
  - Reject Option E (Status Quo / Do Nothing: leaves developer discovery broken).
  - **Adopt Option C (In-Place Cheatsheet Cues) + Option D (Architectural Composition Recipe).**
- **Use-Case Recommendation:**
  - `adopt`: Update `governed-delivery` bullet in place on `SKILL_TRIGGER_CHEATSHEET.md` and `.zh-TW.md`.
  - `adopt`: Add `## Autonomous Software Factory (AI-Native SDLC)` recipe to `04-agent/workflow-recipes.md`.
  - `study`: Agentflow v8.3.3 host session ID normalization (`CLAUDE_CODE_SESSION_ID`).
  - `defer`: Router keyword tuning for bare `"factory"` under ROUTING_CONTRACT R8.

---

## Required Wording Changes

1. **`reflective-prompt-library/skills/SKILL_TRIGGER_CHEATSHEET.md` (Domain packs section, line 245):**
   ```markdown
   - **Deliver end-to-end under governance (Software Factory / AI-native SDLC)** → `governed-delivery` — autonomous or unattended delivery run with a gate sequence, oracle manifest, task packet, failure-signature exits, decorrelated verification, evidence ledger, and named acceptance; emits a host-run delivery contract set, does not enforce it; side effects still gate through `reflective-risk`.
   ```
2. **`reflective-prompt-library/skills/SKILL_TRIGGER_CHEATSHEET.zh-TW.md` (Domain packs section, line 234):**
   ```markdown
   - **在治理之下端到端交付（軟體工廠／AI 原生 SDLC）** → `governed-delivery` — 自主或無人值守的交付執行，含閘門序列、oracle 清單、任務封包、失敗特徵退出、去相關驗證、證據帳本與具名驗收；產出 host 執行的交付契約組，本身不強制執行；副作用仍先走 `reflective-risk`。
   ```
3. **`reflective-prompt-library/04-agent/workflow-recipes.md` (lines 183–221):**
   - Added `## Autonomous Software Factory (AI-Native SDLC)` composition recipe.
   - Enforces the 4-phase outer/inner loop handshake (`brief` $\to$ `spec-plan` $\to$ `verification-map` $\to$ `governed-delivery` $\to$ `flow-loop-harness` $\to$ `review`).
   - Complies with clean-room boundaries by avoiding the forbidden token `'sealed oracle'` (`test_pstack_synthesis_survey_record.py`), using `unlocked oracle manifest` and `host write-protection`.

---

## Shared Findings

1. **The "Factory" Keyword Collision in Minimality:**
   `route_paraphrase_eval.py` (line 223) actively includes `"factory"` as a keyword for `reflective-minimality` to detect OOP overengineering smells. Because `reflective-minimality` has priority index 1 (ahead of `reflective-spec-plan` at index 4 and `reflective-implement` at index 5), adding bare `"factory"` to router keywords causes tie-break distortion and corrupts the R13 `review_led_inspection` boundary. Cues must remain scoped in domain-pack parentheticals.
2. **Cheatsheet Bullet Count Invariant (T2):**
   `test_dormant_conditional_contracts.py` asserts that `## Domain packs` in both cheatsheets contains strictly `len(PACK_NAMES) + 1` bullets (exactly 6 bullets). Adding a new standalone bullet immediately fails CI. Updating the `governed-delivery` bullet in place preserves the invariant.
3. **The Dead-Letter Documentation Trap:**
   Adding a recipe to `04-agent/workflow-recipes.md` without cheatsheet discovery cues creates a "dead-letter architecture" that headless agents never load. Conversely, cheatsheet cues without an architectural recipe leave agents without composition guidance. The two must be paired.
4. **Epistemic Division of Responsibility (Principle P7):**
   The prompt library defines contracts, gates, and evidence schemas; host infrastructure owns physical MicroVM execution, Action Gateway credential injection, and git branch locks. The disclaimer "emits contracts, does not enforce them" must be strictly maintained.
5. **Packet vs. Panel Record Lifecycle:**
   Under the `parallel-lens-review-packet` protocol (`workflow-recipes.md` line 158), the shared review packet (`plans/*-review-packet-*.md`) is a transient input document; this record's deletion of the packet after synthesis is the managed host manual/panel convention, not a requirement of the recipe. *(Correction 2026-10-02:* the canonical recipe requires only a reviewer-readable path — it neither mandates nor verifies deletion.) *The durable synthesis document containing the panel consensus, candidate ledger, and guard evidence is preserved as the panel record.*

---

## Disagreements / Residual Risks

1. **Multi-Skill Handoff Decay:**
   *Raised by MinimalityArchitectureLens and AdversarialSkepticLens:* Multi-turn pipelines in single-agent CLI harnesses can suffer context decay across stages.
   *Resolution:* The recipe mandates the **Artifact-Gated Handshake** (`intent-record`, `task-packet.yaml`, `oracle-manifest.yaml`, `evidence-ledger.yaml`). If context is lost, the agent reconstructs state from committed files, not conversational memory.
2. **Intent Machinery in Implementation:**
   *Advisory concern:* Should `reflective-implement` receive intent cues?
   *Resolution:* Firmly rejected. Line 48 of `reflective-implement` explicitly delegates unclear requirements upstream to `reflective-brief` or `reflective-spec-plan`. Zero hits for `intent` in `reflective-implement` is an intentional architectural separation of concerns.
3. **Router Keyword Tuning Deferral:**
   *Raised by RoutingDiscoveryParityLens:* Cues in cheatsheets do not alter the regex/keyword tables in `route_paraphrase_eval.py`. Adding "software factory" to router tables requires pre-registered holdout (`ROUTE-002`) and adversarial trap (`ROUTE-003`) fixtures under ROUTING_CONTRACT R8. Because cheatsheet in-place updates resolve developer discovery without keyword tuning, router keyword changes are intentionally deferred.

---

## Candidate Adoption Ledger

| ID | Candidate | Status | Evidence | Reopen Trigger |
| :--- | :--- | :--- | :--- | :--- |
| **SFR-1** | Cheatsheet `governed-delivery` in-place cue update (Software Factory / AI-native SDLC) | Adopted 2026-09-28 | `SKILL_TRIGGER_CHEATSHEET.md` line 245; `SKILL_TRIGGER_CHEATSHEET.zh-TW.md` line 234. Exactly 6 bullets preserved. | Parity test failure or user reports of delivery cue ambiguity. |
| **SFR-2** | Autonomous Software Factory composition recipe in `04-agent/workflow-recipes.md` | Adopted 2026-09-28 | `04-agent/workflow-recipes.md` lines 183–221. 4-phase outer/inner loop graph. Clean-room tokens verified. | A multi-skill delivery workflow failing to follow the 4-phase sequence. |
| **SFR-3** | Standalone 10th core skill or 6th domain pack (`software-factory` / `ai-native-sdlc`) | Rejected 2026-09-28 | 4/4 lens consensus: 95% redundant with `governed-delivery`; violates 9-core freeze and Principle P7. | An autonomous delivery failure that cannot be represented by existing core skills + domain packs. |
| **SFR-4** | Core router keyword tuning for "factory" in `route_paraphrase_eval.py` | Deferred 2026-09-28 | Collision with `reflective-minimality` (line 223); R8 requires holdout/adversarial fixtures before tuning. | A verified holdout failure where a user asks for a software factory plan and minimality misroutes it. |

---

## Evidence vs Inference

| Claim | Status | Basis |
| :--- | :--- | :--- |
| Agentflow 8.3.3 is a 1-commit host patch recognizing `CLAUDE_CODE_SESSION_ID` | Observed | Pinned commit `738d0b3` fetched and verified from GitHub API (2026-09-28). |
| `governed-delivery` already implements the 7-gate lifecycle and evidence ledger | Observed | `skills/governed-delivery/SKILL.md` audited line-by-line. |
| The word 'factory' is an active keyword in `reflective-minimality` | Observed | `plans/route_paraphrase_eval.py` line 223. |
| `test_dormant_conditional_contracts.py` asserts strictly 6 bullets in Domain packs | Observed | `test_dormant_conditional_contracts.py` T2 executed and verified. |
| Cheatsheets in EN and zh-TW pass 105 parity assertions with the in-place cue | Observed | `pytest plans/tests/test_cheatsheet*.py` passed 105/105. |
| The temporary review packet was deleted after synthesis | Observed | Packet removal executed by the managed host under its manual/panel convention. (Corrected 2026-10-02: `workflow-recipes.md` line 158 requires a packet path every reviewer can actually read; it does not instruct, verify, or authorize deletion, so deletion is not a recipe-checked fact.) |
| Users will successfully discover `governed-delivery` via the updated cheatsheet cues | `[INFERENCE]` | Based on developer keyword patterns matching cheatsheet parentheticals. |

---

## Evidence Actually Checked

- `agfnow/agentflow` commit `738d0b3f4aa1df870835813d9dcc015136628434` and `docs/CHANGELOG.md` fetched and audited.
- `SKILL_TRIGGER_CHEATSHEET.md` and `SKILL_TRIGGER_CHEATSHEET.zh-TW.md` audited line-by-line.
- Cheatsheet parity tests executed and passed:
  - `test_cheatsheet_r11_parity.py`
  - `test_cheatsheet_route003_parity.py`
  - `test_cheatsheet_boundary_parity.py`
  - `test_cheatsheet_dispatch_meta_parity.py`
  - `test_cheatsheet_boundary_quick_cues.py`
  - `test_dormant_conditional_contracts.py`
- Clean-room token checks: `test_pstack_synthesis_survey_record.py` and `test_prompt_cross_links.py`.
- Full repository test gate: 1,299 passed; `make validate` 0 errors.

---

## Falsifiability

1. **Falsifier for In-Place Cheatsheet Cues (SFR-1):** Falsified if `test_dormant_conditional_contracts.py` T2 fails due to bullet count mismatch, or if any of the 105 cheatsheet parity tests fail.
2. **Falsifier for Recipe Clean-Room Compliance (SFR-2):** Falsified if `04-agent/workflow-recipes.md` contains the banned token `'sealed oracle'` (triggering `test_pstack_synthesis_survey_record.py`) or if `test_prompt_cross_links.py` fails.
3. **Falsifier for Skill Rejection (SFR-3):** Falsified if an autonomous delivery workflow requires a contract artifact or gate that cannot be expressed within `governed-delivery`, `reflective-spec-plan`, and `verification-map-generator`.

---

## Corrections (2026-10-02)

Post-review audit (`review/final-report.md`, finding Factory-5) corrected two attributions while leaving the settled SFR-1/SFR-2 adoptions, the SFR-3 rejection, the SFR-4 deferral, and the panel's decision history unchanged:

1. **Packet lifecycle (:63):** the original wording implied the `parallel-lens-review-packet` recipe makes the packet ephemeral and deleted upon synthesis. The canonical recipe (`workflow-recipes.md` :158) requires only that the packet be at a path every reviewer can actually read; deleting it after synthesis is this host's manual/panel convention, not recipe authority.
2. **Evidence row (:100):** the claim "the temporary review packet is ephemeral and deleted after synthesis — Observed, contract stated in `workflow-recipes.md`" conflated a host cleanup action with a recipe contract. The deletion happened under the managed host's convention; it was not instructed or verified by the cited recipe text.
