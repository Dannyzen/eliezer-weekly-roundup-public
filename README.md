# Eliezer Weekly Roundup

A living, category-first research system for the agentic stack: agents, tools, memory, orchestration, evaluation, local-first infrastructure, and strategy.

The primary lens is the agentic stack itself, not generic AI news. The repo tracks research and releases that change how a builder should design autonomous systems: orchestration, prompting, tool use, memory, deterministic testing, observability, multi-agent systems, model routing, and sovereign or self-hosted infrastructure.

## Latest update

- Friday synthesis, week ending 2026-05-15: [roundup](roundups/2026-05-15.md)
- AgenticAI weekly analysis: [2026-05-15](AgenticAI/2026-05-15/reasoning.md)
- Strategy weekly analysis: [2026-05-15](Strategy/2026-05-15/sovereignty.md)
- Fresh AgenticAI index: [AgenticAI README](AgenticAI/README.md)
- Fresh Strategy index: [Strategy README](Strategy/README.md)
- Latest Deep Dive Wednesday asset: [GUI-Tool Path Orchestration](AgenticAI/gui-tool-path-orchestration/gui-tool-path-orchestration.md)
- Prior Friday synthesis: [week ending 2026-05-08](roundups/2026-05-08.md)
- Earlier Friday synthesis: [week ending 2026-05-01](roundups/2026-05-01.md)

## Current thesis

The agent stack is becoming a compiled runtime for stateful work. The useful question is not “which model is smartest?” but “which tool surface did it see, which workflow profile ran, which model was routed to which phase, which memory state was trusted, which skill version authorized the action, which GUI/tool path was taken, which sandbox contained it, and can the entire run be replayed?”

Friday synthesis 2026-05-15 adds six durable implementation patterns:

- Tool schemas, capability catalogs, workflow profiles, model routing, token budgets, and async futures should be treated as versioned runtime control surfaces.
- Evaluation should move from final answer checks to trajectory and process evidence: prefix warnings, chaos fixtures, test evolution, full-cycle coding eval, and lucky-pass detection.
- Memory and context should be governed state with raw-event preservation, typed promotion, writeback gates, invalidation tests, and retrieval-path provenance.
- Skills are a semantic supply chain: manifest them, fuzz them, version them, pin privileged variants, and log side effects.
- Computer-use agents need path-level traces across GUI actions, tool calls, screenshots, confirmations, and verification.
- Coding and browser agents need session identity, sandbox policy, scoped consent, parameter validation, provenance gates, and parallel guardrails.

## Browse by category

- [AgenticAI](AgenticAI/README.md): implementation-focused analysis on runtimes, evals, memory, tooling, orchestration, and environment design.
- [Strategy](Strategy/README.md): strategic analysis on sovereignty, governance, containment, infrastructure, operating models, and enterprise adoption.

## Durable topics

### AgenticAI

- [Agent Harness Architecture](AgenticAI/agent-harness-architecture/agent-harness-architecture.md)
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
