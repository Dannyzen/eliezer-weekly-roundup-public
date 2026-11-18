# AgenticAI Daily Analysis: 2026-11-18

The strongest signal is that agent quality depends on preserved evidence and measured trajectories. Model scores alone hide retrieval leakage, cache economics, and information lost between workers.

## 1. Capture evidence before outcomes, then replay it

ForecastGym records the results from four commercial search APIs every two days while prediction-market questions are still open. After settlement, it replays those frozen evidence states so models, search providers, and memory strategies can be compared without letting later Web content leak the outcome.

Why it matters: live search mixes retrieval quality with reasoning quality, while retrospective search can expose facts that were unavailable when the prediction was made. ForecastGym found that rerunning the same queries after settlement returned results that nearly stated the outcome for up to 92 percent of questions despite date filters.

Implementable now:
- timestamp and content-address every retrieved result before the evaluated outcome exists;
- store provider identity, query, rank, snippet, URL, and capture time;
- replay identical evidence across models and memory strategies;
- score retrieval, interpretation, calibration, and final outcome separately;
- keep a live market or simple rule baseline beside model scores;
- retain immutable evidence-state manifests for every evaluation run.

Evidence and caveat: the first release contains 150 questions, 614 evidence states, and 131,000 search results. One question was cancelled and five had not settled, leaving 144 scored questions. Switching search providers moved Brier score by up to 0.043, more than the spread across tested models. Persistent notes performed similarly to rereading all evidence at about half the input tokens. The benchmark is forecasting-specific, uses four commercial search APIs, and some diagnostic labels use an outcome-aware model.

Artifact status: no public implementation artifact was resolved from the immutable abstract or full HTML during this run. The paper remains the verified source, and nothing was reproduced.

Implementability score: 0.78

Core source: [ForecastGym v1](https://arxiv.org/abs/2611.23045v1)

## 2. Price context by the whole trajectory

Context Has a Price evaluates context additions and deletions across more than 20,000 open-model coding-agent runs. It separates uncached input, cached input, and output tokens, then measures how the intervention changes later agent behavior.

Why it matters: shorter prompts and fewer search commands do not guarantee lower total cost. Context changes can break reusable prefixes or cause the agent to take more steps.

Implementable now:
- record uncached input, cached input, output tokens, steps, commands, and final resolution;
- calculate cost under the exact provider price vector used in production;
- isolate each run's own prefix reuse from cache warmed by sibling experiments;
- compare context interventions on matched tasks and seeds;
- require outcome parity before accepting a cost optimization;
- retain a full-context control and test rehydration paths.

Evidence and caveat: retrieved evidence reduced read and search commands by 18 to 34 percent, yet increased cost by 33 to 42 percent when cached input cost one tenth of uncached input, with no measurable resolution gain. Removing old observations saved 19 to 36 percent without a cache discount but increased cost by 38 to 116 percent with the discount. These results use seven open models, local serving, specific agents, and modeled price vectors. The associated implementation materials were announced but were not publicly resolved during this scan.

Artifact status: the paper and its documented use of mini-SWE-agent were inspected read-only. The study-specific implementation remains pending.

Implementability score: 0.88

Core source: [Context Has a Price v1](https://arxiv.org/abs/2611.22238v1)

## 3. Preserve conflicts through worker handoffs

Two papers isolate the same multi-agent failure from different directions. Multi-Agent Memory Inconsistency traces controlled factual conflicts through source reads, worker reports, lead evidence, and final reports. DebateGraph tests whether shared memory should collapse contradictions or expose the ranked conflict set to the debate.

Why it matters: more retrieval can produce worse answers when workers summarize evidence into isolated reports. Conflict resolution becomes impossible when the handoff removes one side of the contradiction.

Implementable now:
- require workers to return source-linked claims rather than conclusions alone;
- preserve contradictory claims as separate records with provenance and timestamps;
- compute pair recall at source, worker-report, lead-evidence, and final-report stages;
- permit overlapping source access for cross-document verification tasks;
- surface ranked conflict sets to the lead instead of silently selecting one winner;
- test handoffs with planted contradictions and equal-budget single-agent controls.

Evidence and caveat: across 73 controlled numerical conflicts in 11 Harvey LAB tasks, mandatory delegation raised source pair recall from 50.2 to 68.7 percent but lowered conflict detection from 16.2 to 13.2 percent. Workers reported both claims for only 35.2 percent of retrieved pairs. In DebateGraph, surfacing conflicts improved F1 by 0.340 with a 95 percent confidence interval of 0.267 to 0.414 and reduced successful attacks from 22 to 7 of 122 poisoned items at equal cost. Both evaluations are narrow: planted conflicts, limited domains, and small repeated-run counts.

Artifact status: both papers and their full HTML methods were inspected read-only. No study-specific repository was resolved and inspected during this run.

Implementability score: 0.82

Core sources: [Multi-Agent Memory Inconsistency v1](https://arxiv.org/abs/2611.22245v1), [Surfacing Disagreement Beats Resolving It v1](https://arxiv.org/abs/2611.22461v1)

## 4. Turn skills and MCP changes into regression tests

GitHub Copilot Evals adds repeatable tests for skills, custom agents, and MCP tools. Users define realistic tasks and expected behavior, approve each run, inspect failed checks, and compare runs before and after customization changes.

Why it matters: capability bundles change behavior across models and harnesses. A versioned eval provides an admission and regression gate instead of relying on one successful demonstration.

Implementable now:
- write one eval per critical skill, agent, or MCP journey;
- specify outcome checks and trajectory checks separately;
- pin the model, harness, customization versions, and task fixture;
- require approval before any eval with side effects;
- compare before and after runs and retain failed traces;
- keep production credentials and irreversible actions outside eval fixtures.

Evidence and caveat: this is a GitHub public preview for Copilot Individual, Business, and Enterprise. The release describes workflow and product availability, not independent reliability results or deterministic reproducibility across models.

Artifact status: official GitHub release documentation inspected. No extension or plugin was installed or executed.

Implementability score: 0.92

Core source: [GitHub Copilot Evals public preview](https://github.blog/changelog/2026-11-17-github-copilot-evals-is-now-in-public-preview/)

## Working conclusion

Build the evaluation substrate before tuning the model. Freeze evidence, account for the whole trajectory, preserve contradictions across handoffs, and rerun versioned evals whenever skills, agents, MCP tools, models, or harnesses change.
