bash-scripts
""""""""""""

Here snippets and explanations for writing bash scripts

.. contents:: **Table of Contents**
    :depth: 2



####
qsub
####

********************
my old qsub approach
********************

slave script
============
Create ``qsub_batch.sh`` with the following content:

.. code-block:: bash

    #!/bin/bash

    #$ -S /bin/bash
    #$ -cwd

    #$ -l h_vmem=4G

    ipython "/sbia/home/watanabt/python/analysis/pnc/ncv_conn_random/pnc_randomized_ncv.py" \
        ${age_group} ${clf_name} ${cv_outer} ${cv_inner}
    

minimalist call
===============
No stdout, stderr

.. code-block:: bash

    qsub -v arg1, arg2, arg3, arg4 qsub_batch.sh

master script
=============
This script will repeatedly call above:

.. code-block:: bash

    #!/usr/bin/env bash
    # ===============================================================================
    # Nested 10-fold CV on the PNC data at arbitrary "random_state" values.
    # Script to be called with the falling argv inputs:
    # - argv[1] = age_group ('q1', 'q2', 'q3', or 'all')
    # - argv[2] = clf_name (see available classifiers from "pnc_clf_choice.py")
    # - argv[3] = rand_st_outercv - integer of random_state for outer-cv
    # - argv[4] = rand_st_innercv - integer of random_state for inner-cv
    # 
    # File shall be saved at:/<this script's location>/dump/<clf_name>/***.pkl
    # 
    # Example call from shell:
    # ipython pnc_randomized_ncv.py q1 sklLogregL1 $(shuf -i 1-500000 -n 2)
    # ===============================================================================

    # http://www.thegeekstuff.com/2010/06/bash-array-tutorial/
    age_group=q1
    clf_name=sklLogregL1

    # create random integer between 1 to 500000 for random_state 
    cv_outer=$(shuf -i 1-500000 -n 1)
    cv_inner=$(shuf -i 1-500000 -n 1)
    echo "ipython pnc_randomized_ncv.py ${age_group} ${clf_name} ${cv_outer} ${cv_inner}"

    #qsub -v age_group=${age_group},clf_name=$clf_name,cv_outer=${cv_outer},cv_inner=${cv_inner} qsub_batch.sh


    qsub \
        -v age_group=${age_group},clf_name=$clf_name,cv_outer=${cv_outer},cv_inner=${cv_inner} \
        -o $HOME/sge_job_output/1104_pnc/stdout/${age_group}_${clf_name}_${cv_outer}_${cv_inner}.\$JOB_ID.stdout  \
        -e $HOME/sge_job_output/1104_pnc/stderr/${age_group}_${clf_name}_${cv_outer}_${cv_inner}.\$JOB_ID.stderr  \
        qsub_batch.sh

See ``/home/takanori/Dropbox/work/sbia_work/python/analysis/pnc/ncv_conn_random``
for old execution example

********
qsub-run
********
.. code-block:: bash
    
    # create 
    qsub-run -c python script.py arg1 arg2 > out.sh

    # example
    qsub-run -c python save_0726_bct_weighted_normalized.py 0.15 True > qsub_0726.sh


##########################
place exit 1 to end script
##########################
Similar to how i use ``sys.exit()`` in python

.. code-block:: bash

    # ... bunch of script above ...
    exit 1
    # ... bunch of sciprt below ...
###########################
Style-guide and conventions
###########################
Great reference: https://google.github.io/styleguide/shell.xml

- Variable name: http://unix.stackexchange.com/questions/42847/are-there-naming-conventions-for-variables-in-shell-scripts
    
  - **Variable Names**: Lower-case, with underscores to separate words. 
    Ex: ``my_variable_name``
  - **Constants** and **Environment Variable** Names: All caps, separated with 
    underscores, declared at the top of the file. Ex: ``MY_CONSTANT``

- Indentation: http://unix.stackexchange.com/questions/39210/whats-the-standard-for-indentation-in-shell-scripts
- Line-wrap: http://unix.stackexchange.com/questions/39210/whats-the-standard-for-indentation-in-shell-scripts
  
  - apprently none, so stick with one convention
  - my convention: use the 4-space tab

.. code-block:: bash

    # my 4-space convention
    rsync -rvL --ignore-existing --exclude="/*/*/*/" \
        ${source_dir}/${foldername} \
        ${tob_dir}/$[foldername}


    
######
arrays
######
http://mywiki.wooledge.org/BashGuide/Arrays

Remember to **quote** the ``${arrayname[@]}`` expansion properly

.. code-block:: bash

    $ for file in "${myfiles[@]}"; do
    >     cp "$file" /backups/
    > done

Remember these expansion

- ``${arrayname[@]}`` -- xpands to a list of words, with each array element as 
  one word, no matter what it contains. 
  Even if there are spaces, tabs, newlines, quotation marks, or any other kind of characters
- ``${arrayname[*]}`` -- ONLY useful for converting arrays into a single string 
  with all the elements joined together
- ``${#arrayname[@]}`` -- length of array
- ``${!arrayname[@]}`` -- expand list of indices of array

.. code-block:: bash

    # The easiest way to create a simple array with data is by using the =() syntax:
    names=("Bob" "Peter" "$USER" "Big Bad John")

    # ${#array[@]} = length of lists
    echo "There are ${#names[@]} items in the list"
    >>> There are 4 items in the list

    for name in "${names[@]}"; do echo "$name"; done
    >>> Bob
    >>> Peter
    >>> takanori
    >>> Big Bad John

    #  "${arrayname[*]}". 
    # This form is ONLY useful for converting arrays into a single string with all the elements joined together
    echo "Today's contestants are: ${names[*]}"
    >>> Today's contestants are: Bob Peter takanori Big Bad John


    #http://unix.stackexchange.com/questions/136118/convert-all-text-from-uppercase-to-lowercase-and-vice-versa
    #http://stackoverflow.com/questions/689495/upper-to-lower-case-using-sed
    #https://www.gnu.org/software/sed/manual/html_node/The-_0022s_0022-Command.html
    # (note: \U\1 converts first group to uppercase, \L\2 2nd grou pto lower)
    # (/g is for all)
    # (-E for extended regexp, me believes)
    echo "${names[@]}" | sed -E 's/([a-z])|([A-Z])/\U\1\L\2/g'
    >>> bOB pETER TAKANORI bIG bAD jOHN

    echo "${names[@]}" | sed -E 's/([[:lower:]])/\U\1/g'
    >>> BOB PETER TAKANORI BIG BAD JOHN

*****************
Expanding indices
*****************
``${!arrayname[@]}`` expands to a list of the indices of an array, in sequential order. 

.. code-block:: bash

    $ first=(Jessica Sue Peter)
    $ last=(Jones Storm Parker)
    $ for i in "${!first[@]}"; do
    > echo "${first[i]} ${last[i]}"
    > done
    Jessica Jones
    Sue Storm
    Peter Parker

Can also use the **length of array** syntax ``${#names[@]}``

.. code-block:: bash

    $ a=(a b c q w x y z)
    $ for ((i=0; i<${#a[@]}; i+=2)); do
    > echo "${a[i]} and ${a[i+1]}"
    > done

*****************
practical example
*****************


.. code-block:: bash

    target_dir=${HOME}/data/tob/dti_volumes
    source_dir=${HOME}/data/tob/source
    data_array=$(find  ${source_dir} | egrep 'FA\.nii\.gz')
    for i in  $data_array; do 
      # echo -e "Copy ${i} to ${target_dir}"
      # echo -e "cp ${i} ${target_dir}"
      cp ${i} ${target_dir}
    done

Remember to **always avoid using ls**

.. code-block:: bash

    $ files=$(ls)    # BAD, BAD, BAD!
    $ files=($(ls))  # STILL BAD!
    $ files=(*)      # Good!

#############################
control rsync recursive depth
#############################
http://unix.stackexchange.com/questions/178362/rsync-recursively-with-a-certain-depth-of-subfolders

.. code-block:: bash

    #Facilitate the --exclude= option.
    #To sync to a depth of 2 (files within folder and subfolders):
    rsync -r --exclude="/*/*/" source/ target/

########################################
skip scp if file exist (tldr - use rsync
########################################
- http://unix.stackexchange.com/questions/14191/scp-without-replacing-existing-files-in-the-destination
- ``rsync -a --ignore-existing \${source_dir} \${target_dir}``
- whoa, math-mode is working! $\\frac{1}{2}\\beta$


##############
rsync symlinks
##############
- http://superuser.com/questions/799354/rsync-and-symbolic-links

#################################
Appending/concatenating variables
#################################
- http://stackoverflow.com/questions/4181703/how-can-i-concatenate-string-variables-in-bash
- http://unix.stackexchange.com/questions/163898/how-to-assign-a-string-value-to-a-variable-over-multiple-lines-while-indented

.. code-block:: bash

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

.. code-block:: bash

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

.. code-block:: bash

    out_dir="${HOME}/data/tob/dti_volumes"
    echo ${out_dir}
    echo ${out_dir}/subdirec


#######################################################
Create directory if it doesn't exist 06-14-2016 (00:17)
#######################################################
- ``-p`` option does it, but for pedagogical purpose...
- http://stackoverflow.com/questions/4906579/how-to-use-bash-to-create-a-folder-if-it-doesnt-already-exist

.. code-block:: bash

    if [ ! -d /home/mlzboy/b2c2/shared/db ] 
    then
        mkdir -p /home/mlzboy/b2c2/shared/db
    fi

####################
[@] vs [*] in arrays
####################
http://stackoverflow.com/questions/3348443/a-confusion-about-array-versus-array-in-the-context-of-a-bash-comple

.. code-block:: bash

    perls=(perl-one perl-two)

    # equivalence with *
    compgen -W "${perls[*]} /usr/bin/perl" -- ${cur}
    compgen -W "perl-one perl-two /usr/bin/perl" -- ${cur}

    #equivalence with @
    perls=(perl-one perl-two)
    compgen -W "${perls[@]} /usr/bin/perl" -- ${cur}
    compgen -W "perl-one" "perl-two /usr/bin/perl" -- ${cur}


####
1>&2
####
http://stackoverflow.com/questions/818255/in-the-shell-what-does-21-mean

  

  - File descriptor 1 is the standard output (stdout).
  - File descriptor 2 is the standard error (stderr).

  Here is one way to remember this construct (although it is not entirely 
  accurate): at first, 2>1 may look like a good way to redirect stderr to 
  stdout. However, it will actually be interpreted as "redirect stderr to a 
  file named 1". & indicates that what follows is a file descriptor and not a 
  filename. So the construct becomes: ``2>&1``.

#################################
if statements and test conditions
#################################
- Great table here: http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_07_01.html
- http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO-6.html

#########################################
argh...can't comment over line breaks....
#########################################
http://stackoverflow.com/questions/9522631/how-to-put-line-comment-for-a-multi-line-command

.. code-block:: bash

    # meh, can't do this...
    CommandName InputFiles      \ # This is the comment for the 1st line
                --option1 arg1  \ # This is the comment for the 2nd line
                --option2 arg2    # This is the comment for the 3nd line


####################################
get directory of running bash script
####################################
http://stackoverflow.com/questions/59895/can-a-bash-script-tell-what-directory-its-stored-in

.. code-block:: bash

    DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"