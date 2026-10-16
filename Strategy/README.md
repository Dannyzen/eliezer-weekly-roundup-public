# Strategy

Governance analysis for identity, authority, execution control, evidence provenance, gateways, containment, and sovereignty.

## Latest Structured Update: 2026-10-16 Daily Scan

### Bind approval to the exact stored effect

Summary: Agent Step-Up shows that an approval is meaningful only when a compromised agent cannot produce it and when the approval names the exact effect that will execute.

Analysis: [approve a canonical effect, then execute the stored call](2026-10-16/sovereignty.md#approve-a-canonical-effect-then-execute-the-stored-call)

Core sources: [paper v1](https://arxiv.org/abs/2610.21063v1), [Agent Step-Up](https://github.com/Sports-Vision-Inc/agent-step-up)

Implementable now:
- canonicalize tool, target, and arguments outside the model;
- render approval from the stored call;
- bind a passkey to the effect digest;
- execute once and retain a verifiable receipt.

Implementability score: 0.72

### Preserve evidence class before correlating execution

Summary: ExecWeave keeps framework events and OS-observed process, file, and network activity distinct, then labels every cross-layer bridge as observed, inferred, or causal.

Analysis: [keep semantic and OS evidence separate until attribution is justified](2026-10-16/sovereignty.md#keep-semantic-and-os-evidence-separate-until-attribution-is-justified)

Core sources: [paper v1](https://arxiv.org/abs/2610.21146v1), [ExecWeave](https://github.com/Irish-kw/ExecWeave)

Implementable now:
- preserve separate evidence planes;
- attach support IDs and confidence to derived relations;
- abstain on ambiguity or missing observations;
- propagate stable request and process identities where possible.

Implementability score: 0.70

## Current implication

A user-facing narrative can explain an action. Authority comes from a canonical effect release, and accountability comes from source-typed evidence tied to the realized outcome.
