http://ss64.com/bash

- Here keep list of \*one-liner\* bash commands.
- ``ctrl+f => ongonig`` for **ongoing** cheat-sheets


`[Parent Directory] <./>`_

.. contents:: **Table of Contents**
    :depth: 2

.. sectnum::    
    :start: 1    


######################################
replace whitespace with newline in sed
######################################
http://stackoverflow.com/questions/1853009/replace-all-whitespace-with-a-line-break-paragraph-mark-to-make-a-word-list

``bash 0622_2016_rename_tobvols.sh | sed 's/ /\n/g'``

#######################
check running processes
#######################
The one I use the most frequent

.. code:: bash

    # a <- includes ``root`` in userprocess
    # u <- include ``username`` column
    # x <- list all processes owned by me
    ps aux

####################
nohup vs disown vs &
####################
- Cuz i got annoyed on accidentally closing terminal running ``spyder &``
- http://unix.stackexchange.com/questions/4004/how-can-i-close-a-terminal-without-killing-the-command-running-in-it
- http://unix.stackexchange.com/questions/3886/difference-between-nohup-disown-and

##################
Moving and copying
##################
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


    #--- remove entire directory including files inside recursively ---#
    rm -rf test/


********
scp user
********
- http://ss64.com/bash/scp.html

Warning: scp apparently overwrites existing file w/o warning. Hence ``rsync`` is a safer option.

.. code:: bash

    #========================================================================#
    # relevant options
    #========================================================================#
    #| -r : recursive
    #| -v : verbose (i probably won't need)
    #| -q : quiet

    #========================================================================#
    # demos
    #========================================================================#
    # Copy dummy.txt to home directory in remote host:
    touch ~/dummy.txt
    scp ~/dummy.txt watanabt@cbica-cluster.uphs.upenn.edu:~/

    # copy dummy.txt on server as dummy_cp.txt to local home folder
    scp watanabt@cbica-cluster.uphs.upenn.edu:~/dummy.txt ~/dummy_cp.txt


*****
rsync
*****
http://ss64.com/bash/rsync.html


What ``-a`` does
================
http://serverfault.com/questions/141773/what-is-archive-mode-in-rsync


::
    #========================================================================#
    # it exludes these
    #========================================================================#
    -H, --hard-links preserve hard links
    -A, --acls preserve ACLs (implies -p)
    -X, --xattrs preserve extended attributes

    #========================================================================#
    # does all of these
    #========================================================================#
    -r, --recursive recurse into directories
    -l, --links copy symlinks as symlinks
    -p, --perms preserve permissions
    -t, --times preserve modification times
    -g, --group preserve group
    -o, --owner preserve owner (super-user only)
    -D same as --devices --specials

    --devices preserve device files (super-user only)
    --specials preserve special files


.. code:: bash

    # equilvaent to this
    rsync -r -l -p -t -g -o -D

####
find
####
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

##########################################
\`\`command\`\` vs $(command) (use latter)
##########################################
- $(commands) does the same thing as backticks, but you can nest them.
- `source <http://stackoverflow.com/questions/2657012/how-to-properly-nest-bash-backticks>`_

Why is $(...) preferred over `...` (backticks)? (`link <http://mywiki.wooledge.org/BashFAQ/082>`_)   

.. code:: bash

    echo $(date +"%Y-%m-%d_%H:%M:%S")


#########
ls tricks
#########

********************
ls recursively (use *find*)
********************
http://stackoverflow.com/questions/1767384/ls-command-how-can-i-get-a-recursive-full-path-listing-one-line-per-file

.. code:: bash

    # recursively lists out all files + subdirectories
    find ./test


******************************************
show only symbolic links (**alias lssym**)
******************************************
http://stackoverflow.com/questions/7110119/bash-history-without-line-numbers

.. code:: bash

    ls -l $(find ./ -maxdepth 1 -type l -print)

###############
print timestamp
###############
http://stackoverflow.com/questions/17066250/create-timestamp-variable-in-bash-script

.. code:: bash

    echo $(date +"%Y-%m-%d_%H:%M:%S")

################################
open image ($xdg-open image.png)
################################
``xdg-open image.png``

###############################
Options with **less** (ongoing)
###############################
.. code:: bash

    # -n : enable line numbers
    # -N : disable line numbers

########################
history w/o line-numbers
########################
http://stackoverflow.com/questions/7110119/bash-history-without-line-numbers

.. code:: bash

    history | cut -c 8-

################
awk (one-liners)
################
- http://stackoverflow.com/questions/2021982/awk-without-printing-newline
- http://askubuntu.com/questions/231995/how-to-separate-fields-with-space-or-tab-in-awk
- http://www.catonmat.net/blog/awk-one-liners-explained-part-one/
- http://www.staff.science.uu.nl/~oostr102/docs/nawk/nawk_41.html


.. code:: bash

    ls -l | awk '{printf $5 "\t" $9"\n"}'

**oneliner examples**

- http://tuxgraphics.org/~guido/scripts/awk-one-liner.html

####################
When xargs is needed
####################
Some bash program can't be piped since piping requires the program to accept STDIN commands
(example, ``touch``)

http://unix.stackexchange.com/questions/24954/when-is-xargs-needed

    The difference is in what data the target program is accepting.
    
    If you just use a pipe, it receives data on STDIN (the standard input stream) as a raw pile of data that it can sort through one line at a time. However some programs don't accept their commands on standard in, they expect it to be spelled out in the arguments to the command. For example touch takes a file name as a parameter on the command line like so: touch file1.txt.
    
    If you have a program that outputs filenames on standard out and want to use them as arguments to touch, you have to use xargs which reads the STDIN stream data and converts each line into space separated arguments to the command.


#################
Get computer info
#################
.. code:: bash

    # get cpu information
    cat /proc/cpuinfo

    #-- see gnome version ---
    gnome-shell --version
    lsb_release -a

    # to figure out which linux distribution you are using
    # (ref: http://www.cyberciti.biz/faq/find-linux-distribution-name-version-number/)
    cat /etc/*-release

    locate libfortran.so

#######
mogrify
#######
.. code:: bash

    mogrify -resize 50% *.png
    mogrify -resize 500! *.png     => changes only x-axis
    mogrify -resize 500 *.png      => changes (x,y) axis in proportion
    mogrify -trim *.png

    #| http://arcoleo.org/dsawiki/Wiki.jsp?page=Recursively%20run%20Mogrify%20on%20a%20Directory
    #| Mogrify is an image tool that comes with ImageMagick. It is useful for resizing, compressing, etc. If you have a set of subdirectories to run it on, run
    $ find ./ -name "*.png" -exec mogrify -some_option {} \;
    $ find ./ -name "*.png" -exec mogrify -resize 40% {} \;


##################################
Pipe dreams (xargs, -exec in find)
##################################
http://unix.stackexchange.com/questions/41740/find-exec-vs-find-xargs-which-one-to-choose

- the ``-exec "{}" \;`` approach seems to be specific to ``find``
  (i prefer unity with ``xargs``)

.. code:: bash

    #http://stackoverflow.com/questions/4509624/how-to-limit-depth-for-recursive-file-list    
    # http://ss64.com/bash/find.html
    find . -maxdepth 1 -type d -exec ls -ld "{}" ";"
    find . -maxdepth 1 -type d -exec ls -ld \{\} \;  # same as above
    find . -maxdepth 1 -type d | xargs ls -ld # same as above (i find this the most intuitive)
    ls -ld $(find . -maxdepth 1 -type d) # same as above
    
    # this doesn't give the same result as "xargs" approach...figure out why later
    find . -maxdepth 1 -type d | ls -ld 

####
Grep
####

****************
grep recursively
****************
http://stackoverflow.com/questions/1987926/how-do-i-grep-recursively

.. code:: bash

    grep -r "texthere" .

    # You can also mention files to exclude with --exclude.
    grep -r --include "*.txt" texthere .

*************************************
To grep a string, pipe output of echo
*************************************
http://superuser.com/questions/748724/pass-a-large-string-to-grep-instead-of-a-file-name