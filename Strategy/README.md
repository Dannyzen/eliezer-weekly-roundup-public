# Strategy

Governance analysis for identity, authority, execution control, evidence provenance, gateways, containment, and sovereignty.

## Latest Structured Update: 2026-10-20 Daily Scan

### Bind outbound connections to one-time signed verdicts

Summary: Hold each agent connection before packets leave, then release only on a signed, unexpired, single-use verdict bound to that socket and destination.

Analysis: [bind every outbound connection to a one-time signed verdict](2026-10-20/sovereignty.md#bind-every-outbound-connection-to-a-one-time-signed-verdict)

Core sources: [Connection Escrow v1](https://arxiv.org/abs/2610.26501v1), [repository](https://github.com/45h0kg/benign-attach-gateway)

Implementable now:
- hold high-risk pod egress at the kernel boundary;
- bind verdicts to socket, destination, principal, expiry, and single use;
- isolate verifier keys and fail closed;
- preserve signed release and denial receipts.

Implementability score: 0.58

### Make evidence authority explicit before action

Summary: Retrieval and compression create derived views; the runtime must preserve authoritative source identity and omissions before those views justify an effect.

Analysis: [make evidence authority explicit before action](2026-10-20/sovereignty.md#make-evidence-authority-explicit-before-action)

Core sources: [Same Simulation, Different Evidence v1](https://arxiv.org/abs/2610.26836v1), [KEEP-Bench v1](https://arxiv.org/abs/2610.26827v1)

Implementable now:
- mark authoritative and advisory outputs;
- preserve source IDs and omission manifests;
- rehydrate sources for high-risk actions;
- bind effect receipts to the evidence version used.

Implementability score: 0.81

## Current implication

Evidence and approval both need exact bindings. Derived context must point back to authoritative sources, and runtime approval must name the one effect it authorizes.
