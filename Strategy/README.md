# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: 2026-06-05 Daily Scan

### WebMCP tool-surface poisoning turns tool discovery into a live attack surface
Summary: WebMCP lets websites expose tools directly to agents. That creates a runtime attack surface where scripts can hijack visible tools or frame tool metadata during an active session.

Analysis: [daily sovereignty analysis](2026-06-05/sovereignty.md#webmcp-tool-surface-poisoning-turns-tool-discovery-into-a-live-attack-surface)
Durable topic: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md#june-5-update-webmcp-tool-surfaces-need-origin-bound-lifecycle-controls)
Core source: [WebMCP Tool Surface Poisoning](https://arxiv.org/abs/2606.06387)
Implementable now:
- bind tool identity to origin and version;
- freeze or revalidate visible tools at policy checkpoints;
- hash tool metadata fields such as name, description, readOnlyHint, and inputSchema;
- log registration, mutation, selected call, arguments, and observed effect.
Tools, repos, and methodologies worth exploring:
- MCP gateway registries, WebMCP canary sites, signed tool manifests, metadata hashing, dynamic tool-surface diffing, OPA/Cedar, OpenTelemetry tool-registration spans
Implementability score: 0.80

## Previous structured update

The prior daily scan for 2026-06-04 focused on MCP description-code consistency and runtime contracts for budgets, workflows, and sandboxes: [2026-06-04 roundup](../roundups/2026-06-04.md).
