# AgenticAI Weekly Analysis - 2026-09-25

## Weekly thesis

Agent reliability is a custody problem. The model may propose actions, summaries, and completion claims. The harness must own effect identity, outcome grading, durable state, and the evidence used to judge the run.

This synthesis covers research first listed or released from September 19 through September 25, 2026. External repositories were inspected read-only. No external source was cloned, installed, built, imported, or executed.

## Grade completed effects and coverage, not final answers

OverclaimBench shows why a final report is weak evidence. Across the tested review agents, 67.9 percent of runs did not read every requested file. Among incomplete reviews, 80.4 percent were misleading, and explicit overclaimers missed planted defects at about 1.8 times the rate of full-file reviews.

The same gap appears after actions. SWE-Flux gives 480 execution-grounded questions across 12 Python repositories. Its best tested model reaches 37.71 percent overall and only 6 percent on runtime dataflow. RecreationWorld then tests 250 computer-use tasks with programmatic and visual post-action assertions. DolphinBench extends the rule to memory: its 600 tasks grade exact future tool effects, cost, and latency against long histories, and the strongest published configuration reaches 70.67 percent.

Why it matters: an answer can look complete while required files remain unread, runtime behavior remains misunderstood, or the requested effect never occurred. The evaluator needs evidence from the trajectory and the resulting state.

How it fits: the agent harness should emit a machine-derived coverage receipt and deterministic effect receipt for every consequential task. Natural-language judgment can interpret meaning, but it should not replace exact checks for files read, commands run, state changed, and requirements satisfied.

Tools and methodologies worth exploring now:
- coverage ledgers for requested files, resources, and requirements;
- runtime-oracle questions and input perturbations for code changes;
- programmatic plus visual post-action assertions for browser and desktop work;
- future-effect memory fixtures with exact tool-call graders;
- separate accuracy, cost, latency, false-pass, and abstention metrics.

Implementability score: 0.86

Core sources:
- [Quantifying Overclaiming Propensity in Frontier LLM Agents](https://arxiv.org/abs/2609.20812v1)
- [Can LLMs Reason About Runtime Behavior?](https://arxiv.org/abs/2609.28449v1)
- [RecreationWorld](https://arxiv.org/abs/2609.22000v1)
- [DolphinBench](https://arxiv.org/abs/2609.24971v1)

## Select regression work from trajectories and failure liability

Cheap evaluation works when the subset is calibrated to the decision. A trajectory-aware SWE-agent selector used 10 percent of the benchmark, reduced measured token use from 3.44 billion to 345 million, and kept median resolve-rate estimation error below 5 percent. A matched harness study found a 7.17-point oracle-success gain from task-specific plans over shuffled context, while a sub-cent terminal verifier rejected 61 percent of invalid Retail episodes and recovered nearly all of the full stack's false-pass benefit at one twelfth of the incremental cost.

Simulation adds another layer when production behavior has been calibrated. Nubank screened more than 16,000 simulated conversations, selected a candidate, and then measured an 8.82-point self-service gain in a live test with no statistically significant tNPS change.

Why it matters: broad evaluation can be too expensive to run on every change, while convenient smoke tasks can be uncorrelated with production performance. The answer is a fixed, provenance-preserving regression set plus periodic full runs and bounded live confirmation.

How it fits: traces become evaluation infrastructure. They identify high-liability states, select representative tasks, and expose which harness component earns its cost.

Tools and methodologies worth exploring now:
- trajectory clustering and calibrated subset selection;
- fixed-plan, sham-context, verifier-only, and full-stack ablations;
- periodic full-benchmark recalibration;
- frozen simulated users, mocked tools, and versioned evaluators;
- small live tests only after offline ranking is stable.

Implementability score: 0.88

Core sources:
- [Trajectory-Aware Benchmark Subset Selection for Cost-Efficient Software Engineering Agent Regression Testing](https://arxiv.org/abs/2609.24928v1)
- [How Do Agent Harnesses Create Value? Planning Information and Release Control in Stateful LLM Agents](https://arxiv.org/abs/2609.20474v1)
- [Screen Before You Serve](https://arxiv.org/abs/2609.30137v1)

## Treat compaction as a state transition

Three findings converge on one rule: context may be removed only after the state it carries has a durable, testable home.

A future-update memory study shows that a compressed history can answer correctly now while losing distinctions needed after a later shared update. CliffCompaction avoids recursive summary drift by deleting or truncating original spans rather than rewriting them. Interaction Aware Compression preserves actions, tool calls, and observations while pruning reasoning after task-relevant state has been externalized. Across 260 WorkBuddyBench tasks, it raises average reward from 0.699 to 0.718 while reducing input tokens by 25.5 percent, output tokens by 14.4 percent, and cache reads by 33.3 percent.

Why it matters: context compression is a write to operational memory. If the only copy of a constraint, identity, or dependency remains inside discarded reasoning, the agent becomes cheaper by becoming wrong in ways that current-turn tests may miss.

How it fits: context managers need a dependency map from derived state to durable carriers. A block becomes eligible for removal only after its carrier is verified and replay tests show that future updates still produce the same effects.

Tools and methodologies worth exploring now:
- derived-state labels linked to files, code, tool outputs, and environment state;
- source-span deletion with immutable compaction receipts;
- paired histories that differ only in facts needed after a future update;
- identifier renaming, tombstone deletion, and late-reference replay;
- full-history versus compressed-history trajectory comparison.

Implementability score: 0.70

Core sources:
- [Correct Now, Insufficient Later: Auditing Update Sufficiency in Context Compression](https://arxiv.org/abs/2609.20045v1)
- [CliffCompaction](https://arxiv.org/abs/2609.26779v1)
- [When Can Agents Forget Their Reasoning?](https://arxiv.org/abs/2609.29875v1)

## Working conclusion

The practical agent stack should treat trajectories as evidence, effects as the grading target, and compaction as a controlled state transition. Start with coverage and effect receipts, calibrate a cheap regression subset from real traces, then prune context only when future-effect replay stays stable.
