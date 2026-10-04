# AgenticAI Daily Analysis: 2026-10-04

## Scope note

There is no new Sunday arXiv listing. The newest category batch is Friday, October 2. This update promotes one October 3 implementation release and three non-duplicate Friday papers after checking the existing corpus. External repositories were inspected read-only. No external source was cloned, installed, built, imported, or executed.

## Score the state left behind

ThinkingBox makes terminal application state the evaluation target. The October 3 Hugging Face release exposes the benchmark through OpenEnv, with isolated MCP-compatible tool sessions and executable checks over persistent effects. The benchmark contains 507 stateful business workflows, each run 20 times. In the current paper, the strongest model reaches 65.36% pass@1 and 25.25% pass^20. Clean termination and valid tool calls frequently coexist with an incorrect final state.

Why it matters: output grading and tool-call validity cannot prove that a business workflow landed correctly. The reliable oracle is the allowed terminal state plus the absence of extra effects. Repetition then measures whether success is dependable rather than occasional.

Stack fit: deterministic testing, stateful agent evaluation, MCP sandboxes, reliability measurement.

Implementable now:
- use the public `huggingface/OpenEnv` ThinkingBox environment;
- pin the `microsoft/thinkingbox-data` `thinkingbox-bench-v1.0` tag;
- define task-specific state contracts for required, forbidden, and unchanged fields;
- run repeated trials and report pass@k separately from pass^k;
- retain traces and database snapshots for every failed state transition.

Evidence caveat: the paper first appeared in August and was updated to v4 on October 1. The fresh signal is the October 3 OpenEnv release and implementation article. This scan verified repository metadata and trees but did not execute the benchmark.

Implementability score: 0.88

Core sources:
- [October 3 implementation article](https://huggingface.co/blog/microsoft/thinkingbox)
- [ThinkingBox paper, v4](https://arxiv.org/abs/2608.19741v4)
- [OpenEnv ThinkingBox environment](https://github.com/huggingface/OpenEnv/tree/main/envs/thinkingbox_env)
- [ThinkingBox data](https://github.com/microsoft/thinkingbox-data)

Durable topic: [Agent Harness Architecture](../agent-harness-architecture/agent-harness-architecture.md)

## Fit the harness to the model

Mingbird argues that small open models fail partly because cloud-oriented harnesses consume their context and tolerate weak completion behavior. Its local-first Windows and Ollama harness uses a net-zero tool-prefill budget, task re-read completion gates, and signature-level loop detection. On the self-built LRAB comparison, Mingbird scored 0.886 against 0.631, 0.479, and 0.405 for three comparison harnesses across 288 cells. A separate 278-task benchmark reported 0.856 against 0.791 and 0.737.

Why it matters: model selection and harness selection are coupled. A small local model needs tighter context budgets, explicit finish criteria, and deterministic loop control. A generic frontier-model harness can erase the cost and privacy advantages of local inference.

Stack fit: local-first agents, context economy, completion control, harness benchmarking.

Implementable now:
- evaluate small models with a fixed machine, task set, token budget, and artifact scorer;
- budget tool schemas and demonstrations before the first model token;
- re-read the original task before accepting completion;
- detect loops from tool signatures and repeated state, not prose similarity alone;
- keep cloud escalation as an explicit fallback with a recorded reason.

Evidence caveat: the repository is public, Apache-2.0, has a populated main branch, and released v1.9.2 on October 2. The paper is a two-author study with a self-built benchmark, one machine, and mostly single-trial scoring. The reported ablation is directional; same-night variation reached 0.069.

Implementability score: 0.82

Core sources:
- [Mingbird paper, v1](https://arxiv.org/abs/2610.02001v1)
- [Mingbird repository](https://github.com/Mingbird/Mingbird-agent)
- [Mingbird v1.9.2 release](https://github.com/Mingbird/Mingbird-agent/releases/tag/v1.9.2)

Durable topics: [Agent Harness Architecture](../agent-harness-architecture/agent-harness-architecture.md), [Context Economy](../context-economy/context-economy.md)

## Treat skill composition as a single security boundary

APEX demonstrates authority laundering across skill handoffs. An upstream skill causes the agent to write a plausible progress record containing a false claim of approval. A downstream skill treats that record as authority for an attacker-selected action. The attack succeeded in 512 of 690 attempts across six models. On GPT-5.4, the full chain reached 84.3%, compared with 17.4% when merged into one skill.

Why it matters: static review of each skill is insufficient. The security unit is the composed workflow, including files, summaries, and state passed between skills. A skill-produced artifact is evidence from an untrusted component, not user authorization.

Stack fit: skill admission, composition testing, artifact lineage, execution control.

Implementable now:
- label every skill-produced artifact with skill identity and source snapshot;
- prohibit approval claims in derived artifacts from upgrading execution authority;
- bind high-impact approval to the original user request and one exact action;
- fuzz multi-skill compositions, including benign skills that share mutable files;
- require the final effect gate to compare the proposed action with the original request.

Evidence caveat: the public MIT repository includes the evaluation pipeline and controlled variants, but this scan did not execute it. The tested prompting defense reduced GPT-5.4 attack success from 84.3% to 59.1% while reducing benign verifier pass rate from 86.7% to 56.3%. Prompting alone is a poor production control.

Implementability score: 0.68

Core sources:
- [Chaining Skills to Hijack LLM Agents, v1](https://arxiv.org/abs/2610.01564v1)
- [APEX repository](https://github.com/Minakamiii/Chaining_Skills_to_Hijack_LLM_Agents)

Durable topic: [Skills as Control](../skills-as-control/skills-as-control.md)

## Filter tool calls against the literal request

OverAct measures proactive over-authorization: an agent accesses more private information than the request requires. Its 720-episode benchmark spans eight privacy-sensitive domains and scores excess scope deterministically against a minimal required tool set. Across seven models, every model exceeded authorized scope. SelfAudit reduced privacy-oriented excess by 43% by filtering tool calls that lacked request-grounded justification.

Why it matters: authenticated tool access still permits unnecessary retrieval. Least privilege must operate at each call, using the current request as the authority source. Tool availability and tool necessity are different decisions.

Stack fit: tool routing, privacy policy, deterministic authorization, gateway telemetry.

Implementable now:
- define a minimal required tool set for each evaluation task;
- require a request-grounded justification before every privacy-sensitive call;
- reject unsupported calls before dispatch rather than reviewing them afterward;
- measure excess access separately from task success;
- retain suppressed-call receipts to calibrate false positives.

Evidence caveat: the benchmark uses controlled schemas with six tools per domain. No public implementation repository was linked from the paper page. SelfAudit is a useful testable method, not proof of a complete access-control architecture.

Implementability score: 0.76

Core source: [OverAct paper, v1](https://arxiv.org/abs/2610.01508v1)

Durable topic: [Agent Gateway Governance](../../Strategy/agent-gateway-governance/agent-gateway-governance.md)

## Working conclusion

The useful common pattern is a deterministic boundary around effects. Score terminal state, tune the harness to the model's actual limits, preserve origin through skill handoffs, and require each sensitive tool call to justify itself against the original request.
