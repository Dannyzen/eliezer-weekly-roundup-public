# Strategy

This index tracks the most recent structured strategy research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-09-04

### Treat lifecycle-hook updates as a privileged control plane, not plugin metadata

Summary: HookPry attacks the update path that harnesses trust blindly. Lifecycle hooks run host-privileged commands as configuration, including when the LLM never observes them. Across seven harnesses and 1,000 runs, verified E2E-ASR is 77.9% macro-average. Hermes is 92.5%. Claude Code is 52.5%.

Analysis: [daily strategy](2026-09-04/sovereignty.md#treat-lifecycle-hook-updates-as-a-privileged-control-plane-not-plugin-metadata)
Core source: [paper](https://arxiv.org/abs/2609.03884v1)
Tools and methodologies worth exploring now: hook-command hash pins, plugin-update as new admission, hook-event receipts, hook-only mutation fixtures, hard brokers for host effects
Implementability score: 0.62

### Fresh memory does not authorize a stale plan

Summary: PlanFence distinguishes replica freshness from lineage validity. Plans cite exact parent record IDs. The executor validates only action-relevant parents, then replans or blocks. In 30 live workflows, freshness-only execution issued the obsolete action every time (0/30). PlanFence completed all 30 without an invalid action.

Analysis: [daily strategy](2026-09-04/sovereignty.md#fresh-memory-does-not-authorize-a-stale-plan)
Core source: [paper](https://arxiv.org/abs/2609.03340v1)
Tools and methodologies worth exploring now: parent-ID stamps on plans, action-scoped validation, freshness-only negative fixtures
Implementability score: 0.58

## Previous structured update: 2026-09-03

### Treat reusable skills as covert policy objects

Summary: SkillShift preserves declared functionality and valid outputs while steering shopping and dependency choices. PSR rises to 81.33% and 63.33% at 100% valid-output rate. Static scanners that catch direct injection do not distinguish SkillShift Attack skills from paired Clean skills. Audit skills as frozen policies, not only as packages.

Analysis: [daily strategy](2026-09-03/sovereignty.md#treat-reusable-skills-as-covert-policy-objects)
Core source: [paper](https://arxiv.org/abs/2609.02564v1)
Tools and methodologies worth exploring now: Skill Policy Integrity fixtures, frozen candidate sets, PSR and valid-output metrics, direct-injection positive controls, scanner-plus-behavior release gates
Implementability score: 0.72

### Bind remote tool calls to a fresh workload lease, not OAuth alone

Summary: ACLE-MCP names the post-authorization execution trust gap. A short-lived, sender-constrained capability lease is consumed by an Execution Gate before protected tool logic. In the local simulation, OAuth-only and connect-time attestation block none of six misuse families; full ACLE-MCP blocks the evaluated set at +25.7% p95 latency.

Analysis: [daily strategy](2026-09-03/sovereignty.md#bind-remote-tool-calls-to-a-fresh-workload-lease-not-oauth-alone)
Core source: [paper](https://arxiv.org/abs/2609.02690v1)
Tools and methodologies worth exploring now: invocation-scoped leases, workload-id and freshness binding, non-bypassable execution gates, substitution and stale-appraisal fixtures
Implementability score: 0.48

## Current implication

A trusted plugin, a current replica, and a valid OAuth token can all be true while the runtime is already wrong. Hook updates need admission. Plans need parent IDs. Remote tools still need invocation-scoped leases.
