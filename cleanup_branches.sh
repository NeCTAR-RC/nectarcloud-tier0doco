#!/usr/bin/env bash

# This script, when run on OSX or Linux should clean up all local branches that have been merged to master.
# It works by pipelining the output from one command as input to the next command on.
#
# The first command:
#       git branch --merged master
# lists all your local branches that have been merged into master.
# The next command
#       grep -v "^\*"
# removes any lines that may start with a '*' (i.e. Excludes the branch currently open)
# Then
#       grep -v master
# removes the branch named master from the list.
# If you want to remove any other branches, such as say 'dev', just add them to the pipeline, as we do here
#       grep -v dev
# The final command iterates through the list, running git branch -d on each entry.
#       xargs -n 1 git branch -d
#
# To run the script, simply do a git pull (to make sure you are up to date), then
#       ./cleanup_branches.sh

git branch --merged master | grep -v "^\*" | grep -v master | grep -v dev | xargs -n 1 git branch -d