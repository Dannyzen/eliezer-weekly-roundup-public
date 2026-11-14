# AgenticAI Daily Analysis: Value, Structure, and Auditability

Date: 2026-11-14

No new Saturday arXiv listing exists. These papers were submitted on November 12 and first listed on Friday, November 13. The selection focuses on patterns that can change an agent harness now.

## 1. Value memory by future work, not retrieval relevance

CoReMem evaluates memory against the next task on the same evolving repository. It compares next-task runs with and without individual trajectory segments, then builds compact memory around repository locations and executable checks. Its 27B actor improved resolve rate from 21.0% to 25.7%, used 17% fewer steps, and used 11% fewer cache-aware tokens than the untrained actor without memory.

Why it matters: memory should earn its storage and context cost through downstream task improvement. Semantic similarity is only a retrieval signal. Repository anchors and executable checks make a memory item useful, inspectable, and testable.

Fit in the stack: coding-agent memory, context economy, and cross-task state continuity.

Implementable now:
- retain canonical trajectories and inherited repository state;
- extract source-linked file locations, commands, checks, and failure conditions;
- run matched next-task trials with and without candidate memory;
- measure resolution, steps, tokens, and memory-module cost together;
- promote only memory that improves held-out work.

Evidence and caveat: the reported gains come from ChainSWE and one adapted actor. The valuation method is more transferable than the exact score. No public implementation artifact was inspected during this run.

Implementability score: 0.78

Core source: [CoReMem v1](https://arxiv.org/abs/2611.17316v1)

## 2. Optimize harness structure, not only prompts and tools

MultiLoop used a coding agent to inspect rollouts, diagnose failures, edit a multi-agent harness, and repeat. With 10 training samples, the evolved harness reached 71.88% accuracy, 4.61 points above the base harness and 3.19 points above the best single-agent system. The improvement came from prompt refinements and one new tool. Delegation and information-sharing failures largely persisted.

Why it matters: a rising task score can hide an unchanged coordination architecture. Self-improvement loops need explicit objectives for delegation quality, information preservation, redundancy, verification loops, and integration cost.

Fit in the stack: multi-agent orchestration, harness self-improvement, and evaluation.

Implementable now:
- freeze a small representative training set and a separate test set;
- retain every harness diff, rollout, score, and failure classification;
- grade structural failures separately from final accuracy;
- require proposed changes to name the coordination mechanism they alter;
- compare against fixed single-agent and equal-budget baselines.

Evidence and caveat: this is one DeepSearchQA case study. The paper demonstrates that automated optimization can improve a harness, while also showing that generic score optimization does not force structural repair. No implementation repository was verified.

Implementability score: 0.72

Core source: [MultiLoop v1](https://arxiv.org/abs/2611.15754v1)

## 3. Audit trajectory risks with paired evidence conditions

ReA-Bench organizes agent auditing into six judgment tiers: safety knowledge, internal contradiction, long-context evidence retrieval, source and reasoning verification, indirect steering, and missing information. It includes hard benign trajectories and paired versions where histories are shortened or missing evidence is supplied. At one threshold, GPT-luna reached 87.0% mean recall while flagging 52.0% of benign samples, and GPT-sol reached 88.5% recall with a 54.0% false-positive rate. Grok-high reached 71.0% recall at 5.5% false positives.

Why it matters: overall recall can reward an auditor that labels almost everything risky. Paired trajectories reveal whether the failure came from missing evidence, retrieval, reasoning, or calibration.

Fit in the stack: runtime observability, safety auditing, and trajectory-aware evaluation.

Implementable now:
- create risky and authorization-valid benign pairs from real traces;
- test full, shortened, and evidence-completed variants;
- report recall at fixed false-positive budgets;
- classify knowledge, contradiction, retrieval, verification, steering, and missing-information failures separately;
- keep synchronous state checks beside asynchronous trajectory review.

Evidence and caveat: the benchmark adapts production and red-team scenarios, but its prevalence and false-positive rates do not estimate production incidence. No public implementation repository was verified.

Implementability score: 0.81

Core source: [ReA-Bench v1](https://arxiv.org/abs/2611.16493v1)

## Working conclusion

The common pattern is prospective proof. Memory should improve the next task, harness edits should repair named coordination failures, and auditors should distinguish missing evidence from unsafe behavior. Final task success is too coarse for all three decisions.
