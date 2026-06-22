# AgenticAI

This index tracks the most recent structured update. Each finding includes a short human-readable summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan, 2026-06-22

### Service-language agent runtimes are becoming real infrastructure

Summary: Google ADK and tRPC-Agent-Go show agent frameworks moving into normal service-language runtimes with graph workflows, sessions, memory, tool calling, evaluation, and observability.

Analysis: [daily reasoning analysis](2026-06-22/reasoning.md#service-language-agent-runtimes-are-becoming-real-infrastructure)
Durable topics: [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md), [Agent Serving Runtime](agent-serving-runtime/agent-serving-runtime.md), [Enterprise MCP Orchestration](enterprise-mcp-orchestration/enterprise-mcp-orchestration.md)
Core sources: [ADK docs](https://adk.dev/), [google/adk-python](https://github.com/google/adk-python), [google/adk-go](https://github.com/google/adk-go), [google/adk-java](https://github.com/google/adk-java), [tRPC-Agent-Go](https://github.com/trpc-group/trpc-agent-go)
Implementable now:
- prototype one internal workflow in ADK or tRPC-Agent-Go
- require workflow node, agent role, tool call, session, memory, retry, and cancellation trace fields
- keep graph topology under code review instead of letting prompts invent orchestration at runtime
Tools, repos, and methodologies worth exploring:
- Google ADK, tRPC-Agent-Go, OpenTelemetry spans, graph workflow replay fixtures, A2A and MCP adapters after local state and traces are explicit
Implementability score: 0.82

### UnifAI makes enterprise multi-agent orchestration blueprint-driven

Summary: UnifAI packages enterprise RAG, pluggable agents, YAML or visual blueprints, A2A/MCP protocol support, local LangGraph execution, and distributed Temporal execution. The core pattern is reviewable workflow topology.

Analysis: [daily reasoning analysis](2026-06-22/reasoning.md#unifai-shows-enterprise-multi-agent-orchestration-is-becoming-blueprint-driven)
Durable topics: [Multi-Agent Orchestration](multi-agent-orchestration/multi-agent-orchestration.md), [Enterprise MCP Orchestration](enterprise-mcp-orchestration/enterprise-mcp-orchestration.md), [Agentic Search and Retrieval](agentic-search/agentic-search.md)
Core source: [redhat-community-ai-tools/UnifAI](https://github.com/redhat-community-ai-tools/UnifAI)
Implementable now:
- represent agent teams as YAML or graph blueprints with explicit roles, retrievers, tools, protocols, and execution backend
- require blueprint diffs and trace IDs before deployment
- separate local graph execution from distributed durable workflow execution
Tools, repos, and methodologies worth exploring:
- UnifAI, LangGraph, Temporal, enterprise vector stores, approved Slack/Jira/document/wiki connectors, MCP/A2A gateway policy
Implementability score: 0.70

### AssetOpsBench makes domain agent eval concrete enough to copy

Summary: IBM's AssetOpsBench gives a domain benchmark shape for industrial agents: realistic scenarios, domain-specific MCP servers, specialist agents, orchestration blueprints, trajectory replay, and failure taxonomy analysis.

Analysis: [daily reasoning analysis](2026-06-22/reasoning.md#assetopsbench-makes-domain-agent-eval-concrete-enough-to-copy)
Durable topics: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md), [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md), [Multi-Agent Orchestration](multi-agent-orchestration/multi-agent-orchestration.md)
Core sources: [IBM/AssetOpsBench](https://github.com/IBM/AssetOpsBench), [IBM Research writeup](https://research.ibm.com/blog/asset-ops-benchmark), [AssetOpsBench paper](https://arxiv.org/abs/2506.03828v1), [Hugging Face article](https://huggingface.co/blog/ibm-research/assetopsbench-playground-on-hugging-face)
Implementable now:
- create a 20 to 50 scenario benchmark for one real operating domain
- expose domain tools as MCP-style servers or typed adapters
- score intermediate steps, tool parameters, specialist handoffs, final decisions, and work-product quality separately
Tools, repos, and methodologies worth exploring:
- AssetOpsBench, Agent Trajectory Explorer-style replay, domain-specific MCP servers, trajectory failure taxonomies, scenario suites from real workflows
Implementability score: 0.64
