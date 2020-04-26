#!/bin/bash

assert_eq() {
  local expected="$1"
  local actual="$2"
  local message="$3"

  if [[ $expected == $actual ]]; then
    echo -n "."
    return 0
  else
    echo "$expected == $actual :: $message"
    return 1
  fi
}


source ./validate_pull_request.sh

check_for_jira_issue "[JIRA-1234] a pull request title with a valid  jira issue"
assert_eq 0 $? "FAILED"

check_for_jira_issue "A pull request title with a valid [JIRA-8947] jira issue"
assert_eq 0 $? "FAILED"

check_for_jira_issue "A pull request title with a valid [jira-8947] jira issue"
assert_eq 0 $? "FAILED"


check_for_jira_issue "[JR1A-1234] a pull request title with an invalid jira issue " > /dev/null
assert_eq 1 $?  "FAILED"

check_for_jira_issue "[JR1A-] a pull request title with an invalid jira issue " > /dev/null
assert_eq 1 $?  "FAILED"

check_for_jira_issue "[JIRA-9] a pull request title with an invalid jira issue " > /dev/null
assert_eq 0 $?  "FAILED"


check_for_jira_issue "a pull request without a jira issue " > /dev/null
assert_eq 1 $?  "FAILED"
