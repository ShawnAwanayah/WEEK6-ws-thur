# WEEK6-ws-thur

If a folder starts with . then it is hidden

.github/workflows is to make github actions

yaml = yet another markup [something]

#####
name: echo
on: 
  workflow_dispatch:
  pull_request:
  push:
    branches:
    - main
######
This means do the action on workflow_dispatch, pull request and push but only if the branch is main

####
jobs: # job to do
  build: # name of the job
    name: run tests # name of 1 job
    runs-on: ubuntu-latest # this means run on linux
    steps:
    - uses: actions/checkout@v3