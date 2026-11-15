# Strategy

Control-plane research for authority, identity, provenance, gateways, approvals, privacy, and sovereign infrastructure.

## Latest structured update: 2026-11-15

### Separate operational telemetry from sensitive content

Summary: Google Data Cloud separates content-free metrics and trace spans from opt-in conversation logging in owner-controlled BigQuery tables.

Analysis: [Daily strategy](2026-11-15/sovereignty.md#1-separate-operational-telemetry-from-sensitive-conversation-content)

Core source: [Google Data Cloud announcement](https://cloud.google.com/blog/products/data-analytics/enterprise-ai-agent-observability-with-bigquery-and-looker/)

Implementable now:
- content-free run events by default
- independent gates for prompts, responses, arguments, and payloads
- owner-controlled content stores with separate IAM and retention
- protected-source suppression and logging-failure receipts

Implementability score: 0.90

### Make middleware the task-authority plane

Summary: Microsoft Agent Framework Python 1.26.0 adds application-owned context labeling, task-scoped authority guidance, typed outputs, and finite sandbox execution budgets.

Analysis: [Daily strategy](2026-11-15/sovereignty.md#2-put-context-classification-task-authority-and-execution-budgets-in-middleware)

Core source: [Python 1.26.0 release](https://github.com/microsoft/agent-framework/releases/tag/python-1.26.0)

Implementable now:
- context classification before planning
- principal, task, resource, and expiry-bound grants
- typed agent handoffs
- finite timeouts with cancellation and cleanup tests

Implementability score: 0.86

## Current strategic model

1. Operational telemetry and sensitive content are separate data classes.
2. Context labels inform policy without granting authority.
3. Task grants are scoped, expiring runtime objects.
4. Typed handoffs, timeouts, cancellation, and receipts belong in middleware.
5. Effects remain bound to exact user intent at invocation time.

## Browse

- [Daily roundup](../roundups/2026-11-15.md)
- [Daily strategy](2026-11-15/sovereignty.md)
- [Runtime governance](runtime-governance/runtime-governance.md)
- [Agent gateway governance](agent-gateway-governance/agent-gateway-governance.md)
- [Agent execution control plane](agent-execution-control-plane/agent-execution-control-plane.md)
