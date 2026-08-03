# AgenticAI

This index tracks the most recent structured research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-08-02

### Benchmark tasks need issue-to-oracle alignment proof

Summary: PAIChecker finds that 13.6 percent of SWE-bench Verified instances contain PR-issue misalignment. Its pattern analysis, cross-agent synthesis, and code validation make benchmark admission a checked process rather than a link heuristic.

Analysis: [daily analysis](2026-08-02/reasoning.md#benchmark-construction-needs-an-oracle-alignment-gate)
Core sources: [PAIChecker paper](https://arxiv.org/abs/2607.28587v1), [MIT repository](https://github.com/manyifire/PAIChecker)
Implementable now:
- validate issue, PR, base revision, patch, tests, and discussion as one task manifest;
- reject or adjudicate bundled, follow-up, unrelated, or under-specified pairs;
- keep code validation and maintainer response beside model labels.
Tools, repositories, and methodologies:
- PAIChecker, SWE-bench manifests, code-level validation, maintainer adjudication
Implementability score: 0.84

### Local computer-use agents need selective compute

Summary: one to four recent screenshots stabilize local CUAs, but longer histories, more steps, planner-grounder decomposition, and parallel plans quickly hit diminishing returns or change stalls into false success.

Analysis: [daily analysis](2026-08-02/reasoning.md#local-computer-use-agents-need-selective-compute-not-longer-loops)
Core source: [local CUA scaling study](https://arxiv.org/abs/2607.28573v1)
Implementable now:
- keep compact recent state with source-labeled screenshots;
- detect loops, no progress, format failure, and false completion separately;
- gate success on environment state and escalate only after measured plateau.
Tools, repositories, and methodologies:
- OSWorld-style sandboxes, state hashes, progress monitors, deterministic completion checks, vLLM accounting
Implementability score: 0.76

## Current implication

Agent evaluation needs two preconditions before scores matter: the task must match its oracle, and compute must be allocated against observed failure modes rather than added blindly.
