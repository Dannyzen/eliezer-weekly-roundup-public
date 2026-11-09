# AgenticAI

Implementation research for the deployed agent loop: tool use, memory, orchestration, evaluation, testing, and work-state continuity.

## Latest structured update: 2026-11-09

### Train exact workflows against executable verifiers

Summary: a 3.35B model fine-tuned on scripted TaxOps trajectories reached 93.3 percent exact success on 300 held-out synthetic returns with 0.030 wasted calls per case. The strongest change corrected the demonstration policy instead of teaching more recovery behavior.

Analysis: [Daily analysis](2026-11-09/reasoning.md#1-train-exact-workflows-against-executable-verifiers)

Core source: [TaxOps](https://huggingface.co/blog/Manoj2142/taxops-efficient-tool-agent)

Implementable now:
- typed tools and deterministic final-state verifiers
- scripted oracle trajectories
- exact success, field accuracy, waste, token, and latency metrics
- shifted cases with unseen decoys

Implementability score: 0.78

### Preserve expert cooperation when shrinking MoE models

Summary: HOPE chooses experts with pairwise co-activation and contribution statistics. At 50 percent pruning it outperformed four first-order methods and preserved reported agentic coding performance on Qwen3.5-35B-A3B.

Analysis: [Daily analysis](2026-11-09/reasoning.md#2-preserve-expert-cooperation-when-shrinking-moe-models)

Core source: [implementation walkthrough](https://huggingface.co/blog/amazon/higher-order-pruning-experts)

Implementable now:
- calibration on representative agent trajectories
- interaction-aware and first-order pruning comparisons
- versioned prune-set artifacts
- target-workload quality and serving-cost gates

Implementability score: 0.58

## Current working model

1. Compile bounded workflows into typed actions and executable effects.
2. Train and test against exact verifiers, not prose judgments alone.
3. Preserve cooperative structure when routing or pruning model capacity.
4. Bind every optimization to the exact workload, checkpoint, and receipt.
5. Keep release oracles independent from the acting model.

## Browse

- [Latest roundup](../roundups/2026-11-09.md)
- [Latest dated analysis](2026-11-09/reasoning.md)
- [Friday synthesis](2026-11-06/reasoning.md)
- [Agent harness architecture](agent-harness-architecture/agent-harness-architecture.md)
- [Agent serving runtime](agent-serving-runtime/agent-serving-runtime.md)
- [Memory systems](memory-systems/memory-systems.md)
- [Trajectory-aware evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
- [Skills as control](skills-as-control/skills-as-control.md)
- [Multi-agent orchestration](multi-agent-orchestration/multi-agent-orchestration.md)
