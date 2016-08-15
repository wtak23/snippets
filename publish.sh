#!/usr/bin/env bash
#=============================================================================#
# do all the make at once
# (insert commit message too)
#=============================================================================#
rsync -r build/html/ build_published
# cd build_published
# git aac "${1}" # commit message
# git pu
# cd -