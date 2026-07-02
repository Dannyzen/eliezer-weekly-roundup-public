# Daily Strategy Research - 2026-07-02

Thesis: trust in agent systems is moving toward licensed intermediate states. The strategic question is no longer whether an answer, patch, memory, or skill looks plausible. It is whether each state transition, dependency edge, and benchmark score carries enough evidence to be challenged later.

## Theoria makes informal reasoning auditable through licensed state transitions

Category: Strategy

Core sources:
- Theoria paper: https://arxiv.org/abs/2607.01223v1
- Theoria repository: https://github.com/zaladbar/theoria

Implementability score: 0.56

Theoria sits between formal proof assistants and opaque LLM judges. A candidate solution is rewritten into typed state transitions. Each transition must be licensed by an explicit justification, such as a citation, computation, or problem-given fact. The key invariant is completeness of change: every difference between consecutive proof states must be accounted for, so hidden premises become unlicensed mutations rather than silently passing through an LLM judge.

The reported results are strong enough to matter but not strong enough to treat as solved verification. On HLE-Verified Gold, Theoria certifies 105 of 185 text-only expert problems at 91.4% strict precision. On adversarial poisoned proofs, structured judges catch 94.7% versus 83.2% for holistic judging, with the biggest advantage on hidden premises and fabricated citations. The repository is public and current, but this is still an architecture to adapt, not a drop-in governance layer.

Why it matters: high-stakes agent work needs challengeable proof traces, not only scalar judge scores. Theoria's useful move is to make the verifier inspect each rewrite, not just the final answer. That maps directly onto agent runs where memory writes, tool outputs, delegated claims, generated tests, and final recommendations all mutate the system's believed state.

Strategic stack fit:
- Evidence Provenance Control Plane: each reasoning transition gets a source-owned license.
- Runtime Governance: unlicensed state changes become policy failures.
- Memory Authority Control Plane: memory updates need the same completeness-of-change discipline.
- Agent Execution Control Plane: final effects should be allowed only after required intermediate licenses exist.

Practical tools, repos, and methodologies worth exploring now:
- typed proof-state or reasoning-state schemas
- citation, computation, and problem-given-fact license fields
- diff checks between consecutive reasoning states
- verifier spans in OpenTelemetry or JSONL traces
- adversarial fixtures for hidden premises, fabricated citations, stale source swaps, and unsupported memory updates

The implementable thin version is a transition ledger: every high-risk answer or action gets a sequence of state changes, and every change names the evidence type that licensed it.

## Agent skill supply chains are authority graphs, not markdown folders

Category: Strategy

Core source:
- Skills Are Not Islands: https://arxiv.org/abs/2607.01136v1

Implementability score: 0.73

Skills Are Not Islands is strategically important because it turns the skill ecosystem into an authority graph. The paper models Agent Skill Supply Chains across skill, package, and service dependencies, then shows that skill metadata is often activation-ready but governance-poor. Recursive skill reuse can hide package inventory, and security signals often appear only in transitive dependencies.

The reported scale matters: the authors analyzed more than 1.43 million GitHub-backed skill records from a SkillsMP snapshot and found structural patterns that package-centric SBOM tools miss. Their recommendation set is concrete: typed dependency manifests, dependency-cluster management, risk-warning audit commands for skill infrastructure maintainers, and lockfile-like records for skill developers.

Why it matters: a skill can carry authority even when it never calls a tool directly. It can import procedures, packages, services, credentials, browser paths, or MCP server assumptions through its dependencies. If skill dependencies are implicit, governance cannot answer what capabilities the runtime admitted.

Strategic stack fit:
- Runtime Governance: loaded skills need dependency and risk metadata in the policy path.
- Agent Gateway Governance: service dependencies can become hidden external-effect paths.
- Agent Authority Manifests: skill dependency graphs belong in deployed-agent authority manifests.
- Agent Execution Control Plane: a skill should not cause effects outside its declared dependency and side-effect scope.

Practical tools, repos, and methodologies worth exploring now:
- skill SBOMs with skill/package/service edges
- skill lockfiles with exact source, path, commit, version, hash, and dependency graph
- risk warnings for transitive shell, network, credential, browser, memory, and repository authority
- cluster-level review for skills that share a dependency backbone
- CI checks that fail when a skill dependency graph changes without review

The immediate governance move is simple: never load a skill pack into a privileged runtime without a manifest, lockfile, and transitive authority review.

## Coding-agent benchmark governance needs source-only and replayable score rules

Category: Strategy

Core sources:
- RepoRescue paper: https://arxiv.org/abs/2607.01213v1
- Performance benchmark audit: https://arxiv.org/abs/2607.01211v1

Implementability score: 0.82

The coding-agent eval findings are primarily implementation work, but they also define a governance rule: a benchmark score is an authority claim. RepoRescue shows why a prompt instruction not to edit tests is weaker than runtime enforcement. The performance benchmark audit shows why reference patches and leaderboard ranks can be unstable under machine and scoring-rule changes.

For governance, the implication is that evaluation artifacts need admissibility rules. A submitted patch should declare whether it edited source, tests, dependencies, environment, or harness. A performance score should include replay environment, variance, reference-patch validity, and per-task weight. A benchmark that cannot expose those fields should not be used as strong evidence of coding-agent capability.

Practical governance pattern:
- enforce patch-scope rules at runtime, not in prompts;
- store source-only replay results separately from all-edits results;
- attach replay environment, machine type, scoring rule, and variance to every performance score;
- publish per-task score contribution so aggregate ranks cannot hide weak measurement;
- treat benchmark submissions as evidence packets, not as raw leaderboard rows.

## Watchlist

Adversarial Pragmatics: https://arxiv.org/abs/2607.01153v1 is useful for safety-eval label design because it separates task success, policy compliance, safety risk, refusal outcome, evaluator confidence, judge validity, diagnostic ambiguity, and taxonomy drift. It did not beat the top findings because the public seed is small, but it is a good next fixture source for prompt-injection and LLM-judge validation.

Antaeus: https://arxiv.org/abs/2607.01138v1 is useful for repository-level logic vulnerability detection because it prioritizes functions, grounds reasoning in repository context, derives safety conditions, and validates comparatively. It is narrower than today's control-plane findings but relevant to coding-agent security review.
