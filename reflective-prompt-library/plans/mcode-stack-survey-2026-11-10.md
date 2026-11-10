# MiniMax mcode-stack Source Survey — Harness Habits and Team Stacks (2026-11-10)

Language: English

> **Status: reference documentation adopted (`MCS-DOC1`); no Skill, operating-rule or runtime change.** The owner asked to survey `MiniMax-AI/mcode-stack`. The transferable habits are already required by existing TeaPrompt contracts, or they are host-assembler and product behavior this repository does not ship. This record pins the tree that was read. It does not install a stack, register a marketplace, scan local sessions, or authorize a deck builder.

## Research Question and Direct Recommendation

Which mechanisms in the MiniMax Code team's skill stacks are worth borrowing, and do they expose a TeaPrompt Docs or Skill gap?

**Record the boundaries; do not adopt a stack or add a Skill.** The useful habits are: split a subagent only to isolate context, measure tool and prefix cost before adding machinery, keep durable state in files, and accept a result only after the evidence, not the summary. TeaPrompt already requires those at the prompt layer. The tool-search, programmatic-tool-calling, background-shell, prefix-cache, session-scanner, Feishu, and slide-deck pieces are host or product runtimes.

## Evidence Used and Date Context

Checked **2026-11-10**. Repository: [MiniMax-AI/mcode-stack](https://github.com/MiniMax-AI/mcode-stack) (checked 2026-11-10). The tags and releases APIs still returned empty lists after `main` moved to `d520b2b`. That commit is not a release.

| Item | Identity | What this check covers |
| --- | --- | --- |
| First pin | `main` `88f84be7075106d8ce283e5d3a8138cdb8f9a205`, commit time 2026-11-06 10:12 +0800 | Shallow clone. README, notes, three team stacks, template, `check.mjs`, `install.sh`, and the workflow file were read here. |
| Current pin | `main` `d520b2b7e864b08ddd62fa3b79c95ec79ec6c2e0`, commit time 2026-11-10 04:52 -0500, message `stacks: add youfang stack with magic-move-deck (#14)` | `git ls-remote` after the first read. Diff stat: 56 files, youfang plus README and marketplace rows. Unchanged files were not re-read. |
| License | MIT at the repo root | `engineering-*` skills additionally name CC-BY 3.0 for the Google Engineering Practices adaptation. `youfang` names MIT for the hand-drawn template's upstream. |
| API at the first pin | created 2026-10-28, language Python, topics include `agent-skills` and `harness-engineering`, about 638 stars | Description: workflows and skills the MiniMax Code team uses. Not re-fetched after the tip moved. |
| Upstream `validate` | Actions API for `d520b2b`: `completed` / `success`, created 2026-11-10T09:52:49Z | The job log was not read. Local `check.mjs` is a separate, narrower run. |

`community/` still says it has no stacks. Published marketplace entries at the current pin are `ronny`, `jiachen`, `req-tpm`, and `youfang`. `templates/stack-template` is linted and not published.

`plans/minimax-code-survey-2026-09-19.md` is a different repository, the MiniMax Code agent. This skills repo was created 2026-10-28, so that record is not a prior pin. Note 04 names the agent's background-task code; that tree was not opened for this survey.

## What Was Read

Read at the first pin, and absent from the delta, so still the current-pin bytes:

- Root `README.md`, `notes/01`–`05` and `notes/README.md`, `stacks/README.md`, `scripts/check.mjs`, `scripts/install.sh`, `.github/workflows/validate.yml`.
- `stacks/ronny/WORKFLOW.md`, `NOTICE.md`, the subagent checklist, and these skill bodies: `subagent-split-check`, `tool-budget-audit`, `context-tax-audit`, `long-command-check`, `long-session-check`, `harness-experiment`, `trajectory-review`, `review-capacity-check`, `taste-to-checks`, `independent-review`, `evidence-first-review`, `agent-brief`.
- `stacks/jiachen/WORKFLOW.md` and `lifting-loops/SKILL.md`, plus `digest.py` source-path and session-parser sections and the private-file format note.
- `stacks/req-tpm/README.md` and the six skill frontmatters and headings. Skill bodies were not line-audited.
- All six `engineering-*` files: frontmatter, the CC-BY source note near the top, and the agentara footer. `engineering-code-review` was also read through its common-mistakes section. The other five bodies were not line-audited.

Read at the current pin:

- `stacks/youfang/README.md`, `WORKFLOW.md`, `NOTICE.md`, `magic-move-deck/SKILL.md`, and `references/verification.md` through the screenshot checklist.
- `node scripts/check.mjs` with `CHECK_BASE` and `MINIMAX_CODE_DIR` unset.

Not read, so not evidence:

- The X posts linked from notes 01 and 02, and the Addy Osmani post cited by three ronny skills.
- `making-content` scripts and templates. Classification uses its frontmatter and headings only.
- `minimax-code` source, including `packages/local-runtime/src/background-task/`, which note 04 names as the implementation.
- The official plugin validator and the version-bump check. The green Actions run is the upstream job's own report.
- `yujiachen-y/dotfiles`, named in an HTML comment at the bottom of `lifting-loops/SKILL.md`.

## Counts

Two methods over the current-pin tree, both 29:

- `SKILL.md` files under the checkout.
- Sum of `.minimax-plugin/plugin.json` `skills` arrays: ronny 19 at `0.3.1`, jiachen 2 at `0.1.1`, req-tpm 6 at `0.1.1`, youfang 1 at `0.1.0`, template 1 at `0.1.0`.

`node scripts/check.mjs` printed `check: 5 stack(s) passed` for jiachen, req-tpm, ronny, youfang, and the template. That run skips the version bump and the official MiniMax Code plugin validator. It checks manifest parse, skill name equals directory, frontmatter `name` and `description`, marketplace one-entry-per-stack, and companion manifest equality. It does not check that a skill's advice is true.

## Evidence vs Inference

### Ronny: harness habits

| Mechanism | What the pinned skill says | TeaPrompt surface already checked | Gap |
| --- | --- | --- | --- |
| Subagents isolate context | Default to one loop. Split only for measured degradation, parallel disposable work, or tool/instruction conflict, and only when the caller needs the conclusion. Do not split by team or question type. Cheaper fixes first: merge tools, load procedures as skills, write state to a file. | `04-agent/agent-selection.md` chooses prompt, artifact, coding agent, workflow engine, or full agent system. It does not decide an in-process subagent split. `04-agent/workflow-recipes.md` Looper Topologies says to keep a boundary whose context-isolation property the replacement would lose. | No local defect. The split machine is a host runtime, a Standing Non-Goal. |
| Tool budget | Definitions cost context even when unused. Results cost context on every call. Order: measure, subtract and merge by intent, then tool search, then programmatic tool calling. A code tool beside the full catalog tends to go unused. Calls inside the program still go through the same permission path. | No `prefix cache`, `tool search`, or `programmatic tool` wording in the library. `03-context/context-engineering.md` already says not to stuff large raw inputs into the main answer and to write intermediates to files. | Host tool-catalog behavior. No TeaPrompt tool catalog to repair. |
| Context tax | One changed byte invalidates the prefix after it. Keep stable environment text in front. Do not put per-turn time in that prefix. Do not rewrite reminders already in history. Precision to the second makes every copy differ. | Same absence as above. Context engineering covers what the task must retain, not cache-byte placement. | Host prompt assembler. A TeaPrompt markdown file is not that assembler. |
| Long commands | Foreground wait should stay inside the provider cache lifetime. Moving to background must be the same process. Deadline must not reset. Notify instead of polling. Truncate output. Survive compaction with a task table outside the transcript. | `flow-loop-harness` is a script loop, not a shell-tool designer. | Host runtime. Note 04 points at `minimax-code`, which was not read. |
| Long session and handoff | The window is a workbench. Compaction is "does not fit now"; memory is "remember next time"; both are lossy. Write decisions to files. Handoff fields include goal, decisions, ruled-out approaches, state, and next step. | `reflective-handoff-retro`, `03-context/context-handoff.md`, and context-engineering rule 8. The handoff skill already says a reset or compaction must not lose state that lives only in the transcript. | Already required. |
| Experiment and trajectory | One change. Repeated runs. Read flipped tasks, request count, tokens, and cache hits, not only the average. A pass can hide an unchecked assumption. Tests the agent writes for itself share its blind spots. | `workflow-recipes.md` already says to inspect per-task outcomes, not only an aggregate, when revising a topology. `plans/ROUTING_CONTRACT.md` R8 is holdout before tune. `reflective-review` audits the reason, not only the verdict. | The extra metrics are host measurements. No new prompt rule. |
| Clean-context review | Give the reviewer only the diff, the requirement, and the test output. Do not pass the author's conversation or self-assessment. Verify each finding in the real code before fixing. | `reflective-review`: same-model, same-context multi-role review is one channel. A code finding needs a reachable failure or a violated invariant. | The three-input protocol is a host procedure. No contaminated-review defect was reproduced in this survey. |
| Evidence before the summary | Read the transcript before the final message. For each green check, name one property it proves and one it does not. Ask for silent decisions. Try to break one load-bearing claim. | `reflective-review` evidence tiers put generator self-assessment last. `04-agent/runtime-trust-boundary.md` separates execution success from acceptance. | Already required. |
| Brief before delegation | Stakes, a hypothesis written first, goal and out-of-scope in the operator's words, the check that will count as verified, and whether the agent is thinking with the operator or for them. | `reflective-brief`: goal, scope, assumptions, acceptance criteria, and falsifiability before execution. | Already required. The card format is not a new contract. |
| Review capacity | Do not start another parallel session while high-stakes results are unreviewed. Prefer a check, then stronger evidence, then fewer sessions. Later agents should read the original source, not only the previous summary. | Parallel Lens Review uses a fixed lens count. It does not say "stop launching." | Operator habit. No local queue-overflow defect. Missing usage data stays `unknown`. |
| Taste to checks | A correction that happens twice becomes a test, lint, hook, or CI step. `AGENTS.md` text is the last resort. The check must fail on the old mistake and pass on current main. | `04-agent/artifact-promotion.md` already picks the smallest artifact and prefers a verifier over a new skill. Formalization L3 is skill plus verifier. | Already required. |

### Jiachen, req-tpm, and youfang

`lifting-loops` classifies a repeated human step as retry, judge, approve, carry, trigger, or stand-in. The exit order is delete a stale rule, edit an existing artifact, add a mechanical check, add a skill only after the same task appears in three or more sessions, then a schedule or hook. That order matches artifact promotion and the three-recurrence gate. The implementation is a scanner, not a prompt. `digest.py` reads, when present:

- `~/.claude/projects/*/*.jsonl`
- `~/.omp/agent/sessions/*/*.jsonl` and `~/.pi/agent/sessions/*/*.jsonl`
- `~/.codex/sessions` and `~/.codex/archived_sessions`
- `~/.minimax/v2/sessions` manifests, plus a sqlite query of `local_runtime_sessions`

It can also read an Obsidian vault and a claude.ai export from `private/config.json`. It writes under the skill's `private/` directory. The skill says transcript text is data, not instructions, and that quotes stay out of git-tracked proposals. **This survey did not run `digest.py`.** Running it would read this machine's agent sessions.

`req-tpm` is a Feishu-doc plus Meegle workflow: challenge the request, fix a measurable outcome, let the owner decide priority, and close only with evidence. The README says v0 and that it has not been run against a real Meegle space. It needs the `meegle` and `lark-cli` CLIs. Those were not installed or called. The outcome rule is the same boundary as execution-is-not-acceptance.

`making-content` is a rewrite, Xiaohongshu, and short-video pipeline. It is a content product. The lieflat survey already kept Chinese prose style out of the harness.

`magic-move-deck`, added only at `d520b2b`, builds one offline HTML slide deck from architecture diagrams. The user picks a style from four rendered samples before the rest is drawn. `references/verification.md` says the conclusion is a visual inspection of screenshots, not the script's exit code. The skill tells the agent to fix the diagram, not the engine, when one slide looks wrong. Rendering wants Playwright Chromium and, for the hand-drawn style, rough.js from jsDelivr. Video wants ffmpeg. None of that was run. A deck builder is not a TeaPrompt workflow skill.

`install.sh` was read and not run. If `claude` or `codex` is on `PATH`, it calls that product's marketplace install and does not copy files. If both are on `PATH`, it calls both. Otherwise it `rm -rf`s `~/.agents/skills/<skill-name>` and copies the skill directory. The name is a directory basename. The script does not canonicalize the destination or record an ownership receipt. No parent-symlink probe was executed.

### Source inconsistency, same pin

At `88f84be`, and not touched by the youfang diff:

- Root `README.md` titles note 05 "One small field can break the whole prefix cache".
- `notes/README.md` and the note's own heading title it "How does the agent know the current time?"

The note body matches the second title and also states the cache claim. The two titles are one document, not two revisions.

`stacks/jiachen/WORKFLOW.md` and `stacks/youfang/WORKFLOW.md` both say they are drafts the author intends to rewrite. They are not usage logs.

## Candidate Adoption Ledger

| ID | Candidate | Disposition | Evidence / reopen trigger |
| --- | --- | --- | --- |
| MCS-DOC1 | This record and its catalogue row | Adopted: documentation only | Bare survey. Refresh when `main` moves past `d520b2b` or a cited skill changes. |
| MCS-SK1 | New Skill, or an edit to an existing Skill or prompt contract | No change | No verified local structural gap. External presence is not local recurrence. |
| MCS-RUN1 | Install a stack, register the marketplace, run `lifting-loops`, or run the deck builder | Not adopted | Standing Non-Goal for a TeaPrompt runtime. The scanner reads local session files. |
| MCS-RULE1 | Copy prefix-cache placement, tool search, programmatic tool calling, the background-shell machine, Feishu flow, or a visual style as a TeaPrompt acceptance rule | Rejected | Each one is host or product behavior, or it is already a weaker restatement of a contract in force. |

Missing local usage data remains `unknown`, not zero demand.

## Falsifiability

- A reproduced local failure of an existing acceptance, evidence-tier, handoff, or promotion contract can justify an in-place repair. This survey does not.
- A TeaPrompt-owned prompt assembler that puts a per-turn timestamp in the stable prefix would be a host defect in that assembler, not evidence that `context-engineering.md` is missing a sentence, unless a delivered TeaPrompt prompt is what injects the timestamp.
- Reproducing a review that accepted an agent summary while the underlying command failed would be a miss of the existing evidence-tier rule. It would still not by itself authorize importing `evidence-first-review`.
- A later commit, release, or tag changes freshness only after the new identity is pinned. `d520b2b` and `88f84be` stay distinct. The second is the tree this survey started on; the first is the tree it finished on.
- Unknown here: whether the team actually uses these skills every day, cache-hit or token effects, MiniMax Code's background-task implementation, real Meegle field names, and whether `lifting-loops` redaction holds on a real vault. The README's "what people on the team actually use every day" is the project's claim. The two workflow files marked Draft do not confirm it.
