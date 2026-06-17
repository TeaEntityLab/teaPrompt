# Project-Knowledge Authority and Promotion Decision — 2026-06-17

## Goal

Correct the first TeaPrompt project-knowledge implementation after reviewing
Knowie's upstream origin story, scaffold, handshake, and lifecycle skills.

## Evidence That Changed the Decision

- Knowie was created because its author repeatedly rebuilt the knowledge
  structure and AI-tool connections for each new project; its own knowledge base
  is a dogfood instance, not the product boundary.
- Knowie's project principles are a normative input to design judgement, while
  its host instruction files retain agent operating authority.
- Its lifecycle includes automatic read-first wiring, promotion from draft to a
  long-term tier, causal decision history, and repeated procedures becoming
  project-local skills.
- TeaPrompt's first implementation captured a static rationale index but called
  it non-normative, declared a promotion path without implementing it in the
  owning skill, and used modal-word scanning as a proxy for authority.

## Decision

1. Define project knowledge as **non-authoritative, not non-normative**.
   Project-design principles may guide product and architecture decisions. They
   cannot grant agent authority, authorize actions, or override higher-authority
   instructions, user authorization, AGENTS.md, or skill contracts.
2. Keep agent operating rules in `AGENTS.md` / `SKILL.md`; keep project-design
   judgement in the project-knowledge artifact.
3. Make knowledge promotion an explicit `reflective-handoff-retro` output
   contract with evidence, destination, authority classification, approval,
   provenance, and review/retirement trigger.
4. Treat repeated procedures as project-local skill candidates with a stricter
   human-confirmation gate than prose knowledge.
5. Publish a reusable repository template so TeaPrompt can help other projects
   establish their own judgement layer without importing Knowie's CLI or full
   cognitive taxonomy.
6. Replace generic modal-word policing with an honest structural authority check
   plus a narrow scan for explicit agent-directed rules. Deterministic validation
   is a guardrail, not semantic proof.

## Rejected Alternatives

- Keep `NON-NORMATIVE`: rejected because it prevents project principles from
  doing the judgement work the layer exists to support.
- Copy Knowie's complete directory tree and meta-skills: rejected because the
  target projects should grow structure only when evidence justifies it.
- Add a tenth TeaPrompt core workflow skill: rejected because the existing
  handoff/retro workflow already owns consolidation and promotion.
- Automatically harvest every conversation: rejected because captured material
  is not equivalent to a durable, human-approved project decision.
- Infer authority from every occurrence of `must` or `shall`: rejected because
  wording is not authority and blockquote formatting is not a trust boundary.

## Acceptance Criteria

- The live project-knowledge artifact and reusable template declare a
  non-authoritative boundary while allowing project-design principles.
- Explicit agent-directed rules are rejected even inside blockquotes; ordinary
  normative project-design language is allowed.
- `reflective-handoff-retro` defines a complete promotion candidate contract and
  a project-local skill path.
- Repository guidance points to the reusable template and actual read-first rule.
- The initial decision remains in history and is explicitly refined, not erased.
- Unit, link, governance, and index validation pass.

## State Ledger

| Item | Status | Evidence |
| --- | --- | --- |
| Authority model corrected | verified | live artifact + validator boundary tests |
| Promotion contract connected | verified | handoff-retro contract + regression test |
| Reusable scaffold published | verified | `06-repo/PROJECT_KNOWLEDGE.template.md` + README/methodology links |
| Initial decision supersession recorded | verified | Decision Index + refinement section in initial record |
| Verification complete | verified | 52 tests; project-knowledge, link, skill, governance, index, and diff checks passed |
