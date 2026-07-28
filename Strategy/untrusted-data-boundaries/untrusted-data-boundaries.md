# Untrusted Data Boundaries

Last updated: 2026-07-10

Primary layer: Strategy / runtime governance / agent gateway governance

Implementability score: 0.72

Core sources:
- Untrusted Content Masking for Web Agents with Security Guarantees: https://arxiv.org/abs/2607.05277v1
- Untrusted Content Masking repository: https://github.com/ethz-spylab/untrusted-content-masking
- Agent Data Injection Attacks are Realistic Threats to AI Agents: https://arxiv.org/abs/2607.05120v1
- Your Agent's Memories Are Not Its Own: Forged Reasoning Attacks on LLM Agent Memory and Defenses: https://arxiv.org/abs/2607.05029v1
- SovereignPA-Bench: https://arxiv.org/abs/2607.05363v1
- Agentic Botnets and HalluSquatting: https://arxiv.org/abs/2607.07433v1
- Prismata: https://arxiv.org/abs/2607.08147v1

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

## July 9 update: hallucinated identifiers are untrusted evidence until resolved

HalluSquatting adds a resource-identity version of the untrusted-data problem. A model-generated repository, skill, package, or MCP server name is not a trusted artifact reference. It is an untrusted evidence string that must be resolved through a trusted catalog before it can influence clone, install, load, or execution.

Practical lesson:
- label model-suggested artifact names as `untrusted_identifier`;
- require exact source evidence for artifact identity before fetch;
- preserve the trusted source that supplied the URL, owner, publisher, version, and checksum;
- reject fuzzy or hallucinated identifiers for side-effecting acquisition paths;
- keep resource resolution and artifact admission in the trace.

Source:
- [Agentic Botnets and HalluSquatting](https://arxiv.org/abs/2607.07433v1)

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
- Agentic Botnets and HalluSquatting: https://arxiv.org/abs/2607.07433v1

## July 10 update: contextual least privilege must constrain observation and action together

Prismata adds the missing task-policy layer to untrusted-data boundaries. It derives privilege labels from page structure, limits which untrusted content reaches the planner, and restricts the actions available from that content. The structural rule is important: uncertain labeling should reduce privilege rather than silently widen it.

Practical lesson:
- label DOM regions by origin and trust class before planner exposure;
- derive a task-scoped action allowlist before the agent acts;
- redact unneeded untrusted content or expose it through a typed quarantine read;
- bind effectful actions to the content label, task scope, and policy verdict that authorized them;
- add adaptive attack fixtures and fail closed when labeling uncertainty could expand capability.

No public implementation repository was identified during this scan, so Prismata is currently a design reference rather than try-now software.

Source:
- [Prismata](https://arxiv.org/abs/2607.08147v1)

## July 18 update: head-branch agent instructions are untrusted control data

GitHub Copilot code review now reads multiple instruction and skill files from the pull request head branch. That improves testability, but it also means the proposed change can alter the reviewer's context. The new default firewall on GitHub-hosted review runners is valuable containment, yet it does not turn mutable branch content into trusted policy.

Practical lesson:
- classify base-branch policy and head-branch instructions separately;
- show instruction and skill diffs as first-class review evidence;
- require approval when a change widens setup, skills, runner type, or network access;
- keep self-hosted runners outside the GitHub-hosted firewall claim;
- treat repository-level usage metrics as activity evidence and join them to defects, reverts, rework, and lead time.

Sources:
- [Copilot code review customization and configurability](https://github.blog/changelog/2026-07-17-copilot-code-review-customization-and-configurability-improvements)
- [Repository-level Copilot usage metrics](https://github.blog/changelog/2026-07-17-repository-level-github-copilot-usage-metrics-generally-available)

## July 23 update: privileged agents need bounded residual input

Twin Agent turns privilege separation into a measurable context boundary. An Explore Agent sees untrusted content without privileged tools. A Safe Agent acts without raw untrusted context and receives only a compact, state-conditioned hint.

Practical lesson:
- isolate untrusted observation from privileged execution with separate principals;
- use typed hints and explicit size budgets rather than free-form summaries;
- bind every privileged action to user intent, target, policy, and hint provenance;
- sweep hint budgets and adaptive attacks in regression tests;
- treat compact text as untrusted evidence, never as authority.

Artifact caveat: the primary pages say code is available but expose no exact public repository URL that resolved during this scan. The paper is currently a design reference.

Source:
- [Twin Agent](https://arxiv.org/abs/2607.19595v1)

## July 26 update: issue content is evidence, not execution authority

IssueTrojanBench measures the failure directly. Across 4,176 runs, normal text channels reached 72.2 percent exploit success, while low-authority image alt text reached 16.7 percent. Prompt boundary markers did not stop malicious actions. GitHub's confidence, rationale, and optional approvals improve review flow, but GitHub explicitly says approvals are not a server-side security boundary.

Practical lesson:
- classify issue bodies, comments, PDFs, websites, and source comments as restricted evidence;
- use confidence and rationale to route review, never to widen capabilities;
- keep tokens, tools, repository scope, network, dependencies, and persistence least-privilege;
- require deterministic checks over user intent, evidence class, target, arguments, and effect;
- store proposal, reviewer decision, policy verdict, and server-side mutation receipt.

Sources:
- [IssueTrojanBench](https://arxiv.org/abs/2607.20759v1)
- [IssueTrojanBench artifact](https://doi.org/10.5281/zenodo.19245678)
- [GitHub issue automation controls](https://github.blog/changelog/2026-07-23-agent-automation-controls-in-github-issues-in-public-preview/)
- [Copilot automation security model](https://docs.github.com/copilot/concepts/agents/cloud-agent/about-automations)

## July 28 update: confine taint in engine-owned child trajectories

APPA offers a middle path between permanent whole-context taint and unsafe declassification. The runtime checks acquisition prospectively, isolates restricted reads in a child trajectory, and admits only checked derivatives or atomic one-call rulings back to the unchanged parent.

Practical lesson:
- label sources and sinks before observation;
- let child reads narrow only child authority;
- return typed, bounded, provenance-bearing derivatives;
- bind exceptional authority to one rendered call;
- preserve parent, child, labels, sanitizer, ruling, merge, and effect in one event log;
- evaluate authorized utility beside attack success.

Evidence caveat: APPA is an Archestra AI-authored preprint with an author-built benchmark and no public implementation artifact on the primary pages. Treat it as an architecture pattern pending independent replication.

Sources:
- [Agentic Permissions Policy Algebra](https://arxiv.org/abs/2607.24625v1)
- [ContainmentBench](https://arxiv.org/abs/2607.23999v1)
