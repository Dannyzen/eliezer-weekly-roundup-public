# Strategy

This index tracks the most recent structured update. Each finding includes a short summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: 2026-05-20 Daily Scan

### Managed agents are splitting the brain from the sandboxed hands
Summary: Cloudflare’s Claude Managed Agents integration separates Anthropic’s agent loop from Cloudflare-controlled execution environments with sandboxing, egress policy, private connectivity, browser traces, email, custom tools, and observability.

Analysis: [sovereignty analysis](2026-05-20/sovereignty.md#managed-agents-are-splitting-the-brain-from-the-sandboxed-hands)
Durable topic: [Agent Sandboxing](agent-sandboxing/agent-sandboxing.md)
Core source: [Announcing Claude Managed Agents on Cloudflare](https://blog.cloudflare.com/claude-managed-agents/)
Implementable now:
- run agent sessions as separate execution principals;
- mediate outbound traffic through allowlisted egress proxies;
- inject credentials outside the sandbox instead of exposing raw secrets to the model;
- choose microVM/container backends for developer-style work and isolates for cheap high-scale execution;
- preserve browser recordings, logs, and sandbox state for audit.
Tools, repos, and methodologies worth exploring:
- Cloudflare Sandboxes, Cloudflare Containers, Dynamic Workers/isolates, Workers VPC, Cloudflare Mesh, Browser Run, Email Service, R2/KV/D1 bindings, egress allowlists, `cloudflare/claude-managed-agents`
Supporting sources:
- [Cloudflare docs: Set up Claude Managed Agents](https://developers.cloudflare.com/sandbox/tutorials/claude-managed-agents/)
- [cloudflare/claude-managed-agents](https://github.com/cloudflare/claude-managed-agents)
- [Take your local GitHub sessions anywhere](https://github.blog/news-insights/product-news/take-your-local-github-sessions-anywhere/)
- [Fix with Copilot cloud agent](https://github.blog/changelog/2026-05-19-easily-apply-copilot-code-review-feedback-with-copilot-cloud-agent)
Implementability score: 0.68

## Previous structured update

The prior daily scan for 2026-05-19 focused on managed coding-agent audit APIs, CI auto-fix delegation, and enterprise model placement: [2026-05-19 sovereignty](2026-05-19/sovereignty.md).
