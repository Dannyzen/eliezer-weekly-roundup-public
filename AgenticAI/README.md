# AgenticAI

The latest daily scan is 2026-11-28. Its thesis is that multi-agent systems earn their complexity only when gains survive equal-cost controls and communication leaves measurable evidence.

## Latest findings

### Cost-match parallel subagents before adopting them

Summary: Random repository-construction tasks gained only about 1 to 5 hidden-test percentage points from subagents at 2.6 to 3.8 times the cost. Forced self-checking recovered much of the gain cheaply in one model setting.

Analysis: [Cost-match parallel subagents before adopting them](2026-11-28/reasoning.md#1-cost-match-parallel-subagents-before-adopting-them)

Core source: [Parallel subagents for coding](https://arxiv.org/abs/2611.33893v1)

Implementable now:
- equal-cost and equal-time orchestration bakeoffs
- forced-self-check and fresh-session controls
- decomposition and integration-burden classifiers
- per-agent acceptance receipts

Implementability score: **0.86**

### Train communication, then measure it against compute

Summary: Four agents sharing one small policy learned to pool private evidence while training success rose and token use fell. The current demonstration still needs generally solvable, compute-matched single-agent controls.

Analysis: [Train communication, then measure it against compute](2026-11-28/reasoning.md#2-train-communication-then-measure-it-against-compute)

Core sources: [Hugging Face swarm training](https://huggingface.co/blog/training-swarms), [s3](https://arxiv.org/abs/2611.08615v1), [TRL](https://github.com/huggingface/trl)

Implementable now:
- verifiable shared-information environments
- shared team rewards and policy weights
- message, token, and duplicate-work traces
- matched-budget best-of-N baselines

Implementability score: **0.45**

## Browse

- [Daily synthesis](../roundups/2026-11-28.md)
- [Dated AgenticAI analysis](2026-11-28/reasoning.md)
- [November 27 weekly synthesis](../roundups/2026-11-27.md)
- [Multi-agent orchestration](multi-agent-orchestration/multi-agent-orchestration.md)
- [Trajectory-aware evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
