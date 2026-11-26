# WGS-X4b No-Op Hunt — Preregistered Plan (2026-11-26)

Language: English
> **Status:** plan only (`X4B-PLAN1`), drafted 2026-11-26 under owner direction ("起草獨立的預先登記計畫，不呼叫模型"). This record authorizes no model call, CLI run, fixture execution, permission change, skill edit, commit or push. Execution needs a separate owner authorization that names budget caps, model families and the frozen unit list.

## Question

Which units of the nine core skills change agent behavior on a task that exercises them, and which show no observable effect on any tested model family? A no-op verdict is model-relative ([A8](skill-improvement-plan-2026-07-24.md)) and fixture-relative. The hunt can nominate a deletion; it never deletes.

## Relation to Existing Work

- [WGS-X4b](skill-improvement-plan-2026-07-24.md): evidence gate ruled fired on 2026-11-26 ([SCR-P3](skills-survey-corpus-rethink-2026-11-26.md)); this plan is its next step.
- [DF-C2](fresh-dogfood-campaign-preregistration-2026-10-14.md) and [DF-PB1](procedural-blind-dogfood-preregistration-2026-10-15.md) measure whole-skill effects for `reflective-implement`, `reflective-review` and `reflective-handoff-retro`. Both are held. Neither measures single units, so this plan does not wait on them and does not reuse their pools.
- [P6](skills-survey-corpus-rethink-2026-11-26.md#owner-decisions-and-landing-2026-11-26) and [T1](skills-survey-corpus-rethink-2026-11-26.md#t1-results) are small prototypes of this method on host subagents only. P6 tied 3/3 versus 3/3 because a single-focus fixture let both arms pass. T1 tied on two trims and lost the third to a rubric clause that failed every run in both arms.

## Units and Selection Rule

A unit is one bullet, one numbered step, or one obligation-carrying sentence in a core skill's Module Contract, workflow steps, rules, `Never` list, or verification section. Frontmatter, headings, example pointers and Prompt Sources are out of scope.

The pilot covers twelve units, frozen in a manifest before the first run and reviewed by the owner:

1. Four units whose adoption record cites external evidence only, with no recorded local incident.
2. Four units from the three longest core skills (`reflective-spec-plan`, `reflective-implement`, `reflective-research`).
3. Four units with a recorded reader concern, such as a positive duty inside a prohibition list.

Units pinned by guard tests stay eligible; a later deletion would update those pins in the same change.

## Arms and Fixtures

- **C:** the full skill. **T:** the skill with the unit deleted byte-exactly, with no rewording.
- One synthetic fixture per unit. Each fixture places the unit's behavior inside a multi-part task so the behavior is one detail among several, because P6 showed that a single-focus fixture saturates both arms.
- Fixtures, rubrics and both contract copies are hashed and frozen before any run and live outside the repository during runs.

## Substrate (owner permission, 2026-11-26)

The owner wrote "若要做實驗可以呼叫本機的 agent cli 像 cursor-agent or agy 這種的". Inventory checked 2026-11-26 with no inference: `cursor-agent` 2026.11.22-e9042b2 lists GPT-5.3 Codex, Composer, Claude, Grok and GPT-5.6 models; `agy` 1.5.17 lists Gemini 4, Gemini 3.8, Claude and GPT-OSS models.

- Use at least two model families other than the host's, for example one GPT-5.3 Codex model through `cursor-agent` and one Gemini 4 model through `agy`. Host subagents may form a third family. Prefer models without a "NO ZDR" marking.
- Every invocation follows [`headless-agent-cli-contract`](../skills/headless-agent-cli-contract/SKILL.md): a recipe per CLI and mode, then one qualifying canary per recipe before trial runs.
- Read-only units run in each CLI's plan mode. Units that need writes run only in disposable fixture copies and only under a permission configuration the owner approves. `--force`, `--yolo` and `--dangerously-skip-permissions` stay unused without that approval. A blocked recipe drops its family; it never widens permissions.
- Receipts keep stdout and stderr separately and retain raw output; the strip list removes known side-channels such as `cursor-agent` stderr `claude-mem` lines.

## Measurement and Decision Rules

Fixed before any run:

- Three runs per arm, per family, per unit in the pilot. Outputs are scored with arm labels stripped, using the `arm-blinded-eval-harness` scaffold and a rubric frozen per unit.
- Before freezing, each rubric is applied to two hand-written outputs, one that should pass and one that should fail; a clause that fails the passing output is rewritten before any run. T1-B showed that one miswritten clause can fail every run in both arms.
- **Load-bearing:** in any family, C passes at least two more runs than T.
- **No-op candidate:** in every tested family, T passes at least as many runs as C and at least two of three.
- **Inconclusive:** every other outcome.
- A no-op candidate becomes a deletion proposal only. Deletion needs a per-unit owner approval, lands with its pin updates and a record row, and never rests on one family.
- Stop after the twelve-unit pilot and report. If every non-host recipe is blocked, report `BLOCKED` rather than substituting host-only results.

## Proposed Budget

The owner sets the final caps; these are proposals.

| Item | Runs | Cost basis |
| --- | --- | --- |
| Qualification canaries | ≤ 4 | Owner's Cursor and Antigravity plan quotas |
| Pilot on two CLI families | 12 units × 2 arms × 3 runs × 2 families = 144 | Same quotas; a reported quota exhaustion stops that family, with no API key or overage |
| Optional host-subagent family | 72 | Host session usage |

Wall-clock time and per-run quota draw are unknown until qualification.

## Execution Steps

Each step needs the authorization named beside it.

1. Owner approves caps, families and this plan (authorization A).
2. Freeze the twelve-unit manifest, fixtures and rubrics with hashes; the owner reviews the unit list.
3. Qualify one recipe per CLI and mode.
4. Run the pilot, score blind, assign verdicts.
5. Report; send deletion proposals to the owner one unit at a time.

## Evidence vs Inference

- **Verified:** CLI versions and model lists on 2026-11-26 without inference; the WGS-X4b ruling; DF-C2's whole-skill scope; the P6 tie; the T1 results, including the T1-B rubric defect.
- **Inferred:** multi-part fixtures raise sensitivity; two non-host families reduce single-family bias.
- **Unknown:** per-run quota draw for both CLIs; whether their headless plan modes read fixture files without approval prompts.

## Falsifiability

- If both arms saturate on most units, the fixtures were insensitive; the pilot is inconclusive and is not evidence that units are no-ops.
- If a deleted no-op candidate later coincides with a recorded regression on its behavior, the verdict was wrong and the unit returns.

## Candidate Adoption Ledger

| ID | Candidate | Disposition | Next decision |
| --- | --- | --- | --- |
| X4B-PLAN1 | This plan | Drafted 2026-11-26; plan only | Owner authorization A |
| X4B-RUN1 | Pilot execution | Not authorized | Owner sets caps and families |
| X4B-DEL1 | Any unit deletion | Not authorized | Per-unit owner approval after verdicts |

## Standing Non-Goals

- No skill edit, model call, CLI run, installation, permission widening, commit or push follows from this plan.
