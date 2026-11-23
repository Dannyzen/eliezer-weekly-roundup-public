# AgenticAI Daily Analysis: 2026-11-23

## Scope

Monday's arXiv listing includes papers submitted on 20 November. This scan inspected the immutable v1 papers and public artifacts read-only. No external repository was cloned, installed, built, imported, or executed.

## 1. Isolate the grader from the agent-controlled test environment

[Who Grades the Agent?](https://arxiv.org/abs/2611.27860v1) treats coding-agent evaluation as adversarial measurement. Its SplitBench design runs candidate code in one environment, extracts bounded observations, and lets a trusted Oracle compare those observations with hidden expected values outside the candidate's control.

The authors converted 180 of 202 tasks from Terminal-Bench and DeepSWE. SplitBench and native graders agreed on 98.7% of agent attempts. In adversarial tests, it rejected 117 of 139 completed limited-knowledge attempts and 126 of 168 completed full-knowledge attempts. The remaining passes mostly exposed weak upstream tests or public answers rather than a bypass of SplitBench's separation mechanism.

Why it matters: a sandbox is insufficient when the grader trusts files, test runners, or reports produced inside that sandbox. The final pass decision needs its own privilege boundary.

Practical implementation:
- run candidate code in a disposable, network-bounded environment;
- export only schema-validated observations from that environment;
- keep expected answers and verdict logic in a separate trusted process;
- treat malformed, missing, oversized, or extra observations as failures;
- replay native and separated grading on a fixed corpus before migration;
- keep candidate, observation, Oracle version, and verdict in one receipt.

Artifact status: the paper says the framework, 180 converted tasks, prompts, attempt records, and recomputation script will be released upon publication. No paper-owned public repository was verified today.

Caveat: SplitBench inherits semantic weakness in upstream tests. At least 34 of 180 converted tasks accepted unsolved work. Privilege separation protects verdict integrity, not specification quality.

Implementability score: 0.68

Core source: [Who Grades the Agent? v1](https://arxiv.org/abs/2611.27860v1)

## 2. Grade recovery by exercised outcomes, not feature labels

[Exercised, Rarely Recovered](https://arxiv.org/abs/2611.27090v1) grades 12 persistent agent runtimes, 26 coding-agent harnesses, and 12 research runtimes across eight recovery mechanisms. The evidence ladder separates documentation, demonstrations, measured evaluation, and operator-attributable real use.

Real-use recovery reports were common, but completed recovery was rare. Of 128 reports, 19 described full recovery, 54 partial recovery, and 45 failure. Checkpoint or resume fully recovered once across 27 reports. Rollback or undo fully recovered once across 15. Research runtimes had benchmark evidence but no reported operation, while compensation of external effects appeared in no harness.

Why it matters: a checkbox for checkpointing, undo, approval, or logs does not establish that damaged work, external effects, and operator trust can be restored. Recovery claims need incident-shaped fixtures and receipts.

Practical implementation:
- define a recovery evidence ladder before collecting examples;
- inject crash, stale lease, partial write, lost reply, and destructive-action faults;
- distinguish resume, repair, rollback, and compensation;
- record recovered, partial, failed, and unclear outcomes separately;
- require operator-attributable evidence for production-readiness claims;
- keep external-effect compensation as a separate acceptance gate.

Artifact status: the 70.9 MB replication package is published on Zenodo with the frozen protocol, archived sources, and coded evidence. It was inspected as a landing page only and was not downloaded or executed.

Caveat: most highest-level reports come from a single operator, and missing public evidence means not found rather than not used. The study is a map of public evidence, not a measured failure rate for the installed population.

Implementability score: 0.92

Core sources: [paper v1](https://arxiv.org/abs/2611.27090v1), [replication package](https://doi.org/10.5281/zenodo.24122560)

## Working conclusion

Agent evaluation and recovery need trusted evidence paths outside the agent's writable environment. Isolate verdict authority, then grade recovery from exercised incidents with explicit outcomes.
