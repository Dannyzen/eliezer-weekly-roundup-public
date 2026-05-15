Feature: Retry budgets, rate limits, and quota resilience
  As the infrastructure handling unreliable external capacity
  I want throttling and quota failures to preserve progress with useful recovery states
  So that retries stay safe and operator guidance stays precise

  Background:
    Given NotebookLM may throttle or reject requests under load or quota pressure

  Rule: Transient throttling uses bounded retries
    Scenario: Back off and retry after a 429 during URL attachment
      Given NotebookLM rate-limits URL attachment requests for the current week
      When the operator runs the weekly NotebookLM sync
      Then the system should retry with bounded backoff
      And earlier successful work should remain durable

    Scenario: Mark retry-budget exhaustion as retryable rather than ambiguous
      Given a transient weekly sync stage keeps failing until the retry budget is exhausted
      When the run ends
      Then the final status should remain retryable
      And the retry history and failing stage should be recorded

  Rule: Quota exhaustion preserves partial progress
    Scenario: Stop cleanly on quota exhaustion after partial progress
      Given the weekly sync exhausts a NotebookLM quota after some sources were attached
      When the run finalizes
      Then attached sources should remain durably recorded
      And remaining work should be marked retryable with quota guidance
