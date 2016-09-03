sed (``cs-sed.rst``)
""""""""""""""""""""

.. contents:: `Table of contents`
   :depth: 2
   :local:
   
.. note:: mantra for ``sed``: "When in doubt, experiment."

##########
References
##########

This one is awesome! http://www.grymoire.com/Unix/SedChart.pdf

***********************************
Go to GNU manual for an overkill :)
***********************************
- https://www.gnu.org/software/sed/manual/html_node/index.html (gnu manual)
- https://www.gnu.org/software/sed/manual/sed.html (above as single printable html file)

**The only two pages I need from above**

- `ch3 sed Programs <https://www.gnu.org/software/sed/manual/html_node/sed-Programs.html#sed-Programs>`_
- `Examples <https://www.gnu.org/software/sed/manual/html_node/Examples.html#Examples>`_

******
Others
******
- http://ss64.com/bash/sed.html
- http://www.tutorialspoint.com/sed/index.htm
- http://www.grymoire.com/Unix/Sed.html



###############
Random snippets
###############
.. code-block:: bash
    :linenos:

    echo $PYTHONPATH 
    /home/takanori/Dropbox/work/external-pymodules:/home/takanori/Dropbox/work/sbia_work/python/modules:/home/takanori/work-local/external-python-modules/deepnet:/home/takanori/mybin/spark-2.0.0-bin-hadoop2.7/python/pyspark

    # recall, g for global replacement
    echo $PYTHONPATH | sed 's/:/\n/g'
    /home/takanori/Dropbox/work/external-pymodules
    /home/takanori/Dropbox/work/sbia_work/python/modules
    /home/takanori/work-local/external-python-modules/deepnet
    /home/takanori/mybin/spark-2.0.0-bin-hadoop2.7/python/pyspark

******************
Insightful example
******************
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

**********
fixname.sh
**********
.. code-block:: bash

    #=========================================================================#
    # Repalce string "_static" with "static"
    # Repalce string "_sources" with "sources"
    # Repalce string "_images" with "images"
    #=========================================================================#
    #http://stackoverflow.com/questions/14505047/bash-loop-through-all-the-files-with-a-specific-extension
    build_dir='./_build/html'
    for file in "${build_dir}/*.html"; do
        #echo $file
        sed -i 's/_static\//static\//' $file
        sed -i 's/_sources\//sources\//' $file
        sed -i 's/_modules\//sources\//' $file
        #sed -i 's/_images\//images\//' $file
    done

    # rename directories with underscore
    #mv ${build_dir}/_images ${build_dir}/images
    mv ${build_dir}/_modules ${build_dir}/modules
    mv ${build_dir}/_sources ${build_dir}/sources
    mv ${build_dir}/_static ${build_dir}/static


############
Ultra-basics
############

***************************************
Basics: print, delete, and substitution
***************************************
.. code-block:: bash

    # basic syntax: 
    /regexp/action

    p = prints the line
    d = deletes the line
    s/REGEXP/REPLACEMENT/FLAGS #<= substitues regexp with pattern

*****************
deletion commands
*****************

.. code-block:: bash
    :linenos:

    # deletes all lines
    sed 'd' sed-text.txt

    # delete first line
    sed '1d' sed-text.txt

    # delete 2nd line
    sed '1d' sed-text.txt

    # delete lines 2-3
    sed '2,3d' sed-text.txt

*******************
Substitution basics
*******************
syntax for ``s/STRING_TO_CATPURE/REPLACEMENT/SUBS_FLAGS``

.. code-block:: bash

    # replace *the* with THE in line 3
    sed '3s/[Tt]he/THE/g' sed-text.txt  

    # replace *the* with THE in line3-6
    sed '3,6s/[Tt]he/THE/g' sed-text.txt 

**Substitution Flags** (from http://ss64.com/bash/sed.html)

.. csv-table:: 
    :header: Flag, Description
    :widths: 22,70
    :delim: | 

    g |   Replace all matches, not just the first match.
    NUMBER |  Replace only NUMBERth match.
    p |   If substitution was made, print pattern space.
    w FILENAME  | If substitution was made, write result to FILENAME.
    I or i | Match in a case-insensitive manner.
    M  or m | In addition to the normal behavior of the special regular expression characters ^ and \\$, this flag causes ^ to match the empty string after a newline and \\$ to match the empty string before a newline.

**Range flags**

.. csv-table:: Range options
    :header: Range, Description
    :widths: 10,70
    :delim: |

   
    '4,10d' | Lines starting from 4th till 10th are deleted
    '10,4d' | Only 10th line is deleted, because sed does not work in reverse direction.
    '4,+5d' | This will match line 4 in the file, delete that line, continue to delete the next five lines, and then cease its deletion and print the rest
    '2,5!d' | This will deleted everything except starting from 2nd till 5th line.
    '1~3d'  |  deletes the first line, steps over the next three lines, and then deletes the fourth line. Sed continues applying this pattern until the end of the file.
    '2~2d'  |  tells sed to delete the second line, step over the next line, delete the next line, and repeat until the end of the file is reached.
    '4,10p' | Lines starting from 4th till 10th are printed
    '4,d'   |  would generate syntax error.
    ',10d'  |  would also generate syntax error.

.. code-block:: bash

    $ echo sed | sed 's/sed/awk/'
    >>> awk # subsition took place

    $ echo sed | sed 's/sEd/awk/'
    >>> sed  # no substitution (case sensitivity)

    echo sed | sed 's/sEd/awk/I'
    >>> awk # subsition took place (case insensitive flag)

    echo sed | sed 's/s/awk/I'
    >>> awked

    echo sed | sed '$s/s/awk/I'
    >>> awked
    
    echo sed | sed 's/$s/awk/I'
    >>> sed
    
    echo sed | sed 's/^s/awk/I'
    >>> awked

    echo sed | sed 's/\bs/awk/I'
    >>> awked

    echo "s ed" | sed 's/\bS\b/awk/I' # case insensitive
    >>> awk ed

    echo "s ed" | sed 's/\bs/awk/I'  # case insensitive (\b for word bounary...i think...)
    >>> awk ed

    # === flags can be combined ===

    echo "s ed s ed" | sed 's/\bs/awk/I1' # case insensitive + only replace first *s* (combo of flags)
    >>> awk ed s ed

    echo "s ed s ed" | sed 's/\bs/awk/I1' # case insensitive + only replace second *s*
    >>> s ed awk ed


Here I'm piping the output from my alias definitions

.. code-block:: bash

    $ alias sync_sublime # print the output of this shell....below i'll start replacing parts using ``sed``
    >>> alias sync_sublime='cp -f /home/takanori/.config/sublime-text-3/Packages/User/*.sublime-snippet /home/takanori/Dropbox/git/configs_master/sbia-pc125-cinn/sublime-text/sublime-snippets-sbia/'

    # replaces only the first occurence
    $ alias sync_sublime | sed 's/sublime/SUBLIME/'
    >>> alias sync_SUBLIME='cp -f /home/takanori/.config/sublime-text-3/Packages/User/*.sublime-snippet /home/takanori/Dropbox/git/configs_master/sbia-pc125-cinn/sublime-text/sublime-snippets-sbia/'

    # replaces the 2nd occurence
    alias sync_sublime | sed 's/sublime/SUBLIME/2'
    >>> alias sync_sublime='cp -f /home/takanori/.config/SUBLIME-text-3/Packages/User/*.sublime-snippet /home/takanori/Dropbox/git/configs_master/sbia-pc125-cinn/sublime-text/sublime-snippets-sbia/'

    # replacesa all occurences
    alias sync_sublime | sed 's/sublime/SUBLIME/g'
    >>> alias sync_SUBLIME='cp -f /home/takanori/.config/SUBLIME-text-3/Packages/User/*.SUBLIME-snippet /home/takanori/Dropbox/git/configs_master/sbia-pc125-cinn/SUBLIME-text/SUBLIME-snippets-sbia/'


******************
the -e, -f options
******************
from help:

    If no -e, --expression, -f, or --file option is given, **then the first
    non-option argument is taken as the sed script to interpret**.  All
    remaining arguments are names of input files; if no input files are
    specified, then the standard input is read.

##########
sed --help
##########
Output from ``sed --help``

.. code-block:: none
    :linenos:

    Usage: sed [OPTION]... {script-only-if-no-other-script} [input-file]...

      -n, --quiet, --silent
                     suppress automatic printing of pattern space
      -e script, --expression=script
                     add the script to the commands to be executed
      -f script-file, --file=script-file
                     add the contents of script-file to the commands to be executed
      --follow-symlinks
                     follow symlinks when processing in place
      -i[SUFFIX], --in-place[=SUFFIX]
                     edit files in place (makes backup if SUFFIX supplied)
      -l N, --line-length=N
                     specify the desired line-wrap length for the `l' command
      --posix
                     disable all GNU extensions.
      -r, --regexp-extended
                     use extended regular expressions in the script.
      -s, --separate
                     consider files as separate rather than as a single continuous
                     long stream.
      -u, --unbuffered
                     load minimal amounts of data from the input files and flush
                     the output buffers more often
      -z, --null-data
                     separate lines by NUL characters
          --help     display this help and exit
          --version  output version information and exit

    If no -e, --expression, -f, or --file option is given, then the first
    non-option argument is taken as the sed script to interpret.  All
    remaining arguments are names of input files; if no input files are
    specified, then the standard input is read.

    GNU sed home page: <http://www.gnu.org/software/sed/>.
    General help using GNU software: <http://www.gnu.org/gethelp/>.
    E-mail bug reports to: <bug-sed@gnu.org>.
    Be sure to include the word ``sed'' somewhere in the ``Subject:'' field.

####################
output from man page
####################
``man -P cat sed``

.. code-block:: none
    :linenos:

    SED(1)                                                                                    User Commands                                                                                    SED(1)



    NAME
           sed - stream editor for filtering and transforming text

    SYNOPSIS
           sed [OPTION]... {script-only-if-no-other-script} [input-file]...

    DESCRIPTION
           Sed  is  a  stream  editor.   A stream editor is used to perform basic text transformations on an input stream (a file or input from a pipeline).  While in some ways similar to an editor
           which permits scripted edits (such as ed), sed works by making only one pass over the input(s), and is consequently more efficient.  But it is sed's ability to filter text in a  pipeline
           which particularly distinguishes it from other types of editors.

           -n, --quiet, --silent

                  suppress automatic printing of pattern space

           -e script, --expression=script

                  add the script to the commands to be executed

           -f script-file, --file=script-file

                  add the contents of script-file to the commands to be executed

           --follow-symlinks

                  follow symlinks when processing in place

           -i[SUFFIX], --in-place[=SUFFIX]

                  edit files in place (makes backup if SUFFIX supplied)

           -l N, --line-length=N

                  specify the desired line-wrap length for the `l' command

           --posix

                  disable all GNU extensions.

           -r, --regexp-extended

                  use extended regular expressions in the script.

           -s, --separate

                  consider files as separate rather than as a single continuous long stream.

           -u, --unbuffered

                  load minimal amounts of data from the input files and flush the output buffers more often

           -z, --null-data

                  separate lines by NUL characters

           --help
                  display this help and exit

           --version
                  output version information and exit

           If  no  -e, --expression, -f, or --file option is given, then the first non-option argument is taken as the sed script to interpret.  All remaining arguments are names of input files; if
           no input files are specified, then the standard input is read.

           GNU sed home page: <http://www.gnu.org/software/sed/>.  General help using GNU software: <http://www.gnu.org/gethelp/>.  E-mail bug reports to: <bug-sed@gnu.org>.  Be sure to include the
           word ``sed'' somewhere in the ``Subject:'' field.

    COMMAND SYNOPSIS
           This  is  just  a  brief  synopsis  of  sed commands to serve as a reminder to those who already know sed; other documentation (such as the texinfo document) must be consulted for fuller
           descriptions.

       Zero-address ``commands''
           : label
                  Label for b and t commands.

           #comment
                  The comment extends until the next newline (or the end of a -e script fragment).

           }      The closing bracket of a { } block.

       Zero- or One- address commands
           =      Print the current line number.

           a \

           text   Append text, which has each embedded newline preceded by a backslash.

           i \

           text   Insert text, which has each embedded newline preceded by a backslash.

           q [exit-code]
                  Immediately quit the sed script without processing any more input, except that if auto-print is not disabled the current pattern space will be printed.  The exit code argument  is
                  a GNU extension.

           Q [exit-code]
                  Immediately quit the sed script without processing any more input.  This is a GNU extension.

           r filename
                  Append text read from filename.

           R filename
                  Append a line read from filename.  Each invocation of the command reads a line from the file.  This is a GNU extension.

       Commands which accept address ranges
           {      Begin a block of commands (end with a }).

           b label
                  Branch to label; if label is omitted, branch to end of script.

           c \

           text   Replace the selected lines with text, which has each embedded newline preceded by a backslash.

           d      Delete pattern space.  Start next cycle.

           D      If  pattern  space  contains no newline, start a normal new cycle as if the d command was issued.  Otherwise, delete text in the pattern space up to the first newline, and restart
                  cycle with the resultant pattern space, without reading a new line of input.

           h H    Copy/append pattern space to hold space.

           g G    Copy/append hold space to pattern space.

           l      List out the current line in a ``visually unambiguous'' form.

           l width
                  List out the current line in a ``visually unambiguous'' form, breaking it at width characters.  This is a GNU extension.

           n N    Read/append the next line of input into the pattern space.

           p      Print the current pattern space.

           P      Print up to the first embedded newline of the current pattern space.

           s/regexp/replacement/
                  Attempt to match regexp against the pattern space.  If successful, replace that portion matched with replacement.  The replacement may contain the special character & to refer  to
                  that portion of the pattern space which matched, and the special escapes \1 through \9 to refer to the corresponding matching sub-expressions in the regexp.

           t label
                  If  a  s///  has  done  a successful substitution since the last input line was read and since the last t or T command, then branch to label; if label is omitted, branch to end of
                  script.

           T label
                  If no s/// has done a successful substitution since the last input line was read and since the last t or T command, then branch to label; if label is omitted,  branch  to  end  of
                  script.  This is a GNU extension.

           w filename
                  Write the current pattern space to filename.

           W filename
                  Write the first line of the current pattern space to filename.  This is a GNU extension.

           x      Exchange the contents of the hold and pattern spaces.

           y/source/dest/
                  Transliterate the characters in the pattern space which appear in source to the corresponding character in dest.

    Addresses
           Sed  commands  can be given with no addresses, in which case the command will be executed for all input lines; with one address, in which case the command will only be executed for input
           lines which match that address; or with two addresses, in which case the command will be executed for all input lines which match the inclusive range of lines  starting  from  the  first
           address  and  continuing to the second address.  Three things to note about address ranges: the syntax is addr1,addr2 (i.e., the addresses are separated by a comma); the line which addr1
           matched will always be accepted, even if addr2 selects an earlier line; and if addr2 is a regexp, it will not be tested against the line that addr1 matched.

           After the address (or address-range), and before the command, a !  may be inserted, which specifies that the command shall only be executed if the address  (or  address-range)  does  not
           match.

           The following address types are supported:

           number Match only the specified line number (which increments cumulatively across files, unless the -s option is specified on the command line).

           first~step
                  Match  every  step'th  line starting with line first.  For example, ``sed -n 1~2p'' will print all the odd-numbered lines in the input stream, and the address 2~5 will match every
                  fifth line, starting with the second.  first can be zero; in this case, sed operates as if it were equal to step.  (This is an extension.)

           $      Match the last line.

           /regexp/
                  Match lines matching the regular expression regexp.

           \cregexpc
                  Match lines matching the regular expression regexp.  The c may be any character.

           GNU sed also supports some special 2-address forms:

           0,addr2
                  Start out in "matched first address" state, until addr2 is found.  This is similar to 1,addr2, except that if addr2 matches the very first line of input the 0,addr2 form  will  be
                  at the end of its range, whereas the 1,addr2 form will still be at the beginning of its range.  This works only when addr2 is a regular expression.

           addr1,+N
                  Will match addr1 and the N lines following addr1.

           addr1,~N
                  Will match addr1 and the lines following addr1 until the next line whose input line number is a multiple of N.

    REGULAR EXPRESSIONS
           POSIX.2  BREs  should  be supported, but they aren't completely because of performance problems.  The \n sequence in a regular expression matches the newline character, and similarly for
           \a, \t, and other sequences.

    BUGS
           E-mail bug reports to bug-sed@gnu.org.  Also, please include the output of ``sed --version'' in the body of your report if at all possible.

    AUTHOR
           Written by Jay Fenlason, Tom Lord, Ken Pizzini, and Paolo Bonzini.  GNU sed home page: <http://www.gnu.org/software/sed/>.  General help  using  GNU  software:  <http://www.gnu.org/geth‐
           elp/>.  E-mail bug reports to: <bug-sed@gnu.org>.  Be sure to include the word ``sed'' somewhere in the ``Subject:'' field.

    COPYRIGHT
           Copyright © 2012 Free Software Foundation, Inc.  License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>.
           This is free software: you are free to change and redistribute it.  There is NO WARRANTY, to the extent permitted by law.

    SEE ALSO
           awk(1), ed(1), grep(1), tr(1), perlre(1), sed.info, any of various books on sed, the sed FAQ (http://sed.sf.net/grabbag/tutorials/sedfaq.txt), http://sed.sf.net/grabbag/.

           The full documentation for sed is maintained as a Texinfo manual.  If the info and sed programs are properly installed at your site, the command

                  info sed

           should give you access to the complete manual.



    sed 4.2.2                                                                                 December 2012                                                                                    SED(1)