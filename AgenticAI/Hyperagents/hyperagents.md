# Hyperagents

## Overview
Hyperagents are multi-agent orchestration patterns where distinct roles collaborate on a larger task. In practice, this usually means one agent plans, others execute subtasks, and another verifies or synthesizes results.

## How it fits into the agentic stack
Hyperagents sit above individual tool calls. They are an orchestration strategy, not a single model capability. They are most useful when the task naturally decomposes into roles with clear boundaries.

## Implementable now
- LangGraph for stateful planner-worker-reviewer graphs.
- AutoGen and CrewAI for fast multi-agent prototypes.
- SQLite, Postgres, or Redis for shared state.
- OpenTelemetry or LangSmith for visibility into each role.

## Methodologies
- define role boundaries before adding agents
- use shared state, not only message passing
- keep one owner for final output quality
- add retry policies before adding more complexity

## Implementability score
0.49

## Complexity to implement
Medium to high.
- You need explicit state sharing.
- You need retry and failure rules.
- You need clear ownership for decisions and outputs.

## When to use it
Use hyperagent patterns when one model loop becomes too crowded with planning, execution, validation, and summarization responsibilities.

## Research links
- [Weekly synthesis note](../../roundups/2026-04-05.md#signals-emerging-trends)
- [Meta structured prompting article](https://venturebeat.com/orchestration/metas-new-structured-prompting-technique-makes-llms-significantly-better-at)
- [LangGraph](https://github.com/langchain-ai/langgraph)
- [AutoGen](https://github.com/microsoft/autogen)
- [CrewAI](https://github.com/crewAIInc/crewAI)
