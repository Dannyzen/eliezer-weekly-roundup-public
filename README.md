# Eliezer Weekly Roundup

A living, category-first research system for the agentic stack: agents, tools, memory, orchestration, evaluation, local-first infrastructure, and strategy.
The primary lens is the agentic stack itself, not generic AI news. The repo tracks research and releases that change how a builder should design autonomous systems: orchestration, prompting, tool use, memory, deterministic testing, observability, multi-agent systems, model routing, and sovereign or self-hosted infrastructure.

## Latest update

- Daily scan, 2026-07-06: [roundup](roundups/2026-07-06.md)
- AgenticAI daily analysis: [2026-07-06](AgenticAI/2026-07-06/reasoning.md)
- Strategy daily sovereignty: [2026-07-06](Strategy/2026-07-06/sovereignty.md)
- Fresh AgenticAI index: [AgenticAI README](AgenticAI/README.md)
- Fresh Strategy index: [Strategy README](Strategy/README.md)
- Prior daily scan, 2026-07-05: [roundup](roundups/2026-07-05.md)
- Recent durable AgenticAI topics: [Skills as Control](AgenticAI/skills-as-control/skills-as-control.md), [Coding Agent Control Plane](AgenticAI/coding-agent-control-plane/coding-agent-control-plane.md), [Agent Harness Architecture](AgenticAI/agent-harness-architecture/agent-harness-architecture.md)
- Recent durable Strategy topics: [Agent Execution Control Plane](Strategy/agent-execution-control-plane/agent-execution-control-plane.md), [Runtime Governance](Strategy/runtime-governance/runtime-governance.md)
- Friday synthesis, week ending 2026-07-03: [roundup](roundups/2026-07-03.md)
- Deep Dive Wednesday, 2026-07-01: [Agent Execution Control Plane](Strategy/agent-execution-control-plane/agent-execution-control-plane.md)
- Prior Deep Dive Wednesday, 2026-06-24: [Memory Authority Control Plane](Strategy/memory-authority-control-plane/memory-authority-control-plane.md)
- Prior Deep Dive Wednesday, 2026-06-17: [Evidence Provenance Control Plane](Strategy/evidence-provenance-control-plane/evidence-provenance-control-plane.md)

## Current thesis

The agent stack is moving from prompt-managed behavior to explicit control surfaces that can be versioned, compiled, tested, scoped, revoked, enforced, and measured outside the model's private reasoning loop.

The 2026-07-03 Friday synthesis updated that thesis: autonomy becomes governable only where runtime state is explicit. The 2026-07-06 daily scan tightens the next layer: trust should be process-bound. Skill use, coding conversations, workspace substrates, and database sessions need process evidence before they gain authority.

The latest implementation and governance surfaces are:

- Skill-use evaluation needs process rubrics for selection, following, composition, and reflection, not only final verifier wins.
- Multi-turn coding agents need regression gates that replay prior commitments before accepting later edits.
- Coding-agent oversight should move into constrained substrates: file scope, network policy, typed checks, architecture rules, and local docs surfaces.
- Approved enterprise tasks should compile into budgeted database sessions with signed tokens, row and column scope, query budgets, disclosure budgets, and receipts.
- Memory needs failure-mode tests for sycophancy, stale state, evidence conflict, scope control, and supersession.
- Agent routing should buy reasoning effort before broad tool exposure when the failure class is planning or integration.
- Coding-agent harnesses need live code-plus-test evolution tasks and prompt-level requirement coverage, not only final pass rates.
- Skill marketplaces need composition fuzzing in addition to provenance, static scanning, and behavior detonation.
- Execution control needs principals, grants, targets, scopes, side-effect oracles, and durable audit trails.

## Browse by category

- [AgenticAI](AgenticAI/README.md): implementation-focused analysis on runtimes, evals, memory, tooling, orchestration, and environment design.
- [Strategy](Strategy/README.md): strategic analysis on sovereignty, governance, containment, infrastructure, operating models, and enterprise adoption.

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
