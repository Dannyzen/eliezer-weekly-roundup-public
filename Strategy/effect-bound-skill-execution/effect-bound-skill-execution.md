# Effect-Bound Skill Execution

## Overview

A skill should never carry authority merely because its package passed review. The useful unit of control is a frozen, per-task execution ticket that binds one task, one exact skill version, one subset of host grants, explicit effect obligations, budgets, unresolved risks, and the evidence required to prove what happened.

[RuntimeTickets](https://arxiv.org/abs/2611.03772v1) is the strongest finding of the week because it turns several recurring control-plane ideas into one executable protocol. Static skill scans remain admission evidence. Tool permissions remain a ceiling. Human approval remains a source of authority. The ticket connects those inputs to deterministic checks at the effect boundary and to receipts that a third party can recompute.

This belongs primarily in the Strategy layer. It defines where authority lives and what proof a runtime must retain. Agent frameworks, egress proxies, validators, and receipt stores are the implementation surfaces.

## Why it won the week

The other strong findings improve one boundary at a time:

- [Cross-Interface Authorization](https://arxiv.org/abs/2610.41397v1) binds approval to a route and rechecks state at commit.
- [When Neither Side Confirms](https://arxiv.org/abs/2611.02527v1) shows that destructive approval is usually absent across MCP servers and hosts.
- [Right Tool, Wrong Parameters](https://arxiv.org/abs/2611.04673v1) shows that an attacker can preserve the intended tool while poisoning a recipient or other critical argument.
- [Agent Skills](https://agentskills.io) defines a portable skill package, including instructions, scripts, references, and assets.

RuntimeTickets supplies the missing composition rule: convert task intent and package evidence into a narrow runtime object, enforce that object without trusting the model, and decode the run into obligation-level outcomes. It gives the stack a place to combine route identity, parameter provenance, budgets, skill digests, validators, and approvals.

## Core innovation

The paper defines a ticket as a tuple containing:

- a binding to the task and exact skill version;
- selected grants that must be a subset of the host grant;
- a host budget;
- source-linked obligations;
- unresolved risks.

A model proposes the ticket once before execution. The host freezes it only when it narrows existing authority. The model cannot expand the host grant. During execution, model-free gates evaluate each effect. The paper's reference obligations check the recipient, validate the transmitted object, and cap the cumulative amount sent.

The protocol then records an authenticated account of validations, decisions, completions, observed effects, stream seals, and closure. A deterministic decoder returns one of three states for each obligation:

- `Supported` when a closed and sealed account contains the required evidence;
- `Violated` when the account contains an authenticated counterexample;
- `Unknown` when evidence or coverage is incomplete.

That third state matters. Missing telemetry does not become compliance evidence.

## Why it matters

Static scanning asks whether a skill looks dangerous before a real task exists. A tool allow-list asks whether the deployment generally permits a capability or destination. Both miss the decisive question: did this exact run perform only the effects required by this exact task?

A malicious report-writing skill can send credentials to the same approved destination as the requested report. Destination allow-lists pass both sends. A call-level monitor may see only the shell command that launched the skill's script. RuntimeTickets moves the check to the network effect and validates the object and cumulative amount, not merely the command or endpoint.

The strategic implication is direct: capability catalogs should describe possible behavior, while execution tickets authorize actual behavior. One artifact should never do both jobs.

## Fit in the agentic stack

1. **Skill supply chain:** package digest, provenance, scanner results, and declared capabilities establish admission evidence.
2. **Task compiler:** user intent and trusted business facts become a typed delivery contract.
3. **Authority service:** the host selects a subset of existing grants, sets budgets, records unresolved risks, and freezes the ticket.
4. **Execution control:** route adapters normalize tool, API, CLI, GUI, and script effects into enforceable requests.
5. **Effect gates:** egress, filesystem, credential, payment, and destructive-action gates allow, deny, or defer.
6. **Witness plane:** trusted monitors record effects outside the skill's control.
7. **Receipt plane:** authenticated, chained records bind decisions and observed outcomes to the frozen ticket.
8. **Verification plane:** deterministic decoding yields supported, violated, or unknown obligations.

RuntimeTickets directly demonstrates the egress path. A production architecture must extend the same shape to files, credentials, database writes, money movement, account changes, and durable external sinks.

## Evidence from the paper

The paper builds 60 malicious and benign twin pairs from released skill datasets. Its runtime experiment uses unmodified Hermes Agent and OpenClaw, plus a Claude Code supplementary panel, with real driver models and owned mock receivers.

Reported results:

- 0.0% of attempted attacks passed RuntimeTickets;
- 75.0% of attempted attacks passed the deployment-wide allow-list;
- 0.0% of benign runs were blocked by RuntimeTickets;
- 246 gated accounts with 3,009 decisions were re-derived exactly;
- 8,400 tampered, truncated, or substituted log audits produced no false `Supported` result;
- 3,840 single-evidence removals never changed an obligation to `Supported`.

These results support the protocol shape. They do not prove production completeness.

## What remains conceptual or unproven

The benchmark uses mock services and synthetic canaries. The runtime comparison emphasizes outbound sends. The paper's three reference obligations were fixed by the delivery contract, while mandatory host obligations and unresolved-risk fields were empty in every evaluated ticket. The full activation layer and task inputs are withheld for safety, and no paper-owned public implementation repository was verified.

Production adoption still needs:

- canonical effect schemas for each sink family;
- trustworthy validators for objects and business facts;
- route-complete mediation across API, CLI, GUI, scripts, and MCP;
- race-safe commit checks for mutable external state;
- key management, receipt retention, redaction, and tenant isolation;
- human approval UX for tickets that cannot be resolved deterministically;
- negative tests proving that no unmediated route bypasses the gate.

The weakest point is policy compilation. A model-generated ticket can omit a necessary obligation even when it cannot widen authority. The guardrail is a mandatory host policy layer, schema-required fields, explicit unresolved risks, deny or defer on unknowns, and adversarial regression fixtures for every effect family.

## Practical tools and methodologies to try now

### 1. Define a minimal ticket schema

Start with task ID, skill digest, selected grants, expiry, recipients, object validators, cumulative limits, unresolved risks, and required receipt fields. Use JSON Schema or Pydantic for the contract, and reject missing mandatory fields before execution.

### 2. Gate one consequential boundary

Use a local egress proxy or a tool-dispatch wrapper for one narrow workflow. Normalize each request into recipient, object identity, amount, route, and current state. Permit only requests covered by the frozen ticket.

### 3. Keep authority outside the model

Let the model propose a narrower contract. Let deterministic code prove that the proposal is a subset of host grants. Require trusted code or a human to freeze the ticket.

### 4. Preserve source and parameter provenance

Record which trusted task fact supplied each critical argument. Apply the AuthorityFlow lesson to recipients, amounts, locations, account IDs, and repository targets before dispatch.

### 5. Emit recomputable receipts

Chain ticket digest, normalized request, gate result, witness observation, and completion status. Decode to `Supported`, `Violated`, or `Unknown` without a model.

### 6. Test bypasses, not only happy paths

Build benign and malicious twins. Include same-recipient exfiltration, alternate routes, stale approvals, partial execution, duplicate sends, validator failures, missing witness records, and tampered receipts.

Useful implementation surfaces include Pydantic or JSON Schema for contracts, Open Policy Agent or Cedar for host policy, eBPF or proxy controls for egress, OpenTelemetry for correlated observations, Sigstore-style signing for artifacts and receipts, and stateful test harnesses for replay and mutation testing.

## Implementation complexity

A single bounded egress workflow is feasible with normal engineering effort. A complete cross-interface system is architecture-heavy because every effect-bearing route and durable sink must be normalized, mediated, witnessed, and tested.

The practical sequence is:

1. one skill;
2. one effect family;
3. one deterministic validator;
4. one model-free gate;
5. one recomputable receipt;
6. adversarial twin and bypass tests;
7. broader route coverage only after the first boundary is proven.

## Implementability score

**0.62**

The protocol is implementable now as a narrow control-plane spike. General deployment requires substantial route inventory, validator engineering, key management, and operational proof. The paper does not provide a verified public implementation to adopt directly.

## Strategic implications for Danny's product thinking

This finding strengthens the view that useful agent autonomy comes from explicit control surfaces rather than broader prompts.

For Friend Nodes, managed agents, and client workflows:

- skills are reusable methods, not reusable authority;
- task intent should compile into a visible execution contract;
- the host owns the final grant and can only narrow from approved capabilities;
- every real side effect needs a deterministic gate and a receipt;
- missing evidence is `Unknown`, never success;
- approvals should bind exact effects, arguments, routes, state, and expiry;
- customer trust comes from inspectable contracts and receipts, not claims that the agent is safe.

The product opportunity is an execution-control layer that makes the contract visible before a run and makes the evidence inspectable after it. That is more defensible than another skill marketplace or static AI safety scanner.

## Core sources

- [RuntimeTickets: Source-Grounded Security Obligations for Agent Skills, arXiv:2611.03772v1](https://arxiv.org/abs/2611.03772v1)
- [RuntimeTickets full HTML](https://arxiv.org/html/2611.03772v1)
- [Cross-Interface Authorization for AI Computer-Use Agents, arXiv:2610.41397v1](https://arxiv.org/abs/2610.41397v1)
- [When Neither Side Confirms: Destructive Tool Approval Across MCP Servers and Hosts, arXiv:2611.02527v1](https://arxiv.org/abs/2611.02527v1)
- [Right Tool, Wrong Parameters: Defending LLM Agents Against Parameter Poisoning, arXiv:2611.04673v1](https://arxiv.org/abs/2611.04673v1)
- [Agent Skills open specification](https://agentskills.io)
