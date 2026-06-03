# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: 2026-06-03 Deep Dive + Daily Scan

### Gateway-owned MCP access is now the enterprise data plane
Summary: Object storage, browser-security administration, GitHub/cloud-agent configuration, and SaaS APIs are becoming agent-callable through MCP. The winning control point is a gateway that owns identity, scoped discovery, delegated authority, credential custody, data-flow policy, exfiltration checks, and replayable evidence.

Analysis: [Deep Dive Wednesday dated analysis](2026-06-03/sovereignty.md#deep-dive-wednesday-selection-gateway-owned-delegation-and-storage-policy)
Durable topic: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md#deep-dive-wednesday-2026-06-03-gateway-as-identity-bound-mcp-data-plane)
Core sources: [GCS MCP server](https://cloud.google.com/blog/topics/developers-practitioners/build-ai-agents-faster-with-gcs-google-cloud-storage-mcp-server/), [AgentCore Gateway MCP support](https://aws.amazon.com/blogs/machine-learning/extending-mcp-support-for-amazon-bedrock-agentcore-gateway-2/), [AgentCore Gateway auth code flow](https://aws.amazon.com/blogs/machine-learning/building-a-secure-auth-code-flow-setup-using-agentcore-gateway-with-mcp-clients/), [Overlaying Governance](https://arxiv.org/abs/2606.03518)
Implementable now:
- put storage, SaaS, browser-security, GitHub, and enterprise MCP servers behind a gateway;
- bind requests to user, agent, client, server, session, workflow, and delegated authority;
- scope tools by bucket, prefix, data class, action type, workflow, and approval tier;
- log selected tools, denied tools, object paths, argument projections, auth claims, policy IDs, approval artifacts, and final effects;
- test permission laundering, overbroad prefix access, speculative external observation, weak OAuth registration, and missing audit fields.
Tools, repos, and methodologies worth exploring:
- Amazon Bedrock AgentCore Gateway, Google Cloud Storage MCP server, OAuth/OIDC with PKCE, OpenFGA/Zanzibar-style relationship authorization, OPA/Cedar, OpenTelemetry, DLP labels, canary/taint tests, MCP client capability inventory
Implementability score: 0.76

## Previous structured update

The prior daily scan for 2026-06-02 focused on speculative tool-call privacy and versioned AgentOps runtime control planes: [2026-06-02 roundup](../roundups/2026-06-02.md).
