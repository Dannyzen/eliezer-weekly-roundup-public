# AgenticAI

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: 2026-06-04 Daily Scan

### AutoLab moves agent evaluation into long-horizon research and engineering loops
Summary: AutoLab evaluates iterative artifact improvement: propose changes, edit, run experiments, measure results, and continue. That is the right shape for research and engineering agents because single-answer benchmarks hide loop control, measurement, budget, and stopping failures.

Analysis: [daily reasoning analysis](2026-06-04/reasoning.md#autolab-moves-agent-evaluation-into-long-horizon-research-and-engineering-loops)
Durable topic: [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md#june-4-update-long-horizon-re-agents-need-artifact-loop-benchmarks)
Core sources: [AutoLab paper](https://arxiv.org/abs/2606.05080), [AutoLab repository](https://github.com/autolabhq/autolab), [AutoLab project site](https://autolab.moe/)
Implementable now:
- create small internal artifact-loop fixtures;
- require experiment plans, patch IDs, commands, metric deltas, failed attempts, and stopping reasons;
- score improvement per dollar, tool call, and wall-clock minute.
Tools, repos, and methodologies worth exploring:
- AutoLab benchmark design, LangGraph, Temporal, pytest/bench harnesses, OpenTelemetry spans, cost ledgers, artifact diffs
Implementability score: 0.58

### Web-agent skill retrieval should be grounded in live page state
Summary: State-Grounded Dynamic Retrieval retrieves reusable web-agent skills from the current webpage state rather than only the initial task. This is the practical load gate for browser agents whose state changes after navigation, login, UI branching, or errors.

Analysis: [daily reasoning analysis](2026-06-04/reasoning.md#state-grounded-dynamic-retrieval-makes-web-agent-skills-depend-on-the-live-page-not-only-the-task)
Durable topic: [Skills as Control](skills-as-control/skills-as-control.md#june-4-update-web-agent-skill-retrieval-should-be-state-grounded)
Core sources: [State-Grounded Dynamic Retrieval paper](https://arxiv.org/abs/2606.04391), [skill-dynamic-retrieval repository](https://github.com/plusnli/skill-dynamic-retrieval)
Implementable now:
- index skill preconditions by DOM/page state, route, visible controls, auth state, and task class;
- retrieve skills at checkpoints, not only at task start;
- log each load/no-load decision with matching evidence.
Tools, repos, and methodologies worth exploring:
- state fingerprints, DOM snapshots, Playwright traces, browser-agent skills, vector plus rule retrieval, skill failure ledgers
Implementability score: 0.70

### Token budgets need single-spend resource authority
Summary: Token Budgets frames runaway agent spend as a resource-authority failure. Budgets should be delegated once, spent once, expired explicitly, and visible in the same trace as tools, subagents, and retries.

Analysis: [daily reasoning analysis](2026-06-04/reasoning.md#token-budgets-need-single-spend-resource-authority)
Durable topic: [Runtime Governance](../Strategy/runtime-governance/runtime-governance.md#june-4-update-budget-and-workflow-controls-are-becoming-runtime-artifacts)
Core sources: [Token Budgets paper](https://arxiv.org/abs/2606.04056), [token-budgets artifact repository](https://github.com/sajjadanwar0/token-budgets)
Implementable now:
- create per-run, per-step, per-tool, and per-subagent budget leases;
- halt retry loops when child budgets are exhausted;
- test retry storms, orphaned subagents, stale leases, and recursive delegation.
Tools, repos, and methodologies worth exploring:
- budget ledgers, affine/linear-resource design, LiteLLM spend controls, OpenTelemetry cost attributes, Temporal workflow limits
Implementability score: 0.76

## Previous structured update

The prior daily scan for 2026-06-03 focused on skill permission planes, deterministic memory pruning, multi-agent dependency queues, and MCP storage gateways: [2026-06-03 roundup](../roundups/2026-06-03.md).
