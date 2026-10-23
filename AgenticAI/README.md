# AgenticAI

Implementation analysis for agent evaluation, memory, context policy, tools, model routing, and orchestration.

## Latest Structured Update: 2026-10-23 Daily Scan

### Route skill granularity during execution

Summary: Treat micro tools, macro skills, and macro-to-micro recovery as runtime modes selected from task structure, current state, and verified macro outcomes.

Analysis: [route skill granularity at runtime and recover from failed macros](2026-10-23/reasoning.md#route-skill-granularity-at-runtime-and-recover-from-failed-macros)

Core sources: [paper v1](https://arxiv.org/abs/2610.31461v1), [public repository](https://github.com/Jayceon-3/Adaptive-Skill-Agent)

Implementable now:
- add explicit macro preconditions and postconditions;
- record route and transition reasons;
- downgrade to primitive tools after verified macro failure;
- learn routing only after deterministic outcome logs exist.

Evidence caveat: the main comparison uses 12 mixed tasks.

Implementability score: 0.78

### Train against executable terminal state

Summary: Reuse deterministic checks of database state and side effects as evaluation oracles, task-selection signals, and training rewards.

Analysis: [train agents against executable terminal state](2026-10-23/reasoning.md#train-agents-against-executable-terminal-state)

Core sources: [implementation article](https://huggingface.co/blog/microsoft/thinkingbox-training), [public repository](https://github.com/microsoft/thinkingbox-training)

Implementable now:
- write deterministic end-state checks;
- separate the simulated user from the grader;
- track pass@1, pass@20, and repeated success;
- keep training and benchmark tasks disjoint.

Evidence caveat: the validated training run uses 24 H100 GPUs and a private training pool. The reusable result is the executable reward contract, not the reference compute footprint.

Implementability score: 0.62

## Current implication

Skills and rewards should be runtime-owned objects. Retrieve candidate procedures, then route and verify their execution. Judge the resulting world, not the agent's account of it.
