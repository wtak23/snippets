
.. awk-buildin-vars:

**********************
AWK Built-in Variables
**********************


I have mentioned two kinds of variables: positional and user defined. A user defined variable is one you create. A positional variable is not a special variable, but a function triggered by the dollar sign. Therefore

.. code-block:: bash
    :linenos:
    
    print $1;

and

.. code-block:: bash
    :linenos:

    X=1;
    print $X;

do the same thing: print the first field on the line. There are two more points about positional variables that are very useful. The variable "$0" refers to the entire line that AWK reads in. That is, if you had eight fields in a line,

.. code-block:: bash
    :linenos:

    print $0;

is similar to

.. code-block:: bash
    :linenos:

    print $1, $2, $3, $4, $5, $6, $7, $8

This will change the spacing between the fields; otherwise, they behave the same. You can modify positional variables. The following commands

.. code-block:: bash
    :linenos:

    $2="";
    print;

deletes the second field. If you had four fields, and wanted to print out the second and fourth field, there are two ways. This is the first:

.. code-block:: bash
    :linenos:

    #!/bin/awk -f
    {
        $1="";
        $3="";
        print;
    }

and the second

.. code-block:: bash
    :linenos:

    #!/bin/awk -f
    {
        print $2, $4;
    }

These perform similarly, but not identically. The number of spaces between the values vary. There are two reasons for this. The actual number of fields does not change. Setting a positional variable to an empty string does not delete the variable. It's still there, but the contents has been deleted. The other reason is the way AWK outputs the entire line. There is a field separator that specifies what character to put between the fields on output. The first example outputs four fields, while the second outputs two. In-between each field is a space. This is easier to explain if the characters between fields could be modified to be made more visible. Well, it can. AWK provides special variables for just that purpose.


#######################################
FS - The Input Field Separator Variable
#######################################
AWK can be used to parse many system administration files. However, many of these files do not have whitespace as a separator. as an example, the password file uses colons. You can easily change the field separator character to be a colon using the "-F" command line option. The following command will print out accounts that don't have passwords:

.. code-block:: bash
    :linenos:

    awk -F: '{if ($2 == "") print $1 ": no password!"}' </etc/passwd

There is a way to do this without the command line option. The variable "FS" can be set like any variable, and has the same function as the "-F" command line option. The following is a script that has the same function as the one above.

.. code-block:: bash
    :linenos:

    #!/bin/awk -f
    BEGIN {
        FS=":";
    }
    {
        if ( $2 == "" ) {
            print $1 ": no password!";
        }
    }

Click here to get file: http://www.grymoire.com/Unix/Scripts/awk_nopasswd.awk

The second form can be used to create a UNIX utility, which I will name "chkpasswd", and executed like this:

.. code-block:: bash
    :linenos:

    chkpasswd </etc/passwd

The command "chkpasswd -F:" cannot be used, because AWK will never see this argument. All interpreter scripts accept one and only one argument, which is immediately after the "#!/bin/awk" string. In this case, the single argument is "-f". Another difference between the command line option and the internal variable is the ability to set the input field separator to be more than one character. If you specify

.. code-block:: bash
    :linenos:

    FS=": ";

then AWK will split a line into fields wherever it sees those two characters, in that exact order. You cannot do this on the command line.

There is a third advantage the internal variable has over the command line option: you can change the field separator character as many times as you want while reading a file. Well, at most once for each line. You can even change it depending on the line you read. Suppose you had the following file which contains the numbers 1 through 7 in three different formats. Lines 4 through 6 have colon separated fields, while the others separated by spaces.

.. code-block:: bash
    :linenos:

    ONE 1 I
    TWO 2 II
    #START
    THREE:3:III
    FOUR:4:IV
    FIVE:5:V
    #STOP
    SIX 6 VI
    SEVEN 7 VII

The AWK program can easily switch between these formats:

.. code-block:: bash
    :linenos:

    #!/bin/awk -f
    {
        if ($1 == "#START") {
            FS=":";
        } else if ($1 == "#STOP") {
            FS=" ";
        } else {
            #print the Roman number in column 3
            print $3
        }
    }



Click here to get file: http://www.grymoire.com/Unix/Scripts/awk_example3.awk

Note the field separator variable retains its value until it is explicitly changed. You don't have to reset it for each line. Sounds simple, right? However, I have a trick question for you. What happens if you change the field separator while reading a line? That is, suppose you had the following line

.. code-block:: bash
    :linenos:

    One Two:Three:4 Five

and you executed the following script:

.. code-block:: bash
    :linenos:

    #!/bin/awk -f
    {
        print $2
        FS=":"
        print $2
    }

What would be printed? "Three" or "Two:Three:4?" Well, the script would print out "Two:Three:4" twice. However, if you deleted the first print statement, it would print out "Three" once! I thought this was very strange at first, but after pulling out some hair, kicking the deck, and yelling at muself and everyone who had anything to do with the development of UNIX, it is intuitively obvious. You just have to be thinking like a professional programmer to realize it is intuitive. I shall explain, and prevent you from causing yourself physical harm.

If you change the field separator before you read the line, the change affects what you read. If you change it after you read the line, it will not redefine the variables. You wouldn't want a variable to change on you as a side-effect of another action. A programming language with hidden side effects is broken, and should not be trusted. AWK allows you to redefine the field separator either before or after you read the line, and does the right thing each time. Once you read the variable, the variable will not change unless you change it. Bravo!

To illustrate this further, here is another version of the previous code that changes the field separator dynamically. In this case, AWK does it by examining field "$0", which is the entire line. When the line contains a colon, the field separator is a colon, otherwise, it is a space. Here is a version that worked with older versions of awk:

.. code-block:: bash
    :linenos:

    #!/bin/awk -f
    {
        if ( $0 ~ /:/ ) {
            FS=":";
        } else {
            FS=" ";
        }
        #print the third field, whatever format
        print $3
    }


Click here to get file: http://www.grymoire.com/Unix/Scripts/awk_example4.awk

However, this behavior changed in later versions, so the above script no longer works. What happens is that once the FS variable is changed, you have to re-evaluate the fields by using $0=$0:

.. code-block:: bash
    :linenos:

    #!/bin/awk -f
    {
        if ( $0 ~ /:/ ) {
            FS=":";
            $0=$0
        } else {
            FS=" ";
            $0=$0
        }
        #print the third field, whatever format
        print $3
    }


Click here to get file: http://www.grymoire.com/Unix/Scripts/awk_example4a.awk

This example eliminates the need to have the special "#START" and "#STOP" lines in the input.

#########################################
OFS - The Output Field Separator Variable
#########################################

There is an important difference between

.. code-block:: bash
    :linenos:

    print $2 $3

and

.. code-block:: bash
    :linenos:

    print $2, $3

The first example prints out one field, and the second prints out two fields. In the first case, the two positional parameters are concatenated together and output without a space. In the second case, AWK prints two fields, and places the output field separator between them. Normally this is a space, but you can change this by modifying the variable "OFS".

If you wanted to copy the password file, but delete the encrypted password, you could use AWK:

.. code-block:: bash
    :linenos:

    #!/bin/awk -f
    BEGIN {
        FS=":";
        OFS=":";
    }
    {
        $2="";
        print
    }


Click here to get file: http://www.grymoire.com/Unix/Scripts/delete_passwd.awk

Give this script the password file, and it will delete the password, but leave everything else the same. You can make the output field separator any number of characters. You are not limited to a single character.

##################################
NF - The Number of Fields Variable
##################################
It is useful to know how many fields are on a line. You may want to have your script change its operation based on the number of fields. As an example, the command "ls -l" may generate eight or nine fields, depending on which version you are executing. The System V version, "/usr/bin/ls -l" generates nine fields, which is equivalent to the Berkeley "/usr/ucb/ls -lg" command. If you wanted to print the owner and filename then the following AWK script would work with either version of "ls:"

.. code-block:: bash
    :linenos:

    #!/bin/awk -f
    # parse the output of "ls -l"
    # print owner and filename
    # remember - Berkeley ls -l has 8 fields, System V has 9
    {
        if (NF == 8) {
            print $3, $8;
        } else if (NF == 9) {
            print $3, $9;
        } 
    }


Click here to get file: http://www.grymoire.com/Unix/Scripts/owner_group.awk

Don't forget the variable can be prepended with a "$". This allows you to print the last field of any column

.. code-block:: bash
    :linenos:

    #!/bin/awk -f
    { print $NF; }

Click here to get file: http://www.grymoire.com/Unix/Scripts/print_last_field.awk

One warning about AWK. There is a limit of 99 fields in a single line. PERL does not have any such limitations.

###################################
NR - The Number of Records Variable
###################################
Another useful variable is "NR". This tells you the number of records, or the line number. You can use AWK to only examine certain lines. This example prints lines after the first 100 lines, and puts a line number before each line after 100:

.. code-block:: bash
    :linenos:

    #!/bin/awk -f
    if (NR > 100) {
        print NR, $0;
    }

Click link to get file: `awk_example5.awk <http://www.grymoire.com/Unix/Scripts/awk_example5.awk>`_

##################################
RS - The Record Separator Variable
##################################
Normally, AWK reads one line at a time, and breaks up the line into fields. You can set the "RS" variable to change AWK's definition of a "line". If you set it to an empty string, then AWK will read the entire file into memory. You can combine this with changing the "FS" variable. This example treats each line as a field, and prints out the second and third line:

.. code-block:: bash
    :linenos:

    #!/bin/awk -f
    BEGIN {
    # change the record separator from newline to nothing   
        RS=""
    # change the field separator from whitespace to newline
        FS="\n"
    }
    {
    # print the second and third line of the file
        print $2, $3;
    }

Click here to get file: http://www.grymoire.com/Unix/Scripts/awk_example6.awk

The two lines are printed with a space between. Also this will only work if the input file is less than 100 lines, therefore this technique is limited. You can use it to break words up, one word per line, using this:

.. code-block:: bash
    :linenos:

    #!/bin/awk -f
    BEGIN {
        RS=" ";
    }
    {
        print ;
    }



Click here to get file: http://www.grymoire.com/Unix/Scripts/oneword_per_line.awk

but this only works if all of the words are separated by a space. If there is a tab or punctuation inside, it would not.

##########################################
ORS - The Output Record Separator Variable
##########################################
The default output record separator is a newline, like the input. This can be set to be a newline and carriage return, if you need to generate a text file for a non-UNIX system.

.. code-block:: bash
    :linenos:

    #!/bin/awk -f
    # this filter adds a carriage return to all lines
    # before the newline character
    BEGIN { 
        ORS="\r\n"
    }
    { print }



Click here to get file: http://www.grymoire.com/Unix/Scripts/add_cr.awk

########################################
FILENAME - The Current Filename Variable
########################################


The last variable known to regular AWK is "FILENAME", which tells you the name of the file being read.

.. code-block:: bash
    :linenos:

    #!/bin/awk -f
    # reports which file is being read
    BEGIN {
        f="";
    }
    {   if (f != FILENAME) {
            print "reading", FILENAME;
            f=FILENAME;
        }
        print;
    }


Click here to get file: http://www.grymoire.com/Unix/Scripts/awk_example6a.awk

This can be used if several files need to be parsed by AWK. Normally you use standard input to provide AWK with information. You can also specify the filenames on the command line. If the above script was called "testfilter", and if you executed it with

.. code-block:: bash
    :linenos:

    testfilter file1 file2 file3

It would print out the filename before each change. An alternate way to specify this on the command line is

.. code-block:: bash
    :linenos:

    testfilter file1 - file3 <file2

In this case, the second file will be called "-", which is the conventional name for standard input. I have used this when I want to put some information before and after a filter operation. The prefix and postfix files special data before and after the real data. By checking the filename, you can parse the information differently. This is also useful to report syntax errors in particular files:

.. code-block:: bash
    :linenos:

    #!/bin/awk -f
    { 
        if (NF == 6) {
            # do the right thing
        } else {
            if (FILENAME == "-" ) {
                print "SYNTAX ERROR, Wrong number of fields,", 
                "in STDIN, line #:", NR,  "line: ", $0;
            } else {
                print "SYNTAX ERROR, Wrong number of fields,", 
                "Filename: ", FILENAME, "line # ", NR, "line: ", $0;
            }
        }
    }


Click here to get file: http://www.grymoire.com/Unix/Scripts/awk_example7.awk