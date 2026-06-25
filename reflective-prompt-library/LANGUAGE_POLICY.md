Language: English | [繁體中文](LANGUAGE_POLICY.zh-TW.md)

# Language Policy

## Current Status

TeaPrompt is not fully English today.

The repository currently has two language layers:

1. **Operational layer: English**
   - Root `README.md`
   - `reflective-prompt-library/README.md`
   - `reflective-prompt-library/SKILL_INSTALLATION.md`
   - `reflective-prompt-library/skills/*/SKILL.md`
   - `reflective-prompt-library/plans/*.md`

2. **Prompt source layer: mixed English and Traditional Chinese**
   - Many reusable prompt templates under `00-core/` through `05-domain/` preserve Chinese wording from the original prompt library.
   - This is intentional source material, not an operational inconsistency by itself.

## Decision

Use English as the canonical language for:

- Repository navigation
- Installation docs
- Skill/workflow instructions
- Plans and design records
- File and directory names
- Metadata such as `name`, `description`, and `license`

Allow localized prompt source files when the prompt is meant to be copied by users in that language.

## Why

Skills are execution surfaces. They should be short, portable, and tool-friendly, so English is the safest default.

Prompt files are content artifacts. Preserving the user's original language can be valuable because wording, tone, and cultural context are part of the artifact.

## Naming Convention

When adding localized prompt files:

- Use English file names by default.
- Add a language suffix only when there are multiple language variants:
  - `task-start.en.md`
  - `task-start.zh-TW.md`
- Prefer Traditional Chinese tag `zh-TW` for Chinese prompt variants.

## Future Normalization Options

If the repository must become fully English:

1. Translate all Chinese prompt source files into English.
2. Move Traditional Chinese originals into a dedicated localized folder:
   ```text
   reflective-prompt-library/locales/zh-TW/
   ```
3. Keep English canonical prompts in the current category folders.
4. Add a translation parity checklist to prevent drift.

This is a larger content migration and should not be done casually because it may lose prompt nuance.

## Acceptance Criteria

The repository language state is healthy when:

- All operational docs are English.
- Every intentional non-English prompt source is documented as localized content.
- Skills remain English-only unless a tool-specific localization is explicitly needed.
- README explains the language layering.
- Future contributors know whether they are editing operational instructions or localized prompt content.


## Localization Boundary (2026-06-25)

Panel consensus (Round 6):

- **English remains canonical** for all `skills/*/SKILL.md` contracts and governance plans.
- **Traditional Chinese** is supported for navigation (`README.zh-TW.md`), cheatsheets
  (`SKILL_TRIGGER_CHEATSHEET.zh-TW.md`), and glossary routing lines — not full skill
  contract translation.
- Prompt source files under `00-core/`–`05-domain/` may stay localized when the
  artifact itself is language-specific content.

**Operational test:** A TW adopter can route L1–L2 tasks using cheatsheet + glossary
without a translated `SKILL.md`; deeper contracts load in English. ROUTE-002
includes Traditional Chinese holdout phrases to test intent-normalization fairness
in the deterministic router — not full skill contract translation.
