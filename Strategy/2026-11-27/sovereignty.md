# Daily Strategy Analysis: 2026-11-27

## Thesis

Model routing should start with a routeability audit. A router is operational overhead without evidence that the candidate portfolio has prompt-level complementarity and that a learned selector can capture it.

## Audit routeability before building a router

The Routeability Audit Protocol separates theoretical routing headroom from usable routing gains. Its benchmark covers 66 models across GPQA, IFEval, MMLU-Pro, and Omni-MATH, with 2,987 score-matrix rows and frozen 30-seed splits. The study found that similar oracle headroom can produce very different practical results, and that larger embedding sets, dimensionality reduction, abstention, clustering, and stronger regressors did not reliably beat the single best model across datasets. Omni-MATH provided the clearest positive routing evidence.

Why it matters: a portfolio can look diverse while producing ties, correlated errors, or selector signals too weak to exploit. Router accuracy claims are meaningless until the benchmark proves there is enough model complementarity and recoverable signal.

Strategic fit: model-router governance, evaluation design, cost control, and fail-closed deployment.

Practical tools and methods worth exploring now:
- compute single-best-solver versus virtual-best-solver headroom before training a router;
- report tied-best set sizes, regret, gap closure, and selective-routing behavior;
- compare the router against the single best model and simple budget-matched baselines;
- freeze prompt identities and train, calibration, validation, and test splits;
- deploy routing only on workload slices where gains survive portfolio and predictor changes;
- preserve a deterministic fallback to the single best model.

Evidence boundary: RouteabilityBench is a claim-verification artifact for shipped score matrices and statistical checks. The paper says full embedding pipelines and router refits are outside the release scope, so the method is directly adoptable while end-to-end reproduction remains incomplete.

Implementability score: 0.76

Core source: [Routeability Before Routing v1](https://arxiv.org/abs/2611.34825v1)
