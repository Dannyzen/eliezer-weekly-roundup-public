# AgenticAI Daily Analysis: 2026-05-13

Today's agentic-stack signal is that capability surfaces are getting more realistic and less forgiving. Computer-use agents now need to choose between GUI actions and tool calls as a path-planning problem. Memory systems now need to prove they can maintain evolving multi-entity state. Skill systems now need adversarial tests because a skill is operational text, not passive documentation.

## Computer-use agents need path-level GUI-tool orchestration

ToolCUA is the clearest implementation finding. Computer-use agents can increasingly act through both low-level GUI actions such as click/type and high-level tool calls such as file or API operations. The paper's core claim is that simply exposing both action spaces is not enough: agents can become GUI-centric and ignore tools, or overuse tools and shorten trajectories while still reducing success. ToolCUA addresses that with interleaved GUI-tool trajectory synthesis, Tool-Bootstrapped GUI RFT, and Online Agentic RL using a tool-efficient path reward.

The reported OSWorld-MCP result is useful but should not be over-read as a drop-in recipe: ToolCUA-8B reaches 46.85% accuracy, roughly a 66% relative gain over the stated baseline, but it depends on a specialized training pipeline and a high-fidelity GUI-tool environment. The more durable insight is architectural: hybrid agents need path-level supervision. The harness should know when a GUI step was preferable, when a tool call was preferable, when tool use shortened the path without preserving correctness, and what state evidence justified the switch.

Deep Dive Wednesday selection: [GUI-Tool Path Orchestration](../gui-tool-path-orchestration/gui-tool-path-orchestration.md) is the single strongest finding of the last seven days because it changes the action layer itself. MEME, skill safety, MCP consent, and model routing are all important, but ToolCUA plus ComplexMCP shows that computer-use agents need an observable path policy across GUI, tools, verification, and recovery.

ComplexMCP supplies the complementary evaluation pressure. It builds a benchmark around more than 300 tools across seven stateful sandboxes and reports that top models still fail to exceed 60% success, far below human performance around 90%. Its failure taxonomy is exactly what production agents show: tool retrieval saturation as action spaces scale, over-confidence that skips environment verification, and strategic defeatism that rationalizes failure instead of recovering.

GitHub demand signals reinforce the same direction. `trycua/cua` is actively maintained infrastructure for computer-use agents, sandboxes, SDKs, and benchmarks across macOS, Linux, and Windows. X-PLUG's ToolCUA and OSWorld-MCP repos are new and still early, but they make the GUI-tool path-selection problem concrete enough to evaluate.

Why it matters: desktop agents will not be reliable if the action layer is either all screenshots or all APIs. Real workflows mix GUI-only surfaces, structured tools, flaky state, hidden validation, and recovery paths. The action-choice policy has to become observable and testable.

How it fits into the stack: this belongs in the harness, tool, and trajectory-evaluation layers. The runtime should expose GUI actions, tool calls, screenshots, DOM/accessibility state, file/API results, path length, verification steps, and recovery attempts as one trace. The model's job is not merely to call a tool; it is to choose a path through a mixed action graph.

Implementable now:
- add a `gui_step` versus `tool_call` label to computer-use traces and record why the agent switched;
- compare GUI-only, tool-only, and hybrid runs on the same desktop tasks;
- log path length, verification actions, failed tool retrievals, and recovery attempts, not only final success;
- build small stateful sandbox tasks before trusting a broad MCP catalog;
- use CUA-style sandboxes or OSWorld-MCP-style tasks for read-only evaluation before allowing side effects.

Tools, repos, and methodologies worth exploring:
- ToolCUA project and repo: https://x-plug.github.io/ToolCUA/, https://github.com/X-PLUG/ToolCUA
- OSWorld-MCP: https://github.com/X-PLUG/OSWorld-MCP
- ComplexMCP benchmark methodology: https://arxiv.org/abs/2605.10787v1
- CUA infrastructure: https://github.com/trycua/cua
- path-level trajectory labels, mixed GUI/API evaluation, recovery scoring, OpenTelemetry traces, and deterministic sandbox seeds

Implementability score: 0.64

Core source links:
- https://arxiv.org/abs/2605.12481v1
- https://x-plug.github.io/ToolCUA/
- https://github.com/X-PLUG/ToolCUA
- https://github.com/X-PLUG/OSWorld-MCP
- https://arxiv.org/abs/2605.10787v1
- https://github.com/trycua/cua

## Memory eval now has to test multi-entity evolving state

MEME is the day's best memory finding because it tests the part of memory that product systems most often hand-wave: evolving state across multiple entities. Prior memory benchmarks often ask whether a system can retrieve a fact or handle a simple update. MEME defines six tasks across multi-entity and evolving axes, including Cascade, Absence, and Deletion, which prior benchmarks did not score.

The failure is severe. Across 100 controlled episodes and six memory systems, the project reports collapse on dependency reasoning under default configurations: Cascade averages 3% accuracy and Absence averages 1%, despite adequate static retrieval. Prompt optimization, deeper retrieval, reduced filler noise, and stronger LLMs mostly do not close the gap. A file-based agent paired with Claude Opus 4.7 partially improves results but at roughly 70x baseline cost, which makes the point sharper: brute-force expensive reasoning is not a scalable memory architecture.

Why it matters: a useful memory system must know not only that a fact exists, but whether it was deleted, superseded, dependent on another entity, or absent after a change. Agents fail when a team lead changes, a package manager switches, a user stops using a service, a credential rotates, or a constraint becomes invalid in one project but not another. Static recall can pass while operational memory is wrong.

How it fits into the stack: this belongs in the memory-state and eval layers. Memory should be tested as a state machine over entities, relationships, updates, deletions, absence queries, and dependency cascades. Retrieval accuracy is only one submetric; state-maintenance correctness is the real target.

Implementable now:
- add controlled episodes where several entities change over time and later questions require dependency reasoning;
- score Deletion and Absence explicitly instead of treating "not found" as an ungraded failure;
- preserve supersession, deletion, and dependency metadata with memory writes;
- compare cheap stores, vector stores, file-based memory, and agentic memory under the same episode budget;
- track cost per episode so stronger internal LLMs do not hide architectural weaknesses.

Tools, repos, and methodologies worth exploring:
- MEME project page and data: https://seokwonjung-jay.github.io/meme-eval/
- MEME paper: https://arxiv.org/abs/2605.12477v1
- typed state records, deletion tombstones, supersession edges, entity timelines, dependency tests, Pass@B under cost budgets, and memory-call burden metrics

Implementability score: 0.78

Core source links:
- https://arxiv.org/abs/2605.12477v1
- https://seokwonjung-jay.github.io/meme-eval/

## Skill ecosystems need safety tests at the skill boundary

The skill layer got a blunt security update. SkillSafetyBench, Under the Hood of SKILL.md, and Proteus all point to the same conclusion: a skill is executable-context packaging, not passive documentation. It can steer discovery, selection, governance, local file interpretation, tool use, memory writes, and runtime behavior even when the user request is benign.

SkillSafetyBench evaluates localized non-user attacks where task-relevant skill materials or local artifacts induce unsafe behavior. It includes 155 adversarial cases across 47 tasks, six risk domains, and 30 safety categories, with case-specific rule-based verifiers. The key result is architectural: failures vary across scaffold-model pairings, so base-model alignment is not enough. The same skill can be safe or unsafe depending on how the agent loads it, trusts it, and acts through tools.

Under the Hood of SKILL.md focuses on registry-facing risk. It shows that SKILL.md text can manipulate discovery, selection, and governance: short textual triggers can improve adversarial skill visibility, description-only framing can bias agents toward adversarial variants, and semantic evasion can avoid blocking verdicts. Proteus then makes the red-team point harsher: single-shot audits underestimate residual risk because attackers can adapt skills using audit and runtime feedback, producing many variants that both bypass auditors and cause harm.

Why it matters: skills are becoming a common distribution format for agent capabilities. Public skill repositories and marketplace patterns make reuse easier, but they also create a semantic supply chain. Provenance and signatures help identify where a skill came from; they do not prove the prose, bundled scripts, tool paths, or approval conditions are safe.

How it fits into the stack: this belongs in the skill retrieval, registry, and harness governance layers. Skills should have metadata-triggered loading, risk labels, allowed tools, side-effect declarations, tests, and verifier results. The runtime trace should show which skills were retrieved, loaded, trusted, executed, and denied.

Implementable now:
- pin third-party skills to reviewed commits and keep author provenance separate from behavioral verification;
- add load/no-load gates and require high-risk skills to declare allowed tools, files, network, memory writes, and approval points;
- create adversarial skill fixtures that try prompt injection, secret exfiltration, unsafe scripts, stale policy, and confused-deputy behavior;
- evaluate skills with rule-based verifiers where possible instead of only LLM-as-judge review;
- log skill discovery query, selected candidate, loaded body hash, verifier result, and runtime side effects.

Tools, repos, and methodologies worth exploring:
- SkillSafetyBench-style runnable adversarial cases: https://arxiv.org/abs/2605.12015v1
- SKILL.md registry-stage testing: https://arxiv.org/abs/2605.11418v1
- Proteus-style adaptive skill red-teaming: https://arxiv.org/abs/2605.11891v1
- Anthropic skills repo as a distribution-shape reference: https://github.com/anthropics/skills
- signed registries, static script review, semantic policy checks, Open Policy Agent, rule-based verifiers, and skill trace hashes

Implementability score: 0.67

Core source links:
- https://arxiv.org/abs/2605.12015v1
- https://arxiv.org/abs/2605.11418v1
- https://arxiv.org/abs/2605.11891v1
- https://github.com/anthropics/skills
