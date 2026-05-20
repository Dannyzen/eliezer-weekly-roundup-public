# Strategy Daily Analysis: 2026-05-18

Today’s strategy signal is that agent infrastructure is becoming a semantic trust boundary. Tool exposure, API documentation, and persistent memory are no longer neutral developer conveniences. They decide what agents can plan, what actions they can justify, and which untrusted inputs can survive into future sessions.

## Findings

### Agent-ready APIs need semantic documentation gates before MCP exposure

Core source: [Making OpenAPI Documentation Agent-Ready: Detecting Documentation and REST Smells with a Multi-Agent LLM System](https://arxiv.org/abs/2605.14312)

This paper is useful because it starts from an industrial failure mode instead of an abstract benchmark. An organization wanted to expose 16 production APIs, roughly 600 endpoints, through MCP-based agents. The early proof of concept failed at task planning, tool selection, and payload construction. The APIs were stable and structurally documented, but that did not make them semantically usable by agents.

The authors built Hermes, a multi-agent LLM system that detects documentation and REST smells at the endpoint level and generates diagnostic reports. Their evaluation identified 2,450 smells across the 600 endpoints, with deficiencies present in all analyzed operations. The organization responded by prioritizing selective endpoint adaptation, redefining documentation standards, and integrating automated documentation assessment into API governance workflows.

Why it matters: enterprise “agent enablement” will fail if teams bulk-wrap internal APIs as tools and assume OpenAPI validity is enough. Human-readable docs often rely on tribal knowledge, implied constraints, and examples that agents do not have. Agent-ready API governance needs semantic readiness checks before MCP exposure.

How it fits into the strategy stack: this belongs in agent gateway governance. The gateway’s job is not just auth and rate limiting. It also has to decide whether a tool surface is understandable, constrained, and safe enough for an autonomous planner.

Implementable now:
- add an agent-readiness review before exposing endpoints through MCP or tool registries;
- lint OpenAPI specs for missing descriptions, ambiguous parameter names, missing examples, unclear constraints, and non-standard REST patterns;
- generate small tool-use tasks from each endpoint and test planning, parameter binding, and error handling;
- expose only selected endpoints first instead of mirroring the whole microservice estate;
- require endpoint owners to fix semantic documentation gaps before agents can see privileged tools.

Tools, repos, and methodologies worth exploring:
- OpenAPI linters, Spectral, Schemathesis, Dredd, contract tests, MCP gateways, LLM-based documentation smell reviewers, OPA/Cedar policy gates, trace-linked tool-call evals

Implementability score: 0.86

### Sleeper memory poisoning turns personalization into a long-term attack surface

Core source: [Hidden in Memory: Sleeper Memory Poisoning in LLM Agents](https://arxiv.org/abs/2605.15338)

Sleeper memory poisoning is the delayed version of prompt injection. An attacker places malicious content in a document, webpage, repository, or other external context. A stateful assistant reads it and stores a fabricated memory. The attack can stay dormant until a later conversation retrieves that memory and uses it to steer an action.

The paper evaluates the full write-retrieve-execute pipeline. It reports poisoned memories being added up to 99.8% on GPT-5.5 and 95% on Kimi-K2.6. Among successful retrievals, poisoned memories caused attacker-intended agentic actions in 60% to 89% of evaluations across models. The strategic point is blunt: memory makes prompt injection persistent.

Why it matters: personalization cannot be treated as a harmless UX feature once the same memory can justify tool calls, emails, purchases, code changes, or data movement. A single untrusted document should not be able to create future authority.

How it fits into the strategy stack: this belongs in runtime governance and memory security. Persistent memory is now part of the trusted computing base. It needs provenance, taint, policy, and revalidation at use time, not only cleanup after a bad answer.

Implementable now:
- tag every memory write with source, trust tier, timestamp, and whether the source was user-authored, agent-inferred, or externally supplied;
- require confirmation or review before storing instruction-like or preference-like memories extracted from untrusted content;
- prevent external-descended memories from justifying sensitive actions by themselves;
- revalidate memory provenance at action time, not only write time;
- add sleeper-memory red-team fixtures using malicious docs, webpages, repository files, and emails;
- log which memories influenced each tool call or policy decision.

Tools, repos, and methodologies worth exploring:
- append-only memory logs, provenance DAGs, taint labels, OPA/Cedar policy checks, OpenTelemetry memory spans, memory diff review, prompt-injection fixtures, rollback and forgetting controls

Implementability score: 0.62

## Watchlist signals

RoadmapBench reinforces the same governance posture for coding agents: long-horizon development remains largely unsolved when tasks require multi-target version upgrades, median 3,700-line modifications, and edits across 51 files: https://arxiv.org/abs/2605.15846. That is not a reason to avoid coding agents; it is a reason to evaluate them on roadmap-shaped tasks before granting broad autonomy.
