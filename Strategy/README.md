# Strategy

Governance analysis for identity, authority, execution control, evidence provenance, gateways, containment, and sovereignty.

## Latest Structured Update: 2026-10-19 Daily Scan

### Discovery must not expand authority

Summary: Dynamic tool recommendation should run only after principal and gateway policy produce the eligible catalog, with authorization checked again at execution.

Analysis: [discovery must not expand authority](2026-10-19/sovereignty.md#discovery-must-not-expand-authority)

Core source: [Tool Recommendation for Multi-Step Agents v1](https://arxiv.org/abs/2610.23707v1)

Implementable now:
- compile eligible tools from principal, tenant, agent, service, and tool policy;
- rank only inside that scope;
- keep credentials outside model context;
- bind every effect receipt to principal, tool version, policy, and result.

Implementability score: 0.82

### Relevant memory does not authorize interruption

Summary: Retrieval creates candidate evidence; a separate runtime policy must decide whether the assistant may consume human attention now.

Analysis: [relevant memory does not authorize interruption](2026-10-19/sovereignty.md#relevant-memory-does-not-authorize-interruption)

Core source: [ProPerAgent v1](https://arxiv.org/abs/2610.22671v1)

Implementable now:
- require a current trigger and source-linked memory;
- grade silence outside approved windows;
- impose cooldown, deduplication, and attention budgets;
- separate notification authority from write authority.

Implementability score: 0.45

## Current implication

Recommendation and retrieval are evidence operations. They become authority only through explicit runtime policy, current identity, bounded scope, and an effect receipt.
