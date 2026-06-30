# Strategy Daily Sovereignty - 2026-06-30

Today's governance signal is that agent security is becoming a trajectory problem. The important controls are not only better prompts or better routers. They are runtime evidence: what memory was recalled, which tool transition followed, how routing authority was assigned, and whether the system can prove the decision was based on observed behavior rather than self-description.

## Memory poisoning detection belongs in the trajectory, not the prompt

Core source: https://arxiv.org/abs/2606.30566v1

Forensic Trajectory Signatures for Agent Memory Poisoning Detection is valuable because it treats persistent-memory attacks as observable runtime behavior. In the evaluated architecture, successful exfiltration attacks required a memory recall before an email send. The paper reports that a simple invariant over that transition reached AUC 0.9563, and a random forest over 19 trajectory features reached AUC 0.9904.

Why it matters: memory-poisoning defense has been too focused on classifying memory text. That misses the deployment problem. A stored memory becomes dangerous when it participates in an effectful action path. Tool-call logs, memory-recall events, and action sinks are therefore security evidence, not only telemetry.

How it fits into the strategy layer:
- Memory authority control plane: every memory recall needs origin, scope, authority tier, and allowed effects.
- Evidence provenance: detection should work over trajectory signatures and source lineage, not only final answers.
- Agent gateway governance: recall-to-send, recall-to-write, recall-to-deploy, and recall-to-external-post transitions should be monitored.
- Runtime governance: prefix-only detection matters because blocking after exfiltration is too late.

Practical tools, repos, and methodologies worth exploring now:
- Add memory-recall and effectful-tool transition features to agent traces.
- Create invariants for sensitive paths such as memory recall to email, CRM write, external HTTP, file export, deploy, or credential use.
- Run simple rule detectors first, then train classifiers only after enough local trajectory labels exist.
- Keep prompt-injection and memory-poisoning signatures separate, because they can have different tool-call shapes.

Implementability score: 0.70

The thin version is implementable now if the runtime already logs memory calls and tool calls. The hard version needs reliable labels, privacy-safe trace retention, and model/workflow-specific baselines.

## Multi-agent routing needs empirical capability tests, not self-descriptions

Core source: https://arxiv.org/abs/2606.30555v1

Linguistic Firewall introduces ANTAP, an evaluation-driven multi-agent router that rejects textual self-descriptions as the basis for routing. Instead of trusting an agent's advertised skills or static embedding, ANTAP actively tests capability and stores behavioral operators in a shared semantic space. At inference time, routing uses non-textual projection, which makes description-based attacks structurally less available.

The reported result is strategically useful even if the implementation is still research-grade: near-zero attack success against description-based injection, compared with 67.3% or higher for a description-based router baseline, plus a 20% reduction against adaptive embedding attacks relative to the embedding baseline.

Why it matters: capability discovery is becoming an authority plane. If a multi-agent system routes work based on self-descriptions, tool descriptions, marketplace blurbs, or static embeddings, a malicious or overclaiming worker can steer tasks toward itself. The gateway should ask what the worker has empirically done under test, not what it says it can do.

How it fits into the strategy layer:
- Model-router governance: route by measured capability, calibrated reliability, policy, latency, and cost.
- Agent discovery: separate relevance, authorization, trust, and observed competence.
- Agent gateway governance: do not expose or select workers solely from natural-language descriptions.
- Multi-agent orchestration: compile worker choice from capability evidence, not social proof or prompt text.

Practical tools, repos, and methodologies worth exploring now:
- Build small active probes for each worker/tool class before admission.
- Store capability scores as signed registry facts with date, test suite, model, and policy version.
- Rerun probes after model, prompt, skill, or tool changes.
- Route high-risk tasks only to workers whose tested capability covers the action and data class.

Implementability score: 0.55

The idea is implementable with ordinary probe suites and registries. The exact non-textual algebraic routing architecture is more research-heavy, so start with active capability tests and signed registry evidence.
