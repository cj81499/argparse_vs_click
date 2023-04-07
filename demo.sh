#!/usr/bin/env bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 {click, argparse}"
    exit 1
fi

BLUE='\033[0;34m'
NO_COLOR='\033[0m'

function run {
    echo -en "${BLUE}command: "
    printf "%q " "$@" # log command, escaping arguments
    echo -e "${NO_COLOR}\nBEGIN OUTPUT"
    "$@"
    echo -e "END OUTPUT\nexit code: $?\n\n"
}

cmd="git-$1"

set +e # do not exit on errors

run "$cmd"
run "$cmd" --help

run "$cmd" add
run "$cmd" add --help
run "$cmd" add abc
run "$cmd" add .gitignore
run "$cmd" add .gitignore pyproject.toml
run "$cmd" add .gitignore pyproject.toml abc

run "$cmd" commit
run "$cmd" commit --help
run "$cmd" commit -mhi
run "$cmd" commit -m'hi there'
run "$cmd" commit -m 'hi there'
run "$cmd" commit --message 'hi there'
run "$cmd" commit --message='hi there'
run "$cmd" commit --amend
run "$cmd" commit --no-amend
run "$cmd" commit --amend -m 'hello how are you'
run "$cmd" commit --no-amend -m 'hello how are you'

