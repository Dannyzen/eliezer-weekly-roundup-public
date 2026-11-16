# Strategy

Control-plane research for authority, identity, provenance, gateways, approvals, privacy, and sovereign infrastructure.

## Latest structured update: 2026-11-16

### Verify the plan and enforce every effect

Summary: Soteria verifies tool contracts, progress, and policy compliance before execution, then uses the verified plan as a recovery guide behind runtime enforcement.

Analysis: [Daily strategy](2026-11-16/sovereignty.md#1-verify-the-plan-and-enforce-every-effect)

Core source: [Soteria v1](https://arxiv.org/abs/2611.17880v1)

Implementable now:
- formal tool contracts and sequence policies
- reusable verified sub-plans
- pre-execution verification
- runtime monitoring and recovery receipts

Implementability score: 0.68

### Make forgetting follow memory lineage

Summary: LinEra binds memory encryption to the full derivation graph so one source-key puncture makes every descendant memory unreadable.

Analysis: [Daily strategy](2026-11-16/sovereignty.md#2-make-forgetting-follow-the-memory-derivation-graph)

Core source: [LinEra paper v1](https://arxiv.org/abs/2611.18133v1)

Implementable now:
- complete parent capture at memory write time
- lineage-bound keys
- small-context memory writers
- post-erasure re-derivation from surviving sources

Implementability score: 0.58

## Current strategic model

1. Verify action sequences before side effects.
2. Enforce every call against the same runtime specifications.
3. Treat blocked calls as recovery events, not dead ends.
4. Capture derivation lineage when memory is written.
5. Apply forgetting to the lineage closure and prove the result.

## Browse

- [Daily roundup](../roundups/2026-11-16.md)
- [Daily strategy](2026-11-16/sovereignty.md)
- [Runtime governance](runtime-governance/runtime-governance.md)
- [Memory authority control plane](memory-authority-control-plane/memory-authority-control-plane.md)
- [Agent execution control plane](agent-execution-control-plane/agent-execution-control-plane.md)
