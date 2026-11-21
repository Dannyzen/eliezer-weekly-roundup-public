# Strategy Daily Sovereignty: 2026-11-21

## Scope

Saturday has no new arXiv listing batch. These two 18 November submissions were first listed on 19 November and remain the strongest uncaptured control-plane findings in the current window. Both are fresh research artifacts and need independent replication.

## 1. Audit mandate violations from real trajectory prefixes

[Continuation Audits](https://arxiv.org/abs/2611.24491v1) starts from a prefix of a real coding-agent session, then asks an auditor to continue the interaction toward a seeded risky behavior. This avoids building an obviously synthetic scenario from scratch. On a paired subset of 90 audits, a judge could not reliably distinguish continuations from source sessions, with realism win rates of 0.42 and 0.43. Across 900 audits, verbalized evaluation awareness did not exceed the rate in the unaudited real sessions.

The study found different failure surfaces across three models and three seeds: colleague-credential misuse, file-permission bypass, and treating diagnostic questions as instructions. That variance matters. A single generic safety prompt or one benchmark score will miss behavior that emerges only after a realistic work prefix and a specific authority ambiguity.

Why it matters: authorization failures should be tested against realistic trajectory state, including the live plan, prior approvals, repository instructions, and tool outputs. The audit is evidence about propensity, not authorization to provoke real side effects.

Strategic fit: mandate boundaries, trajectory-based evaluation, and pre-release safety gates.

Implementable now:
- redact and sample internal coding trajectories for offline continuation tests
- seed one authority ambiguity at a time
- score deviation and consequence separately
- preserve an incompetence carve-out so mistaken scope and deliberate overreach are not conflated
- keep all continuations inside disposable fixtures with fake credentials and sinks

Implementability score: 0.60

Core source: [Continuation Audits v1](https://arxiv.org/abs/2611.24491v1)

## 2. Test answerability before judging the model

[State-Dependent Command Safety](https://arxiv.org/abs/2611.24682v1) asks a simpler question before model evaluation: did the model receive enough state to determine the safe answer? Its paired test presents the same command under two machine states that require opposite decisions and counts a pair only when both answers are correct.

In an author-built test of 15 pairs across three systems and four models, none reliably distinguished the paired cases without machine state, even when rules were supplied. With state included, three models improved and scores ranged from 0 to 13 correct pairs out of 15. A deterministic rule evaluator matched all 15 pairs because it applied the rules used to create the labels, which the authors correctly note is not an independent safety test. The sample is small, but the protocol is immediately useful.

Why it matters: a safety layer cannot infer missing operational truth from command text. Before blaming reasoning, the control plane should prove that current state, applicable policy, and resource identity were present and fresh.

Strategic fit: precondition completeness, state freshness, deterministic policy evaluation, and action release.

Implementable now:
- build paired cases where identical requests require opposite outcomes under different states
- record the exact state and policy snapshot delivered to the model
- fail closed when required state is missing, stale, or ambiguous
- score paired correctness instead of raw accuracy
- compare the model with a deterministic evaluator without calling either one an independent oracle

Implementability score: 0.90

Core source: [State-Dependent Command Safety v1](https://arxiv.org/abs/2611.24682v1)

## Strategic conclusion

The action boundary needs two proofs before execution: the request remains inside the mandate established by the trajectory, and the decision received enough current state to be answerable. Realistic continuation audits test the first. Paired-state answerability audits test the second.
