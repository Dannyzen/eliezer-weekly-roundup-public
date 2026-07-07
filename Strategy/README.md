# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan, 2026-07-07

### Untrusted data needs a boundary plane, not better reminders

Summary: UCM, ADI, and FARMA make the same governance point across browser, tool, and memory channels. Untrusted content should be treated as a restricted evidence class with origin, scope, allowed uses, lineage, and effect gates. The model should not be asked to solve that boundary inside private reasoning.

Analysis: [daily sovereignty analysis](2026-07-07/sovereignty.md#untrusted-data-needs-a-boundary-plane-not-better-reminders)
Durable topics: [Untrusted Data Boundaries](untrusted-data-boundaries/untrusted-data-boundaries.md), [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Runtime Governance](runtime-governance/runtime-governance.md), [Memory Authority Control Plane](memory-authority-control-plane/memory-authority-control-plane.md)
Core sources: [Untrusted Content Masking](https://arxiv.org/abs/2607.05277v1), [UCM repository](https://github.com/ethz-spylab/untrusted-content-masking), [Agent Data Injection](https://arxiv.org/abs/2607.05120v1), [FARMA](https://arxiv.org/abs/2607.05029v1)
Implementable now:
- attach trust class, origin, scope, and allowed-use metadata to observations
- keep untrusted text out of the main planner where possible
- expose narrow typed quarantine reads instead of raw text reads
- gate high-risk effects by evidence class
Tools, repos, and methodologies worth exploring:
- UCM, AgentDojo-style injection fixtures, FARMA-style memory poisoning fixtures, OPA or Cedar policy over evidence class, OpenTelemetry spans for boundary events
Implementability score: 0.78

### Agent data injection is the next gateway threat after instruction injection

Summary: ADI attacks tool and page data as evidence. A malicious value can sit in a normal-looking field and steer an agent toward an unauthorized action without ever looking like a prompt injection. Gateway policy must preserve field provenance and trust class.

Analysis: [daily sovereignty analysis](2026-07-07/sovereignty.md#agent-data-injection-is-the-next-gateway-threat-after-instruction-injection)
Durable topics: [Untrusted Data Boundaries](untrusted-data-boundaries/untrusted-data-boundaries.md), [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Evidence Provenance Control Plane](evidence-provenance-control-plane/evidence-provenance-control-plane.md)
Core source: [Agent Data Injection](https://arxiv.org/abs/2607.05120v1)
Implementable now:
- split tool outputs into trusted metadata and untrusted fields
- fuzz delimiter, serialization, and nested-field boundaries
- require high-risk actions to cite trusted evidence or human approval
- deny effects justified only by untrusted content
Tools, repos, and methodologies worth exploring:
- field-level taint tracking, AgentDojo-style attack suites, evidence-object IDs, gateway policy over evidence origin
Implementability score: 0.64

### Personal-agent sovereignty needs consent and platform-mediation tests

Summary: SovereignPA-Bench reframes personal-agent evaluation around user sovereignty, not only personalization or tool success. A personal agent should preserve current user intent while respecting privacy, consent, evidence quality, burden, and resistance to platform incentives.

Analysis: [daily sovereignty analysis](2026-07-07/sovereignty.md#personal-agent-sovereignty-needs-consent-and-platform-mediation-tests)
Durable topics: [Local-First Agents](local-first-agents/local-first-agents.md), [Agent Authority Manifests](agent-authority-manifests/agent-authority-manifests.md), [Runtime Governance](runtime-governance/runtime-governance.md)
Core source: [SovereignPA-Bench](https://arxiv.org/abs/2607.05363v1)
Implementable now:
- add consent scope, revocation, platform influence, and user burden to personal-agent task manifests
- test preference changes over time
- log when platform-provided information influences a recommendation
- create fixtures where service incentives conflict with user intent
Tools, repos, and methodologies worth exploring:
- SovereignPA-Bench dimensions as a product checklist, local-first memory with consent and supersession metadata, approval receipts, user-visible policy manifests
Implementability score: 0.43

## Supporting recent Strategy context

The 2026-07-01 Deep Dive established connection is not authority. The 2026-07-06 scan made process authority explicit. The 2026-07-07 scan adds the missing input layer: observation is not authority either. Browser content, tool fields, and recalled memories need evidence boundaries before they can shape effects.
