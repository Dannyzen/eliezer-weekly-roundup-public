# Strategy Daily Analysis: 2026-05-14

Today's strategy signal is that always-on and background agents need provenance gates below the chat layer. The stronger the agent substrate becomes — memory, skills, cron, filesystem patches, local command execution, and cloud task APIs — the less credible it is to govern each surface in isolation.

## Always-on agents need provenance gates and OS-level sandboxes

Sleeper Channels and Provenance Gates is the most directly relevant security finding. It defines sleeper channels as persistent prompt-injection paths where an untrusted input enters through one surface, persists as memory, a skill, a scheduled job, or a filesystem patch, and fires later through a different surface when the attacker is no longer present. The paper's evaluated attack path is OpenClaw, not Hermes, but the abstract explicitly names always-on autonomous agents that fold messaging, memory, self-authored skills, scheduling, and shell into one authority boundary as the configuration class.

The defense shape is useful: tiered mediation with D2 provenance gates keyed on a canonical action-instance digest and one-shot owner attestations. The strategic lesson is that approval has to bind to the exact action instance and its provenance, not just to a natural-language paraphrase or a broad capability. Otherwise an attacker can launder a dangerous action through persistence, paraphrase, replay, or a different surface.

MCPShield is a supporting signal at the tool-traffic boundary. It encodes an MCP session as a graph of tool calls plus sequential and data-flow edges, then shows that content-level features over arguments and responses matter much more than metadata-only detection. The paper also warns that random splits inflate results; task-disjoint splits are necessary to avoid memorizing attack patterns. That is a useful governance principle: monitors should be evaluated on unseen tasks, not only on shuffled examples.

OpenAI's Windows Codex sandbox is the implementation pressure from local coding agents. The design separates real-user authority from sandbox users, blocks offline sandbox users with Windows Firewall rules, constrains writable roots, and uses a command runner to launch child processes under restricted tokens. This is not just Windows plumbing. It is the product shape for local agents: low-friction reads and workspace writes, explicit network modes, protected paths, and OS-enforced containment rather than prompt warnings.

GitHub's new Copilot cloud agent task API is the scale pressure. Once organizations can start background agent tasks programmatically across many repositories, they need job-level identity, repository scoping, secrets boundaries, progress traces, and provenance for who or what initiated each task. Automation APIs multiply the value of provenance gates.

Why it matters: a serious agent can no longer be governed by asking, "did the user approve this tool?" The better question is: which untrusted input influenced this action, where did it persist, which exact action digest is being authorized, which principal owns it, and what sandbox or firewall boundary contains the effect?

How it fits into the stack or strategy: this belongs in runtime governance, local-agent sandboxing, MCP/tool gateways, durable memory policy, skill governance, and background-agent operations. The control plane should mediate before persistence, before execution, and before cross-surface reuse.

Implementable now:
- bind approvals to canonical action-instance digests, not just natural-language descriptions;
- record provenance for memory writes, skill edits, scheduled jobs, filesystem patches, and tool calls;
- require one-shot or scoped owner attestations before persistent inputs can trigger later side effects;
- evaluate MCP/tool-call monitors on task-disjoint splits and content-aware argument/response features;
- run local coding agents in OS-enforced sandboxes with explicit writable roots, protected paths, and network-deny defaults;
- treat cloud-agent task APIs as privileged automation surfaces with identity, scope, and trace requirements.

Tools, repos, and methodologies worth exploring:
- sleeper-channel provenance gates: https://arxiv.org/abs/2605.13471 and https://github.com/maloyan/sleeper-channels
- MCPShield-style tool-call traffic monitoring: https://arxiv.org/abs/2605.11053
- OpenAI Codex Windows sandbox design: https://openai.com/index/building-codex-windows-sandbox
- GitHub Copilot cloud agent task API: https://github.blog/changelog/2026-05-13-start-copilot-cloud-agent-tasks-via-the-rest-api
- action digests, provenance DAGs, Open Policy Agent, Cedar, content-aware MCP telemetry, OS restricted tokens, firewall-deny defaults, and trace-linked approval artifacts

Implementability score: 0.58

Core source links:
- https://arxiv.org/abs/2605.13471
- https://github.com/maloyan/sleeper-channels
- https://arxiv.org/abs/2605.11053
- https://openai.com/index/building-codex-windows-sandbox
- https://github.blog/changelog/2026-05-13-start-copilot-cloud-agent-tasks-via-the-rest-api
