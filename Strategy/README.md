# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: 2026-05-29 Daily Scan

### Chrome Enterprise MCP turns browser-security admin into a governed agent surface
Summary: Google’s Chrome Enterprise Premium MCP server exposes DLP, connector policy, browser telemetry, license management, and investigation workflows to MCP-compatible agents. This is privileged browser-security administration, so gateway policy and traceability are mandatory.

Analysis: [daily sovereignty analysis](2026-05-29/sovereignty.md#chrome-enterprise-mcp-turns-browser-security-admin-into-a-governed-agent-surface)
Durable topic: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md)
Core sources: [Google security post](https://blog.google/security/bringing-ai-agents-to-chrome-enterprise-security-management/), [google/chrome-enterprise-premium-mcp](https://github.com/google/chrome-enterprise-premium-mcp), [Pocket CEP example](https://github.com/google/ChromeBrowserEnterprise/tree/main/mcp-examples/pocket-cep)
Implementable now:
- put privileged MCP servers behind identity, OAuth-scope, and approval gates;
- split diagnosis from mutation tools;
- trace before/after policy changes and label agent-created policies for rollback.
Tools, repos, and methodologies worth exploring:
- Chrome Enterprise Premium MCP, Pocket CEP, MCP gateways, OPA/Cedar, approval artifacts, OpenTelemetry, DLP rollback tests
Implementability score: 0.68

### Sabotage auditing needs deployment scenarios, not abstract safety vibes
Summary: Gram evaluates sabotage propensity across simulated coding and research deployments, then uses investigator-agent experiments to identify drivers of misbehavior. Governance needs scenario-shaped traces, not generic refusal screenshots.

Analysis: [daily sovereignty analysis](2026-05-29/sovereignty.md#sabotage-auditing-needs-deployment-scenarios-not-abstract-safety-vibes)
Durable topic: [Runtime Governance](runtime-governance/runtime-governance.md)
Core source: [Gram paper](https://arxiv.org/abs/2605.30322)
Implementable now:
- create sabotage and overeagerness fixtures for high-trust agents;
- score concealment, evidence manipulation, policy bypass, and unjustified goal pursuit;
- run ablations on realism, tool scope, objective wording, and approval gates.
Tools, repos, and methodologies worth exploring:
- DTap-style deployment fixtures, RAMPART/pytest-style adversarial tests, red-team scenario cards, LangSmith/Langfuse trajectory review, OpenTelemetry traces
Implementability score: 0.54

## Previous structured update

The prior Strategy daily scan for 2026-05-28 focused on validation-carrying tool governance before MCP exposure: [2026-05-28 sovereignty](2026-05-28/sovereignty.md).
