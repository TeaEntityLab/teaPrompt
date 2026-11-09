# Addy Osmani: Agent Management — Source Survey (2026-11-09)
Language: English

> **Status: recorded; reference-only, non-authoritative (`AOM-DOC1`).** The owner requested a survey of Addy Osmani's X status and then asked to continue. This record preserves source identity, all twelve article sections, product qualifications, scientific attribution and existing TeaPrompt coverage. No Skill, operating rule, acceptance oracle, runtime, installation, model campaign, commit or push is authorized by this record. Earlier surveys and their dispositions remain unchanged.

> **Owner-authorized documentation follow-through (2026-11-09):** the subsequent request to update Docs or Skills if worthwhile adds `AOM-DOC2` below. It repairs an installation-guide ambiguity in both languages; the initial source survey and AOM-SK1/W1/W2/RUN1 dispositions remain unchanged.

## Research Question and Direct Recommendation

Does *Your coding agents made you a manager* expose a useful mechanism missing from TeaPrompt, or mainly explain existing engineering discipline through a management analogy?

**Keep the source-qualified explanation, not a new management skill or runtime.** Its useful synthesis is to provide recoverable context and executable checks, partition independent work, preserve human decision ownership, and scale output only with review capacity. TeaPrompt already addresses these mechanisms. The article's impact ordering, productivity superiority and low rework cost are practitioner judgments, not controlled results.

The decisive qualifications are that a fresh model is not an independent execution oracle, a hook has event-specific failure/termination semantics, a worktree is not an OS sandbox, and session rewind is not complete effect recovery. The human reasoning study supports a bounded overreliance finding; it does not validate the author's self-counterargument remedy for coding work.

## Sources, Identity and Access

All external sources below were checked **2026-11-09**. Vendor documentation is a dated description, not evidence of an installed client's behavior. Its next relevant documentation/client change invalidates the corresponding product row.

| ID | Source and identity | Material actually examined / limit |
| --- | --- | --- |
| S1 | [Supplied X status](https://x.com/addyosmani/status/2119332146485891501); article `2118901185377964033`, *Your coding agents made you a manager*; checked 2026-11-09 | Native X unavailable. [FxTwitter response](https://api.fxtwitter.com/status/2119332146485891501) supplied the body, entity map and image references. Mirror reports creation and modification `2026-11-08T07:32:13.000Z`. All 105 blocks, including the inline Markdown example and image, were inspected. Mirror provenance is not authenticated native-X provenance. |
| S2 | [Your AI coding agents need a manager](https://addyosmani.com/blog/coding-agents-manager/), author blog, 2026-01-08; checked 2026-11-09 | Linked predecessor with a different title and body; not a substitute for S1. |
| S3 | [Cognitive Surrender](https://addyosmani.com/blog/cognitive-surrender/), author blog, 2026-05-05; checked 2026-11-09 | Practitioner interpretation linking the human study, alongside the author's proposed habits. |
| S4 | Shaw & Nave, *Thinking—Fast, Slow, and Artificial: How AI is Reshaping Human Reasoning and the Rise of Cognitive Surrender*, manuscript `v20260111`; checked 2026-11-09 | Full 58-page manuscript text accessible through a [Readwise-hosted PDF mirror](https://readwise-assets.s3.amazonaws.com/media/wisereads/articles/thinking-fast-slow-and-artific/1184.pdf). Coordinator read the methods, confidence, intervention and synthesis passages. Direct [SSRN abstract](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6097646) and PDF requests returned HTTP 403. This is preprint/working-paper evidence through a mirror, not authenticated journal publication or reproduced data. |
| S5 | [Claude Code best practices](https://code.claude.com/docs/en/best-practices.md), checked 2026-11-09 | Current guide and the specific official mechanism pages linked below; documentation only, no Claude session exercised. |
| S6 | [Git worktree documentation](https://git-scm.com/docs/git-worktree), checked 2026-11-09 | Separate working trees with shared repository administration; complemented by the disposable execution below, not by a Claude-runtime test. |

### Extraction receipt

Block IDs `B001`–`B105` below are one-based positions in `tweet.article.content.blocks`, not native article paragraph numbers. A JSON-array count and an independent raw-serialization type-token count both returned 105: 65 unstyled, 26 unordered-list items, 12 headings and 2 atomic blocks. The embedded Markdown payload at B023 was recovered from the entity map; merely reading each block's `text` would miss it.

- Raw fetched JSON SHA-256: `63c92088fb2a085f030bcde1ac77a6e9332c51a1717ff82f13dc6c3ec841ae3e`.
- Plain-block SHA-256: `89930adfc9b41497d1b85efa3900e545baa42a7f161a15d621be7f00a8a70104`, over UTF-8 `"\n".join(block.get("text", "") for block in blocks)`, with no trailing newline. This digest excludes the separate entity payloads and image bytes; the raw-JSON digest covers the embedded metadata/payload, not downloaded image bytes.
- B023's dashboard-performance numbers are explicitly illustrative, not a benchmark.
- The cover and B104's Pangram detector image were viewed. The latter displays “Human-Written” with AI 10%, AI-assisted 0%, Human 90%; that display is neither an authenticated authorship record nor a validated detection result.
- Session evidence: `local://addy-manager-packet-2026-11-09.md`, `local://addy-manager-ledger-2026-11-09.json`, and `local://addy-manager-worktree-2026-11-09.json`. These are supporting receipts; the conclusions and bounds are preserved here without requiring those temporary paths.

## Twelve-Section Assessment and Delivered Coverage

Coverage means the named current contract contains the method, not that agents reliably follow it. B001–B005 define management as enabling outcomes and explicitly deny that agents replace human managers or colleagues; the analogy should be judged on that narrower claim.

| Article section / blocks | Assessment and qualification | Existing TeaPrompt surface |
| --- | --- | --- |
| Give it a way to check its work, B006–B015 | Strong practical advice: inspect observed results rather than a completion declaration. A build proves its assertions; a screenshot supports what is visible. Neither establishes every acceptance criterion. Product-specific evaluators differ below. | [Implement](../skills/reflective-implement/SKILL.md), State Ledger and Verification; [Review](../skills/reflective-review/SKILL.md), Claims Ledger and Evidence Tiers. |
| Set clear context, B016–B025 | Preserve intent, constraints, exclusions and observable success; retrieve discoverable facts rather than asking the owner to restate them. “The agent can discover it” still depends on access and an actual read. Exploratory tasks can use a bounded question rather than a premature full spec. | [Brief](../skills/reflective-brief/SKILL.md), Workflow, spike framing and Intent Fidelity; [Spec/Plan](../skills/reflective-spec-plan/SKILL.md), Planning Fidelity. |
| Make every correction compound, B026–B034 | Useful learning loop, but two corrections do not automatically authorize a policy write or new skill. Revalidate old lessons and distinguish a repair from promotion. | [Handoff/Retro](../skills/reflective-handoff-retro/SKILL.md), Memory Consolidation and Project-Knowledge Promotion Contract; [harness policy](../06-repo/AGENTS.md), Harness Policy and Project Knowledge Layer. |
| Let it decide; enforce what cannot bend, B035–B041 | Keep preferences lightweight without weakening a safety floor. “Always enforced” needs a named hook type, event, failure policy and reachable effect boundary; classifier judgment is not deterministic enforcement. | [Minimality](../skills/reflective-minimality/SKILL.md), Safety Floor; [Governed Delivery](../skills/governed-delivery/SKILL.md), host preconditions and Never rules. |
| Plan before it builds, B042–B046 | Define interfaces and disjoint ownership before parallel editing. Separate checkouts reduce edit collisions but do not eliminate integration conflicts or enforce process confinement. | [Spec/Plan](../skills/reflective-spec-plan/SKILL.md), Planning Fidelity; [Flow Control](../skills/flow-control-generator/SKILL.md), Script Contract and merged-result gate; [Workflow Recipes](../04-agent/workflow-recipes.md), disjoint evidence slices. |
| Steer early, reset fast, B047–B051 | Repeated failure should change strategy, not add identical retries. “Two attempts” is a heuristic, not a universal budget. A fresh session must carry canonical state; rewind has incomplete coverage. | [Implement](../skills/reflective-implement/SKILL.md), Failure Loop; [Handoff/Retro](../skills/reflective-handoff-retro/SKILL.md), Continuation Packet; [Runtime Trust Boundary](../04-agent/runtime-trust-boundary.md), External Effect Recovery Boundary. |
| Delegate the task, never the judgment, B052–B058 | Human ownership of product, security and release decisions survives delegation. Green tests and reasonable names are not product acceptance. The author's almost-shipped complexity example is an anecdote, not comparative evidence. | [Governed Delivery](../skills/governed-delivery/SKILL.md), named acceptance and Delivery Invariants; [Review](../skills/reflective-review/SKILL.md), observable evidence rather than persuasive narrative. |
| Design the run that does not need you, B059–B069 | Definition of done, checks, permissions, budgets, output location and approval form a useful checklist. A pilot of three files is an example, not a sufficient safety certificate. | [Governed Delivery](../skills/governed-delivery/SKILL.md), task packet, oracle split, envelope and acceptance; [Flow Loop](../skills/flow-loop-harness/SKILL.md), bounded externally verified iteration. |
| Scale verification, not attention, B070–B074 | Pair throughput with rework/quality; review capacity constrains useful parallelism. Four or five background agents and an increasing “orchestration tax” are the author's experience, not a measured capacity law. Dashboards and notifications are host features. | [Review](../skills/reflective-review/SKILL.md), evidence channels; [Workflow Recipes](../04-agent/workflow-recipes.md), bounded review packets; [Handoff/Retro](../skills/reflective-handoff-retro/SKILL.md), Gate Retro. No new telemetry runtime. |
| Decide what not to build, B075–B079 | Ask whether the work should exist before optimizing execution. Cheap generation does not eliminate review, maintenance, integration or incident cost. | [Minimality](../skills/reflective-minimality/SKILL.md), Minimality Ladder; [Brief](../skills/reflective-brief/SKILL.md), outcome, failure conditions and falsifiability. |
| Where the analogy breaks, B080–B090 | Human management, junior training and team cohesion are distinct organizational responsibilities. Model changes and correlated errors matter; “one archetype” and “almost free” rework are not universal facts. Human-study transfer is bounded below. | [Review](../skills/reflective-review/SKILL.md), human-behavior evidence dimensions; [Research](../skills/reflective-research/SKILL.md), population/task/intervention limits; [Workflow Recipes](../04-agent/workflow-recipes.md), preserve dissent despite consensus. Human personnel management remains outside scope. |
| You do not need the title, B091–B103 | A useful synthesis of context, checks, planning, learning and ownership; not evidence that these practices turn an engineer into a people manager or establish their relative impact. | [Harness policy](../06-repo/AGENTS.md), goal/scope/acceptance and evidence-backed completion. No additional workflow needed. |

## Product Claims: Documentation Is Not Execution

These are **2026-11-09 documentation checks**, not observed Claude Code runs or security certifications.

| Surface / source | What holds | Material boundary |
| --- | --- | --- |
| [`/goal`](https://code.claude.com/docs/en/goal.md), B012/B064; checked 2026-11-09 | A separate small-fast-model evaluator judges the completion condition after eligible turns. | It reads what Claude surfaced in the conversation and cannot independently read files or run commands. Background work defers evaluation. A model verdict and a prose turn/time clause are not an external oracle or a host-enforced budget. |
| [Hooks guide](https://code.claude.com/docs/en/hooks-guide.md), B013/B036/B040/B065; checked 2026-11-09 | Command hooks can run checks at lifecycle events; prompt/agent hooks ask a model to judge. | The documented Stop override occurs after eight consecutive blocks **with no Claude tool call between them**; the cap is configurable. Hook invocation does not mean every hook is deterministic or an unbreakable completion gate. The general guide also documents non-blocking error paths; event-specific behavior matters. |
| [Permissions and sandbox guidance](https://code.claude.com/docs/en/best-practices.md#limit-access-with-permission-rules-and-the-sandbox), B040/B066; checked 2026-11-09 | Deny rules and managed settings move requirements out of prose; OS sandboxing can constrain shell filesystem/network access. | The guide says a `Read` rule can catch a recognized `cat` but not a script opening the file; a WebFetch deny is not a curl deny without sandboxing. Auto mode is a classifier that can be wrong. These mechanisms are complementary, not interchangeable. |
| [Permission modes](https://code.claude.com/docs/en/permission-modes.md), B040; checked 2026-11-09 | Current docs describe auto as the built-in starting mode for eligible terminal/VS Code sessions. | Explicit settings, host surface, version and availability change that default. Routine pushes to the current repository, including its default branch, may run without a prompt; force-push/production concerns do not imply a blanket no-push gate. No such mode was enabled here. |
| [`/batch` command](https://code.claude.com/docs/en/commands.md), B046; checked 2026-11-09 | Documents decomposition into 5–30 units and separate worktrees. | Work starts **once the plan is approved**. Each worker opens a PR **or reports what happened**; a PR per unit is not guaranteed. The count is this bundled skill's documented shape, not a task-independent optimum. |
| [Checkpointing](https://code.claude.com/docs/en/checkpointing.md), B051; checked 2026-11-09 | `/rewind` can restore tracked code and/or conversation. | Bash-only edits to untracked files remain; later Bash edits to a file already tracked by the session can be restored. Foreground forked-skill edits are covered, whereas other subagent edits to previously untracked files remain. Symlink/hard-link paths are skipped. Rewind is not a substitute for Git or compensation of external effects. |
| [Subagents](https://code.claude.com/docs/en/sub-agents.md), B014/B088; checked 2026-11-09 | Separate contexts and configurable model/tool profiles exist. | Fresh context can reduce shared conversation bias, not prove independent mistakes or review correctness. Different profiles/models make a universal single-archetype claim too broad; heterogeneity alone does not establish decorrelation. |

B086's machine-local auto-memory warning usefully motivates shared, reviewed project knowledge. It does not warrant moving every remembered correction into operating policy. No personal memory, hook configuration or permission setting was changed.

## Human Study: Finding, Denominator and Remedy

**Checked 2026-11-09:** S4's manuscript uses seven open-ended Cognitive Reflection Test questions, a survey-embedded GPT-4o assistant and hidden seed prompts producing correct or intuitive-but-wrong answers with rationales. Samples came from a university behavioral lab and Prolific, not a software-development study. It reports a pooled synthesis of 1,372 participants and 9,593 trials; those are the paper's figures, not an independently reconstructed dataset.

| Evidence | Reported result | Scope / interpretation |
| --- | --- | --- |
| Pooled wrong-answer adoption, p. 44 | 73.2% | Among trials **where the assistant was consulted and was wrong**. Not 73.2% of all people, all trials or developers. |
| Study 1 global post-task confidence, p. 25 | AI-assisted 77.0%; brain-only 65.3%; difference 11.7 percentage points | AI access increased reported confidence despite approximately half the AI answers being faulty. This is not a measured gain or loss across every calibration/metacognition construct. |
| Study 2 intervention, pp. 27–28 | Time pressure versus no timer | A manipulation of deliberation conditions, not self-critique prompting. |
| Study 3 intervention, pp. 33–34 | Incentives plus immediate item-level correctness feedback; faulty-answer override 42.3% versus 20.0% in its control | A combined intervention; cannot assign the effect to incentives alone, feedback alone or a model arguing against itself. The pooled 73.2% is not this control baseline. |

The methods identify time pressure and incentives/feedback as the interventions. A text search across the full converted manuscript for `argue against`, `self.critique`, `self.criticism` and `dialectical` found none; the same search found the known-present `Incentives + Feedback` control phrase. Together with the study designs, this supports the narrow conclusion: **this study does not test the self-counterargument prescription in B087**. It does not prove that such prompting never helps.

S1 places the prescription next to the Wharton finding, but does not explicitly state that the study tested it. Preserve the attribution split rather than accuse the author of claiming a trial he did not describe. In coding, tests, execution and review introduce verification channels absent from these CRT tasks. The finding is a reason to investigate overreliance, not a measured coding failure rate or proof that a particular prompt repairs human judgment. Study data, appendices/exclusion accounting and a possible later publication were not independently audited.

## Executed Boundary Check: Worktrees

**Observed 2026-11-09:** actual Git CLI `git version 2.54.0 (Apple Git-157)` plus a same-user Python subprocess, in a disposable repository with no remote. Hooks and commit signing were disabled for the fixture. A fixture-only initial commit supported two detached worktrees created with `git worktree add --detach`; no TeaPrompt commit was made.

The worker's current directory was worktree A. It wrote A's `sample.txt`, then read and wrote B's explicitly supplied sibling path. All Git setup commands and the worker exited 0.

| Observation | Value after worker exit |
| --- | --- |
| Main checkout `sample.txt` | `baseline` |
| Worktree A `sample.txt` | `worker-a-local` |
| Worktree B `sample.txt` | `cross-worktree-write` |

The positive local-write control proves checkout separation; the successful sibling read/write disproves process confinement by **plain Git worktrees alone**. This does not test or bypass Claude Code's additional permission/worktree checks, an OS sandbox, network controls or hostile concurrent workers. Both worktrees and the fixture repository were removed by the temporary-directory context; the command/worker receipt remains in the session evidence.

## Evidence vs Inference and Adjudication

- **Observed:** complete mirrored article extraction, entity/example recovery, viewed images, author predecessor distinction, current vendor text, the primary manuscript's reported results/design, current local contracts, and the Git/Python file effects above.
- **Author claims:** managerial impact ordering, personal parallel-session capacity, near-free rework, and the proposed overconfidence remedy. None became local efficacy measurements.
- **[INFERENCE]:** the management analogy is useful explanatory material, but no verified missing contract warrants a Skill change. The stronger alternative explanation is familiar specification, verification and ownership discipline expressed in management vocabulary, rather than a new agent-management mechanism.
- **Counterargument:** an existing requirement may be difficult for users to discover or apply; good worked explanations can still help. That justifies this reference, not a new gate without a concrete failure or owner decision.
- **Research process:** three read-only scouts examined product mechanisms, the cognition citation and local coverage. The coordinator re-read decisive sources and ran the worktree check. This was parallel evidence gathering, **not** a consensus panel, multiple independent model replications or a paired efficacy trial.
- **Adjudicated scout proposals:** missing universal diff-size limits and a standardized post-merge metric schema are not confirmed defects. Bounded packets, task-shaped plans, review evidence and gate retros already exist; production metrics need a host/owner. Several returned line references did not match current source positions, so the map above uses checked sections rather than those anchors. `PROJECT_KNOWLEDGE.md` supplies non-authoritative design judgment, not operating authority.
- **Retained research correction:** the cognition scout initially mixed a pooled rate with an intervention comparison; these denominators are separated above. Its later explanation of the aggregate sample discrepancy was inferred, not independently checked, and is not adopted as a fact here.

## Candidate Adoption Ledger

| ID | Candidate | Disposition | Evidence / reopen trigger |
| --- | --- | --- | --- |
| AOM-DOC1 | Source record and catalogue discovery | Recorded; reference-only | Preserve the distinct November article, full-section map, mechanism exceptions, study boundaries and executed worktree result. |
| AOM-DOC2 | Distinguish invocation control from action authorization and acceptance in the existing installation guides | Adopted documentation clarification under the subsequent owner request | The English guide mapped review declarations directly to invocation controls; the translation said those controls execute Human Review. Current vendor documentation establishes only invocation semantics. No Skill or host setting changes. See the follow-through below. |
| AOM-SK1 | New agent-management Skill or extra core rules | No change | Existing contracts cover the mechanisms. A reproduced local failure against a named contract could justify an in-place repair; new-skill promotion retains its separate gate. |
| AOM-W1 | Universal diff-size ceiling / mandatory chunk gate | Not adopted | No consumer failure establishes a threshold or missing rule. Reopen on an accepted change whose review missed a specific interface regression because the declared review scope could not be handled, with the current contract and evidence preserved. |
| AOM-W2 | Standard post-merge rework/throughput ledger | Not adopted | Metrics are useful but no local requirement or host telemetry owner was established. Reopen on an owner-defined outcome and evidence that current gate retros fail to carry it. |
| AOM-RUN1 | Claude hooks, classifiers, dashboards or unattended runner adoption | Not adopted; outside this survey | No installation or runtime grant. Host containment and effect authorization require separate evidence; a documentation survey supplies neither. |

## Falsifiability and Handoff

- Native article recovery or a different body/entity digest could change S1 attribution or coverage; it would not retroactively turn the January predecessor into the same source.
- A changed Claude documentation/client version invalidates the corresponding product row. A configured-host probe could establish its actual stop, rollback or containment behavior; this Git-only check cannot.
- A controlled coding study testing self-counterargument, with error detection and confidence/calibration outcomes, could support the currently unverified remedy. More confident prose or agreement among reviewers cannot.
- A real local consumer failure could reopen AOM-SK1/W1/W2. External recurrence alone is not that failure; missing usage evidence is unknown, not zero demand.
- Sufficiency: the source, material qualifications, current coverage and narrow execution are checked; native-X authenticity, model utility, human learning transfer and complete study-data verification remain explicit unknowns. None is required for the reference-only decision.

Publication touches only this record, the existing external-adoption catalogue, regenerated `index.json` and the [delivery report](../../review/final-report.md#addy-osmani-agent-management-survey-2026-11-09). Repository checks establish discoverability/consistency, not the article's efficacy or host enforcement. No permanent test, Skill, policy, registry entry or runtime change is introduced.

## Documentation Follow-Through — Invocation Is Not Approval (2026-11-09)

The owner subsequently requested worthwhile Docs/Skills updates and a separate
mini-swe-agent survey. Rechecking the existing installation instructions found a
narrow local documentation problem, not a missing management Skill:

- The English guide told installers to map `human_review_required` to invocation
  controls under “Enforcing TeaPrompt's review gates host-side.”
- The zh-TW guide said the host's invocation control actually executes Human
  Review. Restricting who can invoke a Skill does not establish that claim.
- [Claude Code's Skill documentation](https://code.claude.com/docs/en/skills.md#control-who-invokes-a-skill),
  checked 2026-11-09, describes `disable-model-invocation` as preventing automatic
  invocation. [Codex's Skill documentation](https://learn.chatgpt.com/docs/build-skills),
  checked 2026-11-09, describes `allow_implicit_invocation: false` as disabling
  implicit selection while preserving explicit invocation. Neither setting is
  evidence of per-action authorization or acceptance.

`AOM-DOC2` clarifies [the English guide](../SKILL_INSTALLATION.md#enforcing-teaprompts-review-gates-host-side)
and [the zh-TW guide](../SKILL_INSTALLATION.zh-TW.md#安全性注意事項):
metadata declares intent; invocation controls only restrict triggering; action
permissions, required human checkpoints and evidence-based acceptance remain
separate. No installed copy, host permission, Skill, oracle or runtime changed.
The earlier S5 qualifications still apply; no configured Claude/Codex session was
exercised. Reopen this wording if the linked hosts change these controls' semantics.

Twin search covered `invocation control`, `呼叫控制`,
`disable-model-invocation` and `allow_implicit_invocation` across the library.
The two current guides were corrected. The similar mapping in
`skills-surface-plan-2026-07-11.md` is a historical proposal, not an additional
current enforcement contract; it is not retroactively rewritten. The
[delivery report](../../review/final-report.md#mini-swe-agent-survey-and-addy-documentation-follow-through-2026-11-09)
records the exercised publication checks and their limits.
