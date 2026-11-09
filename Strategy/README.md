# Strategy

Control-plane research for authority, identity, provenance, gateways, approvals, privacy, and sovereign infrastructure.

## Latest structured update: 2026-11-09

### Make review provenance a release input

Summary: GitHub now exposes Copilot code-review policy, attribution, effort, and reported skills, MCP servers, and custom instructions through REST and GraphQL APIs. This makes review configuration a queryable release-control surface.

Analysis: [Daily strategy](2026-11-09/sovereignty.md#1-make-review-provenance-a-release-input)

Core source: [GitHub changelog](https://github.blog/changelog/2026-11-06-copilot-code-review-api-management-and-review-overview-updates/)

Implementable now:
- API inventory of review settings by policy scope
- source-SHA-bound review receipts
- retained attribution, effort, skills, MCP servers, and instructions
- independent effect checks for consequential releases

Implementability score: 0.91

## Current strategic model

1. Evidence informs decisions but does not grant authority.
2. Platform policy and reported context belong in the review receipt.
3. Reported provenance is useful but still needs independent effect evidence.
4. Signed transit cannot repair incomplete extraction.
5. Receipts prove what changed.
6. Privacy scope follows traces and downstream propagation.

## Browse

- [Latest roundup](../roundups/2026-11-09.md)
- [Latest dated strategy](2026-11-09/sovereignty.md)
- [Friday synthesis](2026-11-06/sovereignty.md)
- [Evidence provenance control plane](evidence-provenance-control-plane/evidence-provenance-control-plane.md)
- [Effect-bound skill execution](effect-bound-skill-execution/effect-bound-skill-execution.md)
- [Agent execution control plane](agent-execution-control-plane/agent-execution-control-plane.md)
- [Context-to-execution integrity](context-to-execution-integrity/context-to-execution-integrity.md)
- [Memory authority control plane](memory-authority-control-plane/memory-authority-control-plane.md)
- [Runtime governance](runtime-governance/runtime-governance.md)
- [Untrusted data boundaries](untrusted-data-boundaries/untrusted-data-boundaries.md)
