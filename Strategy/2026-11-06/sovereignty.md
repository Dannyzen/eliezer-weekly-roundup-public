# Strategy Daily Analysis: 2026-11-06

## 1. Test social engineering at the action boundary across modalities

Multimodal-SEA evaluates 608 expert-designed tasks across 14 domains and 152 social-engineering scenarios. Seven multimodal models showed attack success rates from 7.1 percent to 34.5 percent. Adding forged multimodal content raised attack success from 19.9 percent to 29.2 percent even though agents performed more proactive verification. Stronger safety instructions reduced attacks, but some gains came with excessive refusal of legitimate requests.

Why it matters: text-only prompt-injection tests miss attacks carried by screenshots, documents, voices, and forged media. Recognition is also insufficient. The security outcome is whether the agent executed a harmful action, asked for independent verification, refused safely, or blocked legitimate work.

Strategy fit: untrusted-data boundaries, multimodal approval views, and execution-time gateway policy.

Implementable now:
- create matched benign and malicious tasks using text, image, document, and audio evidence;
- bind each attack outcome to simulated application logs rather than response wording;
- require independent verification through a trusted channel before consequential writes;
- keep the approval view source-literal and expose origin, recipient, object, amount, and action;
- score attack success, verification coverage, legitimate completion, and over-refusal together;
- preserve cultural and language variants instead of translating one attack template mechanically.

Artifact status: the paper names `Zhitao-He/M-SEABench`, but that repository did not resolve on GitHub during this scan. The paper and its method are verified; the implementation artifact is unavailable.

Evidence caveat: the benchmark uses simulated applications and prepared attacks. It measures intrinsic agent behavior under controlled scenarios, not the full security of a production channel and identity stack.

Implementability score: 0.76

Core source: [Multimodal-SEA v1](https://arxiv.org/abs/2611.08281v1)
