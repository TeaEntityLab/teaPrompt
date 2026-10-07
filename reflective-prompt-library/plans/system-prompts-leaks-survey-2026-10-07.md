# System Prompts Leaks Survey & Architectural Rethink (2026-10-07)

> **Status:** Reference-only record. Pinned upstream at `f015440d2c6a5c880e7503d0d17bfad1cd02133f` (`main`, checked 2026-10-07). Evaluated across four parallel lenses (Provenance/Epistemic, Architecture/Taxonomy, Coding Agent Discipline, Safety/Jailbreak Defenses); SPL-1 reference-only, no skill, runtime, schema, or gate change. `06-repo/AGENTS.md`, `04-agent/agent-scaffold-provenance.md`, and the invoked skill contracts remain authoritative.

## Purpose

User instruction: "Survey this and rethink in parallel https://github.com/asgeirtj/system_prompts_leaks" (checked 2026-10-07) followed by "Record your thoughts".

This record evaluates the heterogeneous corpus at `asgeirtj/system_prompts_leaks` against TeaPrompt's nine-core skill architecture, progressive disclosure model, and host-owned trust boundaries. The recorded population is **1,237 file-like entries inside 16 non-hidden top-level directory buckets**, including `Misc`; it is not 1,237 authenticated prompts or 16 verified vendors. A root-inclusive tracked-file tally is 1,245 and counts a different set.

## Candidate Adoption Ledger

| ID | Candidate | Status | Evidence | Reopen trigger / falsifier |
|---|---|---|---|---|
| SPL-1 | System prompts leaks survey (`asgeirtj/system_prompts_leaks` @ `f015440d`): assembled contexts, progressive disclosure, mutating/non-mutating plan classification, prompt secrecy vs architectural trust boundaries | Reference-only (no change) | Pinned directory-bucket population of 1,237 entries (checked 2026-10-07); selected mirrored artifacts inspected; patterns are compatible with existing TeaPrompt compositions, not vendor-runtime or efficacy proof; zero operational prompt text adopted | Reopen if an authenticated upstream mechanism and an exercised local consumer failure demonstrate a structural gap not covered by existing contracts. |

## Architectural Rethink & Findings

### 1. Corpus Scope & Heterogeneous Epistemic Sourcing
The pinned repository combines prompt text and assembled execution-context artifacts from five source classes. Classification describes inspected paths, not independent authentication of every entry:
- **Official-publication mirrors (`Anthropic/official/`):** Files presented as archives of vendor-published prompt articles.
- **Raw captures (`Anthropic/raw/`):** Sample dumps contain message envelopes and personal-context material such as local paths and memory/thread identifiers; no such values are reproduced here.
- **Packaged-tool extractions (`Anthropic/claude-code/`, `OpenAI/Codex/`):** Files presented as prompt strings extracted from CLI bundles; this survey did not reproduce the extraction process.
- **Workspace dumps (`Meta/muse-agent/`):** Files include agent-workspace artifacts such as `SOUL.md`, `HEARTBEAT.md`, and cron configuration.
- **Community reposts (`Misc/`):** Secondhand material whose authenticity remains unverified.

**Licensing and privacy limits:** Upstream's CC0 declaration does not by itself establish the curator's rights over third-party material or permission to reuse personal-context data. This is a provenance risk, not a legal adjudication. TeaPrompt's existing research contract rejects copying leaked or mirrored prompt text into operational prompts; this survey records transferable mechanisms only.

### 2. Architecture & Prompt Taxonomy: Deconstructing the "Megaprompt"
- **File size is not per-turn context size:** Inspected large Codex artifacts combine instructions, tool catalogs, or rollout content; deferred-schema markers appear in the sampled text. Their on-disk size does not establish what a running vendor service injects on any turn.
- **Smaller sampled instruction files:** `Cursor/cursor.md`, `Google/antigravity-cli.md`, and `OpenAI/Codex/gpt-5.6.md` were inspected separately from large assembled dumps. Neither file size nor a mirror's title authenticates the deployed payload.
- **Recurring anatomy in the sample:** Identity/style, environment, tool/file operations, destructive-action gates, planning, and skill discovery recur in the inspected material. A universal ordering or complete vendor census was not established.
- **Progressive-disclosure patterns:** Sampled artifacts describe compact tool/skill catalogs and on-demand loading. This is compatible with TeaPrompt's `SKILL.md` discovery design [INFERENCE]; the survey did not measure attention degradation, token savings, vendor migration causes, or comparative agent quality.

### 3. Coding Agent Discipline & Tool Execution Protocols
- **Described file-editing preconditions:** Sampled Claude Code artifacts describe read-before-edit tool preconditions; Cursor text states a read-before-edit instruction; Codex material describes patch-format rules. These are source-text observations. No vendor CLI or enforcement implementation was exercised in this survey.
- **Recurring workspace expectations:** Inspected examples discourage reverting user changes and unrequested destructive Git operations, and discuss edit discipline and shell outcomes. These are not established as universal rules or independently verified runtime controls.
- **Plan-mode separation:** Inspected Codex `plan_mode.md` distinguishes mutating actions from non-mutating exploration. The distinction is compatible with TeaPrompt's existing Planning Fidelity contract [INFERENCE], not new adoption authority.

### 4. Safety, Refusal & The Extraction Paradox
- **Secrecy wording is conditional in the sample:** The inspected Grok artifact discourages mentioning its guidelines **unless the user explicitly asks for them**. Other sampled files discourage instruction echoing. The survey did not establish that every corpus entry contains a secrecy clause.
- **Publication does not prove extraction:** A public mirror's existence does not establish how each entry was obtained, that it came from a deployed vendor system, or that an adversarial extraction defeated its controls. No universal extraction claim is supported.
- **Described controls versus enforcement:** Sampled Meta material describes a credential vault; Claude Code material describes untrusted-data wrappers. These observations alone do not verify isolation or authorization enforcement.
- **TeaPrompt's boundary:** `agent-governance-scaffold` and `runtime-trust-boundary.md` specify authority splits, capability-token and broker-receipt contracts, and verification expectations. TeaPrompt does not enforce these controls merely by shipping prompt text or generators; the host owns permissions, isolation, effects, and acceptance.

## Evidence vs Inference

### Evidence Actually Checked
- Upstream Git repository [https://github.com/asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) (checked 2026-10-07).
- Git `ls-remote` pin `f015440d2c6a5c880e7503d0d17bfad1cd02133f` (`main`, checked 2026-10-07).
- Immutable corpus: [pinned tree](https://github.com/asgeirtj/system_prompts_leaks/tree/f015440d2c6a5c880e7503d0d17bfad1cd02133f); [sample Grok artifact with its explicit user-request qualifier](https://github.com/asgeirtj/system_prompts_leaks/blob/f015440d2c6a5c880e7503d0d17bfad1cd02133f/xAI/grok-4.7.md#L29) (checked 2026-10-07). These are mirrored artifacts, not authenticated vendor-runtime evidence.
- Corpus count method: for each original non-hidden top-level directory bucket, sum `p.is_file()` over `bucket.rglob("*")`; aggregate 1,237 file-like entries over 16 buckets, including symlink targets treated as files by that method. The root-inclusive `git ls-tree -r --name-only f015440d2c6a5c880e7503d0d17bfad1cd02133f` tally is 1,245. Both observations were recovered from the dated review; they describe different populations (checked 2026-10-07).
- Selected mirrored file contents inspected: `Cursor/cursor.md`, `Google/antigravity-cli.md`, `Anthropic/claude-code/*`, `OpenAI/Codex/*`, `Meta/muse-agent/*`, `xAI/grok-4.7.md`, and `README.md`. Inspection was selective, not an authentication or runtime audit of all corpus entries (checked 2026-10-07).

### Inferences & Claims
- Progressive disclosure is a plausible way to reduce unnecessary context loading, and is compatible with TeaPrompt's existing design [INFERENCE]. Its efficiency and the vendors' reasons for choosing it remain unmeasured here.
- Prompt-level secrecy wording is not sufficient evidence of a security boundary [INFERENCE]. This judgment rests on TeaPrompt's host-enforcement distinction, not on an unperformed universal extraction experiment.
- Source authenticity, deployed vendor behavior, comparative prompting quality, and actual security-control enforcement remain **unknown**. The four-lens review is a review method, not independent experimental confirmation.

### Recording-turn correction

The interrupted parallel review identified unsupported universal/enforcement claims and a dropped Grok qualifier. This recording change narrows those claims and preserves the 1,237 count with its actual population; it does not change SPL-1's reference-only disposition. The observed runtime defects are separately tracked in the [review handoff](recent-changes-review-handoff-2026-10-07.md).

## Falsifiability

This assessment is wrong if:
1. Monolithic prompt architectures without progressive disclosure demonstrate superior multi-task reasoning and token efficiency over composable, tiered skill libraries across reproducible benchmarks.
2. Natural language prompt secrecy directives reliably prevent prompt extraction and indirect prompt injection without requiring out-of-model harness boundaries or architectural parameter isolation.
