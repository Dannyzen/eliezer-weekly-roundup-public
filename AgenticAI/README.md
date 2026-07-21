# AgenticAI

This index tracks the most recent structured update. Each finding includes a summary, a link into the detailed analysis, core sources, practical implementation paths, and an implementability score from 0 to 1.

## Most Recent Structured Update: Tuesday, 2026-07-21

### Agentic pull requests need diff-coverage gates

Summary: passing tests do not prove that an agent tested its own change. In the analyzed coverage subset, existing tests exercised only 27.0% of changed Python lines, and 64.8% of Python pull requests had no changed line executed.

Analysis: [daily reasoning analysis](2026-07-21/reasoning.md#agentic-pull-requests-need-diff-coverage-gates)
Durable topic: [Coding Agent Control Plane](coding-agent-control-plane/coding-agent-control-plane.md#july-21-update-passing-tests-do-not-prove-an-agent-tested-its-diff)
Core sources: [paper](https://arxiv.org/abs/2607.18057v1), [replication repository](https://github.com/SageSELab/Agentic-Pull-Request-Test-Coverage), [Zenodo 1.0.0](https://doi.org/10.5281/zenodo.21419686)
Implementable now:
- map coverage to changed executable lines, not only project totals;
- distinguish coverage from existing tests and agent-written tests;
- gate uncovered error-handling, auth, persistence, and side-effect code;
- add mutation or assertion-quality checks after the first diff-coverage gate.
Tools, repositories, and methodologies:
- `pytest-cov`, coverage.py, JaCoCo, diff-cover, tree-sitter, srcML, the SageSELab replication package
Implementability score: 0.91

### Verify-repair loops need calibrated stopping and a guarded fallback

Summary: verifier acceptance can rise while true validity falls. Stop on estimated marginal gain, and retain the incumbent when verifier discrimination or calibration collapses.

Analysis: [daily reasoning analysis](2026-07-21/reasoning.md#verify-repair-loops-need-calibrated-stopping-and-a-guarded-fallback)
Durable topic: [Sessionful Agent Loops](sessionful-agent-loops/sessionful-agent-loops.md#july-21-update-verify-repair-loops-need-calibrated-stop-and-guarded-fallback)
Core sources: [paper](https://arxiv.org/abs/2607.17641v1), [VRR-Stop artifact](https://anonymous.4open.science/r/vrr-artifact-2583)
Implementable now:
- replay full repair trajectories before changing production policy;
- estimate repair benefit and repair damage separately;
- track verifier discrimination and decision margin;
- switch to incumbent retention under calibration failure or distribution shift.
Tools, repositories, and methodologies:
- VRR-Stop artifact, cross-fitting, frozen-trajectory replay, bootstrap intervals, calibration-health alerts
Implementability score: 0.67

## Current implication

An agent loop needs evidence that its work changed the right state and evidence that another iteration is still beneficial. Coverage gates control coding exits. Calibrated stop policies control iterative exits.
