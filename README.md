# fuzzy-barnacle
CI workflow Examples


## Prob 1: Logic to validate a pull request title has a JIRA number associated with it



The logic to check for a JIRA issues in the form of [JIRA-1234] is implemented in the shell script
`prob1/validate_pull_request.sh`

The script exits with value 0 when the input string contains a valid JIRA issue number, otherwise
it returns 1.

It can be invoked as the following: 
```
❯ ./prob1/validate_pull_request.sh  "[JIRA-1234] a pull request title with a valid  jira issue"
❯ echo $?
0

❯ ./prob1/validate_pull_request.sh  "[1234] a pull request title with a invvalid  jira issue"
ERROR: Pull request title must contain a JIRA issue number
❯ echo $?
1

❯ ./prob1/validate_pull_request.sh  "a pull request title with missing  jira issue"
ERROR: Pull request title must contain a JIRA issue number
❯ echo $?
1

```

To run the unit tests, type: 

```
❯ cd prob1
prob1❯ ./test_validate_pull_request.sh
.......%
prob1❯  
```

The dots indicate all tests passed successfully.

**NOTE**: This script does not implement server logic to receive webhook paylod for a pull request
event.

However, the BASH script `prob1/validate_pull_request.sh` can be easilty invoked from a configured webhook payload 
handler that receives event http header "X-Github-Event:pull_request". The string to be validated
is typically available in JSON payload `pull_request["title"]` as shown below.

```
{ 
  "action": "opened",
  "pull_request": {
  "url": "https://api.github.com/repos/dkhroad/potential-meme/pulls/2",
  "title": "change message"
   ...
   ...
   ...
}
```

## Prob 2: Validate a string containing just the characters "{,},[,],(,)" and one or more numbers. 

File `prob2/string_validator.py' contains the logic to validate a string.`
The code has been tested with both python 2.7 and python 3.7.
To run the unit tests, type: 
  ```
  python prob2/string_validator.py -v
  ```
Expected output: 
  ```
  ❯ python prob2/string_validator_test.py
  ..
  ----------------------------------------------------------------------
  Ran 2 tests in 0.000s

  OK
  ❯ python prob2/string_validator_test.py -v
  git(master)!
  test_with_bad_values (__main__.TestValidBrackets)
  test with known bad values ... ok
  test_with_known_values (__main__.TestValidBrackets)
  test with known good values ... ok

  ----------------------------------------------------------------------
  Ran 2 tests in 0.000s

  OK
  ```

Program `string_validator` can be invoked directly with first arguments as string to be validated. 

  ```
  ❯ python prob2/string_validator.py "()(3){5}"
  input "()(3){5}" is a valid string

  ❯ python prob2/string_validator.py ")(3"
  input ")(3" is NOT a valid string
  ❯
  ```


### Prob 3: Jenkins Pipeline 


File `prob3/ci/Jenkinsfile` contains the Jenkins Pipeline that runs 3 stages.

1. Build stage

    - Checks out the source code using Git Plugin
    - Generates checksum of all files in JSON format using python script `prob3/ci/scripts/cksum.py`

2. Commit stage 

    - Adds/updates and commits the generated checksum for all source files as `checksums.json` to the master branch.
      The commit messages for this operation can be seen via git log.

    ```
      ❯ git l     
      * c6281d0  (HEAD -> master, origin/master, origin/HEAD) [JENKINS_CI] add/update repo md4 checksum file <jenkins-ci> (17 minutes ago)
      * 5d8c38e  prob3: fix syntax error in Jenkinsfile <Devinder Khroad> (19 minutes ago)
      * .....
    ```

3. Push stage

    - Pushes the changes upstream to master branch
    - For now, Github credentials are provided by personal access token. Using a SSH key would
        be more secure and optimal

For now, the Jenkins job is run manually. A future improvement could be to set up a webhook to
automatically run the job after a pull request merge or a commit to master

Here is a sample of actual Jenkin SCM pipeline job output: 

```

SuccessConsole Output
Started by user dkhroad
Obtained prob3/ci/Jenkinsfile from git https://github.com/dkhroad/fuzzy-barnacle.git
Running in Durability level: MAX_SURVIVABILITY
[Pipeline] Start of Pipeline
[Pipeline] node
Running on Jenkins in /Users/dkhroad/.jenkins/workspace/fuzzy-barnacle-local
[Pipeline] {
[Pipeline] stage
[Pipeline] { (Declarative: Checkout SCM)
[Pipeline] checkout
using credential effective-robot
 > git rev-parse --is-inside-work-tree # timeout=10
Fetching changes from the remote Git repository
 > git config remote.origin.url https://github.com/dkhroad/fuzzy-barnacle.git # timeout=10
Fetching upstream changes from https://github.com/dkhroad/fuzzy-barnacle.git
 > git --version # timeout=10
using GIT_ASKPASS to set credentials 
 > git fetch --tags --progress -- https://github.com/dkhroad/fuzzy-barnacle.git +refs/heads/*:refs/remotes/origin/* # timeout=10
 > git rev-parse refs/remotes/origin/master^{commit} # timeout=10
 > git rev-parse refs/remotes/origin/origin/master^{commit} # timeout=10
Checking out Revision 5d8c38ef81d1df15408f316b455c0553245037bc (refs/remotes/origin/master)
 > git config core.sparsecheckout # timeout=10
 > git checkout -f 5d8c38ef81d1df15408f316b455c0553245037bc # timeout=10
Commit message: "prob3: fix syntax error in Jenkinsfile"
First time build. Skipping changelog.
[Pipeline] }
[Pipeline] // stage
[Pipeline] withEnv
[Pipeline] {
[Pipeline] stage
[Pipeline] { (Build)
[Pipeline] sh
+ python ./prob3/ci/scripts/cksum.py
+ cat checksums.json
{
    "prob1/test_validate_pull_request.sh": "be6f000bb24d53d1eb237291042507b8", 
    "LICENSE": "ab1095a0278453c5154dd4c30720b5c5", 
    "prob3/ci/Jenkinsfile": "81c8146c688979386c0bda5302b2ea45", 
    "prob1/validate_pull_request.sh": "89acada9946162a00fd68bdda400946c", 
    "prob2/string_validator.py": "a905f3b49007c572a45e0028c60f4afe", 
    ".gitignore": "6482f9d8254f7f75af96c66a09031e65", 
    "prob2/string_validator_test.py": "48e76ea3c8f1c99a7ec074dc51fd114f", 
    "checksums.json": "d41d8cd98f00b204e9800998ecf8427e", 
    "prob3/ci/scripts/cksum.py": "169747ce1045ca54a3a705ca59e98c5f", 
    "README.md": "30e5dfcc211097c05d76154bccb2c90c"
}
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Commit)
[Pipeline] withEnv
[Pipeline] {
[Pipeline] sh
+ git checkout -B master
Switched to and reset branch 'master'
+ git config user.name jenkins-ci
+ git config user.email jenkins-ci-user@users.noreply.example.com
+ git add .
+ git commit -am '[JENKINS_CI] add/update repo md4 checksum file'
[master c6281d0] [JENKINS_CI] add/update repo md4 checksum file
 1 file changed, 12 insertions(+)
 create mode 100644 checksums.json
[Pipeline] }
[Pipeline] // withEnv
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Push)
[Pipeline] withEnv
[Pipeline] {
[Pipeline] withCredentials
Masking supported pattern matches of $GIT_USERNAME or $GIT_PASSWORD
[Pipeline] {
[Pipeline] sh
+ echo 'username=****  password=****'
username=****  password=****
+ git config --local credential.helper '!f() { echo username=$GIT_USERNAME; echo password=$GIT_PASSWORD; }; f'
+ git config --local --list
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
core.ignorecase=true
core.precomposeunicode=true
remote.origin.url=https://github.com/****/fuzzy-barnacle.git
remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
user.name=jenkins-ci
user.email=jenkins-ci-user@users.noreply.example.com
credential.helper=!f() { echo username=$GIT_USERNAME; echo password=$GIT_PASSWORD; }; f
+ git push origin HEAD:master
To https://github.com/****/fuzzy-barnacle.git
   5d8c38e..c6281d0  HEAD -> master
[Pipeline] }
[Pipeline] // withCredentials
[Pipeline] }
[Pipeline] // withEnv
[Pipeline] }
[Pipeline] // stage
[Pipeline] }
[Pipeline] // withEnv
[Pipeline] }
[Pipeline] // node
[Pipeline] End of Pipeline
Finished: SUCCESS
```
