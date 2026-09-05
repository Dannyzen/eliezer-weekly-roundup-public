# Agent Serving Runtime

Last updated: 2026-06-30

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

## June 22 update: serving policy needs runtime-level trace fields, not framework names

Google ADK and tRPC-Agent-Go reinforce the serving-runtime point from the application side. If an agent framework exposes graph workflows, tasks, sessions, memory, tool calls, retries, and cancellation, the serving layer can treat an agent as a stateful program rather than a pile of unrelated chat completions.

The practical move is to preserve serving-relevant fields regardless of framework: workflow node, agent role, model call, selected model, session ID, memory touch, tool wait, retry reason, cancellation, human pause, cache reuse, latency, and cost. Without those fields, model routing and capacity planning stay blind.

Sources:
- [ADK docs](https://adk.dev/)
- [tRPC-Agent-Go](https://github.com/trpc-group/trpc-agent-go)

## June 30 update: TraceLab turns coding-agent serving into a measured workload

TraceLab gives this topic the missing public baseline. The paper reports roughly 4,300 coding-agent sessions, about 350,000 LLM steps, and about 430,000 tool calls from Claude Code and Codex usage. The project page exposes a public pool with 357,161 agent steps and 432,510 tool calls.

Practical lesson:
- log agent steps, model calls, tool calls, prefix-cache reuse, append length, compactions, human waits, retries, and costs as first-class serving fields;
- compare local coding-agent traces against TraceLab before changing cache, batching, or model-routing policy;
- make tool latency and human-paced gaps scheduler inputs, not analytics afterthoughts;
- optimize by task-level wall-clock, cost, and failure rate, not only tokens per second.

Source:
- [TraceLab](https://arxiv.org/abs/2606.30560v1)
- [SyFI TraceLab project](https://tracelab.cs.washington.edu/)
- [uw-syfi/TraceLab](https://github.com/uw-syfi/TraceLab)

## What to avoid

- Treating every agent turn as a fresh stateless chat request.
- Routing only by model price or benchmark rank while ignoring tool waits and cache locality.
- Keeping serving logs separate from agent traces, which makes replay and attribution impossible.
- Optimizing accelerator utilization while making the user-visible task slower.

## Implementability score

0.58

A small offline simulator over existing traces is feasible now. Production-grade scheduling is harder because it needs calibrated latency models, cache policy, privacy boundaries, and enough real traffic to avoid optimizing for fake traces.


## July 30 update: supervision is a runtime surface

AgentGUI makes the operator loop concrete for Hermes-class agents. Long-running work needs normalized live events, compact trajectory views, visible artifacts, and explicit intervention controls. The important primitive is not the pixel-art interface. It is the mapping from a run event to an operator decision and then to a measured recovery.

Practical lesson:
- normalize model turns, tool calls, file changes, waits, verifier results, and interventions;
- keep pause, redirect, model switch, terminate, and artifact release outside worker authority;
- preserve pre-intervention state, operator action, post-intervention state, and outcome under one run ID;
- measure time-to-diagnosis, false alarms, recovery rate, and operator workload;
- treat automated manager audits as a second policy layer, not as independent proof.

Artifact caveat: the repository is populated and MIT-licensed, but the user study is small and the automated audit test covers one quantitative completion task.

Sources:
- [AgentGUI](https://arxiv.org/abs/2607.26300v1)
- [eth-medical-ai-lab/agent-gui](https://github.com/eth-medical-ai-lab/agent-gui)
- [AgentGUI project](https://agent-gui-project.github.io/)

## September 4, 2026 update: the serving adapter is part of the measurement

Interface-Induced Trajectory Censoring shows that a tool-call rate read off the serving stack can be zero while the model emits well-formed calls. On BFCL v4, changing only the adapter moves 0.00 to 0.96 / 0.19. Qwen2.5-Coder 32B emits 80/100 well-formed calls while the hermes parser reports 0/100. GRPO can raise pass@1 while multi-turn rescues stay flat.

Practical lesson:

- log raw completion bytes, parser output, and executor admissions as three counters
- run a template-by-parser 2x2 before publishing a tool-call score
- fail closed when HTTP 200 returns empty `tool_calls` but the completion contains a call
- read ERRATA.md before citing the training numbers

The public repository is populated. No clone or execute from this cron.

Implementability score: 0.80

Sources:

- [Interface-Induced Trajectory Censoring](https://arxiv.org/abs/2609.03966v1)
- [nebula-1999/Interface-Induced-Trajectory-Censoring](https://github.com/nebula-1999/Interface-Induced-Trajectory-Censoring)

## September 5, 2026 update: speculate into a snapshot, commit on first-action match

Speculative Macro Commit drafts multi-step macros with a cheap model on an isolated environment snapshot. The official actor commits the remainder only when its next tool call matches the first drafted action. AppWorld wall time falls 44.9% versus sequential execution, with TGC 70/168 to 68/168. Do not expose mined macros as extra tools and hope the model selects them.

Implementability score: 0.55

Source: [Speculative Macro Commit](https://arxiv.org/abs/2609.03236v1)


## Working conclusion

The agent-serving runtime should become an evidence layer between traces and routers. First trace the program, then simulate routing and cache policies, then deploy only the policies whose predicted gains survive real telemetry.
