
# Agent Self-Improvement Governance

## Thesis

Self-improvement is a deployment pipeline, not an introspection feature. An agent may propose a diagnosis, prompt change, new skill, guardrail, memory rule, workflow, or code edit. The runtime must decide whether the failure is real, whether the candidate generalizes, whether authority expands, and whether the change can be rolled back.

The governing rule is simple: no verified failure, no optimization target; no regression and transfer proof, no promotion.

## Why this is a separate control plane

A model can be persuasive at every stage while being wrong about the underlying event. Two recent results show the distinct risks:

- Phantom Guardrails found 15 fabricated violations in 60 patterned legal runs and none in 60 featureless legal controls. The proposer added a rule for a failure the byte-exact oracle disproved.
- Do Agent Optimizers Compound? found that all three tested methods improved in a static first phase, but only the regression-controlled method transferred positively and kept improving after new tasks arrived.

OpenAI's GPT-Red adds the production pattern: automated attackers operate in explicit threat-model environments, are evaluated on held-out scenarios and live-agent transfers, and remain separated from deployed models. The method is useful, but the closed model and large training budget are not reproducible evidence for a normal team.

## Canonical improvement object

Every proposed improvement should carry:

- change ID and parent version;
- failure claim and affected behavior;
- source trace, environment, model, harness, task, and policy versions;
- oracle type, oracle result, and confidence;
- negative control where the correct action is no change;
- candidate artifact or diff;
- authority delta, including tools, data, network, credentials, memory, and execution scope;
- old-task regression results;
- unseen-task transfer results;
- second-round or repeated-application result;
- cost, latency, and operator burden delta;
- reviewer decision, expiry, canary scope, rollback handle, and final promotion receipt.

## Promotion sequence

1. Observe the suspected failure with full trace and environment evidence.
2. Admit it only after a deterministic or source-owned oracle confirms the claim.
3. Propose a versioned, reversible candidate against one declared failure class.
4. Replay the source failure plus legal no-change controls.
5. Transfer the candidate to old regressions, unseen tasks, and a repeated optimization phase.
6. Promote through approval, canary scope, expiry, and automatic rollback thresholds.
7. Monitor outcomes and retire rules that add no verified value.

## What to reject

Reject a candidate when:

- the failure cannot be reproduced;
- the proposer cites evidence the oracle refutes;
- a suppression metric improves without changing a true outcome;
- old tasks regress or unseen-task transfer falls below baseline;
- the candidate expands authority without explicit review;
- the change cannot be isolated, versioned, or rolled back;
- the same model both proposes and solely verifies a high-impact change.

## Practical first implementation

Start with one mutable surface, preferably a prompt or skill version rather than arbitrary code.

- keep a fixed regression pack and a held-out transfer pack;
- require source trace plus deterministic verifier for every admitted failure;
- include examples where the right answer is no change;
- store candidate versions beside exact eval results;
- canary the winning candidate under narrower authority than production;
- auto-rollback on safety, correctness, cost, or latency regression.

Useful tools and methods:
- event-sourced run records;
- Beads, Git, or another append-only change ledger;
- Terminal-Bench or domain-specific executable task packs;
- deterministic counterfactual micro-labs;
- shadow traffic, canary promotion, policy diffs, signed approvals, and rollback automation.

## Implementability

Implementability score: 0.68

The first governance loop is buildable with current version control, eval harnesses, policy checks, and canary infrastructure. The hard part is oracle quality and realistic transfer coverage. A weak oracle turns the entire loop into automated confirmation bias.

## Core sources

- Do Agent Optimizers Compound? A Continual-Learning Evaluation on Terminal-Bench 2.0: https://arxiv.org/abs/2607.14004v1
- Experiment artifacts: https://github.com/relai-ai/Continual-Learning-Terminal-Bench
- Phantom Guardrails: https://arxiv.org/abs/2607.13083v1
- GPT-Red: https://openai.com/index/unlocking-self-improvement-gpt-red/
