Here snippets and explanations for writing bash scripts


`[Parent Directory] <./>`_

.. contents:: **Table of Contents**
    :depth: 2

.. sectnum::    
    :start: 1    

#############################
control rsync recursive depth
#############################
http://unix.stackexchange.com/questions/178362/rsync-recursively-with-a-certain-depth-of-subfolders

.. code:: bash

    #Facilitate the --exclude= option.
    #To sync to a depth of 2 (files within folder and subfolders):
    rsync -r --exclude="/*/*/" source/ target/
    
########################################
skip scp if file exist (tldr - use rsync
########################################
- http://unix.stackexchange.com/questions/14191/scp-without-replacing-existing-files-in-the-destination
- ``rsync -a --ignore-existing ${source_dir} ${target_dir}``

##############
rsync symlinks
##############
- http://superuser.com/questions/799354/rsync-and-symbolic-links

##############################
linewrap convention? (none...)
##############################
- apprently none, so stick with one convention
- http://unix.stackexchange.com/questions/39210/whats-the-standard-for-indentation-in-shell-scripts

#################################
Appending/concatenating variables
#################################
- http://stackoverflow.com/questions/4181703/how-can-i-concatenate-string-variables-in-bash
- http://unix.stackexchange.com/questions/163898/how-to-assign-a-string-value-to-a-variable-over-multiple-lines-while-indented

.. code:: bash

    source_dir="watanabt@cbica-cluster.uphs.upenn.edu:"
    source_dir+="/cbica/projects/autism/TobaccoCAR/Data/Results/Smoothed_Template_Space_Maps"

    # or 
    source_dir="watanabt@cbica-cluster.uphs.upenn.edu:"
    source_dir="${source_dir}/cbica/projects/autism/TobaccoCAR/Data/Results/Smoothed_Template_Space_Maps"
#########################
``command`` vs $(command)
#########################
- $(commands) does the same thing as backticks, but you can nest them.
- `source <http://stackoverflow.com/questions/2657012/how-to-properly-nest-bash-backticks>`_

.. code:: bash

    echo $(date +"%Y-%m-%d_%H:%M:%S")

########################
variable name convention
########################
- UPPERCASE for env-vars and constant values
- lowercase for local vars

http://unix.stackexchange.com/questions/42847/are-there-naming-conventions-for-variables-in-shell-scripts

#######################
How to expand ~ (tilde)
#######################
http://stackoverflow.com/questions/3963716/how-to-manually-expand-a-special-variable-ex-tilde-in-bash
``echo ${HOME}``

.. code:: bash

    out_dir="${HOME}/data/tob/dti_volumes"
    echo ${out_dir}
    echo ${out_dir}/subdirec


#######################################################
Create directory if it doesn't exist 06-14-2016 (00:17)
#######################################################
- ``-p`` option does it, but for pedagogical purpose...
- http://stackoverflow.com/questions/4906579/how-to-use-bash-to-create-a-folder-if-it-doesnt-already-exist

.. code:: bash

    if [ ! -d /home/mlzboy/b2c2/shared/db ] 
    then
        mkdir -p /home/mlzboy/b2c2/shared/db
    fi

####################
[@] vs [*] in arrays
####################
http://stackoverflow.com/questions/3348443/a-confusion-about-array-versus-array-in-the-context-of-a-bash-comple

.. code:: bash

    perls=(perl-one perl-two)

    # equivalence with *
    compgen -W "${perls[*]} /usr/bin/perl" -- ${cur}
    compgen -W "perl-one perl-two /usr/bin/perl" -- ${cur}

    #equivalence with @
    perls=(perl-one perl-two)
    compgen -W "${perls[@]} /usr/bin/perl" -- ${cur}
    compgen -W "perl-one" "perl-two /usr/bin/perl" -- ${cur}