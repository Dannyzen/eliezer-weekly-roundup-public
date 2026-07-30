# AgenticAI

This index tracks the most recent structured research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: Thursday, 2026-07-30

### AgentGUI makes long-running agent supervision operable

Summary: AgentGUI provides a local Hermes-oriented interface for concurrent sessions, live traces, file and terminal inspection, steering, model reassignment, and automated manager audits. A controlled study found 38 percent faster trace comprehension, while one manager audit improved completion across a 0.8B to 9B model ladder.

Analysis: [daily reasoning analysis](2026-07-30/reasoning.md#agentgui-turns-long-running-agent-supervision-into-an-operational-surface)
Core sources: [paper](https://arxiv.org/abs/2607.26300v1), [MIT repository](https://github.com/eth-medical-ai-lab/agent-gui), [project](https://agent-gui-project.github.io/)
Implementable now:
- normalize agent events into one live supervision stream;
- keep redirect, pause, terminate, and model-switch controls outside worker authority;
- log intervention receipts and measure recovery.
Tools, repositories, and methodologies:
- AgentGUI, Hermes Agent, FastAPI, React, WebSockets, trajectory summaries, manager audits
Implementability score: 0.86

### MemSecBench traces poisoning through consequence and repair

Summary: The benchmark follows 310 cases across 24 agent configurations and seven checkpoints. It reports 84.2 percent malicious-memory persistence, 50.3 percent full Write-Execute success, and 56.1 percent selective repair among successfully poisoned cases.

Analysis: [daily reasoning analysis](2026-07-30/reasoning.md#memsecbench-tests-the-entire-memory-attack-lifecycle)
Core source: [paper](https://arxiv.org/abs/2607.27080v1)
Implementable now:
- link write, execute, and forget tasks under one case identity;
- verify external effects and benign-memory preservation separately;
- branch execution and repair from one verified post-write snapshot.
Tools, repositories, and methodologies:
- isolated runtimes, memory diffs, checkpoint judges, programmatic effect gates, paired backend comparisons
Implementability score: 0.68

### Cost-aware stopping controls how much tool surface an agent sees

Summary: CAM-DF converts an existing tool ranking into a cost-aware acquisition depth. Across 1,343 tasks, it performs best under heterogeneous costs and high cost pressure. A 67-task live check reduced pre-execution exposure from seven tools to 4.4 while maintaining comparable observed success.

Analysis: [daily reasoning analysis](2026-07-30/reasoning.md#cost-aware-tool-stopping-limits-exposure-before-execution)
Core source: [paper](https://arxiv.org/abs/2607.27083v1)
Implementable now:
- log ranked candidates, costs, selected prefixes, calls, and outcomes;
- start with fixed-k and score-per-cost baselines;
- shadow learned stopping before reducing production access.
Tools, repositories, and methodologies:
- tool retrievers, score-per-cost thresholds, decision-focused learning, paired bootstrap evaluation, shadow routing
Implementability score: 0.62

## Current implication

Reliable agent operations need explicit control surfaces around the model: live supervision for long runs, lifecycle evidence for memory, and cost-aware admission for tools.
