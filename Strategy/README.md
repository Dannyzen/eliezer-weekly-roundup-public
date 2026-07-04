# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan, 2026-07-04

### Runtime permission UX is a security primitive, not an approval popup

Summary: Janus turns user-involved permission management into a testable runtime design space. The lesson is that permission UX is part of the execution-control plane: the system needs typed requests, escalation policies, fatigue-aware user involvement, and durable grant or denial evidence.

Analysis: [daily sovereignty analysis](2026-07-04/sovereignty.md#runtime-permission-ux-is-a-security-primitive-not-an-approval-popup)
Durable topics: [Agent Execution Control Plane](agent-execution-control-plane/agent-execution-control-plane.md), [Runtime Governance](runtime-governance/runtime-governance.md), [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md)
Core sources: [Janus paper](https://arxiv.org/abs/2607.01510v1), [GraceBrigham/Janus](https://github.com/GraceBrigham/Janus)
Implementable now:
- represent permission requests as typed actor, resource, capability, action, risk, and evidence objects
- test multiple permission-assistant modes instead of one generic approval dialog
- add synthetic responder profiles for fatigue and alignment behavior
- store grants and denials as trace artifacts
Tools, repos, and methodologies worth exploring:
- GraceBrigham/Janus, HCP-style grants and handles, Cedar, OPA, OpenFGA, permission-fatigue fixtures
Implementability score: 0.74

### Skill admission moves from provenance to behavior evidence

Summary: Cloak and Detonate reframes public skills as a malware-sandbox problem. Provenance and static scanning are not enough when a skill can preserve malicious behavior while changing visible form. Production admission needs sandbox detonation tied to runtime policy.

Analysis: [daily sovereignty analysis](2026-07-04/sovereignty.md#skill-admission-moves-from-provenance-to-behavior-evidence)
Durable topics: [Runtime Governance](runtime-governance/runtime-governance.md), [Agent Sandboxing](agent-sandboxing/agent-sandboxing.md), [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [AgenticAI Skills as Control](../AgenticAI/skills-as-control/skills-as-control.md)
Core source: [Cloak and Detonate](https://arxiv.org/abs/2607.02357v1)
Implementable now:
- separate provenance verification, static scanning, behavior detonation, and production admission
- require skill manifests with declared side effects, network needs, tool scopes, memory access, and credential needs
- run new skills against fake secrets, fake repos, and egress traps
- attach detonation traces to skill admission records
Tools, repos, and methodologies worth exploring:
- sandbox workers, static triage plus dynamic taint, skill manifests, lockfiles, egress allowlists, fake secret canaries
Implementability score: 0.62

## Supporting recent Strategy context

The 2026-07-01 Deep Dive remains the foundation: connection is not authority. The 2026-07-04 daily scan adds two product-facing consequences: user permission has to become a measured runtime object, and skill admission has to produce behavior evidence before granting authority.
