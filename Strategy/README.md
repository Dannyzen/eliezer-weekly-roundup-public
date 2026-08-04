# Strategy

This index tracks the most recent structured strategy research. Each finding includes a summary, detailed analysis, primary sources, practical paths, and an implementability score.

## Latest Structured Update: 2026-08-04

### Team specialization needs immutable policy ceilings

Summary: GitHub now supports team-targeted managed settings, team mappings, and additive plugin or marketplace configuration beneath an enterprise baseline. Multiple team files merge using the least restrictive value before enterprise controls apply.

Analysis: [daily analysis](2026-08-04/sovereignty.md#github-team-specialized-settings-make-policy-composition-operational)
Core source: [official GitHub changelog](https://github.blog/changelog/2026-08-03-enterprise-team-specialization-for-managed-settings)
Implementable now:
- separate additive preferences from non-overridable security ceilings;
- compile inherited settings into an effective-policy receipt;
- test multi-team conflict cases in CI.
Tools, repositories, and methodologies:
- `.github-private`, `managed-settings.json`, `team-mappings.json`, JSON Schema, OPA, Cedar
Implementability score: 0.81

## Current implication

Decentralize specialization, not authority. Permissions, egress, credentials, and release power should remain bounded by immutable ceilings and independently testable effective policy.
