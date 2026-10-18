# Strategy Daily Analysis: 2026-10-18

## Thesis

Agent isolation becomes governable when sandbox identity, lifecycle, template provenance, command attachment, and egress policy are explicit runtime objects outside the guest. A microVM alone is only one boundary.

## Make sandbox state, identity, and egress runtime objects

Perplexity open-sourced SPACE on October 15 as an Apache 2.0 platform for agent code execution. The repository defines separate objects for templates, sandboxes, processes, command sessions, and asynchronous lifecycle operations. A sandbox reports the resolved template digest, command attachment uses a session-scoped token, and operator egress profiles admit exact domains, IPs, and CIDRs while rejecting malformed or unavailable policy at admission.

The useful architecture is the separation of concerns. The guest executes untrusted work. The control plane owns create, pause, suspend, wake, and delete operations. The data plane carries command output. Operators own templates, identity, egress composition, recovery, and telemetry. Native smoke scenarios cover authorization, concurrency, replay, recovery, and invalid admission paths.

Implementable now:
- bind every sandbox to a resolved template digest and principal;
- separate lifecycle operations from command-stream authorization;
- keep credentials and egress policy outside the guest;
- admit only exact, versioned egress profiles and fail closed on configuration drift;
- emit operation, process, policy, and recovery receipts;
- test concurrent create, retry, stale attachment, invalid admission, and recovery paths.

Implementability score: 0.64

Core sources: [official open-source announcement](https://www.perplexity.ai/hub/blog/open-sourcing-space), [SPACE repository](https://github.com/perplexityai/SPACE), [architecture guide](https://space.docs.perplexity.ai/guide/architecture.html), [egress profiles](https://space.docs.perplexity.ai/guide/egress-profiles.html)

The weakest point is operational weight. SPACE is a 5,000-file Rust, Kubernetes, Firecracker, and KVM control plane, not a drop-in library. Perplexity's production and security claims are first-party evidence, and independent replication was outside this read-only scan. Use the repository as an implementable reference architecture before treating it as a qualified production substrate.

## Strategic implication

Treat the sandbox as a governed state machine. The durable authority object should bind principal, template digest, lifecycle state, command session, effective egress policy, and receipts. Isolation without that control-plane state leaves retries, recovery, identity, and network authority implicit.
