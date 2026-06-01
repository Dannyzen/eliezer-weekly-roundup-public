# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: 2026-06-01 Daily Scan

### Organization-scoped runtime is the regulated-agent shape
Summary: A new SOC/runtime architecture paper argues that regulated agents need a typed organization/security context enforced across retrieval, tool calls, memory, findings, reports, approvals, and audit.

Analysis: [daily sovereignty analysis](2026-06-01/sovereignty.md#organization-scoped-runtime-is-the-regulated-agent-shape)
Durable topic: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md)
Core source: [Organization-Scoped LLM Agent Runtime Architecture](https://arxiv.org/abs/2605.30604)
Implementable now:
- create typed organization/security context for every workflow trigger;
- pass context through retrieval, tools, memory writes, findings, and reports;
- expose SIEM/XDR operations through governed adapters;
- require evidence-linked findings and tiered HITL gates;
- store append-only audit events for context, tools, approvals, and reports.
Tools, repos, and methodologies worth exploring:
- MCP gateways, OPA/Cedar, SIEM/XDR adapters, OpenTelemetry, append-only audit logs, typed Security Context schemas, Temporal/LangGraph state machines
Implementability score: 0.57

### Agent sandboxes are becoming infrastructure policy, not optional wrappers
Summary: NVIDIA’s NemoClaw/OpenShell and DOCA security materials show the market direction for privileged agents: sandboxed execution, routed inference, network policy, runtime detection, data access control, lifecycle management, and trace evidence.

Analysis: [daily sovereignty analysis](2026-06-01/sovereignty.md#sandbox-and-ai-factory-security-are-moving-below-prompt-policy)
Durable topic: [Runtime Governance](runtime-governance/runtime-governance.md)
Core sources: [NVIDIA enterprise agent release](https://nvidianews.nvidia.com/news/enterprise-software-leaders-build-ai-agents-with-nvidia), [NVIDIA NemoClaw](https://github.com/NVIDIA/NemoClaw), [NVIDIA DOCA in-silicon security](https://developer.nvidia.com/blog/advancing-ai-infrastructure-for-agentic-ai-with-nvidia-doca-in-silicon-security/)
Implementable now:
- run privileged agents inside constrained worker/sandbox environments;
- route inference through governed endpoints with model, cost, and data policy;
- enforce network egress policy per workflow;
- log sandbox lifecycle, network decisions, tool calls, and inference routing;
- treat runtime images, skills, and tool adapters as supply-chain artifacts.
Tools, repos, and methodologies worth exploring:
- `NVIDIA/NemoClaw`, OpenShell-style sandboxes, egress policy, MCP gateways, OpenTelemetry, OPA/Cedar, container/network policy, runtime detection
Implementability score: 0.62

## Previous structured update

The prior daily scan for 2026-05-31 focused on MCP Python SDK principal binding and session-scoped task authority: [2026-05-31 roundup](../roundups/2026-05-31.md).
