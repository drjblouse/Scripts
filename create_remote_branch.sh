#!/bin/sh
if [ "$#" -ne 1 ]; then
    echo "This script requires the branch name."
    exit 1
fi
BRANCH=$1

git checkout -b ${BRANCH}
git push -u origin ${BRANCH} 
