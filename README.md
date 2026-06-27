# Eliezer Weekly Roundup

A living, category-first research system for the agentic stack: agents, tools, memory, orchestration, evaluation, local-first infrastructure, and strategy.
The primary lens is the agentic stack itself, not generic AI news. The repo tracks research and releases that change how a builder should design autonomous systems: orchestration, prompting, tool use, memory, deterministic testing, observability, multi-agent systems, model routing, and sovereign or self-hosted infrastructure.

## Latest update

- Daily scan, 2026-06-27: [roundup](roundups/2026-06-27.md)
- AgenticAI daily analysis: [2026-06-27](AgenticAI/2026-06-27/reasoning.md)
- Strategy daily analysis: [2026-06-27](Strategy/2026-06-27/sovereignty.md)
- Fresh AgenticAI index: [AgenticAI README](AgenticAI/README.md)
- Fresh Strategy index: [Strategy README](Strategy/README.md)
- Friday synthesis, week ending 2026-06-26: [roundup](roundups/2026-06-26.md)
- New durable AgenticAI topic from this week: [Coding Agent Control Plane](AgenticAI/coding-agent-control-plane/coding-agent-control-plane.md)
- Deep Dive Wednesday, 2026-06-24: [Memory Authority Control Plane](Strategy/memory-authority-control-plane/memory-authority-control-plane.md)
- Previous daily scan: [2026-06-25](roundups/2026-06-25.md)
- Previous Friday synthesis: [week ending 2026-06-19](roundups/2026-06-19.md)
- Prior Deep Dive Wednesday, 2026-06-17: [Evidence Provenance Control Plane](Strategy/evidence-provenance-control-plane/evidence-provenance-control-plane.md)
- Prior Friday synthesis: [week ending 2026-06-12](roundups/2026-06-12.md)
- Prior Friday synthesis: [week ending 2026-06-05](roundups/2026-06-05.md)
- Prior Friday synthesis: [week ending 2026-05-29](roundups/2026-05-29.md)

## Current thesis

The agent stack is moving from prompt-managed behavior to explicit control surfaces that can be versioned, compiled, tested, scoped, revoked, and enforced outside the model's private reasoning loop.

The 2026-06-27 daily scan adds a sharper operational point: scale is not a substitute for evidence. Bigger loops, more models, and larger tool catalogs only help when the harness can prove improvement, stop waste, preserve workflow authority, and govern pre-execution authority surfaces.

The latest four implementation and governance surfaces are:

- Iterative agent loops need semantic stopping, cached trajectory replay, and operational-token accounting.
- Legacy workflows should be uplifted through policy-governed agent hooks while deterministic engines keep structural authority.
- Model routers need all-wrong co-failure measurement before routing, voting, or mixture-of-agents complexity is justified.
- Tool and plugin catalogs need source allowlists, update epochs, enabled-set analysis, and poisoning fixtures before agents consume them.

The 2026-06-26 Friday synthesis remains the broadest current weekly map, and the 2026-06-24 Deep Dive Wednesday update remains the strategic foundation underneath memory and authority work: memory is a policy-bearing authority object, not just context.

## Browse by category

- [AgenticAI](AgenticAI/README.md): implementation-focused analysis on runtimes, evals, memory, tooling, orchestration, and environment design.
- [Strategy](Strategy/README.md): strategic analysis on sovereignty, governance, containment, infrastructure, operating models, and enterprise adoption.

## Durable topics

### AgenticAI

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
