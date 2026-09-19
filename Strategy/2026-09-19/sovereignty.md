# Strategy Daily Analysis - 2026-09-19

## Turn review findings into durable release state

GitHub's September 18 Copilot code-review update preserves review progress across commits and classifies findings as open, resolved since the last review, or previously missed. Each finding carries severity and an inline evidence link. Separately, GitHub made its code-coverage ruleset condition manageable through the REST API, including minimum line coverage and maximum tolerated coverage drop.

Together these releases expose a practical release-control pattern: agent findings should be stateful records, and deterministic quality thresholds should be policy objects. A review comment is not durable control. A finding needs identity, severity, evidence, transition history, resolution reason, and current applicability. Coverage should be enforced by repository rules rather than remembered in prompts or reviewer prose.

Why it matters: agent review becomes useful when its findings survive new commits and can be combined with non-model release gates. The agent can discover and explain. The platform must own state transitions and merge policy.

Practical tools and methods worth exploring now:
- persist finding IDs and map them across commit revisions;
- distinguish fixed, incorrect, won't-fix, reopened, and previously missed states;
- require a fresh review after evidence-bearing files change;
- manage coverage thresholds as infrastructure as code through the rulesets API;
- keep coverage, tests, security checks, and human approval as separate gates;
- retain exact commit, finding, rule version, and merge receipt.

Evidence caveat: these features are GitHub-hosted product controls. The coverage rule requires GitHub Code Quality and GitHub Team or Enterprise Cloud, and neither feature proves that the underlying review or threshold is sufficient.

Implementability score: 0.94

Core sources:
- [Copilot code review: An improved review experience](https://github.blog/changelog/2026-09-18-copilot-code-review-an-improved-review-experience)
- [Manage the code coverage ruleset condition with the REST API](https://github.blog/changelog/2026-09-18-manage-the-code-coverage-ruleset-condition-with-the-rest-api)
