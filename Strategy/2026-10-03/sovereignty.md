# Daily Strategy Research: 2026-10-03

## Composition is an authorization boundary

FlowReview supplies a missing rule for multi-agent governance: authority must be checked over the object and action produced by the whole collaboration, not only over each message or worker. A set of individually admissible fragments can jointly reconstruct a protected object and enable a prohibited effect.

The strategic unit is a governed object with four linked properties:
- canonical identity across representations and contributors;
- lineage for every contribution;
- trusted permission bound to the proposed use;
- deterministic enforcement at the final commit boundary.

The paired metric matters as much as the gate. A system that blocks prohibited use by disabling useful collaboration has failed. The test must require both denial of the forbidden effect and completion of the authorized task.

Practical methods worth exploring now:
- freeze the resolved object, permission, action, and target into one release manifest;
- review the union of relevant artifacts before final dispatch;
- keep trusted policy outside contributor-controlled context;
- bind receipts to both the denied effect and the preserved authorized outcome.

Caveat: controlled composition banks establish mechanism, not prevalence in natural production workflows. Representation coverage and permission recovery remain open.

Implementability score: 0.78

Core sources: [Deny Without Disabling](https://arxiv.org/abs/2610.00371v1), [FlowReview](https://github.com/yunbeizhang/FlowReview)

## Baseline selection is a governance decision

False Floors shows that evaluation authority can leak through the comparator. Selecting the best fixed model on evaluation labels grants the baseline information that the router did not receive. Under category shift, that hidden privilege can be as large as the deficit attributed to routing.

The governance rule is simple: benchmark participants and baselines must receive symmetric information. Comparator selection, judge choice, fold construction, and model-pool saturation belong in the signed evaluation contract.

Practical methods worth exploring now:
- select fixed baselines on training or validation folds only;
- hold out request categories and full suites;
- publish both honest and in-sample baseline results;
- preserve fold assignments, judge identity, model pool, and saturation statistics;
- block production routing claims when the evaluated router never switched mid-trajectory.

Caveat: the largest measured effect is concentrated in HELM harm_bench, and automated judges introduce their own bias. The method is immediately useful; the magnitude is not universal.

Implementability score: 0.72

Core source: [False Floors](https://arxiv.org/abs/2610.01535v1)

## Strategic implication

Authorization and evaluation fail for the same reason: the system hides which information was available at the decision boundary. Govern the composed object before execution, and govern the comparator before accepting a routing claim.
