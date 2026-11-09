# Strategy Daily Analysis: 2026-11-09

Today’s strongest control-plane signal is that coding-agent review provenance is becoming queryable and governable through the platform API.

## 1. Make review provenance a release input

GitHub now exposes Copilot code-review settings through REST and GraphQL APIs from enterprise to repository scope. Review and comment objects can carry explicit Copilot attribution, review effort, and the skills, MCP servers, and custom instructions Copilot reported as sources.

This turns configuration provenance from hidden session state into a policy and audit surface. A release system can ask which review policy was active, which tools and instructions informed the comment, and whether enterprise settings prevented repository-level override.

Why it matters: an AI review verdict is not self-proving. The useful object is a review receipt that binds actor attribution, effort, source configuration, repository policy, source SHA, and resulting disposition.

Use now:
- inventory enterprise, organization, and repository review settings through the API;
- persist attribution, effort, reported skills, MCP servers, and instructions with each review;
- bind the review receipt to the exact head SHA and policy version;
- separate reported sources from independently observed tool and effect evidence;
- reject release claims when required provenance fields are absent or policy scope is ambiguous.

Caveat: GitHub exposes what Copilot reports as sources. That is useful provenance, not proof that every source was faithfully applied or that the review is correct. Availability also depends on Copilot plan and administrator scope.

Implementability score: 0.91

Core source: [Copilot code review API management and attribution](https://github.blog/changelog/2026-11-06-copilot-code-review-api-management-and-review-overview-updates/)

## Working conclusion

Review provenance should be a release-gate input, not dashboard decoration. Capture the platform policy, reported context sources, reviewer identity, source SHA, and final disposition under one receipt, then require independent checks for consequential releases.
