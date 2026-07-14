# AgenticAI

This index tracks the most recent structured update. Each finding includes a short human-readable summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan, 2026-07-14

### AgentCheck turns MCP faults into replayable regression fixtures

Summary: AgentCheck records clean tool responses, injects one controlled fault while replaying matching calls, then reruns the identical fault after a mitigation. The public workbench includes 120 scenarios across 12 fault types, deterministic checks, experiment outputs, and an MIT license.

Analysis: [daily reasoning analysis](2026-07-14/reasoning.md#agentcheck-turns-mcp-faults-into-replayable-regression-fixtures)
Durable topic: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core sources: [AgentCheck paper](https://arxiv.org/abs/2607.11098v1), [aritra741/AgentCheck](https://github.com/aritra741/AgentCheck)
Implementable now:
- inject timeout, stale-data, schema-drift, permission, poisoning, and corruption faults into one internal MCP server
- keep deterministic verdicts load-bearing and LLM labels diagnostic
- gate releases on clean, faulted, and mitigated replay traces
Tools, repositories, and methodologies worth exploring:
- `aritra741/AgentCheck`, MCP proxies, response caches, fault injectors, deterministic graders, OpenTelemetry
Implementability score: 0.90

### ToolAtlas moves execution-verified memory to the tool provider

Summary: ToolAtlas stores tool traces, capabilities, failure boundaries, and cross-tool compositions in provider-owned graphs built through verified probing. The memory can be reused across downstream agents and environment instances instead of being rediscovered inside each agent transcript.

Analysis: [daily reasoning analysis](2026-07-14/reasoning.md#toolatlas-moves-execution-verified-tool-memory-to-the-provider-side)
Durable topic: [Enterprise MCP Orchestration](enterprise-mcp-orchestration/enterprise-mcp-orchestration.md)
Core sources: [ToolAtlas paper](https://arxiv.org/abs/2607.11126v1), [PuppyKnightUniversity/ToolAtlas](https://github.com/PuppyKnightUniversity/ToolAtlas)
Implementable now:
- define provider-owned capability, boundary, verifier, and composition records
- build memory only from verified probes and preserve failed probes as evidence
- filter provider memory by principal, tenant, policy, and tool version at the gateway
Tools, repositories, and methodologies worth exploring:
- `PuppyKnightUniversity/ToolAtlas`, MCPMark, MCP-Universe, graph memory, capability frontier probing, verifier-labeled rollouts
Implementability score: 0.78

### Compile Then Page makes procedures executable but keeps paging model-gated

Summary: The method compiles machine-readable SOP constraints into pseudo-code with explicit verifiers and evidence-bearing returns, then runs a symbolic stack machine beside the LLM. Compiled representation is consistently useful, but active-frame paging helps strong models and harms weak ones.

Analysis: [daily reasoning analysis](2026-07-14/reasoning.md#compile-then-page-makes-procedures-executable-but-keeps-paging-capability-gated)
Durable topic: [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md)
Core source: [Compile, Then Page](https://arxiv.org/abs/2607.11346v1)
Implementable now:
- compile one SOP into explicit states, verifier recipes, branches, and refusal exits
- preserve source rule IDs and evidence in every runtime transition
- compare prose, compiled full text, and paged runtime variants per model
Tools, repositories, and methodologies worth exploring:
- typed state machines, Pydantic, JSON Schema, Temporal, LangGraph, SOPBench, state-discipline probes
Artifact caveat:
- no public implementation repository was found during this scan
Implementability score: 0.58

## Supporting recent AgenticAI context

The July 14 scan turns tool reliability into a provider and runtime responsibility. Replayable faults expose whether a mitigation works, provider-side memory prevents every agent from rediscovering the same boundaries, and compiled procedures make paging an explicit model capability decision instead of a prompt-layout guess.
