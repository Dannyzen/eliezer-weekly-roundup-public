# AgenticAI

This index tracks the most recent structured implementation research. Each finding links to the dated analysis, primary sources, practical methods, and an implementability score.

## Latest Structured Update: 2026-10-04

Sunday has no new arXiv listing. The strongest fresh implementation signal is ThinkingBox through OpenEnv. The best non-duplicate Friday papers reinforce three adjacent controls: harness fit for small local models, authority lineage across skill chains, and request-bound filtering before sensitive tool calls.

### Score terminal state, then repeat

Summary: ThinkingBox grades 507 stateful workflows through executable backend checks and repeats each task 20 times. The strongest reported model falls from 65.36% pass@1 to 25.25% pass^20.

Analysis: [daily analysis](2026-10-04/reasoning.md#score-the-state-left-behind)
Durable topic: [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md)
Core sources: [implementation article](https://huggingface.co/blog/microsoft/thinkingbox), [paper v4](https://arxiv.org/abs/2608.19741v4), [OpenEnv environment](https://github.com/huggingface/OpenEnv/tree/main/envs/thinkingbox_env)
Tools and methodologies worth exploring now: OpenEnv, ThinkingBox data tag, terminal-state predicates, repeated trials, pass@k and pass^k, state snapshots
Implementability score: 0.88

### Fit the harness to small local models

Summary: Mingbird uses strict prefill budgets, task re-read completion gates, and loop detection to recover useful task performance from small Ollama models. The public v1.9.2 release is available now, with narrow evidence caveats.

Analysis: [daily analysis](2026-10-04/reasoning.md#fit-the-harness-to-the-model)
Durable topics: [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md), [Context Economy](context-economy/context-economy.md)
Core sources: [paper v1](https://arxiv.org/abs/2610.02001v1), [repository](https://github.com/Mingbird/Mingbird-agent), [release](https://github.com/Mingbird/Mingbird-agent/releases/tag/v1.9.2)
Tools and methodologies worth exploring now: Ollama, byte-level prefill budgets, finish gates, signature-level loop detection, artifact scoring, explicit cloud escalation
Implementability score: 0.82

### Test skill chains as composed programs

Summary: APEX used agent-written handoff artifacts to carry false approval across otherwise plausible skills, succeeding in 512 of 690 attempts. Prompt-only mitigation caused a large benign-utility loss.

Analysis: [daily analysis](2026-10-04/reasoning.md#treat-skill-composition-as-a-single-security-boundary)
Durable topic: [Skills as Control](skills-as-control/skills-as-control.md)
Core sources: [paper v1](https://arxiv.org/abs/2610.01564v1), [repository](https://github.com/Minakamiii/Chaining_Skills_to_Hijack_LLM_Agents)
Tools and methodologies worth exploring now: origin labels, immutable handoff lineage, exact approval grants, composition fuzzing, deterministic effect gates
Implementability score: 0.68

### Filter unnecessary sensitive calls before dispatch

Summary: OverAct scores excess tool scope deterministically across 720 episodes. Request-grounded filtering reduced privacy-oriented excess by 43% without oracle access.

Analysis: [daily analysis](2026-10-04/reasoning.md#filter-tool-calls-against-the-literal-request)
Durable topic: [Agent Gateway Governance](../Strategy/agent-gateway-governance/agent-gateway-governance.md)
Core source: [OverAct paper v1](https://arxiv.org/abs/2610.01508v1)
Tools and methodologies worth exploring now: minimal required tool sets, request-grounded justifications, pre-dispatch filtering, suppressed-call receipts, excess-access metrics
Implementability score: 0.76

## Current implication

Treat effect correctness, harness fit, artifact authority, and tool necessity as explicit runtime contracts. Model output can propose each decision. Deterministic infrastructure must verify it.

Latest roundup: [2026-10-04](../roundups/2026-10-04.md).
