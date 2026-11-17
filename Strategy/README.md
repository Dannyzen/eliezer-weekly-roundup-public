# Strategy

Control-plane research for authority, identity, provenance, gateways, approvals, privacy, and sovereign infrastructure.

## Latest structured update: 2026-11-17

### Govern customization origin and runtime separately

Summary: GitHub now exposes enterprise provenance controls for skills, agents, hooks, MCP servers, and executable extensions, while runtime permissions and sandboxing remain a separate enforcement layer.

Analysis: [Daily strategy](2026-11-17/sovereignty.md#1-govern-customization-origin-and-runtime-separately)

Core source: [GitHub customization controls](https://github.blog/changelog/2026-11-16-control-where-github-copilot-customizations-come-from/)

Implementable now:
- plugin-only policy for high-impact customizations
- known-marketplace restrictions
- explicit harness migration tests
- separately configured permissions and sandbox policy
- provenance, approval, and effect receipts

Implementability score: 0.88

## Current strategic model

1. Inventory every customization source and loaded capability.
2. Admit high-impact extensions only through approved plugins or managed settings.
3. Restrict eligible marketplaces and pin plugin policy.
4. Enforce permissions and sandbox boundaries in the runtime.
5. Verify blocked sources and effects with fail-closed tests.

## Browse

- [Daily roundup](../roundups/2026-11-17.md)
- [Daily strategy](2026-11-17/sovereignty.md)
- [Agent gateway governance](agent-gateway-governance/agent-gateway-governance.md)
- [Runtime governance](runtime-governance/runtime-governance.md)
- [Agent execution control plane](agent-execution-control-plane/agent-execution-control-plane.md)
