# AgenticAI Daily Analysis: 2026-09-15

## Thesis

Scale agent evaluation by controlling the search and spend, not by buying one larger context or one fixed multi-agent topology. Long traces need deliberate evidence expansion, while collaboration should be purchased only when problem difficulty predicts that it will pay.

## Freshness and evidence boundary

arXiv first listed the selected papers on Tuesday, September 15, 2026. The immutable v1 pages record submissions on September 11 or 12, so these are current listing-window findings after the weekend rather than strict trailing-48-hour submissions at scan time. The arXiv API returned HTTP 429; category pages, immutable v1 pages, HTML, and PDF text were used instead. Hugging Face Daily Papers, GitHub metadata, direct feeds, and web news were also scanned. No external repository was cloned, installed, built, imported, or executed.

## Search beyond the first plausible root cause

### Finding

Continual Search treats root-cause attribution as evidence search rather than one-shot judging. Across five settings, the method starts from the benchmark's normal first-pass diagnosis, then repeatedly asks the judge to challenge its standing answer and inspect unresolved evidence. MegaRCA-Mix contributes 50 human-annotated failures with a median execution record of 286K tokens; the other evaluated sets range from 2.4K to 100K median tokens.

After four continuation turns on MegaRCA-Mix, GPT-5.5 rose from 0.349 to 0.498 F1 and Opus-4.8 from 0.478 to 0.620. Evidence coverage for Opus-4.8 rose from 70.8 percent at turn one to 97.4 percent at turn four, while passive continuation plateaued at 77.0 percent. The useful control is the negative result: on short AgentRx and Who&When traces, extra search did not improve reliably and sometimes degraded performance.

### Why it matters

A long trace is not one prompt. Treating it as one invites early closure around the first plausible failure. The evaluator should carry an explicit unread-evidence set, open secondary artifacts such as configurations and raw logs, and stop when coverage or diagnostic confidence no longer improves.

### Fit in the stack

This belongs in trajectory-aware evaluation and observability. It turns artifact retrieval, diagnosis revisions, and stopping conditions into first-class evaluation events.

### Explore now

- Require every diagnosis to name inspected and uninspected evidence classes.
- Add a challenge pass that must open at least one previously unread artifact before revising or confirming the diagnosis.
- Cap turns by evidence coverage gain, not by a fixed reflection count.
- Use the one-pass judge as the control and report short-trace regressions separately.
- Preserve source-bound root-cause labels and exact trace identity.

### Caveat

The paper reports proprietary-model experiments, incomplete visibility into hidden reasoning, and possible label noise in massive traces. No paper-specific public implementation repository was exposed in the primary source. Treat the prompting pattern as implementable, not the reported scores as independently reproduced.

Implementability score: 0.82

Core source: https://arxiv.org/abs/2609.13463v1

## Route collaboration per problem and compare at equal spend

### Finding

The difficulty-aware topology study evaluates five collaboration topologies on 614 APPS, HumanEval+, and LiveCodeBench problems. Hierarchical collaboration beats a single agent by only 2.4 pass@1 points on the easiest third, but by 21.1 points on the hardest third, while consuming about 9.95 times the tokens. Its Difficulty-Aware Topology Selector predicts each topology's success probability and chooses the route that maximizes predicted success minus cost.

At 40 percent of the always-hierarchical token budget, the selector reaches 77.7 percent pass@1 versus 73.6 percent for always-hierarchical and 74.3 percent for the strongest learned comparator. The budget-matched protocol matters more than the specific graph model: a 39-feature representation performs within 1.3 points of heavier encoders, while comparing routers under one shared penalty coefficient lets spend vary from 30 to 52 percent and changes the ranking.

### Why it matters

A fixed multi-agent workflow wastes its largest cost multiple on the easiest work. The load-bearing idea is not "use more agents." It is "make topology a per-task route, then calibrate every candidate to the same realized spend."

### Fit in the stack

This belongs in multi-agent orchestration and model routing. Difficulty estimation happens before execution; the runtime then selects single-agent, peer, debate, or hierarchical paths under a common budget.

### Explore now

- Start with interpretable task features and historical route outcomes, not a new encoder.
- Keep each topology's cached success probability separate from the cost decision.
- Calibrate route penalties to one realized token or dollar budget on held-out tasks.
- Preserve a single-agent default for easy work and reserve hierarchy for predicted hard cases.
- Track route, predicted success, actual spend, outcome, and counterfactual route evidence.

### Caveat

This is a single-author study. Evaluation grids and analysis scripts are supplied as arXiv supplementary material rather than a verified public GitHub repository, and the 4.1-point result was not independently reproduced here. Transfer beyond code and the paper's 400-problem math study remains unproven.

Implementability score: 0.76

Core source: https://arxiv.org/abs/2609.13890v1
