# Eliezer Weekly Roundup

A category-first research system for the agentic stack: evaluation, tools, memory, orchestration, execution control, gateways, and sovereign infrastructure.

The repo separates patterns that can be tried now from ideas that still need research, replication, or operational maturity.

## Latest update

- Daily scan, 2026-10-01: [inspectable adaptation across harnesses, memory, routing, and verification](roundups/2026-10-01.md)
- AgenticAI daily analysis: [SelfSearch, persistent context graphs, and workflow routing](AgenticAI/2026-10-01/reasoning.md)
- Strategy daily analysis: [world-model audits for action verifiers](Strategy/2026-10-01/sovereignty.md)
- Latest implementation index: [AgenticAI](AgenticAI/README.md)
- Latest governance index: [Strategy](Strategy/README.md)
- Deep Dive Wednesday, 2026-09-30: [the model-harness pair is the deployment unit](roundups/2026-09-30.md)
- Friday synthesis, 2026-09-25: [agent reliability is a custody problem](roundups/2026-09-25.md)

## Current thesis

Agent reliability depends on executable authority and inspectable adaptation. The model-harness pair remains the deployment unit, while external control planes must preserve raw evidence, freeze evaluation, validate world models, and own promotion. An editable agent may propose a new harness, memory policy, or route. It must not certify or promote itself.

The current stack therefore emphasizes:

- versioned self-improvement episodes with external evaluation and promotion;
- persistent context graphs that select original evidence instead of rewriting it;
- workflow routing with complete cost, latency, fallback, and validation receipts;
- versioned action-state graphs plus mutation tests and randomized attestation;

- versioned worker identities, capabilities, budgets, artifacts, and terminal receipts;
- execution graphs with typed handoffs and explicit dependency order;
- executable benchmark contracts for tool state and evaluator reads;
- mutation tests for benchmark checkers and scorers;
- composable attack, channel, defense, agent, trace, and verdict matrices;
- machine-checkable payload and policy delivery receipts;
- exact tool-argument and realized-effect predicates;
- typed capability shapes with current-session value validation;
- audience labels that survive derivation and consolidation;
- object-specific grants for memory scope widening;
- exact viewer-set and delivered-context receipts;
- environment identity and conformance per evaluation scenario;
- paired governed and ungoverned trajectory replay;
- signed intervention ledgers that count false alarms and lost corrections;
- typed execution-state nodes with references to immutable raw observations;
- progressive evidence access instead of full transcript replay;
- provenance-root collapse before shared-memory admission;
- source-class gates, contest state, and supersession for persistent claims;
- separate client authentication, delegated credential admission, tool authorization, and effect receipts;
- canonical action manifests with resolved tool identity and typed arguments;
- source-linked obligation ledgers that the model cannot close by claiming completion;
- independent trace capture with remote retention and sequence-gap detection;
- deterministic shutdown, credential, network, queue, and compute revocation below orchestration.

Start with the executable boundary: validate worker and tool contracts, prove delivery and effects, bind context to viewers, and bind dispatch to typed capabilities.

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
- [Composable Agent Harnesses](AgenticAI/composable-agent-harnesses/composable-agent-harnesses.md)
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
