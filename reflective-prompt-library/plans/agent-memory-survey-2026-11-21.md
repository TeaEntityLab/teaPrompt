# Agent Memory Survey — Which Corrections Carry Forward? (2026-11-21)

Language: English

> **Status:** `AMEM-DOC1` records the research; `AMEM-SK1` clarifies an existing handoff Skill and adds a paired example. No new Skill, memory store or background job.

## Evidence and attribution

[Lance Martin's Anthropic Engineering article](https://www.anthropic.com/research/components-of-agent-memory) (November 6) reports the experiments below. [Xiaogai's reading notes](https://x.com/xiaogaifun/status/2123710596139139286) (November 20) supply the red-to-green preference example and the author's dissatisfaction with personal assistants. Both were checked 2026-11-21. The preference example is not one of Anthropic's experiments.

All three direct replies were checked 2026-11-21: [@taiyanghere](https://x.com/taiyanghere/status/2123799418646241512) and [@Meoyyyb](https://x.com/Meoyyyb/status/2123736216562700421) worry about a wrong preference persisting; [@universe2048](https://x.com/universe2048/status/2123790165886095792) suggests forgetting small tasks and loading larger projects' memories on demand. These are reader judgments, not measured outcomes.

Martin uses *memory* for knowledge gained from experience and available as readable context in a later session, not weight updates, learning within one conversation or context compaction. The four components have different jobs: transcripts record what happened; notes capture potentially reusable observations; a representation such as a wiki connects them; a short index or selected notes enter the next session automatically. Dreaming is an offline pass that can check a note against its source, repair links or move detail out of the injected layer. The sleep analogy describes that division of work, not a required pipeline. A transcript can confirm what someone said without confirming that it is still true or applies to another project.

## What the experiments compared

These are Anthropic's reported results. TeaPrompt did not rerun the benchmarks.

| Comparison | Result | Limit |
| --- | --- | --- |
| Pokémon Red, about 10,000 steps in one run per model (Fig. 4) | Sonnet 3.7 wrote 413 files and earned one badge. Fable 5 wrote nine files in two folders **plus** the top-level `global.md`: ten files, four badges. | Fable recorded strategies rather than state already visible on screen. The comparison changes the model; it does not isolate file count. |
| CL-Bench 1.0 database task, fresh session per question with correct-answer feedback (Figs. 3, 5) | Stateless → memory mean reward: Opus 5, 0.564 → 0.828; Sonnet 4.6, 0.330 → 0.364. Asking Sonnet 4.6 to read its notes and test its guesses raised its score to 0.641. | A failures-only rule reduced the memory gain for Opus 4.7 and Opus 5. The result is not a general case against guidance. |
| Mt. Moon, wrong PokéCenter location (Figs. 6–8) | After the offline pass checked the transcript and corrected the note, the agent re-entered the cave and reached Cerulean City. With the original note it fell off the ledge three times; with no memory it also failed to reach the city. | The later navigation choice distinguishes the runs; a successful note write would not. This is one game situation, not an error-rate estimate. |
| Stainless, about 350,000 files and 420M tokens, 25 questions (Fig. 10) | From 2 to 128 wiki-building sessions: wiki alone **13% → 48%** of graded criteria; search plus wiki **54% → 61%**; search alone **53%**. | The mature wiki adds to search; 13% is not the search baseline or the percentage of whole questions answered correctly. The reported saving of about 20,000 tokens per question is on the answering side, not net of construction or upkeep. |
| Merger questions and Harvey LAB tasks (Figs. 11–12) | On merger items requiring cross-document work or judgment, consulting the wiki scored 87% versus 73% for search. One mostly single-document LAB task showed no clear gain; on another task the wiki outgrew the source files. | Test the retrieval work the user actually needs before maintaining a wiki. |

## Product and retention boundaries

- [Claude Code auto memory](https://code.claude.com/docs/en/memory) (checked 2026-11-21): at startup it reads the first 200 lines or 25 KB of `MEMORY.md`, whichever comes first. Topic files are read on demand. This is an index limit, not a cap on every instruction file or a guarantee the model follows a note.
- [Managed Agents Dreams](https://platform.claude.com/docs/en/managed-agents/dreams) (checked 2026-11-21) is a research preview requiring access. An asynchronous job reads one store and 1–100 selected sessions, then produces a **separate** store. The caller can review, attach or discard it; the input is not overwritten. Jobs incur model token charges. Recheck availability, billing and retention in the product docs before deployment.
- [Managed Agents memory stores](https://platform.claude.com/docs/en/managed-agents/memory) (checked 2026-11-21) are workspace-scoped and versioned. Hosted session transcripts persist until deleted. A model judging an item useful is not consent to retain it, disclose it or use it for another person. Define who can use the source and derived notes, and how each can be corrected or removed.

## Candidate Adoption Ledger

| ID | Decision | What changes |
| --- | --- | --- |
| AMEM-DOC1 | Record and link the comparison | This record and the [memory consolidation prompt](../04-agent/memory-consolidation.md) distinguish historical evidence from the scope of a current preference. |
| AMEM-SK1 | Clarify [Memory Consolidation](../skills/reflective-handoff-retro/SKILL.md#memory-consolidation) in place | The [paired handoff example](../skills/examples/reflective-handoff-retro.examples.md#preference-scope-replay) grades the next poster, not the note. It uses fictional project inputs, not a personal profile. |
| AMEM-RUN1 | Do not adopt a memory runtime | Storage, retention, user isolation and scheduling belong to the host. A preference correction is not authority to promote a note into a project rule; the [artifact promotion gates](../04-agent/artifact-promotion.md) still apply. |

## Falsifiability

The replay fails if a later reader applies a one-poster exception to the next poster or ignores an explicit change of default. If that happens repeatedly, compare search alone against search plus reviewed notes on the same later tasks. Count wrong carry-over and missed corrections, as well as the costs of building, maintaining and querying the notes. The example defines what to check; it does not establish that either method performs better.
