# Strategy Daily Sovereignty - 2026-07-15

## Daily thesis

Sovereignty is becoming concrete at two boundaries: where the runtime executes and how it resolves artifact identity. A local agent is useful only if device capabilities are exposed through narrow, reviewable tools. A skill or MCP server is trustworthy only if a model suggestion resolves to an exact, verified identity before installation or startup.

## PalmClaw makes the phone a bounded local agent runtime

### What the paper adds

PalmClaw runs sessions, memory, skills, tools, and the agent loop directly on Android. Instead of driving every task through long tap, swipe, and type sequences, it exposes device capabilities as typed tools with explicit arguments, structured results, and tool-specific execution boundaries. The paper reports an 11.5% relative task-success improvement and a 94.9% reduction in completion time against its strongest baseline.

The public repository is materially populated: Android/Kotlin runtime code, channels, memory, tools, skills, tests, documentation, and signed release history. Version 0.2.1 reports a single process-wide runtime owner, per-session turn coordination, ClawHub pre-install review, and 306 unit or instrumentation tests. Google provides a separate product-side signal through offline Gemma 4 and Functional Gemma mobile actions plus the Tensor SDK beta. That supports the on-device direction, but it is not evidence for PalmClaw's benchmark.

### Why it matters

A phone is not just another inference target. It contains sensors, files, messages, applications, and user presence. The right architecture is therefore not desktop automation shrunk to a screen. It is a local runtime with explicit capability adapters, Android sandboxing, per-tool permissions, and a visible operator surface.

### How it fits into the strategy stack

PalmClaw belongs in local-first agents and sandbox-native workers. The reusable pattern is on-device state plus narrow device tools, with cloud models treated as optional providers rather than the owner of local state or action authority.

### Practical tools, repositories, and methodologies

- inspect `ModalityDance/PalmClaw` as an Android runtime reference without assuming its security claims are proven;
- expose contacts, maps, files, camera, microphone, and settings as separate typed tools with explicit permission checks;
- keep secrets in Android-managed storage and bind every tool call to a session and principal;
- test local-only, remote-model, and selective-escalation modes on the same task set;
- evaluate AGPL obligations or obtain a commercial license before proprietary integration;
- compare PalmClaw's generic Android path with Tensor SDK and LiteRT options on supported Pixel hardware.

Implementability score: 0.76

Core sources:
- [PalmClaw paper](https://arxiv.org/abs/2607.13027v1)
- [ModalityDance/PalmClaw](https://github.com/ModalityDance/PalmClaw)
- [Google on-device AI with Tensor and Pixel](https://developers.googleblog.com/unlocking-the-next-era-of-on-device-ai-with-google-tensor-and-pixel/)

### Weakest point

The paper reports strong relative gains, but the public runtime was not built or executed in this read-only scan. Android sandboxing is not a complete policy layer, and the repository uses AGPLv3 plus a commercial-license option. Google Tensor support is also limited to specific Pixel hardware and terms.

## Skill and MCP trust must start from exact artifact identity

### What the paper adds

Skills That Don't Exist measures a supply-chain precondition at scale. Across 15,000 prompts and 12 model or agent configurations, every configuration hallucinated skill names. Average rates were 36.0% for standalone models and 36.9% for agents, rising to 43.1% on real developer questions. Retrieval grounding reduced one tested rate from 40.8% to 3.2%, but the best defended system recommended the correct skill only about one time in six.

This means recommendation quality and artifact existence are separate checks. A model-generated name must never become an install target by itself. GitHub's July Visual Studio update provides a narrow product-side implementation signal: MCP server configuration and asset fingerprints are compared with a trusted baseline at startup, and changed servers require review before running.

### Why it matters

The attacker does not need to compromise a popular package. The attacker can register a name that agents repeatedly invent. Fuzzy lookup, typo repair, marketplace search, and automatic installation all amplify the same failure. Prompt instructions to verify are insufficient because the model can repeat its original mistake during verification.

### How it fits into the strategy stack

This belongs in agent gateway governance and skills-as-control. Discovery can be model-assisted, but identity resolution, publisher policy, content hashing, permission review, and admission must be deterministic control-plane operations.

### Practical tools, repositories, and methodologies

- deny install, clone, skill load, or MCP startup when the requested identifier came only from model output;
- require exact registry, publisher, canonical URL, version, license, manifest hash, and permission profile;
- reserve repeated hallucinated names and alert on unresolved recommendations;
- fingerprint MCP configuration, assets, tool metadata, and executable identity, then reapprove drift;
- separate `not found`, `found but untrusted`, `trusted but changed`, and `approved` states;
- log requested name, resolution evidence, selected artifact, fingerprint, approval, and denial reason.

Implementability score: 0.90

Core sources:
- [Skills That Don't Exist](https://arxiv.org/abs/2607.12340v1)
- [GitHub Copilot in Visual Studio June update](https://github.blog/changelog/2026-07-14-github-copilot-in-visual-studio-june-update)

### Weakest point

The paper measures the attack precondition, not successful compromise rates in production. GitHub's fingerprint dialog covers changed MCP servers in one IDE, not malicious first installs or cross-registry skill squatting. The general control pattern remains straightforward and should be implemented outside the model.

## What to implement first

1. Require exact artifact identity and publisher proof before any skill or MCP install.
2. Add startup fingerprint checks and explicit drift states for installed tool servers.
3. Prototype one on-device agent flow using narrow typed device tools before enabling GUI-wide control.
4. Keep local execution claims separate from permission, supply-chain, and trace-governance claims.
