#!/usr/bin/env bash
#=============================================================================#
# do all the make at once
#=============================================================================#
make clean
rm -r ./source/generated*
make html
# bash fix_name.sh
# cp ./source/img/favicon-penn.ico ./build/html/static
# firefox ./build/html/index.html
# rsync -r build/html/ published