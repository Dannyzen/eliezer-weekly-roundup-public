# AgenticAI

This index tracks the most recent structured implementation research. Each finding links to the dated analysis, primary sources, practical methods, and an implementability score.

## Latest Structured Update: 2026-10-02 Daily Scan

Today's implementation rule is to expose control flow and experimental factors. Compile repeatable orchestration into code, evaluate the deployed configuration as a system, and intervene on retrieval before optimizing memory.

### Compile recurring multi-agent work into code

Summary: GitHub Dynamic Workflows let a Copilot extension define deterministic commands, tool calls, sequential or parallel agent stages, structured handoffs, checkpoints, resume behavior, and run limits. The feature is a public preview and Copilot CLI requires experimental mode.

Analysis: [daily analysis](2026-10-02/reasoning.md#compile-recurring-multi-agent-work-into-code)
Durable topic: [Multi-Agent Orchestration](multi-agent-orchestration/multi-agent-orchestration.md)
Core sources: [release](https://github.blog/changelog/2026-10-01-dynamic-workflows-in-copilot-cli-and-the-copilot-app/), [documentation](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/use-dynamic-workflows)
Tools and methodologies worth exploring now: Copilot CLI dynamic workflows, typed stage outputs, deterministic joins, explicit parallel branches, review checkpoints, AI-credit limits
Implementability score: 0.90

### Evaluate the whole deployed agent configuration

Summary: A factorial study across four scientific coding tasks found that repeated runs of the same configuration produced about 54 percent of outcome variance. Task information mattered more than model size or time budget, and a dedicated verification tool changed behavior more than a self-verification prompt.

Analysis: [daily analysis](2026-10-02/reasoning.md#evaluate-the-model-harness-tools-prompt-and-budget-as-one-system)
Durable topic: [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md)
Core sources: [paper](https://arxiv.org/abs/2610.01618v1), [trajectory dataset](https://huggingface.co/datasets/lusxvr/agentic-science-trajectories)
Tools and methodologies worth exploring now: factorial configuration sweeps, repeated cells, variance decomposition, dedicated verification tools, trajectory taxonomies
Implementability score: 0.82

### Intervene on retrieval before optimizing memory

Summary: Causal Memory Policy found that 54 percent of required LongMemEval memories and 67 percent on LoCoMo were never exposed to a utility estimator. Randomized retrieval slots with known propensities improved discrimination from 0.54 to 0.66 AUC, while unseen-query retention value remained unresolved.

Analysis: [daily analysis](2026-10-02/reasoning.md#intervene-on-retrieval-before-using-memory-utility)
Durable topic: [Memory Systems](memory-systems/memory-systems.md)
Core source: [Causal Memory Policy](https://arxiv.org/abs/2610.02070v1)
Tools and methodologies worth exploring now: bounded retrieval exploration, propensity logging, inverse-propensity estimates, reversible demotion, no-delete controls
Implementability score: 0.68

## Current implication

Make workflow structure, configuration choices, and retrieval exposure visible in the trace. Optimization is trustworthy only when the system records which control path and evidence opportunity produced the result.

Latest roundup: [2026-10-02](../roundups/2026-10-02.md).
