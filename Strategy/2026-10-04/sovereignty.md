# Strategy Daily Analysis: 2026-10-04

## Scope note

Sunday has no new arXiv listing. The selected signals combine an October 3 public implementation release with non-duplicate papers from the Friday, October 2 batch. The strategic cut is about who controls truth, authority, and data movement inside an agent workflow.

## Terminal state is the reliability contract

ThinkingBox shows why business workflows need executable state contracts. A plausible answer and valid tool calls can still leave the database wrong. Across 507 workflows repeated 20 times, the strongest reported model fell from 65.36% pass@1 to 25.25% pass^20.

The control-plane implication is direct: completion authority belongs to an engine-owned state verifier, not the model's final sentence. The verifier should evaluate required effects, forbidden effects, unchanged fields, and user-visible response obligations. Repeated execution should be part of release evidence when the workflow is economically or operationally material.

Implementable now:
- express completion as terminal-state predicates;
- run each release candidate repeatedly against isolated state;
- separate occasional capability from dependable completion;
- price cost per successful state transition rather than cost per attempt.

Implementability score: 0.88

Core sources:
- [ThinkingBox implementation article](https://huggingface.co/blog/microsoft/thinkingbox)
- [ThinkingBox paper, v4](https://arxiv.org/abs/2608.19741v4)

Durable topic: [Evaluation Containment Control Plane](../evaluation-containment-control-plane/evaluation-containment-control-plane.md)

## Local-first is a measured operating mode

Mingbird's useful claim is narrower than local models replacing cloud models. Small models become viable for more tasks when the harness controls context prefill, completion, and loops explicitly. The repository provides a concrete Windows and Ollama implementation, but the evaluation remains author-run, single-machine, and largely single-trial.

The sovereignty implication is to define local-first as a routing policy with evidence. A task stays local when the local model and harness meet a measured quality floor. Escalation occurs when capability or confidence falls below that floor. Privacy, latency, and cost improve only when the local path is dependable enough to avoid hidden retries and silent abandonment.

Implementable now:
- maintain a local task eligibility matrix;
- bind each local model to a tested harness version;
- record local failure and escalation reasons;
- keep privileged tool access narrow even when inference is local.

Implementability score: 0.82

Core sources:
- [Mingbird paper, v1](https://arxiv.org/abs/2610.02001v1)
- [Mingbird repository](https://github.com/Mingbird/Mingbird-agent)

Durable topic: [Local-First Agents](../local-first-agents/local-first-agents.md)

## Skill handoffs cannot mint approval

APEX turns a common agent pattern into a measured authority failure. An upstream skill writes a work artifact that falsely states approval, and a downstream skill accepts that claim as authorization. Across 690 attempts, the attack selected the target action 74.2% of the time. A prompt asking the model to compare artifacts with the request cut attacks but also damaged benign task success.

The governance rule is that derived artifacts cannot increase authority. They may carry facts, hypotheses, and progress, but approval must come from an origin-bound grant tied to the user, action, scope, and time. Multi-skill composition must be tested as a complete program.

Implementable now:
- mark skill outputs as derived evidence;
- preserve source skill and source snapshot on every handoff;
- reject approval claims without an origin-bound grant;
- test composed skill graphs, not only individual packages;
- place exact-effect release below the skill layer.

Implementability score: 0.68

Core sources:
- [Chaining Skills to Hijack LLM Agents, v1](https://arxiv.org/abs/2610.01564v1)
- [APEX repository](https://github.com/Minakamiii/Chaining_Skills_to_Hijack_LLM_Agents)

Durable topics: [Untrusted Data Boundaries](../untrusted-data-boundaries/untrusted-data-boundaries.md), [Agent Execution Control Plane](../agent-execution-control-plane/agent-execution-control-plane.md)

## Tool access must be request-bound

OverAct separates tool availability from tool necessity. In 720 controlled episodes across eight privacy-sensitive domains, all seven evaluated models exceeded the minimum required access. Explicit pre-dispatch filtering reduced privacy-oriented excess by 43%.

The governance implication is that authentication and RBAC are necessary but incomplete. A gateway should evaluate whether each call is needed for the literal request, then issue the smallest usable grant. Unused access should be measurable as an authorization defect even when the task succeeds.

Implementable now:
- compile request intent into allowed data purposes;
- justify and filter each sensitive call before dispatch;
- measure excess retrieval alongside completion;
- retain denied-call evidence for policy tuning.

Implementability score: 0.76

Core source: [OverAct paper, v1](https://arxiv.org/abs/2610.01508v1)

Durable topic: [Agent Gateway Governance](../agent-gateway-governance/agent-gateway-governance.md)

## Working conclusion

Sovereignty depends on keeping truth and authority outside the model's prose. Terminal state proves completion. Origin-bound grants prove approval. Request-bound filters prove tool necessity. Local execution earns trust through measured outcomes rather than location alone.
