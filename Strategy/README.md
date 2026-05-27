# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: 2026-05-27 Daily Scan

### Permission laundering needs data-flow capability budgets
Summary: ChainCaps shows that per-tool allowlists miss end-to-end data-flow risk. An agent can read confidential data, transform it, and send it elsewhere while every individual tool call looks permitted. Gateway policy has to propagate authority with values.

Analysis: [daily sovereignty analysis](2026-05-27/sovereignty.md#permission-laundering-needs-data-flow-capability-budgets)
Durable topic: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md)
Core source: [ChainCaps](https://arxiv.org/abs/2605.26542)
Supporting sources: [AgentSecBench](https://arxiv.org/abs/2605.26269), [Cordon-MAS](https://arxiv.org/abs/2605.26754)
Implementable now:
- classify tool outputs by data class and allowed sinks;
- carry capability metadata through gateway traces;
- block sink actions when transformed values lack the required authority.
Tools, repos, and methodologies worth exploring:
- MCP proxy/gateway layer, Open Policy Agent or Cedar, taint tracking, information-flow control, signed manifests, OpenTelemetry data-flow spans, adversarial multi-tool fixtures
Implementability score: 0.62

### Lightweight process sandboxing is becoming practical agent infrastructure
Summary: Sandlock targets the gap between weak wrappers and heavyweight containers or microVMs. It uses Linux Landlock, seccomp-bpf, seccomp user notification, and copy-on-write effects to confine agent-generated code without root or image builds.

Analysis: [daily sovereignty analysis](2026-05-27/sovereignty.md#lightweight-process-sandboxing-is-becoming-practical-agent-infrastructure)
Durable topic: [Agent Sandboxing](agent-sandboxing/agent-sandboxing.md)
Core sources: [Sandlock paper](https://arxiv.org/abs/2605.26298), [multikernel/sandlock](https://github.com/multikernel/sandlock)
Implementable now:
- run generated commands under explicit filesystem, syscall, and network policies;
- keep mutable effects in reviewable overlays;
- preserve denial events and final workspace diffs in the trace.
Tools, repos, and methodologies worth exploring:
- Linux Landlock, seccomp-bpf, seccomp user notification, COW filesystem overlays, dedicated agent users, egress allowlists, Incus/LXC or microVM escalation for higher-risk work
Implementability score: 0.78

## Previous structured update

The prior Strategy daily scan for 2026-05-26 focused on MCP tool metadata as a security boundary: [2026-05-26 sovereignty](2026-05-26/sovereignty.md).
