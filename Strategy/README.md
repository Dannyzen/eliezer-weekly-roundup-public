# Strategy

This index tracks the most recent structured strategy research. Each finding links to the dated analysis, durable topics, primary sources, practical methods, and an implementability score.

## Latest Structured Update: 2026-09-20

### Run a closed-world resolver before policy gates

Summary: Selection and authorization both assume that a model-emitted call resolves to a real tool and declared signature. Enforce exact registry membership and schema resolution first, especially when multiple MCP servers share a namespace.

Analysis: [daily strategy analysis](2026-09-20/sovereignty.md#run-a-closed-world-resolver-before-policy-gates)
Durable deep dive: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md)
Core source: [Closed-World Resolution Against Tool Hallucination in LLM Agents](https://arxiv.org/abs/2609.19425v1)
Tools and methodologies worth exploring now: closed-world registries, exact signature checks, qualified MCP identities, collision rejection, resolution receipts, separate resolution and policy failure classes
Implementability score: 0.94

## Current implication

A policy engine cannot govern an unresolved call. Bind the model's emitted name and arguments to one admitted contract before authorization, transaction policy, or execution begins.
