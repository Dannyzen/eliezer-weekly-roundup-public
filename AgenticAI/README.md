# AgenticAI

This index tracks the most recent structured implementation research. Each finding links to the dated analysis, primary sources, practical methods, and an implementability score.

## Latest Structured Update: 2026-09-21

### Verify hybrid computer-use agents with action-conditioned outcome tests

Summary: RecreationWorld combines GUI and code or terminal work across five platforms, then grades agents with hidden programmatic and visual assertions against running references. Static resemblance is insufficient: the leading model passed every programmatic test on only 2.8 percent of tasks.

Analysis: [daily analysis](2026-09-21/reasoning.md#verify-hybrid-computer-use-agents-with-action-conditioned-outcome-tests)
Durable deep dive: [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md)
Core sources: [paper](https://arxiv.org/abs/2609.22000v1), [repository](https://github.com/QwenLM/RecreationWorld), [dataset](https://huggingface.co/datasets/Qwen/RecreationBench), [project](https://recreation-bench.cc/)
Tools and methodologies worth exploring now: reference applications as oracles, action-conditioned state assertions, rendered visual checks, frozen reviewed tests, isolated platform images, complete-workflow scoring
Implementability score: 0.68

### Derive executable training environments from behavior, not ticket history

Summary: CodeMidas compiles implemented source behavior into specifications, executable tests, filtered tasks, and reinforcement-learning environments. The behavior-first pattern broadens the task supply beyond issues and commits, but the public implementation artifact did not resolve.

Analysis: [daily analysis](2026-09-21/reasoning.md#derive-executable-training-environments-from-behavior-not-ticket-history)
Durable deep dive: [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md)
Core source: [CodeMidas](https://arxiv.org/abs/2609.22068v1)
Tools and methodologies worth exploring now: behavioral discovery, reference execution, generated test validation, repeated solution rollouts, task lineage, license and contamination gates
Implementability score: 0.46

## Current implication

Treat executable reference behavior as the source of truth for both evaluation and task construction. A screenshot, ticket, or generated test becomes useful only after outcome checks prove that it captures the behavior that matters.
