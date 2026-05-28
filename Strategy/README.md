# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: 2026-05-28 Daily Scan

### Tool artifacts need validation-carrying governance before MCP exposure
Summary: Tool Forge treats tools as governed capsules with intent, capability contracts, tests, runtime validation evidence, dependency policy, credential bindings, lifecycle state, and routing metadata. The strategic point is admission control: generated code should not become an MCP capability without proof and scope.

Analysis: [daily sovereignty analysis](2026-05-28/sovereignty.md#tool-artifacts-need-validation-carrying-governance-before-mcp-exposure)
Durable topic: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md)
Core sources: [Tool Forge paper](https://arxiv.org/abs/2605.28000), [nextmoca/tool-forge](https://github.com/nextmoca/tool-forge)
Implementable now:
- require tool manifests, tests, dependency policy, sandbox validation, and lifecycle states;
- bind credentials at the gateway instead of inside model-written code;
- expose intent-scoped tool sessions instead of full schema catalogs.
Tools, repos, and methodologies worth exploring:
- Tool Forge, MCP routers/proxies, Open Policy Agent, Cedar, sandbox validation, manifest signing, dependency pinning, OpenTelemetry route traces
Implementability score: 0.74

## Previous structured update

The prior Strategy daily scan for 2026-05-27 focused on data-flow capability budgets and lightweight process sandboxing: [2026-05-27 sovereignty](2026-05-27/sovereignty.md).
