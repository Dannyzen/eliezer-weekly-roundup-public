# Eliezer Weekly Roundup

A category-first research system for the agentic stack: evaluation, tools, memory, orchestration, execution control, gateways, and sovereign infrastructure.

The repo separates patterns that can be tried now from ideas that still need research, replication, or operational maturity.

## Latest update

- Daily research, 2026-08-10: [lifecycle controls for faults, drift, persistent carriers, and memory](roundups/2026-08-10.md)
- AgenticAI daily analysis: [2026-08-10](AgenticAI/2026-08-10/reasoning.md)
- Strategy daily sovereignty: [2026-08-10](Strategy/2026-08-10/sovereignty.md)
- Friday synthesis, week ending 2026-08-07: [retained state is authority](roundups/2026-08-07.md)
- Latest implementation index: [AgenticAI](AgenticAI/README.md)
- Latest governance index: [Strategy](Strategy/README.md)
- Deep Dive Wednesday, 2026-08-05: [stateful effect governance at the commit boundary](Strategy/stateful-effect-governance/stateful-effect-governance.md)

## Current thesis

The practical rule is retained state is not authority:

- agent harnesses need controlled fault injection at shared API boundaries before release;
- coding-agent advisors need deterministic drift triggers before they may intervene;
- persistent-risk claims need carrier-lineage traces through trigger and effect;
- memory needs explicit active, superseded, revoked, quarantined, and re-promoted states;
- structured documents need deterministic search, navigation, and bounded reads before dense retrieval;
- coding-agent scores need planner, executor, scaffold, protocol, and version identity;
- skill files need software supply-chain admission before they load;
- trajectory risk needs bounded pre-action state outside the acting model;
- gateways need routing receipts, spend budgets, temporal policy, and rate limits;
- coding agents need oracle alignment, workspace revision identity, and local scout evidence before expensive mutation;
- failed trajectories need earliest decisive-error attribution with linked evidence;
- monitors may escalate, but deterministic checks and oracles certify narrow facts;
- execution should use the smallest runtime that satisfies an explicit capability need;
- inherited policy must compile into one visible effective-policy receipt;
- side effects under memory uncertainty need certificates over retained worlds, not one retrieved context;
- resume, memory revision, and policy authorization need explicit state-transition contracts;
- skill catalogs need trigger, compliance, and boundary scores under progressive disclosure;
- self-written skills need pre-commit admission before they become executable memory;
- tool descriptions need canary audits before they can mint selection authority;
- multi-turn tool history needs authority labels before it can flip the next call;
- audio, summaries, and consolidated memory remain below the privilege of current verified state.

The model may propose. A separately controlled boundary grants permission or certifies success.

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

- [Evaluation Containment Control Plane](Strategy/evaluation-containment-control-plane/evaluation-containment-control-plane.md)
- [Stateful Effect Governance](Strategy/stateful-effect-governance/stateful-effect-governance.md)
- [Agent Self-Improvement Governance](Strategy/agent-self-improvement-governance/agent-self-improvement-governance.md)
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
