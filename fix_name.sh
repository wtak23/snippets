#!/usr/bin/env bash
#=============================================================================#
# It appears that github.io doesn't recognize directory beginning with "_", 
# the underscore character. 
#-----------------------------------------------------------------------------#
# Repalce string "_static" with "static"
# Repalce string "_sources" with "sources"
# Repalce string "_images" with "images"
#=============================================================================#
#http://stackoverflow.com/questions/14505047/bash-loop-through-all-the-files-with-a-specific-extension
for file in "./build/html/*.html"; do
    #echo $file
    sed -i 's/_static\//static\//' $file
    sed -i 's/_sources\//sources\//' $file
    sed -i 's/_modules\//modules\//' $file
done

# repeat above for list of subdirectories
SUBDIR=('awk-tutorial' )

for subdir in "${SUBDIR[@]}"; do
    for file in "./build/html/${subdir}/*.html"; do
        #echo $file
        sed -i 's/_static\//static\//' $file
        sed -i 's/_sources\//sources\//' $file
        sed -i 's/_modules\//modules\//' $file
    done
done


# rename directories with underscore (so they appear on github.io)
build_dir='./build/html'
mv ${build_dir}/_sources ${build_dir}/sources
mv ${build_dir}/_static ${build_dir}/static
mv ${build_dir}/_modules ${build_dir}/modules

