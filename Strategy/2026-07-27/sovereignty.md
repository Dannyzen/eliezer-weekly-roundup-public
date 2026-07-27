# Strategy Daily Sovereignty, 2026-07-27

## Verdict

Agentic routing should use the task as its unit of supervision, but task-level pinning is a hypothesis to shadow, not a default production policy. The paper has strong benchmark deltas, but we found no paper-owned public implementation artifact as of 2026-07-27.

## Scan boundary

The paper was first listed on Monday, 2026-07-27 and submitted as v1 on Friday, 2026-07-24. The PDF was read as a document. No external repository code was cloned or executed, and no paper-owned implementation repository was found.

## Model routing should learn from terminal task outcomes

### What it found

TRACE-ROUTER assigns a task to one model at admission, pins all later LLM calls to that backend, and updates a contextual bandit from terminal reward that combines accuracy and latency. This aligns the routing decision with delayed task-level supervision rather than treating every call as an independent example.

Across three agentic benchmarks, the paper reports non-dominated accuracy-latency points. On tau2-Bench it beats latency-matched interpolation by 7 to 8 accuracy points. On Terminal-Bench it solves 7.1 more tasks than the strongest single-model baseline while reducing latency by 36 percent.

### Why it matters

Per-call routing can misattribute delayed success and mix model behavior inside one trajectory. Task-level admission creates a cleaner policy object: task features, chosen backend, effective model identity, terminal outcome, wall time, cost, and policy update.

### Fit in the stack

This belongs in model-router governance. It changes allocation policy and observability at the gateway, not the agent's internal reasoning loop.

### Implementable now

- start with a static task-class map and uncertainty-based escalation;
- emit one routing receipt with task identity, policy version, selected backend, latency, cost, and terminal reward;
- shadow a contextual bandit before allowing online selection;
- compare task pinning against per-call routing, strong static heuristics, cascades, and stage-aware escalation;
- define failover behavior without silently changing the learning unit.

Implementability score: 0.45

Core source:
- [TRACE-ROUTER](https://arxiv.org/abs/2607.22465v1)

Evidence caveat: production terminal rewards are often sparse, delayed, gameable, or absent. One-model-per-task pinning can preserve a bad admission decision and prevents mid-trajectory escalation unless the policy explicitly allows it. We found no paper-owned public implementation artifact as of 2026-07-27.

## Rejected branch

Claim Plane proposes deterministic ChangeIntent admission for parallel coding agents. Its six-pair mechanism check is too small to estimate semantic-conflict detection, indirect write-set drift, false blocking, or throughput. Existing worktrees, leases, diff-time scope checks, CI, and merge queues remain the cheaper first step.

Source:
- [Claim Plane](https://arxiv.org/abs/2607.21909v1)

## Working conclusion

> Route at the level where outcomes are measured, but do not confuse a clean learning unit with a complete production policy.
