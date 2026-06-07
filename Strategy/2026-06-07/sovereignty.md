# Strategy Daily Scan: 2026-06-07

Today’s strategy signal is practical: agent tool governance is becoming an admin-managed client and CI surface, not only a gateway diagram.

## Findings

### Agent toolchains are becoming governed client and CI surfaces

GitHub’s enterprise-managed plugins preview for VS Code and Copilot CLI is a clean strategic signal. Enterprise administrators can define plugin marketplaces in `.github-private/.github/copilot/settings.json`, auto-install plugins for licensed users, and keep hooks and MCP configurations always enabled across the enterprise. The important point is not the JSON file itself. It is that agent skills, plugins, hooks, and MCP configuration are becoming centrally managed developer-environment policy.

FastMCP’s June 5 and June 6 releases show the lower-level MCP infrastructure version of the same pattern. v3.4.1 floors Starlette to avoid installs resolving to a CVE-affected version and makes OAuthProxy refresh-token cache misses visible instead of silent. v3.4.2 restores JWT compatibility for providers with private non-critical JWS headers while preserving critical-header rejection. These are not flashy agent features. They are the kind of dependency, OAuth, and JWT hygiene that makes MCP infrastructure operable.

mcp-guard is small, but it is directionally useful because it moves MCP prompt-injection and tool-poisoning checks into build time for C# MCP servers. The release describes Roslyn diagnostics and a CI gate over tool descriptions, hidden Unicode, exfiltration phrasing, capability mismatch, embedded markup, cross-tool shadowing, and description-integrity fingerprints.

Why it matters: the agent tool surface is now a supply chain. It includes client defaults, enterprise settings, MCP server dependencies, auth behavior, tool descriptions, hooks, and CI gates. A serious organization should not let every developer or agent process assemble that surface ad hoc.

How it fits into strategy: this belongs in agent gateway governance. The gateway still mediates runtime authority, but the managed-client and CI layers decide what capabilities reach the user and agent before runtime. Sovereignty means owning those defaults.

Implementable tools, repos, and methodologies:
- enterprise-managed Copilot plugin settings for approved plugins, hooks, MCP configs, and marketplaces;
- MCP server template dependency floors and auth regression tests;
- JWT/OIDC compatibility tests for the identity providers actually used by the organization;
- static checks over MCP tool names, descriptions, schemas, hidden Unicode, and exfiltration language;
- description fingerprinting and review gates before MCP server release;
- gateway logs that record client policy version, server version, tool-description hash, and selected tool.

Implementability score: 0.87

Core sources:
- GitHub enterprise-managed plugins in VS Code: https://github.blog/changelog/2026-06-05-enterprise-managed-plugins-in-vs-code-in-public-preview/
- FastMCP v3.4.1: https://github.com/PrefectHQ/fastmcp/releases/tag/v3.4.1
- FastMCP v3.4.2: https://github.com/PrefectHQ/fastmcp/releases/tag/v3.4.2
- mcp-guard v1.0.0: https://github.com/diomonogatari/mcp-guard/releases/tag/v1.0.0

## Watchlist, not top findings

LiteLLM v1.88.0 is worth tracking because signed Docker images are a good AI-gateway supply-chain signal. Ollama 0.30 is relevant for local-first GGUF runtime operations. Neither beat the managed-plugin plus MCP-hygiene finding today because the latter is closer to Danny’s governance layer: who defines what an agent can see, install, and call.

## Scan quality note

GitHub changelog pages, GitHub release metadata, and repository metadata were verified through primary pages or the GitHub API. No external repository was cloned, installed, built, downloaded, or executed.
