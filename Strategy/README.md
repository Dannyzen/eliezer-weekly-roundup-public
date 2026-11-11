# Strategy

Control-plane research for authority, identity, provenance, gateways, approvals, privacy, and sovereign infrastructure.

## Latest structured update: 2026-11-11

### Put personal-agent policy outside the prompt

Summary: Nod is a local-first personal-agent reference architecture with containerized workspaces, private vault entry, server-side mutation checks, approvals, and action receipts. Its model-based safety check still failed 8 of 240 decisions with a smaller model.

Analysis: [Daily strategy](2026-11-11/sovereignty.md#1-put-personal-agent-policy-outside-the-prompt)

Core sources: [official announcement](https://blog.n8n.io/meet-nod/), [repository](https://github.com/n8n-io/nod), [product and benchmark page](https://nod.n8n.io/)

Implementable now:
- deterministic action authorization where possible
- effect-bound approvals
- secret entry outside model context
- action, identity, cost, and outcome receipts
- hosted-dependency and telemetry review

Implementability score: 0.76

## Current strategic model

1. Local execution does not establish sovereignty by itself.
2. Policy and credentials belong outside model context.
3. Model-based safety decisions need fail-closed thresholds and independent tests.
4. Approvals should bind to one exact effect and identity.
5. Receipts should preserve requests, decisions, actions, costs, and outcomes.
6. Hosted dependencies and telemetry remain part of the data boundary.

## Browse

- [Latest roundup](../roundups/2026-11-11.md)
- [Latest dated strategy](2026-11-11/sovereignty.md)
- [Friday synthesis](2026-11-06/sovereignty.md)
- [Evidence provenance control plane](evidence-provenance-control-plane/evidence-provenance-control-plane.md)
- [Effect-bound skill execution](effect-bound-skill-execution/effect-bound-skill-execution.md)
- [Agent execution control plane](agent-execution-control-plane/agent-execution-control-plane.md)
- [Context-to-execution integrity](context-to-execution-integrity/context-to-execution-integrity.md)
- [Memory authority control plane](memory-authority-control-plane/memory-authority-control-plane.md)
- [Runtime governance](runtime-governance/runtime-governance.md)
- [Untrusted data boundaries](untrusted-data-boundaries/untrusted-data-boundaries.md)
