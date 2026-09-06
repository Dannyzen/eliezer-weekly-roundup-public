# Strategy Daily Analysis - 2026-09-06

No new Sunday arXiv listing. These findings were submitted 29 Aug and 3 Sep 2026 UTC and first listed Friday, 4 Sep 2026. They were not in the 2026-09-04 synthesis or the 2026-09-05 daily.

## A parsable success is not an honest tool

SilentProbe's sovereignty claim is about the tool boundary, not about model quality. An agent that receives HTTP 200 with a JSON body will treat the call as authorized evidence. If the schema never named the legal values, that body can be an answer to a different question. Downstream loops then assert a false negative or invent a figure. The failure is in the contract, and the contract is an authority object.

The fix is admission, not a smarter retry. Put enumerations and bounds in the machine-readable schema. Reject tools whose vocabularies exist only as `e.g.` examples. Treat empty or partial 200s as ambiguous until the API names no-match. Keep a run identifier so a silent result can be re-fetched instead of trusted.

Why it matters: FriendVM, Hermes, and any MCP/OpenAPI gateway that wraps third-party APIs inherit this surface. A gateway that only checks OAuth and HTTP status will launder silent failures into the agent's evidence set.

Fit in strategy: untrusted data boundaries plus agent gateway governance. Tool output is untrusted until the schema can reject it. ACLE-MCP binds invocation-time trust. SilentProbe binds result honesty.

Practical tools and methodologies worth exploring now:
- schema-validate tool arguments before dispatch and tool results before they enter context;
- fail closed on exemplified-only vocabularies;
- score silent-failure and fabricated-figure rates as gateway SLOs;
- do not let a 200 body become standing memory without a typed no-match or error field.

Artifact status: [Jasper0122/silentprobe](https://github.com/Jasper0122/silentprobe) resolves, MIT, populated `master`. Inspected read-only. Live vendor replication needs an aggregator equivalent to Monid.

Implementability score: 0.82

Core sources:
- [SilentProbe, arXiv:2609.00035v1](https://arxiv.org/abs/2609.00035v1)
- [Jasper0122/silentprobe](https://github.com/Jasper0122/silentprobe)

## Hosted judges are not a sovereign measurement plane

The unstable-measurement paper is a containment finding for evaluation. A preregistered observer on a shared endpoint failed its own reliability gates with execution records at ceiling. Switching providers did not restore a frozen instrument. Self-hosting helped only while the server was quiet.

If the judge is a black-box hosted model, the eval is not local-first and it is not reproducible. Sovereignty here means: pin the observer, measure it, and refuse to freeze a gate on a model name that failed Spearman 0.90 same-window or 0.99 next-day replay.

Why it matters: every dual-oracle and LLM-as-judge pipeline in this repo inherits a hidden dependency on observer stability. Without an instrument gate, "the judge said fail" is not evidence.

Fit in strategy: evaluation containment and evidence provenance. The observer is part of the trusted computing base of the eval, not a commodity API.

Practical tools and methodologies worth exploring now:
- run instrument gates before task gates;
- prefer local or batch-invariant observers when a scientific verdict is required;
- publish request hashes and authorisation ledgers with eval results;
- treat a shared model ID as a moving vendor service, not as a pinned artifact.

Implementability score: 0.58 for hosted observers with an instrument gate; 0.40 if the only available judge is an unmeasured shared endpoint.

Core source: [Clean Engineering, Unstable Measurement, arXiv:2609.04198v1](https://arxiv.org/abs/2609.04198v1)

## Replay without tool state is unauthorized reconstruction

DNative-Twin's graph can reconstruct what was stored and still miss what an unobserved tool timeout would have done. Adding replay-contract state and verification results is what moved unresolved-divergence recall off zero. Reconstruction that labels an unobserved timeout as benign is an authorization error: it treats missing evidence as a safe default.

CrowdStrike's 2 Sep Agentic Identity Provider is the product-side rhyme, not today's measured finding. It registers agents, brokers short-lived access, and keeps human/workload attribution. Useful demand signal. It is a vendor control plane, not a replay contract, and the post itself flags unreleased features. Keep it as a watch item.

Why it matters: audit trails that omit tool state will certify decisions that would have gone the other way under a timeout or a failed verifier. That is how GRC evidence becomes theater.

Fit in strategy: evidence provenance plus execution control. Typed trajectories need a replay contract. Identity establishment is necessary and not sufficient.

Practical tools and methodologies worth exploring now:
- refuse reconstructability claims unless tool results and verifier verdicts are in the contract;
- treat missing tool state as unresolved divergence, never as benign;
- keep identity, authorization, and replay as three objects.

Implementability score: 0.45

Core source: [DNative-Twin, arXiv:2609.03787v1](https://arxiv.org/abs/2609.03787v1)

Watch item, not scored as a top finding: [CrowdStrike Agentic Identity Provider](https://www.crowdstrike.com/en-us/blog/crowdstrike-announces-agentic-identity-provider/), dated 2 Sep 2026, with an explicit unreleased-features disclaimer.

## Working conclusion

A 200, a model name, and a decision graph are observations. Honesty needs a schema. Measurement needs an instrument gate. Reconstruction needs tool state. Missing evidence is not a safe default.
