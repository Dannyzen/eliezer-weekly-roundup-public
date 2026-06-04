# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: 2026-06-04 Daily Scan

### MCP descriptions are not contracts unless the gateway checks behavior
Summary: Real MCP servers can have inconsistencies between natural-language tool descriptions and implementation behavior. Since LLMs select tools from descriptions, gateways need behavior evidence before treating a server description as authority.

Analysis: [daily sovereignty analysis](2026-06-04/sovereignty.md#mcp-descriptions-are-not-contracts-unless-the-gateway-checks-behavior)
Durable topic: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md#june-4-update-mcp-descriptions-need-behavior-consistency-checks)
Core source: [Description-Code Inconsistency in Real-world MCP Servers](https://arxiv.org/abs/2606.04769)
Implementable now:
- require MCP manifests with owner, source, version, schemas, side-effect classes, and data classes;
- run description-code consistency tests before production admission;
- deny tools whose descriptions omit mutation, external observation, credential use, or broad data access.
Tools, repos, and methodologies worth exploring:
- MCP gateway registry, schema diffing, static source inspection, dynamic canary probes, OPA/Cedar, taint tests, OpenTelemetry tool-call spans
Implementability score: 0.82

### Budget, workflow, and sandbox controls are becoming runtime contracts
Summary: Token Budgets, Microsoft Agent Framework, AWS Step Functions AgentCore reasoning steps, and GitHub Copilot sandboxes show the same enterprise direction: agents become budgeted workflow nodes and isolated workers with identity, state, observability, policy, and release discipline.

Analysis: [daily sovereignty analysis](2026-06-04/sovereignty.md#budget-workflow-and-sandbox-controls-are-becoming-runtime-contracts)
Durable topic: [Runtime Governance](runtime-governance/runtime-governance.md#june-4-update-budget-and-workflow-controls-are-becoming-runtime-artifacts)
Core sources: [Token Budgets](https://arxiv.org/abs/2606.04056), [Microsoft Agent Framework at BUILD 2026](https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-at-build-2026-announce/), [AWS Step Functions AgentCore reasoning step](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-step-functions-agentcore/), [GitHub Copilot sandboxes](https://github.blog/changelog/2026-06-02-cloud-and-local-sandboxes-for-github-copilot-now-in-public-preview/)
Implementable now:
- define budget authority per workflow, agent, child task, model route, tool, and retry loop;
- wrap high-risk agent work in workflow states with contracts, retry policy, timeout, and approval boundaries;
- run tool execution inside local or cloud sandboxes with filesystem, network, and credential policies.
Tools, repos, and methodologies worth exploring:
- budget leases, spend ledgers, AWS Step Functions, Amazon Bedrock AgentCore, Microsoft Agent Framework, GitHub Copilot sandboxes, OpenTelemetry, CI release gates
Implementability score: 0.72

## Previous structured update

The prior daily scan and deep dive for 2026-06-03 focused on gateway-owned MCP access as the enterprise data plane: [2026-06-03 roundup](../roundups/2026-06-03.md).
