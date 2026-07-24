# AgenticAI

This index tracks the most recent structured update. Each finding includes a summary, a link into the detailed analysis, core sources, practical implementation paths, and an implementability score from 0 to 1.

## Most Recent Structured Update: Friday, 2026-07-24

### Harness-native training needs an explicit rollout adapter

Summary: OpenForgeRL records model calls and environment interactions from production-style harnesses, then feeds them into standard RL infrastructure while isolating rollouts in remote containers. The pattern makes the deployed harness trainable, but full reproduction is infrastructure-heavy and no exact public OpenForge artifact resolved.

Analysis: [daily reasoning analysis](2026-07-24/reasoning.md#harness-native-training-needs-an-explicit-rollout-adapter)
Durable topic: [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md#july-24-update-real-harness-rollouts-need-an-explicit-training-adapter)
Core source: [paper](https://arxiv.org/abs/2607.21557v1)
Implementable now:
- wrap one harness model endpoint with a recording proxy;
- bind model calls, tool receipts, state deltas, rewards, and environment digests to one rollout ID;
- replay the same policy across two harnesses;
- add explicit error-recovery rewards and tests.
Tools, repositories, and methodologies:
- OpenForgeRL architecture, veRL, Kubernetes jobs, container-per-rollout isolation, OpenTelemetry, harness ablations
Implementability score: 0.63

### Working memory should be delivered by cues, not requested by the agent

Summary: A controlled coding task records zero voluntary memory operations over 114 turns. Deterministic cue injection survives all 138 compact-resumes in the reported probe, showing that retrieval policy belongs in runtime events rather than model discretion.

Analysis: [daily reasoning analysis](2026-07-24/reasoning.md#working-memory-should-be-delivered-by-cues-not-requested-by-the-agent)
Durable topic: [Memory Systems](memory-systems/memory-systems.md#july-24-update-working-memory-delivery-should-be-a-harness-policy)
Core source: [paper](https://arxiv.org/abs/2607.20972v1)
Implementable now:
- add typed path, symbol, semantic, event, and temporal triggers;
- re-evaluate cues after compaction and resume;
- log candidate, injected, rejected, and consumed memory IDs;
- compare voluntary, always-on, and cue-triggered retrieval.
Tools, repositories, and methodologies:
- event hooks, path and symbol matchers, compaction callbacks, deterministic trigger tests, false-injection fixtures
Implementability score: 0.61

## Current implication

The harness should observe and deliver state without depending on model cooperation. Capture real rollouts for training, and inject scoped memory from deterministic runtime cues, with both boundaries replayable and independently testable.
