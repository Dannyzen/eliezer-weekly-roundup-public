# Strategy Daily Analysis - 2026-10-20

The strongest governance signal today is that approval must bind to the exact effect, while evidence must retain explicit source authority before it can justify that effect.

## Bind every outbound connection to a one-time signed verdict

Connection Escrow holds each outbound TCP connection inside the kernel before any packet leaves. A verifier in a separate container returns a signed verdict bound to one socket cookie and destination. Expired, replayed, rebound, forged, and late approvals are refused. No verdict by the deadline resets the connection.

The prototype passed a 36-check adversarial suite on the eBPF hold point, gated 600 connections from six pods on a single-node Kubernetes cluster, and reported about 4.5 ms median hold time per released connection. It also attributed sockets to process, executable digest, cgroup, pod, and SPIFFE identity. This closes the gap between application-layer approval and the connection the kernel later opens.

Why it matters:
- SDK hooks and proxy settings are bypassable by child processes, raw sockets, or generated code;
- standing destination policy does not authorize a particular connection;
- one-time effect binding prevents a valid approval from being replayed or rebound.

Implementable now:
- hold egress at cgroup and kernel boundaries for high-risk agent pods;
- bind verdicts to socket identity, destination, principal, expiry, and single use;
- isolate verifier keys and fail closed on timeout;
- issue signed, hash-chained receipts for release and denial.

Artifact status: the public MIT repository is populated and was inspected read-only. The prototype needs Linux 6.x, cgroup v2, eBPF privileges, node access, and careful coexistence testing with Cilium. It currently covers IPv4; UDP is pinned rather than escrowed; Rustls and stripped TLS binaries are not covered by the content gate; the Kubernetes result is single-node.

Implementability score: 0.58

Core sources:
- [Connection Escrow paper v1](https://arxiv.org/abs/2610.26501v1)
- [Connection Escrow repository](https://github.com/45h0kg/benign-attach-gateway)

## Make evidence authority explicit before action

Two fresh studies show that answer quality is a weak proxy for evidence integrity. Same Simulation, Different Evidence found that retrieval changed which tool output agents trusted even when the simulator produced the keyed value. KEEP-Bench found that compressors often dropped qualifiers, alternatives, or minority evidence even when a downstream reader could still answer correctly.

The governance implication is direct: retrieval and compression create derived views. They do not silently replace the source of record. Before an agent uses a derived view to justify a state change, the runtime should know which source was authoritative, what evidence was omitted, and whether the action depends on a qualifier or minority path that survived compression.

Implementable now:
- mark authoritative and advisory outputs in tool contracts;
- preserve source IDs and omission manifests through compression;
- require source rehydration for high-risk or low-confidence actions;
- bind effect receipts to the evidence version actually used.

Implementability score: 0.81

Core sources:
- [Same Simulation, Different Evidence v1](https://arxiv.org/abs/2610.26836v1)
- [KEEP-Bench v1](https://arxiv.org/abs/2610.26827v1)

## Working conclusion

Sovereign agent systems need exact bindings on both sides of a decision: evidence must remain tied to authoritative sources, and approval must remain tied to one concrete effect. Derived summaries and reusable permissions are convenience layers, not authority.
