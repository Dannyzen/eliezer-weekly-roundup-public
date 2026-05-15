# Strategy analysis: Daily scan 2026-04-25

Source window: 2026-04-23 to 2026-04-25

Today’s strategic signal is that agent safety is moving down into SDKs, permission profiles, and adversarial test loops. Policies that live only in prose are too weak for high-autonomy agents that upload files, escalate shell commands, resume sessions, browse hostile pages, or distribute intent across turns.

## Agent boundary safety is moving into SDK defaults and adversarial test loops
Core source: https://github.com/ComposioHQ/composio/releases/tag/py%400.11.6
Supporting sources:
- https://github.com/openai/codex/releases/tag/rust-v0.125.0
- https://arxiv.org/abs/2604.21860v1
- https://arxiv.org/abs/2604.21840v1
- https://github.com/openai/openai-agents-python/releases/tag/v0.14.5

Composio Python 0.11.6 is a small but important sovereignty signal: before auto-uploading a local file, it checks paths against a built-in sensitive denylist such as `.ssh`, `.aws`, and risky filenames. It also adds `@before_file_upload` modifiers, scoped hook composition, explicit blocked-upload errors, and tests for the upload path. That is the right direction. Agent tool SDKs should prevent obvious boundary violations before the model or tool router gets a chance to normalize them.

OpenAI Codex 0.125.0 reinforces the same pattern at runtime level. Permission profiles now round-trip across TUI sessions, user turns, MCP sandbox state, shell escalation, and app-server APIs. The release also says app-server logic respects explicitly untrusted project config instead of auto-persisting trust. This matters because a permission decision is not a chat instruction. It is state that must travel with the session and be enforced by the runtime.

The research papers show why this has to be adversarially tested. “Transient Turn Injection” distributes malicious intent across isolated interactions and exploits stateless moderation, with automated attacker agents searching for model-specific weaknesses. “TraceScope” shows the defensive mirror image: a sandboxed operator agent drives a real GUI browser to elicit phishing behavior, freezes an immutable evidence bundle, and a separate adjudicator checks a MITRE ATT&CK-style checklist on demand. Together they say: context-aware defense and evidence-preserving sandboxes are now table stakes.

Why it matters:
- Agents increasingly touch local files, credentials, shells, browsers, and remote APIs.
- A single missing path check can leak `.ssh`, `.aws`, tokens, customer files, or private project state.
- Stateless moderation misses attacks that distribute intent across turns or tools.
- Security reviewers need evidence bundles and traces, not only “the model said it was safe.”

How it fits into strategy:
- SDK layer: block sensitive local file uploads before tool execution;
- runtime layer: carry permission profiles across sessions, turns, sandboxes, shell escalation, and app-server APIs;
- moderation layer: aggregate session context instead of scoring each turn in isolation;
- sandbox layer: isolate browsing and high-risk execution while preserving immutable evidence;
- procurement layer: prefer agent platforms with visible boundary controls and adversarial-test hooks.

What is implementable now:
- Add denylisted path segments and filename patterns before any agent-managed file upload.
- Require `before_file_upload`-style hooks for tool routers that touch local files.
- Represent permission profiles as serializable data and attach them to every tool call and resumed session.
- Test stateless and stateful moderation separately with multi-turn attack fixtures.
- Run browser or phishing triage agents in disposable sandboxes that emit evidence bundles.

What remains architecture-heavy:
- Keeping denylist and allowlist policy current across operating systems and project layouts.
- Detecting sensitive content when the path itself looks harmless.
- Aggregating enough session context for safety without storing unnecessary private history.
- Producing audit-grade evidence bundles without leaking secrets into the audit log.
- Making permission-profile semantics portable across vendors and agent frameworks.

Practical tools, repos, and methodologies worth exploring:
- Composio sensitive file upload protection and `@before_file_upload` modifiers
- Codex permission profiles and app-server session APIs
- Multi-turn adversarial fixtures inspired by Transient Turn Injection
- Sandboxed browser/operator-agent pipelines inspired by TraceScope
- Sensitive-path and secret-content canaries in CI for agent tool integrations

Opinionated take:
If an agent can upload, browse, execute, or resume, safety must be enforced below the prompt. The minimum viable control plane is path blocking, permission profiles, session-level moderation, sandboxed execution, and evidence-preserving traces.

Implementability score: 0.78

## Strategic take

The sovereign-agent stack is becoming a boundary-control system. Local-first infrastructure matters, but the operational question is sharper: what can the agent see, upload, execute, resume, and remember, and which runtime object enforces that decision when the model is wrong?
