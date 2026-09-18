# Eliezer Weekly Roundup

A category-first research system for the agentic stack: evaluation, tools, memory, orchestration, execution control, gateways, and sovereign infrastructure.

The repo separates patterns that can be tried now from ideas that still need research, replication, or operational maturity.

## Latest update

- Daily scan, 2026-09-18: [the harness is becoming a testable control plane](roundups/2026-09-18.md)
- AgenticAI daily analysis: [conditional harness design, incident replay, and semantic profiling](AgenticAI/2026-09-18/reasoning.md)
- Strategy daily analysis: [reversible skill mutation](Strategy/2026-09-18/sovereignty.md)
- Durable topic: [Incident Replay Testing](AgenticAI/incident-replay-testing/incident-replay-testing.md)
- Deep Dive Wednesday, 2026-09-16: [the social harness is the missing cross-principal control plane](Strategy/agent-community-governance/agent-community-governance.md)
- Friday synthesis, 2026-09-11: [the runtime needs an evidence constitution](roundups/2026-09-11.md)
- Latest implementation index: [AgenticAI](AgenticAI/README.md)
- Latest governance index: [Strategy](Strategy/README.md)

## Current thesis

The harness should be an explicit, testable control plane rather than opaque glue. Component policy belongs to measured model and budget conditions, incident replay belongs in CI, semantic profiling belongs above raw traces, and persistent skill mutation belongs behind localized tests and rollback. A governable stack keeps the following objects outside model self-certification:

- tool progress, remaining work, and cache-policy receipts;
- shared human-agent control identity, relationships, and state;
- evidence lineage, contamination state, and independent validation;
- cumulative authority, threshold, and separation-of-duty policy state;
- benchmark resolution, tier membership, and scaffold identity;
- skill provenance, privilege manifests, review receipts, and probe evidence;
- cross-principal message identity, protocol state, expiry, and violation evidence;
- screenshot, accessibility, widget, and approval-view parity;
- unread-evidence coverage and diagnosis revision receipts;
- per-task collaboration routes calibrated to equal realized spend;
- immutable tool manifests binding package, source, schema, transport, and origin;
- transaction-aware effect contracts for status, idempotency, compensation, staging, dependency, coordination, and visibility;
- operator-specific action permission after package admission;
- process-level fault localization and recovery evidence;
- repository skills bound to one frozen source snapshot and paired controls;
- separate versions for stakeholder requirements and environment models;
- deployment counterexamples that can reopen accepted evaluations;
- budgeted skill evaluation with frozen candidates, holdouts, and receipts;
- worker fanout, memory pressure, wait phases, and restore latency;
- versioned interaction contracts that bind intent, authority, effects, and evidence;
- measured tool admission state, not registry presence;
- schema-valid tool results and runtime-owned completion state;
- binding constraints preserved through compaction and handoff;
- reward lifecycle evidence and temporally valid source truth;
- qualified tests and evidence lineage;
- memory provenance, compatibility, and probe receipts;
- content-addressed skill and harness versions;
- per-principal capabilities and exact-effect witnesses;
- end-principal identity and context ownership across delegation;
- persistent principal history across services and days.

Start with cheap boundaries: immutable admission manifests, outcome lookup, idempotency keys, unread-evidence ledgers, route receipts, startup probes, and schema enumerations. Add heavier search, collaboration, compensation, and fleet controls only when measured failures justify their cost.

## Browse by category

- [AgenticAI](AgenticAI/README.md): implementation analysis on evaluation, memory, context policy, search, tools, and orchestration.
- [Strategy](Strategy/README.md): governance analysis on identity, authority, execution control, gateways, containment, and sovereignty.

## Durable topics

### AgenticAI

- [Agent Static Analysis](AgenticAI/agent-static-analysis/agent-static-analysis.md)
- [Coding Agent Control Plane](AgenticAI/coding-agent-control-plane/coding-agent-control-plane.md)
- [Enterprise MCP Orchestration](AgenticAI/enterprise-mcp-orchestration/enterprise-mcp-orchestration.md)
- [Agentic Search and Retrieval](AgenticAI/agentic-search/agentic-search.md)
- [Agent Harness Architecture](AgenticAI/agent-harness-architecture/agent-harness-architecture.md)
- [Incident Replay Testing](AgenticAI/incident-replay-testing/incident-replay-testing.md)
- [Agent Serving Runtime](AgenticAI/agent-serving-runtime/agent-serving-runtime.md)
- [Multi-Agent Orchestration](AgenticAI/multi-agent-orchestration/multi-agent-orchestration.md)
- [Event-Sourced Agent Runtime](AgenticAI/event-sourced-agent-runtime/event-sourced-agent-runtime.md)
- [GUI-Tool Path Orchestration](AgenticAI/gui-tool-path-orchestration/gui-tool-path-orchestration.md)
- [Ticket-Native Agent Orchestration](AgenticAI/ticket-native-agent-orchestration/ticket-native-agent-orchestration.md)
- [Skills as Control](AgenticAI/skills-as-control/skills-as-control.md)
- [Trajectory-Aware Evaluation](AgenticAI/trajectory-aware-evaluation/trajectory-aware-evaluation.md)
- [Memory Systems](AgenticAI/memory-systems/memory-systems.md)
- [Context Economy for Agents](AgenticAI/context-economy/context-economy.md)
- [Agent Discovery](AgenticAI/agent-discovery/agent-discovery.md)
- [Knowledge-State Orchestration](AgenticAI/knowledge-state-orchestration/knowledge-state-orchestration.md)
- [Sessionful Agent Loops](AgenticAI/sessionful-agent-loops/sessionful-agent-loops.md)
- [Sandbox-Native Agent Workers](AgenticAI/sandbox-native-agent-workers/sandbox-native-agent-workers.md)

### Strategy

- [Agent Fleet Monitoring Control Plane](Strategy/agent-fleet-monitoring-control-plane/agent-fleet-monitoring-control-plane.md)
- [Defense as Skill](Strategy/defense-as-skill/defense-as-skill.md)
- [Evaluation Containment Control Plane](Strategy/evaluation-containment-control-plane/evaluation-containment-control-plane.md)
- [Stateful Effect Governance](Strategy/stateful-effect-governance/stateful-effect-governance.md)
- [Skill Admission Control](Strategy/skill-admission-control/skill-admission-control.md)
- [Agent Self-Improvement Governance](Strategy/agent-self-improvement-governance/agent-self-improvement-governance.md)
- [Operational State Preservation](Strategy/operational-state-preservation/operational-state-preservation.md)
- [Context-to-Execution Integrity](Strategy/context-to-execution-integrity/context-to-execution-integrity.md)
- [Untrusted Data Boundaries](Strategy/untrusted-data-boundaries/untrusted-data-boundaries.md)
- [Persistent-State Agent Control](Strategy/persistent-state-agent-control/persistent-state-agent-control.md)
- [Agent Execution Control Plane](Strategy/agent-execution-control-plane/agent-execution-control-plane.md)
- [Agent Community Governance](Strategy/agent-community-governance/agent-community-governance.md)
- [Memory Authority Control Plane](Strategy/memory-authority-control-plane/memory-authority-control-plane.md)
- [Agent Authority Manifests](Strategy/agent-authority-manifests/agent-authority-manifests.md)
- [Evidence Provenance Control Plane](Strategy/evidence-provenance-control-plane/evidence-provenance-control-plane.md)
- [RL Training Governance](Strategy/rl-training-governance/rl-training-governance.md)
- [Agent Network Containment](Strategy/agent-network-containment/agent-network-containment.md)
- [Agent Gateway Governance](Strategy/agent-gateway-governance/agent-gateway-governance.md)
- [Agent Provisioning Governance](Strategy/agent-provisioning-governance/agent-provisioning-governance.md)
- [Model Router Governance](Strategy/model-router-governance/model-router-governance.md)
- [Local-First Agents](Strategy/local-first-agents/local-first-agents.md)
- [Runtime Governance](Strategy/runtime-governance/runtime-governance.md)
- [Agent Sandboxing](Strategy/agent-sandboxing/agent-sandboxing.md)
- [Governed Workflow Substrates](Strategy/governed-workflow-substrates/governed-workflow-substrates.md)
- [Shared-State Agents](Strategy/shared-state-agents/shared-state-agents.md)

## Repository shape

- `AgenticAI/YYYY-MM-DD/reasoning.md`: dated implementation analysis.
- `Strategy/YYYY-MM-DD/sovereignty.md`: dated strategy analysis.
- `roundups/YYYY-MM-DD.md`: cross-category synthesis.
- `AgenticAI/<topic>/` and `Strategy/<topic>/`: durable deep dives.

## Implementability scores

- `1.0`: straightforward now with existing tools and normal engineering effort.
- `0.5`: implementable, but architecture or operations are material.
- `0.0`: conceptual, speculative, or blocked on missing infrastructure.
