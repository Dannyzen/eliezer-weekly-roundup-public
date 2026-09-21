# AgenticAI Daily Analysis - 2026-09-21

## Verify hybrid computer-use agents with action-conditioned outcome tests

RecreationWorld treats GUI interaction and code or terminal work as one interleaved agent loop. Its benchmark spans 250 held-out recreation tasks across Ubuntu, macOS, Windows, Android, and Web. Each task starts from a running reference application, and evaluation uses programmatic plus visual assertions at multiple interaction depths.

The result exposes the gap between a convincing static replica and working software. GPT-6 Astra leads at 58.1 percent overall, yet passes every programmatic test on only 2.8 percent of tasks. Agents reproduce interface structure more reliably than interactions and computed outputs.

Why it matters: browser and desktop agent tests should grade state transitions and rendered outcomes after actions, rather than screenshots or task summaries alone. The reference application can act as an oracle for hidden tests, while independent programmatic and visual checks catch different failure classes.

Practical tools and methods worth exploring now:
- use reference applications to derive hidden, action-conditioned outcome tests;
- pair DOM or state assertions with rendered visual checks;
- freeze reviewed tests before model evaluation;
- run hybrid agents in isolated platform images with pinned interaction servers;
- score complete workflow behavior separately from static interface similarity;
- preserve external state so long trajectories can be compacted without losing recoverability.

Artifact status: the public QwenLM/RecreationWorld repository, project site, and Qwen/RecreationBench dataset card were inspected read-only. The repository has a populated `main` branch and no published GitHub release. No source was cloned or executed.

Evidence caveat: the authors built the benchmark, training trajectories, and evaluated systems. The five-platform harness is operationally heavy, and the strongest model still fails most complete programmatic task suites.

Implementability score: 0.68

Core sources:
- [RecreationWorld paper](https://arxiv.org/abs/2609.22000v1)
- [RecreationWorld repository](https://github.com/QwenLM/RecreationWorld)
- [RecreationBench dataset](https://huggingface.co/datasets/Qwen/RecreationBench)
- [RecreationWorld project](https://recreation-bench.cc/)

## Derive executable training environments from behavior, not ticket history

CodeMidas uses existing source code as the task-specific input for constructing coding-agent reinforcement-learning environments. Agents explore implemented behavior, write behavioral specifications, construct tests against the original program, then validate candidate tasks through execution checks and repeated solution rollouts.

The reported dataset contains 5,545 training tasks from 3,185 open-source codebases across 23 programming languages and 15 technical domains. Training MiMo-V2.5 on the tasks improved all five reported benchmarks, including DeepSWE by 11.7 percent, ProgramBench by 17 percent, and Terminal-Bench v2.1 by 8.5 percent.

Why it matters: issues and commits expose only a narrow slice of useful software behavior. A behavior-first environment compiler can turn stable functionality, fixtures, examples, and executable interfaces into training or evaluation tasks even when no suitable ticket exists.

Practical methods worth exploring now:
- discover observable behavior before drafting a task specification;
- ground tests in executions of the original program;
- require candidate tests to fail incomplete solutions and pass the reference;
- use repeated solution rollouts to reject ambiguous or brittle tasks;
- retain source revision, generated specification, test lineage, validation runs, and licenses;
- separate task generation agents from the policy trained or evaluated on those tasks.

Artifact status: no public implementation repository or dataset URL resolved from the paper's primary HTML surface or exact-title search. The method is available to study, while reproduction remains blocked on the missing artifact.

Evidence caveat: the environment builder, data filter, and trained model come from the same research effort. Reusing open-source behavior at scale also requires license, contamination, test-quality, and compute controls.

Implementability score: 0.46

Core source: [CodeMidas](https://arxiv.org/abs/2609.22068v1)
