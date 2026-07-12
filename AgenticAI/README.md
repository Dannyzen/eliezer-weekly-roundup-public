# AgenticAI

This index tracks the most recent structured update. Each finding includes a short human-readable summary, a link into the detailed analysis, core sources, practical ways to explore it now, and an implementability score from 0 to 1.

## Most Recent Structured Update: Daily scan, 2026-07-12

### CodeQL makes system-prompt injection a static data-flow finding

Summary: CodeQL 2.26.0 adds `js/system-prompt-injection` for JavaScript and TypeScript, with provider models and tests for untrusted values flowing into system-prompt sinks. This turns one class of agent authority defect into a CI finding before deployment.

Analysis: [daily reasoning analysis](2026-07-12/reasoning.md#codeql-makes-system-prompt-injection-a-static-data-flow-finding)
Durable topic: [Agent Static Analysis](agent-static-analysis/agent-static-analysis.md)
Core sources: [GitHub changelog](https://github.blog/changelog/2026-07-10-codeql-2-26-0-adds-kotlin-2-4-0-support-and-ai-prompt-injection-detection), [public CodeQL query](https://github.com/github/codeql/blob/main/javascript/ql/src/Security/CWE-1427/SystemPromptInjection.ql)
Implementable now:
- enable CodeQL 2.26.0 on JavaScript and TypeScript agent services
- add positive and negative system-prompt taint fixtures
- extend local models for internal prompt builders and make high-authority findings merge-blocking
Tools, repositories, and methodologies worth exploring:
- `github/codeql`, CodeQL code scanning, provider model files, source-to-sink regression fixtures
Implementability score: 0.92

### GitHub Agentic Workflows compiles sandbox and failure policy into the workflow

Summary: The v0.82.8 prerelease adds gVisor runtime selection, reusable sandbox mounts, transitive import resolution, safe-output authorship disclosure, token-failure propagation, stale-lock protection, and idle harness termination. The workflow source is becoming a reviewable run contract.

Analysis: [daily reasoning analysis](2026-07-12/reasoning.md#github-agentic-workflows-compiles-sandbox-and-failure-policy-into-the-workflow)
Durable topics: [Agent Harness Architecture](agent-harness-architecture/agent-harness-architecture.md), [Sandbox-Native Agent Workers](sandbox-native-agent-workers/sandbox-native-agent-workers.md)
Core source: [GitHub Agentic Workflows v0.82.8](https://github.com/github/gh-aw/releases/tag/v0.82.8)
Implementable now:
- pilot gVisor on one self-hosted low-risk workflow
- define reusable read-only and writable mount partials
- preserve transitive imports, lock files, token outcomes, and safe outputs as run evidence
Tools, repositories, and methodologies worth exploring:
- `github/gh-aw`, gVisor-backed runners, shared sandbox partials, conclusion-job fixtures
Implementability score: 0.76

## Supporting recent AgenticAI context

The 2026-07-12 scan extends the week ending 2026-07-10 without replaying its papers. The concrete next layer is delivery enforcement: static source-to-prompt checks before merge, compiled sandbox policy before execution, and explicit failure evidence after the run.
