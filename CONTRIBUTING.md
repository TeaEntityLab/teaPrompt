# Contributing to TeaPrompt

Thank you for your interest in contributing to TeaPrompt! This document outlines the quality standards, review process, and guidelines for contributing prompts, skills, or improvements to the library.

## Project Philosophy

TeaPrompt is a **reflective engineering prompt library** focused on quality over quantity. Our goal is to provide a small, curated set of composable workflows rather than a massive catalog of unmaintained prompts.

**Core principle:** Doing the right thing > doing things right.

## Harness Policy (Nine Skills)

TeaPrompt ships **nine frozen workflow skills** as natural-language harness policy — not a multi-agent runtime.

- Pick **Strictness L1–L6** before choosing a skill ([reflective-dispatch](reflective-prompt-library/skills/reflective-dispatch/SKILL.md)).
- Do **not** add a tenth core skill without the three-recurrence promotion gate ([PROJECT_KNOWLEDGE](reflective-prompt-library/PROJECT_KNOWLEDGE.md)).
- Routing fairness: [ROUTING_CONTRACT](reflective-prompt-library/plans/ROUTING_CONTRACT.md); panel record: [multi-agent-panel-consensus](reflective-prompt-library/plans/multi-agent-panel-consensus-2026-06-25.md).

```bash
make all   # tests + validate (routing, governance, benchmarks fixture, skill examples)
```



## Routing Maintenance

Before tuning `route_paraphrase_eval.py`:

1. Add fresh holdout phrases to `route-002-holdout-eval.yaml` and/or adversarial cases to `route-003-adversarial-eval.yaml`.
2. Run `make all` — `validate_route_fixture.py` enforces minimum fixture coverage.
3. Record governance-surface decisions in `PROJECT_KNOWLEDGE.md` Decision Index when routing contract changes.

See [ROUTING_CONTRACT R8](reflective-prompt-library/plans/ROUTING_CONTRACT.md) and the [Governance Maintenance Playbook](reflective-prompt-library/GLOSSARY.md).

## Quality Standards

### Prompt Quality Requirements

All prompts must include:

1. **Clear Purpose** - A concise statement of what the prompt achieves
2. **Module Contract** - Structured definition of:
   - **Trigger** - When to use this prompt
   - **Methods** - Core techniques or approaches
   - **Output** - Expected output format
   - **Never** - Anti-patterns to avoid
3. **Escalation** - When to route to other workflows or request human review
4. **Evidence-Based** - Claims should be backed by research or experience where applicable

### Skill Quality Requirements

All skills (SKILL.md files) must include:

1. **Frontmatter** with required fields:
   ```yaml
   ---
   name: skill-name
   description: Clear one-line description
   license: MIT
   risk_level: low|medium|high
   human_review_required: true|false
   external_io: true|false
   ---
   ```

2. **Required Sections**:
   - Purpose
   - Module Contract (with Trigger, Methods, Output, Never subsections)
   - Escalation or equivalent risk gating

3. **Quality Signals**:
   - Acceptance criteria where applicable
   - Human Review triggers for high-risk operations
   - Clear boundaries and scope
   - Actionable output format

### Technical Requirements

- **No broken links** - All `ref_file`, `ref_snippet`, and markdown links must validate
- **Valid frontmatter** - YAML frontmatter must parse correctly
- **Appropriate length** - Skills should be focused (typically 50-500 lines)
- **No dangerous patterns** - Explicit gates for destructive operations

## Contribution Process

### 1. Before Contributing

- **Fork the repository** and create a feature branch
- **Run validation tools** to ensure your changes pass quality gates
- **Review existing patterns** - Match the style and structure of similar prompts/skills

### 2. Making Changes

```bash
# Run link and schema validation
python3 reflective-prompt-library/plans/validate_links.py

# Run the linter
python3 reflective-prompt-library/plans/lint_skills.py

# Validate governance metadata
python3 reflective-prompt-library/plans/validate_governance.py

# Regenerate the index
python3 reflective-prompt-library/plans/generate_index.py
```

### 3. Submitting Changes

- **Create a pull request** with clear description of changes
- **Reference related issues** if applicable
- **Include validation results** in the PR description
- **Set the appropriate labels** (e.g., `new-prompt`, `new-skill`, `bugfix`)

### 4. Review Process

All contributions go through review:

1. **Automated Checks** - Validation tools must pass
2. **Manual Review** - Maintainers review for:
   - Alignment with project philosophy
   - Quality and clarity
   - Consistency with existing patterns
   - Documentation completeness
3. **Testing** - When applicable, test the workflow in real scenarios
4. **Feedback** - Maintainers may request changes before merge

## Quality Gates

Contributions must pass these quality gates:

### Required (Blocking)

- ✅ All links validate (no broken references)
- ✅ Frontmatter is valid and complete
- ✅ Required sections are present
- ✅ Governance metadata is complete
- ✅ No dangerous patterns without explicit gates

### Recommended (Non-blocking but encouraged)

- ⚠️  Human Review triggers for high-risk content
- ⚠️  Acceptance criteria for implementation prompts
- ⚠️  Clear escalation paths
- ⚠️  Evidence-based claims with sources

## Types of Contributions

### New Prompts

- Add to appropriate category directory (`00-core/`, `01-thinking/`, etc.)
- Follow existing prompt structure
- Include clear trigger conditions
- Document prompt sources if derived from existing work

### New Skills

- Add to `reflective-prompt-library/skills/`
- Create subdirectory with `SKILL.md`
- Include required frontmatter with governance metadata
- Map to underlying prompt sources
- Consider adding example usage

### Documentation

- Update README files if adding new categories
- Update METHODOLOGY_MAP.md if changing workflows
- Add translations if multilingual
- Keep examples current

### Tooling

- Improve validation scripts
- Add new quality checks
- Enhance index generation
- Fix bugs in existing tools

## Language Policy

- **Operational documentation** (README, CONTRIBUTING, plans) in English
- **Prompt sources** can be English or Traditional Chinese (zh-TW)
- **Translations** welcome - maintain both versions
- See `LANGUAGE_POLICY.md` for details

### Translation Completeness

Translation files (`.zh-TW.md`) must cover:
- All section headings
- All code blocks
- All warning, note, and callout boxes

Narrative sections may be summarised if a disclaimer at the top of the file notes the editorial choice. Translations that omit entire sections without an editorial note should not be merged. Existing abridged translations are grandfathered under this policy.

## Testing Your Changes

### Manual Testing

1. **Test the workflow** - Use the prompt/skill in a real scenario
2. **Test edge cases** - Try unusual inputs or contexts
3. **Test routing** - Ensure it integrates well with other workflows
4. **Test quality** - Verify output meets acceptance criteria

### Automated Testing

```bash
# Run all validations
python3 reflective-prompt-library/plans/validate_links.py
python3 reflective-prompt-library/plans/lint_skills.py
python3 reflective-prompt-library/plans/validate_governance.py

# Test routing consistency
make validate
```

## Style Guidelines

### Writing Style

- **Be concise** - Prefer compact, direct language
- **Be specific** - Avoid vague claims or instructions
- **Be actionable** - Provide clear next steps
- **Be evidence-based** - Distinguish facts from claims

### Code Style

- **Python scripts** - Follow PEP 8 style
- **Markdown** - Use consistent heading levels
- **YAML** - Use simple key-value pairs in frontmatter
- **File naming** - Use kebab-case for files and directories

## Getting Help

- **Questions** - Open an issue with the `question` label
- **Discussions** - Use GitHub Discussions for design conversations
- **Issues** - Report bugs with reproduction steps
- **Documentation** - Suggest improvements via issues or PRs

## License

By contributing, you agree that your contributions will be licensed under the MIT License, consistent with the project's existing license.

## Recognition

Contributors are recognized in the project's contributor list. Significant contributions may be highlighted in release notes.

## Thank You

TeaPrompt relies on community contributions to remain useful and current. We appreciate your help in building a high-quality reflective engineering resource!