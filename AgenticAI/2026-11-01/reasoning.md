# AgenticAI Daily Analysis: 2026-11-01

## Scope

There is no Sunday arXiv listing. These are unreported papers from the Friday, October 30 listing, submitted October 28 or 29. No external repository code was cloned, installed, built, imported, or executed.

## 1. Specialize evidence collection before aggregating a repair

ExploreRepair separates vulnerability diagnosis into three agents that inspect different evidence dimensions, then distills their trajectories and candidate patches before independent aggregators synthesize a final repair. The design matters because security repair under incomplete information is an evidence assembly problem before it is a patch-generation problem.

The paper evaluates 204 vulnerabilities across PatchEval and VulnLoc+. On PatchEval, reported repair success is 39.6% with GPT-5.6-Luna and 71.6% with DeepSeek-V4.1-Flash, improvements of 16.0 and 25.4 percentage points over EvoRepair. VulnLoc+ success is 51.4% and 62.9% for the same models.

Why it matters: parallel agents help when each lane has a distinct evidence contract. Generic duplicate attempts would multiply cost without increasing coverage. The aggregator should receive source-linked observations, attempted patches, execution evidence, and uncertainty rather than prose opinions.

Fit in the stack: multi-agent orchestration, security repair, and evidence-aware aggregation.

Implementable now:
- define orthogonal evidence lanes such as vulnerable location, semantic intent, and executable proof;
- require each lane to return evidence, a candidate patch, and a confidence boundary;
- distill trajectories into a typed evidence bundle before synthesis;
- keep final verification independent of the proposing agents;
- compare the multi-lane system with the best single-agent baseline under the same model and budget.

Evidence caveat: results come from two security-repair benchmarks and model choice has a large effect. No public implementation repository was resolved from the paper during this scan.

Implementability score: 0.72

Core source: https://arxiv.org/abs/2610.39899v1

## 2. Evaluate repairs with the executor that will run them

Repairs for Whom? shows that the value of a trajectory repair depends on the policy that executes the remaining steps. A stronger model, greedy replay, environment oracle, or judge can select a repair that is good for itself and poor for the deployed agent.

With failed trajectories and candidate single-step repairs held fixed, the authors label candidates using independent rollouts of the deployed policy. Greedy replay loses 0.08 to 0.13 expected net success in ALFWorld and 0.06 to 0.13 net reward in WebShop relative to selection with the deployed agent's own rollouts. At equal budget, using Qwen2.5-14B to choose repairs for Qwen2.5-7B loses 0.25 in ALFWorld and 0.07 in WebShop. Similar-sized models from different families also produce bidirectional losses of 0.07 to 0.17.

Why it matters: a repair label is incomplete without model, prompt, history protocol, tool surface, and runtime version. Evaluation with a substitute executor can reorder candidates and change the selected repair location.

Fit in the stack: trajectory evaluation, failure recovery, model routing, and regression testing.

Implementable now:
- bind every repair label to an executor fingerprint;
- use the deployed policy for a small independent rollout sample before promoting a repair;
- compare net gain against keeping the original action, not only post-repair success;
- preserve disagreement cases as executor-specific regression fixtures;
- rerun repair selection after model, prompt, tool, or harness changes.

Evidence caveat: the experiments use ALFWorld and WebShop with specific Qwen and substitute-model configurations. Production transfer still needs domain-specific trials.

Implementability score: 0.86

Core source: https://arxiv.org/abs/2610.38610v1

## Daily conclusion

The shared pattern is evidence specialization with identity-bound judgment. Split exploration by evidence type, then evaluate the proposed intervention with the exact executor and runtime that will inherit it.
