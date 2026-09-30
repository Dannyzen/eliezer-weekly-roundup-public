# AgenticAI

This index tracks the most recent structured implementation research. Each finding links to the dated analysis, primary sources, practical methods, and an implementability score.

## Latest Structured Update: 2026-09-30 Daily Scan

Wednesday's scan strengthens three implementation surfaces: explicit worker contracts, executable benchmark contracts, and composable adversarial testing.

### Compose harnesses through explicit worker contracts

Summary: Raven exposes model and harness pairs as callable workers, then coordinates them through a host agent, execution graph, artifact ledger, and persistent archive. Its public stack includes adapters for 13 external agents, including Hermes Agent.

Analysis: [daily analysis](2026-09-30/reasoning.md#compose-harnesses-through-explicit-worker-contracts)
Durable deep dives: [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md), [Multi-Agent Orchestration](multi-agent-orchestration/multi-agent-orchestration.md)
Core sources: [Raven paper](https://arxiv.org/abs/2609.33439v1), [Raven repository](https://github.com/EverMind-AI/Raven)
Tools and repositories worth exploring now: Raven, ACP, execution graphs, artifact ledgers, worker-contract validation
Implementability score: 0.68

### Make benchmark tool surfaces executable contracts

Summary: An audit of 34 mutating tools across four benchmarks confirmed seven tool defects and one evaluator property. The checker also missed most injected defects, which makes mutation testing of the checker part of the contract.

Analysis: [daily analysis](2026-09-30/reasoning.md#make-benchmark-tool-surfaces-executable-contracts)
Durable deep dives: [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md), [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core sources: [Executable-contract audit](https://arxiv.org/abs/2609.37315v1), [replication artifact](https://github.com/rohithreddybc/tool-contract-conformance)
Tools and repositories worth exploring now: tool-contract-conformance, JSON Schema, state-transition assertions, mutation testing, evaluator provenance
Implementability score: 0.86

### Turn prompt injection into a composable test matrix

Summary: pikit separates attacks, carriers, defenses, agents, traces, and verdicts. The public toolkit includes 13 attacks, 16 channels, 9 defenses, and adapters for common agent frameworks plus OpenClaw and Hermes Agent.

Analysis: [daily analysis](2026-09-30/reasoning.md#turn-prompt-injection-into-a-composable-test-matrix)
Durable deep dives: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md), [Incident Replay Testing](incident-replay-testing/incident-replay-testing.md)
Core sources: [pikit paper](https://arxiv.org/abs/2609.36817v1), [pikit repository](https://github.com/Tencent/AI-Infra-Guard/tree/main/Research/pikit)
Tools and repositories worth exploring now: pikit, delivery receipts, exact-effect judges, paired clean and attacked fixtures
Implementability score: 0.88

## Current implication

Scale agent composition only after worker interfaces, benchmark tools, adversarial delivery, and realized effects are executable and replayable.

Friday synthesis remains the current week-level map: [2026-09-25 reasoning](2026-09-25/reasoning.md).
