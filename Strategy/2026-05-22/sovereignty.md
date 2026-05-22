# Strategy Daily Analysis: 2026-05-22

Today’s strategy signal is narrow and operational: remote MCP is already large enough that authentication failures are no longer theoretical.

## Remote MCP authentication is failing at the client-registration boundary

*A First Measurement Study on Authentication Security in Real-World Remote MCP Servers* reports 7,973 live remote MCP servers. It finds that 40.55% expose tools without authentication. Among 119 OAuth-enabled servers tested in depth, the paper reports at least one flaw in every server, with dynamic client registration flaws affecting 96.6% of that sample and 9 CVE IDs assigned after disclosure.

Why it matters: MCP is becoming the default tool boundary for agents, but remote MCP changes the threat model. The client is often an agent runtime, not a normal web app. OAuth dynamic client registration, delegated authorization, open client environments, and tool execution create a different security boundary from ordinary SaaS login. If that boundary is weak, an agent’s tool surface becomes a remote account-takeover or unauthorized-action surface.

How it fits into the strategy stack: this belongs in agent gateway governance. The strategic posture should not be “connect agents to every remote MCP endpoint.” It should be “treat every remote MCP server as an untrusted integration until identity, scopes, redirect behavior, dynamic registration, token storage, and audit evidence are proven.” MCP discovery is not an auth control. OAuth support is not enough if dynamic registration and redirect validation are loose.

Implementable now:
- require authentication on every non-public MCP server;
- disable or tightly gate dynamic client registration unless there is a tested operational need;
- use OIDC/OAuth scopes that are tool- and resource-specific, not broad service-account tokens;
- pin allowed redirect URIs and client metadata for trusted clients;
- test remote MCP servers for unauthenticated tools, weak dynamic registration, redirect manipulation, missing state/PKCE, token leakage, and overbroad scopes;
- put remote MCP access behind an agent gateway that logs discovery, enabled tools, auth decisions, denied calls, approvals, and final tool effects;
- use governance/tooling projects as references, but verify their controls before placing them in a privileged path.

Tools, repositories, and methodologies worth exploring:
- OAuth 2.1/OIDC conformance tests, PKCE, scoped bearer-token rotation, OPA/Cedar policies, MCP Inspector, Microsoft Agent Governance Toolkit, Cloudflare Access/AI Gateway patterns, gateway-level audit logs, shadow-MCP discovery scans.

Implementability score: 0.82

Core source: [A First Measurement Study on Authentication Security in Real-World Remote MCP Servers](https://arxiv.org/abs/2605.22333)
Supporting sources:
- [Measuring Security Without Fooling Ourselves](https://arxiv.org/abs/2605.22568)
- [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit)
- [modelcontextprotocol/inspector](https://github.com/modelcontextprotocol/inspector)
