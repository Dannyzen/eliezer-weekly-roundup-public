# AgenticAI

This index tracks the most recent structured update. Each finding includes a short human-readable summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan, 2026-07-07

### Untrusted web content should be masked before the planner sees it

Summary: Untrusted Content Masking makes prompt-injection defense a harness problem. Browser agents should not read attacker-controlled comments, reviews, ads, issue bodies, or repository content as raw planning context. Mask those DOM regions first, then expose narrow typed quarantine reads only when the task needs them.

Analysis: [daily reasoning analysis](2026-07-07/reasoning.md#untrusted-web-content-should-be-masked-before-the-planner-sees-it)
Durable topics: [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md), [Strategy Untrusted Data Boundaries](../Strategy/untrusted-data-boundaries/untrusted-data-boundaries.md), [Strategy Agent Gateway Governance](../Strategy/agent-gateway-governance/agent-gateway-governance.md)
Core sources: [Untrusted Content Masking paper](https://arxiv.org/abs/2607.05277v1), [UCM repository](https://github.com/ethz-spylab/untrusted-content-masking)
Implementable now:
- label untrusted DOM regions in controlled web surfaces
- replace untrusted regions with placeholders before planning
- expose a typed quarantine tool for narrow questions over hidden content
- replay seeded WASP-style prompt-injection pages as regression fixtures
Tools, repos, and methodologies worth exploring:
- `ethz-spylab/untrusted-content-masking`, DOM trust labels, CSS selector maps, Q-model typed answers, WebArena GitLab, WASP attack tests
Implementability score: 0.78

### Tool-use failure needs phase labels, not final accuracy

Summary: ToolFailBench shows that aggregate accuracy hides the failure phase. A model that never calls a needed tool, calls it with bad arguments, ignores the returned value, or overuses irrelevant tools needs different fixes. Tool traces should label the phase, not only the final outcome.

Analysis: [daily reasoning analysis](2026-07-07/reasoning.md#tool-use-failure-needs-phase-labels-not-final-accuracy)
Durable topics: [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md), [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md), [Context Economy](context-economy/context-economy.md)
Core source: [ToolFailBench](https://arxiv.org/abs/2607.04686v1)
Implementable now:
- label missed-call, wrong-tool, bad-argument, bad-result-use, and over-tooling failures
- create required-tool tasks whose answers require tool-only values
- create control tasks where tools are present but unnecessary
- record whether the final answer actually used the tool result
Tools, repos, and methodologies worth exploring:
- ToolFailBench-style phase taxonomy, AgentDojo-style fixtures, trace queries over tool exposure, selection, arguments, returns, and final cited values
Implementability score: 0.72

### Data injection turns tool outputs into harness fixtures

Summary: Agent Data Injection attacks the evidence channel. Malicious data can look like normal metadata, field values, labels, or records, then steer an agent without explicit jailbreak instructions. Harnesses should fuzz tool outputs and preserve field trust classes.

Analysis: [daily reasoning analysis](2026-07-07/reasoning.md#data-injection-turns-tool-outputs-into-harness-fixtures)
Durable topics: [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md), [Strategy Untrusted Data Boundaries](../Strategy/untrusted-data-boundaries/untrusted-data-boundaries.md), [Strategy Runtime Governance](../Strategy/runtime-governance/runtime-governance.md)
Core source: [Agent Data Injection](https://arxiv.org/abs/2607.05120v1)
Implementable now:
- split tool responses into trusted metadata, user content, external content, and derived summaries
- fuzz values, identifiers, priorities, deadlines, URLs, recipients, and account references
- require action policies to know which field class justified the action
- log data lineage from tool output to final effect
Tools, repos, and methodologies worth exploring:
- AgentDojo-style attack fixtures, taint tracking for tool responses, schema-level trust classes, policy checks over evidence fields
Implementability score: 0.64

## Supporting recent AgenticAI context

The 2026-07-06 scan made process authority explicit: skills, coding turns, and workspace constraints need process evidence. The 2026-07-07 scan adds the data boundary: before a process can be trusted, the harness has to prove which observations were trusted, masked, quarantined, or merely untrusted evidence.
