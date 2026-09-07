# Strategy Daily Sovereignty - 2026-09-07

## Freshness and selection

arXiv exposed a real Monday, 7 Sep 2026 listing batch. CONTINUITY v1 was submitted on 4 Sep UTC and first listed after the weekend. Claims below were checked against the immutable paper, PDF, and populated public artifact without cloning or execution.

## Security controls need end-to-end continuity contracts

CONTINUITY names a system failure that component audits miss: identity, provenance, grant, policy, transformation, action, or lifecycle context can be valid at one boundary and be dropped, widened, rebound, or reinterpreted before the external effect. Its reference design carries signed root grants, provenance and context manifests, bounded typed releases, role-bound transition receipts, transformation witnesses, and effect-bound finality permits through an assume-guarantee contract.

The deterministic conformance suite covers 32 fault classes across four domains. The paper reports 3,460 scenarios and 24,220 system-scenario executions. The full configuration committed no harmful effect in 2,560 parameterized attack instances, completed all 700 benign tasks, and escalated all 200 ambiguous tasks. The strongest incomplete gateway-plus-finality configuration still committed a harmful effect in 65.6% of its attack instances.

Why it matters: adding provenance, authorization, policy, and an execution gate does not prove that their guarantees compose. The authorization witness must survive every adapter and remain bound to the exact effect at finality.

Fit in strategy: context-to-execution integrity and execution control. The governing object is a complete instruction-to-effect witness, not a bag of individually green middleware checks.

Practical tools and methodologies worth exploring now:
- define an assume-guarantee contract for every context-transforming component;
- canonicalize action fields before signing and bind permits to the canonical digest;
- require witnesses for aliases, currency conversion, path rewrites, and other security-relevant transforms;
- recheck policy, revocation, subject, and single-use state at the finality sink;
- enumerate alternate effect paths and fail the release if any bypass mediation;
- preserve transition receipts and outcome receipts for incident reconstruction.

Weakest point: this is a 1.5-KLOC Python reference with a deterministic synthetic fault space, not a mechanically verified or production-integrated MCP, A2A, IAM, or payment system. That is survivable here because the artifact is useful as a conformance pattern. The guardrail is to adopt its contract tests before its cryptographic machinery, then validate real effect paths and trusted roots locally.

Artifact status: `zast-ai/continuity` is public, MIT licensed, has a populated `main` branch, 30 tests, raw results, ablations, figures, and a claim-to-evidence guide. It was inspected read-only and not reproduced.

Implementability score: 0.83

Core sources:
- [CONTINUITY, arXiv:2609.05269v1](https://arxiv.org/abs/2609.05269v1)
- [zast-ai/continuity](https://github.com/zast-ai/continuity)

## Working conclusion

A chain of individually valid controls can still authorize the wrong effect. Preserve the security context as a typed, signed, current witness from ingress through finality, and test every place that can weaken or bypass it.
