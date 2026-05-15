# Agent Provisioning Governance

Agent provisioning governance is the control-plane discipline for allowing autonomous or semi-autonomous agents to create accounts, spend budget, register domains, mint credentials, and deploy services.

## Why this topic now

Cloudflare and Stripe have made the boundary explicit: agents can now provision Cloudflare accounts, start paid subscriptions, register domains, get API tokens, and deploy production code through Stripe Projects flows.

Core sources:
- Cloudflare: Agents can now create Cloudflare accounts, buy domains, and deploy: https://blog.cloudflare.com/agents-stripe-projects/
- Stripe Projects docs: https://docs.stripe.com/projects
- Cloudflare Agent Skills: https://github.com/cloudflare/skills
- Cloudflare Code Mode MCP: https://blog.cloudflare.com/code-mode-mcp/

## Core thesis

Once an agent can buy, provision, and deploy, governance has to cover commercial authority, not only tool authority.

The operator needs to know:
- who authorized the agent to spend money;
- what budget and provider catalog were available;
- what service was selected and why;
- what account or legal principal owns the created resource;
- what credentials were issued;
- what was deployed and where;
- how to revoke, transfer, or clean up the resulting resources.

## Control layers

### 1. Discovery governance

Service catalogs should be scoped. An agent should not discover every purchasable provider or service by default. Catalog entries need owner approval, risk labels, cost metadata, and allowed workflow contexts.

### 2. Identity and legal principal mapping

A platform identity assertion is not enough by itself. The system should preserve which human, organization, billing entity, and agent workflow were bound together when the account or resource was created.

### 3. Budget and payment controls

Payment tokens should be budgeted and purpose-scoped. The agent should not receive raw card details or unlimited spend authority.

### 4. Credential issuance

API tokens returned to an agent should be short-lived, least-privilege, environment-scoped, and trace-linked. Token issuance is a privileged state transition.

### 5. Human approval and terms acceptance

Human approval should be explicit for high-risk purchases, domain registration, external publication, and terms acceptance. The approval artifact should be stored in the same evidence chain as the agent action.

### 6. Resource lifecycle and revocation

Created accounts, domains, subscriptions, tokens, and deployments need ownership, tagging, expiry, revocation, and cleanup paths.

## What to build now

- Separate permission to build from permission to buy, register, mint tokens, and deploy.
- Maintain workflow-specific budgets and provider allowlists.
- Gate domain registration and public deployment behind approval.
- Issue scoped, short-lived tokens and record token scope in traces.
- Tag agent-created resources with workflow, user, approval, and expiry metadata.
- Add cleanup and transfer workflows for resources created by agents.
- Include provisioning events in the same audit trail as code-generation and deploy events.

## What to avoid

Avoid these traps:
- giving agents broad cloud credentials because the deploy path is inconvenient;
- treating payment confirmation as a UI prompt rather than a policy event;
- letting agents register arbitrary domains without brand or abuse checks;
- logging the deploy but not the account creation, purchase, or token issuance;
- leaving agent-created resources ownerless after the session ends;
- assuming one provider integration solves the cross-cloud governance problem.

## April 30 source update: Cloudflare and Stripe make agents into provisional cloud customers

Cloudflare’s release is the first clean product-shape signal for this topic. Their stated flow has three components: discovery, authorization, and payment. An agent can query a provider catalog, rely on Stripe to attest user identity, use payment tokenization, provision or link a Cloudflare account, obtain an API token, buy a domain, and deploy.

That is powerful because it removes setup drag. It is risky for the same reason. The fewer manual steps exist, the more important the policy and evidence chain becomes. The right architecture is not to block agent provisioning. It is to make provisioning a governed runtime capability with budgets, scoped credentials, approval records, resource tags, and revocation paths.

## Implementability score

0.82

The Cloudflare/Stripe path is already usable inside that ecosystem. Generalizing the pattern across providers and organizations requires meaningful platform work, but the controls themselves are well understood: identity, budget, scoped credentials, approval artifacts, audit traces, and lifecycle management.
