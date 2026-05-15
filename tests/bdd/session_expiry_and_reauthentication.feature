Feature: Mid-run session expiry and reauthentication recovery
  As the operator depending on browser-backed auth
  I want session expiry to stop safely and resume cleanly after reauthentication
  So that auth churn never creates duplicate notebooks, sources, or accidental publication

  Background:
    Given the workflow uses an approved NotebookLM account session

  Rule: Expiry after partial progress is durable and blocked
    Scenario: Session expires after notebook resolution but before source attachment
      Given the run begins with a valid approved session
      And the session expires after the weekly notebook is resolved
      When the weekly sync continues
      Then the run should stop with an auth-blocked status
      And the resolved notebook identity should remain durably recorded

  Rule: Reauthenticated retries reuse prior work
    Scenario: Reauthenticated retry resumes instead of recreating remote objects
      Given a previous run stopped because the session expired after partial progress
      When the operator reauthenticates and reruns the weekly NotebookLM sync
      Then the existing notebook and attached sources should be reused
      And no duplicate notebook or source should be created

  Rule: Publication account changes fail closed
    Scenario: Account identity changes before publication
      Given sync progress was made under the approved account
      And publication is later attempted under a different authenticated account
      When the run reaches the publish step
      Then publication should fail closed
      And prior sync progress should remain intact but unpublished
