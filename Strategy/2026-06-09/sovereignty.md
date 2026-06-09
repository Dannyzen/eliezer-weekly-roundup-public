# Strategy Daily Scan: 2026-06-09

Today's strategic signal is provenance. Tool-using agents do not only read prompts; they create files, logs, intermediate artifacts, summaries, and handoff objects that later steps may treat as neutral context. That makes artifact lineage a security boundary.

## Findings

### Artifact provenance gaps are now an agent attack surface

Context-Fractured Decomposition Attacks on Tool-Using LLM Agents is the strongest governance finding today. The paper points at a deployment assumption that keeps breaking: many jailbreak defenses assume the dangerous instruction sits in one visible conversation. Real agents split work across tools, modules, files, logs, generated artifacts, and time. A later step may consume an artifact without seeing the original adversarial context or the transformation path that made it risky.

The paper names that failure mode the provenance gap and studies Context-Fractured Decomposition attacks, where cross-context, multi-step fragments become dangerous only when recomposed through the agent's workflow. That is exactly the shape serious agent systems need to defend: not only prompt injection, but instruction lineage across persisted state.

Why it matters: artifact-producing agents turn every workspace file, scratchpad, log, generated plan, browser note, memory entry, and tool result into potential future context. If the runtime cannot explain where an artifact came from, what touched it, what trust label it carries, and which later action consumed it, the gateway is blind to cross-step attacks.

How it fits into strategy: this belongs in agent gateway governance and runtime governance. The gateway should not only decide whether a tool call is allowed. It should preserve provenance over artifacts that may become instructions, evidence, memory, or execution inputs later.

Implementable tools, repos, and methodologies:
- assign origin, author, tool, session, task, trust level, and transformation lineage to every durable artifact;
- keep tool outputs, user-provided data, model-generated plans, logs, memories, and scripts in separate trust classes;
- propagate taint labels when artifacts are summarized, rewritten, moved, or converted into code/config;
- require policy checks before untrusted artifacts can become instructions, scripts, credentials, or privileged tool arguments;
- log artifact-read and artifact-write events in the same trace as tool calls and policy decisions;
- create regression fixtures where a benign-looking later file only becomes unsafe when linked to its origin.

Implementability score: 0.72

Core source:
- Context-Fractured Decomposition Attacks on Tool-Using LLM Agents: Exploiting Artifact Provenance Gaps: https://arxiv.org/abs/2606.09084v1

## Watchlist, not top findings

Collaborative Human-Agent Protocol is directionally right: human edits, approvals, escalations, and handoffs should be protocol events with durable evidence. RAILS is a plausible clearing-layer frame for agentic commerce, but it is still more architecture proposal than near-term build. Data Agents Under Attack deserves follow-up for enterprise analytics agents because it recombines database security, tool execution, and agent reasoning failures.

## Scan quality note

Discovery covered arXiv category APIs and recent pages, Hugging Face blog RSS, GitHub Trending as a demand signal, read-only GitHub metadata, Google News RSS, and direct primary-source verification. External source code was not cloned, installed, built, downloaded, or executed.
