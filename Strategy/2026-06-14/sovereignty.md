# Strategy Daily Analysis: 2026-06-14

Today's strategy signal is that agent governance is crystallizing into reference architectures and runtime enforcement pipelines. Enterprise security was built for data boundaries; agent risk moves inside the workflow. The practical response is not more policy documents. It is compiled governance: five-plane architectures that bind authority through delegation chains, and skill-layer pipelines that turn user corrections into runtime checks.

## Five-plane reference architecture governs the agent runtime, not the data perimeter

Enterprise security was built to govern data boundaries: the protected surface was data at rest and in transit, and the controls — access control, data-loss prevention, perimeter inspection — governed crossings of that boundary. Production AI agents dissolve this assumption. An agent reads context, calls tools, invokes connectors, and modifies systems of record on an enterprise's behalf, so risk moves inside the workflow, into sequences of individually-permitted actions that may transform a business process no one authorized.

The paper presents a Five-Plane Reference Architecture for Runtime Governance of Production AI Agents:
1. **Substrate Plane** — compute, network, storage, and hardware attestation
2. **Control Plane** — orchestration, scheduling, and delegation chains with attenuating authority
3. **Data Plane** — context, memory, knowledge, and provenance-tracked artifacts
4. **Agent Plane** — the agent harness, its tools, skills, and execution traces
5. **Policy Plane** — compile-time rules, runtime guards, and audit evidence

Existing policy engines do not extend to this regime: they evaluate request-time decisions against atomic principals, where agentic systems require stateful evaluation against composite principals whose authority attenuates through delegation chains.

Why it matters: this is the first reference architecture that treats agent governance as a runtime substrate problem, not a prompt-safety problem. The five planes map directly to the operational surfaces that platform teams actually control.

How it fits into the stack: this deepens [Runtime Governance](../runtime-governance/runtime-governance.md), [Agent Gateway Governance](../agent-gateway-governance/agent-gateway-governance.md), [Agent Provisioning Governance](../agent-provisioning-governance/agent-provisioning-governance.md), and [Agent Network Containment](../agent-network-containment/agent-network-containment.md). It provides the architectural backbone for the Friday synthesis thesis on evidence-bearing control planes.

Practical tools, repos, and methodologies worth exploring now:
- Map your agent platform to the five planes; identify which planes lack compiled controls
- Replace request-time policy checks with delegation-chain authority evaluation
- Attach provenance to every context artifact, memory write, and tool output
- Build the Policy Plane as a separate compilation target, not scattered guardrails

Implementability score: 0.65

Core sources:
- [A Five-Plane Reference Architecture for Runtime Governance of Production AI Agents](https://arxiv.org/abs/2606.12320v1)

## TRACE compiles user corrections into runtime enforcement for coding agents

Interactive LLM agents are becoming part of daily work, but they do not reliably become easier to work with over time: a correction remembered in one session may still be violated in the next. The paper studies this gap between preference access and preference compliance. In tasks derived from anonymized real-user friction cases, Mem0 memory still leaves 57.5% of applicable preference checks violated.

TRACE (Test-time Rule Acquisition and Compiled Enforcement) is a drop-in skill-layer pipeline for coding-agent runtimes that mines user corrections, rewrites them as atomic rules, and compiles them into runtime checks that must pass before an agent completes future tasks. Unlike runtime checks written ahead of time by developers, TRACE skills come from the user's own chat corrections. The pipeline: correction → atomic rule → compiled check → enforced at task completion.

Why it matters: governance that depends on the model "remembering" preferences fails. Governance that compiles preferences into enforced checks works. TRACE moves preference compliance from the model's context window into the runtime's enforcement layer.

How it fits into the stack: this strengthens [Skills as Control](../../AgenticAI/skills-as-control/skills-as-control.md), [Agent Harness Architecture](../../AgenticAI/agent-harness-architecture/agent-harness-architecture.md), and [Runtime Governance](../runtime-governance/runtime-governance.md). It is the user-correction counterpart to the developer-written admission gates in the Friday synthesis.

Practical tools, repos, and methodologies worth exploring now:
- Add a correction-mining pass to your coding-agent runtime that extracts atomic rules from user feedback
- Compile rules into deterministic checks (linters, type checks, contract validators, custom predicates)
- Enforce checks at task-completion boundaries, not during generation
- Version the rule set per user/project so rollback and audit are trivial

Implementability score: 0.80

Core sources:
- [Getting Better at Working With You: Compiling User Corrections into Runtime Enforcement for Coding Agents](https://arxiv.org/abs/2606.13174v1)

## Strategic readout

The strategic readout is that agent governance is becoming infrastructure code. The five-plane architecture gives platform teams a map of what to build. TRACE gives product teams a pipeline that turns user friction into enforced guarantees. Both point to the same product boundary: the runtime must compile intent — whether organizational policy or user correction — into checks that execute before effects are visible.