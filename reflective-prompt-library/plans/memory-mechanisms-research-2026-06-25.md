# Memory Mechanisms Research — 2026-06-25

Language: English

> **Refresh pointer (2026-10-22):** mem0 main `2c81af3` (SDK 2.2.1, unpinned prior survey → current-only + notable delta); MemPalace `develop` `f41e8e7` / release 3.12.0; Karpathy LLM Wiki gist current-only (`ac46de1`, sole commit 2026-04-04, no later recorded history, no prior pin to diff); ChatGPT Memory help page substantially expanded. Details in `## Latest-version refresh — 2026-10-22` below; adoption judgments unchanged.

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

## Latest-version refresh — 2026-10-22

Source-only refresh; no benchmarks reproduced, no installs. The 2026-06-25 survey was unpinned (no commit SHAs), so prior baselines are "read, date only" and this refresh is current-state evidence plus notable change-family deltas — no invented exact diffs against a prior pin.

### mem0 (`mem0ai/mem0`, default branch `main`)

- **Prior baseline:** unpinned upstream read 2026-06-25 (April 2026 v3 algorithm summary, ADD-only extraction, hybrid retrieval claims).
- **Latest checked:** main `2c81af3bbe27d9bccb09c772d583df9e9be72ee5` (2026-10-20, `docs(platform): rewrite the BYOK page as a feature guide (#7661)`); latest SDK tag **v2.2.1** (`94c3fe9`, 2026-09-25, Python SDK 2.2.1 / TS SDK 3.3.1; `pyproject.toml` version `2.2.1` at HEAD), with v2.2.0 and v2.1.0 in between. No `v3.x` git tag observed — "v3" remains the memory-algorithm generation name in README/docs, not a release tag.
- **Meaningful changes since June (commit-message + README inspection):**
  - OSS/Platform split sharpened: `docs: frame graph memory as a Platform feature, removed from OSS (#6808)` and `docs: redirect deprecated OSS graph memory page to platform graph memory (#6914)` (both 2026-08); `chore: remove OpenMemory from the monorepo (#6530)`. The self-hosted/OSS surface is narrower than at survey time; graph memory is now a Platform-only story per docs.
  - New `feat(profiles): User Profiles v1 — SDK methods + docs (#7340)` (2026-09-24); `feat(sdk, docs): expose agent_custom_instructions for agent-scoped extraction (#6809)`; `feat(cli): version subcommand`, `--filter` JSON shape; integrations: Hermes plugin, Strands MemoryStore, DeepSeek Harness plugin, Kimi Code plugin, Sidekick exclusivity to Claude Code.
  - Privacy/security-adjacent fixes: `fix(vector-store): stop writing service account private key to DEBUG logs in GoogleMatchingEngine (#7506)`; `fix(client): reject empty entity IDs and filters in add and delete_all (#7581)`; `fix(ts-oss): stop add() from mutating the caller's filters object (#6797)`; `fix(oss): stop ConfigManager from injecting OpenAI's baseURL and model into other providers (#7350)`; telemetry attribution/consistency repairs (#7322–#7326, #7358); Vanta/Dependabot vulnerability sweeps (#7280, #7510, #7528). Self-hosted auth is on by default per README (upgrade notes cited).
  - README still claims single-pass ADD-only extraction, entity linking, fused semantic/BM25/entity retrieval, temporal reasoning, and 92.5 on LoCoMo (+21), with an open-sourced evaluation framework link. Benchmark claims still not locally reproduced.
- **Effect on prior findings:** Reference-only judgment unchanged. The OSS narrowing (graph memory → Platform, OpenMemory removed) strengthens the "candidate dependency only for a separate application runtime" framing: integrators must now check which surface (Library / self-hosted / Cloud) carries the feature they need. The transferable pattern (separate write/retrieval/scope/deletion policies) still holds; deletion-semantics detail remains a docs-level unknown.
- **Inspected:** `git ls-remote` symref/tags, `git fetch --depth 200` main log, HEAD `README.md`/`pyproject.toml`; immutable: [HEAD](https://github.com/mem0ai/mem0/commit/2c81af3bbe27d9bccb09c772d583df9e9be72ee5), [v2.2.1](https://github.com/mem0ai/mem0/releases/tag/v2.2.1).

### MemPalace (`MemPalace/mempalace`, default branch `develop`)

- **Prior baseline:** unpinned upstream read 2026-06-25 (local-first, Wings/Rooms/Drawers, ChromaDB default, impostor-domain warnings).
- **Latest checked:** default branch `develop` `f41e8e75ddaadf5588d5127715fa531d79eadb45` (2026-10-20, merge #2866 revision-import fixes); `main` at `602d796c699cabba2971982cd9dccbbf46abfe79` (2026-10-13, post-3.11.0 sync). Release lineage per CHANGELOG: **3.12.0 (2026-10-18)** > 3.11.0 (2026-10-12) > 3.10.0 (2026-09-15) > 3.9.0 (2026-08-31, last git tag `d5250c7`) > 3.8.0 > 3.7.x; note no git tags observed after v3.9.0 — 3.10–3.12 are CHANGELOG/`develop`-line releases, not `refs/tags/`.
- **Meaningful changes since June (CHANGELOG + commit inspection, privacy/truth-maintenance relevant):**
  - **Local-first hardened (3.11.0):** `EntityRegistry.research()`/`confirm_research()` Wikipedia lookups **removed** — the only potential third-party call without a user-configured endpoint is gone, so local-first is now a code property, not a default. Consent-gate hardening: external-LLM gate judges IPs not hostname prefixes; `closet_llm` reads namespaced `MEMPALACE_LLM_*` env vars instead of generic `LLM_*` (3.12.0); endpoint credentials masked in embedding/LLM errors (#2857/#2858).
  - **Trust boundary (3.12.0):** loopback HTTP MCP hub needs no token; any network-reachable bind requires a token (`0600` file, never printed), refuses proxy headers and DNS-rebound hosts; MCP tool args schema-validated pre-run (`-32602`); hook wrappers no longer import `mempalace` from the project CWD. External backends remain opt-in egress as surveyed.
  - **Provenance/verbatim:** conversation mining no longer discards text (exchange chunker fix, 3.11.0; one-time re-mine upgrade note); user turns stored as written, not spell-corrected (3.12.0); lossy parse steps stamped in `transforms`; search hits return `filed_at`/`authored_at_source`/`content_date` + source; drawer timestamps now UTC instants (naive legacy values read as local time); one-wing-per-project slug rule; `kg import-legacy` with conflict reporting.
  - **Retrieval/architecture:** 3-tool `mempalace-light-mcp` + Palace Query Language; optional native Rust exact-vector acceleration; NumPy top-k; read-only searches open collections `read_only` (no writer-lease contention); `shared-brain` `host:harness:project` identities; XDG config on new installs; Python 3.10+ required.
  - Impostor-domain warning still present in README (GitHub + PyPI + mempalaceofficial.com as only official sources).
- **Effect on prior findings:** Experimental-reference judgment unchanged. The local-first removal of the Wikipedia path and the token/egress hardening are positive for the trust-boundary caveat but do not change the "runtime/tool dependency" classification; benchmark claims still independently unverified.
- **Inspected:** `git ls-remote --symref` (default = `develop`), `develop`/`main` fetch logs, CHANGELOG at both tips, HEAD README warning; immutable: [develop HEAD](https://github.com/MemPalace/mempalace/commit/f41e8e75ddaadf5588d5127715fa531d79eadb45), [main HEAD](https://github.com/MemPalace/mempalace/commit/602d796c699cabba2971982cd9dccbbf46abfe79).

### LLM Wiki (Karpathy gist `442a6bf555914893e9891c11519de94f`)

- **Prior baseline:** pattern identified 2026-06-25, no revision recorded.
- **Latest checked:** gist `master` `ac46de1ad27f92b28ac95459c782c07f6b8c964a` (2026-04-04, sole commit, "idea file" `llm-wiki.md`, 75 lines, sha256 `dc3efe98…37401`). **Current-only** — the sole commit predates the survey so no later recorded history exists, but the 2026-06-25 survey recorded no revision and retained no gist text to byte-compare, so no byte-equality claim is made. The compile-at-write-time Markdown wiki framing matches the surveyed pattern description (persistent compounding artifact, Obsidian-as-IDE workflow) at the paraphrase tier, not a text-diff tier.
- **Effect on prior findings:** None; "already partially adopted" judgment unchanged.
- **Inspected:** gist git fetch + file read; immutable: <https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f> (GitHub REST gist endpoint returned HTTP 502 during this refresh; identity established via git protocol instead).

### ChatGPT Memory (OpenAI help center)

- **Prior baseline:** help article read 2026-06-25 (`8590148-memory-faq`).
- **Latest checked:** same article ID, now titled **"Memory in ChatGPT"** (`8590148-memory-in-chatgpt`), page stamped "Updated: 2 hours ago" at read time 2026-10-22. Substantially expanded vs the surveyed summary.
- **Meaningful changes in documented behavior/controls:**
  - **Improved Memory vs legacy saved memories** is now an explicit switchable experience (Settings → Personalization → Memory → Saved memories / Try improved memory); improved memory continually updates a broader summary while legacy keeps an explicit item list.
  - **Regulated workspaces:** improved memory disabled by default in ChatGPT for Healthcare / Enterprise Regulated Workspace; admin-gated; explicitly **not covered under BAA** (PHI guidance); **Project-only memory** scopes references within one project.
  - **Reference chat history off → deletion scheduled within 30 days** from OpenAI systems (chats themselves remain); **Reference saved memories off also turns off Reference chat history**.
  - **Temporary chat** now offers a pre-start personalization choice (Unpersonalized option); temporary chats never create/update memories; saving converts to regular chat with account settings applying.
  - **Locked chats** can use regular Memory but do not personalize regular chats; prior remembered info survives locking.
  - **Memory Sources** shown under responses; deletion may require removing summary + saved memories + regular/archived chats + Library files + connected apps; OpenAI may retain logs of deleted saved memories up to 30 days; safety/security context use is explicitly separate from personalization controls.
- **Effect on prior findings:** No-backend-adoption judgment unchanged — still a closed product feature, not an inspectable substrate. The two-channel pattern (explicit facts + synthesized context) persists and is now joined by a documented improved/legacy switch, project scoping, and 30-day reference-history deletion semantics worth borrowing as control vocabulary.
- **Inspected:** full help article read 2026-10-22 (canonical URL above); launch post `openai.com/index/memory-and-new-controls-for-chatgpt/` not re-read (framing source, unchanged role).

**Untested limits (all four):** no installs, no benchmark reproductions, no API/runtime verification; mem0/MemPalace deltas are commit-message + README/CHANGELOG tier (author reports), LLM Wiki is byte-verified current-only, ChatGPT Memory is official-docs tier. GitHub REST was rate-limited, so release/tag identities came from `git ls-remote` + fetched CHANGELOGs.
