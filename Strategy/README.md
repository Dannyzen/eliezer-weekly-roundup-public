# Strategy

This index tracks the most recent structured strategy research. Each finding links to the dated analysis, durable topics, primary sources, practical methods, and an implementability score.

## Latest Structured Update: 2026-09-23

### Treat MCP metadata and outputs as untrusted control inputs

Summary: A2M attacks MCP agents in two places: tool descriptions attract invocation, then adversarial return content redirects reasoning. Authentication and valid schemas do not establish semantic trust.

Analysis: [daily strategy analysis](2026-09-23/sovereignty.md#treat-mcp-metadata-and-tool-outputs-as-untrusted-control-inputs)
Durable deep dive: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md)
Core sources: [paper](https://arxiv.org/abs/2609.26761v1), [public repository](https://github.com/Lilaizhen/A2M)
Tools and methodologies worth exploring now: metadata admission, manifest diffing, result provenance, taint classes, token and retry budgets, least-privilege isolation, adversarial replay fixtures
Implementability score: 0.78

### Standardize lifecycle telemetry with sensitive content off by default

Summary: GitHub Copilot now exports OpenTelemetry traces, metrics, and events through enterprise-managed settings. Prompts, responses, and tool arguments are excluded by default and should remain disabled until a governed investigation needs them.

Analysis: [daily strategy analysis](2026-09-23/sovereignty.md#standardize-agent-telemetry-while-keeping-content-capture-off-by-default)
Durable deep dive: [Agent Fleet Monitoring Control Plane](agent-fleet-monitoring-control-plane/agent-fleet-monitoring-control-plane.md)
Core sources: [release note](https://github.blog/changelog/2026-09-22-opentelemetry-in-the-github-copilot-app), [documentation](https://docs.github.com/en/enterprise-cloud@latest/copilot/concepts/enterprise/opentelemetry)
Tools and methodologies worth exploring now: OTLP collectors, session and tool spans, token metrics, edit-feedback events, content exclusion, retention policy, state-linked incident receipts
Implementability score: 0.92

## Current implication

Govern semantic inputs and observability outputs as data classes with distinct authority, sensitivity, retention, and isolation rules. Standard telemetry helps only when identity and external state remain linked to each session.
