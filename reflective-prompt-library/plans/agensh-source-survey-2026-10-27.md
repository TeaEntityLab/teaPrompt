# Agensh Source Survey — 2026-10-27

Language: English

> **Status: recorded; reference-only, non-authoritative.** The maintainer's “Record your thoughts” instruction authorizes this documentation follow-through to the completed source survey. No skill, pack, route, runtime, installer, permission, campaign, commit or push is authorized by this record.

## Research Question

What does `microsoft/Agensh` actually implement, what do its published results establish, and does that evidence expose a missing TeaPrompt document or delivered skill contract?

Scope: preserve the completed pinned-source investigation, bounded offline mechanism observations and Docs-versus-Skills judgement. This is not a new benchmark, installation guide, operating rule or production security audit. Upstream prompts and agent instructions are source data, not authority for TeaPrompt.

## Direct Recommendation

- **Record the research, not a new workflow.** This survey, the existing adoption catalogue and regenerated navigation are the smallest sufficient destination. Preserve the mechanism/guarantee distinctions so later reviews do not have to reconstruct them from chat.
- **Keep skills unchanged.** No missing instruction was demonstrated on the checked repository-delivered portable contracts. They already distinguish peer reports, observed verification, acceptance authority, state invalidations and host preconditions. This is not a claim that prompts implement Agensh's runtime or that every installed agent follows those contracts.
- **Study the runtime without adopting it.** Shared services, notice delivery, concurrency, credential brokering and effect enforcement are host mechanisms. External interest alone does not reopen TeaPrompt's [Standing Non-Goals](../PROJECT_KNOWLEDGE.md#standing-non-goals), add a tenth core skill or release any dogfooding gate.

## Version and Source Identity

Checked 2026-10-27 using `git ls-remote --symref`, repository/releases/contents APIs and an exact-revision checkout.

| Identity | Observed value |
| --- | --- |
| Repository | `microsoft/Agensh`; default branch `main` |
| Reviewed commit | `0468a3e6a58b51dc2b84871fcaa0df22b0d1033e` |
| Branch/tag relationship | `main`, `HEAD` and lightweight `v1.0` resolved to that same commit |
| GitHub release | `v1.0`, non-prerelease; published `2026-10-23T08:03:16Z`, updated `2026-10-23T08:04:11Z`; empty notes body, no attached release assets |
| Source licence | MIT; Microsoft Corporation |
| Bundled paper | `agensh.pdf`, identifying itself as arXiv:2609.26781v1, technical report |

These are point-in-time identities, not current-version or production-readiness certifications. Refresh refs/releases, dependencies and host conditions before a future adoption or deployment assessment.

## Evidence Actually Checked

All external links below bind to the inspected source revision unless explicitly a release page. Source publication and inspection establish what is supplied or claimed, not the efficacy of the complete system.

- **S1 — framing and reported experiments; checked 2026-10-27:** [README](https://github.com/microsoft/Agensh/blob/0468a3e6a58b51dc2b84871fcaa0df22b0d1033e/README.md), [bundled paper](https://github.com/microsoft/Agensh/blob/0468a3e6a58b51dc2b84871fcaa0df22b0d1033e/agensh.pdf), [release v1.0](https://github.com/microsoft/Agensh/releases/tag/v1.0) and [MIT licence](https://github.com/microsoft/Agensh/blob/0468a3e6a58b51dc2b84871fcaa0df22b0d1033e/LICENSE). Main paper, implementation and experiment appendices were read.
- **S2 — reproducibility boundary; checked 2026-10-27:** [REPRODUCE](https://github.com/microsoft/Agensh/blob/0468a3e6a58b51dc2b84871fcaa0df22b0d1033e/REPRODUCE.md#experimental-conditions-and-release-differences), including release-versus-historical conditions and evaluation/export limits.
- **S3 — context and evidence labels; checked 2026-10-27:** [shared lessons](https://github.com/microsoft/Agensh/blob/0468a3e6a58b51dc2b84871fcaa0df22b0d1033e/board-service/shared_lessons.py), [text verifier](https://github.com/microsoft/Agensh/blob/0468a3e6a58b51dc2b84871fcaa0df22b0d1033e/board-service/verifier.py) and [board API](https://github.com/microsoft/Agensh/blob/0468a3e6a58b51dc2b84871fcaa0df22b0d1033e/board-service/main.py).
- **S4 — credential and execution boundaries; checked 2026-10-27:** [token service](https://github.com/microsoft/Agensh/blob/0468a3e6a58b51dc2b84871fcaa0df22b0d1033e/secret-service/main.py), [network overlay](https://github.com/microsoft/Agensh/blob/0468a3e6a58b51dc2b84871fcaa0df22b0d1033e/docker/docker-compose.pbench.yml), [worker entrypoint](https://github.com/microsoft/Agensh/blob/0468a3e6a58b51dc2b84871fcaa0df22b0d1033e/agent/entrypoint.sh), [proxy](https://github.com/microsoft/Agensh/blob/0468a3e6a58b51dc2b84871fcaa0df22b0d1033e/scripts/strip_metadata_proxy.py) and [generated infrastructure](https://github.com/microsoft/Agensh/blob/0468a3e6a58b51dc2b84871fcaa0df22b0d1033e/tools/gen-compose-prod.py).
- **S5 — merge and notice semantics; checked 2026-10-27:** [branch-protection bootstrap](https://github.com/microsoft/Agensh/blob/0468a3e6a58b51dc2b84871fcaa0df22b0d1033e/docker/bootstrap/bootstrap.sh#L266-L291) and [MCP notice shim](https://github.com/microsoft/Agensh/blob/0468a3e6a58b51dc2b84871fcaa0df22b0d1033e/mini-router/mcp-notice-shim.cjs#L127-L153).

Two read-only source scouts supplied navigation and challenges, not independent runtime measurements or a consensus panel. The coordinator checked decision-bearing claims against the pinned source and delivered local contracts. Third-party summaries and DeepWiki were not evidence. Semantic discovery was unavailable (403); literal searches and named source reads resolved scope. Python language-server support was not configured.

## Mechanisms and Boundaries

### Decentralized task choice still uses shared infrastructure

Agensh places an organization cooperation protocol above workers' native Copilot ACP loops: gather context, claim work, act, verify and integrate. Gitea supplies the workspace, Mattermost messaging, and a DeLM-derived typed board shared findings. “No central orchestrator” describes agent/task-allocation topology, not the absence of central MySQL, board, Git/chat and credential services. The cooperation sequence is prompt-driven, not a fully enforced acceptance state machine. Evidence: S1, S3–S5.

### Typed context helps navigation; its labels are not truth

`FACT`, `OBSERVED`, `FAIL`, `CLAIM` and `PATCH_SUMMARY` carry short gists with unfoldable detail. The recent view can deduplicate notes, replace a patch candidate and invalidate a textual verified label after a local counterexample. SQL gist history is a separate persistence path; in-memory observations do not establish database recovery.

`verify_note()` normalizes/caps strings and rejects placeholder evidence. It does not run tests. Supplying `evidence=pytest passed` without executing pytest yielded `ok:1/1`, followed by `status=verified` in the recent view. The renderer also describes these entries as candidate fixes requiring review. This is observed textual admission/rendering, not an acceptance oracle or a demonstrated forged-proof vulnerability. Evidence: S3 and the offline scenarios below.

### A work claim is not an exclusive lease

Eight concurrent same-scope claims were admitted in the in-process probe. A zero-TTL claim disappeared from the current view while its underlying recent-memory entry remained. Neither behavior supplies exclusive ownership, fencing or stale-writer rejection. Peer negotiation is part of the cooperation protocol; a typed `CLAIM` does not itself grant authority. Evidence: S3 and the offline scenarios below.

### Notice delivery is not proof of agent consumption

The MCP shim augments infrastructure tool results with DMs/gists, writes augmented output before acknowledgement and allows redelivery after acknowledgement failure. Snapshot preparation advances a reader watermark; it does not establish that an agent read or acted on every item. Explicit board reads and retained history are separate paths. This is source inspection, not an executed crash/replay or exactly-once-effect guarantee. Evidence: S3, S5.

### Security controls have specific, unproven outer boundaries

The token helper validates the whole identifier and canonical token path. Selected invalid names, an escaping symlink and empty-auth startup were refused. HTTP access uses shared `X-Internal-Auth`, also supplied to generated router configurations; canonical-path containment plus a shared internal credential does not establish per-agent subject binding. HTTP endpoints were not exercised.

Compose defines an internal worker network with proxy-mediated model egress. The proxy substitutes the configured upstream credential, and worker code configures permission-denial flags plus model-visible tool exclusions. These are inspected source controls, not live Linux/Copilot qualifications. The CI runner's host Docker socket is a privileged infrastructure boundary, not an observed host escape. Evidence: S4.

Bootstrap blocks ordinary direct pushes to main but allows the coders team to merge PRs with zero required approvals and no status-check gate. This serves the cooperative benchmark topology; it is not equivalent to independent acceptance of privileged effects. Evidence: S5.

## Reported Results: Evidence vs Inference

All results below are **author-reported, not locally reproduced**. Sources S1–S2 were checked 2026-10-27. Each comparison uses a six-hour wall-clock budget; equal elapsed time is not equal spend or token usage.

| Source population / model | Worker comparison | Reported final pass rate |
| --- | --- | --- |
| Five selected hardest ProgramBench tasks, GPT-5.6-sol high | 1 vs 128 | 19.31% vs 28.78% |
| Pandoc, GPT-5.6-sol high | 1 vs 1,024 | 33.89% vs 55.06% |
| Pandoc, GPT-6.1-sol high; README extension | 1 vs 32 | 56.19% vs 79.59% |

These support a reported quality/latency scaling result for the named populations and configurations. Equal-cost efficiency, general software-engineering ROI, hostile-agent safety and the isolated contribution of board, messaging or peer topology remain unknown. Cooperation trajectories are examples, not proof every team converges on a safe protocol.

S2 explicitly discloses release differences: the historical 1,024-worker run used 16 nodes while the release launcher is single-node; its v6 cleanroom/reference binary differs even when version strings match; CLI/MCP versions, output thresholds and archive behavior changed; export/cancellation cutoffs and staggered startup alter active time. Evaluation can exit zero while branches remain incomplete, so canonical-kept reporting and error/archive inspection matter. A release run needs its own source/evaluator/image/configuration identities; it cannot silently inherit historical reproducibility.

Four evidence dimensions remain separate: **existence** of pinned sources is verified; **number/text attribution** matches those sources; **generation/process** was not independently reproduced; **extrapolation** to TeaPrompt, equal spend or production reliability is unknown.

## Executed Verification

The completed investigation ran the actual inspected `secret-service/main.py`, `board-service/verifier.py` and `board-service/shared_lessons.py` mechanisms in clean-environment Python 3.14.7 under macOS Seatbelt. Module bodies were not edited/replaced; no third-party dependencies were installed. This documentation follow-through preserves that historical run rather than claiming another upstream execution.

Historical command; the owned temporary driver/profile were removed after preserving their contents and output:

```text
/usr/bin/sandbox-exec -f /private/tmp/teaprompt-agensh-survey-EC3Z7z/smoke.sb /opt/homebrew/opt/python@3.14/bin/python3.14 /private/tmp/teaprompt-agensh-survey-EC3Z7z/smoke.py
```

Result: **exit 0, PASS for 12 named mechanism scenarios and five containment controls, zero model calls**. PASS means the declared boundary outcome occurred, including refusals and advisory/textual behavior; it is not an overall Agensh certification.

| Scenario | Observed outcome |
| --- | --- |
| `token-name-positive` | Valid synthetic name accepted |
| `whole-token-name-rejection` | Four selected invalid whole names refused |
| `token-symlink-escape-rejection` | Escaping token symlink refused |
| `empty-auth-startup-refusal` | Startup refused with exit 2 |
| `text-evidence-accepted-without-test-execution` | Admission `ok:1/1`; no pytest execution |
| `placeholder-evidence-rejected` | `ok:0/1,ps_invalid_ev=1` |
| `evidence-beyond-stored-cap-rejected` | `ok:0/1,ps_invalid_ev=1` |
| `unknown-note-type-rejected` | `ok:0/1` |
| `overlapping-concurrent-claims-are-advisory` | Eight same-scope workers admitted |
| `claim-expiry-hides-view-without-deleting-retained-entry` | Current-view expiry without removal of the retained in-memory entry |
| `verified-rendering-is-textual-candidate-state` | Textual verified candidate state rendered |
| `local-counterexample-invalidates-patch-label` | Matching local failure invalidated that patch label |

The controls established scratch read/write, denied synthetic-canary read, denied outside-work write, denied loopback networking and child-inherited file denial before upstream imports. The sandbox denied `/Users` reads and confined writes, but its remaining read scope was not a complete confidentiality boundary. Concurrent asyncio calls do not establish multi-process/SQL concurrency or hostile-peer isolation.

| Inspected module | SHA-256 |
| --- | --- |
| `secret-service/main.py` | `c0cf776d68ff42c567e62112da899a3b52949c7d8a2db86b793c70b18f8f4da8` |
| `board-service/verifier.py` | `a7752426de8125c602e18a457621d7215acc5f670d4366eb27cc64c0f3108ea0` |
| `board-service/shared_lessons.py` | `8794761544d353356da4d5d0b7e26a9cc3765acf2fad6c49f4495d5f8c0cbded` |

The supplemental session receipt `agensh-smoke-2026-10-27.json` retains the exact driver/profile, environment and output. Driver SHA-256: `ee52496a705026e158c0ca8230414ae0274087029c9b1373b1d4aa654721e89b`; profile SHA-256: `ad3fda9317acbf4ad300c7369150d3e07bf80a50661f86e33883d9069fb11982`. The observations, source identities and decision limits needed to read this record are embedded above; the receipt and temporary checkout are not documentation dependencies.

No HTTP service, database, Mattermost, Gitea, Copilot ACP, merge, container deployment or benchmark was executed. No permanent upstream-smoke or survey-wording test is added to TeaPrompt.

## Assessment and Counterarguments

1. **[INFERENCE] The interesting contribution is organization, not a larger prompt catalogue.** Self-directed allocation, shared context and peer integration are worth studying together. Counterargument: a useful coordination pattern can sometimes be expressed in a portable skill. Decision: retain the example here; promotion still needs a demonstrated local instruction gap, not a runtime feature renamed as a skill.
2. **[INFERENCE] Recent views and retained history solve different problems.** The observed failure invalidation is a useful example for continuation integrity, but visibility, persistence and semantic truth are separate claims. Counterargument: requiring every agent to reverify every shared fact would discard the efficiency of cooperation. Decision: do not demand universal recomputation; preserve provenance and let the owning verifier/acceptor decide what evidence is sufficient. Existing handoff and review contracts already provide that distinction.
3. **[INFERENCE] Cooperative benchmarks can reasonably choose lighter governance than production systems.** Advisory claims and zero-approval peer merges are not automatically bugs. Counterargument: importing them unchanged into privileged-effect delivery could silently transfer acceptance authority. Decision: describe the topology and its boundary rather than condemn the research system or weaken TeaPrompt's gates.
4. **[INFERENCE] Scaling quality at a fixed deadline is valuable even without equal-cost superiority.** More workers may be appropriate when latency dominates. Counterargument: the headline agent count encourages general ROI or default-worker-count claims unsupported by these comparisons. Decision: preserve attributed results, total-resource uncertainty and release differences; infer no local default or causal component benefit.
5. **[INFERENCE] “No skill change” is not “nothing learned.”** The durable value is a discoverable, falsifiable comparison that avoids repeated novelty-driven promotion. Counterargument: recording every source can itself create archive bloat. Decision: use one source-bound record plus the existing catalogue/index; do not add a wrapper, decision-index lesson, new taxonomy or runtime proposal.

## Candidate Adoption Ledger

Only AGSH-DOC1 is completed as documentation by this follow-through. AGSH-1–AGSH-6 retain the research dispositions, not new adoption approvals.

| ID | Candidate | Disposition | Checked local surface / reopening evidence |
| --- | --- | --- | --- |
| AGSH-DOC1 | Pinned survey and catalogue/navigation entry | Recorded as reference evidence only | This record, [catalogue](external-adoption-case-studies-2026-06-20.md) and generated index. A current duplicate or contrary source identity would require consolidation/correction. |
| AGSH-1 | Self-assigned decentralized loop | Concept/reference only; no new core skill, pack or TeaPrompt runtime | [Standing Non-Goals](../PROJECT_KNOWLEDGE.md#standing-non-goals), [spec-plan](../skills/reflective-spec-plan/SKILL.md) Workflow Design Mode. Reopen on repeated verified local allocation failure plus explicit product-direction authority. |
| AGSH-2 | Typed context, failure memory, invalidation | Existing instruction coverage; no skill edit | [Handoff/Continuation Packet](../skills/reflective-handoff-retro/SKILL.md), [implementation](../skills/reflective-implement/SKILL.md) State Ledger/failure-signature discipline. Reopen on a local lost-state/invalidation failure exposing a missing delivered instruction, not merely noncompliance. |
| AGSH-3 | Verified labels and peer merge acceptance | Reject automatic transfer as proof/governance | [Review](../skills/reflective-review/SKILL.md) Claims Ledger/Four Evidence Dimensions, [governance scaffold](../skills/agent-governance-scaffold/SKILL.md) Methods/Never/Four-Power Split, [flow generator](../skills/flow-control-generator/SKILL.md) merged-result gate. Reopen if a delivered contract accepts self-report or branch tallies as sufficient proof. |
| AGSH-4 | Claims, notices, cursors, recovery | Host-runtime study only | [Spec-plan](../skills/reflective-spec-plan/SKILL.md) ownership/liveness contract and [runtime trust boundary](../04-agent/runtime-trust-boundary.md). Reopen on a required local guarantee the existing contract cannot state/check, with explicit authority to change ownership. |
| AGSH-5 | Credential broker and isolation | No Agensh installer/security-wrapper skill | [Risk](../skills/reflective-risk/SKILL.md) credential/sink rules, [governance scaffold](../skills/agent-governance-scaffold/SKILL.md) privileged-effect/receipt invariants and [headless CLI qualification](../skills/headless-agent-cli-contract/SKILL.md). Reopen on a demonstrated instruction-level gap; a missing OS mechanism is not repaired by prose. |
| AGSH-6 | Scaling and reproduction methodology | Record attribution/confounds; no worker-count default or new eval skill | [Research](../skills/reflective-research/SKILL.md) source/process/extrapolation checks, [review](../skills/reflective-review/SKILL.md) Four Evidence Dimensions and [flow generator](../skills/flow-control-generator/SKILL.md) total-budget caps. Reopen on controlled local evidence of a missing methodological instruction. |

## Falsifiability

- A reproducible local failure outside the checked delivered instructions, or contrary pinned-source/runtime evidence, reopens the corresponding candidate. A new version alone prompts freshness review, not automatic adoption.
- An equal-spend/token-normalized comparison with a declared population could change the efficiency judgement; component ablations could change attribution. Neither is supplied by the existing headline results.
- A crash/replay, HTTP identity, database concurrency, live tool-permission or hostile-worker experiment could establish or refute the particular operational guarantee it exercises. This offline probe does not settle those questions.
- A current duplicate discoverable record would make AGSH-DOC1 redundant. This is a source-specific archival decision, not a promotion into project operating policy.

## Residual Risks and Handoff

Unknown: independent benchmark generation/replication, general task transfer, equal-spend efficiency, live Linux/Docker/Copilot behavior, HTTP subject authentication, SQL transaction failure, notice crash/redelivery, merge safety, hostile-worker isolation, production tenancy and business acceptance.

The documentation decision is sufficient without resolving those deployment questions: preserve evidence and limits, retain current skills, and do not import runtime ownership. Repository documentation verification belongs to the [delivery report](../../review/final-report.md#agensh-survey-recording-2026-10-27), separate from the historical upstream-mechanism observations. Any future deployment or model campaign requires its own scope, authority and qualification.
