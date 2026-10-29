# Strategy Daily Sovereignty Note, 2026-10-29

## 1. Compile reasoning workflows into constrained execution

GitHub Agentic Workflows is now generally available. A Markdown workflow compiles into standard GitHub Actions YAML. Agent jobs are read-only and sandboxed by default, while configured writes pass through separate safe-output jobs with scoped permissions. The release also adds budget forecasting, model routing, micro-VM isolation, and enclaves for cross-repository data boundaries.

Why it matters: reasoning should live inside an existing deterministic execution substrate instead of replacing it. The compiler, lockfile, runner policy, sandbox, output validator, and threat scan create inspectable boundaries around model behavior.

Fit in the strategy: governed workflow substrates, sandbox-native workers, and effect release gates.

Implementable now:
- keep builds, tests, linting, and deployment deterministic;
- compile reasoning tasks into reviewable workflow artifacts;
- default agent jobs to read-only access and restricted network policy;
- buffer writes as typed outputs and apply them in a separate scoped job;
- forecast model and threat-detection spend before enabling recurring runs;
- bind cross-repository work to explicit runner and enclave policy.

Weakest point: the safeguards are configurable, so a permissive workflow author can weaken them. GitHub also presents customer outcome claims that are not an independent benchmark.

Artifact status: the MIT-licensed public repository and v1.0.1 release metadata were inspected read-only. No external source was cloned, installed, imported, or executed.

Implementability score: 0.94

Core sources: [GitHub Agentic Workflows GA](https://github.blog/changelog/2026-10-28-github-agentic-workflows-generally-available/), [github/gh-aw](https://github.com/github/gh-aw)

## 2. Make conversation authority a runtime protocol

Concordat turns consequential agent conversations into finite-state protocols. Tool availability depends on protocol state, human-only decisions remain human transitions, and illegal calls are rejected before side effects.

Why it matters: authority is temporal. Verifying identity, proposing an effect, receiving confirmation, and applying the effect are different states with different legal capabilities.

Fit in the strategy: context-to-execution integrity and runtime governance.

Implementable now:
- encode approval order as state transitions;
- grant only state-legal tools;
- bind approval to the proposed effect;
- keep protocol violations and effect receipts;
- prevent delegated work from duplicating budgets or authority.

Implementability score: 0.79

Core sources: [Concordat paper v1](https://arxiv.org/abs/2610.37461v1), [public repository](https://github.com/miladsikaroudi/concordat)

## Working conclusion

Use deterministic platforms to contain reasoning and typed protocols to contain authority. The model can propose and interpret, while compiled workflows and runtime state decide what may execute.
