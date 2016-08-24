#!/usr/bin/env bash
#=============================================================================#
# do all the make at once
#=============================================================================#
#-------------------------------------------------------------------------#
# when running script from sublime-build, python calls from /usr/bin/python.  
# i want anaconda python to run
#-------------------------------------------------------------------------#
export PATH="$HOME/anaconda2/bin:$PATH" 
# which python # <- verify python from anaconda is running

make clean
rm -r ./source/generated*
make html

#| not 100% happy with this approach in SO:
#| http://stackoverflow.com/questions/14345922/how-to-do-a-link-to-a-file-in-rst-with-sphinx
#| so i'm just gonna manually copy and paste pdf files to the build directory here
# cp -r ./source/_static/pdf ./build/html/_static/
# firefox "$PWD"/build/html/index.html

# bash fix_name.sh
# cp ./source/img/favicon-penn.ico ./build/html/static
# firefox ./build/html/index.html
# rsync -r build/html/ published