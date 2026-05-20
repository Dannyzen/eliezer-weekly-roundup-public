# Strategy Daily Scan: 2026-05-17

Today’s strategic signal is that LLM security evaluation needs explicit threat-surface coverage maps. A benchmark name is not a governance control. If the benchmark only covers a narrow slice of the threat model, passing it can create false confidence.

## LLM security eval needs coverage maps not benchmark name-dropping

`Talk is (Not) Cheap` builds a 507-leaf taxonomy of inference-time LLM attacks from 932 security studies and maps those attacks into a 4x6 Target x Technique matrix grounded in STRIDE. The audit finds that major benchmarks such as HarmBench, InjecAgent, and AgentDojo occupy non-overlapping cells and cover at most 25% of the matrix. Entire STRIDE categories such as Service Disruption and Model Internals lack standardized evaluation despite published attacks with high impact.

Why it matters: agent builders can no longer say “we ran the safety benchmark” without saying which threat cells were covered. An enterprise agent can pass jailbreak-style tests while still being vulnerable to tool-call abuse, token amplification, service disruption, model-internal attacks, cross-tenant leakage, or workflow injection. Governance needs a coverage artifact, not just a score.

How it fits into the strategy layer: this turns security evaluation into portfolio management. The organization should know which agent surfaces are tested, which are untested, which benchmarks overlap, and which threat categories have no regression coverage. That coverage map belongs next to policy, runtime telemetry, red-team planning, and release gates.

Implementable now:
- create a simple Target x Technique coverage matrix for each agent product;
- map current evals such as AgentDojo, HarmBench, InjecAgent, prompt-injection suites, and internal red-team fixtures into matrix cells;
- mark untested categories explicitly rather than hiding them behind aggregate scores;
- add Service Disruption, token amplification, Model Internals, tool-argument abuse, and retrieval/memory poisoning cases to the backlog;
- require release notes to state which threat cells improved and which remain untested.

Tools, repos, and methodologies worth exploring:
- STRIDE, OWASP Top 10 for Agentic Applications, AgentDojo, HarmBench, InjecAgent, garak, promptfoo, CyberArk FuzzyAI, Snyk Agent Scan, Semgrep/CodeQL for agent workflow dataflow, OpenTelemetry security traces.

Implementability score: 0.72

Core source: [Talk is (Not) Cheap: A Taxonomy and Benchmark Coverage Audit for LLM Attacks](https://arxiv.org/abs/2605.15118)

## Strategic implication

The serious move is to treat eval coverage as a governed artifact. A security dashboard should not only show pass rates. It should show threat-cell coverage, untested high-impact categories, last-run dates, failing traces, and the runtime controls attached to each category. This is how agent governance escapes benchmark theater.
