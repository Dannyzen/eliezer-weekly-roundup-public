# Strategy Weekly Sovereignty: Week ending 2026-05-29

This week’s Strategy signal is that sovereignty has moved into the runtime boundary. The strategic asset is not merely model access. It is control over tool admission, MCP identity, OAuth scopes, latent state, memory authority, sandbox policy, approval trails, rollback, and trajectory review.

## Findings

### Agent gateways are becoming the real control plane

MCP and tool governance dominated the week’s strategy layer. Tool metadata can become a security boundary. Generated tools need validation before exposure. Permission laundering shows why data-flow capability budgets matter. Google’s Chrome Enterprise Premium MCP server turns browser-security administration into an agent-callable surface with real DLP, connector, telemetry, and license-management implications.

Why it matters: a privileged MCP server is not a plugin. It is an administration plane. Once an agent can create DLP policies, inspect browser telemetry, call generated tools, or chain tools across permission boundaries, the gateway becomes the effective control plane.

How it fits into the strategy stack: serious operators need a governed tool gateway between agents and authority. That gateway enforces identity, source trust, schema pinning, OAuth scope, data-flow constraints, mutation approvals, logs, and rollback evidence.

Implementable now:
- pin tool schemas, descriptions, and server identities before exposure;
- validate generated tools in a sandbox before MCP registration;
- bind every tool call to user identity, workflow identity, and OAuth scope;
- split diagnostic tools from mutation tools;
- approval-gate broad DLP/org-unit/admin changes;
- record tool name, arguments, user, resource, before/after state, approval artifact, and rollback path.

Tools, repos, and methodologies worth exploring:
- MCP gateways, MCP Inspector, Open Policy Agent, Cedar, OAuth scope review, Tool Forge, Chrome Enterprise Premium MCP, Pocket CEP, OpenTelemetry, approval artifacts, rollback tests

Implementability score: 0.70

Core sources:
- [MCP tool metadata security boundary](https://arxiv.org/abs/2605.24069)
- [Tool-description governance source](https://arxiv.org/abs/2605.24248)
- [Permission laundering / data-flow capabilities](https://arxiv.org/abs/2605.26542)
- [Tool Forge validation-carrying generated tools](https://arxiv.org/abs/2605.28000)
- [nextmoca/tool-forge](https://github.com/nextmoca/tool-forge)
- [Bringing AI agents to Chrome Enterprise security management](https://blog.google/security/bringing-ai-agents-to-chrome-enterprise-security-management/)
- [google/chrome-enterprise-premium-mcp](https://github.com/google/chrome-enterprise-premium-mcp)
- [Pocket CEP MCP example](https://github.com/google/ChromeBrowserEnterprise/tree/main/mcp-examples/pocket-cep)

### Latent state and shared state are sovereignty boundaries

The lowest-implementability but high-importance signal was LCGuard’s KV-cache warning: cached model state can become a hidden data boundary. The same pattern appears in memory gates and MemTrace-style provenance graphs. Shared context, summaries, vector stores, caches, and memory writes can influence future actions without being visible as ordinary tool inputs.

Why it matters: sovereignty collapses when authority moves through state the operator cannot inspect or constrain. A model call can be isolated at the API layer while still inheriting leaked cache state, bad memory, contaminated summaries, or unreviewed retrieved context.

How it fits into the strategy stack: latent state needs threat modeling. Caches, memories, embeddings, summaries, and shared clients should have trust zones, provenance, expiry, deletion semantics, and action-time policy impact labels.

Implementable now:
- separate cache and memory trust zones by tenant, workflow, and sensitivity;
- log which memories, summaries, embeddings, or cached states affected a run;
- require memory-write provenance and rollback;
- attach expiry and deletion semantics to derived state;
- run contradiction and taint checks before promoted memory influences privileged actions.

Tools, repos, and methodologies worth exploring:
- MemTrace, append-only event logs, pgvector with provenance tables, data-retention policy, taint labels, cache-isolation policies, memory-write approval gates, contradiction checks

Implementability score: 0.50

Core sources:
- [LCGuard / KV-cache leakage boundary](https://arxiv.org/abs/2605.22786v1)
- [Personalized memory storage gates](https://arxiv.org/abs/2605.25535)
- [MemTrace memory provenance](https://arxiv.org/abs/2605.28732)
- [zjunlp/MemTrace](https://github.com/zjunlp/MemTrace)

### Deployment-shaped safety governance beats abstract safety scores

A3S-Bench, MCP-client telemetry, ITBench-AA/RAMPART, and Gram all make the same strategic point: safety should be tested in the shape of deployment. Agent failures happen inside roles, tools, incentives, incident workflows, and stateful traces.

Why it matters: generic refusal tests do not predict whether a coding, research, browser, or admin agent will conceal evidence, over-complete a goal, bypass policy, mishandle incident response, or exploit a client/tool gap.

How it fits into the strategy stack: each high-trust agent role should have deployment-shaped adversarial fixtures before scope increases. The review object is a trajectory, not a screenshot.

Implementable now:
- build sabotage, overeagerness, evasion, and incident-response scenarios for each high-authority agent role;
- score concealment, evidence manipulation, policy bypass, excessive objective pursuit, and unjustified mutation;
- preserve full trajectories for human and investigator-agent review;
- run ablations on realism, objective wording, tool scope, approval gates, and role pressure;
- require passing scenario packs before expanding tool scope.

Tools, repos, and methodologies worth exploring:
- A3S-Bench, Agent3Sigma Stage, MCP-client telemetry datasets, ITBench-AA, RAMPART, pytest, red-team scenario cards, LangSmith/Langfuse trajectory review, OpenTelemetry traces, approval-gate ablations

Implementability score: 0.62

Core sources:
- [A3S-Bench](https://arxiv.org/abs/2605.22321v1)
- [Agent3Sigma Stage](https://github.com/antgroup/Agent3Sigma-Stage)
- [MCP client telemetry dataset](https://huggingface.co/datasets/evalstate/mcp-clients)
- [ITBench-AA blog](https://huggingface.co/blog/ibm-research/itbench-aa)
- [RAMPART](https://github.com/microsoft/RAMPART)
- [Gram sabotage auditing](https://arxiv.org/abs/2605.30322)

### Sandboxing and data-flow budgets are the practical policy layer

Permission laundering and Sandlock point at the same operational requirement from different sides. Data can cross boundaries through tool chains even when each tool looks locally acceptable. Risky local execution also needs a cheap isolation layer before container or VM overhead becomes justified.

Why it matters: policy cannot only approve individual calls. It has to reason about information movement, process effects, files, network access, and cumulative tool chains. Lightweight sandboxing makes local containment realistic enough to use by default for many agent actions.

How it fits into the strategy stack: put data-flow capabilities and process restrictions into the runtime policy layer. The agent should not infer its own containment boundary from a prompt.

Implementable now:
- tag data with capabilities and allowed destinations;
- block tool chains that launder restricted data into broader tools;
- wrap local process execution with file/network/syscall constraints;
- log denial reasons and capability consumption;
- escalate high-risk runs to containers or VMs when process-level isolation is insufficient.

Tools, repos, and methodologies worth exploring:
- OPA/Cedar, capability labels, eBPF/audit logs, Sandlock, containers, microVMs, seccomp, file/network allowlists, policy-as-code tests

Implementability score: 0.74

Core sources:
- [Permission laundering / data-flow capabilities](https://arxiv.org/abs/2605.26542)
- [Sandlock paper](https://arxiv.org/abs/2605.26298)
- [multikernel/sandlock](https://github.com/multikernel/sandlock)

## Watchlist

Dissociative Identity is strategically important because it attacks reputation assumptions for mutable agents, but it is less immediately operational than gateway policy, sandboxing, and deployment-shaped audits. Track it for identity/provenance design.

Source:
- [Dissociative Identity](https://arxiv.org/abs/2605.30169)
