# Strategy Daily Sovereignty: 2026-11-04

## Scope

The Wednesday, November 4 arXiv listing is live. The selected papers were submitted November 2 or 3 and first listed November 4. Primary paper pages and available public artifact pages were inspected read-only. No external source code was cloned, installed, built, imported, or executed.

## 1. Convert skill approval into effect-bound runtime obligations

RuntimeTickets turns a task's delivery contract into a frozen ticket of recipients, objects, amounts, budgets, unresolved risks, and source-linked obligations. A host may approve only a ticket that narrows its existing grant. Model-free gates then decide every outbound effect, and trusted witnesses record what happened for deterministic post-run decoding.

Why it matters: package scans and coarse tool allow-lists cannot tell whether a legitimate workflow sends the wrong object to an allowed destination. Security has to bind the approved purpose to the actual effect at the boundary where the effect can still be refused.

The practical control plane is:
- bind the ticket to task identity and the exact skill version;
- require every obligation to cite the skill lines and delivery contract it answers;
- let the host approve only a subset of its existing grant;
- validate recipient, object, amount, and budget before forwarding;
- observe egress and workspace effects with trusted witnesses;
- decode the signed account into obligation-level receipts without another model call.

The paper evaluates 60 malicious and benign twin pairs across unmodified Hermes Agent, OpenClaw, and Claude Code panels. It reports 0% overlooked attempted attacks and 0% blocked benign runs under RuntimeTickets, while a derived allow-list let 75% of attempted attacks through. The environment used mock receivers and synthetic canaries, and no paper-owned implementation repository was verified. The exact result should be treated as controlled evidence, not a production guarantee.

Implementability score: 0.62

Source: [RuntimeTickets](https://arxiv.org/abs/2611.03772v1)

## 2. Authorize the evidence behind every task-critical tool argument

Right Tool, Wrong Parameters isolates parameter poisoning: an agent still calls the intended tool, while untrusted content changes a recipient, amount, location, or other critical argument. AuthorityFlow constructs a task-specific map of which sources may support which facts, traces each candidate parameter to its evidence, then requires both semantic support and source authorization before dispatch.

Why it matters: instruction filters miss attacks that preserve the high-level action. A valid tool name says nothing about whether attacker-controlled text supplied the account number or destination. Tool arguments need their own authority and provenance checks.

The practical control plane is:
- identify task-critical parameters in each tool schema;
- define source authority per fact and use, rather than globally trusted sources;
- retain evidence links for direct and intermediate parameter derivations;
- require semantic support and authorized provenance before execution;
- block or repair the call before dispatch, then rerun the same verification;
- preserve the final evidence path in the effect receipt.

FactAuthBench contains 144 paired cases across banking, Slack, travel, and workspace tasks. With Qwen3.6-27B, no defense produced 93.06% attack success and 90.28% benign utility. AuthorityFlow reduced attack success to 9.03% with 82.64% benign utility. The verifier remains model-based, depends on adequate tool metadata and provenance, and adds inference overhead. No public implementation artifact was verified.

Implementability score: 0.70

Source: [Right Tool, Wrong Parameters](https://arxiv.org/abs/2611.04673v1)

## Deep Dive Wednesday: effect-bound skill execution

RuntimeTickets is the week's strongest finding because it composes the adjacent control problems into one runtime object. Skill provenance, task facts, host grants, parameter authority, route mediation, budgets, validators, witnesses, and receipts all meet in a frozen per-task ticket. The model may propose a narrower contract, while deterministic code owns the authority decision and incomplete evidence remains `Unknown`.

The durable analysis is [Effect-Bound Skill Execution](../effect-bound-skill-execution/effect-bound-skill-execution.md). It explains the protocol, the 60-pair and 246-account evidence, the send-centric limits, the missing public implementation, and a bounded implementation path for one skill and one effect family.

Implementability score: 0.62

Core source: [RuntimeTickets](https://arxiv.org/abs/2611.03772v1)

## Working conclusion

Approval must survive contact with execution. Bind skill runs to frozen effect obligations, and bind every critical argument to authorized evidence before the host commits the side effect.
