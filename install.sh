#!/bin/bash

git_clone_or_update() {
  eg Clone a repo, or pull-update it if it already exists.
  repo=$1
  autodest=${repo##*/} # ## delete longest match of pattern from start
  autodest=${autodest%.git} # %  delete shortest match of pattern from end
  gitdest=${2:-$autodest}
  git clone $repo $gitdest \
    || (pushd $gitdest && git pull && popd)
  return 0
}

python3 -m pip install -r requirements3.txt \
 & wget 'https://raw.githubusercontent.com/eduardtomasek/lz-string-python/master/lzstring.py' \
 & git_clone_or_update https://github.com/GiovanH/mdexts.git \
 & git_clone_or_update https://github.com/GiovanH/peliplugins.git
 
wait
