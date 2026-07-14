# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan, 2026-07-14

### Durable effects need fresh authority at the commit boundary

Summary: Commit-time authorization requires the witness behind a durable effect to remain fresh, causally prior, bound to that exact effect, and eligible when the effect commits. A July 13 OpenBox and Temporal integration supplies a product-side implementation signal through durable workflow interceptors, policy verdicts, approvals, signing, and OpenTelemetry evidence.

Analysis: [daily sovereignty analysis](2026-07-14/sovereignty.md#durable-effects-need-fresh-authority-at-the-commit-boundary)
Durable topics: [Context-to-Execution Integrity](context-to-execution-integrity/context-to-execution-integrity.md), [Governed Workflow Substrates](governed-workflow-substrates/governed-workflow-substrates.md)
Core sources: [Temporary Authority, Permanent Effects](https://arxiv.org/abs/2607.10487v1), [OpenBox and Temporal announcement](https://www.prnewswire.com/news-releases/as-enterprises-move-ai-agents-into-production-openbox-ai-and-temporal-introduce-runtime-governance-for-long-running-agents-302820622.html), [OpenBox Temporal SDK](https://github.com/OpenBox-AI/openbox-temporal-sdk-python)
Implementable now:
- bind principal, target, source version, effect digest, policy epoch, expiry, and branch eligibility into one authorization record
- recheck that record inside the final commit activity after waits, retries, callbacks, or approvals
- score visible completion and authorized completion separately
Tools, repositories, and methodologies worth exploring:
- Temporal, `OpenBox-AI/openbox-temporal-sdk-python`, OpenTelemetry, OPA, Cedar, OpenFGA, controlled invalidation, manifest-bound authorization
Evidence caveat:
- the paper's CommitGuard implementation is not publicly linked, and the OpenBox integration was not executed during this read-only cron scan
Implementability score: 0.74

## Supporting recent Strategy context

The July 14 scan adds a temporal constraint to the evidence-is-not-authority thesis. A release or approval can be valid when planning starts and invalid when the side effect becomes durable. Durable execution therefore needs commit-time reauthorization, not only preserved workflow state.
