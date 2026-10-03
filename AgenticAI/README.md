# AgenticAI

This index tracks the most recent structured implementation research. Each finding links to the dated analysis, primary sources, practical methods, and an implementability score.

## Latest Structured Update: 2026-10-03

Saturday's strongest signal is that agent reliability depends on the correct evaluation and recovery unit. Review the object composed by the team, select routing baselines without test-label privilege, make review callable from the workflow, and persist enough execution state to resume interrupted turns safely.

### Review the composed object

Summary: separately admissible fragments can jointly enable a prohibited use. FlowReview reduced denied commits from 413 of 480 under local review to 0 of 480 under combined-artifact review, while preserving authorized supply at 459 of 480.

Analysis: [daily analysis](2026-10-03/reasoning.md#review-the-composed-object)
Durable topics: [Multi-Agent Orchestration](multi-agent-orchestration/multi-agent-orchestration.md), [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md)
Core sources: [paper](https://arxiv.org/abs/2610.00371v1), [FlowReview](https://github.com/yunbeizhang/FlowReview)
Tools and methodologies worth exploring now: governed-object identity, authorization-paired evaluation, isolated permission ranking, runtime assembly, deterministic commit gates
Implementability score: 0.78

### Use held-out baselines for safety routing

Summary: a best-single-model baseline chosen on test labels creates a false floor under distribution shift. Select the comparator inside each fold and report category-held-out performance.

Analysis: [daily analysis](2026-10-03/reasoning.md#use-held-out-baselines-for-safety-routing)
Durable topics: [Trajectory-Aware Evaluation](trajectory-aware-evaluation/trajectory-aware-evaluation.md), [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md)
Core source: [False Floors](https://arxiv.org/abs/2610.01535v1)
Tools and methodologies worth exploring now: nested baseline selection, held-out categories, suite holdouts, judge-sensitivity checks, branching rollouts
Implementability score: 0.72

### Trigger code review through the API

Summary: GitHub's REST and GraphQL APIs can now request Copilot code review and set effort per request. This turns review into a callable workflow stage.

Analysis: [daily analysis](2026-10-03/reasoning.md#trigger-code-review-through-the-api)
Durable topic: [Coding Agent Control Plane](coding-agent-control-plane/coding-agent-control-plane.md)
Core source: [GitHub changelog](https://github.blog/changelog/2026-10-02-copilot-code-review-api-support-and-new-default-effort-level/)
Tools and methodologies worth exploring now: risk-based review effort, API-triggered review, review receipts, deterministic merge gates
Implementability score: 0.94

### Make long turns restart-safe

Summary: Cloudflare PiHarness binds Pi Durable to Durable Object lifecycle persistence so long-running work can survive interruption. Adoption still needs explicit replay-safety and recovery tests.

Analysis: [daily analysis](2026-10-03/reasoning.md#make-long-turns-restart-safe)
Durable topic: [Sessionful Agent Loops](sessionful-agent-loops/sessionful-agent-loops.md)
Core source: [Cloudflare changelog](https://developers.cloudflare.com/changelog/post/2026-10-02-pi-harness/)
Tools and methodologies worth exploring now: PiHarness, Durable Objects, resume cursors, replay-safe tool classes, interruption fixtures
Implementability score: 0.86

## Current implication

Use the right system boundary. Compose artifacts before authorization, choose baselines without hidden label access, call review from the workflow, and prove that durable turns recover without duplicating side effects.

Latest roundup: [2026-10-03](../roundups/2026-10-03.md).
