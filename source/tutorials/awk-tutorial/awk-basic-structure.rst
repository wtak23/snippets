
.. _awk-basic-structure:

###############
Basic structure
###############
The essential organization of an AWK program follows the form:

.. code-block:: bash
    :linenos:

    pattern { action }

The pattern specifies when the action is performed. Like most UNIX utilities, AWK is line oriented. That is, the pattern specifies a test that is performed with each line read as input. If the condition is true, then the action is taken. The default pattern is something that matches every line. This is the blank or null pattern. Two other important patterns are specified by the keywords "BEGIN" and "END". As you might expect, these two words specify actions to be taken before any lines are read, and after the last line is read. The AWK program below:

.. code-block:: bash
    :linenos:

    BEGIN { print "START" }
          { print         }
    END   { print "STOP"  }

adds one line before and one line after the input file. This isn't very useful, but with a simple change, we can make this into a typical AWK program:

.. code-block:: bash
    :linenos:

    BEGIN { print "File\tOwner"}
    { print $8, "\t", $3}
    END { print " - DONE -" }

I'll improve the script in the next sections, but we'll call it "FileOwner". But let's not put it into a script or file yet. I will cover that part in a bit. Hang on and follow with me so you get the flavor of AWK.

The characters "\t" Indicates a tab character so the output lines up on even boundries. The "$8" and "$3" have a meaning similar to a shell script. Instead of the eighth and third argument, they mean the eighth and third field of the input line. You can think of a field as a column, and the action you specify operates on each line or row read in.

There are two differences between AWK and a shell processing the characters within double quotes. AWK understands special characters follow the "\" character like "t". The Bourne and C UNIX shells do not. Also, unlike the shell (and PERL) AWK does not evaluate variables within strings. To explain, the second line could not be written like this:

.. code-block:: bash
    :linenos:

    {print "$8\t$3" }

That example would print "$8 $3". Inside the quotes, the dollar sign is not a special character. Outside, it corresponds to a field. What do I mean by the third and eight field? Consider the Solaris "/usr/bin/ls -l" command, which has eight columns of information. The System V version (Similar to the Linux version), "/usr/5bin/ls -l" has 9 columns. The third column is the owner, and the eighth (or nineth) column in the name of the file. This AWK program can be used to process the output of the "ls -l" command, printing out the filename, then the owner, for each file. I'll show you how.

Update: On a linux system, change "$8" to "$9".

One more point about the use of a dollar sign. In scripting languages like Perl and the various shells, a dollar sign means the word following is the name of the variable. Awk is different. The dollar sign means that we are refering to a field or column in the current line. When switching between Perl and AWK you must remener that "$" has a different meaning. So the following piece of code prints two "fields" to standard out. The first field printed is the number "5", the second is the fifth field (or column) on the input line.

.. code-block:: bash
    :linenos:

    BEGIN { x=5 }
    { print x, $x}