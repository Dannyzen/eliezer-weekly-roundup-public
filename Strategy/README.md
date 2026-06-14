# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan, 2026-06-14

### Five-plane reference architecture governs the agent runtime, not the data perimeter

Summary: Enterprise security was built for data boundaries. Production AI agents dissolve this assumption — risk moves inside the workflow. The Five-Plane Reference Architecture maps the operational surfaces: Substrate (compute/network/storage), Control (orchestration/delegation chains), Data (context/memory/provenance), Agent (harness/tools/skills/traces), Policy (compile-time rules/runtime guards/audit evidence).

Analysis: [daily sovereignty analysis](2026-06-14/sovereignty.md#five-plane-reference-architecture-governs-the-agent-runtime-not-the-data-perimeter)
Durable topics: [Runtime Governance](runtime-governance/runtime-governance.md), [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Agent Provisioning Governance](agent-provisioning-governance/agent-provisioning-governance.md), [Agent Network Containment](agent-network-containment/agent-network-containment.md)
Core sources: [Five-Plane Architecture](https://arxiv.org/abs/2606.12320v1)
Implementable now:
- map your agent platform to the five planes; identify which planes lack compiled controls
- replace request-time policy checks with delegation-chain authority evaluation
- attach provenance to every context artifact, memory write, and tool output
- build the Policy Plane as a separate compilation target, not scattered guardrails
Tools, repos, and methodologies worth exploring:
- five-plane platform mapping, delegation-chain authority evaluation, provenance tracking, policy-as-code compilation
Implementability score: 0.65

### TRACE compiles user corrections into runtime enforcement for coding agents

Summary: Governance that depends on the model "remembering" preferences fails (Mem0 leaves 57.5% violated). TRACE mines user corrections, rewrites them as atomic rules, and compiles them into runtime checks that must pass before an agent completes future tasks. Correction → rule → check → enforced at task completion.

Analysis: [daily sovereignty analysis](2026-06-14/sovereignty.md#trace-compiles-user-corrections-into-runtime-enforcement-for-coding-agents)
Durable topics: [Skills as Control](../AgenticAI/skills-as-control/skills-as-control.md), [Agent Harness Architecture](../AgenticAI/agent-harness-architecture/agent-harness-architecture.md), [Runtime Governance](runtime-governance/runtime-governance.md)
Core sources: [TRACE](https://arxiv.org/abs/2606.13174v1)
Implementable now:
- add a correction-mining pass to your coding-agent runtime that extracts atomic rules from user feedback
- compile rules into deterministic checks (linters, type checks, contract validators, custom predicates)
- enforce checks at task-completion boundaries, not during generation
- version the rule set per user/project so rollback and audit are trivial
Tools, repos, and methodologies worth exploring:
- correction-mining pipelines, atomic rule compilation, deterministic check libraries, task-completion enforcement hooks, versioned rule stores
Implementability score: 0.80

## Previous structured update: Daily scan, 2026-06-13

### Prompt-injection risk should be scored by stakeholder harm and source locality

Summary: The strongest web-agent security signal today is that attack success is too blunt. Stakeholder-centric prompt-injection evaluation separates who was harmed, where the injected content entered, and whether the delegated task appeared to succeed while another stakeholder paid the cost.

Analysis: [daily sovereignty analysis](2026-06-13/sovereignty.md#prompt-injection-risk-should-be-scored-by-stakeholder-harm-and-source-locality)
Durable topics: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Runtime Governance](runtime-governance/runtime-governance.md)
Core sources: [Who Pays the Price?](https://arxiv.org/abs/2606.13385v1), [StakeBench/SBC](https://github.com/StakeBench/SBC), [PI-Hunter](https://arxiv.org/abs/2606.12737v1)
Implementable now:
- label prompt-injection tests by harmed stakeholder, attack objective, and source path
- log URL, DOM node, file, artifact, memory, tool output, or retrieved chunk that carried untrusted instructions
- score outcome success and process contamination separately
- add source-aware prompt-injection red teams to browser-agent and retrieval-agent CI
Tools, repos, and methodologies worth exploring:
- stakeholder harm matrices, source-locality traces, BrowserUse/NanoBrowser attack logs, source-aware red-team fixtures, process-level contamination metrics
Implementability score: 0.78

### Agentic workflows are now governed Actions resources

Summary: GitHub Agentic Workflows moves agent automation into the CI/control-plane layer. Natural-language Markdown workflow definitions compile into Actions YAML and inherit runner groups, policy constraints, read-only defaults, sandboxing, safe-output validation, and threat detection.

Analysis: [daily sovereignty analysis](2026-06-13/sovereignty.md#agentic-workflows-are-now-governed-actions-resources)
Durable topics: [Runtime Governance](runtime-governance/runtime-governance.md), [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Local-First Agents](local-first-agents/local-first-agents.md)
Core source: [GitHub Agentic Workflows public preview](https://github.blog/changelog/2026-06-11-github-agentic-workflows-is-now-in-public-preview)
Implementable now:
- review workflow Markdown and compiled YAML together
- bind runner group, sandbox image, repository, issue/PR, actor, model/agent, and policy constraints into the trace
- run read-only by default and require explicit approval for mutation
- require safe-output and threat-detection results before applying changes
Tools, repos, and methodologies worth exploring:
- GitHub Actions, runner groups, workflow-as-code review, sandbox/firewall policy, safe-output validation, threat-detection jobs, local policy queues
Implementability score: 0.82

## Previous structured update

The Friday synthesis for 2026-06-12 focused on stateful runtime governance: [week ending 2026-06-12 roundup](../roundups/2026-06-12.md).