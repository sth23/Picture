#!/bin/bash
set -e # exit with nonzero exit code if anything fails

# create the tests folder
mkdir tests
cd tests
git config user.email "you@example.com"
git config user.name "Your Name"
git init
git pull https://github.com/BrythonServer/ggame.git
git pull https://${GH_REPO}
cd ..

python tests/test.py ${TESTMODULE}
