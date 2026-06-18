# Eliezer Weekly Roundup

A living, category-first research system for the agentic stack: agents, tools, memory, orchestration, evaluation, local-first infrastructure, and strategy.
The primary lens is the agentic stack itself, not generic AI news. The repo tracks research and releases that change how a builder should design autonomous systems: orchestration, prompting, tool use, memory, deterministic testing, observability, multi-agent systems, model routing, and sovereign or self-hosted infrastructure.

## Latest update

- Daily scan, 2026-06-18: [roundup](roundups/2026-06-18.md)
- AgenticAI daily analysis: [2026-06-18](AgenticAI/2026-06-18/reasoning.md)
- Strategy daily analysis: [2026-06-18](Strategy/2026-06-18/sovereignty.md)
- Fresh AgenticAI index: [AgenticAI README](AgenticAI/README.md)
- Fresh Strategy index: [Strategy README](Strategy/README.md)
- Related durable topics: [Agent Gateway Governance](Strategy/agent-gateway-governance/agent-gateway-governance.md), [Runtime Governance](Strategy/runtime-governance/runtime-governance.md), [Memory Systems](AgenticAI/memory-systems/memory-systems.md), [Shared-State Agents](Strategy/shared-state-agents/shared-state-agents.md), [Agentic Search and Retrieval](AgenticAI/agentic-search/agentic-search.md), [Agent Sandboxing](Strategy/agent-sandboxing/agent-sandboxing.md), [Evidence Provenance Control Plane](Strategy/evidence-provenance-control-plane/evidence-provenance-control-plane.md)
- Daily scan, 2026-06-17: [roundup](roundups/2026-06-17.md)
- Deep Dive Wednesday, 2026-06-17: [Evidence Provenance Control Plane](Strategy/evidence-provenance-control-plane/evidence-provenance-control-plane.md)
- Daily scan, 2026-06-16: [roundup](roundups/2026-06-16.md)
- Daily scan, 2026-06-15: [roundup](roundups/2026-06-15.md)
- Daily scan, 2026-06-14: [roundup](roundups/2026-06-14.md)
- Daily scan, 2026-06-13: [roundup](roundups/2026-06-13.md)
- Friday synthesis, week ending 2026-06-12: [roundup](roundups/2026-06-12.md)
- Deep Dive Wednesday, 2026-06-10: [Enterprise MCP Orchestration](AgenticAI/enterprise-mcp-orchestration/enterprise-mcp-orchestration.md)
- Previous Friday synthesis, week ending 2026-06-05: [roundup](roundups/2026-06-05.md)
- Prior Friday synthesis: [week ending 2026-05-29](roundups/2026-05-29.md)
- Prior Friday synthesis: [week ending 2026-05-22](roundups/2026-05-22.md)
- Prior Friday synthesis: [week ending 2026-05-15](roundups/2026-05-15.md)

## Current thesis

The agent stack is moving from permissive context and tool catalogs to contract-mediated operational units. The useful question is no longer only "can the model use more memory, search, tools, skills, or agents?" It is "which runtime contract grants authority here, which evidence dimensions were measured, which source owns the claim, and what verifier can stop the action before harm?"

The 2026-06-18 daily scan adds five implementation patterns:
- Tool gates need contract integrity, not only hidden tools. Manifest effects, scopes, and policy predicates are authority-bearing runtime inputs.
- Compliance is becoming trace-time enforcement. Runtime monitors should intercept tool calls and model outputs before external mutation.
- Shared memory needs governance scores, not only recall. Utility, access-control violation, and active-forgetting failure have to be measured together.
- Grounding and web-agent verification need explicit evidence paths. Search route, source rendering, cache behavior, page state, and final-claim linkage should be visible control-plane fields.
- Sandboxes need bounded claims and weakest-link evidence. A sandbox only proves the dimensions it actually measures.

The 2026-06-17 Deep Dive Wednesday asset turns evidence provenance into a durable control-plane model: every high-risk claim, tool output, test, skill, route, policy verdict, and delegated handoff needs source-owned proof that can be replayed.

The 2026-06-17 daily scan added four implementation patterns:
- MCP factuality needs source ownership, not pooled support. Stable tool IDs, source IDs, raw outputs, and claim-to-source verdicts are now core trace fields.
- Skill systems need compositional routing plus per-skill utility evals. Decompose tasks, retrieve skill candidates, compose a dependency DAG, and test skills against no-skill baselines before promotion.
- Evaluation needs trajectory preferences and oracle-aware test gates. Progress-sensitive comparisons and explicit test-oracle checks are more informative than terminal pass/fail or test-file counts.
- Evidence provenance is becoming the control-plane primitive. Agent registries, access graphs, source IDs, policy verdicts, and delegation traces should converge into one audit substrate.

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
