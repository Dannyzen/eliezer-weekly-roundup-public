# Strategy Daily Analysis: 2026-10-17

## Thesis

Tool approval is weak when the approved description and the server's real host capabilities diverge. The runtime must constrain the process effect, because a benign tool name cannot bound ambient filesystem authority.

## Sandbox the server effect, not the tool description

“My Credentials, Please” defines filesystem capability laundering: attacker-influenced arguments cause an MCP tool to access files outside the scope implied by its contract and deployment. Across 21,097 MCP servers from nine registries, 787 of 4,806 triaged servers, or 16.4%, showed filesystem capability signals despite non-filesystem classification. Three-case dynamic validation confirmed 150 vulnerable instances under the tested policies, and coordinated disclosure produced 13 advisories, including two CVEs in Anthropic's Git MCP Server.

The governance implication is concrete: client approval of a tool call cannot substitute for process-level least privilege. A local stdio server commonly inherits the user's filesystem permissions, so a narrow schema or approval prompt can authorize a process with much broader power.

Implementable now:
- launch each server with explicit read-only and read-write roots;
- remove ambient access to home directories and credential stores;
- resolve real paths after symlink expansion before authorization;
- bind allowed roots to exact server revision, tool identity, and deployment context;
- test exploit, benign-operation, and sandbox-containment cases before admission;
- fail closed when the sandbox or path policy is unavailable.

Implementability score: 0.86

Core source: [My Credentials, Please paper v1](https://arxiv.org/abs/2610.22301v1)

The weakest point is the denominator. The 787 cases are screening signals, while 150 are dynamically confirmed instances under the paper's tested policies. The paper describes MCP-FSD in detail but did not link a public implementation artifact in the primary source, so reproducing the ecosystem scan requires meaningful security engineering.

## Strategic implication

Capability governance belongs below model narration. The durable object should bind server revision, tool contract, process permissions, path policy, sandbox health, and observed effects. Approval can then authorize one constrained effect rather than an ambient process.
