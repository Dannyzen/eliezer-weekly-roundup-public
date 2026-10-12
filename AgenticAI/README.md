# AgenticAI

This index tracks the most recent structured implementation research. Each finding links to the dated analysis, primary sources, practical methods, and an implementability score.

## Latest Structured Update: 2026-10-12 Daily Scan

The current implementation signal is feedback-shaped control. Tool routing should respond to observed reliability, and review effort should respond to change complexity and missing repository context.

### Route tools with execution feedback

Summary: RATED combines semantic retrieval with a contextual bandit updated from execution outcomes. It reduces fault selection from 86.2% to 2.9% under a simulated 30% persistent outage over a 5,172-tool benchmark.

Analysis: [daily analysis](2026-10-12/reasoning.md#rated-route-tools-with-execution-feedback)
Durable topic: [Agent Discovery](agent-discovery/agent-discovery.md)
Core sources: [paper v1](https://arxiv.org/abs/2610.13889v1), [EcoAgent repository](https://github.com/Elliotes/EcoAgent)
Tools and methodologies worth exploring now: invocation outcome ledgers, reliability decay, contextual-bandit reranking, shadow routing, catalog-version receipts
Implementability score: 0.88

### Scale review effort to change complexity

Summary: CRBugBench evaluates 1,800 human-verified bug tasks. The best review agent catches 71.9% within its top five comments, while proprietary and non-local changes remain substantially harder.

Analysis: [daily analysis](2026-10-12/reasoning.md#crbugbench-scale-review-effort-to-change-complexity)
Durable topic: [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md)
Core sources: [paper v1](https://arxiv.org/abs/2610.13668v1), [open-source benchmark subset](https://github.com/malusamayo/CRBugBench)
Tools and methodologies worth exploring now: historical bug mining, complexity-tiered review, repository knowledge retrieval, human escalation, recall by change class
Implementability score: 0.73

## Current implication

Replace static tool rankings and uniform review depth with evidence-sensitive routing. Preserve the evidence and keep high-risk release authority outside the reviewing agent.

Latest roundup: [2026-10-12 daily scan](../roundups/2026-10-12.md).
