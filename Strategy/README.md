# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: 2026-05-25 Daily Scan

### Runtime trust needs confidence calibration plus trajectory guardrails
Summary: MARGIN treats multi-agent trust as an online calibration problem instead of a fixed model-ranking problem. AgentDoG 1.5 and the OpenClaw risk analysis show why final-output moderation is too late for privileged local agents: the dangerous event can live in the trajectory, tool path, memory path, or local storage boundary.

Analysis: [daily sovereignty analysis](2026-05-25/sovereignty.md#runtime-trust-needs-confidence-calibration-plus-trajectory-guardrails)
Durable topics: [Model Router Governance](model-router-governance/model-router-governance.md), [Runtime Governance](runtime-governance/runtime-governance.md), [Local-First Agents](local-first-agents/local-first-agents.md)
Core sources: [MARGIN](https://arxiv.org/abs/2605.22949), [AgentDoG 1.5](https://huggingface.co/AI45Research/AgentDoG1.5-Qwen3.5-4B), [OpenClaw risks](https://arxiv.org/abs/2605.23330)
Implementable now:
- log agent/model, task class, self-confidence, selected answer, verifier outcome, and human correction;
- maintain per-agent confidence buckets before using learned routing;
- preserve router traces with calibration and fallback reasons;
- test trajectory-level guardrails offline on stored traces;
- separate local-agent storage, tool, memory, and identity authority in policy.
Tools, repos, and methodologies worth exploring:
- exponentially weighted calibration buckets, Brier/reliability curves, LiteLLM/Portkey-style router traces, OPA/Cedar, trajectory-level classifiers, permission manifests
Implementability score: 0.57

## Previous structured update

The prior Strategy daily scan for 2026-05-23 focused on latent-state data boundaries and stateful evasion/MCP-client telemetry: [2026-05-23 sovereignty](2026-05-23/sovereignty.md).
