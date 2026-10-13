# Ecosystem Packaging, Host Distribution and Governance Health Roadmap — 2026-10-13

Language: English

> **Status: active domain roadmap (record-only; non-authoritative).** Scheduling and architectural companion derived from ecosystem packaging, multi-tool skill distribution, zh-TW localization, and governance hygiene surveys. Preserves standing non-goals, frozen core skills cardinality, and bilingual cheatsheet parity. No new runtime or core skill is adopted by this record.

## Purpose

Summarize packaging, zh-TW navigation parity and governance maintenance against the installation guide's named Claude Code, Codex, Cursor, Antigravity CLI/IDE and OpenCode surfaces. Other host discovery behavior remains unverified rather than inferred from a guessed path.

## Evidence vs Inference

- **Observed Repository Evidence:** Pinned source checkouts, packaging receipts, and validator executions in `checkpoint-packaging-decision-2026-10-11.md`, `checkpoint-2026-10-11-outcome.md`, `checkpoint-2026-10-11-preparation-2026-10-10.md`, `mattpocock-skills-v131-delta-survey-2026-10-07.md`, `managed-skills-learned-survey-2026-10-06.md`, `agnix-agent-skills-hook-survey-2026-08-04.md`, and `frozen-core-parity-review-2026-07-11.md`.
- **Author-Claimed Evidence:** Third-party marketplace adoption counts, upstream installation success claims, and unobserved host runtime behaviors.
- **[INFERENCE]:** Projections of emerging agent skill packaging standards, cross-host symlink behaviors, and future multi-language demands.

## Surveyed Plans Corpus

This roadmap derives directly from the following surveyed plans:
- `checkpoint-packaging-decision-2026-10-11.md`
- `checkpoint-2026-10-11-outcome.md`
- `checkpoint-2026-10-11-preparation-2026-10-10.md`
- `checkpoint-2026-10-11-runbook.md`
- `mattpocock-skills-v131-delta-survey-2026-10-07.md`
- `managed-skills-learned-survey-2026-10-06.md`
- `agnix-agent-skills-hook-survey-2026-08-04.md`
- `baton-dispatch-survey-2026-07-13.md`
- `frozen-core-parity-review-2026-07-11.md`
- `cross-survey-rethink-2026-10-07.md`
- `methodology-only-rethink-panel-2026-10-01.md`
- `d025db7-publication-review-2026-10-02.md`
- `ai-assisted-team-throughput-review-2026-08-12.md`

## Packaging and Distribution Architecture

TeaPrompt maintains a strictly decoupled architecture separating natural-language policy from host environments:
1. **The Frozen Nine Core Skills:** `reflective-dispatch`, `reflective-brief`, `reflective-spec-plan`, `reflective-implement`, `reflective-minimality`, `reflective-review`, `reflective-research`, `reflective-risk`, and `reflective-handoff-retro`. Gated by three-recurrence proof and explicit human approval.
2. **Registered Domain Packs:** 10 registered packs in `DOMAIN_PACK_SKILLS`, invoked by host agents or scripts, never auto-routed by dispatch.
3. **Scoped Factoring:** The October 11 decision moved governance objects to `agent-governance-scaffold/ARTIFACTS.md` and flow bodies to the two flow packs' `TEMPLATES.md`, preserving contracts and body semantics. Other packs are not claimed factored.
4. **Registry-Relative Parity:** English and zh-TW appendices mirror the live domain-pack registry plus the dispatch pointer. Eleven bullets is this snapshot's count, not a future fixed cardinality.
5. **Managed-Skill Boundary:** Host-side managed skills in `~/.omp/agent/managed-skills` remain isolated from repository-authored skills. Memory-derived insights require `04-agent/artifact-promotion.md` §4 gates.

## Horizon Milestones

### Horizon 1 — Standing Invariants & Shipped Distribution
- **Installation Guidance:** Install complete directories using the [canonical guide](../SKILL_INSTALLATION.md). Cursor uses `.agents/skills` or supported `.cursor/skills`, with `.cursor/rules/teaprompt-skills.mdc` as a Rules fallback; do not substitute `.cursorrules` or assert an undocumented OMP path.
- **Cheatsheet Lockstep:** T2 parity holds for the current registry, with eleven bullets in each appendix at this snapshot.
- **Record Hygiene:** For applicable records dated on/after 2026-07-12, status/evidence/ledger/falsifiability checks can fail validation; nearby external access-date detection is a warning heuristic, not a blocking provenance proof.

### Horizon 2 — Source-Bound P6 / T2 Review
- **Next P6 Review (2027-01-11):** Review standalone flow-pack generation evidence under the owning convention. T2 runs on a registry/appendix change, or that January evidence review if unchanged. F4/dormant duties retain their existing source/event conditions; no quarterly recurrence is established here.

### Horizon 3 — Trigger-Gated Queue
- **E2 Archive Restructuring:** A second independent archive-weight complaint **or** a maintainer's real navigation failure attributable to these surfaces reopens the [destructive E2 review](dormant-work-specs-2026-07-11.md#e2--archive-restructuring-panel-transcript-demotion-category-merges). Destinations remain `plans/`, `00-core` and `03-context`; the event is not automatic restructuring authority.
- **Localized Trigger Cues Beyond Cheatsheets:** Reconsider navigation cues on a verified zh-TW adoption signal under the owning June backlog; no full skill-body translation is authorized.

### Horizon 4 — Direction-Gated Non-Goals
- No full translation of `SKILL.md` bodies (cheatsheet, glossary, and navigation parity only).
- Never adopt host-specific CLI hooks (e.g. Agnix or private daemon plugins) into portable skill definitions.
- Never operate a centralized package registry or npm/pypi release pipeline for skills; git-native distribution remains canonical.

## Falsifiability

This planning summary is wrong or stale if:
1. A copied package needs a repository-only path or lacks a required sibling, or factoring changes emitted semantics without an owning behavior decision.
2. Installation guidance names an unsupported discovery path, or a known host copy/symlink failure is treated as successful installation without observing discovery.
3. Registry/appendix parity diverges, warning-tier date checks are reported as blocking proof, or E2/localization is activated without its own review/authority condition.

## Candidate Adoption Ledger

| ID | Candidate / Mechanism | Status | Evidence / Surface | Next Action / Trigger |
|---|---|---|---|---|
| EP-01 | Scoped TEMPLATES/ARTIFACTS Factoring | Adopted | `skills/agent-governance-scaffold/ARTIFACTS.md`, both flow packs' `TEMPLATES.md`; [owning packaging decision](checkpoint-packaging-decision-2026-10-11.md#candidate-adoption-ledger) | Reopen on missing copied reference, stale extraction consumer, changed body semantics or the governance main contract exceeding 20,000 characters |
| EP-02 | T2 Registry-Relative Bilingual Parity | Adopted | `skills/SKILL_TRIGGER_CHEATSHEET*.md`; [owning T2 decision](checkpoint-2026-10-11-outcome.md#t2-decision) | Check on registry/appendix change, or 2027-01-11 evidence review if unchanged |
| EP-03 | Multi-Host Installation Guide | Adopted | `SKILL_INSTALLATION.md` | None |
| EP-04 | Managed-Skill Isolation Boundary | Adopted | `04-agent/artifact-promotion.md` | None |
