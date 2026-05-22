# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: 2026-05-22 Daily Scan

### Remote MCP auth is the exposed agent-gateway fault line
Summary: A new measurement study reports 7,973 live remote MCP servers, 40.55% exposing tools without authentication, and severe flaws across tested OAuth-enabled servers. MCP discovery is not an authorization boundary.

Analysis: [sovereignty analysis](2026-05-22/sovereignty.md#remote-mcp-authentication-is-failing-at-the-client-registration-boundary)
Durable topic: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md)
Core source: [A First Measurement Study on Authentication Security in Real-World Remote MCP Servers](https://arxiv.org/abs/2605.22333)
Implementable now:
- require authentication on every non-public remote MCP server;
- disable or tightly gate dynamic client registration;
- enforce scoped OAuth/OIDC, PKCE, redirect pinning, token rotation, and audit logs;
- test remote MCP servers for unauthenticated tools, redirect manipulation, token leakage, and overbroad scopes;
- place remote MCP access behind an agent gateway with discovery, authorization, denial, approval, and effect logs.
Tools, repos, and methodologies worth exploring:
- OAuth 2.1/OIDC conformance tests, OPA/Cedar, MCP Inspector, Microsoft Agent Governance Toolkit, Cloudflare Access/AI Gateway patterns, shadow-MCP discovery scans
Supporting source: [Measuring Security Without Fooling Ourselves](https://arxiv.org/abs/2605.22568)
Implementability score: 0.82

## Previous structured update

The prior strategy scan for 2026-05-20 focused on managed-agent sandboxes and the split between model-provider “brain” and operator-controlled execution “hands”: [2026-05-20 sovereignty](2026-05-20/sovereignty.md).
