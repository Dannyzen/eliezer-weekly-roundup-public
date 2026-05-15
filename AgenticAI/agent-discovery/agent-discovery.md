# Agent Discovery

Last updated: 2026-04-27

Core sources:
- AgentSearchBench: https://arxiv.org/abs/2604.22436
- Bingo-W/AgentSearchBench: https://github.com/Bingo-W/AgentSearchBench
- AgentSearchBench task dataset: https://huggingface.co/datasets/AgentSearch/AgentSearchBench-Tasks/viewer/single-agent_task_query

## Thesis

Agent selection is becoming a first-class part of the agentic stack. As agent libraries, marketplaces, MCP servers, and specialist tools multiply, the hard question is no longer “can I list available agents?” It is “which agent should receive this task, under this policy, with this cost budget, and what evidence says it will work?”

Descriptions are weak evidence. Behavioral traces are stronger evidence.

## Why this topic now

AgentSearchBench formalizes agent search in the wild using nearly 10,000 agents and more than 66K executions. It shows a consistent gap between semantic similarity and actual performance. That is the important lesson for builders: a pretty capability description does not prove that an agent can execute the current task.

This matters because the same pattern appears across tool routing, MCP server selection, model routing, subagent delegation, and marketplace search. The orchestrator needs a retrieval layer, a probe layer, a routing layer, and an outcome ledger.

## Architecture pattern

1. **Registry:** store agent/tool metadata, permissions, cost, latency, owner, examples, and known failure modes.
2. **Candidate retrieval:** use embeddings, lexical search, tags, and policy filters to find plausible agents.
3. **Behavioral probing:** run cheap task-class probes or smoke tests when the task is high value or risky.
4. **Execution-grounded reranking:** score candidates using probe results, historical outcomes, freshness, cost, and safety fit.
5. **Routing:** delegate only after the agent passes policy and capability checks.
6. **Outcome ledger:** record success, failure, cost, latency, tool use, and human corrections.
7. **Continuous update:** use outcomes to update future routing, but guard against overfitting to narrow benchmark tasks.

## What to build now

- Replace static “available agents” lists with a small registry that stores observed outcomes.
- Add smoke probes for common task classes: repo edit, browser task, data extraction, synthesis, code review, deployment, and support triage.
- Keep probes cheap and reversible; do not let probe execution mutate production state.
- Record why an agent was selected and whether it succeeded.
- Evaluate routing with retrieval metrics and operational metrics: NDCG, completion, cost, latency, intervention rate, and rollback rate.
- Separate selection policy from execution policy. An agent can be capable but still not authorized for a task.

## Practical tools and methods worth exploring

- AgentSearchBench datasets and leaderboard for retrieval/reranking patterns.
- Qwen, BGE, MXBAI, and similar rerankers for candidate scoring.
- LangGraph, Temporal, or Prefect for deterministic probe workflows.
- OpenTelemetry for spans around selection, probe execution, routing, and result quality.
- Policy engines such as Open Policy Agent for authorization checks before delegation.

## Pitfalls

- Ranking by README or store description alone.
- Sending a high-risk task to an unprobed specialist because its description sounds right.
- Failing to update capability records after model, prompt, tool, or permission changes.
- Using benchmarks that do not resemble real user tasks.
- Treating an agent’s capability as independent from its tool permissions and environment.
- Ignoring negative outcomes and human corrections.

## Implementability score

0.74

The pattern is implementable now with registries, probes, traces, and rerankers. The harder work is building representative probes, normalizing outcomes across heterogeneous agents, and keeping capability records fresh as the agent ecosystem changes.
