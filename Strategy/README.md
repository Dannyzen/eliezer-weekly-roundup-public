# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan 2026-06-30

### Memory poisoning detection belongs in the trajectory, not the prompt

Summary: Persistent-memory attacks create runtime signatures. The new forensic trajectory paper shows that memory recall followed by an effectful sink can be a high-signal detector, which means memory security has to live in traces and policy gates, not only in text filters.

Analysis: [daily sovereignty analysis](2026-06-30/sovereignty.md#memory-poisoning-detection-belongs-in-the-trajectory-not-the-prompt)
Durable topics: [Memory Authority Control Plane](memory-authority-control-plane/memory-authority-control-plane.md), [Evidence Provenance Control Plane](evidence-provenance-control-plane/evidence-provenance-control-plane.md), [Runtime Governance](runtime-governance/runtime-governance.md)
Core source: [Forensic Trajectory Signatures for Agent Memory Poisoning Detection](https://arxiv.org/abs/2606.30566v1)
Implementable now:
- log memory recall and effectful tool calls in the same trajectory
- define invariants for recall-to-email, recall-to-export, recall-to-deploy, and recall-to-write paths
- start with rule detectors before training workflow-specific classifiers
- keep memory-poisoning and prompt-injection signatures separate
Tools, repos, and methodologies worth exploring:
- OpenTelemetry spans, memory authority schemas, transition-rule detectors, random-forest baselines, labeled incident traces, privacy-safe trace retention
Implementability score: 0.70

### Multi-agent routing needs empirical capability tests, not self-descriptions

Summary: ANTAP's linguistic firewall reframes multi-agent routing as capability evidence, not trust in descriptions. Agents and tools should be selected from active tests and signed registry facts, not from self-advertised skills or manipulable text.

Analysis: [daily sovereignty analysis](2026-06-30/sovereignty.md#multi-agent-routing-needs-empirical-capability-tests-not-self-descriptions)
Durable topics: [Model Router Governance](model-router-governance/model-router-governance.md), [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Agent Authority Manifests](agent-authority-manifests/agent-authority-manifests.md)
Core source: [Linguistic Firewall](https://arxiv.org/abs/2606.30555v1)
Implementable now:
- build active probes for each worker or tool class before admission
- store capability scores with date, model, test suite, and policy version
- rerun probes after prompt, model, skill, or tool changes
- separate relevance, authorization, trust, and observed competence during routing
Tools, repos, and methodologies worth exploring:
- capability registries, active probe suites, signed test artifacts, calibration curves, model-router logs, gateway admission tests
Implementability score: 0.55

## Supporting recent Strategy context

The 2026-06-26 weekly synthesis remains the broad current governance map: [weekly sovereignty analysis](2026-06-26/sovereignty.md). The 2026-06-29 daily scan said privacy and prompt injection are control-data separation problems. The new 2026-06-30 scan adds trajectory and routing evidence: memory attacks and multi-agent routing both need observed behavior, not description trust.
