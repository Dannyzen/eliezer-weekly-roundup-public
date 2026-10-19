# AgenticAI

Implementation analysis for agent evaluation, memory, context policy, tools, model routing, and orchestration.

## Latest Structured Update: 2026-10-19 Daily Scan

### Recommend tools behind a scoped gateway

Summary: Replace static tool catalogs with a fixed discovery and execution interface that recommends only inside the principal's eligible scope.

Analysis: [recommend tools behind a scoped gateway](2026-10-19/reasoning.md#recommend-tools-behind-a-scoped-gateway)

Core source: [Tool Recommendation for Multi-Step Agents v1](https://arxiv.org/abs/2610.23707v1)

Implementable now:
- expose fixed select, execute, and list interfaces;
- retrieve only from policy-eligible tools;
- rerank ambiguous candidates;
- measure complete required-tool coverage, tokens, cost, and outcome.

Implementability score: 0.82

### Hold harness budgets fixed before blaming the model

Summary: Agent benchmarks must freeze menus, token caps, call limits, turn limits, and result encoding before attributing a failure to the model.

Analysis: [hold harness budgets fixed before blaming the model](2026-10-19/reasoning.md#hold-harness-budgets-fixed-before-blaming-the-model)

Core sources: [ToolBottleneckBench paper v1](https://arxiv.org/abs/2610.21098v1), [MIT repository](https://github.com/zichuanxu/tool-bottleneck-bench)

Implementable now:
- compile matched pressure variants;
- record first unmet obligation and terminal limit;
- sweep completion caps before drawing model conclusions;
- compare harness repairs against model switches.

Implementability score: 0.86

### Store situational insights instead of next-tool prescriptions

Summary: Tool-transition graphs rarely justified their inference cost; source-linked natural-language insights were the stronger memory form.

Analysis: [store situational insights instead of next-tool prescriptions](2026-10-19/reasoning.md#store-situational-insights-instead-of-next-tool-prescriptions)

Core source: [Rethinking the Role of Tool Graph Memory v1](https://arxiv.org/abs/2610.21571v1)

Implementable now:
- keep raw episodes canonical;
- distill situation, action, outcome, and failure insights;
- retrieve insights as soft priors;
- retain no-memory, random-guidance, and extra-compute controls.

Implementability score: 0.74

### Gate proactive memory on interruption value and timing

Summary: Relevant memory is insufficient for proactive assistance; the harness needs a separate gate for whether the current moment warrants interruption.

Analysis: [gate proactive memory on interruption value and timing](2026-10-19/reasoning.md#gate-proactive-memory-on-interruption-value-and-timing)

Core source: [ProPerAgent v1](https://arxiv.org/abs/2610.22671v1)

Implementable now:
- annotate trigger windows and required silence;
- grade retrieval, timing, content, early firing, and repeats separately;
- bind alerts to memory evidence and observed triggers;
- keep proactive actions read-only until separately authorized.

Implementability score: 0.45

## Current implication

The agent stack needs selection systems that preserve source, scope, budget, and authority. Tool discovery, memory retrieval, and evaluation diagnostics should narrow choices without silently granting execution or attention rights.
