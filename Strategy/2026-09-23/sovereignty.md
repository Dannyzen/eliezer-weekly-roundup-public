# Strategy Daily Sovereignty: 2026-09-23

## Semantic surfaces need control-plane treatment

Today's strategy signal is that two ordinary agent surfaces now carry governance weight. MCP metadata and tool outputs can redirect behavior before an external effect. Telemetry can make the full session observable, but its content settings can also create a new sensitive-data path.

## Treat MCP metadata and tool outputs as untrusted control inputs

A2M optimizes malicious tool metadata to attract agent selection, then uses execution traces to refine adversarial tool returns. On LiveMCPBench, direct attacks optimized on GLM-4.6 reached a 93.6 percent malicious tool invocation rate, 32.4 times the benign token cost under cognitive denial of service, and a 74.4 percent mean attack success rate across three consequence classes. Transfer to four other models without re-optimization remained material.

Why it matters: an MCP server can influence both which capability is selected and what the model believes after the call. Authentication and schema validity do not make descriptive metadata or returned content trustworthy.

Fit in the stack: gateway admission, untrusted data boundaries, and runtime isolation.

Tools and methodologies worth exploring now:
- bind tool admission to publisher, package digest, schema hash, endpoint origin, and reviewed metadata;
- diff descriptions and annotations as authority-relevant changes;
- separate relevance ranking from permission to invoke;
- treat tool output as tainted data with explicit provenance;
- cap tokens, retries, and tool-chain depth per invocation;
- isolate external tools from credentials, files, and network destinations they do not need;
- replay adversarial metadata and return fixtures against every supported model and routing policy.

Artifact status: `Lilaizhen/A2M` is public with a populated default branch, benchmark datasets, configurations, and attack modules. No repository license was detected. It was inspected read-only and was not installed or executed.

Evidence caveat: the study assumes an attacker can register a malicious tool. It evaluates one benchmark and a fixed ReAct-style MCP stack, uses three rollouts for candidate ranking, and does not systematically vary prompts, routing policies, tool renaming, safety wrappers, or tool-pool composition.

Implementability score: 0.78

Core sources:
- [A2M paper](https://arxiv.org/abs/2609.26761v1)
- [A2M repository](https://github.com/Lilaizhen/A2M)

## Standardize agent telemetry while keeping content capture off by default

GitHub Copilot now exports OpenTelemetry traces, metrics, and events through enterprise-managed settings. The trace links model calls and tool use across a session, metrics include token usage, and events can record edit acceptance or rejection. Prompt text, responses, and tool arguments are excluded by default.

Why it matters: agent observability is becoming a standard telemetry contract instead of a product-specific transcript viewer. The privacy boundary is part of the contract. Enabling content capture can expose code, file contents, prompts, and tool arguments.

Fit in the stack: fleet monitoring, enterprise governance, and incident reconstruction.

Tools and methodologies worth exploring now:
- send OTLP to a controlled backend or collector;
- preserve principal, task, session, model, tool, policy, and outcome identifiers;
- keep prompt, response, and tool-argument capture disabled until a documented need and retention policy exist;
- separate operational metrics from sensitive payload evidence;
- define access, retention, redaction, and deletion before rollout;
- verify exact client coverage because supported managed-setting properties differ by client;
- connect traces to external state checks before labeling an incident resolved.

Availability caveat: enterprise owners configure this through `managed-settings.json` and need an OTLP-compatible backend. Supported clients include Copilot CLI, VS Code, the Copilot app, cloud agent, and JetBrains IDEs, but property coverage varies.

Implementability score: 0.92

Core sources:
- [GitHub release note](https://github.blog/changelog/2026-09-22-opentelemetry-in-the-github-copilot-app)
- [GitHub OpenTelemetry documentation](https://docs.github.com/en/enterprise-cloud@latest/copilot/concepts/enterprise/opentelemetry)
- [Enterprise-managed settings guide](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/use-managed-settings/get-started)

## Strategy implication

Treat descriptions, tool returns, and telemetry payloads as policy-bearing data classes. Admit and isolate external tools before use. Export lifecycle evidence through a standard schema, with sensitive content excluded unless a governed investigation requires it.
