# Strategy Daily Analysis: 2026-11-15

Today's strategy signal is that production control planes are separating observation, authority, and execution instead of treating the agent transcript as one undifferentiated record.

## 1. Separate operational telemetry from sensitive conversation content

Google Data Cloud now separates aggregate metrics and sanitized trace spans from optional conversation logging. Cloud Monitoring and Cloud Trace can cover request volume, latency, token usage, and step spans without storing prompts, responses, internal thoughts, or generated SQL. Deeper transcript logging is opt-in per agent and lands in a customer-owned BigQuery `agent_events` table.

Why it matters: observability does not require universal transcript capture. A two-layer design gives operators enough data for availability, cost, and latency work while reserving sensitive content access for explicit debugging or audit cases.

Implementable now:
- define a content-free operational event contract for every agent run;
- gate prompt, response, tool argument, and payload logging separately;
- keep content logs in an owner-controlled store with independent IAM and retention;
- skip content logging when protected sources or masking policies make capture unsafe;
- keep user execution available when the logging sink fails, while emitting a logging-failure receipt;
- evaluate prompt or schema changes against reusable test cases before promotion.

Evidence and caveat: Google's first-party path skips conversation logging when row-level security, policy tags, or dynamic masking are active, while agent execution continues if logging fails. Custom ADK and LangGraph agents can emit fuller tool trees through an open plugin. These are vendor capabilities, not independent evidence that the design meets another environment's privacy or recovery requirements.

Artifact status: official announcement and linked public SDK references inspected. Nothing was executed.

Implementability score: 0.90

Core source: [Google Data Cloud agent observability and governance](https://cloud.google.com/blog/products/data-analytics/enterprise-ai-agent-observability-with-bigquery-and-looker/)

Useful artifact: [BigQuery Agent Analytics SDK](https://github.com/GoogleCloudPlatform/BigQuery-Agent-Analytics-SDK)

## 2. Put context classification, task authority, and execution budgets in middleware

Microsoft Agent Framework Python 1.26.0 adds an experimental application-owned `SecureAgentConfig.message_labeler`, task-scoped authority middleware guidance with an executable sample, and a default finite 30-second budget for Hyperlight guest execution. The same release supports schema-bound responses through Pydantic models or JSON Schema mappings.

Why it matters: the framework is moving control decisions out of prompts and into runtime hooks. Applications label context, middleware constrains task authority, schemas constrain handoffs, and the sandbox enforces cancellation and time budgets.

Implementable now:
- classify context-provider messages before they enter planning context;
- bind task authority to principal, task, resources, and expiry;
- require typed outputs at agent and workflow boundaries;
- set finite execution budgets and test cancellation propagation;
- preserve classification, grant, invocation, timeout, and cleanup receipts.

Evidence and caveat: these capabilities appear in the official tagged release and linked examples. `message_labeler` is explicitly experimental, and the Hyperlight change is breaking for older SDKs. Adoption requires exact-version replay rather than broad framework trust.

Artifact status: MIT-licensed repository and release inspected read-only. No source was cloned or executed.

Implementability score: 0.86

Core source: [Microsoft Agent Framework Python 1.26.0](https://github.com/microsoft/agent-framework/releases/tag/python-1.26.0)

## Working conclusion

A serious agent control plane has separate contracts for telemetry, sensitive content, context classification, task authority, typed handoffs, execution budgets, and effect receipts.
