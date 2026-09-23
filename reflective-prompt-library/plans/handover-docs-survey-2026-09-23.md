# Handover-Docs Methodology Survey — 2026-09-23

> **Status: decided — record-only; one durable lesson adopted into PROJECT_KNOWLEDGE.md, no skill or wording installed.** The object is `~/dev/handover-docs/` — a local, reusable **project handover documentation kit** (15 markdown files: README methodology, 9-volume handbook, ops SOPs, templates, glossary) written in Traditional Chinese. Its goal: a successor engineer with **no oral handover and no live support from the original team** can understand the system, operate it safely, and rebuild from zero using only repo docs. All content is templates and placeholders — no credentials, hosts, or real values exist in the kit; nothing sensitive was recorded. Guard: `plans/tests/test_handover_docs_survey_record.py`.

## Research Question

User instruction: "Learn from @~/dev/handover-docs/ and beware about sensitive keywords (avoid recording them). Learn key knowledge from them" — then "record non-sensitive into docs or skills if worth it". Questions: (1) what the kit teaches that generalizes; (2) whether any pattern exposes a gap on an installed TeaPrompt surface; (3) what is worth recording and where.

## Direct Recommendation (as of 2026-09-23)

- **Adopt — one durable lesson into PROJECT_KNOWLEDGE.md.** The kit's five design principles are documentation-engineering contracts that transfer directly to how TeaPrompt writes and reviews records: contract-layer vs implementation-layer separation, snapshot dating with live-truth pointers, decision provenance, pitfalls-as-guards, plain-text artifacts.
- **No new skill.** The kit is a *documentation structure*, not an executable workflow; TeaPrompt's `reflective-handoff-retro` already owns session-transfer, and the kit's task-card/agent-memory formats overlap with existing memory conventions. A skill would duplicate structure without a named local failure.
- **Candidate for later:** if TeaPrompt ever produces handover docs for a product repo, the kit's nine-volume handbook order (01 business → 02 architecture → 03 data → 04 pipelines → 05 ops → 09 tests → 06 decisions → 07 state → 08 rebuild) is the proven sequence.

## Method

Coordinator read all 15 files in full (2026-09-23): `README.md`, `glossary.md`, `handbook/01-09`, `ops/secrets-management.md`, `ops/offsite-backup.md`, `templates/{task-card,incident-entry,agent-memory}.md`. No scouts, no panel. Sensitive-keyword audit: every file is template/placeholder text; no real values present.

## Concept Map

| ID | Concept | TeaPrompt coverage | Disposition |
| --- | --- | --- | --- |
| HD-1 | Contract-layer vs implementation-layer separation — every doc marks what a rebuild must preserve vs what can be dropped | `reflective-spec-plan` spec-vs-impl; verification-map `source_commit`/`last_verified_at` metadata | Adopted into PK lesson |
| HD-2 | Snapshot docs carry 快照日期 + pointer to live truth (task-card `status:`) | PK lessons carry review triggers; Decision Index is the live pointer | Adopted into PK lesson |
| HD-3 | Pitfalls written as guards, not warnings — 「無停止力的警告等於不存在」; silent failures get code guards cross-referenced from docs | `reflective-implement` Verification; ROUTE gates made failable 2026-09-23 (same principle) | Adopted into PK lesson |
| HD-4 | Incident record: symptom ≠ root cause; root cause = "why the design allowed it"; detection delay is signal; 防護落點 names file:test | `06-repo/AGENTS.md` falsifiability; record-hygiene validator | Adopted into PK lesson |
| HD-5 | Task cards: plain markdown, `status:` is live truth, `depends_on` graph, blocked names the specific external input, comments carry decision context | `plans/` records + Decision Index; no card system installed | No change — overlaps existing convention |
| HD-6 | Acceptance as numbers — rebuild phases verify "these queries return these values", never "looks right"; un-rebuildable provenance declared | Verification-map acceptance.yaml; record-hygiene falsifiability | Adopted into PK lesson |
| HD-7 | Secrets docs write location+procedure, never values; mount dirs not files (inode pinning); dual-source mismatch fails loud | Out of scope — TeaPrompt holds no secrets | No change (out of scope) |
| HD-8 | Test-safety doc: danger declaration first, guard + bypass documented, disposable/live layering, test-data pollution policy | `09-running-tests.md` pattern; TeaPrompt tests are doc-only, no live env | No change — no live surface |
| HD-9 | Agent-memory format: feedback/project/reference triage; write-in triggers; don't duplicate handbook knowledge | Mnemopi memory + `learn`/`retain` already serve this | No change — installed equivalent exists |

## Candidate Adoption Ledger

| ID | Candidate | Status | Evidence | Reopen trigger |
| --- | --- | --- | --- | --- |
| HD-1..4,6 | Five documentation-contract principles | Adopted — PK durable lesson | This record; PK lesson entry | A TeaPrompt doc that violates a principle (e.g. a warning-only pitfall, an undated snapshot) |
| HD-5 | Task-card system | No change | `plans/` + Decision Index already provide provenance + live status | A project needing per-task cards outside the plans/ convention |
| HD-7 | Secrets-management SOP | No change (out of scope) | TeaPrompt holds no credentials | TeaPrompt gains a secret-bearing surface |
| HD-8 | Test-safety doc pattern | No change | No live-environment test surface exists | A test suite that can touch a live system |
| HD-9 | Agent-memory format | No change | Mnemopi `retain`/`learn` + managed skills cover it | A gap in current memory conventions |

## Evidence vs Inference

| Claim | Status | Basis |
| --- | --- | --- |
| Kit structure and all quoted principles | Observed | All 15 files read in full, 2026-09-23 |
| No sensitive values present | Observed | Every file is template/placeholder text |
| HD-3 matches TeaPrompt's failable-gates principle | Observed | ROUTE gate fix commit 6b31ab1 same day |
| The nine-volume order is "proven" | `[INFERENCE]` | README asserts it; no external validation of the ordering claim |
| Kit's target audience is a no-oral-handover successor | Observed | README line 3–5 |

## Evidence Actually Checked

- `~/dev/handover-docs/` — all 15 files read in full, 2026-09-23.
- TeaPrompt installed surfaces checked for overlap: `reflective-handoff-retro`, `reflective-spec-plan`, `reflective-implement` Verification, `validate_record_hygiene.py`, `PROJECT_KNOWLEDGE.md` lesson format.
- Not done: no external validation of the methodology against a real handover; the kit is self-described.

## Falsifiability

- Wrong about "no sensitive values" if any file contains a real credential/host — all files read; all fields are placeholders.
- Wrong about HD-5 overlap if `plans/` records lack live-status or provenance — both are enforced by `validate_record_hygiene.py` and the Decision Index.
- The PK lesson is wrong if its principles contradict an installed contract — all five are consistent with existing verification/record conventions.

## Completion Ledger

| Item | Status | Evidence |
| --- | --- | --- |
| Kit read in full; sensitive-keyword audit clean | done | Method; Evidence vs Inference |
| Nine concepts mapped; five adopted into PK lesson | done | Concept Map; Candidate Adoption Ledger |
| PK durable lesson written | done | `PROJECT_KNOWLEDGE.md` |
| Guard written | done | `plans/tests/test_handover_docs_survey_record.py` |
| Full repository gate | done | `make all` from the repository root |
