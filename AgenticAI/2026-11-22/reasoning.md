# AgenticAI Daily Analysis: 2026-11-22

## Scope

Sunday has no new arXiv listing batch. The paper findings are Friday carry-forwards submitted on 19 November and first listed on 20 November. They were selected because they add uncaptured implementation controls. Cloudflare's release is also dated 20 November. External repositories and artifacts were inspected read-only. No external source was cloned or executed.

## 1. Test context compaction by resuming the task

[CompAct-Bench](https://arxiv.org/abs/2611.25673v1) measures whether an executor can finish after another model compacts the working context at an intermediate boundary. Its 200 tasks span 79 BrowseComp searches, 96 SWE-bench tasks, and 25 internal CompanyBench workspace tasks. Every retained task had succeeded in all three pre-compaction screening runs. After compaction, average success across 12 compactors fell to 56.7%, and the best reached 68.5%.

The key distinction is between facts and state. Omitting a useful fact forces repeated search. Falsely marking unresolved work as complete prevents the executor from revisiting it. Summary similarity does not expose either failure reliably.

Why it matters: context compaction is a runtime state transition. It should be tested by restoring the same environment, applying a fixed continuation budget, and grading the completed task.

Stack fit: context economy, session checkpoints, trajectory evaluation, and long-horizon recovery.

Practical methods and artifacts:
- freeze environment state and action budget at the compaction boundary
- replay several compactor candidates with one fixed executor
- score final task completion, repeated work, and false completion claims
- retain unresolved goals, completed effects, resource identities, and evidence pointers as typed fields
- use the [CompAct-Bench project page](https://compaction-eval.github.io/CompAct-Bench/) as a protocol reference; a downloadable benchmark implementation was not verified

Implementability score: 0.72

Core source: [CompAct-Bench v1](https://arxiv.org/abs/2611.25673v1)

## 2. Tune memory dosage per model and conserve provenance

[How Much Should an Agent Remember?](https://arxiv.org/abs/2611.26361v1) reports that memory volume has model-dependent effects. On AppWorld's 168-task `test_normal` split, DeepSeek-V3.2 rose from 79.8% to 89.3% as its injected set grew to all 191 consolidated guidelines. A weaker gpt-oss-120b configuration reached 51.2% with all 199 guidelines and 55.4% as the mean of two runs with about 29 selected guidelines.

The operational lesson is selection, not a universal ideal memory size. The paper also shows why provenance must survive consolidation: support counts become unreliable when merged guidance loses its independent derivation records. The configuration comparison used `test_normal` because no separate held-out selection split remained, so the selected-set maximum is optimistic rather than an unbiased deployment estimate.

Why it matters: memory admission needs model-specific dose curves, source lineage, support counts, and downstream task replay. More stored guidance is not automatically more useful guidance.

Stack fit: procedural memory, memory promotion, retrieval policy, and prospective evaluation.

Practical methods and artifacts:
- preserve source episode IDs through extraction and consolidation
- count independent supporting derivations, not repeated paraphrases
- evaluate increasing memory subsets against one fixed scaffold
- select dosage on a development split and report the held-out result separately
- fail loudly when task or tool errors would otherwise be swallowed
- inspect [AgentToolkit/altk-evolve](https://github.com/AgentToolkit/altk-evolve) read-only before any trial

Implementability score: 0.86

Core sources: [deployment lessons paper v1](https://arxiv.org/abs/2611.26361v1), [altk-evolve repository](https://github.com/AgentToolkit/altk-evolve)

## 3. Park durable waits instead of holding an agent invocation

[Cloudflare Agents SDK v0.34.0](https://developers.cloudflare.com/changelog/post/2026-11-20-pi-harness-pi-1-6/) upgrades PiHarness to Pi 1.6. A tool can park until a human response, deadline, or another session signal, while the Durable Object hibernates and holds no invocation. Sessions can also start from existing history.

Why it matters: approval gates and subagent waits should be explicit persisted state, not polling loops or live model calls. This connects session semantics directly to capacity control.

Stack fit: durable orchestration, human approval, session recovery, and serving efficiency.

Practical methods and artifacts:
- represent waits as persisted park records with deadline and signal identity
- make signal delivery idempotent and bind it to the parked tool call
- resume from durable history rather than reconstructing state from chat text
- test timeout, duplicate signal, cancellation, and MCP reauthorization paths
- retain a migration gate because Pi 1.6 conversations cannot roll back to Pi 1.5

Implementability score: 0.85

Core sources: [Cloudflare changelog](https://developers.cloudflare.com/changelog/post/2026-11-20-pi-harness-pi-1-6/), [Cloudflare Agents repository](https://github.com/cloudflare/agents)

## Actionable cut

1. Grade compaction by completed work after replay.
2. Keep unresolved state and completed effects typed through compaction.
3. Tune memory dosage against a fixed scaffold and a held-out split.
4. Persist waits as resumable runtime objects instead of active invocations.
