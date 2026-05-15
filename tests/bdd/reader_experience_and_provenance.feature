Feature: Reader experience, provenance, and rollback safety
  As the public reader of a shared weekly notebook
  I want one trustworthy weekly entry point with visible provenance
  So that I can understand what I am listening to and trust that rollback is possible if something is wrong

  Background:
    Given the weekly roundup may eventually be shared outside the operator environment

  Rule: Published output should be understandable to readers
    Scenario: Publish a notebook with visible week identity and provenance
      Given the current week is ready for publication
      When the operator publishes the weekly notebook
      Then the public notebook should clearly identify the target week
      And the published package should preserve provenance for the curated markdown and cited sources

    Scenario: Keep one canonical share target per week for readers
      Given the current week has already been published once
      When the operator republishes that same week after a correction
      Then readers should continue using one canonical share target for that week
      And they should not be forced to discover a second conflicting public notebook

  Rule: Rollback stays possible after publication
    Scenario: Revoke public sharing after a post-publish policy violation
      Given the current week has already been published
      And a post-publish review finds a policy violation in the published notebook
      When the operator triggers a publication rollback
      Then the system should attempt to revoke public sharing for that week
      And the week should be marked as rolled back or pending manual recovery
