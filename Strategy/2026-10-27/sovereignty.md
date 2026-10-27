# Strategy Daily Sovereignty Note, 2026-10-27

## 1. Keep assisted permission classification inside deterministic policy

GitHub made assisted permissions generally available across Copilot CLI, the Copilot app, and Visual Studio Code. An LLM classifies requests to run commands, access file paths, or open URLs. Clearly safe requests can proceed automatically; others require approval. Enterprise administrators can block Allow All, disable Assisted separately, and set a default permission mode.

Why it matters: this is a practical reduction in approval fatigue, but the classifier is probabilistic. It should select among policy-permitted paths, never create authority or override deterministic denials.

Fit in the strategy: runtime governance and execution control. The enterprise control plane owns the maximum permission mode, while the classifier handles eligible low-risk requests within that ceiling.

Implementable now:
- define deterministic deny and always-ask classes first;
- let classification auto-approve only reversible, scoped actions inside that set;
- bind every decision to exact command, path, URL, principal, and session;
- retain classifier result, policy version, and final disposition as a receipt;
- shadow-test false approvals before enabling automatic passage;
- default to manual approval when policy or classification is unavailable.

Weakest point: the release note does not provide classifier accuracy, false-approval rates, or adversarial evaluation. The feature is therefore an operational pattern, not evidence that an LLM is a sufficient authorization engine.

Implementability score: 0.84

Core source: [GitHub Copilot assisted permissions generally available](https://github.blog/changelog/2026-10-26-github-copilot-assisted-permissions-generally-available)

Supporting source: [GitHub assisted permissions documentation](https://docs.github.com/copilot/concepts/customizations/allowing-safe-commands)

## Working conclusion

Use assisted classification to reduce prompts only after deterministic policy has bounded the action set. Policy grants authority; the classifier routes eligible requests.
