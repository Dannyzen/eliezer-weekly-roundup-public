# Multi-Agent Orchestration

Last updated: 2026-05-29

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

## Implementability score

0.60

The first version is implementable with ordinary engineering: independent first passes, confidence fields, clustering, budget rules, and trace logging. Full dynamic topology repair and reliable self-evolution need deeper architecture and careful benchmark design.

## Core sources

- CONCAT: Consensus- and Confidence-Driven Ad Hoc Teaming for Efficient LLM-Based Multi-Agent Systems: https://arxiv.org/abs/2605.29612
- DynaGraph: Lightweight Multi-Model Interaction Framework via Dynamic Topological Reconfiguration: https://arxiv.org/abs/2605.29511
- Evolve as a Team: Collaborative Self-Evolution for LLM-based Multi-Agent Systems: https://arxiv.org/abs/2605.29790
