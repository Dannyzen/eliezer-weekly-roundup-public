# Strategy Daily Analysis: 2026-11-17

Today's strategy signal is that agent customization is an authority surface. Enterprises need provenance controls over skills, agents, hooks, MCP servers, executable extensions, and the runtime that loads them.

## 1. Govern customization origin and runtime separately

GitHub Enterprise Cloud can now require five Copilot customization categories to come from plugins or managed settings: skills, custom agents, hooks, MCP servers, and executable extensions. The `strictPluginOnlyCustomization` setting blocks standalone user and project sources. GitHub explicitly warns that plugin-only is not an allowlist, so organizations must pair it with `strictKnownMarketplaces` and plugin policy.

The related VS Code transition moves agent sessions from the older Local harness to the Microsoft Copilot harness by February 2027. The new harness can support managed permissions and sandbox restrictions that the Local harness cannot enforce. Selecting the harness does not enable sandboxing; those controls require separate configuration and verification.

Why it matters: catalog origin and runtime enforcement solve different problems. Approved provenance limits which capability bundles can enter the system. Runtime policy constrains what an admitted bundle can do. One without the other leaves a gap.

Implementable now:
- inventory skills, custom agents, hooks, MCP servers, extensions, and their current source;
- require plugin or managed-setting provenance for high-impact categories first;
- restrict eligible plugin marketplaces and pin required or blocked plugins;
- migrate representative sessions to the new harness before removing exceptions;
- configure permissions and sandbox policy explicitly;
- test that user, project, and unknown-marketplace customizations fail closed;
- preserve policy version, plugin identity, runtime identity, approval events, and effect receipts.

Evidence and caveat: these are current GitHub Enterprise Cloud controls for enterprise-issued Copilot Business or Enterprise licenses. Plugin-only does not imply enterprise-owned plugins, and the Copilot harness does not automatically activate sandboxing. This is product evidence, not an independent safety evaluation.

Artifact status: official GitHub changelog and migration guidance inspected. No software was installed or executed.

Implementability score: 0.88

Core source: [Control where GitHub Copilot customizations come from](https://github.blog/changelog/2026-11-16-control-where-github-copilot-customizations-come-from/)

Supporting source: [VS Code retires the Local harness in February 2027](https://github.blog/changelog/2026-11-16-vs-code-retires-the-local-harness-in-february-2027/)

## Working conclusion

Treat customization provenance and runtime enforcement as two gates. Admit only approved capability bundles, then constrain and audit their effects inside a policy-capable harness.
