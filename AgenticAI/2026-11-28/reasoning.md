# AgenticAI Daily Analysis: 2026-11-28

## Scope

There is no Saturday arXiv listing batch. The two paper findings were submitted on 25 November and first listed on 26 November. The Hugging Face implementation report was published on 26 November. They were selected because they add operational evidence beyond the 27 November weekly synthesis. External repositories and artifacts were inspected read-only. No external code was cloned, installed, built, or executed.

## 1. Cost-match parallel subagents before adopting them

[When Are Parallel Subagents Effective for Coding?](https://arxiv.org/abs/2611.33893v1) compares a single coding agent with a delegating main agent on repository-construction tasks under equal-time and equal-cost views. On randomly drawn tasks, subagents improved hidden-test pass share by only about 1 to 5 percentage points while costing 2.6 to 3.8 times as much.

The gain grew on harder tasks, but the interventions show that several benefits were cheaper than parallelism. With GPT-5.6 Sol, a one-sentence instruction to probe the reference program first recovered most of the subagent gain at a fraction of the cost. Gains also shrank as the single-agent model improved its own checking. The remaining useful cases clustered around fresh context, modular code, and work that could be separated without expensive integration. A smaller Claude Code and Opus 5.5 replication showed similar patterns.

Why it matters: parallelism is an intervention with a cost and a mechanism. Add subagents only after cheaper self-checking, context reset, and modular decomposition controls fail.

Stack fit: coding-agent orchestration, cost-aware delegation, context management, and acceptance testing.

Practical methods:
- run single-agent, forced-self-check, fresh-session, and subagent variants
- compare equal cost and equal wall-clock, not raw pass rate alone
- classify tasks by decomposition and integration burden before routing
- preserve per-agent receipts and score integration failures separately
- prefer independent work units with strong acceptance tests

Implementability score: 0.86

Core source: [Parallel subagents for coding v1](https://arxiv.org/abs/2611.33893v1)

## 2. Train communication, then measure it against compute

Hugging Face's [Swarms, Flocks, Gangs](https://huggingface.co/blog/training-swarms) publishes a reproducible TRL example based on [s3](https://arxiv.org/abs/2611.08615v1). Four logical agents share one Qwen3-0.6B policy, keep separate contexts and private inputs, and learn when to message, read, and submit under a shared team reward.

Across the report's 75-step experiment, training success rose from 6.6% to 82.3%. Checkpoint 75 solved 26 of 32 held-out problems, while generated tokens per training attempt fell 37.4%, from roughly 13,000 to 8,000. Broadcasts increased while total tokens fell. The authors explicitly note that held-out token-efficiency measurements were not retained, and the information-sharing task cannot be solved by a lone agent, so it does not yet prove that a communicating team beats a compute-matched single agent on a generally solvable task.

The practical path is real but infrastructure-heavy. The walkthrough uses the public [huggingface/trl](https://github.com/huggingface/trl) swarm example and reports about five hours on two H200s, roughly $50. The larger recorded experiment used one trainer GPU and seven rollout GPUs. The underlying paper reports stronger matched-budget results, including nearly 50% less repeated exploration and up to 9.4 percentage points over best-of-N, but those claims remain task-specific.

Why it matters: communication topology is trainable behavior. Message count, success, token use, and duplication must be evaluated together.

Stack fit: multi-agent training, communication policy, team credit assignment, and cost-normalized evaluation.

Practical methods and artifacts:
- start with verifiable tasks where private evidence must be pooled
- log messages, generated tokens, duplicate work, and team reward
- compare communicating teams with independent best-of-N at matched budgets
- use shared policies before training separate models per role
- inspect the TRL example and exact revision read-only before any bounded trial

Implementability score: 0.45

Core sources: [Hugging Face swarm training report](https://huggingface.co/blog/training-swarms), [s3 paper v1](https://arxiv.org/abs/2611.08615v1), [TRL repository](https://github.com/huggingface/trl)

## Actionable cut

1. Route to parallel subagents only after a forced self-check and fresh-context control.
2. Compare every multi-agent design at equal cost and equal wall-clock.
3. Treat communication as a learned policy with its own traces and reward.
4. Keep integration burden and duplicated work in the acceptance score.
