# Eliezer Weekly Roundup

A category-first research system for the agentic stack: evaluation, tools, memory, orchestration, execution control, gateways, and sovereign infrastructure.

The repo separates patterns that can be tried now from ideas that still need research, replication, or operational maturity.

## Latest update

- Daily research, 2026-09-06: [a parsable success is not an honest result](roundups/2026-09-06.md)
- AgenticAI daily analysis: [2026-09-06](AgenticAI/2026-09-06/reasoning.md)
- Strategy daily analysis: [2026-09-06](Strategy/2026-09-06/sovereignty.md)
- Friday synthesis, 2026-09-04: [observed success is not authorization](roundups/2026-09-04.md)
- Deep Dive Wednesday, 2026-09-02: [defense as skill](Strategy/defense-as-skill/defense-as-skill.md)
- Latest implementation index: [AgenticAI](AgenticAI/README.md)
- Latest governance index: [Strategy](Strategy/README.md)

## Current thesis

Observed success is not authorization. A green functional test, a parsed tool-call rate, a current replica, a valid OAuth token, a declared skill interface, and a trusted plugin can all be true while the runtime is already wrong. A governable runtime should:

- treat HTTP 200 with a parsable body as incomplete tool success until the schema can reject illegal values;
- treat a shared model name as an unmeasured instrument until same-window and next-day observer gates pass;
- treat a decision graph as incomplete reconstruction until tool state and verifier verdicts are in the replay contract;
- treat functional test success as incomplete acceptance until review-constraint oracles also pass;
- treat Single-PoC crash suppression as incomplete security acceptance until related-PoC and semantic oracles also pass;
- treat GUI overcompliance as unauthorized execution and require terminate-with-conflict as a first-class action;
- index coding-agent traces as owned memory with session/turn provenance rather than pasting transcripts;
- commit speculative tool macros only from isolated snapshots after an exact first-action match;
- treat serving adapters as part of the measurement instrument, logging raw completions separately from parsed tool calls;
- treat reusable skills as covert policy objects and audit them with selection-lift fixtures, not scanner verdicts alone;
- treat loaded skills as delayed-authority objects and consult a task-conditioned guard before sensitive effects;
- treat lifecycle-hook updates as privileged admission, not plugin metadata refresh;
- treat replica freshness as insufficient authorization until plans cite and revalidate exact parent record IDs;
- bind remote tool calls to invocation-scoped workload leases instead of connect-time OAuth alone;
- treat the user invocation as an activation plan over untrusted repository content;
- bind permission checks to the exact resource, model, route, and configuration used;
- remove outbound capabilities from components that read untrusted content;
- separate user preference, standing policy, and exact-effect authorization;
- evaluate runtime controllers separately from fixed workers across cheap fixtures and full-task anchors;
- halt evaluation once a calibrated prefix already predicts the outcome;
- compile operational records into deterministic, replayable evaluation episodes before model judging;
- measure memory as stored state, delivered context, management work, and task outcome;
- carry recurring state only through explicit continuity contracts with provenance and expiry.

The model can propose actions, summaries, skill changes, routes, plans, and experiments. Resource identity, typed bridges, attributable verification, information-flow labels, deterministic policy, and durable authority decide what may change and what may cross a trust boundary.

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
