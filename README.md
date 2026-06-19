# Eliezer Weekly Roundup

A living, category-first research system for the agentic stack: agents, tools, memory, orchestration, evaluation, local-first infrastructure, and strategy.
The primary lens is the agentic stack itself, not generic AI news. The repo tracks research and releases that change how a builder should design autonomous systems: orchestration, prompting, tool use, memory, deterministic testing, observability, multi-agent systems, model routing, and sovereign or self-hosted infrastructure.

## Latest update

- Friday synthesis, week ending 2026-06-19: [roundup](roundups/2026-06-19.md)
- AgenticAI weekly analysis: [2026-06-19](AgenticAI/2026-06-19/reasoning.md)
- Strategy weekly analysis: [2026-06-19](Strategy/2026-06-19/sovereignty.md)
- Fresh AgenticAI index: [AgenticAI README](AgenticAI/README.md)
- Fresh Strategy index: [Strategy README](Strategy/README.md)
- Deep Dive Wednesday, 2026-06-17: [Evidence Provenance Control Plane](Strategy/evidence-provenance-control-plane/evidence-provenance-control-plane.md)
- Daily scan inputs in this synthesis window: [2026-06-13](roundups/2026-06-13.md), [2026-06-14](roundups/2026-06-14.md), [2026-06-15](roundups/2026-06-15.md), [2026-06-16](roundups/2026-06-16.md), [2026-06-17](roundups/2026-06-17.md), [2026-06-18](roundups/2026-06-18.md); the 2026-06-19 files were promoted into the Friday synthesis above
- Previous Friday synthesis: [week ending 2026-06-12](roundups/2026-06-12.md)
- Prior Friday synthesis: [week ending 2026-06-05](roundups/2026-06-05.md)
- Prior Friday synthesis: [week ending 2026-05-29](roundups/2026-05-29.md)
- Prior Friday synthesis: [week ending 2026-05-22](roundups/2026-05-22.md)

## Current thesis

The agent stack is moving from permissive prompts and ad hoc tool catalogs to runtime-owned objects. The useful question is no longer only "can the model use more memory, search, tools, skills, or agents?" It is "which runtime object owns the state, capability, evidence, and authority here?"

The 2026-06-19 Friday synthesis promotes six week-level patterns:
- Sessioned state replaces scattered memory, context, and handoff logs. Branch, replay, memory references, tool evidence, workspace placement, and lineage belong in the object agents transform.
- Tool surfaces become discovered, compiled, and cache-aware. Search capabilities before exposing them, then compile repeated service workflows into effect-typed programs where appropriate.
- Skills become admitted and measured behavior modules. Scan, route, benchmark, freeze, and regression-test skills before they influence a run.
- Evaluation shifts from final outcome to trajectory, oracle, harm, and effort telemetry. Measure the path, evidence, state delta, and effort, not only the answer.
- Governance moves to evidence provenance and runtime contracts. Source IDs, raw outputs, contract hashes, policy verdicts, and correction-derived checks should be trace fields.
- Mutation authority leaves agents for brokers and tamper-resistant paths. Agents should propose actions; brokers should validate certificates, mint short-lived credentials, and record signed outcomes.

## Browse by category

- [AgenticAI](AgenticAI/README.md): implementation-focused analysis on runtimes, evals, memory, tooling, orchestration, and environment design.
- [Strategy](Strategy/README.md): strategic analysis on sovereignty, governance, containment, infrastructure, operating models, and enterprise adoption.

## Durable topics

### AgenticAI

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

## How the repo is organized

- `AgenticAI/YYYY-MM-DD/reasoning.md`: category analysis for the week or day, with source links and implementation guidance.
- `Strategy/YYYY-MM-DD/sovereignty.md`: strategy analysis for the week or day, with source links and implementation guidance.
- `AgenticAI/<topic>/<topic>.md` and `Strategy/<topic>/<topic>.md`: durable deep dives when a pattern deserves to persist beyond one cycle.
- `roundups/YYYY-MM-DD.md`: cross-category synthesis tying implementable patterns to strategic implications.

## What gets selected

Selected items usually have at least one of these properties:
- they change agent orchestration, tool use, memory, or evaluation practice;
- they expose a repeatable implementation pattern that can be tried now;
- they show where local-first or self-hosted infrastructure is becoming practical;
- they reveal a governance, containment, or observability requirement that serious agent builders should design around;
- they clarify model-routing and reasoning tradeoffs rather than merely announcing a bigger model;
- they provide primary-source evidence: paper, repo, release note, official documentation, or vendor post.

## Implementability scores

- `1.0`: straightforward to implement now with standard tools and normal engineering effort.
- `0.5`: implementable, but it needs meaningful architecture or operational sophistication.
- `0.0`: mostly conceptual, speculative, or blocked on missing research or infrastructure.

## Subscribe

Use GitHub's Watch feature if you want repo updates as the research system evolves. The category READMEs are the intended entry points; the roundup is the synthesis layer.
