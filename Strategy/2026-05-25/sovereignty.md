# Strategy Daily Analysis: 2026-05-25

Today’s strategy signal: trust in agent systems is moving from static policy to runtime measurement. Multi-agent coordinators need calibration from live outcomes, and privileged local agents need trajectory-level guardrails because the risky event may be a tool path, memory path, or cross-context aggregation pattern rather than a bad final answer.

## Runtime trust needs confidence calibration plus trajectory guardrails

MARGIN targets a practical multi-agent failure: a coordinator has to decide which agent response to trust, but model self-confidence is often miscalibrated and can become inversely correlated with correctness on hard tasks. The proposed pattern is online per-agent, per-confidence-band calibration from the task stream itself, without model access, held-out calibration data, or retraining.

AgentDoG 1.5 and the new OpenClaw risk paper point at the other side of the same governance problem. Once agents call tools, preserve local state, aggregate context, and act across user or organizational surfaces, the risk is not limited to a single output. A guardrail has to read trajectories: observations, thoughts or plans where available, tool calls, environment responses, and resulting state changes. A local-first agent does not become safe just because it runs locally; persistent local storage and broad tool access create new authority boundaries.

### Why it matters

Agent trust needs live evidence. Static model rankings, agent reputations, and self-reported confidence are not enough. The runtime should learn which agents are reliable in which confidence bands and task types, and it should detect unsafe trajectories before final output moderation would notice anything.

For Danny’s stack, the immediate strategic implication is that routers and gateways should store outcome-linked trust data. A model router that only tracks price and latency is incomplete. A local agent gateway that only scans prompts is incomplete. The governance layer should combine routing evidence, confidence calibration, policy mediation, and trajectory risk classification.

### How it fits into the strategy stack

- Model-router governance: route by live calibrated reliability, not provider reputation alone.
- Runtime governance: scan trajectories and tool paths, not just prompts and final answers.
- Local-first agents: treat local storage, memory, plugins, and tool authority as governed surfaces.
- Agent-network containment: separate confidence signals, policy signals, and authority scopes per agent/principal.

### Implementable now

- Track agent/model, task class, self-confidence, selected answer, verifier outcome, and later human correction.
- Maintain simple per-agent confidence buckets before attempting learned routing.
- Require a router trace: candidates, selected agent, calibration reason, fallback reason, and outcome.
- Test trajectory-level guardrails offline on stored traces before allowing online blocking.
- Separate local-agent storage authority, tool authority, and identity authority in policy.
- Add canary trajectories for unconfirmed actions, tool misuse, privacy leakage, and over-privileged local file access.

### Tools, repos, and methodologies worth exploring

- exponentially weighted calibration buckets
- Brier score and reliability curves per task type
- LiteLLM/Portkey-style routing traces
- OPA or Cedar policy checks before tool execution
- trajectory-level classifiers such as AgentDoG 1.5 for offline evaluation
- local-agent storage/tool/memory permission manifests

### Implementability score

0.57

The basic logging and bucket calibration are straightforward. The harder part is trustworthy online intervention: task-specific verifiers, trace normalization, false-positive handling, policy integration, and safe local-agent permission design.

### Core sources

- MARGIN: Runtime Confidence Calibration for Multi-Agent Foundation Model Coordination: https://arxiv.org/abs/2605.22949
- AgentDoG 1.5 model card: https://huggingface.co/AI45Research/AgentDoG1.5-Qwen3.5-4B
- Security, Privacy, and Ethical Risks in OpenClaw: https://arxiv.org/abs/2605.23330
