Feature: Authentication and account boundaries
  As the owner of the NotebookLM publishing workflow
  I want authentication and account checks to fail closed
  So that the weekly notebook is never created, updated, or shared from the wrong account

  Background:
    Given the system knows the approved publishing account and the current weekly payload

  Rule: No mutation happens without a valid NotebookLM session
    Scenario: Abort before first write when no valid NotebookLM session exists
      Given no valid NotebookLM session exists
      When the operator starts the weekly NotebookLM sync
      Then the sync should fail before any notebook is created or updated
      And the run should be marked blocked by authentication

  Rule: The publishing account must match the approved identity
    Scenario: Reject a valid session for the wrong account
      Given a valid NotebookLM session exists for an account that is not approved for publishing
      When the operator starts the weekly NotebookLM sync
      Then the sync should fail closed before any write or share action
      And the operator should be told that the authenticated account is not approved

  Rule: Share scope must honor notebook-level visibility limits
    Scenario: Refuse to publish a mixed-sensitivity notebook
      Given the weekly notebook contains public roundup material and internal-only notes
      When the operator requests a shareable weekly notebook
      Then publication should be blocked
      And the operator should be told that sharing is only supported at notebook level
