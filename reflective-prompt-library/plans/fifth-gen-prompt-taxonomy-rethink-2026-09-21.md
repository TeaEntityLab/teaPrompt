# Fifth-Generation Prompt-Taxonomy Rethink — pasted seven-category guidance (2026-09-21)

> **Status: decided — record-only; no installed change, no wording adopted.** The object is a pasted claim (zh-TW framing, English list): after fifth-generation models (`astra`/`fable`), only seven prompt categories pay — requirements, output contracts, invariants, validation, transformation, knowledge, observation — and "超出上開列表的提示皆屬多餘甚至可能阻礙模型表現" (everything outside the list is redundant, possibly harmful). The taxonomy is real and sourced — it is the design-by-contract prompt-engineering frame, and GPT-6 Astra / Claude Fable 5/5.1 guidance exists post-cutoff. The exclusivity clause exceeds every located source: no found document claims the seven categories are exhaustive or that other prompt content harms these models. Mapped against the full library, the claim's defensible core is already installed — a coaxing sweep found zero persona/style content — and its strong form is rejected as a category error: a content-type taxonomy cannot abolish a procedure layer.

## Research Question

User instruction, verbatim:

> Rethink: 第五代大模型(astra/fable)問市後最新 prompt 技巧指引如下：
>
> - requirements,
> - output contracts,
> - invariants,
> - validation,
> - transformation,
> - knowledge,
> - observation
>
> ( 超出上開列表的提示皆屬多餘甚至可能阻礙模型表現

Three questions: (1) does the guidance exist, and do the named models; (2) does the library already conform — is there prompt content outside the seven categories that should go; (3) does anything warrant adoption, restructuring, or deletion.

## Source Ledger

| Claim | Source | Source type | Verification status |
| --- | --- | --- | --- |
| Seven-category taxonomy (requirements / output contracts / invariants / validation / transformation / knowledge / observation) | arXiv 2409.08775v2 (Requirement-Oriented Prompt Engineering / design-by-contract); chatbot.ai "prompts as contracts"; gitconnected; sundeepteki; godeltech; towardsdatascience | paper + third-party analyses | held — the taxonomy exists as described, presented as "an interconnected framework", nowhere as exhaustive |
| Fifth-generation guidance: de-couple intent from execution; state-bound instructions; negative prompting for scope creep; strict output schemas + dual-payload; environmental/logical invariants; decoupled validation; turn/cost circuit breakers | openai.com/index/gpt-6-astra; medium GPT-6-Astra patterns; cruxdigits Astra-vs-Fable; buttondown agent-k | vendor + third-party | held as guidance — none of it claims the seven categories are the complete set of legitimate prompt content |
| `astra`/`fable` exist as named models | openai.com GPT-6 Astra page; Anthropic Claude Fable 5/5.1 references (post-cutoff) | vendor | held for existence only; no capability claim independently verified |
| Exclusivity clause: everything outside the seven is redundant or harmful | the user's paste | user-provided artifact | **not held** — no located source states it; it is stronger than the taxonomy's own presentation |

## What the Library Already Is

Inventory: 9 core prompts, 5 thinking prompts, 8 engineering prompts, 6 context prompts, 11 agent prompts, 6 domain prompts, 4 repo surfaces, 9 workflow skills + 3 governance/flow skills + 12 companion example files, plus methodology/governance docs.

The seven categories mapped to installed surfaces:

| Category | Installed surface |
| --- | --- |
| requirements | `reflective-brief`, `reflective-spec-plan`, `02-engineering/usage-first.md`, `task-start.md`; every Module Contract `Trigger` field |
| output contracts | every Module Contract `Output` field; pack manifests; governed-delivery oracle manifest + acceptance record (the dual-payload split: state/metadata vs artifact) |
| invariants | every `Never` list; `reflective-minimality` Safety Floor; Standing Non-Goals; `06-repo/AGENTS.md` anti-cheating rules |
| validation | the repo's deepest installed rule: second-method verification, decorrelated checks, `make all`, route evals, "verify with evidence" — the guidance's "never let the model validate its own work" is already the house position |
| transformation | `04-agent/sop-compiler.md`, `workflow-acquisition.md`, spec→implementation recipes |
| knowledge | `03-context/` pack, `PROJECT_KNOWLEDGE.md`, `GLOSSARY.md`, `memory-consolidation.md` |
| observation | `02-engineering/local-feedback.md`, `04-agent/retro.md`, `context-handoff.md` — thinnest coverage: the live tool-result loop is host-owned (Non-Goal 52); the library writes policy for consuming observations, not the loop itself |

What sits outside the seven categories: the **procedure layer** — `01-thinking` reasoning scaffolds, the nine skills' sequencing, `reflective-dispatch` routing, `workflow-recipes.md`, METHODOLOGY_MAP's classify→strictness→compose→verify loop — plus companion examples and governance/meta docs.

Coaxing sweep (2026-09-21, over `00-core`/`01-thinking`/`02-engineering`/`05-domain`): **three benign role headers** ("You are a Reflective Engineering Agent", "You are an implementation agent", one out-of-scope negation) and **zero persona/style/few-shot-coaxing content** — no "be helpful", no tone instructions, no flattery, no think-step-by-step bait. The library is already contract-shaped; the claim's defensible core describes the status quo.

## Concept Map

| # | Concept | Disposition |
| --- | --- | --- |
| C1 | Contract-shaped prompting dominates coaxing | installed — the library is built this way; sweep confirms |
| C2 | Decoupled validation (never self-validate) | installed — second-method rule, decorrelated verification, `make all` |
| C3 | De-couple intent/planning from execution | installed — `reflective-spec-plan` → `reflective-implement` split; governed-delivery proposal/authorization/effect/acceptance separation |
| C4 | State-bound instructions + negative prompting | installed — `04-agent/runtime-trust-boundary.md`; Never lists; scope-creep bounds |
| C5 | Explicit failure signalling (error schema over workaround) | installed at pack level — governed-delivery failure-signature exits; skill `Escalation` fields are the prompt-level analogue |
| C6 | Turn/cost circuit breakers | host territory — Non-Goal 52; pack-level budgets exist in governance packs; no prompt-layer change |
| C7 | CoT monitorability degradation → verify outcomes, not traces | corroborated — TeaPrompt already verifies outcomes with evidence, never trace inspection |
| C8 | Exclusivity clause (outside-the-list = redundant/harmful) | rejected — category error: the taxonomy classifies prompt *content*; the procedure layer is harness *policy* (METHODOLOGY_MAP's own frame). Sources don't claim it; harm is unverified; the dual audience (pi-warden vindication: NL policy is machine-judged input *and* human-auditable record) makes deletion a governance loss even where a model might not need the scaffold |
| C9 | The taxonomy as a classification vocabulary | noted — a useful audit lens, no local gap found for it to close |

## Candidate Adoption Ledger

| # | Candidate | Decision | Evidence | Reopen trigger |
| --- | --- | --- | --- | --- |
| RT-1 | Add a seven-category classification question to `reflective-minimality` (classify each instruction block; process scaffolding must justify) | No change 2026-09-21 | the gate's operative test — "does this instruction earn its tokens; state each instruction once" — already covers the substance; a seven-slot label adds ceremony, no new test | an audit finds prompt content that is neither contract-shaped nor justified procedure |
| RT-2 | Delete the procedure/scaffold layer per the exclusivity clause | Rejected 2026-09-21 | category error + exceeds sources + dual-audience loss; the clause is the paste's own, not the taxonomy's | controlled evidence that a specific scaffold class degrades fifth-generation outcomes |
| RT-3 | Cut companion `examples/*.md` files (outside the list) | No change 2026-09-21 | examples are installer-facing illustrations, not prompt payloads; harm claim unverified | measured degradation attributable to co-installed examples |
| RT-4 | Adopt sourced adjacent guidance not in the seven (plan/execute decoupling, failure schemas, circuit breakers) | No change 2026-09-21 | installed or host territory — C3/C5/C6 | a verified local gap in one of those mechanisms |
| RT-5 | Record the rethink and the exclusivity rejection | Adopted 2026-09-21 (record-only) | prevents re-litigating the clause on each new model generation | — |

## Evidence vs Inference

- Verified: the taxonomy exists and matches the paste's seven names; Astra/Fable guidance exists post-cutoff; no located source states exclusivity; the library inventory and coaxing-sweep counts; every "installed" row names its surface.
- Author-claimed/unverified: all fifth-generation capability claims; any harm from out-of-list prompt content; whether the paste's parenthetical paraphrases a source or is the user's own strengthening.
- Inference: the claim is directionally aligned with where the library already sits — the recent survey landings (PW-1's confidence-ratchet *contract* sentence, GE-1's ledger intake) are contract-shaped additions, not procedure additions — so the claim adds no correction, only a vocabulary.

## Falsifiability

The record-only verdict is wrong if: (a) a primary source for the exclusivity clause surfaces — then RT-2's rejection is re-examined against it; (b) a controlled comparison shows a TeaPrompt procedure artifact degrading a fifth-generation model's outcome versus its contract-only reduction — then the named artifact, not the library, is cut; (c) an audit finds library prompt content that is neither contract-shaped nor justified procedure — then RT-1's lint is adopted.

## Completion Ledger

| Item | Status | Evidence |
| --- | --- | --- |
| Guidance and model existence verified against sources | done | Source Ledger |
| Seven categories mapped to installed surfaces | done | What the Library Already Is |
| Outside-the-list inventory + coaxing sweep | done | three benign role headers; zero persona/style content |
| Nine concepts mapped; five candidates decided with falsifiers | done | Concept Map; Candidate Adoption Ledger |
| Clean-room boundary on installed surfaces | done | guard vocabulary test |
| Guard written | done | `plans/tests/test_fifth_gen_taxonomy_rethink_record.py` |
| Decision Index row (at head), case-studies row, `index.json` | done | `PROJECT_KNOWLEDGE.md`; `external-adoption-case-studies-2026-06-20.md` |
| Full repository gate | done | `make all` from the repository root |
