bash-commands (``cs-bash-commands``)
""""""""""""""""""""""""""""""""""""
.. rubric :: Some References

- http://ss64.com/bash
- http://www.tldp.org/LDP/abs/html/ (**Advanced Bash-Scripting Guide**)
- http://mywiki.wooledge.org/
- http://wiki.bash-hackers.org/start

.. note:: Greatest one!

    http://www.tutorialspoint.com/unix/index.htm




- ``ctrl+f => ongonig`` for **ongoing** cheat-sheets


.. contents:: `Table of contents`
   :depth: 2
   :local:





#########
Overflows
#########
****************************************************
Should I put my aliases in .bashrc or .bash_aliases?
****************************************************
I wanted to know if there's any reason to define my aliases in ``.bashrc`` or ``.bash_aliases``

.. admonition:: Best Answer

    http://ss64.com/bash/syntax-bashrc.html

        Adding aliases to a separate file called ``.bash_aliases`` has the same affect as putting the aliases in ``.bashrc`` the advantage of .bash_aliases is that having all your aliases in one file makes it easier to re-load them when you make changes.

Below are bunch of links I found along the way.

.. note:: 
    
    I liked the answer in this thread. http://askubuntu.com/questions/121413/understanding-bashrc-and-bash-profile

Other references

- http://unix.stackexchange.com/questions/30925/in-bash-when-to-alias-when-to-script-and-when-to-write-a-function
- http://stackoverflow.com/questions/902946/about-bash-profile-bashrc-and-where-should-alias-be-written-in
- http://askubuntu.com/questions/22037/aliases-not-available-when-using-sudo

************************************
Function in single line (for bashrc)
************************************
- http://askubuntu.com/questions/521937/write-function-in-one-line-into-bashrc

Needed a space between the brackets

.. code-block:: bash

    # needed a space before and after the brackets { whateva; }
    func_name(){ echo "Hello"; }

    # this won't work
    func_name(){echo "Hello";}

************************************************************************
Locale thing (since i'm getting errors in sphinx regarding unicode error
************************************************************************
- https://github.com/sphinx-doc/sphinx/issues/1739
- https://www.google.com/#q=sphinx+encoding+error
- http://masasuzu.hatenablog.jp/entry/20110313/1299997912

.. code-block:: bash

    $ locale
    LANG=en_US.UTF-8
    LANGUAGE=
    LC_CTYPE="en_US.UTF-8"
    LC_NUMERIC="en_US.UTF-8"
    LC_TIME="en_US.UTF-8"
    LC_COLLATE="en_US.UTF-8"
    LC_MONETARY="en_US.UTF-8"
    LC_MESSAGES="en_US.UTF-8"
    LC_PAPER="en_US.UTF-8"
    LC_NAME="en_US.UTF-8"
    LC_ADDRESS="en_US.UTF-8"
    LC_TELEPHONE="en_US.UTF-8"
    LC_MEASUREMENT="en_US.UTF-8"
    LC_IDENTIFICATION="en_US.UTF-8"
    LC_ALL=

In python:

- http://stackoverflow.com/questions/2276200/changing-default-encoding-of-python

.. code-block:: python
    
    # sys.setdefaultencoding() does not exist, here!
    import sys
    reload(sys)  # Reload does the trick!
    sys.setdefaultencoding('UTF8')

::

    In [1]: import sys 

    In [2]: sys.getdefaultencoding()
    Out[2]: 'ascii'     

    In [3]: sys.getfilesystemencoding()
    Out[3]: 'UTF-8'

    In [4]: sys.setdefaultencoding('UTF8')
    ---------------------------------------------------------------------------
    AttributeError                            Traceback (most recent call last)
    <ipython-input-4-daa3932f9332> in <module>()
    ----> 1 sys.setdefaultencoding('UTF8')

    AttributeError: 'module' object has no attribute 'setdefaultencoding'

    In [5]: #  reload does the trick apparently

    In [6]: reload(sys);

    In [7]: sys.setdefaultencoding('UTF8')

    In [8]: sys.getdefaultencoding()
    'UTF8'


*******************
More stuffs with ls
*******************
http://stackoverflow.com/questions/14352290/listing-only-directories-using-ls-in-bash-an-examination

Show only directories: 

.. code-block:: bash

    # using ls only
    takanori@sbia-pc125 ~/anaconda2/lib/python2.7 $ ls -d */
    bsddb/     config/  curses/     email/      hotshot/  importlib/  lib2to3/      lib-tk/   multiprocessing/  pydoc_data/     sqlite3/   wsgiref/
    compiler/  ctypes/  distutils/  encodings/  idlelib/  json/       lib-dynload/  logging/  plat-linux2/      site-packages/  unittest/  xml/

    takanori@sbia-pc125 ~/anaconda2/lib/python2.7 $ ls -ld */ | head -5
    drwxr-xr-x   2 takanori takanori 4.0K Aug 22 11:13 bsddb/
    drwxr-xr-x   2 takanori takanori 4.0K Aug 22 11:13 compiler/
    drwxr-xr-x   2 takanori takanori 4.0K Aug 22 11:13 config/
    drwxr-xr-x   3 takanori takanori 4.0K Aug 22 11:13 ctypes/
    drwxr-xr-x   2 takanori takanori 4.0K Aug 22 11:13 curses/

    # using grep
    takanori@sbia-pc125 ~/anaconda2/lib/python2.7 $ ls -l | grep "^d" | head -5
    drwxr-xr-x   2 takanori takanori 4.0K Aug 22 11:13 bsddb
    drwxr-xr-x   2 takanori takanori 4.0K Aug 22 11:13 compiler
    drwxr-xr-x   2 takanori takanori 4.0K Aug 22 11:13 config
    drwxr-xr-x   3 takanori takanori 4.0K Aug 22 11:13 ctypes
    drwxr-xr-x   2 takanori takanori 4.0K Aug 22 11:13 curses



**********************
Insightful sed example
**********************
http://stackoverflow.com/questions/7209629/extract-string-from-brackets

.. code-block:: bash

    echo "string1 [string2] string3 string4" | sed 's/.*\[\([^]]*\)\].*/\1/g'

Here's a breakdown of the sed command::

    s/          <-- this means it should perform a substitution
    .*          <-- this means match zero or more characters
    \[          <-- this means match a literal [ character
    \(          <-- this starts saving the pattern for later use
    [^]]*       <-- this means match any character that is not a [ character
                    the outer [ and ] signify that this is a character class
                    having the ^ character as the first character in the class means "not"
    \)          <-- this closes the saving of the pattern match for later use
    \]          <-- this means match a literal ] character
    .*          <-- this means match zero or more characters
    /\1         <-- this means replace everything matched with the first saved pattern
                    (the match between "\(" and "\)" )
    /g          <-- this means the substitution is global (all occurrences on the line)

**************************************************
Remove colors from stdout (harder than i expected)
**************************************************
- http://stackoverflow.com/questions/17998978/removing-colors-from-output
- http://unix.stackexchange.com/questions/111899/how-to-strip-color-codes-out-of-stdout-and-pipe-to-file-and-stdout

I expected there to be a unix utility function for this, but i guess not.

Create an alias as below in ``.bashrc``

.. code-block:: bash

    alias stripcolors='sed "s/\x1B\[\([0-9]\{1,2\}\(;[0-9]\{1,2\}\)\?\)\?[mGK]//g"'

Use-case: when I pipe stdout to my clipboard, I don't want the darn color info

.. code-block:: bash

    $ find . -maxdepth 1 | grep .git | xclip -selection clipboard

    # below is what i get when i paste my clipboard on a text-editor
    #>./[01;31m[K.git[m[K
    #>./[01;31m[K.git[m[Kignore

    # so remove the color info prior to clip
    $ find . -maxdepth 1 | grep .git | stripcolors | xclip -selection clipboard
    # awww...much better output from ctrl+v
    ./.git
    ./.gitignore

    #=========================================================================#
    # more usecase
    #=========================================================================#
    # i can pipe grep output to open files
    $ git ls-files | grep copybutton.js | stripcolors | xargs subl

    # open all rst files in new sublime window
    $ subl -n
    $ git ls-files | grep .rst | stripcolors | xargs subl


*****************
SIGINT and SIGSTP
*****************
http://askubuntu.com/questions/510811/what-is-the-difference-between-ctrl-z-and-ctrl-c-in-the-shell

Ha, didn't know the technical term for these ``ctrl+c`` (interrupt) and ``ctrl+z`` (suspend)

*********************************
Quoting with command substitution
*********************************
http://unix.stackexchange.com/questions/118433/quoting-within-command-substitution-in-bash

.. code-block:: bash

    DIRNAME="$(dirname "$FILE")" # the recommended way

**********************
Display function names
**********************
- http://stackoverflow.com/questions/4471364/how-do-i-list-the-functions-defined-in-my-shell

.. note:: ``typeset`` and ``declare`` is synonymous

.. code-block:: bash

    # show all functions (with def)
    typeset -f

    # show just function names
    typeset -F

    # show just function names (but skip first two fields separated by space)
    typeset -F | cut -d ' ' -f 3

    # show specific function
    typeset function_name


*********************************
get n-th line of output (used sed
*********************************
http://stackoverflow.com/questions/1429556/shell-bash-command-to-get-nth-line-of-stdout

.. code-block:: bash

    ls -l | sed -n 2p

    

****************
Quotes with grep
****************
- http://stackoverflow.com/questions/25151067/grep-double-quotes-vs-single-quotes

.. code-block:: bash

    $ echo grep -e show\(  test.txt 
    grep -e show( test.txt

    $ echo grep -e "show\("  test.txt 
    grep -e show\( test.txt

    $ echo grep -e 'show\('  test.txt 
    grep -e show\( test.txt

Reminder on single vs double quotes


- http://stackoverflow.com/questions/3008423/quotes-when-using-grep

.. code-block:: bash

    $ echo "$(date) and 2+2=$((2+2))"
    Tue Aug  5 18:52:39 PDT 2014 and 2+2=4
    $ echo '$(date) and 2+2=$((2+2))'
    $(date) and 2+2=$((2+2))

##################################
Escaping single quotes (a mess...)
##################################
Use ``'"'"'``

http://stackoverflow.com/questions/1250079/how-to-escape-single-quotes-within-single-quoted-strings

####################
Using rename command
####################
- http://unix.stackexchange.com/questions/146743/processing-multiple-extensions
- https://www.gnu.org/software/bash/manual/html_node/Brace-Expansion.html

.. code-block:: bash
    :linenos:

    # rename the filename part "Array" with "_PCA" for all files ending with extension .mat
    rename Array _PCA *.mat

    # rename png "prefix" with "normalized" in files with .png extensions
    rename 's/prefix/normalized/' *.png

    # rename files with either .png or .pkl extension (see link on brack expansion above)
    # (-n will do a dry run, letting me check the rename will do what i want it to do )
    rename -n 's/normalized/test/' *.{png,pkl}

    # creates 3 dir at once
    mkdir {a,b,c}

**********************************
Rename files with suffix or prefix
**********************************
- 2nd answer in http://stackoverflow.com/questions/208181/how-to-rename-with-prefix-suffix

.. code-block:: bash
    :linenos:

    # rename files with extensions (to avoid directory...not robust, but does what i want most of the time)
    for filename in *\.*; do echo $filename; done;
    for filename in *; do echo $filename; done; # <- this includes directory, which me not like


    for filename in *\.*; do mv "${filename}" "prefix_${filename}"; done;


*************************
regexp syntax with rename
*************************
- https://answers.launchpad.net/ubuntu/+question/31247
- http://askubuntu.com/questions/204864/rename-what-does-s-vs-y-mean
- http://manpages.ubuntu.com/manpages/precise/en/man1/sed.1.html

.. code-block:: bash
    :linenos:

    # '-n' option for dry run to verify it'll do what i want it to do
    rename -n 's/graphnet/elasticnet/;' *.m
    >>> graphnet_FA_v06_gender.m renamed as elasticnet_FA_v06_gender.m
    >>> graphnet_FA_v06m_DX.m renamed as elasticnet_FA_v06m_DX.m
    >>> graphnet_FA_v06m_HRp_HRm.m renamed as elasticnet_FA_v06m_HRp_HRm.m
    >>> graphnet_FA_v06m_HRp_LRm.m renamed as elasticnet_FA_v06m_HRp_LRm.m
    >>> graphnet_FA_v06m_risk.m renamed as elasticnet_FA_v06m_risk.m
    >>> graphnet_FA_v12_gender.m renamed as elasticnet_FA_v12_gender.m

    # above looks right, so now actually run it 'verbosely'
    rename -v 's/graphnet/elasticnet/;' *.m

#####################
Random handy snippets
#####################
.. code-block:: bash
    :linenos:

    #=========================================================================#
    # find files with .rst extension at current directory (maxdepth=1)
    # (note: when piping to clipboard, turn grep color off; otherwise you get
    #  character encoding like "ESC[01;31m"
    #  see http://linuxcommando.blogspot.com/2007/10/grep-with-color-output.html
    #=========================================================================#
    # in bash script, don't use ls for globbing (here, it's fine)
    ls | grep \.rst --color=never | c

    # i like this, as things are sorted alphabetically (sed used to replace space with newline, as echo spits everything out in one line
    echo * | sed 's/ /\n/g' | grep \.rst --color=never | c

    # equivalently...(need to sort here)
    find . -maxdepth 1 | sort | grep \.rst --color=never | c


######################################
replace whitespace with newline in sed
######################################
http://stackoverflow.com/questions/1853009/replace-all-whitespace-with-a-line-break-paragraph-mark-to-make-a-word-list

``bash 0622_2016_rename_tobvols.sh | sed 's/ /\n/g'``


*********************************
What if multiple line is spanned?
*********************************
08-05-2016 (12:37)

hmmm...better to leave sed in this case, and use perl?

http://unix.stackexchange.com/questions/26284/how-can-i-use-sed-to-replace-a-multi-line-string

  Summary: Use sed for simple things, and maybe a bit more, but in general, **when it gets beyond working with a single line**, most people prefer something else...

#######################
check running processes
#######################
The one I use the most frequent

.. code-block:: bash
    :linenos:

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

.. code-block:: bash
    :linenos:

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

.. code-block:: bash
    :linenos:

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


.. code-block:: bash
    :linenos:

    # equilvaent to this
    rsync -r -l -p -t -g -o -D

####
find
####
http://ss64.com/bash/find.html

**My Examples**

.. code-block:: bash
    :linenos:

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

.. code-block:: bash
    :linenos:

    List filenames ending in .mp3, searching in the music folder and subfolders: 
    $ find ./music -name "*.mp3"

    Find .doc files that also start with 'questionnaire' (AND) 
    $ find . -name '*.doc' -name questionnaire*    

    Find .doc files that do NOT start with 'Accounts' (NOT)
    $ find . -name '*.doc' ! -name Accounts*        

****************************
Note: **find** vs **locate**
****************************
http://www.thehelloworldprogram.com/linux/locate-find-waldo-bash-shell/

  - Locate searches a pre-written database, making it faster at the sacrifice of accuracy. 
  - Find is more accurate and flexible, but searches in real time, making it slower.    

##########################################
\`\`command\`\` vs $(command) (use latter)
##########################################
- $(commands) does the same thing as backticks, but you can nest them.
- `source <http://stackoverflow.com/questions/2657012/how-to-properly-nest-bash-backticks>`_

Why is $(...) preferred over `...` (backticks)? (http://mywiki.wooledge.org/BashFAQ/082)   

.. code-block:: bash
    :linenos:

    echo $(date +"%Y-%m-%d_%H:%M:%S")


#########
ls tricks
#########

***************************
ls recursively (use *find*)
***************************
http://stackoverflow.com/questions/1767384/ls-command-how-can-i-get-a-recursive-full-path-listing-one-line-per-file

.. code-block:: bash
    :linenos:

    # recursively lists out all files + subdirectories
    find ./test


*******************************************
show only symbolic links (**alias ls_sym**)
*******************************************
Display only files and folders that are symbolic links in tcsh or bash

.. code-block:: bash
    :linenos:

    ls -l $(find ./ -maxdepth 1 -type l -print)

###############
print timestamp
###############
http://stackoverflow.com/questions/17066250/create-timestamp-variable-in-bash-script

.. code-block:: bash
    :linenos:

    echo $(date +"%Y-%m-%d_%H:%M:%S")

################################
open image ($xdg-open image.png)
################################
``xdg-open image.png``

###############################
Options with **less** (ongoing)
###############################
.. code-block:: bash
    :linenos:

    # -n : enable line numbers
    # -N : disable line numbers

########################
history w/o line-numbers
########################
http://stackoverflow.com/questions/7110119/bash-history-without-line-numbers

.. code-block:: bash
    :linenos:

    history | cut -c 8-

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
.. code-block:: bash
    :linenos:

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
.. code-block:: bash
    :linenos:

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

.. code-block:: bash
    :linenos:

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

.. code-block:: bash
    :linenos:

    grep -r "texthere" .

    # You can also mention files to exclude with --exclude.
    grep -r --include "*.txt" texthere .

    # use brace expansion to allow multiple extension
    grep -r --include=*.{py,m} test .

*************************************
To grep a string, pipe output of echo
*************************************
http://superuser.com/questions/748724/pass-a-large-string-to-grep-instead-of-a-file-name


**********************************************************
``\d`` not supported in linux grep as default...seems like
**********************************************************
http://stackoverflow.com/questions/6901171/is-d-not-supported-by-greps-basic-expressions


.. code-block:: bash
    :linenos:

    # these will do
    grep '[0-9]'
    grep '[[:digit:]]'
    grep -P '\d'

**************************************
just use double-quotes for regex query
**************************************
http://askubuntu.com/questions/432064/using-grep-to-search-texts-with-single-quote

.. code-block:: bash
    :linenos:
     
    # to find 'type' => 'select'
    grep  "'type' => 'select'" file 


#############################################
Selecting n-th line or word using sed and awk
#############################################
- http://stackoverflow.com/questions/2440414/how-to-retrieve-the-first-word-of-the-output-of-a-command-in-bash
- 

Remarks

- remember, don't pipe using ls

  - http://mywiki.wooledge.org/ParsingLs <= don't use ``ls`` when a glob would do
- http://ss64.com/bash/awk.html

.. code-block:: bash
    :linenos:

    # select 2nd item (find will spit out line-by-line output)
    itksnap -g $(find ./ | sed -n 2p) &


    # probably the preferred method (according to above link, ``$ find . `` is just as bad. use glob
    # (here, select the 3rd item separated by white space)
    echo * | awk '{print $3}'
    itksnap -g $(echo * | awk '{print $3}') &
    echo * | awk '{print $3}' | xargs itksnap -g &


###########################################################
Use xargs to execute a command once per line of piped input
###########################################################
http://unix.stackexchange.com/questions/7558/execute-a-command-once-per-line-of-piped-input

.. code-block:: bash
    :linenos:

    # below is not practical, but gives a good idea of how xargs work
    find -maxdepth 1 | egrep '0627' | xargs -n1 echo

##########################################
Run same command multiple times (for loop)
##########################################
http://stackoverflow.com/questions/3737740/is-there-a-better-way-to-run-a-command-n-times-in-bash

.. code-block:: bash
    :linenos:

    for run in {1..10}
    do
      command
    done

    # single line
    for run in {1..30}; do ipython t_0809c_enet_tobpnc_age.py; done

####################
clipboard with xclip
####################
http://stackoverflow.com/questions/5130968/how-can-i-copy-the-output-of-a-command-directly-into-my-clipboard

.. code-block:: bash
    :linenos:


    # Only copy the content to the X clipboard
    sphinx-quickstart --help | xclip 
    
    xclip -o # output prints

    # to paste somewhere other than xapplication, 
    sphinx-quickstart --help | xclip -selection clipboard

    # Above is cumbersome to type....so i created function cb() in .bashrc
    # http://madebynathan.com/2011/10/04/a-nicer-way-to-use-xclip/
    sphinx-quickstart --help | cb

    # i also created these
    alias c="xclip -selection clipboard" 
    alias v="xclip -o -selection clipboard"

    sphinx-quickstart --help | c

##############
IO Redirection
##############
http://www.tutorialspoint.com/unix/unix-io-redirections.htm

******************************
Piping vs command substitution
******************************
- http://unix.stackexchange.com/questions/17107/process-substitution-and-pipe

One example: with ``<``, program doesn't know the filename (only interprets as an input stream)


.. code-block:: bash

    # (from http://www.tutorialspoint.com/unix/unix-io-redirections.htm)
    # here filename outputted too
    $ wc -l users
    2 users

    # here filename not recognized
    $ wc -l < users
    2
    
*********************
redirecting vs piping
*********************
- http://askubuntu.com/questions/172982/what-is-the-difference-between-redirection-and-pipe
- http://stackoverflow.com/questions/9553628/piping-and-redirection


- Redirect passes output to file/stream
- Pipe passes output to another program/utility

************************************************
Output stdout and stderr to terminal and logfile
************************************************
- http://stackoverflow.com/questions/418896/how-to-redirect-output-to-a-file-and-stdout
- http://stackoverflow.com/questions/18460186/writing-outputs-to-log-file-and-console

.. code-block:: bash

    # save stdout and stderr to a file
    bash mymake.sh >> log.txt 2>&1

    # save logfile like above, but also print on terminal screen http://stackoverflow.com/questions/418896/how-to-redirect-output-to-a-file-and-stdout
    bash mymake.sh 2>&1 | tee log.txt

****************
syntax reference
****************
- http://www.tldp.org/LDP/abs/html/io-redirection.html


.. code-block:: bash

    # Single-line redirection commands (affect only the line they are on):
    # --------------------------------------------------------------------
    1>filename
       # Redirect stdout to file "filename."
    1>>filename
       # Redirect and append stdout to file "filename."
    2>filename
       # Redirect stderr to file "filename."
    2>>filename
       # Redirect and append stderr to file "filename."
    &>filename
       # Redirect both stdout and stderr to file "filename."
       # This operator is now functional, as of Bash 4, final release.
    2>&1
       # Redirects stderr to stdout.
       # Error messages get sent to same place as standard output.
    i>&j
       # Redirects file descriptor i to j.
       # All output of file pointed to by i gets sent to file pointed to by j.
    >&j
       # Redirects, by default, file descriptor 1 (stdout) to j.
       # All stdout gets sent to file pointed to by j.
    |
       # Pipe.
       # General purpose process and command chaining tool.
       # Similar to ">", but more general in effect.
       # Useful for chaining commands, scripts, files, and programs together.
       cat *.txt | sort | uniq > result-file
       # Sorts the output of all the .txt files and deletes duplicate lines,
       # finally saves results to "result-file".


.. code-block:: bash

    COMMAND_OUTPUT >
       # Redirect stdout to a file.
       # Creates the file if not present, otherwise overwrites it.

    : > filename
       # The > truncates file "filename" to zero length.
       # If file not present, creates zero-length file (same effect as 'touch').
       # The : serves as a dummy placeholder, producing no output.

    > filename    
       # The > truncates file "filename" to zero length.
       # If file not present, creates zero-length file (same effect as 'touch').
       # (Same result as ": >", above, but this does not work with some shells.)

    COMMAND_OUTPUT >>
       # Redirect stdout to a file.
       # Creates the file if not present, otherwise appends to it.

    M>N
      # "M" is a file descriptor, which defaults to 1, if not explicitly set.
      # "N" is a filename.
      # File descriptor "M" is redirect to file "N."
    M>&N
      # "M" is a file descriptor, which defaults to 1, if not set.
      # "N" is another file descriptor.
      0< FILENAME
       < FILENAME
         # Accept input from a file.
         # Companion command to ">", and often used in combination with it.
         #
         # grep search-word <filename

      [j]<>filename
         #  Open file "filename" for reading and writing,
         #+ and assign file descriptor "j" to it.
         #  If "filename" does not exist, create it.
         #  If file descriptor "j" is not specified, default to fd 0, stdin.
         #
         #  An application of this is writing at a specified place in a file. 
         echo 1234567890 > File    # Write string to "File".
         exec 3<> File             # Open "File" and assign fd 3 to it.
         read -n 4 <&3             # Read only 4 characters.
         echo -n . >&3             # Write a decimal point there.
         exec 3>&-                 # Close fd 3.
         cat File                  # ==> 1234.67890
         #  Random access, by golly.



#############
Bit on printf
#############
- http://ss64.com/bash/printf.html
- http://unix.stackexchange.com/questions/65803/why-is-printf-better-than-echo
  
  - "Basically, it's a portability (and reliability) issue."

.. code-block:: bash

    $ var1="hello   world\n"

    # no quotes
    $ printf %s $var1
    helloworld\n$ 

    # double quotes
    $ printf "%s" $var1
    helloworld\n

    # single quotes get substituted too
    $ printf '%s' $var1
    helloworld\n

    $ printf [%s] $var1
    [hello][world\n]

    $ printf "[%s]" $var1
    [hello][world\n]

    $ printf '[%s]' $var1
    [hello][world\n]

    # here the white-spaces are respected (double-quoted var1)
    $ printf "[%s]" "$var1"
    [hello   world\n]


******************
Examples from ss64
******************
.. code-block:: bash

    $ for ((num=1;num<=5;num+=1)); do echo $(printf "%03d" $num); done
    001
    002
    003
    004
    005

    $ distance=15
    $ printf "Distance is %5d Miles\n" $distance   
    Distance is    15 Miles

    # default precision for float: 6 decimal places
    $ printf "%f\n" 5
    5.000000
    $ printf "%.2f\n" 5
    5.00
    $ printf "%5.2f\n" 5
     5.00


    $ printf "Hello, $USER.\n\n"
    Hello, takanori.

    $ printf "There are %d orders of cheese burgers. cost at \$%.2f.\n" 5 15.32
    There are 5 orders of cheese burgers. cost at $15.32.

    # with command substitution
    $ printf "This is $(uname -s) running on a $(uname -m) processor.\n"
    This is Linux running on a x86_64 processor.




########
for loop
########

******
basics
******
- http://tldp.org/LDP/abs/html/loops1.html
- http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO-7.html
- http://stackoverflow.com/questions/49110/how-do-i-write-a-for-loop-in-bash

.. code-block:: bash


    # Classic for loop
    for word in ...; do ...; done

    # C-style for loop
    for ((x=1; x<=10; x++)); do ...; done

    # classic for loop - multiline
    for w in word1 word2 word3
    do
      doSomething($w)
    done

    # to iterate over all directories in some path, for example:
    for d in $(find $somepath -type d)
    do
      doSomething($d)
    done

    # recall arithmetic expansion in bash needs double parantheis 
    # http://tldp.org/LDP/abs/html/arithexp.html
    # http://wiki.bash-hackers.org/syntax/ccmd/c_for
    # (C-style for loop)
    for ((i = 0 ; i < 5 ; i++ )); do echo "$i"; done

    # C-style for loop with step size
    $ for ((x = 0 ; x <= 100 ; x += 10)); do
    >   echo "Counter: $x"
    > done
    Counter: 0
    Counter: 10
    Counter: 20
    Counter: 30
    Counter: 40
    Counter: 50
    Counter: 60
    Counter: 70
    Counter: 80
    Counter: 90
    Counter: 100

    # $((EXPRESSION)) is arithmetic expansion.  
    #  Not to be confused with command substitusion

    # avoids spawning external program `seq`
    $ for i in {1..5} ; do printf "%d " "$i" ; done
    1 2 3 4 5

    # command substitute on `seq`
    $ for i in $(seq 1 5) ; do printf "%d " "$i" ; done
    1 2 3 4 5

    for i in $(seq 1 5);
    do
            echo $i
    done
    > 1
    > 2
    > 3
    > 4
    > 5

    # while loop
    COUNTER=0
    while [  $COUNTER -lt 10 ]; do
        echo The counter is $COUNTER
        let COUNTER=COUNTER+1 
    done

*********************
multiline in terminal
*********************
.. code-block:: bash

    # i can literally type like this w/o using backslash \ to linewrap
    $ for x in 1 2 3; 
    > do
    > echo $x
    > done

***************************
Looping over array elements
***************************
keep in mind the distinction between ``"${arrayname[*]}"`` (i rarely use this...) vs ``"${arrayname[@]}`` (i use this a lot via for loops)

- http://mywiki.wooledge.org/BashGuide/Arrays
- http://mywiki.wooledge.org/BashGuide/Parameters
- http://www.tutorialspoint.com/unix/unix-special-variables.htm

- ``"$*"`` = takes the entire list as one argument with spaces between

  - this form is **ONLY** useful for converting arrays into a single string (`link <http://mywiki.wooledge.org/BashGuide/Arrays>`_)
- ``"$@"`` = takes the entire list and separates it into **separate arguments** (Double quoted, it expands to a list of them all as individual words)

.. code-block:: bash

    # "$*" syntax: converts array to single thing
    $ names=("Bob" "Peter" "$USER" "Big Bad John")
    $ echo "${names[*]}"
    Bob Peter takanori Big Bad John
    $ b="${names[*]}"
    $ echo $b
    Bob Peter takanori Big Bad John

    # with $@, each item is treated as *separate arguments*
    # (think of [@] as a special kind of positional argument)
    $ for name in "${names[@]}"; do echo "${name}"; done
    Bob
    Peter
    takanori
    Big Bad John

    # so yeah, "$*" doesn't give what i want
    $ for name in "${names[*]}"; do echo "${name}"; done
    Bob Peter takanori Big Bad John

*****************************************************
number of elements in an array using ``${#array[@]}``
*****************************************************
.. code-block:: bash

    $ array=(a b c)
    $ echo ${#array[@]}
    3


**********************************
avoid $(ls)...use globbing or find
**********************************
see http://mywiki.wooledge.org/BashGuide/Arrays

.. code-block:: bash

    #=========================================================================#
    # don't use $(ls) to get items (woolmore)
    #=========================================================================#
    $ ls
    books.txt  commands  quote.txt  sed-tutorial.gnu.rst  sed-tutorial.tutorialspoints.rst

    for i in *; do
        echo item: $i
    done

    $ for i in *; do echo item: $i; done
    item: books.txt
    item: commands
    item: quote.txt
    item: sed-tutorial.gnu.rst
    item: sed-tutorial.tutorialspoints.rst

    # globs only looks at current dir-level
    $ for i in *; do echo item: $i; done
    item: awk-tutorial
    item: sed

    # to recurse over directories, use ``find``
    $ for i in $(find .); do echo item: $i; done
    item: .
    item: ./awk-tutorial
    item: ./awk-tutorial/awk-basic-structure.rst
    item: ./awk-tutorial/awk-builtin-vars.rst
    item: ./awk-tutorial/awk-summary-commands.rst
    item: ./awk-tutorial/awk-essential-syntax.rst
    item: ./awk-tutorial/index.rst
    item: ./sed
    item: ./sed/quote.txt
    item: ./sed/books.txt
    item: ./sed/commands
    item: ./sed/sed-tutorial.tutorialspoints.rst
    item: ./sed/sed-tutorial.gnu.rst

###########################
arithmetic expansion ((..))
###########################
- http://wiki.bash-hackers.org/syntax/arith_expr


************
let vs (())?
************
- http://stackoverflow.com/questions/18704857/bash-let-statement-vs-assignment

::
    
    http://wiki.bash-hackers.org/commands/builtin/let#examples
    There is almost no difference between let and (( )).


.. code-block:: bash

    # let version
    $ let 'b = a' "(a += 3) + $((a = 1)), b++"
    $ echo "$a - $b - $?"
    4 - 2 - 0

    # equivalent (()) version 
    $ (( b = a, (a += 3) + $((a = 1)), b++ ))
    $ echo "$a - $b - $?"
    4 - 2 - 0
