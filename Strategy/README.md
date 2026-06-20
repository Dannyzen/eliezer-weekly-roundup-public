# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan, 2026-06-20

### Repo-native instructions and issue-field MCP make GitHub a governed agent substrate

Summary: GitHub Copilot code review now reads root `AGENTS.md`, and the GitHub MCP server can read/write issue fields. Repository instructions and structured work metadata are becoming agent authority surfaces.

Analysis: [daily sovereignty analysis](2026-06-20/sovereignty.md#repo-native-instructions-and-issue-field-mcp-make-github-a-governed-agent-substrate)
Durable topics: [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Runtime Governance](runtime-governance/runtime-governance.md), [Ticket-Native Agent Orchestration](../AgenticAI/ticket-native-agent-orchestration/ticket-native-agent-orchestration.md)
Core sources: [AGENTS.md support](https://github.blog/changelog/2026-06-18-copilot-code-review-agents-md-support-and-ui-improvements), [issue fields MCP support](https://github.blog/changelog/2026-06-18-duplicate-detection-and-issue-fields-mcp-support-for-github-issues), [github/github-mcp-server](https://github.com/github/github-mcp-server)
Implementable now:
- add concise root `AGENTS.md` files to repos where agents review code
- scope issue-field MCP writes by workflow identity
- log field mutations as work-state changes
Tools, repos, and methodologies worth exploring:
- GitHub MCP server, GitHub Projects custom fields, CODEOWNERS, branch protection, CodeQL, secret scanning, repository audit logs
Implementability score: 0.90

### Policy ledgers move governance before mutation

Summary: LedgerAgent makes governance executable by checking typed task state before side-effecting tools run. This is stronger than prompt-only policy because the policy has a structured state object to inspect.

Analysis: [daily sovereignty analysis](2026-06-20/sovereignty.md#policy-ledgers-move-governance-before-mutation)
Durable topics: [Runtime Governance](runtime-governance/runtime-governance.md), [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Evidence Provenance Control Plane](evidence-provenance-control-plane/evidence-provenance-control-plane.md)
Core source: [LedgerAgent](https://arxiv.org/abs/2606.20529)
Implementable now:
- split state observation from final action generation
- run policy checks against ledger fields before mutation tools
- record ledger snapshot hash, policy ID, verdict, and arguments in the trace
Tools, repos, and methodologies worth exploring:
- OPA, Cedar, signed tool manifests, OpenTelemetry policy spans, broker-mediated execution
Implementability score: 0.82

### Multi-agent scale creates an operations problem before it creates an intelligence problem

Summary: Enterprise-scale orchestration degrades because agent discovery noise grows with the population. The strategic layer needs service-catalog discipline, queueing, preemption, and assignment telemetry before it needs more specialist agents.

Analysis: [daily sovereignty analysis](2026-06-20/sovereignty.md#multi-agent-scale-creates-an-operations-problem-before-it-creates-an-intelligence-problem)
Durable topics: [Runtime Governance](runtime-governance/runtime-governance.md), [Agent Gateway Governance](agent-gateway-governance/agent-gateway-governance.md), [Agent Network Containment](agent-network-containment/agent-network-containment.md)
Core source: [Autonomous Event-Driven Multi-Agent Orchestration](https://arxiv.org/abs/2606.20058)
Implementable now:
- cap visible agents per workflow using capability metadata and reliability
- add priority, related-event merge, and preemption before large-agent planning
- make discovery failure and queue latency operating metrics
Tools, repos, and methodologies worth exploring:
- service catalogs, Temporal/Inngest/PubSub queues, OpenTelemetry, routing postmortems
Implementability score: 0.57
