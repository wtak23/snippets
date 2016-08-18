awk
"""
.. contents:: **Contents (current page)**
    :depth: 2


For a quick **table** type reference: http://www.grymoire.com/Unix/AwkRef.html    
    
###########################
note: do I really need awk?
###########################
.. note::

    tl;dr --- I probably don't need its programming functionality, but just know some of the handy **one-liners** i can use in the commandline

- when things get complicated, I use ``perl`` or ``python``, which I use on a more regular basis (hence it sticks with me...awk i don't use it often enough)
- basically, I rarely find the rare niche right between not needing it at all and needing to whip out Perl/Python (ie, spectrum between tr/cut/sed to python/perl)
- see the answers I hilited in this SO thread: http://stackoverflow.com/questions/107603/is-there-still-any-reason-to-learn-awk

I tend to agree with this comment:

  I wouldn't advise you spend a whole lot of time on it, but it might come in handy to know the basics of the syntax -- at least enough that you can consult the manual quickly should you ever want to use it.

**Conclusion**: I'd like to learn more about it, but I have ton of other things I need to learn.

#########################################################
My use-case for awk (for files containing columns/fields)
#########################################################
http://stackoverflow.com/questions/107603/is-there-still-any-reason-to-learn-awk

.. code-block:: bash

    #=========================================================================#
    # For dealing with multicolumn files
    #=========================================================================#
    # I think awk is great if your file contains columns/fields. 
    # Example: below will print only if the 2nd column value in a tab seperated 
    # file is greater than the 3rd column value.
    awk -F \t '{ if ($2 > $3) print; }' <filename>

    #=========================================================================#
    # For auto-splitting
    #=========================================================================#
    # The only reason I use awk is the auto-splitting.
    # This prints the third whitespace-delimited field in file.in
    awk '{print $3}' < file.in

    # above is arguably easier than
    tr -s ' ' < file.in | cut -d' ' -f3


###############
Random snippets
###############
.. code-block:: bash

    $ ls -l
    total 68K
    drwxr-xr-x  4 takanori takanori 4.0K Aug 17 23:41 build
    drwxr-xr-x 13 takanori takanori 4.0K Aug 17 22:18 build_published
    drwxr-xr-x  8 takanori takanori 4.0K Aug 17 23:31 source
    -rw-r--r--  1 takanori takanori 7.5K Aug  5 13:45 Makefile
    -rw-r--r--  1 takanori takanori  666 Aug 17 22:05 mymake.sh
    -rw-rw-rw-  1 takanori takanori  343 Aug 12 12:38 publish.sh
    -rw-r--r--  1 takanori takanori  651 Aug  5 14:37 readme.rst
    -rw-r--r--  1 takanori takanori  487 Jun 14 19:24 sed-text.txt

    # pull out the 5th and 9th field (file-size and file-name)
    $ ls -l | awk '{printf $5 "\t" $9"\n"}'

    4.0K    build
    4.0K    build_published
    4.0K    source
    7.5K    Makefile
    666 mymake.sh
    343 publish.sh
    651 readme.rst
    487 sed-text.txt

################
awk (one-liners)
################
- http://stackoverflow.com/questions/2021982/awk-without-printing-newline
- http://askubuntu.com/questions/231995/how-to-separate-fields-with-space-or-tab-in-awk
- http://www.catonmat.net/blog/awk-one-liners-explained-part-one/
- http://www.staff.science.uu.nl/~oostr102/docs/nawk/nawk_41.html

********************
Great examples here!
********************
- http://tuxgraphics.org/~guido/scripts/awk-one-liner.html

##########
awk --help
##########
.. code-block:: none

    Usage: awk [POSIX or GNU style options] -f progfile [--] file ...
    Usage: awk [POSIX or GNU style options] [--] 'program' file ...
    POSIX options:      GNU long options: (standard)
        -f progfile     --file=progfile
        -F fs           --field-separator=fs
        -v var=val      --assign=var=val
    Short options:      GNU long options: (extensions)
        -b          --characters-as-bytes
        -c          --traditional
        -C          --copyright
        -d[file]        --dump-variables[=file]
        -e 'program-text'   --source='program-text'
        -E file         --exec=file
        -g          --gen-pot
        -h          --help
        -L [fatal]      --lint[=fatal]
        -n          --non-decimal-data
        -N          --use-lc-numeric
        -O          --optimize
        -p[file]        --profile[=file]
        -P          --posix
        -r          --re-interval
        -S          --sandbox
        -t          --lint-old
        -V          --version

    To report bugs, see node `Bugs' in `gawk.info', which is
    section `Reporting Problems and Bugs' in the printed version.

    gawk is a pattern scanning and processing language.
    By default it reads standard input and writes standard output.

    Examples:
        gawk '{ sum += $1 }; END { print sum }' file
        gawk -F: '{ print $1 }' /etc/passwd
