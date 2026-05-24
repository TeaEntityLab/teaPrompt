# Research Synthesis: Prompting to Skills as Workflow

## Goal

Design a concise, maintainable skills-as-workflow layer for the Reflective Prompt Library.

## Evidence Used

### Claude / Anthropic Skill Model

- Sources: https://code.claude.com/docs/en/skills, https://support.claude.com/en/articles/12512198-how-to-create-custom-skills, https://claude.com/docs/skills/overview
- Official Claude Code docs define skills as directories with `SKILL.md` and YAML frontmatter. The `description` helps the model decide when to load the skill automatically.
- Claude docs emphasize progressive disclosure: metadata first, `SKILL.md` when activated, and supporting resources only when needed.
- Official guidance recommends keeping skill bodies concise, moving detailed references to supporting files, and using focused skills rather than one large skill.

### obra/superpowers DeepWiki

- Source: https://deepwiki.com/obra/superpowers
- DeepWiki describes Superpowers as a multi-platform methodology built from composable skills and a mandatory protocol.
- Its core strength is preventing agents from jumping directly into code by forcing a step back into specs/design before implementation.
- Notable patterns: meta-skill routing, TDD, systematic debugging, YAGNI/DRY, safety isolation, structured idea-to-code pipeline, and two-stage review.

### mattpocock/skills DeepWiki

- Source: https://deepwiki.com/mattpocock/skills
- DeepWiki describes this repository as a collection of small, adaptable, composable skills based on engineering experience rather than vibe coding.
- Useful patterns: product planning, PRD slicing into vertical slices, TDD, disciplined diagnosis, plan grilling against docs, handoff, and shared domain language through a compact context file.
- The strongest lesson for this library is to keep skills small and let workflow composition happen naturally.

### jnMetaCode/superpowers-zh GitHub

- Source: https://github.com/jnMetaCode/superpowers-zh
- DeepWiki note: a DeepWiki page for this fork was not discoverable during this pass, so the GitHub repository README was used as upstream evidence.
- The Chinese edition expands Superpowers with Chinese-language workflow conventions, wider tool support, hooks/bootstrap setup, and additional workflow-runner / MCP-builder ideas.
- Useful patterns: localization matters, explicit manual invocation for culture-specific reference skills can reduce automatic-trigger pollution, and install automation is valuable only after the skill set stabilizes.

## Design Decisions

1. Create 8 workflow skills, not 49 prompt skills.
2. Keep `SKILL.md` files self-contained and concise.
3. Store detailed prompts as source material under the existing prompt library.
4. Avoid scripts, manifests, hooks, or installers for now.
5. Use one router skill plus seven practical workflows.
6. Treat high-risk review as a gate that can precede any other workflow.
7. Treat DeepWiki as a research map, not a substitute for official docs or upstream source.

## Resulting Skills

| Skill | Role |
| --- | --- |
| `reflective-dispatch` | Route a task to the smallest useful reflective workflow. |
| `reflective-brief` | Convert ambiguity into goal, assumptions, scope, acceptance, falsifiability, and next step. |
| `reflective-spec-plan` | Produce spec, usage-first design, and task slices. |
| `reflective-implement` | Execute code changes with traceability and verification. |
| `reflective-review` | Review artifacts/code/plans with critique, traceability, and required fixes. |
| `reflective-research` | Conduct source-backed research, DeepWiki inspection, and long-document synthesis. |
| `reflective-risk` | Gate high-risk work with threat model, dry-run, rollback, and Human Review. |
| `reflective-handoff-retro` | Preserve handoff context and convert retros into reusable rules. |

## Anti-overengineering Rules

- Add scripts only when a repeated step becomes deterministic and tedious.
- Add install automation only after the skill set is used enough to justify it.
- Add per-domain reference files only when `SKILL.md` exceeds useful size or domain details start competing.
- Do not add hooks until automatic triggering failures are observed repeatedly.

## Validation Checklist

- Every skill has `name` and `description`.
- Every skill maps to a repeatable workflow.
- No skill depends on unavailable scripts.
- No skill requires reading the whole prompt library before use.
- High-risk work is gated before implementation.
- Prompting remains the source of nuance; skills remain the execution wrapper.
