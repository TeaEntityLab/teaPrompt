# Archdev Factory Survey — What Reaches the Next Worker? (2026-11-21)

Language: English

> **Status:** Reference case and in-place prompt guidance. Carry a decision with the task it governs, check the repaired revision with an existing consumer, and measure team attention per accepted feature before increasing concurrency. No daemon, queue, merge permission or worker quota is adopted.

## Evidence and attribution

Calvin Grunewald's [October 23 workflow](https://thebuildingmachine.com/p/my-new-agentic-workflow) reserves direct collaboration for high-impact work that needs his judgment. His [November 19 factory account](https://thebuildingmachine.com/p/a-look-inside-the-factory) describes how he delegates other work. Both articles and their figures were checked 2026-11-21. The operating figures are his reports, not measurements of TeaPrompt or an independent audit of the factory.

- **A visible blocker can still lose its answer.** Grunewald reports 151 requests from workers **to the overseer** in about 21 hours, not 151 human interruptions. Separately, 67 task pauses went unannounced; even when he answered in chat, the next worker received only the task name and description. His fix attached the question, reason and recommendation to the paused task, then included the owner's answer in the next worker's input. A recommendation is not that answer. His playbook reserves credentials, spending, live infrastructure (including merges), irreversible actions, product choices and explicit sign-off for him; those are his boundaries, not grants to another team.
- **The handoff to verification has a revision.** The overseer assigns ready tasks from a dependency graph. On the private-remote path, each worker pushes from its own worktree; the daemon claims a SQLite job for that exact commit, runs the repository's policy in a fresh worktree, then watches the PR for CI failures, feedback and conflicts. Lint, policy and test failures may *enter repair*; they are not permission to publish. A repaired commit is a new candidate. Opening a PR, merging it and accepting the feature are different events.
- **Volume and capacity have denominators.** The [weekly chart](https://substack-post-media.s3.amazonaws.com/public/images/4138ccfd-57c6-4173-b9cc-ccd41a6182af_1800x810.png), checked 2026-11-21, totals 1,940 merged PRs from `factory/` branches in the `firstlanding` monorepo since August 21; the last week covers Monday through Thursday. It does not count distinct features, defects or human minutes. The author reports four workers plus four daemon jobs together on one 128 GB machine, then two machines using task leases. Moving all execution to the cloud was still ahead, not a demonstrated scaling result.

### What the discussion adds

Checked 2026-11-21: [Grunewald's announcement](https://x.com/CalvinGrunewald/status/2123472779559436533) credits Kun Chen for the daemon idea. [Chen's quote](https://x.com/kunchenguid/status/2123478958494904388) recommends the account of solving bottlenecks. [Asked by Dan Tao](https://x.com/dan_tao/status/2123485215775490174), [Chen distinguishes novel problems from identical units](https://x.com/kunchenguid/status/2123486191781900324); [Grunewald's reply](https://x.com/CalvinGrunewald/status/2123499972205351001) compares reconfiguration, quality control and visibility, not identical products.

[Daniel Lenton](https://x.com/DanielLenton1/status/2123529523962826918) singles out being asked to approve a temporary checkout. [Jean](https://x.com/JohnStrongHodl/status/2123496449140752413) asks whether the extra output builds a better business. [Jaden's question on the October article](https://thebuildingmachine.com/p/my-new-agentic-workflow/comment/368884600) makes the latter concern measurable: who writes the tasks, who reviews, and how much time does the team spend understanding the changes? These are individual public comments, checked 2026-11-21, not independent delivery results.

## Replay the repair, including when to decline

Grunewald reports replaying the fix step on frozen PR heads, findings and reference fixes with a separate grader. The October 20 comparison had **six policies, 19 graded cases, nine high- and 14 medium-severity findings**. The units are findings, not 23 PRs. Three published rows illustrate the tradeoff:

| Fix policy | High fixed | Medium fixed | Grader-reported regressions | USD per high fixed |
| --- | ---: | ---: | ---: | ---: |
| Current | 9/9 | 14/14 | 0 | 2.98 |
| Reproduce first | 9/9 | 14/14 | 0 | 3.09 |
| Lower-cost Sol model | 9/9 | 13/14 | 0 | 0.85 |

The author also describes Sol deleting a public wrapper when the right response was to decline the requested change. An absent review comment cannot tell whether a caller still works. For a local replay, include both a real defect and a mistaken finding. Run the same consumer on the original and candidate revisions; score the intended behavior, including compatibility on the no-change case. Do not read the table as production defect rates or a rerun of any model here.

## Compare team attention per accepted feature

Apply the existing [attention measurement guidance](agent-control-plane-comparison-survey-2026-11-04.md#measuring-attention-without-hiding-failure) to comparable features under the usual and proposed workflows. Fix the acceptance criterion and follow-up window before either starts. Count all team minutes spent planning, answering, reviewing, repairing and maintaining the workflow, including failed and abandoned attempts. Divide by features accepted by the requester and not withdrawn for a defect during that window. If none qualify, report the time and zero acceptances, not zero minutes per feature.

For example, suppose each workflow delivers one such feature. Two PRs take the owner 20 minutes and the reviewer 10. Five PRs take the owner 8 minutes and the reviewer 27. With other costs equal, team attention **rises from 30 to 35 minutes**, despite fewer owner minutes and more merges. This is an illustration, not factory data. Report blocker waiting time separately from active minutes, alongside throughput, escaped defects, reverts and model/CI cost. Try carrying answers across handoffs before buying more worker capacity.

## Candidate Adoption Ledger

| ID | Decision | Destination or limit |
| --- | --- | --- |
| AFAC-DOC1 | Record the case and the comparison | This record and the catalogue; fewer notifications are not evidence of savings. |
| AFAC-SK1 | Clarify two existing workflows | [Context Handoff](../03-context/context-handoff.md) carries the owner's scoped answer; [Review → Rating → Fix](../04-agent/review-rating-fix.md) checks the consumer, not just the finding. The portable Skills are `reflective-handoff-retro` and `reflective-review`. |
| AFAC-RUN1 | Do not adopt the runtime | Persistence, delivery of the answer, isolation and enforcement of publication or merge authority belong to the host. A handoff is not an authorization service. |

## Falsifiability

Try the [blocked CSV handoff](../skills/examples/reflective-handoff-retro.examples.md#resume-a-blocked-csv-change) with the [Continuation Packet](../skills/reflective-handoff-retro/SKILL.md#continuation-packet) and [code review guidance](../skills/reflective-review/SKILL.md#for-code-review). A repeated question despite a current answer, action on an unapproved proposal, or reuse of an answer outside its scope fails the handoff. A quieter review that breaks the existing importer fails the repair. A matched comparison that moves time to reviewers or hides failed work does not establish an attention saving.
