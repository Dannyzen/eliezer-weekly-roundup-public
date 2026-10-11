# Strategy Daily Analysis: 2026-10-11

## Thesis

Capability activation is a governance decision. An installed MCP server should not become ambient authority merely because an IDE session started, and a managed default model should be described honestly as a starting preference when users can still choose another model.

## Treat MCP startup as capability activation

GitHub's October 10 Copilot for JetBrains release adds enterprise-managed default models and a setting that disables automatic MCP server startup for Copilot and Claude. It also routes diagnostic fixes into agent mode when available.

The MCP control is the meaningful governance change. Automatic startup turns configuration into ambient capability activation. Disabling it creates a deliberate activation point, which is easier to log, review, and pair with session-specific task scope.

The model control has a narrower effect. Administrators can select the default model for new conversations, while users retain an explicit model picker. This is fleet steering and cost-quality guidance, not a hard model allow list.

Practical controls worth exploring now:
- disable automatic MCP startup for sessions that do not require external tools;
- record the exact MCP servers enabled at session start and when each becomes active;
- separate installed, configured, started, authorized, and invoked states;
- pair server activation with sandbox, network, credential, and tool-level policy;
- treat default-model settings as preferences unless a separate enforcement layer restricts model choice.

Limits: the release note describes JetBrains behavior. It does not claim per-tool authorization, sandboxing of remote MCP effects, or immutable model enforcement. Startup control reduces ambient authority but does not replace gateway policy.

Implementability score: 0.96

Core source: [GitHub Copilot for JetBrains release](https://github.blog/changelog/2026-10-10-new-controls-and-chat-improvements-in-copilot-for-jetbrains)

## Strategic conclusion

Make capability activation visible and intentional. Keep model defaults honest, keep MCP startup explicit, and bind every active server to runtime policy before a session can use it.
