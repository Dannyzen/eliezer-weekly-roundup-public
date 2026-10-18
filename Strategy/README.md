# Strategy

Governance analysis for identity, authority, execution control, evidence provenance, gateways, containment, and sovereignty.

## Latest Structured Update: 2026-10-18 Daily Scan

### Make sandbox state, identity, and egress runtime objects

Summary: Safe code execution requires a control plane that binds template identity, lifecycle state, command authorization, and effective egress policy outside the untrusted guest.

Analysis: [make sandbox state, identity, and egress runtime objects](2026-10-18/sovereignty.md#make-sandbox-state-identity-and-egress-runtime-objects)

Core sources: [official SPACE announcement](https://www.perplexity.ai/hub/blog/open-sourcing-space), [repository](https://github.com/perplexityai/SPACE), [architecture guide](https://space.docs.perplexity.ai/guide/architecture.html), [egress profiles](https://space.docs.perplexity.ai/guide/egress-profiles.html)

Implementable now:
- bind sandboxes to resolved template digests and principals;
- separate lifecycle operations from command-stream authorization;
- keep credentials and egress policy outside the guest;
- fail closed on invalid or missing policy;
- test concurrency, retries, stale attachment, and recovery.

Implementability score: 0.64

## Current implication

A sandbox should be governed as a state machine, not treated as an opaque process container. Isolation, identity, network policy, lifecycle, and receipts must converge before execution authority is granted.
