# AgenticAI Daily Analysis - 2026-08-15

## Scope note

There is no Saturday arXiv listing. These are non-duplicate papers first listed Friday, August 14, with v1 submissions from August 12 and 13. The scan also checked Hugging Face, GitHub Trending, official changelogs, and vendor releases. No stronger Saturday primary-source release displaced this paper-led cut.

External repositories were inspected read-only through metadata, trees, READMEs, licenses, and releases. No external code was cloned, installed, built, imported, or executed.

## Action gates need bidirectional calibration

### Finding

[SteerBench-Work](https://arxiv.org/abs/2608.12654v1) tests the decision immediately before a tool commits an effect: proceed or hold for review. Its 106 incident-anchored scenarios span developer operations, finance, legal, medical, HR, customer service, and security. Across 30 model conditions, wrong holds dominated wrong acts: models held authorized work on 28.1% of opportunities but allowed unsafe work on 1.0%. Evidence-reversed mirrors of famous incidents scored 63.8%, versus 98.5% on the recognizable incidents.

### Why it matters

A safety gate can be unusable while looking conservative. Over-refusal creates queue pressure, encourages bypasses, and can block time-sensitive recovery. Evaluation therefore needs two error budgets, not one safety score: false allow and false hold.

### Fit into the stack

This belongs at the action boundary between model proposal and tool execution. The gate should read a typed action manifest plus structured evidence, return a typed decision, and remain independent of the model that proposed the action.

### Practical tools and methods

- Start with the tagged [SteerBench-Work v2026-05 artifact](https://github.com/AgentDock/steerbench-work), which contains a replayable 256-file benchmark release, MIT-licensed runner code, and CC BY 4.0 data.
- Add local mirrored pairs where one evidence field reverses the correct decision.
- Report false allow, false hold, calibration by action class, and denial-recovery outcomes separately.
- Bind each verdict to action identity, evidence version, gate version, and the exact effect receipt.

Implementability score: 0.90

Evidence caveat: scenarios are constructed, single-turn descriptions rather than live tool executions. Each condition uses five trials, individual model differences are descriptive, and proceed cases may be intrinsically harder than hold cases.

Core sources:
- https://arxiv.org/abs/2608.12654v1
- https://github.com/AgentDock/steerbench-work
- https://steerbench.com

## Reliability certificates must model shared failure

### Finding

[Agent Behavioral Contracts II](https://arxiv.org/abs/2608.12895v1) tests the conditional-independence assumption behind multiplying component reliabilities. In a preregistered two-agent handoff over 18,000 missions, scored by deterministic code with no LLM judge, two instances of the same model co-failed on 90.0% of missions where either failed. Replacing one instance with a different model reduced dependence in six of six contrasts. Replacing the vendor after the model was already different did not. Fourteen measured moment functionals narrowed the assumption-free interval by 85.7% and raised the certified floor from 0.2455 to 0.4116.

### Why it matters

Running two agents is not redundancy when they share the same failure surface. Independence-based reliability can over-credit precisely the configurations that look diverse in topology but are homogeneous in model behavior.

### Fit into the stack

The contract belongs in the evaluator and orchestrator. It should certify the composed route from measured joint behavior, not infer safety from component pass rates.

### Practical tools and methods

- Use the [agentassert-abc artifact](https://github.com/qualixar/agentassert-abc) as a design and reproduction reference. The public AGPL-3.0 repository has a populated 606-file tree, preregistration, analysis scripts, and release v0.7.0.
- Log component and joint failures under identical missions.
- Compare same-model, cross-model, and cross-provider compositions.
- Prefer finite-sample lower bounds over fitted dependence models when the joint structure is not identified.
- Block reliability claims that cite only marginal success rates.

Implementability score: 0.78

Evidence caveat: the headline result is a controlled two-agent handoff. The certificate is mathematically stronger than an independence product, but integrating it requires repeated matched missions and explicit contract design.

Core sources:
- https://arxiv.org/abs/2608.12895v1
- https://github.com/qualixar/agentassert-abc

## Self-improvement needs write and reuse gates

### Finding

[Practice Makes Unsafe](https://arxiv.org/abs/2608.12851v1) follows compromised experience through authoring, retrieval, and fresh-session execution. Across 25 agent-method configurations, each covering 525 tasks in 25 episodes, all 21 evolved configurations authored unsafe skill artifacts, while 15 produced fresh-session harm. Three malicious exposure tasks raised carryover attack success from 16.0% to 35.3%. SafeEvolve reduced unsafe retrieval by 26.7 percentage points and fresh-session harm by 17.3 points while changing mean benign utility by only 0.4 points.

### Why it matters

A successful trajectory is not safe training data. Once distilled into a reusable skill, the original trigger disappears and the unsafe procedure can look like normal operational knowledge.

### Fit into the stack

Skill evolution is a release pipeline. Drafting, static inspection, behavioral replay, promotion, retrieval, execution, and retirement need separate states and receipts.

### Practical tools and methods

- Treat the [MisEvolve artifact](https://github.com/henrymao2004/misevolve) as an early benchmark reference, not a drop-in dependency. It exposes a 59-file harness across multiple agent runtimes but has no tag, no release, and no detected license file.
- Quarantine newly authored skills until held-out replay passes.
- Scan the skill text and the originating trajectory for network, credential, persistence, destructive, and exfiltration behavior.
- Gate both write admission and later retrieval.
- Retire by immutable skill version and record every downstream use.

Implementability score: 0.72

Evidence caveat: the benchmark covers executable computer-use skills under a designed malicious-exposure lifecycle. Longer natural task streams, other memory mechanisms, and multimodal adaptation remain untested.

Core sources:
- https://arxiv.org/abs/2608.12851v1
- https://github.com/henrymao2004/misevolve

## Tool responses need semantic authority contracts

### Finding

[PIPES](https://arxiv.org/abs/2608.12789v1) treats each tool-response unit as a claim with a semantic prior and source provenance. Across three VitaBench and three AgentDyn splits with Gemma 4 31B IT, atomic removal reduced average attack success from 84.7% to 2.3%, while benign utility was 92.5% with PIPES versus 90.6% without it. The paper also reports GPT-5.6 Luna falling from 21.6% to 1.1% attack success without reducing average benign utility.

### Why it matters

Instruction filtering is too late if attacker-controlled content has already changed the agent's perceived state. A response component should only make claims within the informational authority of its source and field.

### Fit into the stack

This is an observation-boundary control between raw tool output and model-visible state. It complements, but does not replace, action authorization and information-flow controls.

### Practical tools and methods

- Add field-level contracts for stable schemas and provenance metadata for open-ended response units.
- Screen claims before they enter memory or the planning context.
- Use remove, warn, block, or escalate policies based on source authority and action risk.
- Preserve raw response, extracted units, provenance, prior, screening verdict, and downstream action in one trace.
- Re-run adaptive attacks and clean-utility tests after every schema or screening-model change.

Implementability score: 0.64

Evidence caveat: no public implementation artifact was verified from the primary paper. PIPES does not establish factual truth, depends on trusted provenance and informative priors, and was tested on two benchmarks, two target models, single-surface attacks, and atomic removal.

Core source:
- https://arxiv.org/abs/2608.12789v1

## Practical synthesis

The four findings define one executable sequence:

1. Screen observations before they shape state.
2. Admit persistent procedures before later reuse.
3. Certify composed routes from joint behavior.
4. Gate exact effects with separate false-allow and false-hold budgets.

The model can propose at every stage. It should not own any of these release decisions.
