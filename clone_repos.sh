#!/bin/bash

#Clone my-bash-scripts in ~
if [ -d "~/my-bash-scripts/" ]; then
  echo "Directory my-bash-scripts exists.. overwriting.."
  rm -rf ~/my-bash-scripts/
fi
mkdir ~/my-bash-scripts/
git clone https://github.com/Typeaway14/my-bash-scripts ~/my-bash-scripts
