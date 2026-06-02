# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: 2026-06-02 Daily Scan

### Ghost tool calls make precommit observation a privacy effect
Summary: Speculative tool dispatch can leak inferred user intent to external services before the agent commits to a branch. Read-only status and allow-lists do not undo observation; the control has to happen at issue time.

Analysis: [daily sovereignty analysis](2026-06-02/sovereignty.md#ghost-tool-calls-make-observation-before-commit-a-privacy-effect)
Durable topic: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md)
Core source: [Ghost Tool Calls](https://arxiv.org/abs/2606.02483v1)
Implementable now:
- classify external observation as an effect, not only mutation;
- keep speculative planning local when possible;
- add issue-time policy before precommit external calls;
- redact or project arguments before speculative dispatch;
- log branch state, speculative calls, suppressed calls, argument projections, and final commit path.
Tools, repos, and methodologies worth exploring:
- gateway-owned issue-time policy, OPA/Cedar, data-class labels, precommit/commit runtime states, argument projection, local tool simulators, speculative-call ledgers
Implementability score: 0.60

### AgentOps is converging into versioned runtime control planes
Summary: AWS AgentOps, Microsoft Agent Framework, and IBM’s agent-logic framing point at the same production shape: agents, tools, memory configs, identity, evals, traces, policies, and release gates become versioned runtime infrastructure.

Analysis: [daily sovereignty analysis](2026-06-02/sovereignty.md#agentops-is-converging-into-versioned-runtime-control-planes)
Durable topic: [Runtime Governance](runtime-governance/runtime-governance.md)
Core sources: [AWS AgentOps](https://aws.amazon.com/blogs/machine-learning/agentops-operationalize-agentic-ai-at-scale-with-amazon-bedrock-agentcore/), [Microsoft Agent Framework at BUILD 2026](https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-at-build-2026/), [IBM agent logic](https://huggingface.co/blog/ibm-research/agent-logic-and-scalable-ai-adoption)
Implementable now:
- version agent definitions, tool manifests, memory configuration, prompts, policies, and eval fixtures together;
- require pre-prod tests for identity propagation, tool authorization, memory access, HITL gates, and rollback;
- register agents, tools, skills, MCP servers, and ownership metadata;
- emit traces for decisions, tool calls, denied calls, memory use, cost, latency, errors, and outcomes.
Tools, repos, and methodologies worth exploring:
- Amazon Bedrock AgentCore Runtime, Identity, Memory, Gateway, Observability, and Agent Registry; Microsoft Agent Framework and Foundry; OpenTelemetry; MCP; A2A; Playwright CLI; policy-as-code; CI/CD release gates
Implementability score: 0.76

## Previous structured update

The prior daily scan for 2026-06-01 focused on organization-scoped runtime context and sandboxed AI-factory security: [2026-06-01 roundup](../roundups/2026-06-01.md).
