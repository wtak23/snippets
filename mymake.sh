#!/usr/bin/env bash
#=============================================================================#
# do all the make at once
#=============================================================================#
make clean
make html
# bash fix_name.sh
cp ./source/img/favicon-penn.ico ./build/html/static
# firefox ./build/html/index.html
# rsync -r build/html/ published