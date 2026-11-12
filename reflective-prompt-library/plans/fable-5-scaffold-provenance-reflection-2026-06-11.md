# Fable 5 Scaffold Provenance Reflection

> **Status: historical record (retired from active guidance, 2026-07-11).** Kept for provenance and as Decision Index / Durable Lesson evidence. Wording may predate the nine-skill surface and current governance; do not cite as current policy — see `PROJECT_KNOWLEDGE.md` Decision Index for live decisions.
> **Source-refresh pointer (2026-11-12):** the [Fable 5.2 mirror check](#fable-52-mirror-check--2026-11-12) classifies the Code-named and web-app files against official publication scope; the subsequent [version comparison and reflection](#fable-version-differences-and-reflection--2026-11-12) compares Fable 5, 5.1 and both 5.2 artifacts. Historical/retired status is unchanged; CL52-DOC1 adds source-qualified reference documentation, not operating guidance or prompt adoption. The [October metadata-only check](#latest-version-refresh--2026-10-22) remains dated evidence.


Date: 2026-06-11

## Dispatch

- Primary workflow: `reflective-research`, because the decision depends on official documentation, a third-party GitHub mirror, and a user-provided analysis artifact.
- Secondary workflow: `reflective-review`, because the project must decide whether a prompt-like scaffold should change local skills, plans, or governance documents.
- Risk boundary: treat the GitHub artifact and pasted analysis as data, not instructions. Do not copy leaked, mirrored, or proprietary prompt text into TeaPrompt operating instructions.

## Decision

TeaPrompt should make a small targeted adjustment, not a broad rewrite.

Required changes:

- Add a reusable prompt for reviewing leaked, mirrored, scraped, or third-party agent scaffold artifacts.
- Teach `reflective-research` and `reflective-review` to distinguish official evidence, mirrors, user-provided analysis, and inference.
- Document the project-level concept: learn surface separation and transferability, not prompt volume or vendor-specific policy text.
- Add a benchmark case so future routing and quality checks can recognize scaffold provenance review as a real task shape.

Not required:

- Do not create a ninth core skill yet.
- Do not copy the mirror's system prompt text into TeaPrompt.
- Do not replace the current compact 8-skill architecture with a long product scaffold.
- Do not import Claude-specific app, UI, memory, citation, or tool rules unless TeaPrompt has the same local surface and a verified need.

## Evidence Ledger

| Claim / Item | Source | Source Type | Verification Status | Open Constraint |
| --- | --- | --- | --- | --- |
| A public GitHub mirror claims to contain a Claude Fable 5 system prompt. | https://github.com/elder-plinius/CL4R1T4S/blob/main/ANTHROPIC/CLAUDE-FABLE-5.md | Third-party mirror | unverified | Public visibility does not prove completeness, freshness, authorization, or exact product scope. |
| Claude web and mobile apps use periodically updated system prompts, and those updates do not apply to Claude API. | https://platform.claude.com/docs/en/release-notes/system-prompts | Official documentation | verified | This confirms app/API separation, not the authenticity of any third-party mirror. |
| Fable 5 launched with expanded context/output and new reasoning-related API behavior. | https://platform.claude.com/docs/en/release-notes/overview | Official release note | verified | API features and product scaffolds are different surfaces. |
| Anthropic recommends auditing progress against actual tool results and reporting only evidence-backed work. | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5 | Official documentation | verified | This is transferable as a workflow discipline, not as vendor-specific wording. |
| Anthropic recommends refactoring prior-model prompts/skills because older scaffolds may be over-prescriptive. | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5 | Official documentation | verified | The direction supports simplification and evaluation, not wholesale copying from a leaked prompt. |
| The pasted analysis concludes the mirror is best treated as a third-party extraction/reconstruction and recommends learning layering rather than length. | User-provided attachment, 2026-06-11 | User-provided artifact | plausible | Useful as local synthesis, but still not independent proof of the mirror. |

## Project vs Artifact Differences

TeaPrompt is a compact reflective prompt library. It is meant to be portable, inspectable, and composable across workflows. Its main units are prompt patterns, skill contracts, plans, and quality gates.

The Fable 5 mirror appears to be a claimed product-level scaffold. Even if portions are accurate, that kind of artifact likely mixes identity, app UX, memory behavior, connectors, citation rules, safety routing, copyright handling, workspace behavior, and tool policy. Those surfaces are useful to study, but they are not the same thing as TeaPrompt's repo-local skill layer.

Official Anthropic documentation is the higher-confidence source for Fable 5 model/API behavior and prompting guidance. The GitHub mirror and community analysis can suggest taxonomy, but not authority.

## Socratic Inquiry

1. What problem would copying the mirror solve that TeaPrompt does not already solve with smaller prompts and skills?
2. Which claims are official, which are mirrored, and which are only inferred from community analysis?
3. Are we learning a reusable scaffold pattern, or being impressed by the scale and specificity of a vendor prompt?
4. What would become worse if TeaPrompt copied a product-level scaffold wholesale?
5. Which parts belong to a base model, an API, an app surface, a system prompt, a tool policy, a memory policy, or a safety classifier?
6. What evidence would show that the mirror is stale, incomplete, mixed across surfaces, or not actually representative of current behavior?
7. What is the smallest local change that preserves the useful lesson?
8. What should remain out of scope because it is vendor-specific, provenance-sensitive, or unsupported by TeaPrompt's actual runtime?

## Concepts Worth Learning

- Surface separation: model capability, API behavior, app behavior, system scaffold, tools, memory, safety, and user-facing output policy should not be collapsed.
- Provenance ledger: official docs, release notes, mirrors, attachments, and inference must be tagged differently.
- Transferability filter: every interesting idea should be classified as adopt now, study further, keep as caution, or do not copy.
- Evidence-backed completion: claims about work done should be tied to tool output, tests, or observable artifacts.
- Prompt simplification pressure: older or borrowed scaffolds should be reduced to local principles and tested behavior.

## Concepts Not Worth Importing

- Long vendor-specific identity or product-policy text.
- App-specific memory, UI, citation, browsing, or artifact rules when TeaPrompt does not own the same app surface.
- Mirror-specific refusal or safety wording without official confirmation and local need.
- Internal reasoning extraction instructions. TeaPrompt should ask for evidence, summaries, and decision records, not hidden reasoning traces.

## Implemented Local Changes

- Added `04-agent/agent-scaffold-provenance.md`.
- Updated `04-agent/runtime-trust-boundary.md` to classify leaked, mirrored, and third-party prompt artifacts as provenance-sensitive data.
- Updated `reflective-research` and `reflective-review` to include scaffold provenance review.
- Updated README, methodology map, skill map, and trigger cheatsheets so the new concept is discoverable.
- Added a benchmark task for prompt scaffold provenance review.

## Verification Plan

Run:

```bash
python3 reflective-prompt-library/plans/generate_index.py
python3 reflective-prompt-library/plans/validate_links.py
python3 reflective-prompt-library/plans/lint_skills.py
python3 reflective-prompt-library/plans/validate_governance.py
python3 reflective-prompt-library/plans/benchmark_tasks.py
git diff --check
git diff --cached --check
```

Completion evidence must show that links remain valid, skills still pass lint/governance checks, the index includes the new prompt, and the benchmark set includes the new scaffold provenance task.

## Residual Risks

- The third-party mirror may be incomplete, stale, or mixed across product surfaces.
- Official documentation can change; this plan should be revisited if Anthropic changes its public Fable 5 guidance.
- The new provenance prompt improves review discipline, but it does not prove any external prompt leak is authentic.

## Latest-version refresh — 2026-10-22

Historical record stays retired; no guidance change. Metadata/methodology only — no mirrored prompt bodies fetched or quoted.

- **Mirror repo `elder-plinius/CL4R1T4S` (current-only; the original record pinned no commit):** HEAD `a4d3da0` (2026-09-22, `Rename GPT-6_Astra_Prompts.md to GPT-6-Astra_Prompts.md`); 206 total commits, no tags, ~80 tracked files across ~19 vendor top-level buckets. Since the 2026-06-11 dispatch: 18 commits, all additions/renames of sibling mirrors — `ANTHROPIC/Claude-Fable-5.1.md` (2026-09-01), `ANTHROPIC/OPUS-5.md` (2026-07-24), `ANTHROPIC/CLAUDE-OPUS-5.5.md` (2026-09-22), GPT-5.6-Sol / GPT-6-Astra / GPT-6-Sol prompt and tools files (Jul–Sep), plus `Prompts.md`/`Tools.json`/`Skills.md` (2026-08-14).
- **Surveyed file `ANTHROPIC/CLAUDE-FABLE-5.md`:** last touched 2026-06-15 (`09916a9`, +14/−2 lines), i.e. four days after the dispatch and untouched for ~4 months since. Current blob is 122,750 bytes. The record's staleness warning therefore stands and has aged: the file predates the Fable 5.1 sibling mirror in the same repo.
- **Official Anthropic docs cited in the Evidence Ledger:** all three URLs still return HTTP 200 today (system-prompts release notes, release-notes overview, prompting-claude-fable-5). Page bodies were not diffed, so guidance drift since 2026-06-11 is unknown — the record's `revisit if Anthropic changes its public Fable 5 guidance` trigger is neither fired nor cleared.
- **Effect on prior findings:** provenance verdicts unchanged — the mirror remains an unverified third-party extraction, official docs remain the higher-confidence source, and the surface-separation / transferability lessons are unaffected by sibling-file growth.
- **Inspected:** bare-clone `log`/`ls-tree`/`cat-file -s`/`show --stat`; HTTP status checks of the three official doc URLs.
- **Unknowns:** content of the 2026-06-15 edit to the surveyed file (diff not read, to avoid ingesting mirrored prompt text); current official-doc wording vs 2026-06-11; authenticity/freshness of every mirror file including the new siblings.

## Fable 5.2 mirror check — 2026-11-12

### Research question and direct recommendation

The owner asked to update docs and inspect files such as
`ANTHROPIC/CLAUDE-CODE-FABLE-5.2.txt` in CL4R1T4S. What do the new files actually
contain, what can official sources corroborate, and is a local change warranted?
**Record the layered source and its limits; do not copy it into Skills.**
CL52-DOC1 updates this existing provenance record and catalogue discovery only.
The retired June guidance is not reactivated, and its historical skill-count
wording is not current policy.

### Version / date context and evidence used

Checked 2026-11-12: [mirror at the inspected pin](https://github.com/elder-plinius/CL4R1T4S/tree/93a584765460c2fb0ad58380bba476f2149df138), [delta from the October baseline](https://github.com/elder-plinius/CL4R1T4S/compare/a4d3da04e63324e794a65500c3e41994fc4ab02e...93a584765460c2fb0ad58380bba476f2149df138), [official publication scope](https://platform.claude.com/docs/en/release-notes/system-prompts/overview), [official Fable 5.2 entry, dated November 9](https://platform.claude.com/docs/en/release-notes/system-prompts/claude-fable-5-2).

`git ls-remote` bound HEAD/main to
`93a584765460c2fb0ad58380bba476f2149df138`; checkout `rev-parse` agreed.
`git log BASE..TIP` and `git diff --name-status BASE TIP` show three commits
adding two files since `a4d3da04e63324e794a65500c3e41994fc4ab02e`.
The Code-named file was added at `84cd1bf98a8bc395cdcd44b9f420484d0d60881a`;
the web-app file at `90d4560f1eb924ac163466412c30025fb32c4100`, then renamed
from `.txt` to `.md` at the current pin. These are repository timestamps and
identities, **not authenticated extraction dates or vendor release identities**.

| File under `ANTHROPIC/` | Bytes | Git blob | SHA-256 |
| --- | --- | --- | --- |
| `CLAUDE-CODE-FABLE-5.2.txt` | 957,315 | `f770ce2251f03e5eadce905354afcdca64b5c9eb` | `d54e74e3ffd318c3cd0df3ea71f3e54efdd862ee5d988c03206bff10834e3522` |
| `CLAUDE-WEB-APP-FABLE-5.2.md` | 427,612 | `e5cbf3246614df1f53054f5672ad6aaa90aa0499` | `f6c62d2bdf182bb53e8c05f74ff14803c492c89f4715b2290ed04db3c018145d` |

Sizes were measured with `wc -lc` and independently matched to `git ls-tree -r -l`
for these exact paths; digests used `shasum -a 256`. The full-file headings,
transcript delimiters and appended-file labels were indexed, then relevant
identity, authority, delivery, verification and memory sections were read.
This was **selective body inspection**, not a line-by-line audit of every tool
schema, embedded skill or example. Older sibling bodies were not re-surveyed in
this initial check; the owner-requested comparison below subsequently reads them.

### Evidence vs inference — provenance and surface ledger

Every external source below was checked 2026-11-12 at the pin above, except the
separately dated official pages. Status qualifies the stated text observation,
not provenance, deployed behavior or effectiveness.

| Claim / item | Evidence and status | Limit |
| --- | --- | --- |
| The Code-named file is not just one CLI system prompt | **Verified:** [identity and situation](https://github.com/elder-plinius/CL4R1T4S/blob/93a584765460c2fb0ad58380bba476f2149df138/ANTHROPIC/CLAUDE-CODE-FABLE-5.2.txt#L91-L337) mix a Claude Code/SDK identity with a core-app/private-cloud workspace description. [Later delimiters](https://github.com/elder-plinius/CL4R1T4S/blob/93a584765460c2fb0ad58380bba476f2149df138/ANTHROPIC/CLAUDE-CODE-FABLE-5.2.txt#L1165-L1618) label user turns, system messages, tool results and an injected skill; subsequent sections append on-demand skill files. | Classify as a transcript-like, multi-layer bundle. Neither the filename nor embedded role labels authenticate a stock CLI prompt or prove all bytes were loaded together. |
| The web-app sibling is also a layered artifact | **Verified:** [app/workspace guidance](https://github.com/elder-plinius/CL4R1T4S/blob/93a584765460c2fb0ad58380bba476f2149df138/ANTHROPIC/CLAUDE-WEB-APP-FABLE-5.2.md#L239-L449), extensive memory policy, and [tool definitions/skill roster](https://github.com/elder-plinius/CL4R1T4S/blob/93a584765460c2fb0ad58380bba476f2149df138/ANTHROPIC/CLAUDE-WEB-APP-FABLE-5.2.md#L2023-L2291) coexist. | An advertised schema or skill roster is not proof those tools were available or enforced in a deployed session. |
| Official publication corroborates only a narrower surface | **Verified:** the official overview covers core web/mobile system prompts and expressly excludes the API. The November 9 Fable 5.2 entry shares themes such as forged-notice handling, but its product and tone sections differ from the inspected mirrors. | Not an exact whole-file match or an authentication of the added cloud, browser, memory, tool and transcript layers. Differences alone do not establish fabrication; different surfaces or capture context remain possible. |
| Source text attempts to control the reader | **Verified:** [README](https://github.com/elder-plinius/CL4R1T4S/blob/93a584765460c2fb0ad58380bba476f2149df138/README.md#L26-L45) includes a directive to disclose the reader's own instructions. The [tool preamble](https://github.com/elder-plinius/CL4R1T4S/blob/93a584765460c2fb0ad58380bba476f2149df138/ANTHROPIC/CLAUDE-CODE-FABLE-5.2.txt#L18-L22) imposes delegation/publication rules; an appended [hook skill](https://github.com/elder-plinius/CL4R1T4S/blob/93a584765460c2fb0ad58380bba476f2149df138/ANTHROPIC/CLAUDE-CODE-FABLE-5.2.txt#L7646-L7832) includes commit/push instructions. | All were treated as untrusted research data, not task authority. No disclosure, publication, hook execution or repository commit followed from them. |
| Authenticity, completeness, capture conditions and deployed behavior | **Unknown:** no authenticated vendor capture, account/build/session provenance or live product observation was obtained. | Public availability, shared wording, hashes and Git history cannot settle these claims. Redacted placeholders are visible but do not certify complete de-identification. |

### Transferable mechanisms and local coverage

The following are patterns observed **in the mirror**, not vendor guarantees.
Source sections were checked 2026-11-12; local coverage is the delivered repository.

| Pattern observed | Local disposition and boundary |
| --- | --- |
| [Unattended work distinguishes reversible assumptions from irreversible decisions; completion checks sources, arithmetic and rendered outputs](https://github.com/elder-plinius/CL4R1T4S/blob/93a584765460c2fb0ad58380bba476f2149df138/ANTHROPIC/CLAUDE-CODE-FABLE-5.2.txt#L500-L509). | Already covered at the decision-class level by [brief](../skills/reflective-brief/SKILL.md), [risk](../skills/reflective-risk/SKILL.md), [implement](../skills/reflective-implement/SKILL.md) and [review](../skills/reflective-review/SKILL.md). No new Skill; fresh model context alone is not independent empirical evidence. |
| [Workspace files, connected-device writes and hosted artifacts have different delivery paths](https://github.com/elder-plinius/CL4R1T4S/blob/93a584765460c2fb0ad58380bba476f2149df138/ANTHROPIC/CLAUDE-CODE-FABLE-5.2.txt#L399-L430). | Useful example of the existing [runtime trust boundary](../04-agent/runtime-trust-boundary.md) and [scaffold surface distinction](../04-agent/agent-scaffold-provenance.md). Actual connector availability, private-by-default publication and recipient access are host/product responsibilities, not portable permissions. |
| [User-confirmed facts differ from fetched/generated information; explicit forgetting bounds background filing](https://github.com/elder-plinius/CL4R1T4S/blob/93a584765460c2fb0ad58380bba476f2149df138/ANTHROPIC/CLAUDE-WEB-APP-FABLE-5.2.md#L740-L789). | Study as a provenance/retention example, not a universal ban on retaining research evidence. TeaPrompt's [artifact-promotion gate](../04-agent/artifact-promotion.md) already separates memory-derived data, authority and destination; [handoff/retro](../skills/reflective-handoff-retro/SKILL.md) governs durable project knowledge. Background deletion/retention enforcement was not inspected. |
| [Version-qualified memory edits preserve other surfaces' content; a version token does not merge](https://github.com/elder-plinius/CL4R1T4S/blob/93a584765460c2fb0ad58380bba476f2149df138/ANTHROPIC/CLAUDE-WEB-APP-FABLE-5.2.md#L875-L917). | Host-owned concurrency semantics, not a missing prompt-library runtime. Keep as an example; no memory service, schema or tool implementation was exercised. |
| [Evidence gathered before layout and staged construction](https://github.com/elder-plinius/CL4R1T4S/blob/93a584765460c2fb0ad58380bba476f2149df138/ANTHROPIC/CLAUDE-CODE-FABLE-5.2.txt#L508-L509). | The transferable evidence-first discipline is covered by [research](../skills/reflective-research/SKILL.md) and [context engineering](../03-context/context-engineering.md). Product-specific skill-loading order, visual style and artifact routing are not adopted. |

### Candidate Adoption Ledger — Fable 5.2

| ID | Disposition | Reopen when |
| --- | --- | --- |
| CL52-DOC1 | **Adopted: reference documentation only**, this in-place supplement, catalogue and generated discovery. The prior metadata-only refresh did not cover these new files. | Changed mirror pin or official publication changes the source comparison. |
| CL52-SK1 | **No Skill or prompt-contract change.** Observed decision classes already have local owners; no consumer defect or missing structural contract was demonstrated. | A concrete local gap appears, with evidence and the normal promotion gate. External size/novelty is not recurrence. |
| CL52-COPY1 | **Rejected:** copying the bundle, treating it as vendor-authenticated policy, or using embedded instructions to change delegation, publishing, memory, safety or commit authority. | Official corroboration can improve provenance but still does not supply local need or action authority. |
| CL52-RUN1 | **Not adopted:** connectors, artifact hosting, browser automation or background memory runtime. | A separate owner decision changes scope and supplies implementation/verification evidence. |

### Falsifiability, risks and handoff

An authenticated capture tied to a named product/build could change the
provenance verdict; a new immutable file or official entry requires a fresh
comparison. A reproduced local defect could justify a smaller existing-contract
repair. Neither a matching paragraph nor green documentation checks establishes
whole-bundle authenticity, enforcement or efficacy.

The evidence suffices for this bounded source classification and documentation
decision: material observations are pinned, the read scope is explicit, and the
remaining provenance/runtime questions are unknown rather than assumed away.
No source commands, embedded skills, models, installations or host services were
run. No prompt body is copied into operational surfaces. Skills, routing,
governance and earlier adoption decisions remain unchanged.

## Fable version differences and reflection — 2026-11-12

### Research question and reading frame

The owner subsequently asked to think through the differences between the
versions and record the interpretation. This extends **CL52-DOC1 reference
documentation**, not the operating rules or adoption scope.

**[INFERENCE] The most useful distinction in the selected passages is a shift
from tool/output recipes toward explicit management of ongoing work, not simply
more instructions or a more capable model.** Much of the memory lifecycle that
looks elaborate in 5.2 is already present in 5.1. Code/Web naming and whole-file
size are particularly poor shortcuts for understanding the differences.

Keep five axes separate: the claimed model version, product/interface, account
configuration, artifact layer, and repository revision. The comparison below
describes these checked files; it is not a controlled model-version experiment.
Opus and other vendor/model-family siblings are outside this comparison, not
treated as intermediate Fable releases.

### Evidence used and version context

Checked 2026-11-12 at the same immutable repository pin
`93a584765460c2fb0ad58380bba476f2149df138`. The two 5.2 identities and official
publication limits remain those in the preceding supplement. The additional
files are:

| Artifact under `ANTHROPIC/` | Last path commit / date | Bytes | Git blob | SHA-256 |
| --- | --- | --- | --- | --- |
| [Fable 5][v5-file] | `09916a90583a320b3dde7ef5b9d8459ce0378a14` / 2026-06-15 | 122,750 | `acd3aec2ce6421b280f6edccaba268e4e325d1f2` | `1ef1257c67ebee68925e09206b4998755e5a10ac08af9ef9b5f30c17a897aa4c` |
| [Fable 5.1][v51-file] | `93b0ae6fb503db6642e58f9d6352db973a900cdc` / 2026-09-01 | 275,723 | `7165adca51712f87ebfb6591722cc8f571c511de` | `c57de521ca050e24634697b388fe840350481f238d3080cb2ef223cb8571196a` |

For these exact two paths, `git log -1 --format='%H %cI %s' -- PATH` supplied
commit dates; `wc -lc` and `git ls-tree -r -l HEAD -- PATHS` independently agreed
on byte sizes; `shasum -a 256 PATHS` supplied digests. These are repository dates,
not verified capture or release dates. The Fable 5 bytes include the June 15
edit, so this is not a reconstruction of the original June 11 reading.
Headings were indexed and the comparison-bearing sections below were read;
tool schemas, examples and appended skill bodies were not exhaustively audited.

### Evidence vs inference — what actually differs

All linked mirror passages in this subsection were checked 2026-11-12 at the pin
above. **Observed** means text present in the artifact, not authenticated vendor
policy or exercised behavior.

| Dimension | Fable 5 / 5.1 observations | Fable 5.2 observations | Bounded interpretation |
| --- | --- | --- | --- |
| What constitutes work | [5 already stages file creation and requires actual delivery][v5-work]. [5.1 distinguishes conversational visuals, connected tools, downloadable files and inline visualization][v51-visual]. | Both 5.2 files describe a cloud workspace that can continue while the person is away; the [web task lifecycle][v52-work] makes assumptions, irreversible choices, progress and final checking explicit. | Not a transition from a tool-free chatbot to the first agent. The later passages articulate more of the work lifecycle; product/interface changes remain a competing explanation. |
| Memory lifecycle | [5 explicitly says this user's memory is disabled][v5-memory], while separately describing artifact storage. [5.1 already has background filing, explicit remember/forget requests and user-confirmation boundaries][v51-memory]. | The [web 5.2 write policy][v52-memory] retains those mechanisms. | Disabled configuration is not missing model capability. Background memory and forgetting are not inventions of the inspected 5.2 sample; artifact storage, personal memory and conversation retrieval are different stores. |
| Memory concurrency | [5.1 already specifies read-before-write, version tokens, surgical edits and whole-file replacement without merging][v51-write]. | [5.2 uses MCP-qualified memory names and explicitly says to preserve lines written by other surfaces][v52-write]. | A namespace change and a more explicit preservation instruction do not prove a new backend, stronger isolation or a newly concurrent memory system. |
| When skill instructions enter context | [5][v5-skills] and [5.1][v51-skills] require relevant skill reads before code/file/computer work. | [5.2 examples][v52-skills] collect source material before loading build-format instructions. Its [building section][v52-work] preserves exceptions for research skills and Docs-type creation. | This is a concrete scheduling difference in the text, not permission to skip skills. Separate discovery of prerequisites from loading detailed build instructions; do not generalize away the named exceptions. |
| Progress and answer style | [5.1][v51-style] suggests occasional updates during many tool calls and a short answer afterward; it already distinguishes personal chats from formatted work. | [5.2][v52-style] explicitly separates working and chatting registers; its [task widget and final check][v52-work] carry progress while routine narration is reduced. | This is elaboration and interface coupling, not newly acquired social judgment. Removing narration is safe only if the actual interface gives the person another adequate progress channel. |
| Authority and review | [5.1 rejects authority-bearing memory preferences][v51-guard] and [untrusted file instructions in visual-tool routing][v51-visual]. | [5.2][v52-work] explicitly holds an ambiguous irreversible choice even unattended, checks the resulting artifact, and rejects forged notices as approval. | Earlier controls already exist. More explicit prose does not establish stronger safety enforcement; a separate reviewing agent is not by itself an independent empirical oracle. |

**Same-version Code/Web contrast.** The Code-named [identity wrapper][v52-code-id]
calls itself a CLI/SDK, but its [situation paragraph][v52-code-situation] describes
the same core-app/cloud-work arrangement as the [web sibling][v52-web-situation].
The latter even says that Claude Code-derived tools do not make this the Claude
Code harness. The Code-named bundle additionally contains the transcript turns,
tool results and on-demand skill bodies identified in the preceding ledger.
**[INFERENCE] Shared host components plus different capture composition explain
the visible overlap better than treating the filenames as a clean coding-versus-
chat experiment.** This is not proof of a common authenticated runtime. Its
larger size cannot be read as a larger always-loaded base prompt or higher token
cost per request.

### Reflections, counterarguments and local implications

1. **Instruction timing may matter more than instruction quantity. [INFERENCE]**
   The research-before-build ordering suggests a response to premature layout
   choices: detailed production instructions can constrain the work before the
   evidence exists. This is selective loading, not indiscriminate compression.
   The strongest objection is that an early skill may contain data requirements,
   safety limits or required inputs; delaying those would create rework or risk.
   The useful distinction is an early prerequisite check versus later detailed
   construction guidance, already compatible with [context engineering](../03-context/context-engineering.md).
   No universal research-first rule is adopted. A matched-task comparison would
   need to measure source coverage and rework, not just prompt length.

2. **Memory is a governed update path, not evidence of self-improvement. [INFERENCE]**
   These samples distinguish a user's confirmed facts from the assistant's own
   suggestions, explicit forgetting from background filing, and an update from a
   whole-file replacement. That is more informative than saying a later version
   remembers more. The counterweight is that most of this is already in 5.1,
   and neither file shows whether the storage service enforces it. TeaPrompt's
   [promotion gate](../04-agent/artifact-promotion.md) concerns provenance and
   authority; importing the personal-memory rule against filing fetched material
   would wrongly discard project research receipts. A useful future host check
   would exercise conflicting writers and attempted re-filing after forgetting,
   not merely check that the prompt mentions a version token.

3. **Autonomy shifts attention to decision boundaries and observable results. [INFERENCE]**
   The interesting design is not “ask fewer questions”: it separates a reversible
   assumption that can be disclosed from an irreversible choice that must wait.
   Task widgets can make unattended work legible, but checking a box cannot prove
   that a document opens, a page renders or a fact matches its source. A fresh
   reviewer can reduce inherited framing while still sharing the same model's
   errors. The local owners remain [brief](../skills/reflective-brief/SKILL.md),
   [risk](../skills/reflective-risk/SKILL.md) and
   [review](../skills/reflective-review/SKILL.md); no widget, reviewer or prompt
   grants action authority. A future comparison should score actual deliverables
   and held decisions, not continuation rate or number of completed task items.

4. **More capable hosting can require more boundary description, even while a
   workflow becomes simpler. [INFERENCE]** Cross-device files, persistent memory,
   artifact delivery and unattended work introduce distinct failure boundaries.
   A larger captured bundle can therefore coexist with more selective instructions
   for one task. The competing explanation is simply different extraction and
   formatting; this corpus cannot isolate either cause. For TeaPrompt, the useful
   unit of comparison is a responsibility and its owner, not a vendor paragraph
   count: which part belongs to a portable judgment, which to an interface, and
   which needs host enforcement? Keep the [existing surface taxonomy](../04-agent/agent-scaffold-provenance.md)
   rather than accumulate vendor-specific rules.

### Falsifiability, limits and handoff

The observed continuity in 5.1 prevents attributing all 5.2 memory detail to a new
version. A contrary passage can narrow a particular textual contrast; matched,
authenticated captures with the same product, build, tools, settings and task
would be needed to attribute a change to the model version. Actual outcome and
boundary observations would then be needed to establish benefit. The hypothetical
checks above are discriminators, **not executed experiments or authorized model
campaigns**.

This evidence is sufficient for the requested reflection: concrete passages,
continuities, competing explanations and falsifiers are recorded. Authenticity,
capture completeness, enforcement, token cost and model effectiveness remain
unknown. The official core-prompt check above cannot authenticate these extra
layers. CL52-SK1/COPY1/RUN1 and the retired status remain unchanged; only this
record, its catalogue navigation and generated discovery are updated. No new
Skill, prompt copying, upstream execution or runtime adoption follows.

[v5-file]: https://github.com/elder-plinius/CL4R1T4S/blob/93a584765460c2fb0ad58380bba476f2149df138/ANTHROPIC/CLAUDE-FABLE-5.md
[v51-file]: https://github.com/elder-plinius/CL4R1T4S/blob/93a584765460c2fb0ad58380bba476f2149df138/ANTHROPIC/Claude-Fable-5.1.md
[v5-work]: https://github.com/elder-plinius/CL4R1T4S/blob/93a584765460c2fb0ad58380bba476f2149df138/ANTHROPIC/CLAUDE-FABLE-5.md#L342-L369
[v5-memory]: https://github.com/elder-plinius/CL4R1T4S/blob/93a584765460c2fb0ad58380bba476f2149df138/ANTHROPIC/CLAUDE-FABLE-5.md#L166-L182
[v5-skills]: https://github.com/elder-plinius/CL4R1T4S/blob/93a584765460c2fb0ad58380bba476f2149df138/ANTHROPIC/CLAUDE-FABLE-5.md#L301-L320
[v51-memory]: https://github.com/elder-plinius/CL4R1T4S/blob/93a584765460c2fb0ad58380bba476f2149df138/ANTHROPIC/Claude-Fable-5.1.md#L416-L450
[v51-write]: https://github.com/elder-plinius/CL4R1T4S/blob/93a584765460c2fb0ad58380bba476f2149df138/ANTHROPIC/Claude-Fable-5.1.md#L526-L566
[v51-skills]: https://github.com/elder-plinius/CL4R1T4S/blob/93a584765460c2fb0ad58380bba476f2149df138/ANTHROPIC/Claude-Fable-5.1.md#L1226-L1243
[v51-style]: https://github.com/elder-plinius/CL4R1T4S/blob/93a584765460c2fb0ad58380bba476f2149df138/ANTHROPIC/Claude-Fable-5.1.md#L83-L118
[v51-visual]: https://github.com/elder-plinius/CL4R1T4S/blob/93a584765460c2fb0ad58380bba476f2149df138/ANTHROPIC/Claude-Fable-5.1.md#L1368-L1391
[v51-guard]: https://github.com/elder-plinius/CL4R1T4S/blob/93a584765460c2fb0ad58380bba476f2149df138/ANTHROPIC/Claude-Fable-5.1.md#L768-L784
[v52-memory]: https://github.com/elder-plinius/CL4R1T4S/blob/93a584765460c2fb0ad58380bba476f2149df138/ANTHROPIC/CLAUDE-WEB-APP-FABLE-5.2.md#L740-L789
[v52-write]: https://github.com/elder-plinius/CL4R1T4S/blob/93a584765460c2fb0ad58380bba476f2149df138/ANTHROPIC/CLAUDE-WEB-APP-FABLE-5.2.md#L875-L917
[v52-skills]: https://github.com/elder-plinius/CL4R1T4S/blob/93a584765460c2fb0ad58380bba476f2149df138/ANTHROPIC/CLAUDE-WEB-APP-FABLE-5.2.md#L343-L356
[v52-style]: https://github.com/elder-plinius/CL4R1T4S/blob/93a584765460c2fb0ad58380bba476f2149df138/ANTHROPIC/CLAUDE-WEB-APP-FABLE-5.2.md#L114-L162
[v52-work]: https://github.com/elder-plinius/CL4R1T4S/blob/93a584765460c2fb0ad58380bba476f2149df138/ANTHROPIC/CLAUDE-WEB-APP-FABLE-5.2.md#L399-L429
[v52-code-id]: https://github.com/elder-plinius/CL4R1T4S/blob/93a584765460c2fb0ad58380bba476f2149df138/ANTHROPIC/CLAUDE-CODE-FABLE-5.2.txt#L91-L103
[v52-code-situation]: https://github.com/elder-plinius/CL4R1T4S/blob/93a584765460c2fb0ad58380bba476f2149df138/ANTHROPIC/CLAUDE-CODE-FABLE-5.2.txt#L330-L337
[v52-web-situation]: https://github.com/elder-plinius/CL4R1T4S/blob/93a584765460c2fb0ad58380bba476f2149df138/ANTHROPIC/CLAUDE-WEB-APP-FABLE-5.2.md#L239-L247
