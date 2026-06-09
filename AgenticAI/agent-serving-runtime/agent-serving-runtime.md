# Agent Serving Runtime

Last updated: 2026-06-09

Core sources:
- AGENTSERVESIM: https://arxiv.org/abs/2606.09613v1
- Improving token efficiency in GitHub Agentic Workflows: https://github.blog/ai-and-ml/github-copilot/improving-token-efficiency-in-github-agentic-workflows/
- Token Budgets: https://arxiv.org/abs/2606.04056

## Thesis

Agent serving is not normal LLM serving with more requests. A multi-turn agent is a stateful program that alternates model calls, tool waits, file reads, user pauses, verifier checks, retries, and cache reuse. The serving runtime needs to schedule the program, not only the prompt.

## June 9 update: simulator-first routing for multi-turn agents

AGENTSERVESIM makes the missing runtime layer explicit. Request-level serving simulators optimize around isolated prompts, batch size, and model throughput. Agent workloads add turn dependencies, external tool gaps, reusable KV state, memory hierarchy choices, routing policy, and arrival-rate interactions. Testing every serving design directly on accelerators is expensive, so simulation becomes the cheap way to compare policies before production rollout.

The useful lesson is to connect the agent trace to the serving layer. If a trace records when the model was thinking, when a tool was running, when the agent paused, when KV could be reused, and when a verifier forced a retry, that trace can become simulator input. The router can then choose with evidence instead of treating every turn as stateless.

## What to build now

- Emit serving-relevant trace events: model turn, tool call start/end, wait state, retry, verifier decision, cache reuse, selected model, effective model, queue delay, and cost.
- Replay recent agent traces through a simple simulator before changing routing, batching, cache, or hardware policy.
- Compare policies by task-level latency, wall-clock time, dollar cost, failure rate, and user-visible wait, not only tokens per second.
- Treat tool-induced gaps as scheduling opportunities, but preserve privacy and tenant isolation when reusing cache or moving workloads.
- Calibrate simulator predictions against live serving telemetry before trusting them for online routing.

## What to avoid

- Treating every agent turn as a fresh stateless chat request.
- Routing only by model price or benchmark rank while ignoring tool waits and cache locality.
- Keeping serving logs separate from agent traces, which makes replay and attribution impossible.
- Optimizing accelerator utilization while making the user-visible task slower.

## Implementability score

0.58

A small offline simulator over existing traces is feasible now. Production-grade scheduling is harder because it needs calibrated latency models, cache policy, privacy boundaries, and enough real traffic to avoid optimizing for fake traces.

## Working conclusion

The agent-serving runtime should become an evidence layer between traces and routers. First trace the program, then simulate routing and cache policies, then deploy only the policies whose predicted gains survive real telemetry.
