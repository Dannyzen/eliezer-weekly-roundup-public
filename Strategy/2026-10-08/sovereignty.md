# Daily Strategy Analysis: 2026-10-08

## Thesis

The control plane should own time, delegation, skill admission, and memory lineage. Models can propose estimates, sub-agents, skills, and learned relations. Runtime contracts decide what becomes authority.

## Treat time budgets as runtime contracts

AgentTime shows large differences in duration following across native agent harnesses. A model can finish early, overrun, or sleep after apparent completion while still satisfying a superficial wall-clock target.

Strategic implication: the scheduler owns deadline, cancellation, active-work accounting, checkpoint cadence, and completion evidence. Model forecasts are advisory inputs. The runtime should compare requested duration, actual active work, task quality, and resource use.

Implementability score: 0.90

Sources: [paper v1](https://arxiv.org/abs/2610.09944v1), [repository](https://github.com/michaelofengenden/agenttimebench)

## Make concurrency an earned execution mode

Dynamic sub-agent execution increased mean runtime in 14 of 15 agent-benchmark combinations and produced sharply different results by task horizon. It helped some large decomposable tasks and harmed bounded ones.

Strategic implication: concurrency needs an admission rule based on independence, shared-state risk, expected integration cost, and available verification. Each lane needs ownership, a deadline, a result contract, and a parent-owned cumulative gate.

Implementability score: 0.86

Sources: [paper v1](https://arxiv.org/abs/2610.10263v1), [trajectory artifact](https://github.com/schwerli/Concurrency-Failures-Trajectory-Artifact)

## Require admission evidence before skill reuse

SkillSandbox demonstrates that many skills remain unexercised even after hundreds of downstream tasks. Waiting for organic reuse leaves harmful or overfit procedures in the library without evidence.

Strategic implication: skill admission should be a release process. Require a versioned claim, synthesized novel scenarios, paired execution evidence, boundary tests, and a reversible Keep or Reject decision.

Implementability score: 0.74

Sources: [paper v1](https://arxiv.org/abs/2610.10088v1), [implementation snapshot](https://anonymous.4open.science/r/skillsandbox-647C/)

## Bind learned memory to source artifacts

ExperienceIndex improves retrieval and cost by storing experience against stable artifact identities and relations between artifacts.

Strategic implication: memory entries should carry source ID, source version, derivation task, confidence, supersession state, and retrieval evidence. A memory write without source lineage should remain advisory and should never silently override current source material.

Implementability score: 0.65

Source: [paper v1](https://arxiv.org/abs/2610.10091v1)

## Current decision

Build the runtime around external contracts: scheduler-owned time, selective delegation, evidence-gated skill admission, and origin-bound memory. The model supplies proposals. Receipts and policy gates decide what persists or executes.
