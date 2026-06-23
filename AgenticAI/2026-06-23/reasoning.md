# AgenticAI Daily Analysis - 2026-06-23

Today's strongest implementation signal is that agent evaluation is moving below final-answer grading. The useful systems now ask whether the agent used the right evidence path, followed a disciplined engineering process, and produced a trajectory that can be audited and improved. More tasks and better benchmark scores are not enough if the run path is unverifiable.

## GroundEval makes evidence-path evaluation deterministic

GroundEval attacks a failure mode this repo has been circling for weeks: LLM-as-judge can approve a plausible final answer even when the agent never retrieved the artifact its answer depended on. The paper frames this directly: in one case study, two frontier LLM judges scored a plausible response above 0.85, while GroundEval scored it 0.000 because the trace showed the required evidence was never fetched.

The useful move is deterministic trajectory scoring. GroundEval does not ask another model whether the answer sounds right. It checks what the agent searched, fetched, cited, and was allowed to access, then scores the final answer against that recorded path.

Its three evaluation tracks are especially portable:
- silence: did the agent verify absence before claiming a fact was missing;
- perspective: did the agent restrict itself to evidence available at the relevant time;
- counterfactual: did the agent use the right causal mechanism rather than a plausible alternative.

Why it matters: stateful agents fail in ways final-answer evaluation hides. A response can be polished, cited, and still unsupported by the actual retrieved evidence. GroundEval turns trace provenance into a test surface.

Stack fit: trajectory-aware evaluation, evidence provenance, stateful agent eval, audit logs, deterministic testing.

Implementable now:
- require `source_id`, `raw_output_ref`, `retrieval_time`, and `access_scope` fields in high-risk agent traces;
- write deterministic checks for silence, perspective, and counterfactual tasks before adding judge models;
- fail evaluation when the final answer depends on an artifact that is absent from the trace;
- store per-question diagnostics so engineers can debug evidence-path failures without rereading whole transcripts;
- use LLM judges only after deterministic evidence-path checks pass.

Tools, repos, and methodologies worth exploring:
- JSONL or OpenTelemetry trace exports with stable source IDs;
- rule-based evaluators over search, fetch, citation, and access-control events;
- source-aware claim checking from the evidence-provenance-control-plane work;
- regression suites for absence claims and stale-perspective leakage;
- policy checks that bind evaluation to permitted evidence, not only available evidence.

Implementability score: 0.84

Core source: https://arxiv.org/abs/2606.22737v1

## RigorBench measures how coding agents work, not only whether they pass

RigorBench is useful because it refuses the normal coding-agent shortcut: judging only whether the final patch passes tests. The benchmark scores process discipline across five pillars: Planning Fidelity, Verification Coverage, Recovery Efficiency, Abstention Quality, and Atomic Transition Integrity.

The paper reports a 30-task suite across Plan-Then-Build, Verify-Or-Die, Doom Loop Gauntlet, Know When to Fold, and Don't Break the Build. Its headline result is that structured process discipline improves process quality scores by 41% on average and improves downstream outcome correctness by 17%.

The exact numbers should be treated as early benchmark evidence, not settled law. The durable pattern is stronger than the metric: coding-agent quality has to include planning, verification, recovery, abstention, and step integrity. A reckless agent that eventually passes is not equivalent to one that preserved invariants while getting there.

Why it matters: agent coding systems are increasingly wrapped in harnesses, skills, memory, and subagents. If evaluation only sees the final diff, teams will optimize for lucky commits and miss the operational behaviors that make the agent safe to delegate to.

Stack fit: coding-agent harnesses, process-aware evaluation, trajectory analysis, CI gates, agent skill governance.

Implementable now:
- add process-rubric checks to coding-agent replay suites;
- require an explicit plan before mutation for non-trivial tasks;
- score whether tests or verifiers were run before declaring success;
- detect doom loops, repeated failed fixes, and tool thrashing as first-class failures;
- add an abstention path when context is insufficient or the action is too risky;
- preserve atomic step transitions so reviewers can see what changed after each evidence event.

Tools, repos, and methodologies worth exploring:
- RigorBench-style rubrics;
- trajectory analysis over coding-agent logs;
- pre-mutation plan checks;
- CI fixtures that validate verification behavior, not only final test pass;
- code-review gates for agent-authored diffs with missing evidence.

Implementability score: 0.74

Core source: https://arxiv.org/abs/2606.22678v1

## Watchlist

Managing Procedural Memory in LLM Agents and the AFTER benchmark are worth tracking. The paper reports 382 enterprise tasks, 6 professional roles, 22 procedural skills, and controlled tests for local improvement, cross-task transfer, cross-role transfer, and cross-model generalization. The strongest practical lesson is that skills derived from diverse multi-model traces generalize better than single-model skills, but some procedures remain role-specific.

This did not beat GroundEval or RigorBench today because it is more about skill-memory evaluation than immediate runtime control. It belongs in the next memory-systems pass.

Watchlist source: https://arxiv.org/abs/2606.23127v1
