# Skill-Library Comparison Survey — Superpowers vs. Three Known Libraries + 2026-11 Reddit Read (2026-11-25)

Language: English
> **Status:** source-qualified reference record (`CMP-DOC1`); no Skill, prompt-body, operating-rule, or runtime change.**

The owner asked to compare three previously-surveyed libraries (`mattpocock/skills`, `backnotprop/pstack`, `addyosmani/agent-skills`) against Superpowers, and to account for recent Reddit discourse, especially November 2026. This record synthesizes the four pinned trees, the existing adoption records for each, and a bounded Reddit scan. It does not re-adopt, install, or run anything; prior per-repo dispositions stand unless noted.

## Research Question and Direct Recommendation

What actually distinguishes these four libraries at the mechanism level, and does November 2026 community discourse change any TeaPrompt disposition?

**No new adoption; one new deferred note.** All four libraries are variations on the same premise — SKILL.md packaging of reusable agent instructions — but they split on **where enforcement lives**. Superpowers pushes invocation into the host harness (plugins, session bootstrap, subagent scripts); the other three stay inside the skill files themselves. The Nov 2026 Reddit signal is consistent with prior records (skills-over-agents, progressive disclosure, composability), adds one genuinely new item — a community skill-vetting tool for supply-chain risk — and changes nothing about existing TeaPrompt contracts.

## Evidence Used and Date Context

Checked 2026-11-25. Fresh shallow clones of the three libraries; Superpowers read from the existing adoption record (`superpowers-v6.4-adoption-2026-10-03.md`, refreshed 2026-10-22). Reddit scan via `google_search`, treated as discourse evidence, not implementation evidence.

| Item | Pinned HEAD | Prior record / disposition |
| --- | --- | --- |
| `obra/superpowers` | `22f0b46` (main; record pinned `v6.4.2` `8ca22db`, refreshed `v7.0.1`) | Adopted SP-1/SP-2 wording repairs 2026-10-03; SP-3–SP-6 rejected (runtime/host non-goals) |
| `mattpocock/skills` | `d653911` | `mattpocock-skills-v131-delta-survey-2026-10-07.md` — reference-only, no gap |
| `backnotprop/pstack` | `2a56216` | `pstack-matt-lauren-survey-2026-10-03.md` + follow-throughs — reference-only |
| `addyosmani/agent-skills` | `e997ac5` | `agent-ecosystem-harness-survey-2026-10-11.md` + delta 2026-11-19 (`0.6.13→0.6.17`) — reference-only, AE-01–16 stands |

## The Four Libraries — Mechanism Split

| Library | What it actually is | Enforcement location | Distinctive mechanism |
| --- | --- | --- | --- |
| **Superpowers** (obra) | ~40+ skills + plugins + scripts that make the *host* enforce invocation | **Host harness** — SessionStart hooks, `using-superpowers` bootstrap, `subagent-driven-development`, `executing-plans`, git-worktree orchestration | The only one that treats skills as a *runtime concern*: session bootstrap injects skills, a plugin enforces them, subagent scripts run plan-execute loops |
| **mattpocock/skills** | Personal daily-driver skills by a working engineer ("real engineering, not vibe coding") | **Skill files only** — no hooks, no runtime | Anti-process-ownership: explicitly rejects GSD/BMAD/Spec-Kit-style frameworks that "take away your control"; small, composable, model-agnostic; install via `skills.sh` editable copy |
| **backnotprop/pstack** | Standalone mirror of `cursor/plugins/pstack` (Poteto's playbooks) | **Skill files only** | Verification-methodology densest: `create-verification-skill`, `create-formal-verification-skill` + `statechart`, `arena`/`blast-radius` debate/stress skills, `interrogate`, `correct`, `principle-*` discipline skills; `unslop`/`bro`/`ketchup` named-style skills |
| **addyosmani/agent-skills** | Production-grade engineering lifecycle pack (26 skills, 10 slash commands) | **Skill files + command layer** — `/spec /plan /build /test /review /ship` TOML commands activate skills | Most *lifecycle-structured*: every command maps to a development phase; spec→plan→build→test→review→ship pipeline; `/build auto` is a governed full-pass; domain packs (a11y, webperf, frontend) outside TeaPrompt scope |

## Key Differences vs. Superpowers

1. **Enforcement boundary.** Superpowers' signature move is pushing invocation into the host: `using-superpowers` SessionStart hooks, `subagent-driven-development`/`executing-plans` scripts, worktree orchestration. The other three deliberately stay inside the skill files — mattpocock explicitly rejects process-owning frameworks, pstack and addyosmani ship no runtime. For TeaPrompt (no runtime, standing non-goal) this is the decisive split: Superpowers' *value* is host machinery that SP-3–SP-6 already rejected; the other three are closer to TeaPrompt's own shape but demonstrate no new local gap.
2. **Methodology density.** pstack is the outlier — it carries the most explicit verification/correctness playbooks (`verifier≠author`, `patch-id binding`, `contiguous-verified-run landing`, formal-verification/statechart). Superpowers is workflow-complete; mattpocock is minimalist engineering craft; addyosmani is lifecycle-complete.
3. **Adoption status.** Only Superpowers yielded adopted wording (SP-1: plans-as-decisions on `reflective-spec-plan`; SP-2: named `Declined to Judge` on `reflective-review`) — both because they were *epistemic rules*, not runtime. The other three remain reference-only: nothing they encode is absent from the nine core skills.
4. **Distribution.** All four now ride the `skills.sh`/open-standard install path; Superpowers additionally runs as a plugin. mattpocock's editable-copy install, pstack's mirror-maintenance, and addyosmani's command-packaging are three different governance postures for the same spec.

## November 2026 Reddit Discourse — What Changed

| Claim in discourse | Assessment |
| --- | --- |
| Skills libraries preferred over agent-per-task / multi-agent swarms (coordination overhead, API cost, token latency) | Consistent with prior records (ALV, MTS, UAS surveys); reinforces, does not alter, existing dispositions |
| Progressive disclosure treated as the settled design (YAML metadata → body → on-demand files) | Same architecture TeaPrompt already uses |
| Community catalogs proliferating (`ai-skill-navigator`, `samber/cc-skills`, `spotkit`, Remocn, repo-memory/repo-relay handoffs) | Volume signal only; no specific mechanism verified |
| **`agent-skill-vet` — a tool to scan downloaded skills for hidden instructions/unverified scripts before install** | **New mechanism note**: supply-chain vetting of community skills. Recorded as a deferred doc note — TeaPrompt already treats installed skills as trusted local artifacts and its own skills are source-reviewed; a vetting gate would matter only if TeaPrompt ever imports third-party skills wholesale, which adoption policy already gates |
| No empirical benchmarks comparing agent-per-task vs skills-library outcomes | Confirms the standing caveat: community preference is discourse, not measured efficacy |

## Evidence vs Inference

- **Verified:** four pinned HEADs; README/frontmatter structure of each; the Superpowers adoption record's disposition and SP-1/SP-2 anchors; the Reddit-scan themes above.
- **Supplier-summarized (unverified):** star/download counts, "production-grade" labels, the `agent-skill-vet` tool's actual detection quality (existence noted, not audited), Reddit representativeness.
- **Inference (this record):** the mechanism-split table; the judgment that only Superpowers crosses the runtime boundary and therefore only Superpowers produced adopted wording; that CMP-DOC2 (supply-chain vetting note) is dormant while TeaPrompt's skills remain self-authored.
- **Unknown:** real-world efficacy deltas between the four libraries; whether `agent-skill-vet` and similar tools are accurate; whether the November discourse is representative beyond Claude-centric subreddits.

## TeaPrompt Contract Map and Disposition

| Finding | Existing surface | Disposition |
| --- | --- | --- |
| Skill-files-only packaging (all three) | Nine frozen TeaPrompt skills already use the same shape | Restated; no gap |
| Lifecycle-structured commands (addyosmani) | `reflective-dispatch` routes to spec-plan → implement → review | Same lifecycle, prompt-layer routing |
| Verification-methodology playbooks (pstack) | `reflective-review` claims ledger, `verification-map-generator`, `arm-blinded-eval-harness`, governed-delivery oracles | Restated; pstack's formal-verification/statechart skills are domain packs out of scope |
| Host-enforced invocation (Superpowers) | Standing non-goal; SP-3–SP-6 rejected for this reason | Confirmed again — the one adoption-bearing library is also the one whose *runtime* is out of scope |
| Community supply-chain vetting (`agent-skill-vet`) | `runtime-trust-boundary.md` external-content treatment; adoption policy already requires per-item review | Deferred doc note — a vetting checklist is dormant while all TeaPrompt skills are self-authored and source-reviewed |

## Candidate Adoption Ledger

| ID | Candidate | Disposition | Evidence / reopen trigger |
| --- | --- | --- | --- |
| CMP-DOC1 | This comparison record and its catalogue row | Adopted; documentation only | Refresh when any pinned library changes materially or a new comparison candidate appears |
| CMP-DOC2 | Skill supply-chain vetting note (inspired by `agent-skill-vet`): a checklist for reviewing third-party skills before adoption | Deferred | Dormant while TeaPrompt's skills remain self-authored; reopen on the first third-party skill import proposal |
| CMP-SK1 | Any new skill from the comparison | Not adopted | No verified local gap across the four libraries |
| CMP-RUN1 | Any host-enforcement machinery (Superpowers plugins/hooks, subagent scripts) | Not adopted | Standing non-goal; SP-3–SP-6 already rejected |
| CMP-RULE1 | Treat November-2026 community preference or download counts as evidence a library is effective | Rejected | Discourse is not efficacy; mechanism transfer requires reproduced local need |

## Falsifiability

- A demonstrated case where a pstack/addyosmani/mattpocock skill catches a defect TeaPrompt's existing surfaces miss would reopen CMP-SK1.
- A first third-party skill import proposal activates CMP-DOC2.
- If Superpowers' host machinery ever becomes TeaPrompt-relevant (a TeaPrompt runtime exists), SP-3–SP-6 and CMP-RUN1 reopen together.

## Standing Non-Goals

- No runtime, Skill, prompt-body, routing, or governance change; prior per-repo dispositions (SP, PML, AGS) stand.
- No install, plugin, hook, or model call; no commit or push beyond this record and its catalogue row.
- Reddit posts were used as discourse evidence only — none are cited as verified implementation claims.
