# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan, 2026-07-12

### LiteLLM makes delegated MCP identity a gateway lifecycle

Summary: LiteLLM v1.92.0 adds MCP OAuth On-Behalf-Of discovery, persisted Dynamic Client Registration, per-server concurrency limits, catalog search, credential hardening, and Google Distributed Cloud Gemini. The gateway is becoming the place where delegated identity, tool discovery, policy, and sovereign routing meet.

Analysis: [daily sovereignty analysis](2026-07-12/sovereignty.md#litellm-v1920-makes-delegated-mcp-identity-a-gateway-feature)
Durable topics: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Local-First Agents](local-first-agents/local-first-agents.md)
Core sources: [LiteLLM v1.92.0 release notes](https://docs.litellm.ai/release_notes/v1.92.0/v1-92-0), [GitHub release](https://github.com/BerriAI/litellm/releases/tag/v1.92.0)
Implementable now:
- stage one remote MCP server behind delegated OAuth
- test discovery, Dynamic Client Registration persistence, refresh, revocation, concurrency, and audit
- filter tool search by authorization before exposing results to the model
Tools, repositories, and methodologies worth exploring:
- `BerriAI/litellm` v1.92.0, OAuth On-Behalf-Of, RFC 9728, RFC 8414, per-server MCP concurrency budgets
Implementability score: 0.82

### Compiled sandbox policy is becoming portable infrastructure

Summary: GitHub Agentic Workflows v0.82.8 makes gVisor and mount policy workflow fields, while surfacing token failures and safe-output completion. The strategic shift is from assumed isolation to a declared execution manifest with durable terminal evidence.

Analysis: [daily sovereignty analysis](2026-07-12/sovereignty.md#compiled-sandbox-policy-is-becoming-portable-infrastructure)
Durable topics: [Agent Sandboxing](agent-sandboxing/agent-sandboxing.md), [Governed Workflow Substrates](governed-workflow-substrates/governed-workflow-substrates.md)
Core source: [GitHub Agentic Workflows v0.82.8](https://github.com/github/gh-aw/releases/tag/v0.82.8)
Implementable now:
- create approved sandbox partials for read-only source and writable scratch
- bind lock state, imports, sandbox runtime, mounts, token outcome, and safe-output type into the run receipt
- fail closed when token checks or terminal output integration fail
Tools, repositories, and methodologies worth exploring:
- `github/gh-aw`, gVisor, compiled lock evidence, safe-output schemas, runner policy checks
Implementability score: 0.72

## Supporting recent Strategy context

The 2026-07-12 scan sharpens the sovereignty thesis: delegated identity should terminate at a governed tool gateway, and the resulting work should execute inside a declared sandbox. Model choice stays replaceable. Identity, containment, and receipts remain the durable control plane.
