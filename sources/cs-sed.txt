sed
"""

.. contents:: **Table of Contents**
    :depth: 3   


############
ultra-basics
############

.. code-block:: bash
    :linenos:

    echo sed | sed 's/sed/awk/'
    echo sed | sed 's/sEd/awk/'
    echo sed | sed 's/sEd/awk/I'
    echo sed | sed 's/s/awk/I'
    echo sed | sed '$s/s/awk/I'
    echo sed | sed 's/$s/awk/I'
    echo sed | sed 's/^s/awk/I'
    echo sed | sed 's/\bs/awk/I'
    echo sed | sed 's/\bs\b/awk/I'
    echo "s ed" | sed 's/\bS\b/awk/I' # case insensitive
        > awk ed
    echo "s ed" | sed 's/\bs/awk/I'  # case insensitive
    echo "s ed s ed" | sed 's/\bs/awk/I1' # case insensitive + only replace first *s*
        > awk ed s ed
    echo "s ed s ed" | sed 's/\bs/awk/I1' # case insensitive + only replace second *s*
        > s ed awk ed

.. code-block:: bash
    :linenos:

    alias sync_sublime
        > alias sync_sublime='cp -f /home/takanori/.config/sublime-text-3/Packages/User/*.sublime-snippet /home/takanori/Dropbox/git/configs_master/sbia-pc125-cinn/sublime-text/sublime-snippets-sbia/'

    # replaces only the first occurence
    alias sync_sublime | sed 's/sublime/SUBLIME/'
        > alias sync_SUBLIME='cp -f /home/takanori/.config/sublime-text-3/Packages/User/*.sublime-snippet /home/takanori/Dropbox/git/configs_master/sbia-pc125-cinn/sublime-text/sublime-snippets-sbia/'

    # replaces the 2nd occurence
    alias sync_sublime | sed 's/sublime/SUBLIME/2'
        > alias sync_sublime='cp -f /home/takanori/.config/SUBLIME-text-3/Packages/User/*.sublime-snippet /home/takanori/Dropbox/git/configs_master/sbia-pc125-cinn/sublime-text/sublime-snippets-sbia/'

    # replacesa all occurences
    alias sync_sublime | sed 's/sublime/SUBLIME/g'
        > alias sync_SUBLIME='cp -f /home/takanori/.config/SUBLIME-text-3/Packages/User/*.SUBLIME-snippet /home/takanori/Dropbox/git/configs_master/sbia-pc125-cinn/SUBLIME-text/SUBLIME-snippets-sbia/'

###########
More Basics
###########

******************
the -e, -f options
******************
from help:

    If no -e, --expression, -f, or --file option is given, **then the first
    non-option argument is taken as the sed script to interpret**.  All
    remaining arguments are names of input files; if no input files are
    specified, then the standard input is read.


*****************
deletion commands
*****************
.. code-block:: 

    # basic syntax: 
    /regexp/action

    p = prints the line
    d = deletes the line
    s/regexp/pattern/ <= substitues regexp with pattern

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

******************
substitution flags
******************
.. code-block:: bash
    :linenos:

    # replace *the* with THE in line 3
    sed '3s/[Tt]he/THE/g' sed-text.txt  

    # replace *the* with THE in line3-6
    sed '3,6s/[Tt]he/THE/g' sed-text.txt 

.. csv-table:: 
    :header: Flag, Description
    :widths: 22,70
    :delim: | 

    g |   Replace all matches, not just the first match.
    NUMBER |  Replace only NUMBERth match.
    p |   If substitution was made, print pattern space.
    w FILENAME  | If substitution was made, write result to FILENAME.
    I or i | Match in a case-insensitive manner.
    M  or m | In addition to the normal behavior of the special regular expression characters ^ and $, this flag causes ^ to match the empty string after a newline and $ to match the empty string before a newline.

