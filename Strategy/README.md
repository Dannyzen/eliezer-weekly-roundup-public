# Strategy

Control-plane research for authority, identity, provenance, gateways, approvals, privacy, and sovereign infrastructure.

## Latest structured update: 2026-11-08

### Define prompt injection by source authority

Summary: untrusted content can preserve the user's task while changing a rule, state fact, action value, or observation meaning. Defenses focused on explicit instruction override can therefore miss unauthorized effects performed through expected tools.

Analysis: [Daily strategy](2026-11-08/sovereignty.md#1-define-prompt-injection-by-source-authority)

Core sources: [paper](https://arxiv.org/abs/2611.07640v1), [public benchmark repository](https://github.com/amazon-science/task-tampering-prompt-injection)

Implementable now:
- per-value source-authority rules
- critical-argument provenance
- state, rule, consequence, and observation-tampering fixtures
- separate legitimate-completion and unauthorized-effect scores

Implementability score: 0.82

### Sign requirements after source-bound extraction

Summary: signed requirement manifests sharply reduced unsafe multi-agent commits, but every remaining unsafe decision in the oracle comparison came from extraction errors before signing. Transit integrity starts after the real trust boundary.

Analysis: [Daily strategy](2026-11-08/sovereignty.md#2-sign-requirements-after-source-bound-extraction)

Core source: [Signed but Not Safe](https://arxiv.org/abs/2611.07483v1)

Implementable now:
- verbatim requirement evidence plus typed predicates
- canonical manifests signed outside model access
- deterministic final-effect checks
- separate pre-signing extraction audits

Implementability score: 0.76

## Current strategic model

1. Evidence informs decisions but does not grant authority.
2. Authority belongs to sources and the decision variables they govern.
3. Signed transit cannot repair incomplete extraction.
4. Effect-bound tickets narrow host grants.
5. Receipts prove what changed.
6. Privacy scope follows traces and downstream propagation.

## Browse

- [Latest roundup](../roundups/2026-11-08.md)
- [Latest dated strategy](2026-11-08/sovereignty.md)
- [Friday synthesis](2026-11-06/sovereignty.md)
- [Effect-bound skill execution](effect-bound-skill-execution/effect-bound-skill-execution.md)
- [Evidence provenance control plane](evidence-provenance-control-plane/evidence-provenance-control-plane.md)
- [Agent execution control plane](agent-execution-control-plane/agent-execution-control-plane.md)
- [Context-to-execution integrity](context-to-execution-integrity/context-to-execution-integrity.md)
- [Memory authority control plane](memory-authority-control-plane/memory-authority-control-plane.md)
- [Runtime governance](runtime-governance/runtime-governance.md)
- [Untrusted data boundaries](untrusted-data-boundaries/untrusted-data-boundaries.md)
