# Strategy Weekly Sovereignty: 2026-11-06

The strategic finding this week is that writable context must never become authority by implication. Repository instructions, tool metadata, summaries, memory, and multimodal content can inform a plan. Consequential effects need a separate host-owned grant, current-state check, and receipt.

## 1. Keep authority outside writable context

Coding-agent memory files can steer secure-completion outcomes even when agents recognize the attack. ARCBench finds that many post-compaction violations occur while the rule remains present. The handoff-summary study shows that self-written summaries can introduce unsupported permissions or requirements. MCP tool-poisoning research measured real execution across framework, model, attack, and tool combinations rather than prompt compliance alone.

Why it matters: content awareness is not a security boundary. A model can quote the right rule and still choose the wrong effect.

Strategic fit: untrusted-data boundaries, context-compaction provenance, and host-owned authorization.

Implementable now:
- classify repository instructions, summaries, memory, tool descriptions, and tool output as untrusted claims;
- store policy, permissions, and revocations in a separate authoritative ledger;
- reauthorize after compaction, handoff, tool-set change, or stale-state detection;
- add poisoned-instruction and conflicting-request fixtures to release gates;
- use the [handoff-audit repository](https://github.com/Chuw1/handoff-audit) for read-only methodology reference.

Implementability score: 0.90

Core sources:
- [Security Impact of Coding Agent's Memory Files](https://arxiv.org/abs/2610.38521v1)
- [Do Agents Still Follow the Rules?](https://arxiv.org/abs/2611.03223v1)
- [When Do Summaries Become Instructions?](https://arxiv.org/abs/2611.06545v1)
- [MCP Tool Poisoning in Agentic AI Frameworks](https://arxiv.org/abs/2611.03555v1)

## 2. Compile consequential work into effect-bound tickets

RuntimeTickets proposes source-grounded security obligations for agent skills. The broader weekly evidence adds two requirements: the host must own destructive approval, and authorization must remain valid across GUI, CLI, API, script, and MCP routes that reach the same effect.

Why it matters: tool permission lists say what a component can call. They do not prove that a specific amount, recipient, path, or disclosure is authorized now.

Strategic fit: the agent execution control plane and effect-bound skill execution.

Implementable now:
- compile task intent into a signed or authenticated ticket with principal, effect, critical arguments, evidence requirements, expiry, and allowed route;
- intersect the ticket with host grants so a skill can only narrow authority;
- require deterministic preflight before dispatch and a matching sink receipt after execution;
- preserve `Unknown` and `Escalate` when required evidence is missing;
- use Cedar, Open Policy Agent, JSON Schema, and idempotency keys for a narrow first implementation.

Implementability score: 0.62

Core sources:
- [RuntimeTickets: Source-Grounded Security Obligations for Agent Skills](https://arxiv.org/abs/2611.03772v1)
- [Host-owned destructive approval](https://arxiv.org/abs/2611.02527v1)
- [Authorization across interface changes](https://arxiv.org/abs/2610.41397v1)

## 3. Treat traces and propagation as privacy-bearing state

PrivacyTrace reports 26.25 percent profile-inference success from tool-call traces versus 17.97 percent from priors across 1,000 synthetic profiles and 4,000 trajectories. Task-Graph Contextual Integrity shows why access control at the first hop is insufficient: the same item can become unsafe through cumulative or downstream disclosure.

Why it matters: observability and collaboration create a second data plane. Arguments, results, joins, and downstream routing can reveal more than the original prompt.

Strategic fit: gateway governance, trace retention, and route-scoped data authorization.

Implementable now:
- minimize logged payloads and separate operational metrics from content-bearing traces;
- bind sensitive items to purpose, recipient, retention, and propagation scope;
- prevent unauthorized joins across sessions and principals;
- test direct, cumulative, and downstream disclosures;
- use the [PrivacyTrace repository](https://github.com/AI45Lab/PrivacyTrace) as a read-only audit reference.

Implementability score: 0.68

Core sources:
- [PrivacyTrace](https://arxiv.org/abs/2610.41885v1)
- [Task-Graph Contextual Integrity](https://arxiv.org/abs/2610.39532v1)

## 4. Verify social engineering at the action boundary

Multimodal-SEA argues that attacks cross text, image, audio, and video surfaces while defenses are often measured in one modality. The operational control is modality-independent: compile the expected workflow before untrusted content is consumed, then verify the actual effect through a trusted channel.

Why it matters: another classifier does not close the gap between suspicious content and a completed browser, payment, or messaging action.

Strategic fit: browser authority, trusted-channel verification, and adversarial release testing.

Implementable now:
- define the allowed action graph before page or media ingestion;
- require trusted-channel confirmation for recipient, amount, destination, and scope;
- retain screenshots, DOM or accessibility evidence, tool events, and sink receipts under one case identity;
- test cross-modal attacks against the application workflow, not only the model response.

Implementability score: 0.76

Core source:
- [Multimodal-SEA](https://arxiv.org/abs/2611.08281v1)

## Strategic conclusion

The control plane should allow broad reading and narrow acting. Context can suggest. Only a current, effect-bound grant plus a matching receipt should authorize and prove a consequential change.
