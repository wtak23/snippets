sed-tutorial-tutorials-points
"""""""""""""""""""""""""""""
http://www.tutorialspoint.com/sed/sed_workflow.htm

.. contents:: **Contents**
    :depth: 3

##############
Sed - workflow
##############
The following process repeats until the file is exhausted.

- **read**: SED reads a line from the input stream (file, pipe, or stdin) and stores it in its internal buffer called **pattern buffer**.
- **Execute**: All SED commands are applied sequentially on the pattern buffer. By *default*, SED commands are applied on *all lines (globally)* unless line **addressing** is specified.
- **Display**: Send the (modified) contents to the output stream. After sending the data, the **pattern buffer** will be empty.


Notes

- By default, all SED commands are applied on the pattern buffer, hence the input file remains unchanged. GNU SED provides a way to modify the input file in-a-place. We will explore about it in later sections.
- There is another memory area called **hold buffer**. Data can be stored in a hold buffer for later retrieval. At the end of each cycle, SED removes the contents of the pattern buffer but the contents of the hold buffer remains persistent between SED cycles. 
- If no input files are provided, then SED accepts input from the standard input stream (**stdin**).
- If **address range** is not provided by default, then SED operates on each line.

#########################
Basic syntax and examples
#########################

Suppose we have a file ``books.txt`` with the following content::

    1) A Storm of Swords, George R. R. Martin, 1216 
    2) The Two Towers, J. R. R. Tolkien, 352 
    3) The Alchemist, Paulo Coelho, 197 
    4) The Fellowship of the Ring, J. R. R. Tolkien, 432 
    5) The Pilgrimage, Paulo Coelho, 288 
    6) A Game of Thrones, George R. R. Martin, 864

``quotes.txt``::

    There is only one thing that makes a dream impossible to achieve: the fear of failure. 
     - Paulo Coelho, The Alchemist

********
Examples
********
.. code-block:: bash

    # in line command
    sed [-n] [-e] 'command(s)' files 

    # specify a script file with sed commands (i probably won't ever use this)
    sed [-n] -f scriptfile files

    # emulates the `cat` command (displays the content of the file)
    $ sed '' books.txt
    $ cat books.txt

    # run 3 separate commands with the -e option (delete line1, 2, 5)
    $ sed -e '1d' -e '2d' -e '5d' books.txt 
    3) The Alchemist, Paulo Coelho, 197 
    4) The Fellowship of the Ring, J. R. R. Tolkien, 432 
    6) A Game of Thrones, George R. R. Martin, 864

    # create scriptfile command.txt, and then run it
    $ echo -e "1d\n2d\n5d" > commands
    $ sed -f commands books.txt 
    3) The Alchemist, Paulo Coelho, 197 
    4) The Fellowship of the Ring, J. R. R. Tolkien, 432 
    6) A Game of Thrones, George R. R. Martin, 864

****************
Standard options
****************
.. code-block:: bash

    # -n, --quiet, --silent (probably will never use unless -f option is used)
    sed -n '' quote.txt # <- won't print anything
    sed '' quote.txt # <- prints file (like cat)

    # -e: next argument is an editing command. can be used to specify multiple commands
    $ sed -e '' -e 'p' quote.txt
    There is only one thing that makes a dream impossible to achieve: the fear of failure. 
    There is only one thing that makes a dream impossible to achieve: the fear of failure. 
     - Paulo Coelho, The Alchemist
     - Paulo Coelho, The Alchemist

    # -f for using scriptfile. 
    $ echo "p" > commands 
    $ sed -n -f commands quote.txt # here -n makes sense
    There is only one thing that makes a dream impossible to achieve: the fear of failure. 
     - Paulo Coelho, The Alchemist
    $ sed -f command quote.txt # w/o -n, gets printed out twice
    There is only one thing that makes a dream impossible to achieve: the fear of failure. 
    There is only one thing that makes a dream impossible to achieve: the fear of failure. 
     - Paulo Coelho, The Alchemist
     - Paulo Coelho, The Alchemist

********************
GNU specific options
********************
::

    -n, --quiet, --silent: 
        Same as standard -n option.
    -e script, --expression=script: 
        Same as standard -e option.
    -f script-file, --file=script-file: 
        Same as standard -f option.
    --follow-symlinks: 
        If this option is provided, the SED follows symbolic links while editing files in place.
    -i[SUFFIX], --in-place[=SUFFIX]: 
        This option is used to edit file in place. 
        If suffix is provided, it takes a backup of the original file, otherwise it overwrites the original file.
    -l N, --line-lenght=N: 
        This option sets the line length for l command to N characters.
    --posix: 
        This option disables all GNU extensions.
    -r, --regexp-extended: 
        This option allows to use extended regular expressions rather than basic regular expressions.
    -u, --unbuffered: 
        When this option is provided, the SED loads minimal amount of data from the input files and flushes the output buffers more often. 
        It is useful for editing the output of "tail -f" when you do not want to wait for the output.
    -z, --null-data: 
        By default, the SED separates each line by a new-line character. 
        If NULL-data option is provided, it separates the lines by NULL characters.

###############
Loops, Branches
###############
Skipped. These are complete overkills for me.

Loops uses **label**

::

    :label 
    :start 
    :end 
    :up

Branches use ``t`` command to jump to labels if previous substitutie command is successful.

##############################################
Address range (search by specifying line-nums)
##############################################
**********
'p' syntax
**********
.. code-block:: bash

    # this works like cat
    $ sed '' book.txt
    1) A Storm of Swords, George R. R. Martin, 1216 
    2) The Two Towers, J. R. R. Tolkien, 352 
    3) The Alchemist, Paulo Coelho, 197 
    4) The Fellowship of the Ring, J. R. R. Tolkien, 432 
    5) The Pilgrimage, Paulo Coelho, 288 
    6) A Game of Thrones, George R. R. Martin, 864

    # this print books twice
    $ sed 'p' books.txt
    1) A Storm of Swords, George R. R. Martin, 1216 
    1) A Storm of Swords, George R. R. Martin, 1216 
    2) The Two Towers, J. R. R. Tolkien, 352 
    2) The Two Towers, J. R. R. Tolkien, 352 
    3) The Alchemist, Paulo Coelho, 197 
    3) The Alchemist, Paulo Coelho, 197 
    4) The Fellowship of the Ring, J. R. R. Tolkien, 432 
    4) The Fellowship of the Ring, J. R. R. Tolkien, 432 
    5) The Pilgrimage, Paulo Coelho, 288 
    5) The Pilgrimage, Paulo Coelho, 288 
    6) A Game of Thrones, George R. R. Martin, 864
    6) A Game of Thrones, George R. R. Martin, 864

    # what you probably wanted
    $ sed -n 'p' books.txt
    1) A Storm of Swords, George R. R. Martin, 1216 
    2) The Two Towers, J. R. R. Tolkien, 352 
    3) The Alchemist, Paulo Coelho, 197 
    4) The Fellowship of the Ring, J. R. R. Tolkien, 432 
    5) The Pilgrimage, Paulo Coelho, 288 
    6) A Game of Thrones, George R. R. Martin, 864

    # print only the 3rd line
    $ sed -n '3p' books.txt 
    3) The Alchemist, Paulo Coelho, 197 

    # print lines 2 to 5 (range inclusive)
    $ sed -n '2,5 p' books.txt 
    2) The Two Towers, J. R. R. Tolkien, 352 
    3) The Alchemist, Paulo Coelho, 197 
    4) The Fellowship of the Ring, J. R. R. Tolkien, 432 
    5) The Pilgrimage, Paulo Coelho, 288 

    # print last line using $
    $ sed -n '$ p' books.txt 
    6) A Game of Thrones, George R. R. Martin, 864

    # print from 3rd to last line
    $ sed -n '3,$ p' books.txt 
    3) The Alchemist, Paulo Coelho, 197 
    4) The Fellowship of the Ring, J. R. R. Tolkien, 432 
    5) The Pilgrimage, Paulo Coelho, 288 
    6) A Game of Thrones, George R. R. Martin, 864

*************
'M,+n' syntax
*************
.. code-block:: bash

    #=========================================================================#
    # 'M,+n' syntax
    #=========================================================================#
    # 'M,+n' means print n-lines, starting from line M
    $ sed -n '2,+2 p' books.txt 
    2) The Two Towers, J. R. R. Tolkien, 352 
    3) The Alchemist, Paulo Coelho, 197 
    4) The Fellowship of the Ring, J. R. R. Tolkien, 432

    $ sed -n '2,+0 p' books.txt 
    2) The Two Towers, J. R. R. Tolkien, 352 

*************
'M,~n' syntax
*************
.. code-block:: bash

    #=========================================================================#
    # tilde ~ syntax (step size)
    # 'M~n' means starting from Line-M, print every n-lines
    #=========================================================================#
    $ sed -n '1~2 p' books.txt 
    1) A Storm of Swords, George R. R. Martin, 1216 
    3) The Alchemist, Paulo Coelho, 197 
    5) The Pilgrimage, Paulo Coelho, 288 

    $ sed -n '2~2 p' books.txt 
    2) The Two Towers, J. R. R. Tolkien, 352 
    4) The Fellowship of the Ring, J. R. R. Tolkien, 432 
    6) A Game of Thrones, George R. R. Martin, 864

#####################################################################
Pattern range - search for simple-text or regexp using /regex/ syntax
#####################################################################
- In the previous chapter, we learnt how SED handles an **address range**. 
- This chapter covers how SED takes care of a **pattern range**. 

  - A pattern range can be a **simple text** or a **complex regular expression**.

.. code-block:: bash

    $ sed -n 'p' books.txt
    1) A Storm of Swords, George R. R. Martin, 1216
    2) The Two Towers, J. R. R. Tolkien, 352
    3) The Alchemist, Paulo Coelho, 197
    4) The Fellowship of the Ring, J. R. R. Tolkien, 432
    5) The Pilgrimage, Paulo Coelho, 288
    6) A Game of Thrones, George R. R. Martin, 864

    # find lines containing simple text-string "Paulo"
    $ sed -n '/Paulo/ p' books.txt
    3) The Alchemist, Paulo Coelho, 197 
    5) The Pilgrimage, Paulo Coelho, 288 

    #=========================================================================#
    # combine *pattern range* with *address range*
    #=========================================================================#
    # search for line with "Alchemist", and print until line 5
    $ sed -n '/Alchemist/, 5 p' books.txt
    3) The Alchemist, Paulo Coelho, 197 
    4) The Fellowship of the Ring, J. R. R. Tolkien, 432 
    5) The Pilgrimage, Paulo Coelho, 288 

    # search for line with "Alchemist", and print until final line ($)
    $ sed -n '/Alchemist/, $ p' books.txt
    3) The Alchemist, Paulo Coelho, 197 
    4) The Fellowship of the Ring, J. R. R. Tolkien, 432 
    5) The Pilgrimage, Paulo Coelho, 288 
    6) A Game of Thrones, George R. R. Martin, 864

    #=========================================================================#
    # specify more than one pattern range using command(,) operator
    #=========================================================================#
    # print all lines that exist between the patterns "Two" and "Pilgrimage"
    $ sed -n '/Two/, /Pilgrimage/ p' books.txt
    2) The Two Towers, J. R. R. Tolkien, 352 
    3) The Alchemist, Paulo Coelho, 197 
    4) The Fellowship of the Ring, J. R. R. Tolkien, 432 
    5) The Pilgrimage, Paulo Coelho, 288 

    # after finding the match, print 4 more lines
    $ sed -n '/Two/, +4 p' books.txt
    2) The Two Towers, J. R. R. Tolkien, 352 
    3) The Alchemist, Paulo Coelho, 197 
    4) The Fellowship of the Ring, J. R. R. Tolkien, 432 
    5) The Pilgrimage, Paulo Coelho, 288 
    6) A Game of Thrones, George R. R. Martin, 864

############################################
Basic commands (delete, read, write, append)
############################################

*************************************
Delete command [address1[,address2]]d
*************************************

*****************************************
Write command [address1[,address2]]w file
*****************************************

**************************
Append command [address]a\
**************************

**************************************
Change command [address1[,address2]]c\
**************************************

**************************
Insert Command [address]i\
**************************

*******************************************************
Translate command [address1[,address2]]y/list-1/list-2/
*******************************************************
    
*********
I command
*********

***********************
Quit Command [address]q
***********************

****************************
Read Command [address]r file
****************************

*************************************************
Exectuve Command [address1[,address2]]e [command]
*************************************************

**********************
Miscellaneous Commands
**********************
