# Plan: Reflective Prompt Library Build

## Goal

Create a filesystem prompt library from the provided Reflective Engineering Prompt Library guidance.

## Assumptions

- The primary deliverable is Markdown artifacts, not executable software.
- The canonical library root is `reflective-prompt-library/`.
- Additional named prompts from the source text should be preserved even when they were not included in the suggested directory tree.
- Code or workflow work should be captured as plan files instead of implemented implicitly.

## Scope In

- Core prompt files.
- Thinking prompts.
- Engineering prompts.
- Context prompts.
- Agent and workflow prompts.
- Domain prompts.
- Repo instruction templates.
- Plan files for future code and workflow work.

## Scope Out

- Building a prompt management app.
- Creating an eval harness.
- Installing skills, agents, or external tools.
- Modifying the repository root `AGENTS.md`.
- Running tests that do not exist for this documentation-only repo.

## Acceptance Criteria

- `reflective-prompt-library/` exists.
- Each directory named in the requested structure exists.
- Each mentioned Markdown artifact has a corresponding `.md` file.
- Code-bearing or workflow-bearing follow-ups are recorded under `reflective-prompt-library/plans/`.
- Files contain copyable prompts or operational guidance.

## Verification

- List all Markdown files under `reflective-prompt-library/`.
- Check for empty Markdown files.
- Review `git status --short` to confirm created artifacts.

## Residual Risks

- Some source sections are usage guidance rather than prompt files; these are consolidated into `README.md` and `04-agent/workflow-recipes.md`.
- Future users may want exact verbatim prompt text; current files preserve the substance and structure, with minor formatting normalization.

