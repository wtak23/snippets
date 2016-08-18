
.. _awk-summary-commands:

#######################
Summary of AWK Commands
#######################
There are only a few commands in AWK. The list and syntax follows: 

.. code-block:: bash
    :linenos:

    if ( conditional ) statement [ else statement ]
    while ( conditional ) statement
    for ( expression ; conditional ; expression ) statement
    for ( variable in array ) statement
    break
    continue
    { [ statement ] ...}
    variable=expression
    print [ expression-list ] [ > expression ]
    printf format [ , expression-list ] [ > expression ]
    next
    exit

t this point, you can use AWK as a language for simple calculations; If you wanted to calculate something, and not read any lines for input, you could use the BEGIN keyword discussed earlier, combined with a exit command:

.. code-block:: bash
    :linenos:

    #!/bin/awk -f
    BEGIN {

    # Print the squares from 1 to 10 the first way
        i=1;
        while (i <= 10) {
            printf "The square of ", i, " is ", i*i;
            i = i+1;
        }

    # do it again, using more concise code
        for (i=1; i <= 10; i++) {
            printf "The square of ", i, " is ", i*i;
        }

    # now end
    exit;
    }

The following asks for a number, and then squares it:

.. code-block:: bash
    :linenos:

    #!/bin/awk -f
    BEGIN {
        print "type a number";
    }
    {
        print "The square of ", $1, " is ", $1*$1;
        print "type another number";
    }
    END {
        print "Done"
    }

The above isn't a good filter, because it asks for input each time. If you pipe the output of another program into it, you would generate a lot of meaningless prompts.

Here is a filter that you should find useful. It counts lines, totals up the numbers in the first column, and calculates the average. Pipe ``"wc -c *"`` into it, and it will count files, and tell you the average number of words per file, as well as the total words and the number of files. 

.. code-block:: bash
    :linenos:

    #!/bin/awk -f
    BEGIN {
    # How many lines
        lines=0;
        total=0;
    }
    {
    # this code is executed once for each line
    # increase the number of files
        lines++;
    # increase the total size, which is field #1
        total+=$1;
    }
    END {
    # end, now output the total
        print lines " lines read";
        print "total is ", total;
        if (lines > 0 ) {
        print "average is ", total/lines;
        } else {
        print "average is 0";
        }
    }


You can pipe the output of "ls -s" into this filter to count the number of files, the total size, and the average size. There is a slight problem with this script, as it includes the output of "ls" that reports the total. This causes the number of files to be off by one. Changing

.. code-block:: bash
    :linenos:

    lines++;

to

.. code-block:: bash
    :linenos:

    if ($1 != "total" ) lines++;

will fix this problem. Note the code which prevents a divide by zero. This is common in well-written scripts. I also initialize the variables to zero. This is not necessary, but it is a good habit.     