# Strategy

Control-plane research for authority, identity, provenance, gateways, approvals, privacy, and sovereign infrastructure.

## Latest structured update: 2026-11-10

### Govern shared memory as an implicit message bus

Summary: agents coordinated through a shared writable store without being told that other agents existed. One workspace-recheck instruction moved a tested model from 1 of 50 to 50 of 50 coordinated worlds in both implementations.

Analysis: [Daily strategy](2026-11-10/sovereignty.md#1-govern-shared-memory-as-an-implicit-message-bus)

Core sources: [paper v1](https://arxiv.org/abs/2611.12412v1), [replication package](https://doi.org/10.5281/zenodo.23965306)

Implementable now:
- private namespaces by default
- explicit shared audiences
- attributed and supersedable writes
- cross-agent-read telemetry
- shared, private, and no-store controls

Implementability score: 0.88

## Current strategic model

1. Evidence informs decisions but does not grant authority.
2. Shared state is a communication channel and needs an audience contract.
3. Private and shared namespaces require different permissions.
4. Cross-agent reads should be retained as communication events.
5. Receipts bind source, author, policy, and resulting effect.
6. Privacy scope follows traces and downstream propagation.

## Browse

- [Latest roundup](../roundups/2026-11-10.md)
- [Latest dated strategy](2026-11-10/sovereignty.md)
- [Friday synthesis](2026-11-06/sovereignty.md)
- [Evidence provenance control plane](evidence-provenance-control-plane/evidence-provenance-control-plane.md)
- [Effect-bound skill execution](effect-bound-skill-execution/effect-bound-skill-execution.md)
- [Agent execution control plane](agent-execution-control-plane/agent-execution-control-plane.md)
- [Context-to-execution integrity](context-to-execution-integrity/context-to-execution-integrity.md)
- [Memory authority control plane](memory-authority-control-plane/memory-authority-control-plane.md)
- [Runtime governance](runtime-governance/runtime-governance.md)
- [Untrusted data boundaries](untrusted-data-boundaries/untrusted-data-boundaries.md)
