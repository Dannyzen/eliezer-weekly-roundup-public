# Untrusted Data Boundaries

Last updated: 2026-07-07

Primary layer: Strategy / runtime governance / agent gateway governance

Implementability score: 0.72

Core sources:
- Untrusted Content Masking for Web Agents with Security Guarantees: https://arxiv.org/abs/2607.05277v1
- Untrusted Content Masking repository: https://github.com/ethz-spylab/untrusted-content-masking
- Agent Data Injection Attacks are Realistic Threats to AI Agents: https://arxiv.org/abs/2607.05120v1
- Your Agent's Memories Are Not Its Own: Forged Reasoning Attacks on LLM Agent Memory and Defenses: https://arxiv.org/abs/2607.05029v1
- SovereignPA-Bench: https://arxiv.org/abs/2607.05363v1

## Overview

Untrusted data boundaries are the control-plane layer between observation and authority.

An agent can observe many things: page text, issue comments, support tickets, CRM records, emails, API responses, search results, retrieved memories, summaries, and platform recommendations. Those observations are not equal. Some are trusted system state. Some are user-provided task data. Some are third-party content. Some are attacker-controlled. Some are old memories whose authority may have expired.

If the runtime flattens all of them into one context blob, the model is forced to solve security, provenance, and authorization inside private reasoning. That is the wrong layer.

The control plane should decide, before and after model exposure, which observations can influence planning and which evidence classes can authorize effects.

## Core thesis

Untrusted content is not just dangerous text. It is a restricted evidence class.

That means every observation should carry at least:

- origin principal or source;
- trust class;
- data class;
- task scope;
- allowed uses;
- derived-from lineage;
- expiry or supersession state;
- quarantine status;
- evidence-to-effect authorization rule.

The planner should not automatically see all raw observations. The action layer should not automatically trust all planner-cited evidence.

## Why this topic now

The 2026-07-07 scan surfaced three aligned failure modes.

1. Untrusted Content Masking shows the browser case. Web pages mix trusted interface structure with untrusted comments, reviews, ads, issue bodies, and repository content. UCM masks untrusted DOM regions before the planner sees them and exposes a typed quarantined read path.
2. Agent Data Injection shows the tool-output case. Malicious data can masquerade as trusted metadata or evidence without using instruction-like language.
3. FARMA shows the memory case. Forged reasoning traces can be stored and later retrieved as if they were the agent's own prior rationale.

Together, they make the same point: the system needs a boundary plane across browser, tool, and memory observations.

## Practical architecture

### 1. Label observations at ingress

Do not wait until action time. Label data when it enters the runtime.

Suggested labels:

- `trusted_system_state`
- `user_task_input`
- `operator_approval`
- `third_party_content`
- `user_generated_content`
- `tool_return_metadata`
- `tool_return_untrusted_field`
- `retrieved_memory`
- `derived_summary`
- `quarantined_answer`

### 2. Mask high-risk content before planning

For browser and document agents, untrusted text should be hidden from the main planner when possible. Use placeholders, element IDs, selectors, or structured object references.

When the task needs hidden content, expose a narrow quarantine tool:

- input: element ID plus a specific natural language question;
- output: typed value such as bool, int, float, enum, date, or bounded string;
- trace: source element, question, model, answer type, answer, and policy verdict.

### 3. Split tool outputs by trust class

Tool responses should not return one blob that mixes trusted metadata and untrusted fields. Use explicit fields.

Example shape:

```json
{
  "trusted_metadata": {"record_id": "...", "source_system": "..."},
  "user_content": "...",
  "external_content": "...",
  "derived_summary": "...",
  "trust_policy": {"allowed_effects": ["read", "summarize"]}
}
```

### 4. Gate effects by evidence class

High-risk actions should ask: which evidence class caused this action?

Examples:

- A third-party review can inform a summary, but should not authorize a payment.
- An issue comment can inform triage, but should not authorize secret access.
- A recalled memory can personalize wording, but should not override current user approval.
- A quarantined answer can answer a narrow question, but should not carry free-form instructions.

### 5. Preserve lineage through summaries and memory

Summaries and memories must carry their source authority. If a summary erases origin, untrusted content can reenter later as apparently trusted context.

## Implementable now

- Add `trust_class`, `origin`, `derived_from`, `allowed_uses`, and `expires_at` to tool outputs and memory records.
- Mask untrusted DOM regions in controlled internal web apps and test pages.
- Build prompt-injection and data-injection fixtures for comments, reviews, tickets, emails, README files, and API responses.
- Require high-risk tool calls to cite evidence objects, not only natural language reasons.
- Add policy checks over evidence class before external sends, purchases, deploys, account changes, data exports, and memory writes.
- Log boundary events: observe, mask, quarantine-read, derive, retrieve, authorize, deny, and effect.

## Tools, repos, and methodologies worth trying

- `ethz-spylab/untrusted-content-masking` for browser masking, quarantined model reads, WebArena GitLab tests, WASP attack experiments, and automatic boundary detection.
- AgentDojo-style security fixtures for tool and data injection.
- FARMA-style memory poisoning tests for forged reasoning traces.
- OPA, Cedar, OpenFGA, or custom policy code over evidence class and action target.
- OpenTelemetry trace spans for evidence lineage and boundary decisions.
- Local markdown or JSON fixtures for seeded attack content before running against real SaaS.

## What remains conceptual or fragile

- UCM is strongest on controlled or labelable surfaces. Arbitrary web pages need reliable boundary detection.
- ADI's advertised artifact repository did not resolve during this cron run, so the method is paper-backed but not yet verified as a usable public tool.
- Typed quarantine answers reduce instruction flow, but they do not solve every side channel. A bounded string can still carry adversarial payloads if the receiving layer treats it as authority.
- Memory summaries are especially dangerous because they can launder source authority unless lineage is preserved.
- Human-facing UX is still underdeveloped. Operators need to see why a piece of evidence was allowed or denied without reading every trace span.

## July 7 update: browser, tool, and memory channels are one boundary problem

The daily scan's top security findings should be treated as one design primitive, not three isolated papers.

- UCM says untrusted browser content should be masked before planning.
- ADI says untrusted tool data should not be allowed to masquerade as trusted metadata.
- FARMA says untrusted or forged reasoning should not become trusted memory.
- SovereignPA-Bench says personal agents should be tested against platform-mediated incentives and consent drift.

The product implication is clear: agent runtimes need an evidence boundary plane. It should sit below prompts and above effects, mediate browser, tool, and memory observations, and preserve enough lineage for action-time authorization.

## Implementation checklist

- [ ] Define observation trust classes.
- [ ] Add trust metadata to tool outputs and memory records.
- [ ] Mask untrusted page regions before planner exposure.
- [ ] Add a typed quarantine-read tool.
- [ ] Require effectful actions to cite evidence object IDs.
- [ ] Deny high-risk effects justified only by untrusted content.
- [ ] Preserve lineage through summaries, embeddings, and handoffs.
- [ ] Add ADI, prompt-injection, and forged-memory regression fixtures.
- [ ] Trace observe, mask, quarantine, derive, retrieve, authorize, deny, and effect events.
- [ ] Review boundary-policy diffs before widening tool or memory authority.

## Source notes

Primary sources:
- Untrusted Content Masking: https://arxiv.org/abs/2607.05277v1
- UCM repository: https://github.com/ethz-spylab/untrusted-content-masking
- Agent Data Injection: https://arxiv.org/abs/2607.05120v1
- FARMA forged reasoning memory attack: https://arxiv.org/abs/2607.05029v1
- SovereignPA-Bench: https://arxiv.org/abs/2607.05363v1
