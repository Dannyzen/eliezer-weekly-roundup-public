# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: 2026-05-31 Daily Scan

### MCP auth hardening is moving into the official SDK
Summary: `modelcontextprotocol/python-sdk` v1.27.2 adds subject/claims to access tokens, binds transport sessions to authenticated principals, and scopes experimental tasks to the creating session. That turns MCP security from guidance into runtime identity plumbing.

Analysis: [daily sovereignty analysis](2026-05-31/sovereignty.md#mcp-auth-hardening-is-moving-into-the-official-sdk)
Durable topic: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md)
Core sources: [MCP Python SDK v1.27.2 release](https://github.com/modelcontextprotocol/python-sdk/releases/tag/v1.27.2), [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
Implementable now:
- bind every MCP transport session to an authenticated principal;
- log subject, claims, client, server, session ID, and task origin;
- scope async/background tasks to the creating session unless policy delegates authority;
- test cross-session access and task-resume failure cases.
Tools, repos, and methodologies worth exploring:
- official MCP Python SDK, OAuth/OIDC subject and claims, MCP gateways, MCP Inspector, OPA/Cedar, OpenTelemetry, per-session task ledgers, token-scope audits
Implementability score: 0.90

## Previous structured update

The prior daily scan for 2026-05-30 focused on NSA MCP security guidance, batch-invariant inference, and structured MCP knowledge tools: [2026-05-30 roundup](../roundups/2026-05-30.md).
