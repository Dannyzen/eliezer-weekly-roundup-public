# AgenticAI Daily Scan: 2026-06-08

Today’s useful signal is about skill and search measurement. Skills are not magic context, and coding agents are not solved because a final patch passes. The agent stack needs to measure whether the right procedural control and the right repository evidence reached the run.

## Findings

### Declarative skills help only when retrieval is already good

Declarative Skills for AI Agents in Knowledge-Grounded Tool-Use Workflows is useful because it puts a boundary around the current skills hype. The paper compares a DeclarativeAgent with three domain-specific natural-language skill files, an ImperativeAgent with explicit state-machine phases, and an unscaffolded baseline across customer-service workflows over an unstructured knowledge base. The important result is not that skill files always win. The important result is conditional: retrieval quality is the dominant bottleneck, and skill files cannot recover evidence that the retriever failed to supply. Under high-quality retrieval, declarative skills improve procedural accuracy and reduce orchestration errors, while the imperative state machine is brittle and does not reliably improve task success or compliance.

The implementable move is to treat skills as procedural control that sits after evidence quality, not instead of it. A skill should declare workflow rules, preconditions, allowed tools, examples, and validators. The harness should then test no-skill, thin-skill, full-skill, and imperative-state-machine variants under the same retrieval conditions before promoting the skill to default behavior.

Why it matters: teams can waste months turning every workflow into state-machine code or bloated skill markdown. This paper says the right first question is whether the evidence substrate is good enough. If retrieval is poor, neither declarative nor imperative orchestration saves the agent.

How it fits into the stack: this belongs in the skills-as-control layer and the agentic-search layer. Skills are useful when they constrain procedure over real evidence. Retrieval remains the authority surface that decides whether the procedure has the right facts.

Implementable tools, repos, and methodologies:
- domain-specific skill files with explicit preconditions, workflow rules, examples, and validators;
- retrieval-quality tiers in evals, so skill gains are not confused with evidence gains;
- no-skill, thin-skill, full-skill, and imperative-state-machine baselines under identical retrieval;
- orchestration-error labels such as missing prerequisite, wrong phase, unsupported answer, and premature tool call;
- traces that record retrieved evidence, loaded skill hash, cited skill section, and final verifier outcome.

Implementability score: 0.84

Core source:
- Declarative Skills for AI Agents in Knowledge-Grounded Tool-Use Workflows: https://arxiv.org/abs/2606.06923v1

### Repository exploration should be scored before patch success

SWE-Explore isolates a capability that normal coding-agent benchmarks hide: finding the right code regions before editing. Instead of grading only whether the final patch resolves an issue, SWE-Explore asks an explorer to return relevant source files and line ranges under a fixed line budget. The benchmark covers 848 issues across 10 languages and 203 repositories, with line-level ground truth derived from independent successful repair trajectories.

That is the right measurement unit for coding-agent search. Patch success conflates repository understanding, context retrieval, code localization, diagnosis, editing, and testing. A coding agent can fail because it never opened the right file, because it found the right file but missed the decisive line, or because it found the evidence and edited badly. SWE-Explore makes the first two failures visible through coverage, ranking, and context-efficiency metrics.

Why it matters: context engineering for coding agents should not be judged only by green tests. The harness needs to know whether its search path gave the model the smallest sufficient evidence set.

How it fits into the stack: this belongs in agentic search, harness architecture, and trajectory-aware evaluation. It turns repo exploration into a separate eval layer that can be improved before full patch generation.

Implementable tools, repos, and methodologies:
- a fixed-line-budget explorer eval for internal repos;
- file-level and line-level coverage metrics;
- ranking metrics that reward putting decisive code regions early;
- context-efficiency metrics that penalize bloated evidence packs;
- traces that separate search, read, localization, diagnosis, edit, and verification phases;
- read-only inspection of SWE-Explore-Bench as a reference artifact before any manual sandbox run.

Implementability score: 0.80

Core sources:
- SWE-Explore: Benchmarking How Coding Agents Explore Repositories: https://arxiv.org/abs/2606.07297v1
- SWE-Explore-Bench repository: https://github.com/Qiushao-E/SWE-Explore-Bench

## Watchlist, not top findings

Socratic-SWE is highly relevant because it distills historical solving traces into structured agent skills and then generates targeted repair tasks, but no public implementation artifact was verified during this run. DuMate-DeepResearch is a good research-agent architecture signal for recursive search and rubric-grounded reasoning, but today’s stronger implementable signal is the smaller eval primitive: measure repository exploration and skill usefulness before adding another deep-research scaffold. AARRI-Bench is worth tracking for research-lifecycle evaluation, but it is less directly actionable than SWE-Explore for Danny’s agent-stack map.

## Scan quality note

Discovery covered arXiv category APIs and abstract pages, Hugging Face blog RSS, GitHub changelog RSS, vendor RSS feeds, GitHub Trending as a demand signal, and read-only GitHub repository metadata plus raw README files. `blogwatcher-cli` was missing, so feed discovery used direct RSS/API retrieval. The newest high-signal arXiv batch was submitted on 2026-06-05; this run did not force fake Monday freshness. External source code was not cloned, installed, built, downloaded, or executed.
