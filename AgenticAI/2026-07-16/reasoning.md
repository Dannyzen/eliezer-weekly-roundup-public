
# AgenticAI Daily Analysis - 2026-07-16

## Daily thesis

The strongest implementation signal is separation of control decisions from model behavior. Agent evaluation should separate benchmark, harness, and environment. Memory should expose retrieval, plan injection, consolidation, and forgetting as policy actions. Both make the system easier to test than a monolithic agent loop.

## AgentCompass separates benchmark, harness, and environment

AgentCompass defines three independent evaluation components: benchmark task and scoring semantics, harness interaction logic, and environment execution primitives. That decomposition matters because model, scaffold, task world, and infrastructure failures otherwise collapse into one pass rate.

The paper reports support for more than 20 benchmarks across five capability dimensions, an asynchronous fault-tolerant runtime, and trajectory analysis for failures such as reward hacking. The public repository is active, has a populated 494-entry tree, exposes CLI and Python entry points, and documents 21 current benchmarks covering tool use, deep research, coding, and GUI interaction.

Why it matters:
- one benchmark can compare multiple harnesses without rewriting execution logic;
- one harness can be evaluated across different environments and model protocols;
- retry details, progress events, run metadata, and per-task records become reusable evidence;
- environment and harness regressions can be diagnosed separately from model capability.

How it fits the stack:
- evaluation substrate below model and agent comparisons;
- trajectory and retry evidence beside the runtime;
- benchmark, harness, and environment registries as explicit integration contracts.

Implementable now:
- define separate interfaces for task preparation and scoring, agent execution, and environment actions;
- store run configuration, model identity, harness version, environment identity, retry records, and per-task results under one run ID;
- compare at least two harnesses with the same model, task set, budget, and environment;
- treat post-analysis as diagnostic unless its verdict is backed by deterministic checks.

Tools, repositories, and methodologies worth exploring:
- `open-compass/AgentCompass`;
- Terminal-Bench, SWE-bench, SkillsBench, and GUI benchmarks behind one component model;
- OpenAI Chat, OpenAI Responses, and Anthropic protocol adapters;
- async task runners, deterministic task scorers, trajectory viewers, and OpenTelemetry.

Artifact caveat:
- the repository had no detected license file, published release, or package release during this read-only scan;
- the repository was inspected through metadata, tree, README, and docs only, not installed or executed.

Implementability score: 0.84

Core sources:
- https://arxiv.org/abs/2607.13705v1
- https://github.com/open-compass/AgentCompass

## MemCon makes memory access a feedback-controlled policy

MemCon treats memory behavior as a small control problem rather than a fixed retrieval heuristic. Its policy chooses when and how much to retrieve, when to inject a plan, when to re-retrieve after the agent is stuck, and when to consolidate, forget, or do nothing.

The controller is intentionally lightweight: a tabular contextual bandit with UCB exploration, task-level binary feedback, no pretraining, and no additional LLM calls. Across six benchmarks, three agent frameworks, and three model backbones, the paper reports up to 15.2 points higher task success and 5 to 20 percent lower token consumption than tested baselines.

Why it matters:
- retrieval volume becomes an observable decision rather than a hidden constant;
- no-op and forget actions make restraint part of memory quality;
- task outcome can update memory policy without rewriting stored knowledge;
- the same controller can wrap different memory backends.

How it fits the stack:
- a memory control plane between durable stores and active context;
- task feedback as a policy signal, not permission to rewrite evidence;
- consolidation and forgetting as explicit operations with separate audit needs.

Implementable now:
- start with a fixed state vector: goal type, step phase, stuck signal, memory size, plan availability, and learning phase;
- expose retrieve, plan inject, re-retrieve, consolidate, forget, and no-op actions;
- log chosen action, policy state, selected memory IDs, token cost, task outcome, and update;
- keep memory truth, provenance, and deletion authority outside the learned controller;
- compare static retrieval, always-on retrieval, selective intervention, and learned control on identical task streams.

Tools, repositories, and methodologies worth exploring:
- `ericjiang18/MemCon` as a read-only architecture reference;
- contextual bandits with UCB;
- MemOps operation traces for correctness;
- event-sourced memory, bitemporal evidence, and explicit abstention.

Artifact caveat:
- the repository README declares MIT, but no license file was detected by GitHub metadata;
- the 6,678-entry tree vendors multiple frameworks, has no release, and was last pushed on May 7;
- pilot the controller contract before considering the full experiment stack.

Implementability score: 0.73

Core sources:
- https://arxiv.org/abs/2607.13591v1
- https://github.com/ericjiang18/MemCon

## Watchlist: Harness Handbook maps behavior to code evidence

Harness Handbook is the right representation idea for evolving large agent runtimes. It organizes code into system overview, behavior-unit overview, and behavior-unit detail, then links each claim back to static program facts. Its Behavior-Guided Progressive Disclosure method starts from a behavior question and narrows toward source evidence and an edit plan.

The pattern is actionable, but the public surface is a paper, project page, and interactive studio rather than a reusable implementation package. Treat it as a design reference for code graphs, call-path analysis, and behavior localization.

Source:
- https://arxiv.org/abs/2607.13285v1
- https://ruhan-wang.github.io/Harness-Handbook/

## Stack implication

Agent systems become easier to improve when evaluation and memory stop being invisible helper logic. Make their decisions typed, versioned, and attributable. Then a model or policy can be changed without erasing which benchmark, harness, environment, memory action, and verifier produced the result.
