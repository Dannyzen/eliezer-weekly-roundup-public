# Agent Static Analysis

Last updated: 2026-07-12

Agent static analysis is the preflight layer for source-code agent programs. It recovers the agent graph before execution so the runtime can see which prompts, models, tools, memories, policies, handoffs, and loops actually exist.

## Core thesis

Normal static analysis sees code. Agent static analysis has to see code plus framework semantics.

An agent constructor, a tool decorator, a memory attachment, a handoff declaration, a retry loop, a model call, and a policy wrapper may look like ordinary host-language calls. Operationally, they define who can observe what, which tool can be triggered, which state can grow, and which side effect can repeat. Those relationships need typed graph objects before the agent is allowed to act.

## Why this topic now

The 2026-07-04 scan surfaced two paired sources:

- AgentFlow: https://arxiv.org/abs/2607.01640v1
- When Agents Do Not Stop: https://arxiv.org/abs/2607.01641v1

AgentFlow introduces Agent Dependency Graphs for agent programs. Its ADG represents agents, prompts, models, capabilities, memory states, and control policies as typed nodes, with component, control-flow, and data-flow edges. The paper evaluates the method on 5,399 real-world agent programs and reports 238 taint-style prompt-to-tool risks.

IAL-Scan applies the same kind of framework-aware static recovery to infinite agentic loops. It builds an Agentic Loop Dependence Graph and checks whether repeated feedback paths can reach costly or state-growing operations without an effective bound. The paper reports 68 confirmed IAL failures across 47 projects, with 91.9% precision over manually reviewed findings.

The combined lesson is practical: agent preflight should recover the graph and check it before runtime.

## Core graph objects

A useful first ADG for an internal agent stack should include:

- agent nodes
- prompt and instruction nodes
- model and router nodes
- tool and capability nodes
- memory and context-store nodes
- policy and approval nodes
- handoff and delegation nodes
- external resource nodes
- loop, retry, and continuation nodes
- trace sink and audit nodes

Useful edge types:

- component dependency
- model-call dependency
- tool invocation
- prompt-to-tool taint
- memory-to-tool taint
- handoff and delegation
- policy coverage
- approval coverage
- loop feedback
- state growth
- external side effect

## Minimum checks to build now

1. Agent BOM generation: list all agents, prompts, models, tools, memories, policies, and external resources.
2. Tool reachability: identify which agent can invoke which tool and under which policy.
3. Prompt-to-tool taint: flag paths where untrusted prompts or retrieved context can steer high-risk tools.
4. Memory-to-tool taint: flag paths where mutable memory can steer shell, browser, external-send, deploy, or credential-use tools.
5. Loop-bound coverage: prove every feedback path that can hit model calls, tools, memory growth, or external side effects is covered by a real bound.
6. Handoff coverage: prove delegated agents inherit explicit scopes rather than ambient authority.
7. Policy gap report: list high-risk tools reachable without approval, grant, sandbox, or deny-audit coverage.

## Fit into the stack

Agent static analysis sits before the runtime and feeds every later layer:

- Coding-agent control plane: config and tool scope become graph nodes.
- Sessionful loops: feedback paths get explicit bounds.
- Skills as control: loaded skills and their side effects become dependencies.
- Agent harness architecture: fixtures can target graph-identified failure paths.
- Runtime governance: grants and policies can be checked against recovered reachability.
- Evidence provenance: every graph report becomes a preflight artifact attached to the run.

## Practical implementation path

Start narrow.

1. Pick one framework or internal agent DSL.
2. Parse agent constructors, tool declarations, model calls, memory attachments, policies, and handoffs.
3. Emit JSON nodes and edges.
4. Generate a human-readable Agent BOM.
5. Add two checks: high-risk tool reachability and loop-bound coverage.
6. Store the graph hash and finding list with the run trace.
7. Expand framework coverage only after the first extractor catches real issues.

## Tools, repos, and methodologies worth exploring

- Tree-sitter parsers for Python and TypeScript agent code.
- CodeQL or Semgrep rules for framework-specific constructs.
- Agent BOM JSON as a CI artifact.
- OpenTelemetry spans that include graph hash and policy coverage.
- Harness fixtures for prompt-to-tool taint, memory-to-tool taint, handoff leakage, and loop-bound gaps.
- Existing framework APIs from LangGraph, OpenAI Agents SDK, CrewAI, AutoGen, and Hermes plugin code as extraction targets.

## Implementability score

0.72

A useful internal version is implementable now. The first extractor only needs to handle the frameworks actually used in the stack. The hard part is generality: framework-agnostic precision across arbitrary public repos requires more research and many adapters.

## Core source links

- AgentFlow: Building Agent Dependency Graphs for Static Analysis of Agent Programs: https://arxiv.org/abs/2607.01640v1
- When Agents Do Not Stop: Uncovering Infinite Agentic Loops in LLM Agents: https://arxiv.org/abs/2607.01641v1

## July 12 update: system prompts are now a static taint sink

CodeQL 2.26.0 turns one part of the agent graph into a shipping control. The new `js/system-prompt-injection` query follows untrusted JavaScript or TypeScript values into system-prompt sinks. Its public provider models and tests cover OpenAI, Anthropic, Google GenAI, LangChain, OpenRouter, and agent APIs.

Practical lesson:

- run the query in CI for JavaScript and TypeScript agent services;
- extend CodeQL models for internal prompt wrappers and agent builders;
- keep positive and negative source-to-sink fixtures beside agent code;
- block merges when user-controlled data reaches system policy on high-authority services;
- keep runtime checks for retrieval, tool output, memory, and generated action arguments, which static system-prompt analysis does not cover.

Sources:

- [GitHub CodeQL 2.26.0 changelog](https://github.blog/changelog/2026-07-10-codeql-2-26-0-adds-kotlin-2-4-0-support-and-ai-prompt-injection-detection)
- [CodeQL system-prompt-injection query](https://github.com/github/codeql/blob/main/javascript/ql/src/Security/CWE-1427/SystemPromptInjection.ql)

## Working conclusion

Agent static analysis should become the agent equivalent of dependency scanning plus control-flow review. Before an agent runs, the platform should know what can influence its system policy, what it can call, what can loop, and which policy objects actually cover the dangerous paths.
