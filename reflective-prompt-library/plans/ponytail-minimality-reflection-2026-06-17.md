# Ponytail Minimality Reflection

> **Status: historical record (retired from active guidance, 2026-07-11).** Kept for provenance and as Decision Index / Durable Lesson evidence. Wording may predate the nine-skill surface and current governance; do not cite as current policy — see `PROJECT_KNOWLEDGE.md` Decision Index for live decisions.


Date: 2026-06-17
Skill route: `reflective-dispatch` -> `reflective-research` + `reflective-review` + `reflective-implement`
Strictness Level: L3/L5. This changes workflow-skill routing and benchmark coverage, but stays within documentation and local validation tooling.

## Sources Checked

| Source | Status | Use |
| --- | --- | --- |
| `https://github.com/DietrichGebert/ponytail` | Verified | Repository structure, README positioning, install surface, commands, release metadata. |
| `https://raw.githubusercontent.com/DietrichGebert/ponytail/main/README.md` | Verified | Claims about code reduction benchmark, portability, command set, and ladder. |
| `https://raw.githubusercontent.com/DietrichGebert/ponytail/main/AGENTS.md` | Verified | Always-on rule shape, minimality ladder, non-negligence boundaries, runnable-check requirement. |
| `https://raw.githubusercontent.com/DietrichGebert/ponytail/main/skills/ponytail/SKILL.md` | Verified | Skill-level trigger cues, intensity levels, output style, debt comment convention. |
| `https://raw.githubusercontent.com/DietrichGebert/ponytail/main/skills/ponytail-review/SKILL.md` | Verified | Complexity-only review tags and `net: - lines possible` scoring. |
| `https://raw.githubusercontent.com/DietrichGebert/ponytail/main/skills/ponytail-audit/SKILL.md` | Verified | Repo-wide complexity audit surface. |
| `https://raw.githubusercontent.com/DietrichGebert/ponytail/main/skills/ponytail-debt/SKILL.md` | Verified | `ponytail:` marker ledger and no-trigger risk reporting. |
| `https://raw.githubusercontent.com/DietrichGebert/ponytail/main/skills/ponytail-help/SKILL.md` | Verified | Help card, mode reference, and command summary. |
| `https://raw.githubusercontent.com/DietrichGebert/ponytail/main/hooks/ponytail-instructions.js` | Verified | Shared instruction-builder pattern and fallback rule injection. |
| `https://raw.githubusercontent.com/DietrichGebert/ponytail/main/pi-extension/index.js` | Verified | Pi extension entry point, mode parser, session-mode recovery, command registration, and `before_agent_start` prompt injection. |
| DeepWiki search / direct URL | Not verified | Search did not expose a stable readable DeepWiki page for this repo in the available tool path. Do not treat DeepWiki-specific commentary as evidence. |

## Core Finding

Ponytail is not a better implementation agent. Its useful idea is narrower: make the agent first doubt whether new code, a new dependency, a new abstraction, or extra explanation should exist.

For TeaPrompt, this belongs as a **Minimality Gate**, not as a replacement for reflective planning, risk review, implementation discipline, or correctness review.

## Socratic Critique

1. If TeaPrompt already has `reflective-implement` and `reflective-review`, why add anything?

   Because those skills mention small safe changes and overengineering scans, but neither makes minimality the primary artifact. A user asking "is this overbuilt?" should not have to enter a full correctness review just to get a delete-list.

2. Does this violate the earlier decision to avoid a ninth skill for runtime governance?

   No. Runtime trust boundaries are a supporting lens applied across many workflows. Minimality is an independently invokable gate with a distinct output contract: skip/delete/reuse/shrink/implement minimum, plus debt markers and a complexity-only review format.

3. What is the strongest objection?

   Minimality can become underengineering. A "use native input" answer may be correct for an internal tool and wrong for locale, timezone, accessibility, browser, hardware, or product requirements. The new skill therefore includes a safety floor and escalation rules rather than adopting Ponytail as an always-on personality.

4. What should not be copied?

   Do not copy the full Ponytail runtime: hooks, command set, mode persistence, benchmark claims, or terse-output personality. TeaPrompt's goal is reflective engineering, not a universal lazy mode. The benchmark claims are useful but task-shape-specific; they should not become general proof that less code is always better.

5. What is the falsifiable adoption claim?

   If `reflective-minimality` is useful, it should route small overengineering/dependency/abstraction requests more directly than `reflective-review`, produce actionable cuts, and preserve safety-critical requirements. If it causes agents to skip required behavior or tests, it should be demoted back into `reflective-review`.

6. What did the follow-up code-map check correct?

   The main entry-point model is right, but the surface is broader than "three commands." The Pi extension registers `/ponytail`, `/ponytail-review`, `/ponytail-audit`, `/ponytail-debt`, and `/ponytail-help`; audit and debt are first-class one-shot skills, not only secondary documentation. TeaPrompt should keep those as concepts inside `reflective-minimality`, not add separate runtime commands yet.

## Adopted Change

Add `reflective-minimality` as a compact cross-cutting skill:

- Existence challenge before implementation.
- Delete/narrow/defer before adding.
- Standard library, platform-native behavior, existing dependency, one-line/one-file ladder.
- Safety floor for validation, security, privacy, auth, data-loss prevention, accessibility, compatibility, and explicit requirements.
- Intentional debt marker with ceiling and upgrade trigger.
- Complexity-only review output format.
- Repo-wide complexity audit and debt-ledger concepts, without adding runtime commands.

## Rejected Changes

- Rejected: Install Ponytail as a runtime dependency.
  Reason: TeaPrompt should learn the gate pattern without coupling its library to an external plugin.

- Rejected: Make minimality always-on for every skill.
  Reason: Some tasks need specification, risk modeling, documentation, or verification more than code reduction.

- Rejected: Add hooks, modes, and a debt scanner immediately.
  Reason: No repeated local workflow evidence yet. Prompt-level gate is the smallest useful step.

## Updated Files

- `skills/reflective-minimality/SKILL.md`
- `skills/skill-map.md`
- `skills/SKILL_TRIGGER_CHEATSHEET.md`
- `skills/SKILL_TRIGGER_CHEATSHEET.zh-TW.md`
- `README.md`
- `README.zh-TW.md`
- `METHODOLOGY_MAP.md`
- `METHODOLOGY_MAP.zh-TW.md`
- `plans/benchmark_tasks.py`
- `plans/benchmark-tasks.json`
- `index.json`

## Future Promotion Criteria

Consider a script or hook only if at least five real tasks show repeated need for:

- Scanning `ponytail:` markers into a debt ledger.
- Detecting new dependencies or one-implementation abstractions in diffs.
- Enforcing a minimality review before implementation on high-bloat tasks.

Until then, keep it as a skill-level gate.
