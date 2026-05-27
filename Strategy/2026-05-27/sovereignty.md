# Strategy Daily Scan: 2026-05-27

Today’s Strategy signal is about containment at the data-flow and process layers. Tool allowlists are not enough if values can launder authority across tools, and containers are not the only practical sandbox shape for agent-generated code. The stack is moving toward capability-carrying data, gateway-visible flow control, and lightweight Linux confinement for ordinary agent workstations.

## Permission laundering needs data-flow capability budgets

ChainCaps names a failure mode that normal per-tool permission checks miss: an agent can read a confidential document with one allowed tool, summarize it with another allowed tool, and send the summary through a third allowed tool. Every tool call can be individually permitted while the end-to-end flow is unsafe. The paper calls this permission laundering and proposes monotonic capability attenuation: every value carries a sink-specific capability budget, and tool composition can only preserve or reduce authority, never gain it.

Why it matters: agent gateways often govern tool access as a flat allowlist. That is too weak for real workflows because authority travels with data, not only with tool names. ChainCaps’ transparent MCP proxy framing is especially relevant: the control point can sit between agents and tools without modifying the agent or tool server, but manifest quality becomes the bottleneck.

How it fits the stack: this belongs in agent gateway governance. The gateway needs to see data class, source, destination, and sink authority across the tool chain. MCP admission, OAuth scopes, and per-tool RBAC are necessary but insufficient.

Implementable now:
- classify tool outputs by data class and allowed sinks;
- attach source and capability metadata to tool results in the trace;
- intersect authority across transformations instead of resetting permissions at every tool call;
- block external-send, publish, email, database-write, or shell actions when input capability does not permit that sink;
- review and test tool manifests because bad manifests collapse the guarantee.

Tools, repos, and methodologies worth exploring:
- MCP proxy/gateway layer, Open Policy Agent or Cedar, taint tracking, information-flow control, schema-level data classes, signed tool manifests, OpenTelemetry spans carrying data-class/capability metadata, adversarial multi-tool fixtures for permission laundering.

Implementability score: 0.62

Core source: [ChainCaps: Composition-Safe Tool-Using Agents via Monotonic Capability Attenuation](https://arxiv.org/abs/2605.26542)

Supporting sources: [AgentSecBench](https://arxiv.org/abs/2605.26269), [Cordon-MAS](https://arxiv.org/abs/2605.26754)

## Lightweight process sandboxing is becoming practical agent infrastructure

Sandlock is useful because it targets the gap between ad-hoc wrappers and heavyweight containers or microVMs. The paper and repository describe a Linux process sandbox using Landlock, seccomp-bpf, seccomp user notification, copy-on-write filesystem effects, dynamic network decisions, and HTTP-level access controls without root, cgroups, containers, or image builds. The repository describes the goal plainly: “The lightest AI sandbox.”

Why it matters: coding agents increasingly run shell commands, tests, scripts, package managers, and third-party tools. Full VM isolation is safer but expensive to operationalize for every small task. Unprivileged process confinement gives agent operators a lower-friction default for local and CI-adjacent workloads.

How it fits the stack: this belongs in the sovereign/local runtime layer. The model provider should not inherit the human’s workstation authority, and the execution process should not inherit the entire host just because a task needs `python` or `npm test`.

Implementable now:
- run generated commands under a separate confined process policy;
- grant read/write paths explicitly instead of sharing the whole home directory;
- keep network egress denied by default or mediated through host/path/method rules;
- use copy-on-write or overlay effects so workspace mutations are reviewable;
- preserve command, syscall/network denial, filesystem diff, and exit status in the agent trace.

Tools, repos, and methodologies worth exploring:
- Linux Landlock, seccomp-bpf, seccomp user notification, COW filesystem overlays, egress allowlists, dedicated agent users, Incus/LXC or microVMs for higher-risk work, Sandlock as a read-only candidate for manual evaluation.

Implementability score: 0.78

Core sources: [Sandlock paper](https://arxiv.org/abs/2605.26298), [multikernel/sandlock](https://github.com/multikernel/sandlock)
