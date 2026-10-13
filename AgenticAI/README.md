# AgenticAI

This index tracks the most recent structured implementation research. Each finding links to the dated analysis, primary sources, practical methods, and an implementability score.

## Latest Structured Update: 2026-10-13 Daily Scan

The current implementation signal is explicit verification state. Long-horizon agents need source-linked evidence and open gaps outside the transcript, while coding agents need test adequacy measured against requirement-targeted failures.

### Separate evidence, conclusions, and unresolved gaps

Summary: LongHarness keeps active evidence, evolving conclusions, and open information gaps as distinct runtime state. On OfficeQA Pro V2, removing persistent states reduces exact match by 7.8 points and removing evidence-conclusion coevolution reduces it by 9.4 points.

Analysis: [daily analysis](2026-10-13/reasoning.md#longharness-separate-evidence-conclusions-and-unresolved-gaps)
Durable topic: [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md)
Core source: [LongHarness paper v1](https://arxiv.org/abs/2610.13075v1)
Tools and methodologies worth exploring now: typed evidence records, active or inactive status, conclusion-to-evidence links, unresolved-gap search, citation validation, retrieval-adoption-transformation metrics
Implementability score: 0.66

### Grade tests against requirement-targeted mutants

Summary: TestSuiteBench covers 165 applications and shows that frontier agents generate mostly valid tests while remaining below 60% mutation score. The public MIT artifact includes a populated benchmark tree and three Hugging Face datasets.

Analysis: [daily analysis](2026-10-13/reasoning.md#testsuitebench-grade-test-adequacy-against-requirement-targeted-mutants)
Durable topic: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core sources: [paper v1](https://arxiv.org/abs/2610.13065v1), [repository](https://github.com/eth-sri/testsuitebench), [datasets](https://huggingface.co/collections/eth-sri/testsuitebench)
Tools and methodologies worth exploring now: requirement-targeted mutation, independent wrong implementations, validity versus adequacy scoring, frozen hidden mutant sets, surviving-mutant review
Implementability score: 0.87

## Current implication

Move verification state out of prose. Evidence needs lifecycle state and source identity, while tests need independent wrong implementations that prove behavioral discrimination.

Latest roundup: [2026-10-13 daily scan](../roundups/2026-10-13.md).
