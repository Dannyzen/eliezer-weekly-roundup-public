# AgenticAI Weekly Analysis, 2026-08-14

## Thesis

Evidence is not authority. This week’s strongest research converges on a split control plane: models may propose actions, repairs, memories, skills, and plans, while deterministic runtime components verify the path, authorize the change, preserve valid state, govern promotion, and record the outcome.

## Conjunctive acceptance replaces terminal success

### Finding

Three studies expose different false-green paths.

QuoteBench crosses generation contracts with execution transports on 56 exact-state Bash tasks. Replaying the same reply through one additional parser reduces success by 55.4 to 73.2 percentage points. For GPT-5.6-sol, a matched-path difference of only -3.6 points hides -64.3 points of transport damage plus +60.7 points of model compensation.

CAPRI evaluates 180 Isabelle proof-repair runs. Isabelle accepts 144 terminal candidates, but six modified protected text. A proof-body-only interface removes the observed authority violations while giving up two valid repairs out of 36 compared with the full-theory workflow.

The IaC repair study reconstructs 5,968 timelines. Its conservative strict security-regression rate is 3.3 percent of scenarios. Regressing transitions have 2.6 times more churn and 4.9 times more strict-mode check volatility. Cumulative-best reporting hides those raw trajectory regressions.

### Why it matters

Outcome validity, transport fidelity, change authorization, and property preservation are independent predicates. A system that collapses them into one final score cannot attribute failure or justify release.

### Fit into the stack

Primary layers: trajectory-aware evaluation, coding-agent control, execution adapters, and release gating.

### Practical tools and methods

- Replay fixed generated actions through shell, SSH, container, CI, and remote-execution wrappers.
- Validate exact final state separately from generated text.
- Express editable files, regions, resources, and effect classes as machine-readable contracts.
- Retain per-property pass, fail, ambiguous, restored, and waived states across iterations.
- Bind original state, diff, contract, path transforms, validator results, policy verdict, and final state into one receipt.
- Use QuoteBench as a read-only design reference for task schemas, validators, offline scoring, and transport comparisons.

Implementability score: 0.88

Artifact status: QuoteBench is a populated Apache-2.0 repository inspected read-only. CAPRI’s claimed artifact was not resolved. The IaC study has no verified paper-owned implementation.

Core sources:
- https://arxiv.org/abs/2608.13547v1
- https://github.com/LeonardNJU/quoteBench
- https://arxiv.org/abs/2608.13459v1
- https://arxiv.org/abs/2608.13404v1

## Memory and skills need governed promotion

### Finding

Retained state becomes a control surface when it can alter later behavior.

Trajectory-poisoning experiments place three poisoned records in a 30-record promotion batch. The attacker behavior survives into 546 of 600 SkillClaw trials and 369 of 600 Trace2Skill trials. Malicious skill-file experiments under auto-approved delegated execution report exploitation in 95.5 to 96.1 percent of Gemini CLI runs and 71.6 to 74.0 percent of Qwen Code runs in the tested setup.

TEPA’s temporal entailment and provenance model scores 0.950 under reversal, compared with 0.210 for append-only and last-write-wins memory. MAP-Graph shows the other half of the problem: permission filtering can prevent unauthorized retrieval, but retrieved evidence still needs an independent gate before it can authorize a high-risk action.

### Why it matters

Memory, summaries, shared artifacts, and skills are not passive context. Promotion can convert evidence into durable instruction. Retrieval can convert stored state into immediate influence. Those transitions need explicit authority.

### Fit into the stack

Primary layers: memory systems, skills-as-control, shared-state orchestration, and agent self-improvement governance.

### Practical tools and methods

- Give evidence, memories, summaries, and skills stable identities and ancestry.
- Use active, superseded, revoked, quarantined, and re-promoted states.
- Apply permission filtering before relevance ranking.
- Preserve inherited restrictions through summaries and handoffs.
- Separate proposer, evaluator, and promoter roles.
- Replay historical and adversarial cases before promotion.
- Require a second effect gate after retrieval.

Implementability score: 0.72

Weakest point: TEPA and MAP-Graph did not expose verified exact public implementations in this scan. AgentJailbreak is populated but lacks a declared license, and its rates come from two agents, one benign task, auto-approval, and a short execution window.

Core sources:
- https://arxiv.org/abs/2608.05563v1
- https://arxiv.org/abs/2608.05223v1
- https://arxiv.org/abs/2608.07429v1
- https://arxiv.org/abs/2608.10509v1

## Evaluation must vary hidden conditions and inspect the process

### Finding

The week’s evaluation work repeatedly finds confounding behind aggregate scores.

AgentChaos injects 65 runtime fault configurations at the shared API boundary. Pass@1 falls by up to 50 points, while fault-type and fault-step diagnosis remain below 53 and 56 percent. SpecPath finds that 35 of 100 blocks passing a consolidated specification fail under at least one contract-equivalent history. HarnessSafe tracks 328 cases across memory, skills, MCP/tools, summaries, delegation, and shared artifacts instead of collapsing persistent risk into attack-success rate.

Beyond Final Scores evaluates seven models, 36 long-horizon R&D tasks, and 756 rollouts. The avg@3 gap between strongest and weakest systems is 0.237, compared with 0.122 for best@3. Transferred experience improves one model by 0.093 and harms another by 0.017.

### Why it matters

The object under evaluation is not only the model. It is the model plus harness, history, transport, tools, faults, retained experience, and recovery behavior. Hidden variation in any one of those can reverse a conclusion.

### Fit into the stack

Primary layers: agent harness architecture, trajectory-aware evaluation, observability, and containment testing.

### Practical tools and methods

- Inject test-only crash, omission, delay, and value faults at the LLM HTTP boundary.
- Pair consolidated prompts with contract-equivalent histories.
- Record the earliest consequential error and the recovery path.
- Report avg@N beside best@N.
- Compute progress retention, regression, recovery, and checkpoint quality from deterministic events.
- Trace persistent carriers through their full lifecycle.

Implementability score: 0.82

Artifact status: AgentChaos has a populated repository and Zenodo artifact. TrajDebug is a preview. SpecPath and AutoResearchEval lacked resolved exact artifacts.

Core sources:
- https://arxiv.org/abs/2608.06790v1
- https://github.com/IntelligentDDS/AgentChaos
- https://arxiv.org/abs/2608.09799v1
- https://arxiv.org/abs/2608.06984v1
- https://arxiv.org/abs/2608.13417v1

## Deterministic interfaces should bound adaptive reasoning

### Finding

The strongest operational pattern is not removing models. It is narrowing where model judgment is allowed to operate.

READ exposes deterministic `search`, `list`, `outline`, and bounded `read` operations over structured documents. LivePlan triggers advice only after deterministic drift signals. OpenCodeReview uses deterministic dispatch, bounded investigation, and independent falsification, reporting up to 2.17 times higher SEM-F1 with 5 to 15 times fewer tokens. POLIS’s immutable-provenance guard admits 0 of 96 laundering violations, compared with 22 of 96 for a local-state guard, while 44 of 51 blocked episodes later complete safely.

### Why it matters

Models are useful for synthesis and judgment, but weak as the sole owner of lifecycle transitions, evidence access, admission, or release. Deterministic interfaces make the adaptive part observable and bounded.

### Fit into the stack

Primary layers: retrieval, coding-agent control, multi-agent orchestration, and recovery.

### Practical tools and methods

- Expose deterministic evidence operations with line-level references.
- Define lifecycle phases and drift triggers before asking for model advice.
- Dispatch files and rules deterministically.
- Give a separate stage authority to falsify the proposed finding.
- Model denied actions as typed states with bounded safe alternatives.
- Record attempted action separately from realized effect.

Implementability score: 0.86

Artifact status: OpenCodeReview is public, populated, and Apache-2.0. READ and LivePlan lacked verified exact repositories. POLIS is inspectable but single-author, unreplicated, and non-standardly licensed.

Core sources:
- https://arxiv.org/abs/2608.06305v1
- https://arxiv.org/abs/2608.06701v1
- https://arxiv.org/abs/2608.09290v1
- https://github.com/alibaba/open-code-review
- https://arxiv.org/abs/2608.09828v1

## Portable capability packages need hostile-world admission tests

### Finding

GitHub Agent Plugins 1.0 packages skills and MCP configuration across VS Code, Copilot CLI, SDK, and the Copilot app while preserving client namespaces. ToolHazard supplies stateful adversarial environments across 28 domains, with tasks averaging 15.56 steps and 18.75 candidate tools. Quadrat-IPI publishes 16,800 injections and 63,000 clean documents, with detector recall varying by 4 to 76 points across attack cells.

### Why it matters

Packaging lowers distribution cost. It does not lower authority. A portable bundle can enlarge the blast radius of a weak manifest, hidden tool grant, malicious skill, or detector blind spot.

### Fit into the stack

Primary layers: capability discovery, skills-as-control, agent gateways, and executable security evaluation.

### Practical tools and methods

- Validate manifests, digests, namespaces, and component identities.
- Grant each skill, tool, and server separately for each client and policy profile.
- Bind traces and approvals to interface-schema versions.
- Convert incidents into isolated state machines with deterministic final-state fixtures.
- Evaluate detectors by attack family at fixed false-positive budgets.
- Pilot one low-risk skill and one read-only MCP server before broader admission.

Implementability score: 0.90

Artifact status: Agent Plugins has a public 1.0 specification and GA GitHub implementations. ToolHazard is populated and MIT-licensed. Quadrat publishes a dataset and Apache-2.0 harness; its corpus is new and needs independent replication and source-license review.

Core sources:
- https://github.blog/changelog/2026-08-12-agent-plugins-1-0-in-vs-code-copilot-cli-and-the-copilot-app/
- https://github.com/agentplugins/agent-plugins-spec/blob/main/spec/1.0.0.md
- https://arxiv.org/abs/2608.11878v1
- https://github.com/MurrayTom/ToolHazard
- https://huggingface.co/blog/mihailgribov/compare-prompt-injection-detectors

## Implementation bridge from stable releases

The control-plane pattern is moving into mainstream SDKs. OpenAI Agents Python 0.20.0 adds durable staged input, MCP v1/v2 support, and explicit sandbox credential-exposure acknowledgement. Agno 2.9.0 closes an MCP approval bypass and persists paused human-in-the-loop runs. PydanticAI 2.30.0 binds deferred-tool callability to provider-visible evidence. Microsoft Agent Framework Python 1.14.0 adds enforcement middleware, durable approval stores, checkpoints, and recovery fixes.

These releases do not prove the research claims. They show that the required primitives are implementable now.

Sources:
- https://github.com/openai/openai-agents-python/releases/tag/v0.20.0
- https://github.com/agno-agi/agno/releases/tag/v2.9.0
- https://github.com/pydantic/pydantic-ai/releases/tag/v2.30.0
- https://github.com/microsoft/agent-framework/releases/tag/python-1.14.0

## Current implication

Treat the model as proposer and reasoner. Keep admission, authority, transport, preservation, and release verification in separately testable runtime components.
