# Handover-Docs Methodology Survey — 2026-09-23

> **Refresh pointer (2026-10-22):** Current-only snapshot — not a git repo; no later mtime observed (all 16 files carry 2026-09-23 mtimes); sha256 snapshot below in `## Latest-version refresh — 2026-10-22` establishes a hash baseline but proves no byte-equality with 2026-09-23 content. Prior findings stand.

> **Status: decided — record-only; one durable lesson adopted into PROJECT_KNOWLEDGE.md, no skill or wording installed.** The object is `~/dev/handover-docs/` — a local, reusable **project handover documentation kit** (16 markdown files by documented enumeration: 1 README methodology + 1 glossary + 9 handbook volumes + 2 ops SOPs + 3 templates; the original banner said "15 markdown files" — corrected 2026-10-02) written in Traditional Chinese. Its goal: a successor engineer with **no oral handover and no live support from the original team** can understand the system, operate it safely, and rebuild from zero using only repo docs. All content is templates and placeholders — no credentials, hosts, or real values exist in the kit; nothing sensitive was recorded. Guard: `plans/tests/test_handover_docs_survey_record.py`.

## Research Question

User instruction: "Learn from @~/dev/handover-docs/ and beware about sensitive keywords (avoid recording them). Learn key knowledge from them" — then "record non-sensitive into docs or skills if worth it". Questions: (1) what the kit teaches that generalizes; (2) whether any pattern exposes a gap on an installed TeaPrompt surface; (3) what is worth recording and where.

## Direct Recommendation (as of 2026-09-23)

- **Adopt — one durable lesson into PROJECT_KNOWLEDGE.md.** The kit's five design principles are documentation-engineering contracts that transfer directly to how TeaPrompt writes and reviews records: contract-layer vs implementation-layer separation, snapshot dating with live-truth pointers, decision provenance, pitfalls-as-guards, plain-text artifacts.
- **No new skill.** The kit is a *documentation structure*, not an executable workflow; TeaPrompt's `reflective-handoff-retro` already owns session-transfer, and the kit's task-card/agent-memory formats overlap with existing memory conventions. A skill would duplicate structure without a named local failure.
- **Candidate for later:** if TeaPrompt ever produces handover docs for a product repo, the kit's nine-volume handbook order (01 business → 02 architecture → 03 data → 04 pipelines → 05 ops → 09 tests → 06 decisions → 07 state → 08 rebuild) is the proven sequence.

## Method

Coordinator reported reading all files in full (2026-09-23). The kit's documented enumeration totals **16** files: `README.md`, `glossary.md`, `handbook/01-09`, `ops/secrets-management.md`, `ops/offsite-backup.md`, `templates/{task-card,incident-entry,agent-memory}.md`. No scouts, no panel. Sensitive-keyword audit: the enumerated files are template/placeholder text; no real values present. *(supersession 2026-10-02: this paragraph originally claimed "read all 15 files in full" — a historical self-report for which no VCS or per-file receipts exist; whether the 16-file enumeration was miscounted or one file was missed cannot be reconstructed, and this record does not retroactively claim a verified 16-file full read.)*

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
| Kit structure and all quoted principles | Observed | Documented enumeration is 16 files; the 2026-09-23 "all read" claim is a self-report without per-file receipts (see Method) |
| No sensitive values present | Observed | Every file is template/placeholder text |
| HD-3 matches TeaPrompt's failable-gates principle | Observed | ROUTE gate fix commit 6b31ab1 same day |
| The nine-volume order is "proven" | `[INFERENCE]` | README asserts it; no external validation of the ordering claim |
| Kit's target audience is a no-oral-handover successor | Observed | README line 3–5 |

## Evidence Actually Checked

- `~/dev/handover-docs/` — 16 files by documented enumeration; original 2026-09-23 self-report claimed all read without VCS/per-file receipts (supersession 2026-10-02; see Method).
- TeaPrompt installed surfaces checked for overlap: `reflective-handoff-retro`, `reflective-spec-plan`, `reflective-implement` Verification, `validate_record_hygiene.py`, `PROJECT_KNOWLEDGE.md` lesson format.
- Not done: no external validation of the methodology against a real handover; the kit is self-described.

## Falsifiability

- Wrong about "no sensitive values" if any file contains a real credential/host — per the 2026-09-23 audit, all enumerated files are placeholders (the all-read claim remains a self-report; see Method).
- Wrong about HD-5 overlap if `plans/` records lack live-status or provenance — both are enforced by `validate_record_hygiene.py` and the Decision Index.
- The PK lesson is wrong if its principles contradict an installed contract — all five are consistent with existing verification/record conventions.

## Completion Ledger

| Item | Status | Evidence |
| --- | --- | --- |
| Kit surveyed; sensitive-keyword audit clean | done | Method; Evidence vs Inference (16-file enumeration vs all-read self-report noted there) |
| Nine concepts mapped; five adopted into PK lesson | done | Concept Map; Candidate Adoption Ledger |
| PK durable lesson written | done | `PROJECT_KNOWLEDGE.md` |
| Guard written | done | `plans/tests/test_handover_docs_survey_record.py` |
| Full repository gate | done | `make all` from the repository root |

## Latest-version refresh — 2026-10-22

Read-only metadata refresh; no content re-audit, no sensitive data handled. The kit is **not a git repository** (`git rev-parse` fails), so there is no commit pin to compare — current-only snapshot evidence.

- **Prior baseline:** 16-file documented enumeration surveyed 2026-09-23 (all-read claim is a self-report without per-file receipts; see Method).
- **Latest checked:** same 16 files present at the same paths (`README.md`, `glossary.md`, `handbook/01–09`, `ops/secrets-management.md`, `ops/offsite-backup.md`, `templates/{task-card,incident-entry,agent-memory}.md`); **all mtimes 2026-09-23 11:37–11:42** — no later mtime observed, no files added or removed. **Status: current-only** (mtime + enumeration tier; no prior hashes exist, so byte-equality with 2026-09-23 content is not claimed — this snapshot establishes the hash baseline for future diffs).
- **sha256 snapshot (2026-10-22, methodology files only):**
  - `README.md` `e1e4910f…0102b6`, `glossary.md` `ef41a1f4…0014b53`
  - `handbook/01-business-context.md` `35520efe…be3db`, `02-architecture.md` `24a3a2a4…e6e0`, `03-data-model.md` `fb5381c9…1609b47`, `04-pipelines-sync.md` `3868698d…a02e30`, `05-operations-runbook.md` `14b88b26…9642f`, `06-decisions-incidents.md` `c6ac4359…82d`, `07-current-state.md` `2eafe744…89c302`, `08-rebuild-runbook.md` `a3480a9d…5cda139`, `09-running-tests.md` `63099dfe…48734a`
  - `ops/offsite-backup.md` `bfdf722e…4c15f`, `ops/secrets-management.md` `4cf9e9e5…40fcab`
  - `templates/agent-memory.md` `021c8a57…23c3b8da`, `templates/incident-entry.md` `1e790e19…04300ab1a`, `templates/task-card.md` `9fe1680d…25e51a`
  - (Full 64-hex digests recorded in the refresh receipt `local://refresh-RefreshMemory.json`; prefixes above are collision-irrelevant for a 16-file snapshot but the receipt is authoritative.)
- **Effect on prior findings:** None. The HD-1..4,6 PK lesson stands; HD-5/7/8/9 no-change dispositions stand. No new methodology to evaluate.
- **Inspected:** directory listing, per-file mtimes, `shasum -a 256` of all 16 files. No file bodies re-read (same-mtime tier only; the no-sensitive-values claim still rests on the 2026-09-23 audit).
- **Untested limits:** no byte-equality claim — byte comparison against 2026-09-23 content is impossible without prior hashes. A future refresh can diff against this snapshot's full digests.
