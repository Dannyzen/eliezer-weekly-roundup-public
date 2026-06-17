# Strategy Daily Analysis: 2026-06-17

Today's strategy signal is that evidence provenance is becoming the real control plane. Agent systems are not trusted because they use tools, cite sources, or add tests. They are trusted when every claim, source, skill, route, test, and merge decision has replayable evidence.

## Evidence provenance is becoming the control-plane primitive

Core sources:
- ProvenanceGuard: Source-Aware Factuality Verification for MCP-Based LLM Agents: https://arxiv.org/abs/2606.18037v1
- All Smoke, No Alarm: Oracle Signals in Agent-Authored Test Code: https://arxiv.org/abs/2606.18168v1
- Zscaler agentic AI security platform announcement: https://www.zscaler.com/press/zscaler-unveils-new-product-innovations-secure-agentic-ai
- Salesforce Agentforce Multi-Agent Orchestration: https://www.salesforce.com/agentforce/multi-agent-orchestration/

ProvenanceGuard and All Smoke, No Alarm describe the same governance problem from two execution surfaces. In MCP-grounded answers, pooled evidence can hide cross-source conflation: a claim may be true somewhere while attributed to the wrong source. In coding-agent pull requests, test-file presence can hide weak verification: 80.2% of analyzed agent-authored test patches contained weak or no explicit oracle signals. Both cases break naive governance dashboards. A system can look sourced or tested while the actual evidence chain is missing.

The market is moving in the same direction. Zscaler is packaging an AI Broker, Agent Registry, and AI Access Graph around MCP/A2A traffic, agent permissions, identity, and data lineage. Salesforce's multi-agent orchestration page frames the primary agent as a routing point to specialist agents with observability and policy controls. The vendor language is not proof of product maturity, but it validates the strategic category: the agent platform is becoming a governed evidence and delegation plane.

Why it matters: the enterprise control boundary is no longer just user identity or network access. It is claim provenance, tool provenance, skill provenance, test provenance, and delegation provenance. If those records are absent, the organization cannot distinguish real verification from theater.

How it fits into the strategic layer:
- MCP governance: captured traces need source IDs, tool IDs, and raw outputs.
- Coding-agent governance: test gates need oracle-signal checks, not only file counts.
- Multi-agent governance: primary-to-specialist delegation needs agent identity, route reason, policy scope, and final evidence.
- Security operations: agent registries and access graphs should connect permissions, data lineage, and trace evidence.

Implementable now:
- require every high-risk agent answer to carry claim-to-source evidence, not only citations;
- make MCP source IDs stable enough for audit and replay;
- run oracle-aware checks on agent-authored test files before merge;
- log agent identity, selected specialist, delegated task, tool surface, policy verdict, and output evidence for multi-agent handoffs;
- treat vendor AI brokers and access graphs as design references, but keep local evidence schemas portable.

Tools, repos, and methodologies worth exploring:
- MCP trace schemas, source-aware factuality checks, source IDs, claim decomposition, NLI or entailment checks, test-oracle linters, mutation testing, CodeQL/AST rules, OpenTelemetry spans, OPA/Cedar policy, OpenFGA-style relationship graphs, agent registries, access graphs.

Implementability score: 0.78

## Strategic implication

The winning control plane will not merely decide which model or agent gets a task. It will preserve why that agent was allowed, which evidence it used, which source owned each claim, which test oracle verified the code, and which policy bound the handoff. Without that, a multi-agent system is just a faster way to produce plausible artifacts with weak provenance.

## Watchlist

- Salesforce's primary-agent and specialist-agent model is a useful enterprise product shape, but the page is product documentation, not an independent evaluation.
- Zscaler's announcement is strong market validation for agent identity, MCP/A2A brokers, data lineage, and endpoint/plugin controls. Treat it as strategy signal, not proof that the full control plane is solved.
- ProvenanceGuard's harder multi-source result matters: exact source-plus-relation accuracy is still weak when sources are semantically similar. Portable evidence schemas are implementable now; perfect attribution is not.

## Scan quality note

This scan used primary arXiv pages/API metadata, selected PDF text verification, managed extraction for source pages, Google News RSS as lead discovery only, and official vendor pages for strategy signals. External repositories were not cloned, installed, built, imported, or executed.
