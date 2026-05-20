# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: 2026-05-19 Daily Scan

### Managed coding agents are becoming an audited control plane
Summary: GitHub’s latest Copilot cloud-agent releases expose the operational layer around enterprise coding agents: repo config audit APIs, one-click Actions fixes, and cheaper model choices for simpler delegated work. OpenAI and Dell’s Codex partnership points in the same direction for hybrid/on-prem placement near governed enterprise data.

Analysis: [sovereignty analysis](2026-05-19/sovereignty.md#managed-coding-agents-are-moving-into-the-enterprise-control-plane)
Durable topic: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md)
Core source: [Audit repository Copilot cloud agent configuration via the REST API](https://github.blog/changelog/2026-05-18-audit-repository-copilot-cloud-agent-configuration-via-the-rest-api)
Implementable now:
- inventory Copilot cloud-agent configuration across repositories;
- audit MCP servers, enabled tools, workflow policy, and firewall configuration;
- route simple CI/lint fixes to cheaper models while reserving stronger models for ambiguous work;
- require trace-linked review for auto-generated fixes before merge.
Tools, repos, and methodologies worth exploring:
- GitHub Copilot cloud agent, GitHub REST API, GitHub Actions, MCP config inventory, OPA/Cedar policy checks, OpenTelemetry traces, branch protection, review gates, model-routing policy
Supporting sources:
- [One-click fixes for failing Actions with Copilot cloud agent](https://github.blog/changelog/2026-05-18-one-click-fixes-for-failing-actions-with-copilot-cloud-agent)
- [Copilot cloud agent: Fast, cost-efficient models for simple tasks](https://github.blog/changelog/2026-05-18-copilot-cloud-agent-fast-cost-efficient-models-for-simple-tasks)
- [OpenAI and Dell Technologies partner to bring Codex to hybrid and on-premises enterprise environments](https://openai.com/index/dell-codex-enterprise-partnership)
Implementability score: 0.78

## Previous structured update

The prior daily scan for 2026-05-18 focused on OpenAPI/MCP agent-readiness gates and sleeper memory poisoning defenses: [2026-05-18 sovereignty](2026-05-18/sovereignty.md).
