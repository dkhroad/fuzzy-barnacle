#!/bin/bash

# A shell script to check if the given string
# cantains a sub string in the form of [JIRA-<number]. 
# where <number> as string of digits. For example: [JIRA-124578]
# 

JIRA_REGEX="\[JIRA-\d+\]"

# returns 0 if the the string provided as the first argument contains
# a sub string with JIRA issue number in square brackets.
# for example:
# check_for_jira_issue "[JIRA-1234] a pull request title with a valid  jira issue"


check_for_jira_issue() {
  local message=$1
  if  echo $message | grep -iqE $JIRA_REGEX ; then
    return 0 
  else
    echo "ERROR: Pull request title must contain a JIRA issue number"
    return 1
  fi
}


# the following check enables sourcing of this file from the test harness
# see test_validate_pull_request.sh for more info 
if ! [[ -z $1 ]]; then
  check_for_jira_issue "$1"
fi
