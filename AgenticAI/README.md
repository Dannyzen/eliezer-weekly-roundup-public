# AgenticAI

This index tracks the most recent structured implementation research. Each finding links to the dated analysis, primary sources, practical methods, and an implementability score.

## Latest Structured Update: 2026-10-06

The strongest implementation signal is that agent behavior must remain reviewable and repository policy must be executable across the full trajectory.

### Organize agent behavior into source-linked evidence

Summary: AgentMonBench evaluates consequential-decision identification and evidence localization. EBG builds deterministic behavior graphs so semantic monitors and human reviewers can trace a decision back to source evidence.

Analysis: [daily analysis](2026-10-06/reasoning.md#organize-agent-behavior-into-source-linked-evidence)
Durable topic: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core sources: [paper v1](https://arxiv.org/abs/2610.06406v1), [EBG repository](https://github.com/zhk-lab/EBG), [AgentMonBench dataset](https://huggingface.co/datasets/ZhaoHongKang/AgentMonBench)
Tools and methodologies worth exploring now: source-linked behavior graphs, separate decision and evidence scores, consequential-choice review queues, frozen oversight fixtures
Implementability score: 0.82

### Compile repository policy into executable checks

Summary: SWE-CC turns repository guidance into 823 deterministic checkers across 12 projects and grades both trajectories and final deliverables. Functionally correct patches still violated 43.1% of applicable policies.

Analysis: [daily analysis](2026-10-06/reasoning.md#compile-repository-policy-into-executable-checks)
Durable topic: [Coding Agent Control Plane](coding-agent-control-plane/coding-agent-control-plane.md)
Core sources: [paper v1](https://arxiv.org/abs/2610.06193v1), [SWE-CC repository](https://github.com/dangtruong01/swe-cc-arxiv)
Tools and methodologies worth exploring now: policy compilation, trajectory checkers, not-applicable outcomes, policy-discovery metrics, revision-bound compliance receipts
Implementability score: 0.90

## Current implication

Treat source-linked behavior evidence and repository-local executable policy as separate release inputs. Functional tests alone do not prove that an agent contribution is reviewable or compliant.

Latest roundup: [2026-10-06](../roundups/2026-10-06.md).
