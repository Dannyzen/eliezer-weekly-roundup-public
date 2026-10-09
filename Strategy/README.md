# Strategy

This index tracks the most recent structured strategy research. Each finding links to the dated analysis, durable topics, primary sources, practical methods, and an implementability score.

## Latest Structured Update: 2026-10-09

The governance signal is early authority control: intervene before failure completes, require obligations before completion, bind skill selection before use, and compile policy before state changes.

### Treat skill selection as authority routing

Summary: Co-installed skill conflicts can silently remove normative behavior while task completion remains green. Skill loading needs overlap detection, first-read enforcement, and selection receipts.

Analysis: [daily strategy analysis](2026-10-09/sovereignty.md#treat-skill-selection-as-authority-routing)
Durable topic: [Skill Admission Control](skill-admission-control/skill-admission-control.md)
Core sources: [paper v1](https://arxiv.org/abs/2610.11647v1), [replication package](https://github.com/ltroin/conflict)
Tools and methodologies worth exploring now: catalog similarity scans, namespaces, precedence rules, first-read hooks, exclusive-function regression tests
Implementability score: 0.90

### Treat missing obligations as safety failures

Summary: Allowed actions do not prove a safe terminal state. Cleanup, verification, rollback, disclosure, and handoff need explicit obligations and evidence.

Analysis: [daily strategy analysis](2026-10-09/sovereignty.md#treat-missing-obligations-as-safety-failures)
Durable topic: [Runtime Governance](runtime-governance/runtime-governance.md)
Core sources: [paper v1](https://arxiv.org/abs/2610.11773v1), [public repository](https://github.com/THU-Agent/ObligationGuard)
Tools and methodologies worth exploring now: positive obligations, terminal-state checks, unresolved-obligation reports, completion authority gates
Implementability score: 0.78

### Make intervention a runtime-owned capability

Summary: Streaming trajectory monitoring can identify likely failure before completion, but automatic abort needs shadow evaluation, calibrated thresholds, and reversible rollout.

Analysis: [daily strategy analysis](2026-10-09/sovereignty.md#make-intervention-a-runtime-owned-capability)
Durable topic: [Runtime Governance](runtime-governance/runtime-governance.md)
Core source: [paper v1](https://arxiv.org/abs/2610.12375v1)
Tools and methodologies worth exploring now: streaming telemetry, trajectory references, warn and pause policy, intervention receipts, false-positive review
Implementability score: 0.62

### Compile policy before granting tool authority

Summary: NOMOS provides a control-plane shape that binds authored policy, typed rules, static schema checks, replay preflight, active versions, and deterministic block receipts.

Analysis: [daily strategy analysis](2026-10-09/sovereignty.md#compile-policy-before-granting-tool-authority)
Durable topic: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md)
Core sources: [paper v1](https://arxiv.org/abs/2610.11030v1), [artifact repository](https://github.com/iamupd/NOMOS), [Zenodo record](https://zenodo.org/records/22123420)
Tools and methodologies worth exploring now: typed policy IR, schema validation, preflight replay, deterministic action gates, safety and benign-utility metrics
Implementability score: 0.58

## Current implication

Governance should attach to the earliest decisive boundary: first skill read, terminal obligation, live trajectory deviation, or state-changing call. Later review remains evidence for improvement, not permission for the action that already happened.

Latest roundup: [2026-10-09](../roundups/2026-10-09.md).
