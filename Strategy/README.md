# Strategy

Control-plane research for authority, identity, provenance, gateways, approvals, privacy, and sovereign infrastructure.

## Latest structured update: 2026-11-07

### Separate recurring execution from approval and measurement policy

Summary: GitHub now supports cron-based local automations with workspace custom agents and opt-in assisted approvals. Scheduling, authorization, and telemetry are separate control surfaces. Engagement metrics do not prove reliable or authorized outcomes.

Analysis: [Daily strategy](2026-11-07/sovereignty.md#1-separate-recurring-execution-from-approval-and-measurement-policy)

Core sources: [GitHub Copilot weekly releases](https://github.blog/changelog/2026-11-06-github-copilot-weekly-releases-november-2/), [Copilot impact dashboard update](https://github.blog/changelog/2026-11-06-copilot-impact-dashboard-adds-chat-and-vs-code-agent-usage/)

Implementable now:
- versioned recurring-task manifests
- effect-scoped assisted approval rules
- idempotency, current-state preflight, and sink receipts
- separate scheduled, denied, failed, partial, completed, and reviewed metrics

Implementability score: 0.82

## Current strategic model

1. Evidence informs decisions but does not grant authority.
2. Writable context is a claim surface, not a policy store.
3. Recurring work needs separate trigger, authority, and evidence contracts.
4. Effect-bound tickets narrow host grants.
5. Receipts prove what changed.
6. Privacy scope follows traces and downstream propagation.

## Browse

- [Latest roundup](../roundups/2026-11-07.md)
- [Latest dated strategy](2026-11-07/sovereignty.md)
- [Friday synthesis](2026-11-06/sovereignty.md)
- [Effect-bound skill execution](effect-bound-skill-execution/effect-bound-skill-execution.md)
- [Evidence provenance control plane](evidence-provenance-control-plane/evidence-provenance-control-plane.md)
- [Agent execution control plane](agent-execution-control-plane/agent-execution-control-plane.md)
- [Memory authority control plane](memory-authority-control-plane/memory-authority-control-plane.md)
- [Runtime governance](runtime-governance/runtime-governance.md)
- [Untrusted data boundaries](untrusted-data-boundaries/untrusted-data-boundaries.md)
