Feature: Source sync resilience and idempotent imports
  As the infrastructure responsible for NotebookLM synchronization
  I want source ingestion to survive retries and partial failures
  So that curated research is not duplicated, lost, or silently skipped

  Background:
    Given the weekly notebook exists or can be created
    And the sync manifest tracks notebook and source state

  Rule: The system imports both markdown and external sources
    Scenario: Import roundup markdown and external cited URLs
      Given the week's roundup markdown contains external URLs and local repo links
      When the operator runs the weekly NotebookLM sync
      Then the roundup markdown should be attached as a file source
      And only external cited URLs should be attached as URL sources

  Rule: Partial failures preserve successful progress
    Scenario: Continue syncing when one cited URL is unreachable
      Given the week's cited URL manifest contains valid URLs and one unreachable URL
      When the operator runs the weekly NotebookLM sync
      Then successful sources should remain attached to the weekly notebook
      And the unreachable URL should be recorded as a retryable failure

    Scenario: Resume after an interrupted sync without duplicate source uploads
      Given some weekly sources were attached before the sync process stopped unexpectedly
      When the operator reruns the weekly NotebookLM sync
      Then only the missing sources should be attached on retry
      And already attached sources should not be duplicated
