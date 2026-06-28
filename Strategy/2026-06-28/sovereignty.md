# Strategy Daily Sovereignty: 2026-06-28

## Bottom line

Today's strategy signal is that agent security is converging on external enforcement, but the evaluation standard is rising.

Two patterns matter:

1. Skill specifications need live reference monitors that can reason over traces, value flow, and temporal obligations.
2. Prompt-injection defenses need adaptive, defense-aware evaluation, not fixed benchmark victory laps.

Both reinforce the same sovereignty rule: the model can propose actions, but runtime policy and adversarial evaluation decide what is trusted.

## Skill specifications need runtime reference monitors

Core source: https://arxiv.org/abs/2606.26524v1

VIGIL argues that agent skills already carry natural-language behavioral specifications: access permissions, disclosure limits, execution privileges, required preconditions, and artifact obligations. The problem is that these specifications are usually documentation. The runtime trusts the agent to honor them.

The paper's practical move is to compile context-specific behavioral requirements into executable policies over typed agent-tool events. VIGIL evaluates finite traces, including event order, argument constraints, temporal dependencies, and cross-call value flow. Its reported evaluation on real agent runs reaches 95.8 percent recall at 89.6 percent precision and surfaces confirmed skill-bundle violations.

Why it matters: single-call filters miss violations that only appear across steps. A skill can produce an intermediate artifact, skip validation, pass it to another tool, and still produce schema-valid output. The policy violation is in the trace, not the final JSON.

How it fits into the strategy stack: this is runtime governance plus skills-as-control. Skills should ship with manifests and behavioral specs, but production systems need a trusted monitor that observes the live trace and blocks or escalates before effects land.

Practical tools, repos, and methodologies worth exploring:

- finite-trace policy templates for precedence, response, absence, and artifact-binding obligations
- typed event logs for skill invocation, arguments, outputs, statuses, artifact IDs, and consuming calls
- SMT-style or state-machine validators for high-risk skill rules
- skill manifests with explicit file, network, memory, disclosure, and prerequisite fields
- denial feedback that lets the agent replan without silently bypassing the monitor
- skill fixtures that test multi-step violations, not only malicious single calls

Implementability score: 0.64

The idea is deployable, but not as a casual wrapper. A useful first version should target a small skill set with obvious temporal rules. General natural-language-to-policy compilation and low-noise monitoring across a large skill ecosystem require real engineering.

## Prompt-injection defenses need adaptive out-of-band evaluation

Core source: https://arxiv.org/abs/2606.26479v1

Adaptive Evaluation of Out-of-Band Defenses Against Prompt Injection gives a needed correction to the recent security consensus. The field is right to move enforcement outside the model: capabilities, taint labels, information-flow rules, and reference monitors are better than asking the model to recognize malicious text. But fixed static benchmarks are not enough evidence. In-band defenses looked strong under static tests until adaptive attacks broke many of them.

The paper organizes defenses such as CaMeL, FIDES, Progent, RTBAS, and FORGE through classical integrity protection, reference monitoring, and least privilege. It then reproduces and extends Progent-style adaptive testing on AgentDojo with Qwen2.5-7B on a single H200. In that small-scale reproduction, Progent reduces mean attack success from 25.8 percent to 4.2 percent, and the hand-crafted adaptive attack does not raise it, at 2.6 percent.

Why it matters: deterministic out-of-band enforcement is promising, but the proof burden is now adversarial. A defense should be tested by an attacker that knows the defense class, not only by a frozen set of injection strings.

How it fits into the strategy stack: this belongs in agent gateway governance. Prompt injection is an authorization failure at the tool boundary. The gateway or reference monitor must enforce structure, and the evaluation harness must try to break that structure adaptively.

Practical tools, repos, and methodologies worth exploring:

- AgentDojo-style indirect-prompt-injection tasks with defense-aware attack variants
- paired static and adaptive test suites for every high-risk agent workflow
- action-level policy gates over data source, destination, capability, and allowed effect
- least-privilege capability handles rather than broad tool access
- red-team reports that separate model refusal, policy denial, tool denial, and task utility loss
- regression tests that rerun adaptive attacks after policy, tool, prompt, or model changes

Implementability score: 0.69

Adaptive evaluation is implementable now. The cost is maintenance: attacks must evolve with the defense, and success metrics must include task utility, denial reasons, bypasses, and false positives. Treat this as a recurring security test, not a one-time paper score.

## Strategic read

The sovereignty move is not to make agents more obedient. It is to make critical obligations executable and to test them against an adaptive opponent. Skill specs, prompt-injection policy, gateway authorization, and runtime traces should all converge into one evidence path: proposed action, governing rule, monitor verdict, final effect, and regression fixture.

## References

- VIGIL: Runtime Enforcement of Behavioral Specifications in AI Agent Skills: https://arxiv.org/abs/2606.26524v1
- Adaptive Evaluation of Out-of-Band Defenses Against Prompt Injection in LLM Agents: https://arxiv.org/abs/2606.26479v1
- CaMeL: https://arxiv.org/abs/2503.18813
- FORGE: https://arxiv.org/abs/2605.04864v1
