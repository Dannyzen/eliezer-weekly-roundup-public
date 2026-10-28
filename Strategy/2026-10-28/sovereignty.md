# Strategy Daily Sovereignty Note, 2026-10-28

## 1. Give autonomous workloads their own revocable identity

GitHub Copilot SDK now accepts short-lived installation tokens from organization-installed GitHub Apps. A service can make Copilot requests without borrowing a signed-in user's credentials. Usage is attributed to the organization and identified by `app_client_id` in CSV reports. Organization model policies and budgets apply, and access can be stopped by suspending or uninstalling the app.

Why it matters: unattended agents should operate as workloads with explicit ownership, billing, policy, and revocation. A human credential hides who initiated the work and makes offboarding or incident response harder.

Fit in the strategy: identity, execution control, and cost governance. The workload principal should be distinct from the human approver and from the downstream resource credentials used by tools.

Implementable now:
- assign one GitHub App identity per bounded service or trust domain;
- mint short-lived installation tokens and disable fallback to stored user credentials;
- bind model policy and spending controls to the owning organization;
- retain app identity, model, usage, task, and effect receipts together;
- revoke the workload independently from human accounts;
- use a budget that stops usage when a hard ceiling matters.

Weakest point: the feature is in public preview, attribution appears in CSV rather than the interactive usage view, and GitHub does not support a per-app budget. Organization-level budgets therefore need an external per-workload guard if one noisy app must be contained without stopping all others.

Implementability score: 0.90

Core source: [GitHub Copilot supports server-to-server authentication](https://github.blog/changelog/2026-10-27-github-copilot-supports-server-to-server-authentication/)

Supporting sources: [server-to-server authentication documentation](https://docs.github.com/copilot/how-tos/copilot-sdk/auth/server-to-server-tokens), [GitHub App Copilot access and billing controls](https://docs.github.com/copilot/how-tos/administer-copilot/manage-for-organization/manage-app-copilot-access)

## Working conclusion

Give unattended agents workload-owned, short-lived, revocable identity. Human approval remains a separate authority layer, and organization policy remains the ceiling.
