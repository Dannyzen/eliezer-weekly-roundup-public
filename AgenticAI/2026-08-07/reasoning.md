# AgenticAI Daily Analysis - 2026-08-07

## Verdict

Today's implementation signal is authority over retained state. Failed trajectories need earliest decisive-error attribution, tool policies need protection from misleading history, and skill libraries need admission before writeback. The useful units are lifecycle-traced critical errors, oracle-state tool decisions, and pre-commit skill gates.

## TRAJDEBUG turns failed trajectories into auditable critical-error evidence

TRAJDEBUG attacks cascading failure in long-horizon agents by locating the earliest decisive error, not merely the first local mistake or the step nearest the terminal crash. The framework builds multi-granularity trajectory views, then runs three auditable stages:

- error trigger detection
- error state classification
- critical attribution

The paper evaluates on a benchmark of 486 manually annotated failed trajectories from τ²-Bench and SWE-Bench Pro. Diagnoses converted into targeted guidance before re-execution improve success by about 10.80 percent on average. Aggregating a small set of historical failure diagnoses into reusable failure memory and transferring them to held-out tasks yields about 5.70 percent average improvement.

The public repository `THU-KEG/TrajDebug` is non-empty, updated 2026-08-06, and ships detector code, unified data adapters, evaluation tools, a local viewer, and dataset layout folders. This scan inspected the paper PDF, abstract page, repository metadata, tree, and README read-only and did not execute the detector.

Why it matters: most trajectory logs are too coarse for repair. Teams either blame the final tool call or retrain from full failed rollouts. TRAJDEBUG makes criticality an evidence-verification problem. That is the right object for coding-agent and multi-tool harnesses that need to convert failures into patches, guards, or failure memory instead of vibes.

Implementable now:

- store multi-granularity trajectory views, not only final transcripts;
- label candidate error triggers separately from terminal failure;
- require evidence links when attributing a critical step;
- convert critical-error diagnoses into re-execution guidance before another full attempt;
- promote repeated critical patterns into failure memory with held-out transfer checks;
- keep trajectory, diagnosis, guidance, and outcome under one run receipt.

Tools and repositories worth exploring:

- THU-KEG/TrajDebug, SWE-Bench Pro failed-trace corpora, τ²-Bench tool-use traces, trajectory viewers, failure-memory stores, Hermes coding-lane receipts

Evidence and caveat: headline gains are paper-reported averages on the authors' annotated set and transfer setup. Reproduce on your own failed coding and tool-use traces before treating 10.80 percent or 5.70 percent as portable lift.

Implementability score: 0.78

Core sources:

- https://arxiv.org/abs/2608.06346v1
- https://github.com/THU-KEG/TrajDebug

## Misleading multi-turn history can flip tool decisions the model already knows

When History Lies shows a distinct tool-use failure mode. Tool-calling agents infer task state from accumulated dialogue and tool traces. In persistent sessions, historical traces can remain syntactically valid and semantically plausible after they stop being authoritative for the current request. That stale history can hijack a policy the model already possesses under clean state.

The paper compares a polluted trajectory containing an inserted misleading trace against an Oracle State view that keeps only reliable task state. On Qwen3-1.7B, pollution flips about 32.1 percent of decisions the model can otherwise execute correctly under reliable context. The durable eval object is therefore not only next-tool accuracy. It is whether the same model, with the same tools and latest request, changes its action when untrusted history remains in context.

Why it matters: sessionful agents and MCP-backed assistants keep identifiers, failed calls, and prior arguments around because they look useful. That memory is also an attack and error surface. If history is treated as trusted state, the harness launders stale tool traces into live authority.

Implementable now:

- separate latest request plus verified current state from raw multi-turn history;
- mark tool traces with authority status: verified, superseded, failed-no-effect, or untrusted;
- evaluate tool policies under polluted-history and oracle-state views;
- strip or quarantine misleading traces before high-impact tool calls;
- require state revalidation when a historical identifier or prior argument would change the next action;
- log whether the selected tool depended on history that failed authority checks.

Tools and methodologies worth exploring:

- session state ledgers, tool-trace authority labels, oracle-state fixtures, multi-turn tool-use eval harnesses, MCP conversation stores, Hermes session memory boundaries

Evidence and caveat: this scan verified the arXiv abstract and PDF text. No paper-owned public implementation repository resolved from the primary pages, so treat the polluted-versus-oracle split as the method to implement, not a ready benchmark package.

Implementability score: 0.64

Core source: https://arxiv.org/abs/2608.06057v1

## Self-evolving skill pools need pre-commit gates, not post-hoc cleanup

When Self-Evolution Backfires formalizes skill contamination in agents that distill reusable skills from their own trajectories. Capability growth is not monotonic. Past a critical pool size, newly admitted skills degrade performance instead of improving it. The authors taxonomize contamination at individual, combinatorial, and system levels, and they argue that ad hoc rollback recovers only a small fraction of lost performance once a bad skill has entered runtime context.

The proposed control is Verifier-as-Gatekeeper (VaG): a pre-commit admission gate applied before a candidate skill enters the agent's runtime skill set. Verification timing moves from deferred post-evaluation to a gate that can reject the write. Behavioral replay is treated as a load-bearing check, not an optional offline audit.

Why it matters: Hermes-style and coding-agent skill catalogs are becoming writable control planes. If every successful trajectory can mint a skill, the library becomes a contamination accumulator. The durable rule is simple. A skill becomes executable only after admission evidence beats a held-out or replay gate.

Implementable now:

- treat skill writeback as a privileged state transition;
- require pre-commit verification before a new or edited skill is loadable;
- include behavioral replay, not only static lint or self-score;
- track pool size and performance against a contamination threshold;
- keep rejected candidates out of progressive-disclosure catalogs;
- prefer append-plus-gate over blind overwrite of skill files.

Tools and methodologies worth exploring:

- skill registries with draft versus admitted states, replay harnesses, held-out task suites, Skill-Use-style facet scoring, progressive disclosure loaders, Hermes skill catalogs

Evidence and caveat: the paper is clear on irreversibility and the pre-commit framing, but no public implementation repository was verified in this scan. Implement the gate architecture from the method; do not assume portable critical-size constants.

Implementability score: 0.69

Core source: https://arxiv.org/abs/2608.05810v1

## Watchlist: HarnessOpt-Bench and Activity Frames

HarnessOpt-Bench (Scale AI) measures whether an LLM can improve the harness around a fixed model: prompts, tools, control flow, memory, and orchestration code under expensive stochastic evaluation. It is the right eval object for harness engineering, but this scan found no verified public benchmark package, so keep it as a design reference rather than a top implementable finding.

Activity Frames compile passive screen activity into deterministic, zero-model episodic memory for computer-use agents. The paper reports fast full-day compilation and byte-identical reproducibility. That is promising for routine replay, but no public artifact resolved here.

Watchlist sources:

- https://arxiv.org/abs/2608.06301v1
- https://arxiv.org/abs/2608.05784v1

## Current implication

Do not let retained text decide the next privileged action. Failed trajectories need critical-error evidence. Session history needs authority labels. Skills need admission before they can load. The harness should own those gates.
