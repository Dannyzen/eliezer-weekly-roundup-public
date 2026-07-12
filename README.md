# Eliezer Weekly Roundup

A living, category-first research system for the agentic stack: agents, tools, memory, orchestration, evaluation, local-first infrastructure, and strategy.

The primary lens is the agentic stack itself, not generic AI news. The repo tracks research and releases that change how a builder should design autonomous systems: orchestration, prompting, tool use, memory, deterministic testing, observability, multi-agent systems, model routing, and sovereign or self-hosted infrastructure.

## Latest update

- Daily scan, 2026-07-12: [roundup](roundups/2026-07-12.md)
- AgenticAI daily analysis: [2026-07-12](AgenticAI/2026-07-12/reasoning.md)
- Strategy daily sovereignty: [2026-07-12](Strategy/2026-07-12/sovereignty.md)
- Fresh AgenticAI index: [AgenticAI README](AgenticAI/README.md)
- Fresh Strategy index: [Strategy README](Strategy/README.md)
- Prior daily scan, 2026-07-11: [roundup](roundups/2026-07-11.md)
- Friday synthesis, week ending 2026-07-10: [roundup](roundups/2026-07-10.md)
- Deep Dive Wednesday, 2026-07-08: [Context-to-Execution Integrity](Strategy/context-to-execution-integrity/context-to-execution-integrity.md)
- Prior Friday synthesis, week ending 2026-07-03: [roundup](roundups/2026-07-03.md)
- Prior Deep Dive Wednesday, 2026-07-01: [Agent Execution Control Plane](Strategy/agent-execution-control-plane/agent-execution-control-plane.md)
- Prior Deep Dive Wednesday, 2026-06-24: [Memory Authority Control Plane](Strategy/memory-authority-control-plane/memory-authority-control-plane.md)
- Prior Deep Dive Wednesday, 2026-06-17: [Evidence Provenance Control Plane](Strategy/evidence-provenance-control-plane/evidence-provenance-control-plane.md)

## Current thesis

The agent stack is moving from prompt-managed behavior to explicit control surfaces that can be versioned, compiled, tested, scoped, revoked, enforced, and measured outside the model's private reasoning loop.

The 2026-07-10 Friday synthesis made the operating rule explicit: evidence is not authority. Agents can read messy context, but protected side effects need typed releases, scoped grants, exact identities, deterministic gates, and receipts.

The 2026-07-11 daily scan adds the asynchronous corollary: work that continues after the user disconnects, the rollout engine lags, or the context window stretches needs stronger run evidence, not weaker oversight.

The 2026-07-12 daily scan adds the delivery corollary: agent policy should fail in ordinary engineering systems. Static taint checks, delegated gateway identity, compiled sandbox fields, and terminal run evidence are more durable than prompt-only rules.

The latest implementation and governance surfaces are:

- System-prompt injection can now be checked as JavaScript and TypeScript source-to-sink data flow before merge.
- Delegated MCP identity needs gateway-owned discovery, registration, refresh, concurrency, catalog filtering, and audit.
- Sandbox runtime, mounts, imports, token outcomes, and safe outputs are becoming compiled workflow fields.
- Causal data-science agents need hidden-ground-truth evals, deterministic grading, and scored abstention.
- Agentic RL needs action-to-observation trace boundaries before expensive asynchronous training can be trusted.
- Long-context model methods can lower trace pressure, but context selection, compression, retrieval, and audit remain runtime policy.
- Managed agent platforms are becoming background execution substrates with remote MCP, persistent sandboxes, credential refresh, and client reconnect.
- Preflight agent graphs expose models, tools, memory, policies, handoffs, effects, and loop-bound risks before execution.
- Executable harness contracts move source scope, routing, output rules, trace hygiene, and recommendation language out of prompt prose and into testable runtime code.
- Framework-aware eval packs make model, scaffold, task world, supervisor loop, recovery behavior, and wall-clock cost separate benchmark variables.
- Tool-use traces need phase labels, action severity, and causal root-cause slices, not only final task accuracy.
- Memory systems need scoped state roles, conflict preservation, provenance, and an explicit remain-silent path before influencing action.
- Skills, tool servers, package names, and repository identifiers are supply-chain authority and need exact provenance before load or install.
- Browser and tool observations need untrusted-data boundaries, quarantine reads, byte-faithful approvals, and contextual least privilege.

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
