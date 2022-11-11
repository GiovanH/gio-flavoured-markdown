#!/bin/bash

git config --global user.name "Glitch Client"
git config --global user.email gio-flavoured-markdown@glitch.me

git_clone_or_update_force() {
  # Clone a repo, or pull-update it if it already exists.
  repo=$1
  autodest=${repo##*/} # ## delete longest match of pattern from start
  autodest=${autodest%.git} # %  delete shortest match of pattern from end
  gitdest=${2:-$autodest}
  git clone $repo $gitdest \
    || (pushd $gitdest && git fetch; git reset --hard origin; git pull && popd)
  return 0
}

python3 -m pip install -r requirements3.txt \
 & wget -nc 'https://raw.githubusercontent.com/marcel-dancak/lz-string-python/master/lzstring.py' \
 & git_clone_or_update_force https://github.com/GiovanH/mdexts.git \
 & git_clone_or_update_force https://github.com/GiovanH/peliplugins.git
 
wait
