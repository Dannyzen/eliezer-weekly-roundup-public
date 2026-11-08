# AgenticAI Daily Analysis: 2026-11-08

No new arXiv listing appeared on Sunday. These are Friday carry-forwards submitted November 5 and first listed November 6. The strongest unreported implementation findings concern failure classification and migration tests that catch plausible wrong behavior.

## 1. Separate hard issues, weak models, and bad runs

Trajectory-based monitors promise to stop, retry, or reroute failing coding-agent runs. The new study asks whether they detect run-specific failure or merely rediscover which issues are hard and which models are weak.

On public SWE-bench Verified trajectories, a run-independent issue-difficulty score reached 0.92 AUROC, while trajectory predictors reached about 0.62. Within an issue, model identity predicted failure better than the tested trajectory predictors. After controlling for issue and model, the trajectory contribution was statistically equivalent to zero. A repeated-run pilot showed real run variance, but the current predictors could not distinguish a retryable bad run from a task beyond the model's ability.

Why it matters: a high failure-prediction score can justify the wrong intervention. Retrying helps stochastic run failures. Switching models may help capability failures. Stopping saves cost only when the classifier knows which failure class it sees.

Stack fit: trajectory evaluation, model routing, retry policy, and coding-agent observability.

Implementable now:
- collect repeated attempts for the same issue and model;
- report issue-only, model-only, and trajectory-aware baselines;
- label failure cause before evaluating stop, retry, or switch policies;
- compare interventions under equal budgets and on held-out runs;
- retain outcome variance instead of collapsing each issue-model pair to one attempt.

Evidence caveat: the paper is a five-page study built from public SWE-bench trajectories plus a repeated-run pilot. It challenges current evaluation design more strongly than it validates a replacement predictor.

Implementability score: 0.84

Core source: [Hard Issue, Weak Model, or Bad Run?](https://arxiv.org/abs/2611.08285v1)

## 2. Derive migration tests from changed contracts

Accepted but Wrong tests 73 tasks spanning 60 documented changes in CPython, Node.js, and SQLite. Typical-input assertions released 41.0 percent of wrong repairs. Adding one edge input derived from the release note cut the wrong-release rate to 6.5 percent overall and 6.1 percent on 15 unseen clusters. Three inputs from a blind GPT-5.6-luna writer reached 7.0 percent. Under harder distractor menus, 15.3 to 16.8 percent of wrong programs still passed, so the gate improved sharply without becoming sufficient.

Why it matters: migration failures are often semantically valid calls with changed effects. Generic tests and self-tests tend to confirm the old behavior. Release notes and changed contracts identify the edge where compatibility actually broke.

Stack fit: code-repair harnesses, upgrade gates, oracle design, and release evidence.

Implementable now:
- parse each dependency or runtime change into a before-and-after contract;
- generate at least one edge input from the changed clause before accepting a repair;
- run candidates on the real old and new runtimes when differential behavior is available;
- keep hidden contract checks independent from the repair model;
- archive the release note, input, expected effect, runtime versions, and verdict as one receipt.

Evidence caveat: the task bank is finite, model-written self-tests were weaker, and artifacts are available from the authors on request rather than through a verified public repository.

Implementability score: 0.87

Core source: [Accepted but Wrong](https://arxiv.org/abs/2611.08269v1)

## Working conclusion

Agent operations should classify failure causes before changing policy, and release gates should derive tests from the contract that changed. A trajectory score without a causal baseline and a passing migration test without an edge contract both create false confidence.
