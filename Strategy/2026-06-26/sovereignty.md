# Strategy Weekly Sovereignty: Week ending 2026-06-26

This week's strategic signal is that agent sovereignty is moving from prompt ownership to authority-object ownership. The operator has to own manifests, grants, memory authority, capability discovery, policy gates, and mutation monitors before the model acts.

## Executive summary

1. **Authority manifests and revocable capabilities define agent scope.** AgentRiskBOM, PORTICO, LedgerAgent, and GitHub issue-field MCP support make agent authority machine-readable, diffable, and time-bound.
2. **Memory becomes a policy-bearing authority object.** Origin-bound memory authority and governed shared memory make persistent memory part of the security perimeter, not just better recall.
3. **Instructions and tool catalogs need external policy gates.** Autoformalized Cedar policies, least-privilege tool tests, ARD-style capability discovery, and ShareLock all say that prompts and tool descriptions are not sufficient boundaries.
4. **Mutation and safety move below the prompt.** Phoenix and the Unfireable Safety Kernel point at the same deployment rule: agents propose, but external state machines, reference monitors, and fail-closed kernels decide whether action happens.

## Authority manifests and revocable capabilities define agent scope

The week's clearest sovereignty primitive is the authority manifest. AgentRiskBOM proposes a machine-readable bill of materials for autonomy level, tools, memory scope, credential scope, approval gates, audit signals, inter-agent communication, and external action capability. PORTICO adds the missing temporal dimension: an agent may need a capability for one episode, but that capability should close when the subtask closes. LedgerAgent adds pre-mutation checks over explicit state. GitHub's issue fields MCP support makes the same point in product form: project state is now agent-mutable control state.

Why it matters: an agent's risk is not described by its model name. It is described by what it can access, remember, delegate, mutate, and retain after a task ends. If those permissions live in prose, they cannot be diffed or reliably revoked.

How it fits into the strategy stack: authority manifests should sit beside runtime config, deployment manifests, and CI policy. They are the bridge between product intent, agent runtime permissions, gateway enforcement, and audit.

Implementable now:

- define a JSON Schema authority manifest for every agent workflow
- include tools, write paths, credential scopes, memory scopes, discovery scopes, delegation rights, approval gates, and external effects
- fail CI when authority expands without review
- issue scoped capability handles for privileged tasks, then close them on subgoal completion
- reject stale handle replay before file, git, network, ticket, message, or production mutation
- log grant, invoke, close, deny, policy epoch, and affected resource in the same trace

Tools, repos, and methodologies worth exploring:

- JSON Schema or Cue authority manifests
- scoped capability handles and closure predicates
- OPA or Cedar over manifest fields
- GitHub issue fields as typed work-state, guarded by MCP identity and workflow scope
- deployment mutation diff detectors
- trace events for grants, revocation, and stale replay denial

Core sources:

- AgentRiskBOM: A Risk-Scoping Security Bill of Materials for Agentic AI Systems: https://arxiv.org/abs/2606.21877v1
- Lingering Authority: Revocable Resource-and-Effect Capabilities for Coding Agents: https://arxiv.org/abs/2606.22504v1
- LedgerAgent: Structured State for Policy-Adherent Tool-Calling Agents: https://arxiv.org/abs/2606.20529
- GitHub issue fields MCP support: https://github.blog/changelog/2026-06-18-duplicate-detection-and-issue-fields-mcp-support-for-github-issues
- GitHub MCP server: https://github.com/github/github-mcp-server

Implementability score: 0.81

The manifest is easy. Binding it to real capability handles, revocation, and target-system rejection of stale authority is the hard part.

## Memory becomes a policy-bearing authority object

Memory was the durable Strategy finding of the week. The memory-poisoning work shows how persistent memory can launder adversarial content across sessions, summaries, trusted tools, and apparent corroboration. Its proposed fix is non-malleable origin-bound authority for memory records. Governed Shared Memory adds the fleet version: multi-agent memory services need scoped retrieval, direct-read controls, stale-propagation handling, contradiction supersession, and provenance reconstruction. ESAA-Conversational and Multi-Agent Transactive Memory make the implementation pressure obvious: agents will increasingly reuse prior trajectories and handoff state.

Why it matters: memory is not context. Memory can grant future influence after the original interaction is gone. A poisoned memory can steer tool use, retrieved evidence, or future decisions while looking like a normal remembered fact.

How it fits into the strategy stack: memory needs the same policy path as tools. Search, direct read, derivation, propagation, summarization, contradiction handling, and trusted recall all need principal, origin, scope, and authority checks.

Implementable now:

- add origin principal, source event, authority tier, scope, derivation, expiration, and elevation policy to memory records
- distinguish quoted external text, user-confirmed fact, tool-observed fact, and agent-derived summary
- route semantic memory search and direct memory reads through the same policy gate
- require elevation before a memory can authorize tool use or external effects
- test laundering, stale propagation, contradiction persistence, direct-ID scope bypass, and derivation reconstruction
- keep raw episodes and memory events as evidence, then project compact recall views from them

Tools, repos, and methodologies worth exploring:

- MEM-INV-Bench / TMA-NM: https://github.com/yedidel/mem-inv-bench
- MEM-INV-Bench dataset: https://huggingface.co/datasets/anonymos-2321135/MEM-INV-Bench
- memory records with origin and authority metadata
- policy gates over vector search and direct reads
- append-only memory event logs with supersession records
- contradiction tests before multi-agent memory propagation

Core sources:

- Securing LLM-Agent Long-Term Memory Against Poisoning: https://arxiv.org/abs/2606.24322v1
- MEM-INV-Bench / TMA-NM repository: https://github.com/yedidel/mem-inv-bench
- MEM-INV-Bench dataset: https://huggingface.co/datasets/anonymos-2321135/MEM-INV-Bench
- Governed Shared Memory for Multi-Agent LLM Systems: https://arxiv.org/abs/2606.24535
- ESAA-Conversational: https://arxiv.org/abs/2606.23752

Implementability score: 0.68

Origin metadata and policy checks are implementable now. The difficult part is making every memory path honor the same authority model, especially semantic search, direct reads, summarization, and multi-agent propagation.

## Instructions and tool catalogs need external policy gates

The policy boundary got sharper on Friday. Autoformalization of Agent Instructions into Policy-as-Code translates system prompts, MCP tool definitions, and written policy corpora into Cedar policies through a generator-critic loop, then enforces those policies outside the model before actions execute. ShareLock attacks the opposite seam: it splits malicious intent across multiple benign-looking MCP tool descriptions so isolated tool review fails. ToolPrivBench shows agents still over-select or escalate to higher-privilege tools. Agentic Resource Discovery and GitHub Agent Finder make capability discovery dynamic, which means discovery itself is an authority plane.

Why it matters: prompt instructions, tool descriptions, and catalog search all influence what an agent can do. None of them should be trusted as the enforcement layer. A serious gateway has to decide allowed resources, allowed combinations, policy verdicts, and update gates outside the model.

How it fits into the strategy stack: this is agent gateway governance. Natural language can be a policy source. Tool descriptions can be a discovery source. Neither should be the boundary. The boundary should be Cedar, OPA, OpenFGA, IAM, broker logic, or another deterministic enforcement layer.

Implementable now:

- put Cedar or OPA in front of one privileged agent tool
- compile natural-language rules into explicit action, resource, principal, context, and data-class fields
- use generator-critic loops as policy drafting assistance, not final authority
- inspect enabled-tool sets and update epochs, not only individual MCP tool records
- require escalation justification when higher-privilege tools are selected over lower-privilege alternatives
- log discovery query, selected resource, trust score, policy verdict, denied combination, and final effect

Tools, repos, and methodologies worth exploring:

- Cedar policy engines and schema checks
- Sondera Harness: https://github.com/sondera-ai/sondera-harness-python
- MCP catalog diffing and enabled-tool graph analysis
- least-privilege paired-tool test suites
- ARD-style capability registries with separate relevance and trust scores
- canary MCP clients that fuzz tool subsets for reconstructed hidden intent

Core sources:

- Autoformalization of Agent Instructions into Policy-as-Code: https://arxiv.org/abs/2606.26649v1
- Sondera Harness Python: https://github.com/sondera-ai/sondera-harness-python
- ShareLock: A Stealthy Multi-Tool Threshold Poisoning Attack Against MCP: https://arxiv.org/abs/2606.27027v1
- When Lower Privileges Suffice: Investigating Over-Privileged Tool Selection in LLM Agents: https://arxiv.org/abs/2606.20023v1
- AISafetyHub agent tool-selection bias repository: https://github.com/AISafetyHub/agent-tool-selection-bias
- Agent Finder for GitHub Copilot: https://github.blog/changelog/2026-06-17-agent-finder-for-github-copilot-now-available/
- Agentic Resource Discovery specification: https://commandline.microsoft.com/agentic-resource-discovery-specification-ard/
- hf-discover repository: https://github.com/huggingface/hf-discover

Implementability score: 0.70

Single-tool policy enforcement and catalog diffing are practical now. Robust defense against set-level tool poisoning and dynamic discovery abuse still needs adversarial fixtures and gateway-level discipline.

## Mutation and safety move below the prompt

The final strategic theme is enforcement placement. Phoenix routes issue-to-PR work through specialized agents, labels, baseline tests, post-patch comparison, layered safety controls, WAF handling, token expiry handling, permission boundaries, and flaky-CI paths. The Unfireable Safety Kernel makes the lower-level version explicit: separate the agent from a pre-action monitor, fail closed, and require signed external evidence before privileged actions mutate the world. The Trustless Agents paper reinforces the same worry from another angle: safety claims are weak when the runtime that reasons also owns the enforcement path.

Why it matters: if the model can mutate production directly, safety is advisory. The platform only owns the boundary when the target system refuses actions that did not pass the external monitor, state machine, broker, or kernel.

How it fits into the strategy stack: high-risk actions should move through state machines and reference monitors. The agent proposes an intent artifact. External policy, live-state checks, tests, credentials, and audit decide whether the artifact becomes a side effect.

Implementable now:

- route issue-to-PR work through labels, issue fields, baseline tests, post-patch comparison, branch protection, and role separation
- wrap one high-risk tool with an external reference monitor that logs allow, deny, timeout, and fail-closed outcomes
- remove standing write credentials where possible and mint scoped credentials only after policy approval
- require signed evidence packets for privileged tool calls
- reject direct mutation identities at target systems when a broker path is required
- measure monitor coverage, false positives, false negatives, time-to-response, and override frequency

Tools, repos, and methodologies worth exploring:

- GitHub label and issue-field state machines
- branch protection and baseline/post-patch CI comparison
- external reference monitors around shell, git, email, cloud, database, and deployment tools
- Cedar or OPA policy gates for signed action certificates
- workload identity, AWS STS, Kubernetes TokenRequest, and short-lived credentials
- fail-closed timeout policies and signed audit records

Core sources:

- Phoenix: Safe GitHub Issue Resolution via Multi-Agent LLMs: https://arxiv.org/abs/2606.20243v1
- The Unfireable Safety Kernel: https://arxiv.org/abs/2606.26057v1
- Can Trustless Agents Be Trusted?: https://arxiv.org/abs/2606.26028v1
- GitHub issue fields MCP support: https://github.blog/changelog/2026-06-18-duplicate-detection-and-issue-fields-mcp-support-for-github-issues
- PORTICO / Lingering Authority: https://arxiv.org/abs/2606.22504v1

Implementability score: 0.61

A wrapper around one dangerous tool is straightforward. A true kernel or broker architecture is harder because it must own credentials, target-system policy, fail-closed behavior, and evidence that the agent cannot forge.

## Strategic read

The sovereignty move is not owning the agent's words. It is owning the objects that determine what those words can change: authority manifests, memory records, capability catalogs, policy verdicts, scoped grants, and mutation monitors. Prompts can request. The platform has to decide.

## References

- LedgerAgent: Structured State for Policy-Adherent Tool-Calling Agents: https://arxiv.org/abs/2606.20529
- GitHub MCP issue fields support: https://github.blog/changelog/2026-06-18-duplicate-detection-and-issue-fields-mcp-support-for-github-issues
- GitHub MCP server: https://github.com/github/github-mcp-server
- Agentic Resource Discovery specification: https://commandline.microsoft.com/agentic-resource-discovery-specification-ard/
- GitHub Agent Finder: https://github.blog/changelog/2026-06-17-agent-finder-for-github-copilot-now-available/
- ToolPrivBench: https://arxiv.org/abs/2606.20023v1
- AgentRiskBOM: https://arxiv.org/abs/2606.21877v1
- PORTICO / Lingering Authority: https://arxiv.org/abs/2606.22504v1
- Securing LLM-Agent Long-Term Memory Against Poisoning: https://arxiv.org/abs/2606.24322v1
- MEM-INV-Bench / TMA-NM: https://github.com/yedidel/mem-inv-bench
- Governed Shared Memory for Multi-Agent LLM Systems: https://arxiv.org/abs/2606.24535
- The Unfireable Safety Kernel: https://arxiv.org/abs/2606.26057v1
- Can Trustless Agents Be Trusted?: https://arxiv.org/abs/2606.26028v1
- Autoformalization of Agent Instructions into Policy-as-Code: https://arxiv.org/abs/2606.26649v1
- Sondera Harness Python: https://github.com/sondera-ai/sondera-harness-python
- ShareLock: https://arxiv.org/abs/2606.27027v1
