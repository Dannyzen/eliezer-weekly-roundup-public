# AgenticAI Daily Reasoning - 2026-07-12

## Daily thesis

The strongest weekend signal is that agent controls are becoming ordinary engineering artifacts. Prompt injection can now fail CI, sandbox choice can be compiled into a workflow, and safe-output failures can become explicit job conclusions. This is more useful than another framework announcement because it moves agent safety from guidance into tools that already sit on the delivery path.

## CodeQL makes system-prompt injection a static data-flow finding

CodeQL 2.26.0 adds the `js/system-prompt-injection` query for JavaScript and TypeScript. It detects paths where untrusted user-controlled values flow into system-prompt sinks. GitHub also expanded sink models across OpenAI, Anthropic, Google GenAI, LangChain, OpenRouter, and agent APIs. The public query, library models, and provider-specific tests are visible in `github/codeql`.

Why it matters:

- system prompts often carry tool policy, data boundaries, and behavioral constraints;
- a user-controlled value entering that channel is a pre-execution authority defect, not only a bad-response risk;
- the check can run during code review before an agent is deployed;
- provider models and regression fixtures make the control inspectable and extensible.

Fit into the stack:

This belongs in the agent static-analysis layer. It is a concrete prompt-to-model taint check that can sit beside Agent BOM generation, prompt-to-tool reachability, loop-bound checks, dependency scanning, and secret scanning.

Implementable now:

- enable GitHub code scanning or CodeQL 2.26.0 on JavaScript and TypeScript agent services;
- add a positive fixture where request data reaches a system prompt and a negative fixture where it remains in a user-message channel;
- extend local CodeQL models for internal prompt builders and wrappers;
- make a new `js/system-prompt-injection` alert a merge blocker on high-authority agent services;
- pair the static query with runtime tests for retrieved content, tool output, memory, and action arguments, which this query does not cover.

Tools, repositories, and methodologies worth exploring:

- `github/codeql`;
- `javascript/ql/src/Security/CWE-1427/SystemPromptInjection.ql`;
- provider models under `javascript/ql/lib/ext/`;
- code-scanning required checks and small source-to-sink fixtures.

Implementability score: 0.92

Core sources:

- [GitHub changelog: CodeQL 2.26.0](https://github.blog/changelog/2026-07-10-codeql-2-26-0-adds-kotlin-2-4-0-support-and-ai-prompt-injection-detection)
- [CodeQL system-prompt-injection query](https://github.com/github/codeql/blob/main/javascript/ql/src/Security/CWE-1427/SystemPromptInjection.ql)

Caveat: this is a narrow but valuable check. It covers JavaScript and TypeScript source-to-system-prompt flows. It does not prove that retrieved documents, tool outputs, mutable memory, or model-generated arguments are safe at runtime.

## GitHub Agentic Workflows compiles sandbox and failure policy into the workflow

GitHub Agentic Workflows v0.82.8 adds `sandbox.agent.runtime: gvisor`, reusable `sandbox.agent.mounts` in shared partials, transitive `uses:` resolution, an AI-authorship `disclosure-header` safe output, and propagation of OAuth or missing-token failures into the conclusion job. It also fixes stale lock handling, a confused-deputy check, and idle Copilot harness termination.

Why it matters:

- sandbox backend and mount policy become reviewable workflow fields rather than runner folklore;
- shared partials can carry reusable containment policy across workflows;
- transitive imports and lock guards make the compiled workflow dependency surface more explicit;
- authentication failures and terminal safe outputs become durable workflow outcomes instead of disappearing inside the agent loop.

Fit into the stack:

This belongs in harness architecture and sandbox-native workers. The useful object is the compiled run contract: workflow source, imported partials, lock state, sandbox runtime, mounts, network policy, token state, safe-output type, and final conclusion.

Implementable now:

- pilot gVisor on one self-hosted, low-risk workflow;
- define reusable read-only and writable mount partials;
- preserve compiled lock files and transitive import identities as review artifacts;
- require conclusion jobs to surface token, firewall, safe-output, and idle-termination outcomes;
- verify that the chosen runner actually supports the declared sandbox backend.

Tools, repositories, and methodologies worth exploring:

- `github/gh-aw` v0.82.8;
- gVisor-backed runners;
- shared workflow partials for sandbox policy;
- safe-output schemas and conclusion-job regression fixtures.

Implementability score: 0.76

Core source:

- [GitHub Agentic Workflows v0.82.8](https://github.com/github/gh-aw/releases/tag/v0.82.8)

Caveat: v0.82.8 is a prerelease, and gVisor adoption still depends on runner topology, Docker-in-Docker choices, mount discipline, and local infrastructure validation.

## What to do next

1. Add CodeQL 2.26.0 to one JavaScript or TypeScript agent service and create a system-prompt taint fixture.
2. Express one agent workflow's sandbox backend, mounts, and terminal outcomes as a compiled contract.
3. Keep runtime prompt-injection and sandbox escape tests separate from static and configuration checks.
