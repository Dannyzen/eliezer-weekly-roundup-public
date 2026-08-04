# Strategy Sovereignty Analysis - 2026-08-04

## Verdict

Policy inheritance is becoming a product surface, but the dangerous detail is composition. A team override system can decentralize governance without weakening the enterprise baseline only if authority merges are explicit, testable, and fail closed.

## GitHub team-specialized settings make policy composition operational

GitHub now lets enterprise administrators mark individual `managed-settings.json` keys as team-overridable, map team files through `team-mappings.json`, and add team-level plugins or marketplaces above an enterprise baseline. Enforcement spans VS Code, Copilot CLI, the Copilot App, and Copilot cloud agent for eligible Business and Enterprise users.

The unflattering fact is the merge rule: when a user belongs to multiple teams, team settings combine using the least restrictive value for each key before the enterprise file is applied. That is survivable for defaults and additive plugin catalogs, but dangerous for bypass permissions, model access, network scope, or tools with side effects.

Why it matters: bounded agents need the same hierarchy Danny uses elsewhere: owner policy, organization baseline, role specialization, run-specific grants, and immutable denials. Configuration files are useful only if the effective policy and merge proof are visible before execution.

Stack fit: runtime governance, gateway policy, identity, and agent authority manifests.

Implementable now:
- separate additive settings from security-sensitive ceilings;
- compile all inherited files into one effective-policy receipt per run;
- test multi-team membership and conflict cases in CI;
- make permissions, egress, credential scope, and release authority non-overridable by default;
- require pull-request review for changes to managed policy repositories.

Tools, repositories, and methodologies:
- `.github-private`, `copilot/managed-settings.json`, `copilot/teams/`, and `team-mappings.json`;
- JSON Schema, policy-as-code tests, effective-policy snapshots, and OPA or Cedar for independent enforcement.

Caveats: this is a GitHub Copilot Business or Enterprise capability, not a portable standard. The least-restrictive team merge needs adversarial tests before it is trusted for safety-sensitive controls.

Implementability score: **0.81**

Core source:
- Official GitHub changelog, 2026-08-03: https://github.blog/changelog/2026-08-03-enterprise-team-specialization-for-managed-settings

## Strategic implication

Choose explicit policy compilation over runtime guessing. Team-local flexibility is valuable, but only immutable ceilings and a visible effective-policy receipt keep specialization from becoming authority drift.
