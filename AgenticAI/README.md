# AgenticAI

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan 2026-06-07

### Failed trajectories should become harness repairs, not prompt patches
Summary: A failed agent run should become a layer-attributed harness repair candidate. The first move is not another prompt tweak. It is trace replay across tools, context, lifecycle, verification, environment, policy, and model behavior.

Analysis: [daily reasoning analysis](2026-06-07/reasoning.md#failed-trajectories-should-become-harness-repairs-not-prompt-patches)
Durable topics: [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md), [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core source: [From Failed Trajectories to Reliable LLM Agents](https://arxiv.org/abs/2606.06324v1)
Implementable now:
- capture trace IR with task state, tools, observations, verifiers, lifecycle events, and policy decisions;
- replay failures before mutating prompts;
- label the broken harness layer and promote repaired failures into regression fixtures.
Tools, repos, and methodologies worth exploring:
- trace IRs, failed-trajectory replay, layer-attributed failure labels, OpenTelemetry spans, LangSmith-style traces, harness regression fixtures
Implementability score: 0.82

### Multi-agent workflows need normalized baselines before more agents
Summary: Multi-agent systems should beat matched single-agent baselines under the same loader, tool access, answer contract, usage accounting, and trajectory logging. Otherwise the topology is getting unearned credit.

Analysis: [daily reasoning analysis](2026-06-07/reasoning.md#multi-agent-workflows-need-normalized-baselines-before-more-agents)
Durable topic: [Multi-Agent Orchestration](multi-agent-orchestration/multi-agent-orchestration.md)
Core sources: [Do More Agents Help?](https://arxiv.org/abs/2606.05670v1), [MASArena / BenchAgent](https://github.com/LINs-lab/MASArena/tree/BenchAgent)
Implementable now:
- compare single-agent, fixed-MAS, and evolving-MAS runs under identical protocols;
- log inter-agent messages, tool calls, cost, latency, and final-state checks;
- run topology ablations before adding broadcast collaboration.
Tools, repos, and methodologies worth exploring:
- BenchAgent-style protocol alignment, MASArena metadata, topology ablations, usage-normalized scorecards, inter-agent trace logs
Implementability score: 0.75

### Memory search needs policy and bitemporal conflict handling
Summary: Personal-agent memory should not inject the nearest embedding by default. Retrieval needs policy gates, and persistent writes need bitemporal contradiction handling with evidence and supersession.

Analysis: [daily reasoning analysis](2026-06-07/reasoning.md#memory-search-needs-policy-and-bitemporal-conflict-handling)
Durable topic: [Memory Systems](memory-systems/memory-systems.md)
Core sources: [Beyond Similarity](https://arxiv.org/abs/2606.06054v1), [TOKI](https://arxiv.org/abs/2606.06240v1), [TOKI repository](https://github.com/ZenAlexa/toki-bitemporal-memory)
Implementable now:
- gate memory retrieval by domain, sensitivity, consent, recency, confidence, and downstream tool action;
- store bitemporal facts with evidence, valid time, transaction time, supersession, and conflict operator;
- test stale, sensitive, contradictory, cross-domain, and action-triggering memories.
Tools, repos, and methodologies worth exploring:
- bitemporal fact stores, retrieval policy gates, evidence-linked memory rows, conflict-resolution operators, memory safety fixtures
Implementability score: 0.69

## Previous structured update

The prior daily scan for 2026-06-06 focused on memory as a profiled systems workload and causal tool-frontier filtering: [2026-06-06 roundup](../roundups/2026-06-06.md).
