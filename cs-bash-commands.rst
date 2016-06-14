http://ss64.com/bash

Here keep list of \*one-liner\* bash commands.


`[Parent Directory] <./>`_

.. contents:: **Table of Contents**
    :depth: 2

.. sectnum::    
    :start: 1    

####################
Moving and copying
####################
- http://ss64.com/bash/cp.html
- http://ss64.com/bash/mv.html

.. code:: bash

    # rename a directory (note '/' after directory name has NO impact here,  there are cases I should be careful of the backslash)
    mv /home/user/oldname /home/user/newname

    #=== cp helper ===#
    # copy files *inside* the folder "test/" inside folder "target" 
    gosnippets; cd tests; mkdir source target; cd source; touch a b c; cd ..

    # copy files *inside* the folder "test/" inside folder "target" (note: -R and -r are the same here)
    cp -r source/* target

    # copy entire folder *source* into *target* (without ``-r``, the subdirectories won't get copied) 
    cp -r source* target

    #--- cleanup test files from above---#
    cd ..; rm -r tests/* 

********************
scp user
********************
- http://ss64.com/bash/scp.html

Warning: scp apparently overwrites existing file w/o warning. Hence ``rsync`` is a safer option.

.. code:: bash

    #========================================================================#
    # relevant options
    #========================================================================#
    -r : recursive
    -v : verbose (i probably won't need)
    -q : quiet

    #========================================================================#
    # demos
    #========================================================================#
    # Copy dummy.txt to home directory in remote host:
    touch ~/dummy.txt
    scp ~/dummy.txt watanabt@cbica-cluster.uphs.upenn.edu:~/

    # copy dummy.txt on server as dummy_cp.txt to local home folder
    scp watanabt@cbica-cluster.uphs.upenn.edu:~/dummy.txt ~/dummy_cp.txt

###############################################################################
find
###############################################################################
http://ss64.com/bash/find.html

**My Examples**

.. code:: sh

    find $DIR # recursively print out file directories
    find $PWD | grep helper.md
    find $PWD | grep helper.html | xclip
    find $PWD -maxdpeth 1 
    find . -iname "*chrome*" # case insensitive
    find . -name "*chrome*" # case sensitive
    find . -iname "*chrome*" # print filenames, followed by a NULL character instead of the "newline" chracter that -print uses

    # ignore any file containing "est" (even in the directory name) and print out rest
    # (note: -o is the OR operator...see "operator" list below)
    find . -wholename '*est*' -prune -o -print

    # stuffs with -type option
    find . d # list directories
    find . f # list regular files    
    find . l # list symlinks

    #=====================================================================#
    # name vs. whilename
    # - suppose i have file /Data_Science/test.txt
    #=====================================================================#
    find . -iwholename "*Sci*.txt"
        # this will find the above file
    find . -iname "*Sci*.txt"
        # this will NOT find the above file

**Selected examples from ss64**

.. code:: bash

    List filenames ending in .mp3, searching in the music folder and subfolders: 
    $ find ./music -name "*.mp3"

    Find .doc files that also start with 'questionnaire' (AND) 
    $ find . -name '*.doc' -name questionnaire*    

    Find .doc files that do NOT start with 'Accounts' (NOT)
    $ find . -name '*.doc' ! -name Accounts*        

********************
Note: **find** vs **locate**
********************
http://www.thehelloworldprogram.com/linux/locate-find-waldo-bash-shell/

  - Locate searches a pre-written database, making it faster at the sacrifice of accuracy. 
  - Find is more accurate and flexible, but searches in real time, making it slower.    

###############################################################################
\`\`command\`\` vs $(command) (use latter)
###############################################################################
- $(commands) does the same thing as backticks, but you can nest them.
- `source <http://stackoverflow.com/questions/2657012/how-to-properly-nest-bash-backticks>`_

.. code:: bash

    echo $(date +"%Y-%m-%d_%H:%M:%S")

###############################################################################
print timestamp
###############################################################################
.. code:: bash

    echo $(date +"%Y-%m-%d_%H:%M:%S")