# AgenticAI

This index tracks the most recent structured update. Each finding includes a short human-readable summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan 2026-07-01

### ECHO turns context pruning into traceable credit assignment

Summary: ECHO compresses completed turns into source-indexed memory records, reconstructs bounded policy contexts by selecting records, and routes outcome credit back to the evidence that supported successful answers. The useful implementation pattern is compact memory for action plus source pointers for learning.

Analysis: [daily reasoning analysis](2026-07-01/reasoning.md#echo-turns-context-pruning-into-traceable-credit-assignment)
Durable topics: [Memory Systems](memory-systems/memory-systems.md), [Context Economy](context-economy/context-economy.md), [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md), [Agent Serving Runtime](agent-serving-runtime/agent-serving-runtime.md)
Core source: [ECHO paper](https://arxiv.org/abs/2606.31650v1)
Implementable now:
- add stable source IDs to turn-level memory records
- log which memory IDs are selected into every bounded context
- compare full history, rolling summaries, selected turn memory, and no-memory variants
- use source-indexed selections as eval data before changing memory or compaction policy
Tools, repos, and methodologies worth exploring:
- turn-level memory ledgers, JSONL trajectory logs, offline memory-selection ablations, credit assignment over selected evidence
Implementability score: 0.74

### CubeSandbox makes agent sandboxes an egress-governed substrate

Summary: CubeSandbox is a read-only verified open-source runtime candidate for code agents: KVM/RustVMM isolation, E2B SDK compatibility, templates, snapshots, and a v0.4 CubeEgress proxy for credential injection, domain filtering, and egress audit logs.

Analysis: [daily reasoning analysis](2026-07-01/reasoning.md#cubesandbox-makes-agent-sandboxes-an-egress-governed-substrate)
Durable topics: [Sandbox-Native Agent Workers](sandbox-native-agent-workers/sandbox-native-agent-workers.md), [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md), [Agent Serving Runtime](agent-serving-runtime/agent-serving-runtime.md), [Strategy Agent Sandboxing](../Strategy/agent-sandboxing/agent-sandboxing.md)
Core sources: [CubeSandbox repo](https://github.com/TencentCloud/CubeSandbox), [v0.4 changelog](https://github.com/TencentCloud/CubeSandbox/blob/master/docs/changelog/v0.4.0.md), [security proxy guide](https://github.com/TencentCloud/CubeSandbox/blob/master/docs/guide/security-proxy.md)
Implementable now:
- evaluate CubeSandbox on a disposable KVM host, without trusting repo claims blindly
- test E2B compatibility against existing sandbox client code
- model secrets as egress-injected credentials rather than sandbox environment variables
- attach egress audit JSONL to agent run traces
Tools, repos, and methodologies worth exploring:
- CubeSandbox, E2B SDK compatibility, KVM/RustVMM, CubeEgress, domain allowlists, credential-injection rules, sandbox snapshots
Implementability score: 0.86

### agents-cli packages agent delivery as skills plus commands

Summary: Google's agents-cli turns a coding assistant into an operator for the ADK and Gemini Enterprise Agent Platform lifecycle. It ships skills and commands for scaffolding, evaluation, deployment, publishing, and observability.

Analysis: [daily reasoning analysis](2026-07-01/reasoning.md#agents-cli-packages-agent-delivery-as-skills-plus-commands)
Durable topics: [Skills as Control](skills-as-control/skills-as-control.md), [Coding Agent Control Plane](coding-agent-control-plane/coding-agent-control-plane.md), [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md)
Core sources: [google/agents-cli](https://github.com/google/agents-cli), [getting started docs](https://google.github.io/agents-cli/guide/getting-started/), [v0.6.1 release](https://github.com/google/agents-cli/releases/tag/v0.6.1)
Implementable now:
- try `uvx google-agents-cli setup` in a disposable project
- install skills only with `npx skills add google/agents-cli` for comparison
- run scaffold, eval generate, eval grade, eval analyze, and deploy on a toy ADK agent
- compare plain coding-agent output against skills-plus-CLI output on the same task
Tools, repos, and methodologies worth exploring:
- agents-cli, ADK templates, local eval datasets, trace generation, LLM-as-judge grading, Cloud Trace, lifecycle skills
Implementability score: 0.88

## Supporting recent AgenticAI context

The 2026-06-26 weekly synthesis remains the broad current implementation map: [weekly reasoning analysis](2026-06-26/reasoning.md). The 2026-06-30 scan added real workload traces and MCP server-pattern inventory. The 2026-07-01 scan adds the work-surface version: memory selection, sandbox execution, and lifecycle skills are all becoming explicit artifacts that a runtime can test.
