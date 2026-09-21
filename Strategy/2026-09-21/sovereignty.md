# Strategy Daily Analysis - 2026-09-21

## Bind approval to one canonical action at use time

Loopjacking names a precise failure in human approval systems: a person approves operation A, while the implementation later releases materially different operation B. The paper separates representation mismatch, where B is hidden or misrepresented during review, from post-approval substitution, where mutable workflow state replaces the reviewed action.

The author reproduced post-approval substitution across seven tested Agno AgentOS releases ending at 3.0.9 and 12 tested versions of a conditional in-memory LangGraph Agent Server composition ending at 0.14.0. OpenClaw 2026.2.23 reproduced a representation mismatch that 2026.2.24 rejected. OpenAI Agents SDK 0.22.0 and 0.22.2 acted as a negative control by preserving exact per-call binding and rejecting mutated actions.

Why it matters: a human approval is useful only when the rendered object, approved object, queued object, and executed object are the same canonical action. An approval token that authorizes a mutable workflow slot creates authority without stable meaning.

Practical controls worth exploring now:
- render the complete canonical action, including recipient, resource, arguments, scope, and side-effect class;
- hash or sign the reviewed action manifest;
- compare the exact action again immediately before execution;
- invalidate approval when any material field or dependency changes;
- prevent unauthorized mutation of pending state;
- retain rendered manifest, approval identity, bound digest, final invocation, and result in one receipt.

Artifact status: the public evidence archive was inspected read-only. It contains reproduction material and explicitly states that all runs were operated by one researcher, so independent reproduction is not yet established.

Evidence caveat: this is a purposive product set, not an ecosystem prevalence estimate. GUI comprehension was not measured in the OpenClaw harness.

Implementability score: 0.96

Core sources:
- [Loopjacking paper](https://arxiv.org/abs/2609.21081v1)
- [Loopjacking evidence archive](https://github.com/adithyan-ak/loopjacking)

## Put deterministic payment policy after planning and before transfer

APort Vault evaluates payment authorization as a separate deterministic boundary around a tool-using agent. The benchmark replays 4,371 human-authored attacks from 1,128 public competition sessions across 14 models from eight labs, five policy configurations, and two replay tracks. It records 225,964 evaluations.

At policy levels 2 through 4, transfers to recipients forbidden by the passport numbered 140 of 76,842 with the model alone and 0 of 69,297 behind the deterministic pre-action layer. On 68,970 matched model, prompt, and track triples, the comparison was 105 versus 0. The layer still executed 25,370 payments, so the result did not come from refusing every action.

Why it matters: model intent classification and agent planning should not be the authorization source of truth for money movement. A structured, user-bound payment passport can permit routine transfers while a deterministic check rejects recipient, amount, or policy mismatches at the commit boundary.

Practical controls worth exploring now:
- express allowed recipients, amount ceilings, time windows, and approval requirements in a typed policy object;
- bind the policy to the user, agent session, account, and intended tool;
- evaluate the final transfer request immediately before the payment API call;
- separate request, tool call, policy decision, execution, and final outcome in telemetry;
- replay real red-team prompts against model-only and model-plus-policy conditions;
- keep an authoritative transfer lookup for uncertain responses and retries.

Artifact status: the APort Vault dataset card and release record were inspected read-only. Access to the 175 MB corpus is gated behind acceptance of research conditions, so the files were not opened or reproduced in this run.

Evidence caveat: each attack belongs to one policy level, so policy and attack cohort vary together outside the matched-triple analysis. The paper has one author, and the deterministic layer implements the author's Open Agent Passport specification.

Implementability score: 0.93

Core sources:
- [APort Vault paper](https://arxiv.org/abs/2609.22076v1)
- [APort Vault dataset](https://huggingface.co/datasets/aporthq/vault-benchmark-v1)
