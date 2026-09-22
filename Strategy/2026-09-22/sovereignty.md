# Strategy Daily Analysis - 2026-09-22

## Let models propose policy, then certify and freeze it before effects

ActGov separates policy construction from runtime authorization. An LLM proposes and refines rules from tool specifications, benign tasks, and attack traces. Z3 checks the complete finite policy model against declared safety invariants before deployment. The resulting bundle is frozen, and a deterministic runtime monitor maps each proposed tool call plus context into the same record space before allowing an external effect.

On AgentDojo, ActGov reduced attack success rate to zero across four tested agent models while retaining more clean-task utility than most compared defenses. The security gain still had a cost. For DeepSeek-v4-pro, clean utility moved from 0.878 without defense to 0.755 with ActGov. On AgentDyn, attack success fell from 0.046 to 0.004 for Qwen3.6-flash and from 0.086 to 0.007 for DeepSeek-v4-pro, while clean utility moved from 0.667 to 0.667 and from 0.767 to 0.600 respectively.

Why it matters: a model can help draft a policy without becoming the authority that releases effects. The verification boundary must use the same typed semantics as runtime enforcement, and the final action decision must be deterministic.

Practical controls worth exploring now:
- define a finite record schema for task permission, hard invariants, procedural obligations, provenance, target role, and approval state;
- use models only to propose or refine candidate policies;
- prove invariant preservation and expose counterexamples before promotion;
- freeze the reviewed policy bundle by version and digest;
- evaluate each candidate tool action immediately before the external call;
- report security and clean or attacked utility together so deny-all systems cannot look safe;
- retain tool proposal, record abstraction, matched policy, decision, effect, and outcome in one receipt.

Artifact status: no public ActGov implementation repository resolved from the primary paper page or exact-title search. The paper is an architecture and evaluation reference, not a drop-in control plane.

Evidence caveat: the main policy-generation setting used GPT-5.5 over ten refinement rounds with human review. The authors report poor cross-environment utility when a policy bundle is transferred to an unseen benchmark, even while attack success stays at zero. Open-world policy generalization remains unresolved.

Implementability score: 0.48

Core source: [ActGov](https://arxiv.org/abs/2609.24446v1)
