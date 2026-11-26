# Uber Agent-Skills Platform Survey — Evals at Enterprise Scale (2026-11-24)

Language: English
> **Status:** source-qualified reference record (`UAS-DOC1`); no Skill, prompt-body, operating-rule, or runtime change.**

The owner asked to survey Uber's "How Uber Evals 1 Million Agent Skill Invocations a Month" article. This record preserves the primary source, separates verified mechanics from self-reported outcomes, and maps the transferable distinctions onto existing TeaPrompt contracts. It does not install Skill Workshop, `aifx`, or an eval harness; call a model; or authorize any runtime. Most mechanisms — lint-style skill quality gates, eval suites, minimal-context loading — already exist in TeaPrompt in prompt form; the genuinely new item is a *measured* ablation/effectiveness loop, recorded as a deferred doc note, not a reproduced local gap.

## Research Question and Direct Recommendation

Which mechanisms in Uber's skills platform are worth borrowing, and do they expose a TeaPrompt Docs or Skill gap?

**Record the boundaries; adopt the reference, defer the worked notes.** Uber's report is the first major enterprise-scale account of SKILL.md-style skills in production (5,000+ skills, 1M+ invocations/month, self-reported). Its transferable mechanisms: a three-tier promotion model for shared skills, telemetry-driven per-skill metrics, a spec→SKILL.md compile step so skills survive model churn, an authoring linter, a golden/real/author eval mix tested in a clean room, with/without-skill ablation with a blind judge, "code over LLM" cost levers, and an always-on `log-papercut` skill letting agents file structured friction reports. Each either restates an existing TeaPrompt contract or is a host-runtime concern; the closest thing to a local gap is that TeaPrompt lacks an effectiveness ablation for prompt text — recorded as deferred documentation.

## Evidence Used and Date Context

Checked 2026-11-24. Article: Uber engineering blog, "How Uber Evals 1 Million Agent Skill Invocations a Month" (Andrew Mager, Jason Varbedian, Uday Kiran Medisetty), published 2026-11-23, read via `uber.com/gb/en/blog/optimizing-ubers-agent-skills/`. The linked format spec `agentskills.io` resolves (HTTP 200, redirects to `/home`). No companion code, dataset, or Skill Workshop artifact is public; all platform numbers below are the article's own.

## What the Article Actually Claims

- **Format.** A skill is a SKILL.md (name + ~100-token description + body under ~500 lines) plus scripts/references, loaded in three stages: description always, body when invoked, files on demand. Git repo = marketplace; three tiers — **Domain** (team-owned, one peer review + CI), **Core** (platform-reviewed, maintained), **Always-on** (~100 skills everyone gets).
- **Distribution.** `aifx` CLI normalizes skill install across Claude Code, Codex, OpenCode, and internal agents; six-layer config merge (company→team→repo→dir→user→local), later layers only add.
- **Telemetry.** OpenTelemetry hooks record skill name, version, and whether the agent or the user invoked it — **no prompt text, no file contents** — feeding 12 per-skill metrics (users, retention, cost, latency, errors, …).
- **Authoring.** Skill Workshop compiles SKILL.md + test prompts from a `spec.md` (goal, outputs, required/forbidden tool actions, target agents/models) and **recompiles when a model or agent changes**. A linter enforces: numbered single-objective steps each with at least a soft verify; concrete commands with result checks; an error-recovery table ("try again" doesn't count).
- **Evals.** Suite guidance ≈ **5% golden / 80% real prompts graded on trajectory / 15% author-judged**; runs in three environments including a clean room that caught laptop-dependent assumptions. Article's experience: **evals passing 70–90% are more informative than 100%** (a perfect rate may mean the eval stopped detecting meaningful change); LLM-judges need human-annotated sets.
- **Ablation.** Replays real prompts with vs. without a skill, blind judge picks; also tests *word removal* inside skills ("as models get better, more words can reduce performance"). Reported: a warehouse-query skill — sessions without it made **13% more tool calls, 6× tool errors, 31% longer**, and the with-skill answer won **87%** of blind comparisons.
- **Cost levers.** Per-invocation cost = session-cost delta bracketing the skill call. Levers: run invariant steps as code ("Code Mode", citing Cloudflare's post; 100+ MCP tool definitions cost 50–70k tokens preloaded vs ~900 after); dispatch the skill to a cheaper-model worker so large results stay in the worker's context (tracing skill −46%/invocation); run scripts at load time (−32% mean cost on one search skill); move polling to a background agent.
- **Papercuts.** An always-on `log-papercut` skill lets agents file structured friction reports (tried/expected/actual/suggested fix); thousands filed in three months, hundreds fixed, each fix re-evaluated and regression-checked. Human signals: PR-review outcomes feed back into eval sets.
- **Open problem (their words).** Evaluating workflows that run rarely, matter a lot, and are hard to judge. Next: A/B testing skills, per-model skill compiling, trace indexing, skill recommendations, a task router.

## Evidence vs Inference

- **Verified:** the article text and figure captions above; `agentskills.io` resolves; Cloudflare's Code Mode post exists as cited.
- **Supplier-summarized (unverified):** every number — 5,000+ skills, 1M invocations/month, the 87%/13%/6×/31% ablation figures, the −46%/−32% cost deltas, "thousands of papercuts / hundreds fixed", and the 5%/80%/15% eval mix as practiced. No dataset, harness code, or statistical detail is published; intervals in Figure 13 are unlabeled beyond "95%".
- **Inference (this record):** the contract-map dispositions; the judgment that TeaPrompt's prompt-layer equivalents already cover most duties. Skill Workshop, aifx, Minion, AES, and Fawkes internals were not inspected.
- **Unknown:** whether the ablation judge was blinded to skill presence in the *output* (not just the run setup); papercut false-positive/duplication rates; how "trajectory" is scored; whether the 70–90% heuristic was measured or anecdotal.

## TeaPrompt Contract Map and Disposition

| Finding | Existing surface | Disposition |
| --- | --- | --- |
| SKILL.md three-stage loading (desc → body → on-demand files) | TeaPrompt's nine frozen skills already use frontmatter+body; `teaprompt-artifact-promotion` keeps invocation cheap | Same architecture; Uber's ~100-token description / ~500-line body budgets are host conventions, not new rules |
| Linter rules: numbered single-objective steps, concrete commands with result checks, error-recovery table | `skill-creator` (SKILL.md architecture + eval loop); hygiene validators | Restated; a dedicated authoring-time SKILL lint is a host tool — deferred doc note |
| Golden/real/author eval mix; trajectory vs outcome split; 70–90% pass-rate heuristic | `golden-benchmark-runner`; `arm-blinded-eval-harness`; `flow-loop-harness` | Same structure (golden set + blinded comparison); the 70–90% calibration claim is supplier-anecdote, logged as a heuristic not a rule |
| Spec→SKILL.md compile, recompiled on model/agent change | `plans/` adoption ledgers pin adopted text at single surfaces; skills are prompt artifacts, not generated | Different lifecycle (TeaPrompt pins human-written text); compile-step is a host tool — reference only |
| With/without-skill ablation + blind judge + word-removal tests | `arm-blinded-eval-harness` covers blinded paired scoring and `golden-benchmark-runner` defines bare-versus-skill runs; **no executed ablation run has measured TeaPrompt skill text** | Closest real gap: deferred doc note (UAS-DOC2), not a Skill — no run has been authorized or executed |
| Code-over-LLM ("Code Mode"), worker-on-cheaper-model, load-time scripts, polling offload | `runtime-trust-boundary.md` deterministic-tool preference; `flow-control-generator` host scripts; standing non-goal on runtime | Cost engineering of a hosted agent platform; methodology already prefers deterministic paths — reference only |
| `log-papercut`: always-on skill for agents to file structured friction reports | `reflective-handoff-retro` captures session lessons; `learn`/`memory` conventions exist | In-session agent-originated telemetry is a runtime feature; a prompt-layer analog (friction note in handoff) is a deferred doc note |
| Telemetry with no prompt text / no file contents | `runtime-trust-boundary.md` data-policy gating | Same privacy posture; Uber's OTel implementation is host infra |
| Human PR-review signals feed eval sets | `reflective-review` + adoption ledgers (real outcomes revise dispositions) | Same loop in prompt form |

## Candidate Adoption Ledger

| ID | Candidate | Disposition | Evidence / reopen trigger |
| --- | --- | --- | --- |
| UAS-DOC1 | This source-bound record and its catalogue row | Adopted; documentation only | Refresh when Uber publishes eval/ablation methodology detail, Skill Workshop artifacts, or a skills-spec change |
| UAS-DOC2 | Optional worked references: (a) with/without ablation + word-removal as an effectiveness check for prompt text; (b) papercut-style friction capture in handoff/retro; (c) 70–90% pass-rate calibration heuristic | Deferred | No reproduced local gap; joins the deferred worked-reference queue (ACL-DOC2, CKB-DOC2). Reopen if a TeaPrompt skill's effectiveness is ever questioned with data. **(b) adopted in place 2026-11-25 as SUR-ED2 ([record](skills-update-review-2026-11-25.md)); owner ratified 2026-11-26; (a) and (c) stay deferred.** |
| UAS-SK1 | New skill-lint, ablation-eval, or papercut Skill | Not adopted | No verified local structural gap; evaluation duties live in `arm-blinded-eval-harness`/`golden-benchmark-runner` as methodology |
| UAS-RUN1 | Adopt aifx/Skill Workshop/telemetry pipeline patterns | Not adopted | Host/product implementation; a TeaPrompt runtime is a standing non-goal |
| UAS-RULE1 | Treat Uber's scale numbers (5,000 skills, 1M invocations, 87% ablation win) as evidence the mechanisms generalize | Rejected | Self-reported single-company outcomes without published data; mechanism transfer requires reproduced local need, not vendor volume |

## Falsifiability

- A reproduced local case where a TeaPrompt skill demonstrably *hurts* task outcomes (measurable with/without difference) would reopen UAS-DOC2/UAS-SK1 with a concrete gap.
- Published Uber methodology (ablation protocol, judge blinding details, papercut precision) would upgrade the supplier-summarized rows; absence keeps them qualified.
- This survey ran no eval, no model call, and no tooling install; it cannot certify Uber's numbers, only that the article claims them.

## Standing Non-Goals

- No runtime, Skill, prompt-body, routing, or governance change.
- No Skill Workshop/aifx install, no eval-harness construction, no model call, no commit or push beyond this record and its catalogue row.
- The Stratechery-sourced "atomic unit is the workflow" framing is quoted context, not adopted TeaPrompt doctrine.
