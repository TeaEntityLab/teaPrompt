# mini-swe-agent — Source Survey and Execution Boundaries (2026-11-09)
Language: English

> **Status: recorded; reference-only, non-authoritative (`MSW-DOC1`).** The owner requested worthwhile Docs/Skills updates after the Addy Osmani survey and a survey of `SWE-agent/mini-swe-agent`. This record preserves pinned implementation evidence and an offline execution probe. No Skill, runtime, dependency, host configuration or model campaign is adopted. The separate `AOM-DOC2` installation-guide clarification is recorded in the [Addy follow-through](addy-osmani-agent-management-survey-2026-11-09.md#documentation-follow-through--invocation-is-not-approval-2026-11-09).

## Research Question and Direct Recommendation

Does a small single-agent shell loop supply a missing TeaPrompt mechanism, or a useful concrete example of mechanisms already covered?

**Keep it as a readable research baseline and a boundary case study, not a new Skill or execution engine.** Its useful properties are a small model/environment/agent split, inspectable message history, fresh shell processes and explicit termination states. None makes a shell safe, a submission correct, a trajectory authoritative, or a budget preemptive. TeaPrompt already separates those obligations. No demonstrated local contract failure warrants duplicating them.

## Sources, Version and Access

Pins and public documentation were checked **2026-11-09**. Branch, tag and registry identities are recorded separately; a future release or source change requires re-pinning before an adoption recommendation.

| Surface | Observed identity / evidence |
| --- | --- |
| `main` | `04d809ceab9df28f9adaed044884180159172930`, dated 2026-09-03; [GitHub commit API](https://api.github.com/repos/SWE-agent/mini-swe-agent/commits/main), checked 2026-11-09. This detached source checkout was executed. |
| Latest GitHub release | `v2.4.6`, published 2026-07-23; tag commit `a83fcae82d2a08f0ee0c688f9d137b3566c097f8`; [release](https://github.com/SWE-agent/mini-swe-agent/releases/tag/v2.4.6), checked 2026-11-09. |
| PyPI | `2.4.6`; [registry JSON](https://pypi.org/pypi/mini-swe-agent/json), checked 2026-11-09. Registry metadata was inspected; the published wheel was not installed or proven equivalent to the checkout. |
| Actual version delta | `git diff --stat a83fcae82d2a08f0ee0c688f9d137b3566c097f8 04d809ceab9df28f9adaed044884180159172930`: two files, `.pre-commit-config.yaml` and `src/minisweagent/config/benchmarks/programbench.yaml`. A separate diff of `agents/default.py`, `environments/local.py` and `exceptions.py` was empty. Different identities do not imply different core-loop behavior. |
| Source scope | [Pinned repository](https://github.com/SWE-agent/mini-swe-agent/tree/04d809ceab9df28f9adaed044884180159172930), checked 2026-11-09: README, package metadata, initialization, agent/local-environment code, deterministic model, LiteLLM adapter, CLI and confirmation paths. Two read-only scouts also inspected model/config paths and benchmark evidence; the coordinator checked decisive code and sources. This was not an independent-model panel. |

### Architecture and qualifications

Paths below are relative to `src/minisweagent/` at the executed pin.

| Mechanism | Checked implementation and limit |
| --- | --- |
| Small control loop | `agents/default.py`: query a model, execute its actions, append observations, save the trajectory. Models and environments are replaceable protocols. The small class is not the whole installation: `pyproject.toml` declares Python >=3.10, MIT and Alpha status, with dependencies including LiteLLM, Pydantic, datasets, Typer and Textual. |
| v2 action interface | `models/litellm_model.py` sends a `bash` tool; the text-regex adapter remains an alternative. “Only bash” describes the action surface, not absence of tool calling or restricted authority. |
| Fresh shell | `environments/local.py` starts a new `Popen(shell=True)` process/session per action. Shell exports and `cd` do not persist; filesystem effects and inherited environment do. `cwd` is a starting directory, not confinement. README's `subprocess.run` wording is an architectural shorthand, not the exact current implementation. |
| Completion | `LocalEnvironment._check_finished` raises `Submitted` for a successful command whose first non-whitespace output line is `COMPLETE_TASK_AND_SUBMIT_FINAL_OUTPUT`. It does not inspect the task's acceptance criteria. An ordinary nonzero shell exit becomes an observation, not automatic agent termination. |
| Limits | `DefaultAgent.query` checks step/cost/time before the next model query. A step counts a query, not shell actions. Reported cost is added after a response; its actions can run before the next check. Wall time does not interrupt a query or action already running. Consecutive format errors have a separate terminal state. |
| Timeout and recovery | The local environment attempts to kill the launched process group on command timeout and returns an error observation. Host signal permissions matter; already completed writes are not rolled back. This is not protection against every descendant escape or an external sink's completed action. |
| Interactive versus batch use | `run/mini.py` defaults to the interactive agent and local environment. `--yolo` changes action-confirmation mode; `--exit-immediately` separately disables the completion/new-task prompt. Supplying `-c` replaces the default config list, so an override does not implicitly retain `mini.yaml`. These are source checks, not an exercised headless CLI recipe or approval to bypass confirmations. |
| Import/config effects | Package import creates `MSWEA_GLOBAL_CONFIG_DIR` (otherwise the platform config directory) and may print a banner. The CLI's first-run wizard can write its dotenv configuration. The probe redirected home/config/temp paths and supplied no credentials. |
| Cost failure path | The LiteLLM adapter rejects missing/nonpositive cost unless `cost_tracking="ignore_errors"`; that opt-out is not a reliable spending cap and is not recommended here. The deterministic probe uses synthetic costs and does not exercise real billing or provider retries. |
| Trajectory boundary | `save` writes messages and serialized configuration as JSON. Explicit `LocalEnvironment.config.env` values are included. Ambient `os.environ` is available to commands and template variables, but is **not automatically copied wholesale** by `LocalEnvironment.serialize`. Command output, templates or explicit config can still expose secrets; this is not an authenticated, redacted acceptance record. |

### Benchmark claims are narrower than the headline

The pinned README claims >74% on SWE-bench Verified and says mini “beats Claude Code and Codex on DeepSWE.” Those are upstream claims, not results of this survey or guarantees for the checked release.

The [Datacurve primary comparison](https://deepswe.datacurve.ai/blog/deepswe#evaluation-harness), checked 2026-11-09, describes a **small pilot on the same 10 SWE-Bench Pro tasks**, not the main 113-task DeepSWE corpus:

| Model | mini pass rate | Native harness pass rate | mini / native median output tokens |
| --- | --- | --- | --- |
| Claude Opus 4.7 | 50% | Claude Code: 40% | 59k / 48k |
| GPT-5.5 | 40% | Codex CLI: 40% | 16k / 25k |
| Gemini 3.1 Pro | 40% | Gemini CLI: 20% | 18k / 15k |

Codex ties on pass rate. The primary source itself says “matches or beats” and notes possible prompt-tuning effects; output tokens are not a complete cost measure. This survey checked the published text, not trial data, task equivalence, significance or reproducibility. These results do not establish a universal daily-driver advantage, and the source's historical harness is not assumed identical to this checkout.

## Executed Offline Boundary Check

Executed the pinned `DefaultAgent`, `LocalEnvironment` and upstream `DeterministicModel` under macOS `sandbox-exec`, using Python 3.14.7 and a disposable virtual environment. Responses and costs were scripted; one tiny model subclass injected the upstream `FormatError` exception to exercise the agent's handler, not a real provider/parser.

The host used deny-default networking and writes confined to the disposable work directory. Before importing upstream code, separate protected-file read/write attempts and an IP-literal TCP connection to `1.1.1.1:443` each returned `EPERM`. The protected fixture remained `protected-baseline`. These are controls for this probe, not guarantees supplied by mini.

Final driver exit: **0**. It emitted **16 named observations**: three host-boundary controls plus thirteen mechanism cases. The count was checked independently against the emitted JSON lines and saved receipt; it is not sixteen model trials.

| Case group | Observed result |
| --- | --- |
| Shell state, ambient environment, sibling path | A shell export disappeared and `cwd` reset; a file remained. A synthetic inherited environment marker was readable. Writing `../sibling.txt` succeeded inside the host's allowed scratch tree, outside the task directory. |
| Submission and two negative controls | `Submitted` returned `claimed-done` while required `required.txt` was absent. The same marker with command exit 7, or after another output line, did not trigger submission. |
| Step bound | With `step_limit=1`, one reply executed two actions producing `AB`; the next query stopped as `LimitsExceeded`. |
| Cost bound | With limit 1.0 and synthetic response cost 1.25, the response's action ran, then the next query stopped as `LimitsExceeded`. No real charge occurred. |
| Format-error handling | Two injected errors at synthetic cost 0.4 each ended as `RepeatedFormatError`; two calls and total 0.8 were retained. |
| Wall-clock bound | A scripted 1.2-second model delay exceeded a 1-second limit; its subsequent action still wrote `late.txt`, then the next query ended as `TimeExceeded`. |
| Command timeout | The earlier `partial.txt` write survived a 1-second timeout. With the corrected host signal policy, the process group's delayed child artifact was absent after its scheduled write time. This does not prove containment of descendants that deliberately leave that group. |
| Shell-error continuation | A command exiting 7 appeared in the observation; a later scripted command submitted successfully. |
| Trajectory round trip / explicit config | Saved JSON round-tripped with `Submitted` and format `mini-swe-agent-1.1`; explicit `EXAMPLE_TOKEN=synthetic-not-a-secret` remained in serialized environment config. |

Dependencies used for the bounded probe: Pydantic 2.14.3, Jinja2 3.1.6, python-dotenv 1.2.4, platformdirs 4.14.5, Rich 15.0.0 and PyYAML 6.0.3. Only disposable dependency wheels were installed; the upstream project, provider SDK stack and host skills were not installed. No model API, credentials, container engine, benchmark or production action was used.

**Harness failures retained:** the first sandbox profile prevented executable startup (`SIGABRT`; kernel denial of reading the root directory). A literal root-directory read fixed launch without allowing descendant file contents. Timeout verification then exposed missing signal permission: `target children` allowed the direct shell but not its Python grandchild. Kernel logs identified the `same-sandbox` denial; the final profile permitted signals only within the same sandbox. Network and write boundaries were unchanged. Failed runs remain failures, not upstream regressions or passing checks.

Supporting session receipts: `local://mini-swe-ledger-2026-11-09.json` and `local://mini-swe-smoke-2026-11-09.json`. The reproducible mechanism, inputs, assertions and limits are summarized here; temporary checkout, dependencies and driver are not shipped as a TeaPrompt runner.

## Coverage and Candidate Adoption Ledger

| ID | Candidate | Disposition | Existing coverage / reopen trigger |
| --- | --- | --- | --- |
| MSW-DOC1 | Pinned source survey, worked boundary cases and catalogue discovery | Recorded; reference-only | Makes the concrete execution/evidence distinctions discoverable without a new operating contract. Refresh on upstream/source change. |
| MSW-SK1 | New minimal-agent Skill, or duplicate loop/budget/trajectory rules | No change | [Flow-loop harness](../skills/flow-loop-harness/SKILL.md) already requires external verification, bounded loops and host permissions. [Review](../skills/reflective-review/SKILL.md) distinguishes observations from self-report. [Runtime trust boundary](../04-agent/runtime-trust-boundary.md) covers effect recovery, redaction and host-owned enforcement. Reopen on a named local consumer failure, not external popularity. |
| MSW-CLI1 | Ship a mini-specific headless invocation recipe | Not adopted | The existing [headless CLI contract](../skills/headless-agent-cli-contract/SKILL.md) already requires inventory, exact transport/permission/output qualification and host budgets. Source-read flags alone do not meet it; no installed CLI or authorized tool-using recipe was exercised. |
| MSW-CTX1 | Copy fixed head/tail output limits or mandate stateless shell steps | No change | [Context engineering](../03-context/context-engineering.md) already covers selective reads and bounded artifacts. Elision can hide relevant evidence; shell reset neither guarantees idempotency nor suits every host. Reopen on an observed local truncation or state-assumption failure. |
| MSW-RUN1 | Adopt the runtime, dependencies, containers or benchmark campaign | Not adopted; outside this delivery | TeaPrompt's [standing non-goals](../PROJECT_KNOWLEDGE.md#standing-non-goals) keep it a methodology library. Deployment would need a separately authorized host, permission/budget envelope and current supply-chain review. |

## Evidence vs Inference

- **Observed:** separate source identities, two-file version delta, cited implementation, published benchmark table, real local shell/file effects, injected control-flow outcomes and JSON serialization under the recorded host boundary.
- **[INFERENCE]:** mini is a useful small reference implementation for understanding single-agent loops; that does not establish it as the best daily driver or a missing TeaPrompt capability.
- **Adjudication:** a scout's blanket “zero telemetry” and “entire environment serialized” claims were not accepted. No transitive dependency/network audit was performed; explicit config serialization differs from template access to ambient environment. Stateless actions were not promoted as idempotent actions. No automatic cost-tracking bypass was adopted.
- **Counterargument:** a tiny core can reduce inspection effort, but inspection effort is not safety or performance. Its dependency surface, arbitrary shell authority, external-effect recovery and human acceptance still require separate controls.
- **Unknown:** model efficacy, installed CLI behavior, container confinement, provider retry/billing behavior, transitive telemetry, full supply-chain safety and real-world cost. None is inferred from the offline stub run.

## Falsifiability and Handoff

- An upstream change to completion, budget timing, environment inheritance or serialization invalidates the corresponding code/probe row; re-pin and rerun that scenario.
- A matched task/model/harness comparison with complete failure and cost accounting could change the performance assessment; a README headline or a green test suite cannot.
- A reproducible failure of an existing TeaPrompt consumer could justify an in-place repair. New Skill/runtime admission remains separate from this reference-only record.
- Sufficiency: source identity, decisive mechanics, local coverage and the bounded probe are checked; operational/model claims outside that evidence remain explicit unknowns. No such unknown blocks the documentation-only decision.

Delivery changes the existing bilingual installation guides for AOM-DOC2, appends the Addy follow-through, records this survey and updates catalogue/index discovery. Skills, routing, runtime, dependencies and permanent tests stay unchanged. The [delivery report](../../review/final-report.md#mini-swe-agent-survey-and-addy-documentation-follow-through-2026-11-09) records repository verification; those checks do not certify mini's safety or efficacy. No commit or push is included.
