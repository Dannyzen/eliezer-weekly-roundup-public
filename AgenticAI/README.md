# AgenticAI

This index tracks the most recent structured update. Each finding includes a short human-readable summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan 2026-06-27

### Semantic early stopping cuts agent-loop spend without quality loss

Summary: Fixed `max_iterations` is a wasteful default for iterative agent loops. Semantic stopping uses draft-embedding distance plus patience to halt when meaning stops changing, and the reported judge-free version cut operational tokens by 38 percent at parity quality on a HotpotQA split.

Analysis: [daily reasoning analysis](2026-06-27/reasoning.md#semantic-early-stopping-cuts-agent-loop-spend-without-quality-loss)
Durable topics: [Sessionful Agent Loops](sessionful-agent-loops/sessionful-agent-loops.md), [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md), [Context Economy for Agents](context-economy/context-economy.md), [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core sources: [Semantic Early-Stopping](https://arxiv.org/abs/2606.27009v1), [semantic-halting-problem repo](https://github.com/SahilShrivastava-Dev/semantic-halting-problem)
Implementable now:
- add embedding-distance stopping to one writer-critic, RAG, or code-review loop
- replay fixed-cap, semantic-stop, quality-gated, and oracle selectors over the same cached trajectories
- log operational tokens separately from judge or measurement tokens
- tune patience and distance thresholds per workflow class
Tools, repos, and methodologies worth exploring:
- draft embeddings, cosine-distance patience windows, replayed trajectory caches, operational-token accounting, round-selection ablations
Implementability score: 0.86

### Process harnesses put agents around workflows instead of replacing them

Summary: CUGA FLO gives the right enterprise migration pattern: keep the deterministic workflow engine structurally authoritative, then let policy-governed agents reason only at designated task, decision, and flow hooks.

Analysis: [daily reasoning analysis](2026-06-27/reasoning.md#process-harnesses-put-agents-around-workflows-instead-of-replacing-them)
Durable topics: [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md), [Agent Serving Runtime](agent-serving-runtime/agent-serving-runtime.md), [Multi-Agent Orchestration](multi-agent-orchestration/multi-agent-orchestration.md), [Governed Workflow Substrates](../Strategy/governed-workflow-substrates/governed-workflow-substrates.md)
Core sources: [CUGA FLO process harness](https://arxiv.org/abs/2606.27188v1), [IBM CUGA examples](https://huggingface.co/blog/ibm-research/cuga-apps), [cuga-project/cuga-agent](https://github.com/cuga-project/cuga-agent)
Implementable now:
- choose one deterministic workflow and mark only the control points where reasoning is allowed
- define TaskAgent, DecisionAgent, and FlowAgent responsibilities before writing prompts
- make the workflow engine own ordering, state transitions, and required approvals
- attach policy fields to every hook: tools, data scope, escalation, audit event, and rollback path
Tools, repos, and methodologies worth exploring:
- CUGA, process-harness overlays, TDF-style hook maps, process FRAME policy bundles, OpenAPI/MCP integration behind workflow control
Implementability score: 0.74

## Supporting recent AgenticAI context

The 2026-06-26 weekly synthesis remains the broadest current map: [weekly reasoning analysis](2026-06-26/reasoning.md). The new 2026-06-27 daily scan narrows the implementation lesson: shrink uncontrolled loops and wrap real workflows with explicit hooks instead of adding orchestration by default.
