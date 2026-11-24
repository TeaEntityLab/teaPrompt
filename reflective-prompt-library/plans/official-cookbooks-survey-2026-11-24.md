# Official Cookbooks Survey — OpenAI, Anthropic, Gemini (2026-11-24)

Language: English
> **Status:** source-qualified reference record (`CKB-DOC1`); no Skill, prompt-body, operating-rule, or runtime change.**

The owner asked to survey the major platforms' official docs and cookbooks, anchored on `openai/openai-cookbook`. This record pins three HEADs, reads the mechanism-bearing docs in each, and maps the transferable distinctions onto existing TeaPrompt contracts. It does not run a notebook, call a model, install an SDK, or authorize a runtime. The useful mechanisms — external verifiers, deterministic-first gates, budget caps, staged repair — are already required by existing TeaPrompt contracts; no reproduced local gap was found.

## Research Question and Direct Recommendation

Which mechanisms in the official cookbooks are worth borrowing, and do they expose a TeaPrompt Docs or Skill gap?

**Record the boundaries; do not adopt a runtime or add a Skill.** All three cookbooks are API-callable example collections, not method contracts: their value for TeaPrompt is vocabulary plus a few disciplined mechanism notes. The strongest transferable example is Gemini's **0-token verbatim citation gate** — a pure-Python check that rejects fabricated/frankenquote/misattributed citations before any judge call — which restates TeaPrompt's deterministic-first, cheap-then-expensive verification ordering with a named taxonomy of citation failure modes.

## Evidence Used and Date Context

Checked 2026-11-24. Blobless clones; only the files named below were fetched and read.

| Item | Pinned HEAD | What this check covers |
| --- | --- | --- |
| `openai/openai-cookbook` | `dfd760b4` | `AGENTS.md`, `articles/per_run_spending_controller_responses_api.md`, `articles/techniques_to_improve_reliability.md`, `examples/evaluation/Building_resilient_prompts_using_an_evaluation_flywheel.md`, `examples/{decisions,evals,codex,agent_optimization}` listings |
| `anthropics/anthropic-cookbook` | `8ad5de64` | `CLAUDE.md`, `managed_agents/README.md` (19-notebook CMA matrix), `patterns/agents/README.md`, `skills/README.md` + `CLAUDE.md`, `evals/`, `tool_evaluation/` listings |
| `google-gemini/cookbook` | `fdb37e26` | `README.md`, `quickstarts/` + `examples/` listings; markdown cells of `Governed_Function_Calling_With_PII_And_Cost_Guardrails.ipynb` and `Citation_Faithfulness_Check.ipynb` |

## What Each Cookbook Actually Contains

- **OpenAI** (`168 md / 277 nb`): `AGENTS.md` is a contributor-governance doc — naming conventions, `registry.yaml` publication, secrets rules, and a **merge gate requiring the `docs-editor` skill on every changed markdown/notebook before PR merge** plus P0/P1 resolution. Mechanism articles: the **per-run spending controller** (reserve worst-case cost per request with `Fraction`-exact accounting, refund actuals, `verified_at` price pinning, explicit "not real prices" disclaimers) and the **evaluation flywheel** (analyze → measure → improve; baseline before rewriting; cites the AI Evals course reader). `examples/codex/` carries iterative-repair and review recipes; `examples/evals/` covers imagegen/realtime evals while the dataset-backed Evals platform retires (migration to Promptfoo documented).
- **Anthropic** (`91 md / 104 nb`): the most structured of the three. `CLAUDE.md` pins contributor conventions (ruff, conventional commits). `patterns/agents/` implements the Building Effective Agents topology set (chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer). `managed_agents/` is a 19-notebook **hosted-runtime** tutorial matrix whose one-line descriptions double as a governance checklist: session `budget` caps with `budget_reached` pause, `requires_action` human gates with custom-tool `decide()/escalate()`, prompt versioning + rollback by session pinning, memory stores with read-only mounts, `inference_geo` pinning, per-agent effort as cost lever, `multiagent` coordinator with scoped toolsets + `advisor` roster entries, and **outcome grading — a stateless grader that fetches every cited URL and checks quotes against a rubric before revisions pass**. `skills/` mirrors the SKILL.md + progressive-disclosure layout TeaPrompt already uses.
- **Gemini** (`28 md / 157 nb`): quickstart-shaped; README tracks model releases. Mechanism examples: **`Citation_Faithfulness_Check`** — structured-output citations (`document_id` + verbatim quote) screened by a 0-token verbatim gate before an optional burden-of-proof judge; names three failure modes (fabricated, frankenquote, misattributed) — and **`Governed_Function_Calling_With_PII_And_Cost_Guardrails`** — TealTiger policies (PII regex block, tool allowlist, per-session budget, audit trail) evaluated deterministically before each tool call, "no LLM in the governance path, <2ms". Also present: an **Agents API** managed-agents quickstart and a **Decisions API** returning typed yes/no/choice/score with calibrated probabilities at zero output-token cost.

## Evidence vs Inference

- **Verified:** the pinned HEADs; file counts; every mechanism described in the three sections above (read directly from the named files).
- **Supplier-summarized (unverified):** all API behaviors the notebooks assume (budget enforcement, `requires_action` semantics, Decisions calibrated probabilities, TealTiger's <2ms claim); cookbook claims about model capabilities.
- **Inference (this record):** the contract-map dispositions; the judgment that transferable duties are already covered. Notebook code cells were not executed or audited line-by-line.
- **Unknown:** whether the deterministic gates hold under adversarial inputs in practice; cookbook maintenance cadence vs. actual API drift; whether OpenAI's `docs-editor` merge gate is enforced in CI or by convention.

## TeaPrompt Contract Map and Disposition

| Finding | Existing surface | Disposition |
| --- | --- | --- |
| 0-token verbatim citation gate before any judge call; named citation failure modes | `reflective-review` evidence checks; `governed-delivery` decorrelated verification; `verification-map-generator` | Restates deterministic-first ordering; the fabricated/frankenquote/misattributed taxonomy is a deferred doc note, not a missing rule |
| Deterministic policy evaluation (PII regex, tool allowlist, budget) in the tool-call path, no model in the gate | `04-agent/runtime-trust-boundary.md` authority map and deterministic gates | Same pattern; TeaPrompt already requires determinism where enforceable and Human Review where not |
| Per-run / per-session budget with reserve-refund accounting and `budget_reached` pause | `flow-loop-harness` deterministic caps; `governed-delivery` task-declared budgets | Restated; OpenAI's `Fraction`-exact reserve-refund and `verified_at` price pinning are worked-implementation details |
| Eval flywheel: qualitative failure-mode analysis → baseline → targeted fix → re-measure | `flow-loop-harness`; `golden-benchmark-runner`; eval-driven promotion gates | Same loop; no new obligation |
| CMA runtime matrix (prompt versioning + rollback, `requires_action` gates, scoped toolsets, advisor roster, outcome grader) | `reflective-review` evidence quoting; `runtime-trust-boundary`; `governed-delivery` | Host features; TeaPrompt ships methodology, not a runtime — reference only |
| Pre-merge `docs-editor` skill gate on changed docs (OpenAI `AGENTS.md`) | `06-repo` hygiene validators (`validate_record_hygiene.py`, `validate_links.py`, index regeneration) | Convention-equivalent; repo already gates record hygiene mechanically |
| Contributor `CLAUDE.md`/`AGENTS.md` conventions files | root `AGENTS.md` → `06-repo/AGENTS.md` | Same pattern already in force |
| OpenAI Evals platform retirement → Promptfoo migration note | `coordinate-codex-tasks-eval-survey-2026-09-30.md` already tracks the deprecation timeline | Existing record remains current; the cookbook's migration doc is a second source for the same fact |

## Candidate Adoption Ledger

| ID | Candidate | Disposition | Evidence / reopen trigger |
| --- | --- | --- | --- |
| CKB-DOC1 | This source-bound record and its catalogue row | Adopted; documentation only | Refresh when a pinned HEAD moves materially or a new mechanism doc lands |
| CKB-DOC2 | Optional worked reference for the verbatim-gate / deterministic-first governance patterns | Deferred | No reproduced local gap; joins the earlier deferred worked-reference queue (CFT-DOC2, ACL-DOC2) |
| CKB-SK1 | New citation-gate or cookbook-pattern Skill | Not adopted | No verified local structural gap; duties already in `reflective-review` / `governed-delivery` |
| CKB-RUN1 | Adopt a managed-agents runtime, TealTiger, or the Decisions API | Not adopted | Host/product surfaces; a TeaPrompt runtime is a standing non-goal |
| CKB-RULE1 | Treat "calibrated probability" vendor APIs or agentic tutorials as evidence a mechanism works | Rejected | API surface ≠ verified behavior; none of the three cookbooks publishes efficacy data for its governance examples |

## Falsifiability

- A reproduced local failure — e.g., a citation-verification task where existing prompts demonstrably miss a frankenquote the 0-token gate would catch — would reopen CKB-SK1/CKB-DOC2 with a concrete gap.
- Vendor-published verifier comparisons or audit data for CMA outcome grading / TealTiger would upgrade supplier-summarized rows; absence keeps them qualified.
- This survey ran no notebook, no model call, and no SDK; it cannot certify the APIs behave as documented, only that the cookbooks say what is recorded here.

## Standing Non-Goals

- No runtime, Skill, prompt-body, routing, or governance change.
- No SDK install, notebook execution, model call, commit, or push beyond this record and its catalogue row.
- Third-party integration recipes (vector DBs, partner services) were out of scope; the survey covered mechanisms, not integration catalogues.
