# AgenticAI

This index tracks the most recent structured update. Each finding includes a short human-readable summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Week ending 2026-06-26

### Repository-local agent control becomes a tested supply-chain artifact

Summary: Repo-local agent instructions are becoming a real control surface. `AGENTS.md`, `DESIGN.md`, IDE rules, and coding-agent configs need probes, hashes, permission declarations, drift checks, and compiled targets instead of living as unmanaged prose.

Analysis: [weekly reasoning analysis](2026-06-26/reasoning.md#repository-local-agent-control-becomes-a-tested-supply-chain-artifact)
Durable topics: [Coding Agent Control Plane](coding-agent-control-plane/coding-agent-control-plane.md), [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md), [Skills as Control](skills-as-control/skills-as-control.md), [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core sources: [Probe-and-Refine](https://arxiv.org/abs/2606.20512v1), [A Deterministic Control Plane for LLM Coding Agents](https://arxiv.org/abs/2606.26924v1), [GitHub AGENTS.md support](https://github.blog/changelog/2026-06-18-copilot-code-review-agents-md-support-and-ui-improvements), [DESIGN.md](https://github.com/google-labs-code/design.md)
Implementable now:
- add concise `AGENTS.md` files and test them with synthetic bug-fix probes
- maintain `DESIGN.md` or equivalent UI context as a linted artifact
- hash and lock agent rules, skill references, tool permissions, and generated client targets
- log config hash, target client, permission profile, and drift verdict with each run
Tools, repos, and methodologies worth exploring:
- `AGENTS.md`, `DESIGN.md`, repo guidance probes, SHA-256 lockfiles, CI config linters, OpenTelemetry config spans, content-addressed agent definitions
Implementability score: 0.82

### Runtime blueprints and tool tests make agent services reviewable

Summary: Agent services are becoming normal platform surfaces. ADK, tRPC-Agent-Go, UnifAI, AssetOpsBench, ToolBench-X, and Constraint Tax all point toward reviewable workflow topology, explicit tools, session state, traces, recovery tests, and separation between tool reasoning and strict serialization.

Analysis: [weekly reasoning analysis](2026-06-26/reasoning.md#runtime-blueprints-and-tool-tests-make-agent-services-reviewable)
Durable topics: [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md), [Multi-Agent Orchestration](multi-agent-orchestration/multi-agent-orchestration.md), [Agent Serving Runtime](agent-serving-runtime/agent-serving-runtime.md), [Agent Gateway Governance](../Strategy/agent-gateway-governance/agent-gateway-governance.md)
Core sources: [Google ADK](https://adk.dev/), [tRPC-Agent-Go](https://github.com/trpc-group/trpc-agent-go), [UnifAI](https://github.com/redhat-community-ai-tools/UnifAI), [ToolBench-X](https://arxiv.org/abs/2606.25819v1), [Constraint Tax](https://arxiv.org/abs/2606.25605v1)
Implementable now:
- put graph or YAML workflow definitions under code review
- require trace IDs, tool contracts, retriever declarations, execution backend, and owner before deployment
- add unreliable-tool fixtures for high-value workflows
- test tool calling plus strict schema output jointly, then use two-pass execution where needed
Tools, repos, and methodologies worth exploring:
- Google ADK, tRPC-Agent-Go, UnifAI, ToolBench-X, AssetOpsBench, Temporal, LangGraph, A2A/MCP integration contracts, two-pass structured output
Implementability score: 0.74

### Evaluation moves to evidence paths, recovery, and novelty

Summary: Final-answer grading is too lossy for agents. GroundEval, RigorBench, ToolBench-X, MIRROR, and GUI-vs-CLI evals make source paths, raw evidence, process discipline, recovery behavior, novelty, and final-state verification the useful scoring layer.

Analysis: [weekly reasoning analysis](2026-06-26/reasoning.md#evaluation-moves-to-evidence-paths-recovery-and-novelty)
Durable topics: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md), [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md), [Agentic Search and Retrieval](agentic-search/agentic-search.md), [Evidence Provenance Control Plane](../Strategy/evidence-provenance-control-plane/evidence-provenance-control-plane.md)
Core sources: [GroundEval](https://arxiv.org/abs/2606.22737v1), [RigorBench](https://arxiv.org/abs/2606.22678v1), [ToolBench-X](https://arxiv.org/abs/2606.25819v1), [MIRROR](https://arxiv.org/abs/2606.26793v1), [GUI vs. CLI](https://arxiv.org/abs/2606.24551)
Implementable now:
- attach source IDs, raw-output references, access scope, and retrieval timestamps to traces
- add deterministic evidence-path checks before LLM-as-judge scoring
- score planning, verification, recovery, abstention, and atomic transition integrity
- report duplicate rates and novelty-adjusted red-team success, not only attack success
Tools, repos, and methodologies worth exploring:
- GroundEval-style validators, RigorBench-style process rubrics, ToolBench-X recovery tests, MIRROR novelty gates, final-state verifiers, OpenTelemetry trace fields
Implementability score: 0.80

### Agent state becomes ledgered, event-sourced, and reusable

Summary: Agents should not reconstruct state from transcripts. LedgerAgent, ESAA-Conversational, Multi-Agent Transactive Memory, and governed shared memory converge on typed ledgers, append-only event logs, deterministic handoff projections, and indexed trajectory reuse.

Analysis: [weekly reasoning analysis](2026-06-26/reasoning.md#agent-state-becomes-ledgered-event-sourced-and-reusable)
Durable topics: [Event-Sourced Agent Runtime](event-sourced-agent-runtime/event-sourced-agent-runtime.md), [Memory Systems](memory-systems/memory-systems.md), [Multi-Agent Orchestration](multi-agent-orchestration/multi-agent-orchestration.md), [Shared-State Agents](../Strategy/shared-state-agents/shared-state-agents.md)
Core sources: [LedgerAgent](https://arxiv.org/abs/2606.20529), [ESAA-Conversational](https://arxiv.org/abs/2606.23752), [Multi-Agent Transactive Memory](https://arxiv.org/abs/2606.19911), [Governed Shared Memory](https://arxiv.org/abs/2606.24535)
Implementable now:
- define typed task ledgers for high-risk workflows
- check ledger conditions before write, refund, delete, send, deploy, or PR actions
- store visible agent events in append-only JSONL or database tables
- regenerate handoff files and working state from the event log before another agent consumes them
Tools, repos, and methodologies worth exploring:
- SQLite or Postgres event tables, JSONL activity logs, deterministic projection scripts, policy checks over ledger fields, indexed trajectory repositories
Implementability score: 0.78

## Supporting recent AgenticAI context

The 2026-06-26 durable topic [Coding Agent Control Plane](coding-agent-control-plane/coding-agent-control-plane.md) is the newest implementation surface. The 2026-06-24 Strategy deep dive [Memory Authority Control Plane](../Strategy/memory-authority-control-plane/memory-authority-control-plane.md) is the strongest cross-category governance foundation for state and memory work.
