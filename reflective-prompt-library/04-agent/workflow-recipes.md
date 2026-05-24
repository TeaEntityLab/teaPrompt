# Workflow Recipes

This file captures recommended prompt compositions and workflow sequences.

## General Thinking

```text
Socratic Prompt
-> Critical Thinking Prompt
-> Why / What / How / Done
-> Decision
```

## Engineering Task

```text
Task Start Prompt
-> Spec Writer
-> Usage-first
-> Task Slicer
-> Implementation Agent
-> Code Review
-> Test Designer
-> Retro
```

## High-risk Task

```text
High-risk Prompt
-> Assumption Audit
-> Threat Model
-> Dry-run Plan
-> Human Review
-> Implementation
-> Review
-> Rollback Check
```

## Long Research Task

```text
Research Prompt
-> Document Map
-> Evidence Check
-> Counterargument
-> Synthesis
-> Context Handoff
```

## Agent System Design

```text
Agent Selection Prompt
-> Why / What / How / Done
-> Spec Writer
-> Usage-first
-> Task Slicer
-> Workflow Engine Plan
-> Review-Rating-Fix
```

## Cost Modes

Low-cost daily mode:

```text
core-short
+ socratic-reviewer
+ critical-thinking-check
+ why-what-how-done
```

Medium-cost engineering mode:

```text
AGENTS.md
+ spec-writer
+ usage-first
+ task-slicer
+ implementation-agent
+ code-reviewer
```

High-cost strict mode:

```text
master-prompt
+ high-risk
+ review-rating-fix
+ hidden eval
+ context-handoff
+ retro
```

Agent / workflow mode:

```text
prompt library
+ skills
+ scripts
+ state files
+ eval harness
+ dashboard
```

## Practical Principle

Do not put everything into one giant prompt. Prefer:

```text
core identity prompt
+ task prompt
+ situation prompt
+ validation prompt
```

