Feature: Backfill and correction workflows
  As the operator maintaining the weekly knowledge base
  I want to repair missed or corrected weeks without harming the current week
  So that publication remains resilient across backfills and edits

  Background:
    Given weekly notebooks are tracked by week key in the local sync manifest

  Rule: Backfills are isolated to the targeted week
    Scenario: Backfill a previously missed week without altering the current week
      Given a prior week has curated roundup artifacts that have never been synced
      And the current week already has its own weekly notebook
      When the operator runs a backfill sync for the prior week
      Then a notebook should be created or updated only for the targeted prior week
      And the current week's notebook should remain unchanged

  Rule: Corrections preserve the canonical share target
    Scenario: Correct a published week without creating a second share link
      Given a published week has corrected roundup markdown or cited URLs
      When the operator reruns sync and publication for that same week
      Then the published week should keep one canonical share target
      And readers should not receive a second conflicting share link for that week
