# AgenticAI

Implementation analysis for agent evaluation, memory, context policy, tools, model routing, and orchestration.

## Latest Structured Update: 2026-10-18 Daily Scan

### Grade customer outcomes, not ticket completion

Summary: Delivery agents should be scored on customer uplift, incidents, hidden constraints, and stakeholder cost rather than whether they completed the written request.

Analysis: [grade customer outcomes, not ticket completion](2026-10-18/reasoning.md#grade-customer-outcomes-not-ticket-completion)

Core sources: [FDE-Gym paper v1](https://arxiv.org/abs/2610.22350v1), [repository](https://github.com/deeplethe/fde-gym), [open examples](https://huggingface.co/datasets/DeepLethe/FDE-Gym-examples)

Implementable now:
- convert one workflow into a hidden-acceptance case;
- grade business uplift and cap incidents;
- charge for clarification, retries, waiting, and stakeholder contact;
- preserve a complete evidence receipt.

Implementability score: 0.82

### Train on windows between verified experiments

Summary: Group the decisions between deterministic experiment results into one learning window, then separate infrastructure failures from model errors.

Analysis: [train on windows between verified experiments](2026-10-18/reasoning.md#train-on-windows-between-verified-experiments)

Core sources: [MLExpert paper v1](https://arxiv.org/abs/2610.22344v1), [repository](https://github.com/InternScience/MLExpert), [model](https://huggingface.co/InternScience/MLExpert)

Implementable now:
- segment trajectories at experiment-result boundaries;
- attach code, inputs, metrics, cost, and environment identity;
- filter infrastructure failures;
- retain a persistent best-candidate workspace.

Implementability score: 0.47

## Current implication

Agent harnesses need two proof layers: an outcome layer showing whether the delivered system improved the target metric, and an execution layer showing which bounded decision window produced each measured result.
