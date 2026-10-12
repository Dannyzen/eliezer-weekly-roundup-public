# Daily AgenticAI Research: 2026-10-12

## Scope

This scan covers the arXiv batch first listed on Monday, October 12, 2026. Every selected paper is an immutable v1 submitted on Friday, October 9, 2026. Hugging Face, GitHub Changelog, OpenAI, and fresh GitHub repository surfaces produced no stronger non-duplicate finding inside the same operational window.

External repositories were inspected through GitHub metadata, trees, and README files only. No external source code was cloned, installed, built, imported, or executed.

## Thesis

Agent reliability needs two feedback loops: execution outcomes should change future tool selection, and review coverage should increase with change complexity and missing project context.

## RATED: route tools with execution feedback

RATED separates semantic matching from reliability adaptation. A frozen dual encoder retrieves relevant candidates, then a discounted contextual bandit reranks them from recent execution outcomes.

The EcoAgent benchmark contains 5,172 tools and more than 210,000 query-tool pairs. RATED reports a 52.2% relative MRR improvement over the ToolLLM API retriever on real queries. Under a simulated persistent outage affecting 30% of tools, it reduces fault selection from 86.2% to 2.9% while adding 0.172 ms over encode-only inference.

### Why it matters

Static retrieval assumes the catalog describes current reality. Agent runtimes know more: authentication fails, schemas drift, endpoints disappear, and providers degrade. Reliability should therefore be an observed, time-sensitive routing signal rather than a static metadata field.

### Stack fit

- Agent discovery and tool retrieval
- Runtime routing
- Outcome ledgers
- Reliability-aware gateways

### Practical methods worth exploring

- Log tool identity, catalog version, result class, latency, and retry outcome for every invocation.
- Keep semantic relevance and operational reliability as separate features.
- Decay old reliability evidence so recovered tools can re-enter the candidate set.
- Shadow a bandit reranker against the current static ranker before online promotion.
- Preserve cold-start and never-tried states instead of treating them as failures.

### Evidence and caveat

The public [EcoAgent repository](https://github.com/Elliotes/EcoAgent) has a populated 44-path tree, benchmark data, training and evaluation scripts, and a license file described as Apache 2.0. The paper evaluates injected persistent outages over a simulated execution stream. Live-agent validation and cold-start behavior for newly added tools remain future work.

Implementability score: **0.88**

Core sources:
- [RATED paper v1](https://arxiv.org/abs/2610.13889v1)
- [EcoAgent repository](https://github.com/Elliotes/EcoAgent)

Duplicate status: thematic extension of earlier agent-discovery and model-routing work. The new control layer is execution-derived tool reliability.

## CRBugBench: scale review effort to change complexity

CRBugBench evaluates bug-detection review agents on 1,000 tasks from 98 open-source repositories and 800 additional tasks from two proprietary industry repositories. The best reported configuration catches 71.9% of known bugs within its top five comments, up from 47.7% for an earlier model configuration. Performance drops by as much as 25.5% on proprietary tasks where project context and non-local reasoning matter more.

Exploration-nudging prompts improve detection by up to 5.8% at 10% higher cost. The study finds comprehensive prompts more cost-effective than multi-agent review configurations.

### Why it matters

Automated review is useful now, but its miss rate is still too high for unattended release. The practical control is selective escalation: spend more review effort on complex diffs, changes with non-local dependencies, and repositories where relevant knowledge is absent from the review context.

### Stack fit

- Coding-agent harnesses
- Regression and review gates
- Context retrieval
- Human escalation

### Practical methods worth exploring

- Grade detection against human-verified historical bugs rather than synthetic style issues.
- Route low-complexity changes through one review pass and escalate high-complexity changes.
- Retrieve repository policy, incidents, dependency context, and prior review findings before review.
- Track recall by repository, change class, dependency span, and model or harness version.
- Keep human review on changes where missing context or non-local effects dominate.

### Evidence and caveat

The authors cannot publish the full replication package. The paper links a public [CRBugBench repository](https://github.com/malusamayo/CRBugBench) with 995 open-source Harbor-format tasks across 98 repositories. Its recursive tree is populated, but GitHub reports no license. A full run is operationally heavy: the README estimates about 650 GB for all task builds and requires model-backed judge panels.

Implementability score: **0.73**

Core sources:
- [CRBugBench paper v1](https://arxiv.org/abs/2610.13668v1)
- [CRBugBench repository](https://github.com/malusamayo/CRBugBench)

Duplicate status: extension of prior test and trajectory evaluation work. This finding measures review recall against historical production bugs and exposes where human oversight remains necessary.

## Working conclusion

Treat tool reliability as live routing state and code review as risk-priced coverage. Static catalogs and uniform review depth both discard operational evidence that the runtime already has.
