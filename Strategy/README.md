# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Week ending 2026-06-05

### The agent gateway is becoming the identity-bound MCP data plane
Summary: MCP is moving from connector convenience into infrastructure for storage, SaaS, browser security, cloud workflows, and local tools. The gateway is where identity, delegated authority, scoped discovery, credentials, data projection, approvals, and audit evidence have to meet.

Analysis: [weekly sovereignty analysis](2026-06-05/sovereignty.md#the-agent-gateway-is-becoming-the-identity-bound-mcp-data-plane)
Durable topic: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md)
Core sources: [NSA MCP security release](https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/4496698/nsa-releases-security-design-considerations-for-ai-driven-automation-leveraging/), [MCP Python SDK v1.27.2](https://github.com/modelcontextprotocol/python-sdk/releases/tag/v1.27.2), [GCS MCP server](https://cloud.google.com/blog/topics/developers-practitioners/build-ai-agents-faster-with-gcs-google-cloud-storage-mcp-server/), [AgentCore Gateway MCP support](https://aws.amazon.com/blogs/machine-learning/extending-mcp-support-for-amazon-bedrock-agentcore-gateway-2/), [Overlaying Governance](https://arxiv.org/abs/2606.03518)
Implementable now:
- put MCP servers behind a gateway instead of exposing them directly to clients;
- bind user, agent, client, server, session, workflow, and delegated authority into each request;
- scope tool discovery, project data before disclosure, and record policy evidence.
Tools, repos, and methodologies worth exploring:
- Amazon Bedrock AgentCore Gateway, Google Cloud Storage MCP server, MCP Python SDK, OAuth/OIDC with PKCE, OPA/Cedar, OpenTelemetry gateway spans, permission-laundering canaries
Implementability score: 0.76

### Tool surfaces and runtime contracts are now security boundaries
Summary: MCP description mismatch, WebMCP poisoning, token-budget overruns, workflow engines, and sandboxes all say the same thing: tool metadata and runtime conditions decide what the model believes it can do.

Analysis: [weekly sovereignty analysis](2026-06-05/sovereignty.md#tool-surfaces-and-runtime-contracts-are-now-security-boundaries)
Durable topics: [Runtime Governance](runtime-governance/runtime-governance.md), [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md)
Core sources: [MCP description-code inconsistency](https://arxiv.org/abs/2606.04769), [WebMCP Tool Surface Poisoning](https://arxiv.org/abs/2606.06387), [Token Budgets](https://arxiv.org/abs/2606.04056), [Microsoft Agent Framework](https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-at-build-2026-announce/), [GitHub Copilot sandboxes](https://github.blog/changelog/2026-06-02-cloud-and-local-sandboxes-for-github-copilot-now-in-public-preview/)
Implementable now:
- hash and revalidate tool metadata, origin, version, and registration source;
- freeze or revalidate visible tools at policy checkpoints;
- enforce single-spend budget leases and trace workflow/sandbox contracts.
Tools, repos, and methodologies worth exploring:
- signed tool manifests, metadata hashing, dynamic tool-surface diffing, browser isolation, token-budget ledgers, workflow engines, sandbox attestation, effect validators
Implementability score: 0.81

### Speculative external observation is an effect, not a harmless read
Summary: Ghost tool calls show that external systems can observe sensitive intent before the agent commits a final mutation. A read or exploratory call may already leak the user’s plan.

Analysis: [weekly sovereignty analysis](2026-06-05/sovereignty.md#speculative-external-observation-is-an-effect-not-a-harmless-read)
Durable topic: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md)
Core source: [Ghost Tool Calls](https://arxiv.org/abs/2606.02483v1)
Implementable now:
- classify tools by external observability, not only read/write status;
- redact or project sensitive arguments before exploratory calls;
- require approval before calls that expose private intent to third parties.
Tools, repos, and methodologies worth exploring:
- issue-time policy engines, argument projection, local search mirrors, dry-run APIs, privacy labels for tools, OPA/Cedar policies
Implementability score: 0.60

### Runtime contracts now cover budgets, workflows, sandboxes, and serving conditions
Summary: Production agent governance now includes batch invariance, org-scoped runtime context, token budgets, workflow retries, sandbox identity, hosted-agent versions, and rollback evidence.

Analysis: [weekly sovereignty analysis](2026-06-05/sovereignty.md#runtime-contracts-now-cover-budgets-workflows-sandboxes-and-serving-conditions)
Durable topic: [Runtime Governance](runtime-governance/runtime-governance.md)
Core sources: [MarginGate](https://arxiv.org/abs/2605.30218v1), [Organization-scoped regulated-agent runtime](https://arxiv.org/abs/2605.30604), [NemoClaw](https://github.com/NVIDIA/NemoClaw), [AWS AgentOps](https://aws.amazon.com/blogs/machine-learning/agentops-operationalize-agentic-ai-at-scale-with-amazon-bedrock-agentcore/), [Token Budgets](https://arxiv.org/abs/2606.04056), [GitHub Copilot sandboxes](https://github.blog/changelog/2026-06-02-cloud-and-local-sandboxes-for-github-copilot-now-in-public-preview/)
Implementable now:
- record model, server version, batch conditions, retry policy, budget lease, and sandbox identity as trace metadata;
- cap token, tool, cost, and wall-clock budgets with explicit lease IDs;
- bind sandbox permissions to task, repo, network policy, credentials, and artifact paths.
Tools, repos, and methodologies worth exploring:
- AWS AgentOps, Microsoft Agent Framework, Step Functions AgentCore, GitHub Copilot sandboxes, NemoClaw, budget ledgers, workflow engines, OpenTelemetry, deterministic replay metadata
Implementability score: 0.72

## Previous structured update

The prior Friday synthesis for week ending 2026-05-29 focused on gateways as admission-control and runtime-sovereignty boundaries: [2026-05-29 roundup](../roundups/2026-05-29.md).
