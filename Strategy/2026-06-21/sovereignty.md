# Strategy Daily Analysis - 2026-06-21

Today's strategy signal is that agent capability access is becoming a governed marketplace problem. Discovery, repository guidance, issue mutation, and tool privilege choice are all authority surfaces. If the platform does not govern what an agent can find, what guidance it follows, and which privilege level it chooses, the model will invent the policy at runtime.

## Agentic Resource Discovery makes capability discovery a governed plane

GitHub Agent Finder and the Agentic Resource Discovery specification make tool discovery part of the control plane. Instead of hand-wiring every MCP server, skill, tool, canvas, and agent into a context window, an AI client can submit a task description to an ARD service and receive ranked matching capabilities with metadata.

The strategic detail is that ARD is not just search UX. Microsoft's announcement frames ARD as a common layer for publishing, indexing, and discovering agentic resources: agents, MCP servers, APIs, workflows, and other capabilities. Discovery responses can include function, operator, hosting location, invocation method, required authority, and trust or policy suitability. GitHub's implementation says Agent Finder can use a curated public catalog or a private enterprise registry, and managed settings decide which resources agents may discover and use. The docs also make the critical safety point: discovery does not mean silent installation.

Why it matters: the agent stack is moving from static tool catalogs to runtime capability discovery. That only works if discovery is scoped, logged, and policy-aware. Otherwise a capability marketplace becomes a permission-laundering path.

Strategic fit: agent gateway governance, agent discovery, context economy, enterprise agent operations, local-first registry design.

Implementable now:
- create a private registry of approved MCP servers, skills, agents, and workflows;
- expose discovery through a resolver that is scoped by principal, tenant, repo, workflow, and risk tier;
- record query text, returned capability IDs, publisher, media type, score, selected capability, install decision, and final tool exposure;
- make relevance score explicitly separate from trust score;
- never auto-install or auto-connect a discovered capability without an explicit policy or human approval.

Tools, repos, and methodologies worth exploring:
- GitHub Agent Finder and GitHub's public catalog;
- `ards-project/connectors` for Copilot/Claude/ChatGPT/Gemini-side discovery skills;
- `huggingface/hf-discover` as an ARD client/server reference implementation;
- MCP registries with allowlist enforcement;
- OpenTelemetry spans for discovery, selection, installation, denial, and use.

Implementability score: 0.84

Core sources:
- https://github.blog/changelog/2026-06-17-agent-finder-for-github-copilot-now-available/
- https://commandline.microsoft.com/agentic-resource-discovery-specification-ard/
- https://docs.github.com/en/copilot/concepts/mcp-management#agent-finder
- https://github.com/ards-project/connectors
- https://github.com/huggingface/hf-discover

## Least-privilege tool choice is not solved by general safety alignment

ToolPrivBench is strategically important because it isolates a failure most agent stacks still blur: choosing the correct privilege level is a capability, not a side effect of being generally safe. The paper defines over-privileged tool selection as selecting or escalating to a higher-privilege tool even when a lower-privilege alternative is sufficient.

The reported result is bad in the useful way: across eight domains and five recurring risk patterns, over-privileged tool selection is common among mainstream LLM agents and is amplified by transient failures. General safety alignment does not reliably transfer to least-privilege tool choice. Prompt-level controls help only partially, especially after tool failures. The authors release ToolPrivBench and a code repository, but the repository is young and should be treated as a benchmark artifact to inspect, not a mature dependency.

Why it matters: least privilege cannot live only in IAM. Agents choose among tools, retries, fallbacks, and escalations. A model can obey a generic safety prompt and still pick the admin-grade tool because it looks more reliable.

Strategic fit: agent gateway governance, runtime governance, tool routing, least-privilege policy, safety evaluation.

Implementable now:
- split tools into read, limited-write, broad-write, admin, and external-effect tiers;
- require the router to justify why a lower-privilege tool is insufficient before escalation;
- log transient failure, retry, fallback, and escalation events separately;
- test tool routers with paired lower/higher privilege alternatives;
- block high-privilege escalation when the lower-privilege path failed for a transient reason rather than insufficiency.

Tools, repos, and methodologies worth exploring:
- ToolPrivBench-style paired tool-choice tests;
- `AISafetyHub/agent-tool-selection-bias` for read-only benchmark inspection;
- OPA or Cedar rules over tool tier, task class, and escalation reason;
- gateway traces that include available lower-privilege alternatives.

Implementability score: 0.77

Core sources:
- https://arxiv.org/abs/2606.20023v1
- https://github.com/AISafetyHub/agent-tool-selection-bias

## Phoenix reinforces that coding autonomy belongs behind host-state policy

Phoenix belongs in Strategy as well as AgenticAI because it shows how a real issue-to-PR agent path fails operationally. The system uses a label-based GitHub webhook state machine, six specialized agents, baseline-aware test evaluation, and seven layered safety controls. Its useful admission is that even with correctness preservation, about half of manually inspected PRs were not well-targeted because planner localization failed.

Why it matters: coding-agent deployment is not a binary choice between autonomy and no autonomy. The operating model should move autonomy behind host-state policy: labels, issue fields, baseline tests, branch protection, code ownership, permission boundaries, and explicit PR review.

Strategic fit: ticket-native orchestration, runtime governance, GitHub as agent substrate, CI safety.

Implementable now:
- gate every autonomous issue run through label/state transitions;
- separate issue triage, reproduction, patching, testing, failure analysis, and PR creation;
- compare post-patch tests to baseline tests before PR creation;
- preserve failure states for WAF filtering, token expiry, permission denial, and flaky CI;
- use issue fields and branch protection as policy surfaces, not optional metadata.

Tools, repos, and methodologies worth exploring:
- GitHub webhooks, labels, issue fields, Actions, Checks API, branch protection, CODEOWNERS;
- SWE-bench Lite plus internal real-issue slices;
- baseline-aware CI comparison and generated-PR review queues.

Implementability score: 0.72

Core source: https://arxiv.org/abs/2606.20243v1
