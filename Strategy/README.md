# Strategy

This index tracks the most recent structured strategy research. Each finding links to the dated analysis, durable topics, primary sources, practical methods, and an implementability score.

## Latest Structured Update: 2026-10-14 Daily Scan

The current governance signal is authority lifecycle control. Risk can be forecast before execution, and granted capability should disappear immediately after its last justified use.

### Gate unauthorized actions before execution

Summary: A linear readout of open-weight model residual states forecasts unauthorized actions before the tool call with AUROC 0.94. The signal can reduce violations, but it requires model access, domain calibration, and an external authority gate.

Analysis: [daily strategy analysis](2026-10-14/sovereignty.md#internal-state-gates-can-stop-unauthorized-actions-before-execution)
Durable topic: [Runtime Governance](runtime-governance/runtime-governance.md)
Core sources: [paper v1](https://arxiv.org/abs/2610.17301v1), [code and experimental record](https://github.com/AryaFayyazi/Honesty)
Tools and methodologies worth exploring now: matched authorization twins, pre-action shadow scoring, conformal thresholds, escalation budgets, frozen readouts, domain-transfer gates
Implementability score: 0.44

### Expire capabilities after their last justified use

Summary: CreepScope measures stale authority at every workflow step. An injected stale send succeeds in all nine persistent-policy episodes and none of the three step-lease episodes in its local agent case.

Analysis: [daily strategy analysis](2026-10-14/sovereignty.md#creepscope-expire-authority-after-its-last-justified-step)
Durable topic: [Agent Execution Control Plane](agent-execution-control-plane/agent-execution-control-plane.md)
Core source: [paper v1](https://arxiv.org/abs/2610.15988v1)
Tools and methodologies worth exploring now: step-bound leases, grant-use-expiry event logs, Capability-Step Exposure, Residual Privilege Debt, stale-action injection, exact replay-grid gates
Implementability score: 0.78

## Current implication

Evaluate authorization as a lifecycle: predict risk before effect release, bind capability to one justified step, and prove expiry afterward.

Latest roundup: [2026-10-14 daily scan](../roundups/2026-10-14.md).
