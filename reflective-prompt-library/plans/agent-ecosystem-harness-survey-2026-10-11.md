# Agent Ecosystem and Harness Survey (2026-10-11)

> **Status: decided — research-reference-only; no skill, pack, routing, runtime, dependency or oracle adoption.**
> All seven supplied inputs are addressed. Company figures remain source-reported, with access and denominator limits below.
> This decision archive is evidence, not agent operating instructions, a host-adoption decision or a campaign grant.

## Research Question and Authority

User request: survey the supplied production-setup synthesis, arXiv `2606.20683`,
`addyosmani/agent-skills`, `anthropics/claude-quickstarts`, `wshobson/agents`,
`anthropics/knowledge-work-plugins`, and `msitarzewski/agency-agents`.

Which mechanisms are useful to TeaPrompt, what do the sources actually establish,
and is there a verified local gap warranting a change?

Strictness: L3 research/content work. The deliverable is this record plus generated
discovery metadata. It does not authorize installing plugins, running upstream
programs, invoking models, changing governance, promoting project knowledge,
committing or pushing. The [canonical policy](../06-repo/AGENTS.md),
[external-adoption review](../04-agent/external-adoption-review.md), and
[existing project judgement](../PROJECT_KNOWLEDGE.md#lesson-external-tool-adoption-is-mechanism-vs-product-local-gap-gated)
retain their separate authority.

The private Apple-runtime qualification is a different workstream, not evidence
for any surveyed repository. TEST-001 consumer/scorer adoption and named
host/capture/leak-audit owners, and Stage-1/TEST-002–004 campaign approval, remain
owner-held. This survey closes none of those gates.

## Direct Recommendation

Retain the mechanisms as references; make no installed change. Three distinctions
carry the decision:

- A production job, a runtime responsibility, a workflow skill and an agent persona
  are different objects. Ten job labels and large rosters do not justify additional
  core routing rows.
- Prompt guidance, configuration declarations, executable hooks and demonstrated
  enforcement are different evidence classes. Source inspection establishes the
  first three, not live containment or safe deployment.
- The evidence supports task-conditional model–harness interaction, not “the model
  is the smallest part,” “six rules guarantee success,” or a universal multi-agent
  advantage.

Useful references include independent verification, scope restraint, explicit
source failure, acknowledgement-bound state updates, provenance-aware memory and
portable context packaging. Existing TeaPrompt contracts positively cover those
concerns. Two adjacent ideas—diff-scoped floor checks and targeted mutation during
review—remain inert investigation candidates, not reproduced local defects.

## Source Identity, Version and Access

All source checks below were made on **2026-10-11**. Exact repository revisions were
obtained with `git ls-remote --symref <repository-URL> HEAD`, shallow-cloned,
detached at the selected SHA and checked with `rev-parse` equality. These are
checked `main` snapshots, not release-tag claims. New revisions or changed host
capabilities require fresh inspection before reuse.

| Input | Checked identity and access | Copy/delivery boundary |
| --- | --- | --- |
| Production synthesis | `local://paste-4.md`, 269 lines, 24,018 bytes; SHA-256 `4f087af20e0f2dfa07cc5cf392eb70402ffbf8403807a56880865a609dbf5846`; full input read | Unattributed secondary synthesis; its citations are claims about sources, not primary evidence. No underlying “70+ posts” corpus supplied. |
| Paper | [From Question Answering to Task Completion: A Survey on Agent System and Harness Design, v1](https://arxiv.org/abs/2606.20683v1), published 2026-06-14; [versioned PDF](https://arxiv.org/pdf/2606.20683v1), full extracted study and references read; checked 2026-10-11 | Literature/benchmark synthesis, not an executable harness; publication metadata does not establish peer review. No paper text or code imported. |
| Engineering workflows | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills/tree/1be8e34187e34647bb83adc3a1323b26ae6f6abe), `1be8e34187e34647bb83adc3a1323b26ae6f6abe`; committed 2026-10-10; checked 2026-10-11 | MIT repository; external rule registries can have different licences. Portable skills plus native integrations, scripts and optional host hooks. |
| Reference applications | [anthropics/claude-quickstarts](https://github.com/anthropics/claude-quickstarts/tree/9ec32b91df50b0d4906cae64b13c6298055ff40d), `9ec32b91df50b0d4906cae64b13c6298055ff40d`; committed 2026-10-07; checked 2026-10-11 | Root MIT; `autonomous-coding/README.md` also says “Internal Anthropic use,” an unresolved component-level licence statement. Support app is explicitly a prototype. |
| Multi-harness marketplace | [wshobson/agents](https://github.com/wshobson/agents/tree/46891e7e60da0e52baf1050b7b6391b64e84c6d9), `46891e7e60da0e52baf1050b7b6391b64e84c6d9`; committed 2026-10-04; checked 2026-10-11 | MIT root; remote marketplace entries have their own licences. Prompt components, adapters and host-executed governance hooks are distinct surfaces. |
| Knowledge-work plugins | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins/tree/02ffa99ff00ce4d3046ccebabb8357cb39f3ab06), `02ffa99ff00ce4d3046ccebabb8357cb39f3ab06`; committed 2026-10-11; checked 2026-10-11 | Apache-2.0 root; partner-built Slack, Zoom, Apollo and Brand Voice declare MIT, Common Room Apache-2.0. Connectors require separate services, credentials and permissions. |
| Persona catalog | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents/tree/f99f6aa910a442b0197b768ce0ea7751e35e2060), `f99f6aa910a442b0197b768ce0ea7751e35e2060`; committed 2026-10-07; checked 2026-10-11 | MIT; Markdown personas plus conversion/install utilities and a separately distributed app. No app downloaded or installer executed. |

### Prior Local Decisions and Search Bound

Literal source-name/repository-ID searches in the current library, including
`plans/` and `PROJECT_KNOWLEDGE.md`, did not recover an earlier source-specific pin
for these five repositories or this paper. The same search facility detected the
known-present `obra/superpowers` control. Semantic `find` could not judge files
because its upstream API returned 403; its “no hits” output is not absence evidence.

Broader Osmani-name searches recovered the
[DevOps/agentic trends record](devops-agentic-trends-survey-2026-09-28.md) and
[Software Factory inner/outer-loop record](software-factory-sdlc-inner-outer-loop-survey-2026-09-28.md).
Their human-intent, decorrelated-verification and host-enforcement boundaries are
relevant conceptual baselines, not prior repository revisions. This is a first
recovered pinned inspection, not a fabricated release delta or a claim that no
prior conversation exists.

## Evidence Actually Checked

### Evidence Classes and Retrieval Limits

`verified` below means the stated source text or pinned implementation was
inspected. It never means that company telemetry, model efficacy or deployed
security was independently reproduced. `needs-qualification` preserves a material
scope, attribution or access limitation. `unknown` retains a claim the available
source access could not establish; `refuted` names the exact stronger claim rejected.

The parent read the paper and selected local/source sections; seven read-only
scouts inspected the five snapshots and both halves of the paste's citations.
Their reports were advisory inputs, not adoption authority. Counts and load-bearing
recommendations were reconciled during integration. No upstream demo, generator,
eval harness, hook, installation or model call was executed.

Some publisher pages returned 403. DoorDash review and flag-cleanup claims were
checked through syndication/industry reporting; Vera through an accessible blog
mirror; Dasher support through an LLMOps summary. Microsoft metrics also relied
on indexed text and the official SRE repository's linked summaries where full
blog bodies were unavailable. Those rows retain their weaker access class rather
than becoming primary-body verification.

### Catalog Measurements — Different Populations, Not Quality Rankings

First method: `Bun.Glob.scanSync` over the detached filesystem with the exact
patterns below, plus JSON manifest/registry parsing. Independent method:
`git ls-tree -r -z --name-only <SHA>` and depth-matching path filters over tracked
files at the same pins. Agency persona selection was additionally checked against
filesystem frontmatter and a nonempty `name` in the 18 declared divisions.
No upstream counting/validation program was run.

| Snapshot | Input population | Observed result |
| --- | --- | --- |
| Osmani | `skills/*/SKILL.md`; `agents/*.md`; `evals/cases/*.json`; `scripts/**/*.js`; `hooks/*.sh`; `hooks/*.md` | 25 skills, 4 personas, 25 case files, 14 JS files, 7 shell hooks and 2 hook documents |
| Quickstarts | `managed-agents/**/deployment.md`; `managed-agents/*/agents/*/agent.md` | 1 deployment Markdown and 1 agent Markdown in these populations; Sentry uses Python deployment, so this is not a count of all examples |
| wshobson | `plugins/*/agents/*.md`; `plugins/*/skills/*/SKILL.md`; `plugins/*/commands/*.md`; local plugin manifests; marketplace JSON | 202 agents, 184 skills, 105 commands, 92 local plugins; 94 marketplace entries = 92 local + 2 external |
| Knowledge work | root and `partner-built/*` plugin manifests; `**/skills/*/SKILL.md`; marketplace JSON | 17 root + 5 partner manifests = 22 local plugins; 225 skill files; 123 marketplace entries = 22 local + 101 remote |
| Agency | Markdown under declared division directories, with first-line `---` and nonempty frontmatter `name`; `divisions.json`; `tools.json` | 282 selected persona files, 18 divisions, 17 tool keys; broader `*/**/*.md` population has 325 files |

Integration corrected two scout inventory claims: Osmani has seven shell-hook
files, not the report's inconsistent six-file total; Agency's 279 figure occurs
in historical installer comments and is not this pin's selected-file count.
The Knowledge Work README's “11 plugins” list is a narrower introductory list,
not the current marketplace population. None of these counts measures competence,
independent agent processes, successful executions or local demand.

## Production Synthesis — Ten Setups and Material Claims

The ten labels are the paste author's convenience taxonomy. The paper's six
responsibilities and the repositories' component types classify different axes.
The tables retain all company examples and their material figures. Publication
figures are dated reports, not refreshed service-wide measurements.

### 1. Background Coding

| Source and access, checked 2026-10-11 | Claim checked | Status and boundary |
| --- | --- | --- |
| Stripe [Minions part 1](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents) and [part 2](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents-part-2); primary body; checked 2026-10-11 | More than 1,000, later 1,300, minion-produced merged PRs per week; coded blueprints interleave deterministic and agent nodes, with isolated devboxes and Toolshed | `verified` as Stripe self-report. Human-reviewed merges; no total-PR denominator or independent quality comparison. Blueprint orchestration is code, not a prompt-only guarantee. |
| Spotify [feedback loops](https://engineering.atspotify.com/2025/12/feedback-loops-background-coding-agents-part-3) and [Code with Claude](https://engineering.atspotify.com/2026/6/code-with-claude-coding-is-no-longer-the-constraint); primary body; checked 2026-10-11 | Stop-hook verifiers precede PR opening; task/diff LLM judge vetoes about a quarter of sessions, with about half subsequently corrected | `needs-qualification`. The headline 2.5 million maintenance PRs belongs to multi-year Fleet Management/Fleetshift automation predating Honk, not an LLM-agent output count. Veto/recovery figures are author reports; the judge's eval coverage is limited. |
| Shopify [Under the River](https://shopify.engineering/under-the-river); primary body; checked 2026-10-11 | One in eight merged PRs coauthored by River; 3,536 coauthored merges and 59,918 sessions in a reported 30-day window | `verified` as self-report. Coauthoring is not unattended human-free delivery; sessions and merged PRs are different denominators. |

### 2. Code Review

| Source and access, checked 2026-10-11 | Claim checked | Status and boundary |
| --- | --- | --- |
| Cloudflare [AI code review](https://blog.cloudflare.com/ai-code-review/); primary body; checked 2026-10-11 | Up to seven specialist reviewers; 131,246 runs across 48,095 merge requests in the first 30 days; median 3m39s and $0.98; 0.6% break-glass use | `verified` as self-report. Runs include repeated reviews; median cost is not average cost. The reported population is internal GitLab work, not comparative defect recall or universal review latency. |
| DoorDash [reviewer article](https://careersatdoordash.com/blog/doordash-built-an-ai-code-reviewer-engineers-actually-listen-to), accessed through [daily.dev syndication](https://daily.dev/posts/how-doordash-built-an-ai-code-reviewer-engineers-actually-listen-to-psc8auyls); checked 2026-10-11 | Lead scout, two deep reviewers and rebuttal; 10,000+ weekly PRs; 60.2% acceptance versus roughly 46% baseline; roughly $3/review | `needs-qualification`: secondary access, high/critical findings only. Acceptance/code change is not independently labelled correctness, and suppressed lower-severity findings are outside this numerator. |
| Uber [uReview](https://www.uber.com/tw/en/blog/ureview/); primary body; checked 2026-10-11 | Multiple comment generators, grading/deduplication; 75% useful and over 65% addressed | `needs-qualification`: usefulness is among developers interacting with the tool; addressing a comment is a separate metric. uReview comments on diffs; it does not account for initial PR generation. |

The paste's separate Uber headline is also qualified by
[Running a Software Factory Efficiently at Uber Scale](https://www.uber.com/us/en/blog/efficient-software-factory/), checked 2026-10-11:
“more than 70%” is PR attribution to local **or** cloud agents, including interactive
workflows, not 70% autonomous generation or merge.

### 3. Migration

| Source and access, checked 2026-10-11 | Claim checked | Status and boundary |
| --- | --- | --- |
| Airbnb [test migration](https://airbnb.tech/infrastructure/accelerating-large-scale-test-migration-with-llms/); company tech-blog body; checked 2026-10-11 | Nearly 3,500 Enzyme→RTL test files; 97% automatic conversion; six weeks versus an estimated 1.5 years; state machine with test/lint/type feedback | `needs-qualification`: estimate is not an observed control arm; remaining work required humans. Specific React-test migration, tuned prompts and substantial retry allowances, not a general migration effect size. |
| Google [large-scale migrations](https://arxiv.org/abs/2501.06972), experience-report text; checked 2026-10-11 | Ads ID migration: 80% of landed modifications fully AI-authored; JUnit migration: 5,359 files in three months | `verified` as industrial author report. Different migrations and denominators; human review/editing and static code-search infrastructure remain part of the system. |
| DoorDash [flag-cleanup reporting](https://www.infoq.com/news/2026/09/doordash-feature-flag-cleanup/); secondary industry report; checked 2026-10-11 | Human selects flags; bounded worktree parallelism; 95% patch-coverage gate; 45/50 usable PRs; $4.79 and 13.8 minutes per cleanup | `needs-qualification`: small 50-flag cohort, revisions and human interventions; source-reported costs. Patch coverage is a gate, not semantic deletion-safety proof. Primary-paper replication not performed. |

### 4. SRE / On-Call

| Source and access, checked 2026-10-11 | Claim checked | Status and boundary |
| --- | --- | --- |
| Microsoft [context-engineering post](https://techcommunity.microsoft.com/blog/appsonazureblog/context-engineering-lessons-from-building-azure-sre-agent/4481200) and [official SRE repository](https://github.com/microsoft/sre-agent); blog access limited, repository/indexed summaries; checked 2026-10-11 | Simplification from 100+ tools/50+ agents to five core tools/generalists; 35,000+ incidents; App Service mitigation 40.5h→3m | `needs-qualification`. Incident/mitigation metrics originate in later Customer Zero/GA accounts, not solely the context-engineering citation. App Service is a particular service. Full mode/denominator details and the exact “more than four transfers” threshold are not independently established here; no universal handoff limit follows. |
| Ramp [OCA](https://builders.ramp.com/post/how-we-built-oca-our-ai-on-call-assistant); primary body; checked 2026-10-11 | Interim/final reports around 5/13 minutes; assisted 575/1,220 incident-fix PRs over four weeks; 37% fewer engineers | `needs-qualification`: observational comparison among incidents with merged fixes; estimated involvement, not randomized labour savings. Read-only investigation and human action gates are explicit. |
| Meta [reliability flywheel](https://atscaleconference.com/teaching-ai-to-fight-fires-building-the-reliability-flywheel-at-meta/); company conference account; checked 2026-10-11 | Cited tool queries; median detection-to-mitigation about 9.5h→3.8h | `needs-qualification`: scoped collaborative agent-plus-engineer workflow in recommendation systems. Not autonomous incident resolution or all-Meta performance. |

### 5. Security

| Source and access, checked 2026-10-11 | Claim checked | Status and boundary |
| --- | --- | --- |
| Cloudflare [agentic security operations](https://blog.cloudflare.com/agentic-security-operations/); primary body; checked 2026-10-11 | Deterministic versioned evidence collection before inference; four specialists; typed synthesis; application citation checks and abstention on insufficient evidence | `verified` as an architectural description. Final enforcement remains with analysts; textual description is not a containment probe or independently measured precision. |
| Figma [internal security agents](https://figma.com/blog/how-we-secure-figmas-internal-systems-with-agents/); primary body; checked 2026-10-11 | Cost-tiered routing, steering memory, deterministic draft-PR post-step; 71% faster resolution and 20% fewer pages | `needs-qualification`: internal alert population and self-reported operational effects. Draft conversion is a Tines workflow action, not a prompt request. Memory corrections need their own governance boundary. |
| Shopify [Dispatch harness](https://shopify.engineering/building-an-agentic-harness-that-outlasts-the-model); primary body; checked 2026-10-11 | Partitioned hunters, different-model verifiers and executable tests; 300+ findings across 80+ apps in roughly six weeks; $50–$300 full scans, over $400,000 equivalent bounty value | `needs-qualification`: bounty value is internal valuation, not cash paid; findings include defence-in-depth improvements, with two rated critical. Scan cost, finding count and validated severity are distinct measures. Different models alone do not prove independence. |

### 6. Data Analysis

| Source and access, checked 2026-10-11 | Claim checked | Status and boundary |
| --- | --- | --- |
| DoorDash [Vera](https://careersatdoordash.com/blog/inside-vera-doordashs-data-agent), via [blog mirror](https://raw.githubusercontent.com/vibedatascience/agentic_ds_resources/main/company-blog-posts/2026-09-16_doordash.md); checked 2026-10-11 | 200,000+ datasets; eval-gated sources; 43%→90% over 1,900+ evals; Vera 2.60/3 versus Claude Code 2.16/3 | `needs-qualification`: mirror access, not authenticated publisher-body access. The compared scores are a 100-question Opus 4.8 ablation, not the full eval suite or production model. LLM grading, timeouts and small hard-question slices limit inference; no business-outcome causality established. |
| Notion [Data Scout](https://www.notion.com/blog/how-we-built-a-personal-data-scientist-for-every-notion-employee); primary body; checked 2026-10-11 | Employee Snowflake credentials, shared definitions and nightly review; roughly 80% fewer data-team requests in two months | `needs-qualification`: request volume is not answer accuracy. The source warns that a searchable definition database is not a semantic layer and query success is not correctness. |
| OpenAI [in-house data agent](https://openai.com/index/inside-our-in-house-data-agent/); primary body; checked 2026-10-11 | Six context layers; 3,500+ internal users, 600+ PB; correction memory | `needs-qualification`: the source describes asking to save corrections, not automatically persisting every correction. Internal deployment scale is not a public accuracy benchmark. Permission passthrough is a host/data-service obligation. |

The proposed Knowledge Work `data` plugin is a useful prompt starting point, not
a delivered Vera/Data Scout equivalent. Its actual execution/connector limits are
recorded below.

### 7. Support

| Source and access, checked 2026-10-11 | Claim checked | Status and boundary |
| --- | --- | --- |
| Lyft [LangChain platform case study](https://www.langchain.com/blog/lyft-built-a-self-serve-ai-agent-platform-for-customer-support-with-langgraph-and-langsmith); platform/vendor account; checked 2026-10-11 | Meta-agent and configurable subgraphs, turn safety checks, sampled trace judging; six months→two weeks, resolution rate +16% | `needs-qualification`: build-time reduction applies to configurable agents, not every specialised workflow. Improvement is reported since launch; baseline volume, percentage-point interpretation and causal controls are not established here. |
| DoorDash [Dasher support](https://careersatdoordash.com/blog/large-language-modules-based-dasher-support-automation), via [ZenML summary](https://www.zenml.io/llmops-database/llm-based-dasher-support-automation-with-rag-and-quality-controls); checked 2026-10-11 | RAG, two-tier grounding checks, LLM monitoring; hallucinations down 90%, severe compliance issues down 99% | `needs-qualification`: secondary summary access and unavailable absolute rates/denominators. Bounded driver-support knowledge and human escalation; not independently reproduced reductions. |
| Coinbase [CEEcil](https://www.coinbase.com/blog/ceecil-engineering-a-support-teammate-with-human-memory); primary body; checked 2026-10-11 | Small router, deterministic low-cost rungs and full-agent path; human PR merge | `needs-qualification`: internal engineering teammate, not external customer support. The source reports most steady-state traffic reached the expensive full agent, contrary to a presumed cheap-path majority; no universal outbound checker is demonstrated. |

Quickstarts' `customer-support-agent` demonstrates a RAG chat prototype, not the
complete routing, memory and safety architecture of these production systems.

### 8. Research

| Source and access, checked 2026-10-11 | Claim checked | Status and boundary |
| --- | --- | --- |
| Anthropic [multi-agent research](https://www.anthropic.com/engineering/multi-agent-research-system); primary body; checked 2026-10-11 | Opus lead, Sonnet workers and citation pass; 90.2% improvement; around 15× chat tokens; 80% token-explained variance | `needs-qualification`: 90.2% is the internal research eval; 80% is a BrowseComp variance analysis, not the same comparison. Token use is a predictor, not proof of architectural causality; shared-context/sequential tasks can be poor fits. |
| Harvey [Playbook Review](https://www.harvey.ai/blog/rebuilding-playbook-review-as-a-multi-agent-system); primary body; checked 2026-10-11 | Per-rule document branches and conflict reconciliation; redline rubric 53%→87%, latency 2.6→3.8 minutes, reported +47% | `needs-qualification`: proprietary dataset and LLM-judge committee, not blinded attorney trials. Latency/resource tradeoff and human deal judgement remain explicit. |
| Perplexity [Deep Research](https://www.perplexity.ai/hub/deep-research) and [Computer account](https://www.perplexity.ai/hub/blog/deep-research-now-in-computer); primary account; checked 2026-10-11 | Search-as-code and parallel retrieval; BrowseComp 40.7%→83.8% | `needs-qualification`: changes include execution/search and model-routing configuration, not an isolated multi-agent treatment. No TeaPrompt transfer effect established. |

### 9. Knowledge / Second Brain

| Source and access, checked 2026-10-11 | Claim checked | Status and boundary |
| --- | --- | --- |
| Meta [tribal knowledge](https://engineering.fb.com/2026/04/06/developer-tools/how-meta-used-ai-to-map-tribal-knowledge-in-large-scale-data-pipelines/); primary body; checked 2026-10-11 | 50+ agents; 4,100+ pipeline files into 59 context files; coverage roughly 5%→100%; 40% fewer tool calls | `needs-qualification`: documentation coverage, not verified behavioural coverage. Tool/token reduction came from preliminary tests on six tasks in proprietary pipelines; source also discusses contexts where added files can hurt. |
| Meta [organizational second brain](https://engineering.fb.com/2026/09/02/ml-applications/organizational-second-brain-ai-learns-from-experts/); primary body; checked 2026-10-11 | 200+ knowledge files; fact-free procedural recipes; adversarial review/replay; around 80% fewer tokens, days→minutes | `needs-qualification`: particular regulatory-review domain, SME feedback and internal regressions; no public baseline/treatment benchmark. Knowledge edits still pass human checkpoints. |
| Notion [Lore](https://www.notion.com/blog/building-shared-memory-for-ai-agents-in-notion); primary body; checked 2026-10-11 | Five linked databases and expiry; 102/149 with seeded memory versus 82/149 without | `needs-qualification`: paired results include **27 improvements and seven regressions**. Curated seeded memory was tested, not the messy pilot vault. Aggregate gain does not justify saving everything. |

The paste's `/undefined-ui/second-brain-os` pointer is not the published Notion
Lore implementation. The inspected Notion article points to
[makenotion/lore](https://github.com/makenotion/lore), checked 2026-10-11.
This identifies the source's reference; neither external memory project is an
additional pinned repository survey or adopted dependency here.

### 10. Scheduled Automation

| Source and access, checked 2026-10-11 | Claim checked | Status and boundary |
| --- | --- | --- |
| Anthropic [effective automations](https://claude.dev/blog/building-effective-agent-automations), plus pinned Quickstarts daily brief; primary account/source; checked 2026-10-11 | Weekday cron, per-source bookmarks, unreadable-source reporting, separate preferences/state and declared $5/run cap | `verified` as a reference design. Prompt steps, platform mount/network configuration and billing enforcement are different layers. Not a measured organisation-wide SLA. |
| GitHub [Agentic Workflows](https://github.blog/ai-and-ml/automate-repository-tasks-with-github-agentic-workflows/); primary account; checked 2026-10-11 | Markdown compilation into Actions, read-only default and safe outputs; no automatic PR merge in the described design | `needs-qualification`: technical-preview workflow/tool policy, not a general agent rule or immutable current service guarantee. Scheduling and allowed output policy are configuration-dependent. |
| Microsoft [scheduled versus incident guidance](https://techcommunity.microsoft.com/blog/appsonazureblog/getting-the-best-out-of-azure-sre-agent/4559745); publisher body unavailable, search/indexed account only; checked 2026-10-11 | Claimed scheduled score 4.5/5 versus broad incident-plan score 1.7/5 | `unknown` for a fully verified numerical comparison: exact scoring rubric, populations and full body not established through available access. Do not use the claimed ratio as causal or quantitative evidence for task selection. |

### Foundations and Universal Prescriptions

The [OpenAI practical agent guide](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf), checked 2026-10-11,
and [Anthropic Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)
were read, checked 2026-10-11. Model/tools/instructions, workflow-versus-agent, and
Anthropic's five patterns—chaining, routing, parallelization, orchestrator/workers,
evaluator/optimizer—are supported conceptual definitions, not a frequency census.

| Paste assertion | Disposition and reason |
| --- | --- |
| “70+ posts” reviewed; ten setups exhaust the useful designs | `unknown`: no corpus, inclusion criteria or bibliography supplied. Ten jobs are useful examples, not a validated taxonomy. |
| Model is the smallest/easy part | `refuted` as a general measured conclusion; no size/effort denominator is provided, and the paper also documents material fixed-harness model effects. |
| MCP gateway is the universal tool-access mechanism | `needs-qualification`: MCP is present in examples, but direct API/CLI calls and other tool substrates also appear. The paste says “typically”; the supplied sample does not establish prevalence. |
| The executing agent never grades its own work | `refuted` as universal: daily brief includes same-agent verification; prototype feature status is self-written. An independent acceptance channel is desirable where risk requires it, not an observed property of every example. |
| Every real-world change needs per-action human approval | `refuted` as universal: a pre-authorised daily brief can post to Slack without a new confirmation. Human approval, delegated envelope and sink enforcement are separate concepts. |
| Six copied rules guarantee success | `refuted`: no universal trial; source-reported costs, memory harms and task-dependent failures contradict the guarantee. |
| Every company started with one boring measured task | `unknown` as a universal history claim; Microsoft explicitly describes an over-complex initial design. “Start narrow” is advice, not an established origin story for the full sample. |

A scout's universal-rule rebuttal mistakenly attributed Spotify's 2.5 million
Fleetshift PRs to Honk. Integration rejected that statement rather than using the
same attribution error to attack the paste. Likewise, source descriptions of
multi-agent difficulty do not establish a universal four-handoff failure law.

## Paper Survey — Method, Findings and Limits

Source: versioned [arXiv 2606.20683v1 PDF](https://arxiv.org/pdf/2606.20683v1),
checked 2026-10-11; full extracted text read. Extraction includes table/figure
layout artefacts, so no inferred cell alignment or recreated chart is used here.

### Method and Definitions

The paper is an evolution-first narrative literature synthesis spanning roughly
2020–2026, with observational analysis of public SWE-bench, Terminal-Bench and
WebArena configurations. The inspected text does not establish a reproducible
systematic-review search/screening protocol or randomized factorial ablation.

Its functional agent definition is goal-directed perception, state maintenance,
reasoning/decision-making, action and feedback adaptation. Its implementation view
couples a model with six runtime responsibilities:

| Responsibility | Design question | Existing TeaPrompt relationship |
| --- | --- | --- |
| Observation | Which environment events become trustworthy input? | Research source ledger and runtime trust-boundary source/action map |
| Context | What is selected, structured and retained in the active window? | Context engineering and task-packet/brief contracts |
| Control | Who chooses sequence, delegation, stopping and retry? | Static topology versus externally verified loop distinction in the flow packs |
| Action | Which tools, parameters and effects are permitted? | Host capability/approval contracts; prompt text is not enforcement |
| State | What survives a turn or process, and what is authoritative? | Handoff/retro, workflow record-class and stale-version contracts |
| Verification/governance | Which evidence releases a gate and who accepts the result? | Oracle split, independent channels and named acceptance in governed delivery |

Four development phases are an explanatory history, not mutually exclusive runtime
classes. Horizon, environment richness and autonomy are task pressures; the paper's
L1–L4 task-level notation is **not** TeaPrompt Strictness L1–L6 or Formalization L0–L4.
These responsibilities are not six proposed skills or proof of an optimal design.

### Empirical Findings

- SWE-bench and WebArena tables show substantial cross-harness spreads with a
  nominally fixed model, and model improvements inside a fixed harness. Public
  rows bundle prompt, model-snapshot, tool, budget, retry and implementation
  differences; they do not isolate a single causal factor.
- Terminal-Bench analysis starts from 75 public submissions/32,604 trials and a
  stricter 48-submission matched population. Token coverage is reported at 45.0%
  and USD coverage at 15.2%; runtime/timeout observations are more available.
  These are the paper authors' historical population/counts, not this survey's
  rerun or a current leaderboard inventory.
- Success alone hides cost, latency, variability and recovery differences.
  Value-aware objectives, held-out verification/recovery, reusable substrate and
  task-specific adapters are proposed design/evaluation directions, not validated
  universal utility functions.

### Limits and Applicability

No raw benchmark data was reproduced here. Incomplete telemetry, public-submission
selection, configuration confounding and changing model/host versions limit causal
claims. A fixed nominal model name is not proof of identical effective inference
conditions. Benchmark success does not establish deployed safety or business value.

[INFERENCE] Task pressures are a better comparison axis for TeaPrompt than job
labels or roster size: they expose the need for control, evidence and an enforcing
host without turning every domain into a core route. This is a design judgement
consistent with current contracts, not a demonstrated TeaPrompt effect size.

## Five Pinned Repository Surveys

### addyosmani/agent-skills — Engineering Workflow Pack

Checked 2026-10-11 at the pin above. Representative sources: [spec workflow](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/spec-driven-development/SKILL.md), [incremental implementation](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/incremental-implementation/SKILL.md), [review](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/code-review-and-quality/SKILL.md), [constraint development](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/constraint-driven-development/SKILL.md), [eval documentation](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/evals/README.md); all checked 2026-10-11.

Mechanisms: capability-map decomposition before multi-module specs; explicit
spec-approval stop; vertical/risk/contract slicing; scope-restraint report;
severity-led review and targeted test mutation; measured/enforced constraint
ratchets with owned exceptions; native-stack discovery and outcome-based tests;
context hierarchy and restartable progress records.

Evaluation separates structural lint, deterministic lexical trigger/collision
checks, and token-spending behavioural/plugin comparisons. Native routing figures
in the source—review invocation 5/7 and TDD 2/7 on stated prompts/model/CLI—are
upstream observations, not rerun results. TF-IDF fit does not establish semantic
routing, and a structured LLM grading response does not establish independent truth.

Delivery matters: the pinned README explicitly warns that single-skill `npx`
installation copies `skills/<name>/`, not shared root `references/`; issue #361
tracks unavailable supplementary checklists. Monorepo link validation is not proof
of standalone installation. Optional cache hooks run HEAD revalidation; the
`simplify-ignore` hook masks/restores real disk content. Its docs describe
crash/manual recovery: that is an operational risk, not a measured crash frequency.
No hook was installed or exercised.

Local comparison: brief/spec-plan, implement/minimality, research/review and the
existing anti-cheating/oracle contracts cover the workflow concerns. A blanket
later-turn approval rule would constrain already-authorised low-risk work; no
local evidence justifies adopting it. Active hooks and automatic per-slice commits
would change host/user authority and are not adopted.

### anthropics/claude-quickstarts — Heterogeneous Reference Applications

Checked 2026-10-11. Selected sources: [support route](https://github.com/anthropics/claude-quickstarts/blob/9ec32b91df50b0d4906cae64b13c6298055ff40d/customer-support-agent/app/api/chat/route.ts), [coding driver](https://github.com/anthropics/claude-quickstarts/blob/9ec32b91df50b0d4906cae64b13c6298055ff40d/autonomous-coding/agent.py), [daily-brief instructions](https://github.com/anthropics/claude-quickstarts/blob/9ec32b91df50b0d4906cae64b13c6298055ff40d/managed-agents/daily-brief/agents/daily-brief/agent.md), [deployment](https://github.com/anthropics/claude-quickstarts/blob/9ec32b91df50b0d4906cae64b13c6298055ff40d/managed-agents/daily-brief/agents/daily-brief/deployment.md), [knowledge-wiki notebook](https://github.com/anthropics/claude-quickstarts/blob/9ec32b91df50b0d4906cae64b13c6298055ff40d/managed-agents/knowledge-wiki/distill_documents_into_knowledge_wiki.ipynb); all checked 2026-10-11.

- Support is a Next.js/Bedrock RAG prototype: retrieval followed by one model call
  per request, with chat messages supplied by the client. This is not persistent
  teammate memory or a tool-using agent loop. Retrieval errors can become empty
  context while response generation continues; the prototype disclaimer matters.
- Autonomous coding uses an initializer and fresh-context coding sessions,
  feature/progress files, a shell allowlist hook and SDK sandbox configuration.
  The outer loop checks iteration limits, not independently verified all-feature
  completion. The agent edits feature `passes` flags itself; this is progress
  bookkeeping, not a sealed acceptance oracle. Command parsing and requested SDK
  sandboxing are not proof of actual containment.
- Daily brief declares weekday cron, read-only preferences, writable state and
  credential/network restrictions. Its instructions distinguish unreadable sources
  from quiet ones, preserve failed-source bookmarks, inspect destination history,
  use posting/posted/maybe-posted/held records, and advance bookkeeping only on
  positive Slack acknowledgement. The $5 cap is a platform declaration, not an
  exercised billing control here. Title-history deduplication is not a proven
  concurrent sink-idempotency contract.
- Knowledge wiki separates extraction, unresolved questions, consolidation and
  read-only query sessions. Facts carry source/as-of provenance and conflicts are
  retained/escalated. Query-time writes would bypass the described quality path.
  Sentry supplies another scheduled example; roadtrip-planner exposes managed
  session events and multi-agent threads. Those examples require their own cloud
  services and are not one portable runtime package.

Local comparison: flow control/loop, verification maps, handoff/retro, governed
acceptance and the external-effect recovery boundary already separate these
concerns. The useful protocols are references; no Anthropic/AWS service, credential
binding, self-attesting completion path or mandatory feature-count convention is
imported. Root MIT does not silently resolve the conflicting component README.

### wshobson/agents — Marketplace, Adapters and Governance Hooks

Checked 2026-10-11. Sources: [authoring](https://github.com/wshobson/agents/blob/46891e7e60da0e52baf1050b7b6391b64e84c6d9/docs/authoring.md), [adapter capability map](https://github.com/wshobson/agents/blob/46891e7e60da0e52baf1050b7b6391b64e84c6d9/tools/adapters/capabilities.py), [Pi adapter](https://github.com/wshobson/agents/blob/46891e7e60da0e52baf1050b7b6391b64e84c6d9/tools/adapters/pi.py), [marketplace](https://github.com/wshobson/agents/blob/46891e7e60da0e52baf1050b7b6391b64e84c6d9/.claude-plugin/marketplace.json), [plugin evaluation](https://github.com/wshobson/agents/blob/46891e7e60da0e52baf1050b7b6391b64e84c6d9/docs/plugin-eval.md); all checked 2026-10-11.

Agent/persona Markdown, activated skill instructions, user-invoked command prompts,
executable hooks and the external host loop are different surfaces. Orchestrator
commands describe phases, disk records and human checkpoints; Markdown choreography
is not a demonstrated deterministic state machine.

Adapters transform tool/model names, formats, namespaces, body/reference layouts
and permissions for different hosts. Translation can be lossy: Codex uses a coarse
sandbox-mode mapping; Cursor drops finer allowlists; Pi's locked-agent handling
avoids an empty-list inheritance widening. These are inspected adapter choices,
not live cross-host permission proofs or tested current model availability.

Governance hooks call a pinned Cedar evaluator and emit signing receipts. A local
approval-file bypass and host hook execution are additional trust boundaries;
cryptographic receipts do not establish the appropriateness of an action or safe
approval-file ownership. No policy evaluator/signing hook was run.

The `plugin-eval` layers must not be conflated: static lint, experimental LLM
judgement and repeated reply simulations. Its docs describe judge self-generated
prompts, limited input slices, reply/nonempty and length proxies, and static-only
plugin-directory/quick CI scoring. A badge is not observed native routing,
correctness or safety. The README says Pensyve Cloud stopped on 2026-10-01;
self-hosted source and dead hosted endpoints are distinct, dated delivery facts,
not independently tested uptime claims.

Local comparison: existing host-boundary, progressive-disclosure, routing holdout
and metric-discipline contracts fit. No adapter framework, arbitrary imperative
quota, badge threshold, Cedar dependency or memory service is adopted.

### anthropics/knowledge-work-plugins — Domain Prompts and Connector Declarations

Checked 2026-10-11. Sources: [data connector config](https://github.com/anthropics/knowledge-work-plugins/blob/02ffa99ff00ce4d3046ccebabb8357cb39f3ab06/data/.mcp.json), [query workflow](https://github.com/anthropics/knowledge-work-plugins/blob/02ffa99ff00ce4d3046ccebabb8357cb39f3ab06/data/skills/write-query/SKILL.md), [analytical QA](https://github.com/anthropics/knowledge-work-plugins/blob/02ffa99ff00ce4d3046ccebabb8357cb39f3ab06/data/skills/validate-data/SKILL.md), [knowledge synthesis](https://github.com/anthropics/knowledge-work-plugins/blob/02ffa99ff00ce4d3046ccebabb8357cb39f3ab06/enterprise-search/skills/knowledge-synthesis/SKILL.md), [memory management](https://github.com/anthropics/knowledge-work-plugins/blob/02ffa99ff00ce4d3046ccebabb8357cb39f3ab06/productivity/skills/memory-management/SKILL.md); all checked 2026-10-11.

The `data` selection supplies SQL dialect guidance, query drafting, an offer to
execute through a connected warehouse, analytical QA and a prompt-context
extraction/packaging path. Snowflake/Databricks endpoint slots are empty in the
inspected config. A “validate data” analytical checklist is not an implemented SQL
AST validator, semantic layer, executable eval suite or host permission gate.
The source can guide building such a system; it does not deliver the production
architecture described in the paste.

Customer research and enterprise synthesis distinguish source categories and
require attributed location/date/author details. Productivity memory uses a hot
context cache plus deeper Markdown files and prompt-guided promotion/demotion.
Those are useful procedural conventions, not a demonstrated persistent retrieval
service. Host/MCP services own credentials, data access and effects; documenting
hook schemas in plugin-authoring references is not installing those hooks.

Local comparison: research provenance, memory promotion and domain-specific
implementation/review are already covered at the methodology layer. No database
connector, SQL-domain pack, hot-cache numerical quota or organisational-memory
store is adopted. Remote marketplace entries are not implementations inspected
inside this checkout, and component licence exceptions remain separate.

### msitarzewski/agency-agents — Persona Catalog and Distribution Utilities

Checked 2026-10-11. Sources: [minimal-change persona](https://github.com/msitarzewski/agency-agents/blob/f99f6aa910a442b0197b768ce0ea7751e35e2060/engineering/engineering-minimal-change-engineer.md), [reality checker](https://github.com/msitarzewski/agency-agents/blob/f99f6aa910a442b0197b768ce0ea7751e35e2060/testing/testing-reality-checker.md), [converter](https://github.com/msitarzewski/agency-agents/blob/f99f6aa910a442b0197b768ce0ea7751e35e2060/scripts/convert.sh), [installer](https://github.com/msitarzewski/agency-agents/blob/f99f6aa910a442b0197b768ce0ea7751e35e2060/scripts/install.sh), [originality check](https://github.com/msitarzewski/agency-agents/blob/f99f6aa910a442b0197b768ce0ea7751e35e2060/scripts/check-agent-originality.sh); all checked 2026-10-11.

Persona identity, expertise, memory and success metrics are instructions/aspirations,
not demonstrated capabilities. The minimal-change prompt's diff/review/regression
figures do not supply a controlled evaluation. QA prompts assume external Laravel
paths and `qa-playwright-capture.sh`; the named originating-project dependencies
are not delivered by the selected catalog files. This limits portability rather
than proving every persona unusable.

Conversion supplies pass-through, skill, TOML/rules and split-workspace formats,
plus indexing/lazy selection. Installer code preserves existing files and foreign
symlinks through a target-prefix ownership check. That is source-level intent,
not proof against canonical-root escape, races or arbitrary link replacement.
The entity-neutralized shingle/Jaccard check targets superficial prompt re-skins;
its existence does not prove originality or useful role differentiation.

NEXUS/runbook handoff documents describe teams and phases; they are not an executed
swarm or enforced capability broker. The README's OpenCode capacity warning is an
upstream host claim, not a live measured limit here. The separate desktop app was
not surveyed as an executable artifact.

Local comparison: minimality, severity-led review, source-backed proof, handoff and
host-owned control already have positive matches. Persona volume, unmeasured
“production-ready” language, NEXUS and the Hermes router justify no new core skill,
pack or distributed runtime.

## Candidate Adoption Ledger

All rows are **non-adopted**. “Existing” means the named contract was read, not
that runtime compliance or superiority was proved. Authority remains the
[canonical harness policy](../06-repo/AGENTS.md) and invoked skill contracts;
this table cannot promote an operating rule. No-copy boundary throughout:
mechanisms only, no upstream prompt/code transplantation or installation.

| ID / mechanism | Checked local destination and positive coverage | Decision, counterargument and falsifier |
| --- | --- | --- |
| AE-01 Task-pressure/model–harness lens | [brief](../skills/reflective-brief/SKILL.md), [spec-plan](../skills/reflective-spec-plan/SKILL.md), runtime trust-boundary context/action map | **Concept only.** Useful diagnostic lens, not six new skills. Reopen for a reproduced task whose required control/evidence cannot be expressed through these existing contracts. |
| AE-02 Smallest topology and bounded loops | [flow-control-generator](../skills/flow-control-generator/SKILL.md) topology selection; [flow-loop-harness](../skills/flow-loop-harness/SKILL.md) external verifier and task-declared caps | **No change.** Swarms can fit independent breadth tasks, but no universal roster/handoff count follows. Falsifier: a real local structure failure not fixable in the existing topology/loop surfaces. |
| AE-03 Specification/slicing/scope restraint | [spec-plan](../skills/reflective-spec-plan/SKILL.md) Definition of Ready/Planning Fidelity; [implement](../skills/reflective-implement/SKILL.md) scope/sufficiency; [minimality](../skills/reflective-minimality/SKILL.md) safety floor | **No change.** Named scope-restraint reports are optional presentation, not a missing invariant. Reopen if a specific allowed scope transition produces a reproducible unintended edit. |
| AE-04 Diff-scoped floor/threshold audit | [review](../skills/reflective-review/SKILL.md) reward-hacking scan; [canonical anti-cheating rules](../06-repo/AGENTS.md#anti-cheating-rules); [governed delivery](../skills/governed-delivery/SKILL.md) oracle ownership | **Inert verifier candidate.** Automation could catch cheap-to-green moves; no missed local defect or approved detector contract established. Falsifier/reopen evidence: a seeded, reachable weakening missed by existing checks, with false-positive controls for authorised changes. No universal threshold or copied scanner. |
| AE-05 Targeted review-time mutation | [review](../skills/reflective-review/SKILL.md) test-gap findings; [test design](../02-engineering/test-designer.md) failure signals/anti-cheating; [implement](../skills/reflective-implement/SKILL.md) failing-before/passing-after verification | **Inert method candidate**, not mandatory review mutation. Existing anti-gaming design is relevant but does not prove mutation coverage. Reopen for a plausible surviving defect missed by ordinary checks, with isolated restoration and an explicit review scope. |
| AE-06 Mandatory later-turn spec approval | [spec-plan](../skills/reflective-spec-plan/SKILL.md) readiness and Human Review; [brief](../skills/reflective-brief/SKILL.md) material missing inputs | **Reject blanket rule.** Source describes a workflow preference, not host enforcement. It would stop already-authorised combined work. Reopen for a specific unauthorised spec→execution transition not prevented by existing authority checks. |
| AE-07 Trigger/collision/static/behavioural eval layers | [routing contract](ROUTING_CONTRACT.md), [research](../skills/reflective-research/SKILL.md) fixture/efficacy distinction | **No change.** Lexical checks can flag ambiguity; synthetic ranks and reply simulations cannot replace actual routing/behaviour. Reopen for a description collision missed by current holdouts that a bounded complementary check detects. |
| AE-08 Denominators, harms, costs and independent scoring | [golden benchmark](../skills/golden-benchmark-runner/SKILL.md) completed-pair/censoring/measurement rules; [blinded eval](../skills/arm-blinded-eval-harness/SKILL.md); [review](../skills/reflective-review/SKILL.md) four evidence dimensions | **No change.** Upstream metrics expose why the existing distinctions matter. Falsifier: a consumer-visible metric misreport allowed by the current contract, not another vendor aggregate. No badge or fixed-model causal claim imported. |
| AE-09 Progressive disclosure and portable support files | [installation guide](../SKILL_INSTALLATION.md); [context engineering](../03-context/context-engineering.md); co-installed flow `TEMPLATES.md`/governance `ARTIFACTS.md` disclosures | **No change.** Root provenance links are not installed dependencies; arbitrary 500-line/8KB thresholds are source/host-specific. Reopen for an actual supported-install missing reference or truncation failure. |
| AE-10 Provenance-aware memory and correction proposals | [handoff/retro](../skills/reflective-handoff-retro/SKILL.md) quality/revalidation/promotion; [research](../skills/reflective-research/SKILL.md) source/freshness ledger | **No change.** Richer stores may help some domains but can regress others. Falsifier: a validated correction is lost or an unapproved inference becomes authoritative through a specific current contract gap. No universal hot-cache quota or automatic saving. |
| AE-11 Unreadable source versus empty result | [research](../skills/reflective-research/SKILL.md) unknowns/positive-controlled absence; [runtime trust boundary](../04-agent/runtime-trust-boundary.md) missing-data discipline | **No change.** Source-accounting is already explicit. Reopen for a reproduced error-as-zero claim that the existing carrying rule permits; no invented claim of perfect recall. |
| AE-12 Posting acknowledgement/unknown outcome | [external-effect recovery](../04-agent/runtime-trust-boundary.md#4a-external-effect-recovery-boundary); [review](../skills/reflective-review/SKILL.md) dispatch/receipt/idempotency/owner checks | **No change.** Daily brief is a useful concrete example, not proven concurrency-safe idempotency. Falsifier: an affected local adapter advances state or retries an ambiguous dispatch despite the current contract. Slack/cloud implementation stays host-owned. |
| AE-13 Read-only canonical inputs and independent acceptance | [governed delivery](../skills/governed-delivery/SKILL.md) oracle split, non-model channel, named acceptance; [governance scaffold](../skills/agent-governance-scaffold/SKILL.md) capability/host sealing | **No change.** Configured mounts/hooks can enforce where a host supports them; declaration alone cannot. Reopen for an adopted host's reproduced boundary escape, under separate authority. No self-written feature PASS accepted as oracle truth. |
| AE-14 SQL/domain guidance and production start points | [implement](../skills/reflective-implement/SKILL.md) repo-native implementation; [review](../skills/reflective-review/SKILL.md) reachable defects; [risk](../skills/reflective-risk/SKILL.md) data/permission gates | **No change.** A domain reference can be useful without becoming a portable production harness. Reopen for an observed local SQL/domain failure with specified dialect, execution and evidence requirements; no new connector or domain pack by catalog analogy. |
| AE-15 Host adapters, hooks, installers and schedulers | [runtime trust boundary](../04-agent/runtime-trust-boundary.md); [installation guide](../SKILL_INSTALLATION.md); [governance scaffold](../skills/agent-governance-scaffold/SKILL.md) host obligations | **No change / host responsibility.** Adapter breadth and ownership checks are useful references, not verified cross-host safety. Reopen for a supported delivery failure or explicitly authorised host integration with canonical-path, ownership and concurrent-write controls. |
| AE-16 Persona re-skin/originality checks | [minimality](../skills/reflective-minimality/SKILL.md) duplicate-instruction scan; [research](../skills/reflective-research/SKILL.md) local-gap gate | **Concept only.** Shingle similarity is not semantic usefulness; bilingual/common-contract text needs controls. Reopen for recurring accidental duplicates missed by existing authoring review. No arbitrary similarity quota adopted. |

### Integration Disagreements and Rejected Overclaims

- The engineering scout proposed adopting a mandatory spec turn-stop and optional
  mutation/floor methods. The final decision keeps the first rejected as a blanket
  rule and the latter two inert: source novelty and a scout recommendation do not
  establish a local gap or supply adoption authority.
- Quickstarts recommendations to “adopt” acknowledgement, preference isolation and
  unreadable-source accounting were mapped to already-read carrying contracts.
  Those principles are covered; the concrete cloud implementations are not adopted.
- “TeaPrompt is more rigorous”/“superior” comparisons were rejected as unmeasured.
  Positive contract matches are observable; comparative agent outcomes are unknown.
- Static converter/installer/originality checks were not described as successfully
  enforcing security or originality. The corresponding upstream programs were not
  executed, and documented recovery/permission limits remain visible.

## Evidence vs Inference

**Observed:** seven inputs, five exact pins, independently reconciled inventory
populations, selected implementation/configuration paths, full paper text and
primary/secondary company accounts with the access bounds above. Existing local
contracts carry concrete scope, evidence, independent acceptance, source failure,
unknown-outcome and promotion clauses.

**[INFERENCE]:** comparing task pressures and enforcement ownership is more useful
for TeaPrompt than copying a company topology or expanding routing by job labels.
Reference-only retention is the smallest justified action on the current evidence.

**Unknown:** independent vendor data validity; comparative TeaPrompt utility; raw
cost/latency distributions and failed/abandoned deployment populations; live plugin
loading/permission semantics; full Microsoft scheduled-score methods; inaccessible
publisher-body details; component licence conflict resolution; host-specific safe
installation/concurrency; how much demand exists for the two inert candidates.
Unknown demand is not zero demand or a permanent veto.

## Competing Perspectives and Blind Spot

Production accounts organise by operational jobs and successful deployments. The
paper organises coupled responsibilities and task pressure. Engineering workflow
packs emphasise repeatable developer behaviour; domain plugins emphasise business
context/connectors; persona catalogs emphasise role discoverability and distribution.
Host operators additionally own isolation, permissions, costs and effects.

The strongest counterargument to no change is that repeated prompt-only gaps may
benefit from a cheap author-side verifier or richer adapter. The survey establishes
relevant external mechanisms, not a missed local defect or the adapter's safe
execution. The unresolved blind spot is comparative performance on TeaPrompt's
real tasks—including harms, cost and failures—not another roster inventory. That
needs a separately authorised, task-bound evaluation; the held campaign is not
activated to fill the gap.

## Falsifiability and Revisit Triggers

A source update contradicting a material row, a corrected publisher-body account,
a released component licence clarification, or a reproduced local failure can
reopen the affected claim/candidate. An inventory recheck uses the same named
population and two independent methods; it does not replace historical results
with an unexplained different count.

For any proposed adoption, the deciding evidence would be a bounded local failure
and candidate treatment with unchanged input/acceptance, negative controls,
independent observation, task-declared caps, harm/censoring accounting and the
appropriate human authority. Static source matches, self-grading, clone equality,
model diversity or a green badge are insufficient substitutes.

## Verification and Consumer Map

Source verification exercised actual retrieval, detached-source inspection, JSON
registry parsing, filesystem inventory and independent Git-tree counts. These are
investigation results, not upstream behavioural tests. Immutable/dated source
receipts and scout ledgers are retained session-locally in
`agent-ecosystem-paste-receipt-2026-10-11.json`,
`agent-ecosystem-catalog-counts-2026-10-11.json`,
`agent-ecosystem-independent-catalog-audit-2026-10-11.json`, and the survey packet.
This record contains the portable source identities, populations and conclusions;
private receipts are not installed dependencies or committed repository files.

Publication verification uses the actual repository consumers:

- `python3 reflective-prompt-library/plans/generate_index.py`
- `make all` — existing tests and the repository's link, skill, governance,
  knowledge, hygiene, benchmark/example and routing validators.
- Render this Markdown with the existing Markdown renderer and open the result in
  Chromium; inspect headings, tables and citations at desktop/narrow widths.

Results belong to the session's final report/receipts, not inferred from this list
of commands. No new permanent test or dependency is created for a reference record.

| Consumer class | Scope and disposition |
| --- | --- |
| Human survey reader | New record, source/candidate links and rendered-document surface exercised for publication |
| Generated discovery | `index.json` regenerated after the record's final edit; existing current-index consumer checks content binding |
| Record/link/governance validators | Existing repository consumers used, with their observed results reported separately |
| Core/pack runtime callers | Not applicable: no skill contract, registry, route, CLI recipe or executable template changed |
| Fixtures/persisted campaign artifacts | Not applicable: no oracle, campaign manifest, pilot receipt or protected fixture changed |
| Project-knowledge authority | Map-only Decision Index pointer added by the later landing repair below; no new Durable Lesson or agent operating rule |

## Handoff and Remaining Work

Research deliverable: one complete reference/no-change record and refreshed
discovery. No upstream runtime verification or company-data replication is claimed.
No implementation, installation, commit or push follows from this survey.

The explicitly scoped unknowns above are limitations of the evidence, not hidden
unfinished engineering. Inert candidates require a local failure and a separate
approval decision before any skill/verifier/host change. Existing TEST-001 and
campaign owner gates remain unchanged.

## Publication and Worthiness Follow-through (2026-10-11)

Later user direction: “Fix and update docs and skills if worthy.” This supplies
authority to repair live survey defects and assess this survey's candidates,
not to install an upstream runtime or activate the held campaign.

The delayed truncated-preview finding was already corrected. The initial
publication receipt binds source SHA-256
`48bbb5bf91bfbbe84d54a8a52f6d8215529a81900b70781ad5fbd3b09a89ab75`
to complete 71,432-byte HTML with closed style/main/document, 16 tables and
digest-bound desktop/narrow captures. These are **pre-follow-through** source
and rendering measurements, not hashes or counts for this amended record.
The empty stdin transport, incorrect integrity assertion and invalid CSS selector
were publication-harness failures; their correction is not an upstream runtime
or model result. All 46 new-record access-date warnings were also corrected;
the 35 older-record warnings were not repaired by this survey.

No additional survey-specific paragraph-pin test is warranted. This record
adopts no installed contract; the existing discovery, link, metadata and
governance consumers cover publication structure, not source truth or efficacy.
The [Adoption Guard Closure](../GLOSSARY.md#adoption-guard-closure) rule and the
[XM-11/AF841-M1 precedents](external-adoption-case-studies-2026-06-20.md#2026-09-30-absence-claim-method-repair)
do not require wording guards for a reference/no-change outcome.

Worthiness ruling: **documentation only; existing skills unchanged**. The
actual carrying clauses already cover source-versus-data verification,
independent count populations, qualified comparisons, missing-source accounting,
memory revalidation/promotion and host-owned effect/acceptance enforcement.
The AE-01–AE-16 ledger identifies those surfaces and their reopen evidence;
positive contract coverage is not measured agent adherence. AE-04 and AE-05
remain inert candidates, and generic fix direction supplies neither their
missing local-failure evidence nor host/campaign acceptance.

The [external-adoption case comparison](external-adoption-case-studies-2026-06-20.md#case-comparison)
now discovers this outcome. Follow-through source bindings, rendered surfaces
and final repository-gate output are retained separately in
`local://agent-ecosystem-follow-through-evidence-2026-10-11.json`;
the original publication receipt remains historical and unchanged.
No skill, registry, route, protected oracle, project-knowledge promotion,
commit or push is part of this follow-through.

## Survey Landing Advisory Ruling (2026-10-11)

Later user direction: “fix and next.” The Case Comparison finding is stale:
the existing [case row](external-adoption-case-studies-2026-06-20.md#case-comparison)
already links this survey and its no-change outcome. It is not added twice.
The missing [Decision Index](../PROJECT_KNOWLEDGE.md#decision-index) pointer is
repaired as a human-navigation path, following the existing map convention.
This is not a new lesson, operating rule or AE candidate adoption. The previous
publication/follow-through scope statements describe their earlier revisions;
their source-bound receipts remain historical, not this repair's verification.

The cited predecessor test mixes structural ledger/containment checks with
exact fact, quote and prose assertions. Its existence does not make another
survey-specific test file mandatory. No new source-wording pin is added:
word presence cannot prove source truth, company efficacy or candidate utility.
Existing knowledge, link, record-hygiene and generated-index consumers remain
the publication checks. A disposable before/after reader check binds the new
navigation, all sixteen candidate rows/reopen conditions and unchanged
installed/registry/routing surfaces to the actual source.

Acceptance and current verification evidence are retained separately in
`local://agent-ecosystem-landing-evidence-2026-10-11.json`. This check is not an
upstream runtime, model or independent company-data reproduction.

Next roadmap gate: the Apple private replacement's qualified implementation
does not supply TEST-001 host/consumer/scorer adoption or campaign authorization.
Resolve that owner choice before dispatch; Stage-1 additionally retains its
approval, roles, memory bindings and enforced isolation/cap requirements.
No skill, test, dependency, protected oracle, commit or push changes here.

