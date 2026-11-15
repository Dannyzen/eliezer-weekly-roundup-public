# AgenticAI Daily Analysis: 2026-11-15

There is no Sunday arXiv announcement batch. The paper findings below are Friday carry-forwards, first listed on November 13 and submitted on November 12. The useful common pattern is concrete: deterministic boundaries should own write authority and native execution scheduling, while models supply plans and candidates.

## 1. Derive write authority from schemas and user-stated values

CapLite tests whether small language models can safely author the programs, policies, dependency graphs, or constraint lists that enforcement systems later trust. Across 15 open-weight models, model-written policies admitted attacks on 14 models, graphs on 13, and constraints on 11. CaMeL was breached in 20 of 13,935 attacked episodes, but its generated programs failed to run in up to 68 percent of episodes.

CapLite removes that security artifact from the model. Fixed rules derive authority-bearing arguments from tool schemas. A planner that sees only the user request commits write calls before untrusted tool output enters context. A deterministic mediator then admits a write only when its recipient, amount, object identifier, or destination matches a value stated by the user.

Why it matters: prompt-injection defenses should not ask the same model being defended to define its own authority boundary. The reusable pattern is request-bound write integrity, with deterministic argument checks at the effect boundary.

Implementable now:
- classify tool fields that determine recipient, amount, object, or destination;
- freeze intended write calls before reading untrusted content;
- require authority-bearing arguments to match normalized user-stated values;
- test matched benign, write-injection, and answer-only injection cases;
- preserve the request, proposed effect, policy decision, and final receipt.

Evidence and caveat: no attack succeeded in 13,935 attacked AgentDojo episodes. Utility under attack was 29.0 percent, comparable to CaMeL's 27.2 percent, at 17.1k tokens per episode. The guarantee covers write integrity. The paper shows an answer-only injection that CapLite repeats, so it is not a general content-integrity defense. No public implementation artifact was identified in the primary source.

Artifact status: paper and HTML inspected. No external code was executed.

Implementability score: 0.78

Core source: [CapLite v1](https://arxiv.org/abs/2611.17115v1)

## 2. Schedule native accelerator work at the command boundary

Metal Sandbox combines per-instance filesystem restrictions, native macOS command execution, and command-level scheduling across connected Macs. Parallel-safe commands run concurrently. Serial GPU-sensitive commands share one slot per node, and eligible waiting work can migrate to another Mac while results return to the originating agent workspace.

Why it matters: agent rollouts spend most wall time on model calls, editing, and CPU work rather than GPU execution. Scheduling an entire session wastes scarce native accelerator capacity. The command is the better scheduling unit when the runtime preserves workspace identity and returns results to the correct trajectory.

Implementable now:
- separate parallel-safe commands from serialized accelerator commands;
- preserve a private workspace and HOME per agent instance;
- bind every migrated command to instance, node, queue, and return-channel identity;
- measure queue wait, accelerator occupancy, batch elapsed time, and correctness;
- replay fixed traces before enabling live migration.

Evidence and caveat: four Mac mini M4 nodes produced 1.68 to 2.05 times command-throughput gains under concentrated demand. Replay of 16 measured traces estimated 2.14 times sustained throughput and reduced mean tool wait by 18.8 percent and batch elapsed time by 22.3 percent. The replay assumes unchanged phase durations and continuously replenished sessions. The public repositories were inspected read-only; the main Metal Sandbox repository exposes no detected license in GitHub metadata.

Artifact status: public repositories resolved and README pages were inspected read-only. No source was cloned or executed.

Implementability score: 0.66

Core source: [Metal Sandbox v1](https://arxiv.org/abs/2611.17294v1)

Public artifacts: [Metal Sandbox](https://github.com/WangHaoZhe/metal-sandbox), [Harbor integration](https://github.com/WangHaoZhe/harbor)

## Working conclusion

The model can propose work. Deterministic runtime code should own who or what a write affects, where native commands run, and how the result returns to the correct trajectory.
