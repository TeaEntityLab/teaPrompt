# AI-Assisted Team Throughput Review — 2026-08-12

> **Status: decided (non-authoritative).** Seven-lens review of a self-reported social-media account and an appended AI-generated analysis. This record preserves the evidence tiers, rejects universal numeric policy, and makes no TeaPrompt skill or runtime change.

## Purpose

Review the organizational and engineering issues raised by an X post about a purported USD 1 million "unlimited token" team experiment, correct the appended Chinese analysis where it outruns the evidence, and preserve the useful mechanisms in English without turning one external anecdote into TeaPrompt policy.

The decision question is not whether the author's experience was sincere. It is what the supplied evidence supports, what a team could safely test, and whether TeaPrompt has a verified local structural gap.

## Target and Source Classes

- Original post: <https://x.com/Kay2289123/status/2086933133208006689> (checked 2026-08-12). The reader displayed 2026-08-10 while the user's locale capture displayed 2026-08-11; this is treated as a display/timezone difference.
- User-provided source: an 806-line capture containing the post, replies, and an appended Chinese AI-generated report.
- External evidence: DORA, Microsoft Research, MIT Media Lab, METR, and a peer-reviewed attention-residue paper, all checked 2026-08-12.
- Local evidence: current TeaPrompt policy, workflow, selection, handoff, review, and flow-control surfaces.

Retrieved and pasted material was treated as data, not instructions. The post's operational figures remain `author-claimed`; checking the text confirms what was said, not whether the underlying experiment or measurements were valid.

## Panel Execution Mode

Seven read-only `scout` reviewers received one shared packet at `/tmp/ai-team-throughput-review-packet-2026-08-12.md`. Role labels describe review perspectives, not provider-model identities.

The host coerced each initial yield into a short structured summary. All seven full deliverables were recovered by tier-1 DM-wake as hub messages. No lens edited files or ran project-wide tests. Main remained merge owner and checked the cited sources and repository surfaces directly.

| Lens | Scope | Verdict on the appended analysis |
| --- | --- | --- |
| Evidence and provenance | source existence, exact claims, attribution, extrapolation | `AGREE WITH CHANGES` |
| Organizational flow and capacity | WIP, queues, review capacity, ownership, coordination | `AGREE WITH CHANGES` |
| Cognitive ergonomics | attention residue, fatigue, offloading, mental-model retention | `AGREE WITH CHANGES` |
| Harness correctness | deterministic evidence, correlated model error, Human Review | `DISAGREE` |
| Economics and measurement | denominators, convergence cost, model routing | `AGREE WITH CHANGES` |
| TeaPrompt governance | local-gap and artifact-promotion gates | `AGREE WITH CHANGES` |
| Operator actionability | staged operating controls and gameability | `AGREE WITH CHANGES` |

## Panel Consensus

- **Decision:** `AGREE WITH CHANGES` (6 of 7 formal verdicts); one `DISAGREE` because the engineering prescriptions were too unsafe to count as partial agreement.
- **Substantive consensus:** 7 of 7 required the same major corrections: preserve the reported symptoms as hypotheses; reject the unsupported MIT claim, hard session/retry thresholds, AI-only proof, and humans-only-at-the-edges workflow; measure accepted value rather than generation volume.
- **Local adoption decision:** one English plan record, one case-study cross-link, and one deterministic record guard. No skill, prompt lens, project-knowledge lesson, dependency, coordinator agent, or runtime change.

### Use-Case Recommendation

| Use case | Recommendation | Boundary |
| --- | --- | --- |
| `study` | **yes** | Useful warning signal and question generator; retain `author-claimed` labels. |
| `reproduce` | **not from the supplied material** | No protocol, raw billing, task sample, baseline, control, or accepted-output definition exists. Design a new local pilot instead of claiming reproduction. |
| `adopt` | **select mechanisms only** | Small batches, bounded WIP, evidence-carrying work units, whole-loop cost, author ownership, and explicit acceptance gates are testable hypotheses, not universal policy. |
| `deploy` as an organization-wide policy or runtime | **no** | Calibrate locally first; TeaPrompt does not operate or enforce an agent runtime. |

## Required Wording Changes

The appended report should be rewritten with these corrections:

1. **Opening claim**
   - Reject: "The experiment reveals organizational systemic failure."
   - Use: "A self-reported post from one team describes high token spend, fatigue, review load, reduced synchronous coordination, and occasional AI-mediated drift. The underlying data and causal interpretation were not independently verified."

2. **Bottleneck claim**
   - Reject: "The AI bottleneck has moved from generation capacity to the carbon-silicon interface."
   - Use: "The report is consistent with a possible mismatch between generation rate and downstream human verification, integration, and decision capacity. DORA reports a related verification tax, but neither source proves a universal bottleneck shift."

3. **Cognitive terminology**
   - Replace `Mental KV-Cache Miss` with `attention residue` or `cognitive context-switching cost`.
   - Replace `brain rot`, `brain damage`, or equivalent language with the narrower observed or studied construct: `cognitive fatigue`, `reduced recall`, `lower reported ownership`, or `critical-thinking effort`, depending on the source.
   - Treat `carbon-silicon bandwidth` and `dual-agency dilemma` as optional analogies, not established scientific terms.

4. **Economic terminology**
   - Do not label the event a Jevons paradox or tragedy of the commons from the available evidence. Say that removing an individual usage constraint may increase generation while moving cost into review, rework, and coordination. The causal mechanism remains a hypothesis.

5. **Concurrency and retry policy**
   - Reject universal limits of two sessions or two failed iterations.
   - Use: "Set task-specific WIP and retry budgets from observed review capacity, task coupling, verification automation, risk, and convergence history. Recalibrate when queues, rework, defects, or human workload worsen."

6. **AI review**
   - Reject: "A second AI session provides independent adversarial verification."
   - Use: "A second model pass can generate objections, but it is advisory evidence. Correlated blind spots remain; objective checks, source provenance, and accountable human acceptance are still required where failure matters."

7. **Human role**
   - Reject: "Humans should own only requirements and final acceptance while the harness owns the middle."
   - Use: "Automate bounded, mechanically verifiable execution while preserving human ownership at specification, test-strategy, architectural, risk, escalation, and acceptance decisions. The human responsible for the result must retain enough system understanding to explain and maintain it."

8. **`AI-native` rhetoric**
   - Replace the label with the concrete missing capability: small batches, accessible context, stable priorities, author-side verification, explicit ownership, review capacity, recovery, or outcome measurement.

## Claims Ledger

| ID | Claim | What was checked | Status |
| --- | --- | --- | --- |
| X1 | A 20+ person team received a USD 1M unlimited-token budget. | Original post text exists and contains the claim. No employer, budget, protocol, or accounting evidence was available. | `author-claimed` |
| X2 | Peak individual daily spend was USD 7,000 and team median was USD 2,000. | Exact figures appear in the post; model mix, cache treatment, time window, billing export, and accepted-output denominator are absent. | `author-claimed` |
| X3 | Team members used roughly five parallel sessions and reported greater fatigue and review burden. | Exact report appears in the post; no baseline instrument or time-use log exists. | `author-claimed`; mechanism plausible |
| X4 | Cheap models sometimes cost more after repeated retries. | Exact report appears in the post; no controlled task comparison or routing history exists. | `author-claimed`; mechanism plausible |
| X5 | Meetings fell almost 80%, detail mastery declined, questions moved offline, and some AI-mediated exchanges drifted. | Exact report appears; meeting count does not establish coordination quality or causality. | `author-claimed` |
| U1 | `Mental KV-Cache`, `carbon-silicon bandwidth`, `dual-agency dilemma`, semantic entropy, and AI Jevons are established explanations. | Terms appear in the appended report; checked literature supports narrower constructs, not these combined labels. | metaphors / `[INFERENCE]` |
| U2 | Two sessions, two retries, and dual-session review are generally optimal. | No cited source or local calibration supports the thresholds or independence claim. | `refuted` as universal policy |
| U3 | Human-at-front-and-back plus an autonomous middle solves the problem. | Existing evidence supports automation for bounded work but also identifies verification, expertise, and integration risks. | limited-use hypothesis; unsafe as a default |
| E1 | DORA reports verification overhead, reviewer load, tool-sprawl toil, and an association between higher AI adoption, throughput, and instability. | DORA's 2026 analysis of 1,110 open-ended Google engineer responses was read directly. | source text `verified`; causality/generalization limited |
| E2 | GenAI confidence and self-confidence relate differently to reported critical-thinking effort. | CHI 2025 publication page: 319 knowledge workers, 936 examples; higher GenAI confidence associated with less critical thinking and higher task self-confidence with more. | source text `verified`; survey association, not causal trial |
| E3 | MIT found more than three parallel AI sessions cause "brain rot." | MIT project page: 54 initial participants, 18 in session four, essay-writing context, preliminary preprint; FAQ rejects damage language. | `refuted` |
| E4 | AI made experienced developers slower, therefore AI is generally unproductive. | METR's 2026 update confirms the early 19% slowdown estimate and says later estimates suffer severe selection and timing problems, including concurrent-agent measurement difficulty. | broad conclusion `refuted`; source caveats `verified` |
| E5 | Switching away from unfinished work can leave attention residue and impair the next task. | Leroy 2009 bibliographic abstract reports two experiments. | mechanism `verified`; no AI-specific numeric threshold |

## Candidate Adoption Ledger

| ID | Candidate | Status | Evidence | Next action or trigger |
| --- | --- | --- | --- | --- |
| ATT-1 | Durable English decision record | Adopted 2026-08-12 | Explicit user request plus seven-lens review | Keep this record self-contained; no temporary path as a live dependency. |
| ATT-2 | Cross-link from the external-adoption case-study index | Adopted 2026-08-12 | Existing no-change-record convention | Link this record and preserve the no-skill/no-runtime outcome. |
| ATT-3 | Deterministic guard for evidence tiers, rejected thresholds, dispositions, and cross-link | Adopted 2026-08-12 | Parallel Lens Review adoption-closure contract | Run focused record, hygiene, and link tests. |
| ATT-4 | Add outcome-normalized convergence cost and downstream review capacity to `04-agent/agent-selection.md` or `04-agent/workflow-recipes.md` | Deferred 2026-08-12 | Six lenses proposed variants; current selection already names token cost, human time cost, and failure cost, while loop/flow packs already require budgets and gates | Reconsider after repeated local routing errors show the existing factors cause bad decisions, or an explicitly approved in-place revision supplies local examples and focused tests. |
| ATT-5 | Add mandatory cognitive-WIP or context-handoff wording to core workflow policy | Deferred 2026-08-12 | Attention residue and DORA support the mechanism; no local recurrence or calibrated threshold was demonstrated | Reconsider after a local workflow repeatedly loses state or overloads review despite current handoff and bounded-concurrency contracts. |
| ATT-6 | Require a fresh session as independent proof for high-blast reviews | Rejected 2026-08-12 | Separate context may reduce anchoring, but it does not establish failure independence; high-risk work already requires evidence and Human Review | Re-litigate only with a concrete correlated-failure incident and a verifier stronger than session separation. |
| ATT-7 | Universal two-session or two-retry rule | Rejected 2026-08-12 | No source supports these thresholds; task coupling, risk, automation, and review capacity vary | A local controlled pilot with superior accepted outcomes and wellbeing would be needed to propose a scoped threshold. |
| ATT-8 | New coordinator agent, workflow skill, or TeaPrompt runtime | Rejected 2026-08-12 | Existing handoff, flow, review, and governance surfaces cover the methodology; owned runtime remains a standing non-goal | Reconsider only after the normal local recurrence and explicit approval gates fire. |
| ATT-9 | Promote a durable Project Knowledge lesson | Deferred 2026-08-12 | One external incident is not local recurrence evidence | Requires at least three local recurrences, a stable lesson, explicit human approval, and a durable evidence pointer. |

## Shared Findings

### 1. The post is a warning signal, not a controlled experiment

The source is useful because it names failure modes many teams can test: review queues, context switching, hidden human labor, weak routing, loss of shared context, and output drift. It cannot establish prevalence, causality, optimal thresholds, or return on investment.

Replies are not independent corroboration. They are a convenience sample affected by engagement ranking, self-selection, and visible spam.

### 2. Output is not throughput

Generated text, code, tokens, sessions, and meeting reduction are activity measures. Organizational throughput ends at accepted, integrated, useful outcomes. Faster generation can increase work inventory when review, testing, integration, product decisions, or deployment remain constrained.

Calling humans "the bottleneck" hides an authority distinction. Review capacity is a flow constraint; acceptance authority and maintenance accountability are governance responsibilities. The aim is not to route around humans, but to move mechanical checks earlier and reserve human judgment for decisions that cannot be delegated safely.

### 3. Bound work inventory, not browser tabs

Session count is a poor proxy for cognitive load. One tightly coupled task split across several agents can be easier to supervise than two unrelated architectural changes. Conversely, one large session can contain excessive unreviewed work.

A safer control is pull-based: start new generation only when the team can verify and integrate the resulting unit. Track active task units, unresolved decisions, unreviewed change size, and queue age. Any numeric limit should come from the team's task classes and baseline, not this post.

### 4. Price the whole convergence loop

The relevant cost includes model and infrastructure spend, human prompting and review time, retries, rework, integration, and escaped-failure cost. "Cheap model" and "expensive model" are task-specific labels once convergence and human time are included.

Model routing should be evaluated on comparable task classes using first-pass acceptance, time and iterations to acceptance, quality/stability, and total cost. A fixed cheap-first or premium-first rule is not supported.

### 5. AI criticism is not independent verification

A second model can broaden the objection set, but shared data, assumptions, prompt framing, tool limits, and incentives create correlated error. A persuasive debate transcript is not a deterministic gate. Review artifacts should carry source provenance, raw check output, acceptance-criteria traceability, assumptions, and unresolved risks.

### 6. Preserve human mental models deliberately

Writing less code is not itself deskilling, and manual work is not inherently virtuous. The risk arises when the accountable owner cannot explain the design, evaluate the evidence, or recover from failure without first asking an AI what happened.

Maintain understanding through small batches, author-written intent and acceptance criteria, review of high-leverage decisions, structured handoffs, incident drills, and occasional explanation or diagnosis without AI assistance where that capability matters.

### 7. Fewer meetings is an ambiguous metric

Meeting reduction can represent less waste or loss of synchronization. Pair it with decision latency, blocked work, rework from misunderstood decisions, incident coordination, and whether accountable owners can answer current-state questions from project evidence.

## Minimal Operating Playbook

This is a testable starting point, not TeaPrompt policy.

1. **Baseline before scaling.** Segment work by task type and risk. Record accepted throughput, whole-loop cost, review queue time, batch size, rework, stability, working time, and a lightweight owner-understanding check.
2. **Use pull-based WIP.** Admit new agent work only when an owner and an acceptance path exist and review inventory stays within locally chosen bounds.
3. **Make units evidence-carrying.** Each unit carries goal and acceptance criteria, base revision and tool/model configuration where relevant, bounded outputs/diff, raw checks and results, decisions and assumptions, residual risks, and a named human owner/gate.
4. **Verify at the author side.** Move compilation, tests, static checks, and policy checks before peer review. Do not let the generator weaken its own gate or treat test presence as proof of intent.
5. **Keep humans at leverage points.** Human judgment remains at ambiguous requirements, architecture, test strategy, security/permission/production boundaries, failed convergence, and acceptance. Routine mechanically checked execution may stay automated.
6. **Route from observed convergence.** Compare candidate models on representative tasks. Include human review time and failed loops. Escalate because the diagnosed failure calls for more capability, not merely because a counter reached two.
7. **Stop on queue or comprehension failure.** Pause new generation when review age, unverified inventory, rework, incidents, working hours, or owner understanding worsens beyond the pilot baseline. Diagnose missing context, weak acceptance criteria, environment defects, or model mismatch before spending more.
8. **Review the organization, not only the model.** Revisit priorities, batch size, context access, ownership, reviewer allocation, and recovery. Do not use `AI-native` as a substitute for a named mechanism.

### Minimum Metric Set

Use a small metric constellation; no single target is safe from gaming.

| Measure | Definition | Caution |
| --- | --- | --- |
| Accepted outcome throughput | Comparable accepted work units per elapsed period | Segment by task class; count alone rewards tiny or low-value work. |
| Total convergence cost per accepted unit | Model/infrastructure cost plus human prompting, review, retry, rework, and attributable failure cost | Requires consistent labor and task accounting; do not compare unlike outputs. |
| First-pass acceptance and iterations-to-accept | Share accepted without repair; loops before acceptance | High first-pass rates can reflect easy task selection or weak gates. |
| Review load | Human review minutes, queue age, and unreviewed inventory | Low review time can mean automation or neglect; pair with stability. |
| Batch and WIP | Active task units and change size awaiting acceptance | Lines/files are rough proxies for semantic complexity. |
| Stability and recovery | Escaped defects, change failures, rollback/recovery time | Lagging indicators; segment by risk. |
| Human sustainability and understanding | Working time/fatigue signal plus whether the accountable owner can explain key decisions and evidence | Do not turn comprehension checks into performance theater or surveillance. |

## Evidence vs Inference

### Observed

- The original post exists and contains X1–X5.
- The appended report contains U1–U3 and the named hard prescriptions.
- The cited external pages contain the study designs, sample sizes, findings, and limitations summarized in E1–E5.
- TeaPrompt already covers token/human/failure cost, bounded flow and loop budgets, deterministic gates, context handoff, claims ledgers, transition ownership, Human Review, and a no-owned-runtime boundary.

### Author-claimed

- The team, budget, spend, session median, fatigue, meeting reduction, routing economics, understanding loss, and chat-drift incident details.

### `[INFERENCE]`

- The likely transferable problem is a mismatch among generation, verification, integration, and human decision capacity.
- Pull-based WIP, evidence-carrying work units, whole-loop accounting, and preserved human ownership are safer experiments than fixed session counts.
- No TeaPrompt governed-surface change is justified yet because the current evidence is external and adjacent coverage already exists.

## Disagreements / Residual Risks

1. **Formal verdict severity:** the harness lens chose `DISAGREE`; six lenses chose `AGREE WITH CHANGES`. The substantive corrections were aligned, so the synthesis preserves the dissent without treating it as a different fact pattern.
2. **Immediate TeaPrompt repairs:** several lenses proposed additions to `agent-selection.md`, `workflow-recipes.md`, `context-handoff.md`, `reflective-review`, or `PROJECT_KNOWLEDGE.md`. The merge decision defers them: the user requested English documentation, current coverage is adjacent, and external evidence is not a verified local recurrence.
3. **Economic label:** one lens preferred a zero-price or commons framing. The record uses neither as settled fact because allocation rules, incentives, and output value are unknown.
4. **Numeric WIP:** the operator lens criticized arbitrary caps but then proposed its own two-item and two-retry limits. The synthesis removes those numbers and requires local calibration.
5. **Measurement burden:** whole-loop metrics can create surveillance, accounting overhead, and gaming. Start with a short pilot and the smallest useful set.
6. **Task diversity:** evidence from Google engineers, knowledge workers, essay writers, and experienced open-source developers does not directly estimate effects for every organization, model, or task.
7. **Human-review quality:** preserving a human gate is not enough if the human lacks time, expertise, independence, or authority. Acceptance design must address those conditions explicitly.

## Evidence Actually Checked

### External sources

- Original X post through the reader (checked 2026-08-12): <https://x.com/Kay2289123/status/2086933133208006689>.
- DORA, "Balancing AI tensions" (checked 2026-08-12): <https://dora.dev/insights/balancing-ai-tensions/>.
- Microsoft Research, CHI 2025 critical-thinking survey, DOI 10.1145/3706598.3713778 (checked 2026-08-12): <https://www.microsoft.com/en-us/research/publication/the-impact-of-generative-ai-on-critical-thinking-self-reported-reductions-in-cognitive-effort-and-confidence-effects-from-a-survey-of-knowledge-workers/>.
- MIT Media Lab, "Your Brain on ChatGPT" project page and FAQ (checked 2026-08-12): <https://www.media.mit.edu/projects/your-brain-on-chatgpt/overview/>.
- METR, 2026 developer-productivity experiment update (checked 2026-08-12): <https://metr.org/blog/2026-02-24-uplift-update/>.
- Leroy 2009 attention-residue bibliographic abstract (checked 2026-08-12): <https://ideas.repec.org/a/eee/jobhdp/v109y2009i2p168-181.html>.

### Repository surfaces

- `reflective-prompt-library/06-repo/AGENTS.md`
- `reflective-prompt-library/PROJECT_KNOWLEDGE.md`
- `reflective-prompt-library/04-agent/workflow-recipes.md`
- `reflective-prompt-library/04-agent/agent-selection.md`
- `reflective-prompt-library/04-agent/workflow-engine.md`
- `reflective-prompt-library/04-agent/artifact-promotion.md`
- `reflective-prompt-library/04-agent/external-adoption-review.md`
- `reflective-prompt-library/04-agent/workflow-acquisition.md`
- `reflective-prompt-library/03-context/context-handoff.md`
- `reflective-prompt-library/skills/reflective-review/SKILL.md`
- `reflective-prompt-library/skills/flow-control-generator/SKILL.md`
- `reflective-prompt-library/skills/flow-loop-harness/SKILL.md`

### Commands and execution evidence

- Read all 806 lines of the user-provided source.
- Used `cx overview` before targeted repository reads.
- Searched the relevant repository surfaces for cost, budget, concurrency, handoff, cognitive-load, prioritization, and verification concepts.
- Ran seven lenses in one parallel scout batch; recovered 7 of 7 complete deliverables by tier-1 DM-wake.
- `git branch --show-current` returned `main` after the panel.
- No private experiment, billing export, team interview, internal message audit, benchmark, or production pilot was executed.

## Falsifiability

This record should be revised if any of the following occurs:

1. The author publishes a protocol, raw billing and time-use data, task/outcome taxonomy, baseline/control design, and accepted-output results that materially support or refute the causal account.
2. A local TeaPrompt workflow repeatedly makes bad selection decisions because `token cost`, `human time cost`, and `failure cost` fail to expose whole-loop convergence or review capacity; that would fire ATT-4's in-place-repair trigger.
3. Repeated local workflows lose state or overload reviewers despite current bounded concurrency, evidence gates, and handoff contracts; that would fire ATT-5's review trigger.
4. A controlled team pilot shows that an explicit scoped session/retry threshold improves accepted throughput, stability, human workload, and system understanding across representative task classes; that could reopen ATT-7 without creating a universal rule.
5. AI-only adversarial review demonstrates failure independence against held-out correlated-error cases and deterministic acceptance gates; that could reopen ATT-6's narrower methodology claim, not prove universal independence.
6. The proposed metric set costs more to collect than the decisions it improves, or becomes a gameable productivity score; then remove or narrow it.

## Human Review

No high-risk action was taken. Any future organization-wide concurrency mandate, worker surveillance metric, billing policy, production gate, skill change, or runtime enforcement requires separate scope, local evidence, and the applicable Human Review gate.
