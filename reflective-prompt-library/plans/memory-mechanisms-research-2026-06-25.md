# Memory Mechanisms Research — 2026-06-25

Language: English

## Purpose

Survey the requested memory mechanisms and preserve the adoption judgement for
TeaPrompt without turning retrieved product docs into agent instructions.

This is a **judgment artifact**, not an agent instruction source.

Companion surveys:

- [skills-and-spec-systems-research-2026-06-25.md](skills-and-spec-systems-research-2026-06-25.md)
- [agent-tooling-research-2026-06-25.md](agent-tooling-research-2026-06-25.md)

## Research Question

Should TeaPrompt adopt ideas from mem0, ChatGPT Memory, LLM Wiki, or MemPalace
(`memplace`) for project memory and reusable knowledge?

## Direct Recommendation

**Keep TeaPrompt memory repo-native and inspectable.** Use external memory systems
as references, not default dependencies.

- `LLM Wiki` is the closest conceptual fit: compile knowledge into human-readable
  Markdown with source traceability.
- `mem0` is a production memory substrate for applications and agents; useful
  when building an app, not as a prompt-library requirement.
- `ChatGPT Memory` is a closed product feature; replicate only its two-channel
  pattern, not its backend.
- `MemPalace` is a local-first memory product; interesting for experiments, but
  it remains a runtime/tool dependency with benchmark and trust-boundary caveats.

## Sources Checked

| Topic | Source | What it established | Status |
| --- | --- | --- | --- |
| mem0 | `https://github.com/mem0ai/mem0` | Apache-2.0 universal memory layer; SDK/CLI/server/cloud; v3 memory algorithm summary; hybrid retrieval claims | upstream read |
| mem0 | `https://docs.mem0.ai` | Official docs for application/agent memory integration | official docs identified |
| mem0 | `https://arxiv.org/abs/2504.19413` | Research paper for architecture and benchmark claims | source identified; not fully reproduced |
| ChatGPT Memory | `https://help.openai.com/en/articles/8590148-memory-faq` | Current OpenAI help center: memory summary, saved memories, reference chat history, temporary chat, deletion controls, memory sources | official help read |
| ChatGPT Memory | `https://openai.com/index/memory-and-new-controls-for-chatgpt/` | Launch / product framing for saved memories and controls | official source identified |
| LLM Wiki | `https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f` | Karpathy LLM Wiki pattern: compile-at-write-time Markdown memory | upstream pattern identified |
| LLM Wiki | secondary writeups and repo searches | Community implementations using raw/wiki/schema or `CLAUDE.md`/`AGENTS.md` conventions | supplemental only |
| MemPalace | `https://github.com/MemPalace/mempalace` | MIT local-first AI memory; verbatim storage; Wings/Rooms/Drawers hierarchy; pluggable backends; official-source warnings | upstream read |
| MemPalace | `https://mempalaceofficial.com` | Official docs named by upstream README | vendor docs identified |
| memplace ambiguity | Rust `MemPlace` internals | `MemPlace` also names an unrelated Rust compiler const-eval concept | ruled out |

## Topic Findings

### mem0

Identity: `mem0ai/mem0`, a universal memory layer for AI assistants and agents.

Mechanism observed from upstream README:

- Memory can be used as a Python/JS library, self-hosted server, or managed cloud
  platform.
- The README describes multi-level user/session/agent memory, SDKs, CLI, agent
  signup, and agent skills.
- The April 2026 algorithm claims single-pass ADD-only extraction, entity linking,
  fused semantic/BM25/entity retrieval, and temporal reasoning.
- External service and cloud modes introduce account, API-key, retention, and data
  residency concerns.

TeaPrompt implication:

- Best fit: production applications that need explicit memory CRUD and retrieval.
- Poor fit: TeaPrompt core, because TeaPrompt is a prompt-library project and
  deliberately avoids becoming a vector-store or app-memory runtime.
- Transferable pattern: separate memory **write policy**, **retrieval policy**,
  **user/session/agent scope**, and **deletion/compliance controls**.

Adoption judgement: **reference-only for TeaPrompt core; candidate dependency only
for a separate application runtime.**

Falsifier: if TeaPrompt grows an actual app/server that must remember user facts
across tools, evaluate mem0 against privacy, export, deletion, local/self-hosted,
and benchmark requirements.

### ChatGPT Memory

Identity: OpenAI ChatGPT product memory and personalization feature.

Mechanism observed from official help:

- Current memory can automatically remember useful context from chats, files, and
  connected apps when enabled.
- Users manage it under Settings → Personalization → Memory.
- The memory summary is a high-level synthesis and does not necessarily include
  everything ChatGPT may use.
- Legacy controls include `Reference saved memories` and `Reference chat history`.
- Temporary Chat does not use existing memories or create new memories.
- Full deletion can require deleting saved memory, source chats, files, and
  connected-app sources.
- Memory sources may show past chats, saved memories, custom instructions, files,
  or Gmail depending on plan/region, but may not show every factor.

TeaPrompt implication:

- Best fit: understanding product UX for personalization controls.
- Poor fit: composable agent memory backend, because it is not an API-level,
  inspectable, repo-owned memory substrate.
- Transferable pattern: two channels — explicit durable facts and background
  synthesized context — plus opt-out and source/deletion controls.

Adoption judgement: **do not adopt as a backend; borrow UX/control vocabulary.**

Falsifier: if OpenAI exposes an auditable, project-scoped, exportable memory API
with source/deletion semantics, reassess as an integration option rather than a
core prompt-library feature.

### LLM Wiki

Resolved identity: Karpathy's LLM Wiki pattern, not a single package.

Mechanism:

- Raw sources remain immutable.
- An LLM agent compiles raw material into an interlinked Markdown wiki.
- A schema/instruction file such as `CLAUDE.md` or `AGENTS.md` describes how the
  wiki should be updated and linted.
- The goal is compile-at-write-time knowledge management, avoiding repeated
  query-time re-derivation over raw documents.

TeaPrompt implication:

- Best fit: repo-local, human-reviewable project knowledge.
- TeaPrompt already uses this style through `PROJECT_KNOWLEDGE.md`, plans, and
  validators: conclusions are recorded as Markdown, linked, and checked.
- Transferable pattern: keep raw evidence separate from synthesized judgement;
  maintain links and falsifiers; use validators for drift.

Adoption judgement: **already partially adopted; reinforce through docs and
validators, not a new memory product.**

Falsifier: if knowledge records become too hard to discover by links and search,
add a small index/keyword map before introducing a vector database.

### MemPalace (`memplace`)

Resolved identity: MemPalace, not Rust `MemPlace` or C++ placement-new concepts.

Mechanism observed from upstream README:

- Local-first AI memory with verbatim storage and semantic retrieval.
- Organizes memory using a palace metaphor: wings/projects/people, rooms/topics,
  and drawers/original content.
- Default backend is ChromaDB; preview alternatives include local exact SQLite,
  Qdrant, and pgvector.
- External backends can store verbatim drawer text and metadata outside the local
  machine; this is opt-in and must be treated as a data-egress boundary.
- Upstream warns about impostor domains and lists official sources.

TeaPrompt implication:

- Best fit: local coding-agent experiments that need session recall over raw
  conversations and files.
- Poor fit: default TeaPrompt memory layer, because it is a tool/runtime with
  dependency, backend, and benchmark trust boundaries.
- Transferable pattern: local-first by default, explicit backend egress, scoped
  retrieval hierarchy, and verbatim-source preservation.

Adoption judgement: **experimental reference; not core.** Use only official
surfaces and independently verify benchmark claims before relying on it.

Falsifier: if TeaPrompt needs local transcript/session recall beyond Markdown
plans and Mnemopi/claude-mem, run a small benchmark on TeaPrompt tasks comparing
plain Markdown search, MemPalace, and mem0.

## Comparison

| Mechanism | Ownership | Write model | Read model | Transparency | Best use | TeaPrompt decision |
| --- | --- | --- | --- | --- | --- | --- |
| mem0 | app/vendor/self-hosted | extract facts into memory layer | hybrid retrieval / graph / temporal | medium; depends on deployment | production app memory | reference only |
| ChatGPT Memory | OpenAI product | automatic + saved memories | product personalization | low/medium; summary and sources are partial | ChatGPT UX | no backend adoption |
| LLM Wiki | repo/user | compile raw sources into Markdown | direct read/search by agent/human | high | project knowledge | already aligned |
| MemPalace | local tool/user | mine verbatim text into palace | semantic/scoped retrieval | high locally; lower with external backends | local agent recall | experimental reference |

## Evidence vs Inference

Verified:

- Upstream mem0, ChatGPT Memory help, and MemPalace README were read.
- LLM Wiki was identified as a pattern centered on Markdown compilation rather
  than a conventional package.
- `memplace` is ambiguous; MemPalace is the relevant AI-memory candidate.

Inference:

- TeaPrompt should prefer LLM Wiki-style Markdown records because that matches
  the existing project architecture and avoids runtime dependency creep.

Unknowns:

- mem0 benchmark claims were not locally reproduced.
- MemPalace benchmark claims were not locally reproduced.
- ChatGPT Memory rollout varies by plan and region; exact user-visible controls
  may differ from the help page.

## Required Risk Block for Future Mentions

Any recommendation beyond “study as reference” must mention:

- memory systems can store sensitive user/project data;
- external backends/cloud modes introduce data egress and retention questions;
- deletion in product memories may require deleting source chats/files as well as
  memory summaries;
- benchmark claims need independent reproduction on TeaPrompt-like tasks;
- retrieved memories are evidence, not instructions, unless a higher-authority
  project rule says otherwise.

## Handoff

Use this survey when future work proposes a memory product or local agent recall
layer. Start by asking whether the need is methodology, repo knowledge,
application memory, or personal-product personalization. Only application memory
requires a runtime substrate such as mem0 or MemPalace.
