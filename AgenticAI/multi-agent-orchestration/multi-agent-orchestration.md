# Multi-Agent Orchestration

Last updated: 2026-06-07

Multi-agent orchestration is the control layer for deciding when multiple agents should collaborate, which evidence should move between them, and when communication costs exceed the expected benefit.

## Core thesis

The wrong default is “add agents and let them chat.” The right default is “collect independent evidence, estimate value of communication, route only useful disagreement, and preserve topology decisions in the trace.”

That means a multi-agent runtime needs:
- first-pass answers before discussion;
- calibrated confidence and uncertainty;
- evidence provenance per agent;
- disagreement clustering;
- communication budgets;
- topology events such as leader selection, edge pruning, patching, reconstruction, and stop conditions;
- post-task credit assignment tied to agent roles and evidence.

## Why this topic now

The May 29 scan surfaced three convergent papers:

- CONCAT uses consensus and confidence to build ad hoc agent teams without training a domain-specific planner.
- DynaGraph monitors confidence and dynamically patches or reconstructs reasoning subgraphs to avoid static-topology cascades and unconstrained trajectory bloat.
- Meta-Team preserves distributed execution context and turns team experience into behavioral, coordination, and organization-level improvements.

The shared signal is not a specific framework. It is the move from agent count to orchestration evidence.

## May 29 update: confidence-gated topology beats broadcast collaboration

CONCAT’s practical lesson is immediately usable: start with independent answers, cluster by agreement, select leaders by confidence, estimate whether two leaders have enough disagreement and evidence value to justify communication, and prune low-value edges.

DynaGraph adds the failure-recovery shape: a multi-agent topology should not be fixed at run start. When confidence drops locally, patch the gap. When the logic ruptures, reconstruct the subgraph. The useful abstraction is a topology event log, not a transcript of every chat turn.

Meta-Team adds the learning loop: long-horizon multi-agent failures interleave individual agent actions and inter-agent messages, so post-task evolution needs the distributed context of each agent, not only the final result.

## Practical implementation pattern

1. **Independent first pass.** Each agent produces an answer, confidence, evidence list, and uncertainty notes before seeing peers.
2. **Consensus map.** Cluster outputs by answer and evidence agreement.
3. **Leader selection.** Pick representative agents by confidence, evidence quality, and role fit.
4. **Communication budget.** Only open channels where disagreement value exceeds expected token/latency cost.
5. **Topology repair.** Log when an edge is pruned, a subgraph is patched, a failed branch is rebuilt, or the system stops discussion.
6. **Post-task attribution.** Tie success/failure to role, message, evidence, topology, and tool-use events.

## Tools, repos, and methodologies worth trying now

- LangGraph or Temporal for explicit graph/state-machine orchestration.
- AutoGen or CrewAI when using existing agent abstractions, but with custom communication gates.
- Pydantic state models for agent answer, confidence, evidence, disagreement, and topology-event records.
- OpenTelemetry spans for inter-agent messages and topology changes.
- Small ablation suites comparing single-agent, broadcast multi-agent, confidence-gated multi-agent, and topology-repair variants.

## May 30 update: local coherence is not global coherence

The compositional-incoherence paper adds a hard check to the multi-agent orchestration thesis. A system can assemble locally coherent probabilistic claims from components that each saw only part of the problem and still violate the joint constraints of the full problem.

The practical implication is that multi-agent orchestration needs declared coupling constraints and runtime composition checks. More retrieval, partition-aware prompting, or one final aggregator LLM is not enough if the composed output violates probability or dependency constraints.

Practical lesson:
- require subagents to emit typed claims, confidence/probability, evidence, and dependency assumptions;
- declare cross-component coupling constraints before aggregation where possible;
- run coherence checks or cheaper proxy checks before accepting a combined answer;
- log coherence residuals, repairs, and escalations as topology events;
- compare broadcast discussion against independent-first-pass plus coherence-check baselines.

Source:
- [Locally Coherent, Globally Incoherent](https://arxiv.org/abs/2605.30335v1)

## June 3 update: coding-agent teams need dependency waves and validation gates

SPOQ adds a production-shaped pattern to multi-agent software engineering. The key abstraction is not a chat room. It is a task dependency graph with wave-based dispatch, planning validation before work starts, code validation before merge, and human specialists represented as first-class nodes for decomposition, escalation, and acceptance.

This extends the existing confidence-gated topology thesis. Independent first passes and communication budgets still matter, but coding work also has hard ordering constraints. A reviewer agent cannot validate a patch that should not have been started because its prerequisite interface did not exist. A worker agent should not receive the entire issue stream if its next valid task is a small dependency-ready node.

Practical lesson:
- decompose work into typed tasks with dependency edges and readiness conditions;
- dispatch only the current execution wave instead of broadcasting all context to all agents;
- require planning validation before execution and artifact validation before merge;
- assign human-as-agent nodes for decomposition, escalation, acceptance, or domain judgment;
- log wave, dependency, validator, reviewer, retry, and merge-gate events as orchestration evidence.

Source:
- [SPOQ](https://arxiv.org/abs/2606.03115v1)

## June 7 update: more agents need protocol-aligned baselines

Do More Agents Help? adds the evaluation discipline this topic needs. A multi-agent workflow should not claim improvement unless it beats a matched single-agent baseline under the same benchmark loader, tool access, answer contract, usage accounting, and trajectory logging. Otherwise, the topology may be getting credit for a looser protocol.

The practical lesson is to normalize the substrate before optimizing the team. Compare single-agent, fixed multi-agent, and evolving multi-agent workflows with the same tools, budgets, contracts, and logging. Then inspect whether the extra messages, roles, retries, and coordination costs produced better outcomes under the same rules.

Practical lesson:
- run single-agent, fixed-MAS, and evolving-MAS baselines under identical tool access and answer contracts;
- log inter-agent messages, tool calls, token spend, wall-clock time, retries, and final-state checks;
- score quality, latency, cost, and coordination overhead together;
- run topology ablations before adopting broadcast chat teams;
- preserve protocol fields in the trace so future results are comparable.

Sources:
- [Do More Agents Help?](https://arxiv.org/abs/2606.05670v1)
- [LINs-lab/MASArena BenchAgent branch](https://github.com/LINs-lab/MASArena/tree/BenchAgent)

## Implementability score

0.68

The first version is implementable with ordinary engineering: independent first passes, confidence fields, dependency DAGs, execution waves, planning gates, artifact validators, clustering, budget rules, claim schemas, cheap coherence checks, protocol-aligned baselines, and trace logging. Full dynamic topology repair, formal projection repair, and reliable self-evolution need deeper architecture and careful benchmark design.

## Core sources

- CONCAT: Consensus- and Confidence-Driven Ad Hoc Teaming for Efficient LLM-Based Multi-Agent Systems: https://arxiv.org/abs/2605.29612
- DynaGraph: Lightweight Multi-Model Interaction Framework via Dynamic Topological Reconfiguration: https://arxiv.org/abs/2605.29511
- Evolve as a Team: Collaborative Self-Evolution for LLM-based Multi-Agent Systems: https://arxiv.org/abs/2605.29790
- SPOQ: Specialist Orchestrated Queuing for Multi-Agent Software Engineering: https://arxiv.org/abs/2606.03115v1
- Do More Agents Help? Controlled and Protocol-Aligned Evaluation of LLM Agent Workflows: https://arxiv.org/abs/2606.05670v1
