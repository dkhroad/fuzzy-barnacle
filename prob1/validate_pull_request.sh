#!/bin/bash

JIRA_REGEX="\[JIRA-\d+\]"

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
