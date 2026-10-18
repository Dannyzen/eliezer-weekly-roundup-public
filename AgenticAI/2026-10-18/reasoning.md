# AgenticAI Daily Analysis: 2026-10-18

## Thesis

Today's strongest implementation signal is to grade agents against the real outcome boundary, then use intermediate execution results as explicit learning and control points. Ticket completion and final answers hide whether the agent found the actual requirement, improved the customer's metric, or learned from the experiment that just ran.

## Grade customer outcomes, not ticket completion

FDE-Gym evaluates 95 end-to-end delivery tasks from 20 customer scenarios across 18 sectors. Agents enter production-like systems, question scripted stakeholders, modify the environment, and receive a score based on improvement to the customer's own success metric. In the realistic condition, the best of 13 model configurations reached a mean score of 0.56 and resolved 14 of 95 tasks, where resolution required at least 0.8 business uplift and no incident. Even when the best configuration recovered every key fact on 23 tasks, only 10 reached the 0.8 uplift threshold.

Why it matters: agents can satisfy a written request while solving the wrong problem. Evaluation needs hidden constraints, stakeholder cost, production incidents, and a customer-owned outcome metric.

Stack fit: trajectory-aware evaluation, delivery harnesses, coding-agent control planes, and human-agent collaboration.

Implementable now:
- convert one internal workflow into a hidden-acceptance delivery case;
- score the deployed effect against a baseline and reference result;
- charge for clarification, retries, waiting, and stakeholder contact;
- cap any run that causes an operational incident;
- preserve the brief, stakeholder answers, actions, final state, and grader receipt.

Implementability score: 0.82

Core sources: [FDE-Gym paper v1](https://arxiv.org/abs/2610.22350v1), [public repository](https://github.com/deeplethe/fde-gym), [three open example cases](https://huggingface.co/datasets/DeepLethe/FDE-Gym-examples)

Evidence caveat: the stakeholders are scripted and the full 20-scenario dataset requires manual access approval. The public site is early, and its own documentation warns that shared deployments execute user-written code and need careful isolation. The repository and open examples were inspected read-only; no external code was executed.

## Train on windows between verified experiments

MLExpert treats the decisions between successive experiment results as one execution window and assigns the window a shared outcome reward. Its Windowed Interaction Reinforcement Learning path uses asynchronous collection, policy correction, and feedback filtering so infrastructure failures are excluded rather than mislabeled as model errors. On 22 MLE-Bench Lite competitions, the paper reports that a 35B mixture-of-experts model improved from a 37.9% to a 72.7% medal rate under the MLExpert harness. With Claude Code, the model improved from 42.4% to 69.7% relative to its base model.

Why it matters: one experiment result reflects several preceding decisions. Step-level labels can reward locally plausible actions that produced a bad experiment, while end-of-run rewards arrive too late and mix many unrelated choices.

Stack fit: long-horizon agent training, experiment harnesses, trajectory credit assignment, and autonomous machine learning engineering.

Implementable now:
- segment trajectories at deterministic experiment-result boundaries;
- attach code revision, inputs, metrics, cost, and environment identity to each window;
- filter infrastructure failures from model-quality rewards;
- preserve the best-known candidate and experiment history in a persistent workspace;
- require human review of generated preparation and grading code.

Implementability score: 0.47

Core sources: [MLExpert paper v1](https://arxiv.org/abs/2610.22344v1), [Kaggle-MLE Factory repository](https://github.com/InternScience/MLExpert), [public model weights](https://huggingface.co/InternScience/MLExpert)

Artifact caveat: the model weights are public and ungated, and the repository contains a populated Kaggle task factory. The GitHub repository has no detected top-level license, while the factory subdirectory and model card state Apache 2.0. Running the 35B model and reproducing post-training require substantial multi-GPU and evaluation infrastructure.

## Implementation order

1. Convert one real workflow into a hidden-outcome delivery case.
2. Record deterministic experiment windows and outcome receipts in an existing harness.
3. Compare window-level analysis against step-level and final-only baselines.
4. Consider model training only after the evaluation and provenance path is stable.
