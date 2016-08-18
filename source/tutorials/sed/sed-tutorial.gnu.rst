sed-tutorial-gnu
""""""""""""""""
ch3 - https://www.gnu.org/software/sed/manual/html_node/sed-Programs.html#sed-Programs

(basically the only chapter i need to know)

.. contents:: **Contents**
    :depth: 2

##############################
Execution Cycle: How sed works
##############################
sed maintains two data buffers (both initially empty):

1. the active **pattern space**, and 
2. the auxiliary **hold space** (**address**, i think...). 

sed operates by performing the following cycle on **each line of input**: 

- first, sed reads one line from the input stream, removes any trailing newline, and places it in the **pattern space**. 
- Then commands are executed; 

  - each command can have an address associated to it (**hold space**): 
  - a command is only executed if the condition is verified before the command is to be executed.

When the end of the script is reached, unless the ``-n`` option is in use, the **contents of pattern space are printed out to the output stream**, adding back the trailing newline if it was removed.


Unless special commands (like ``‘D’``) are used, the pattern space is deleted between two cycles. The hold space, on the other hand, keeps its data between cycles (see commands ``‘h’, ‘H’, ‘x’, ‘g’, ‘G’`` to move data between both buffers). 

###################################
Addresses: Selecting lines with sed
###################################
Options influcencing below:

- ``-n`` (--quiet): suppress automatic printing of **pattern space**
- ``-r`` (extended regexp): use extended regular expressions
- ``-i`` (inplace): edit files in place
- ``-s`` (separte): consider files as separate rather than as a single continuous long stream

*******************
Single address form
*******************
Addresses in a sed script can be in any of the following forms (if no addresses are given, then all lines are matched): 

.. http://docutils.sourceforge.net/docs/ref/rst/directives.html#id4        
.. csv-table:: 
    :header: address,description
    :widths: 20,70
    :delim: |

    *n* | match only the specified line in the input (note: sed counts lines continuously across all input files unless ``-i, -s`` options are spceified)
    ``first~stepsize`` | ``1~2`` select odd-numbered lines. ``2~3`` starts from line2, selects every 3 lines. ``10~5`` pick every 5th line starting from line 10. (you get the idea...)
    \$ |  match the **last line** of the **last file** (or the last line of **each file** if ``-i`` or ``-s`` option is used)
    /regexp/ |  Select any lines matching *regexp*. if the *regexp* includes any ``/`` char, it must be espaced with ``\``. The empty regexp ``//`` repeats the last regexp match.
    \%regexp% |  (``%`` can be replaced with any other single-char) Same as above, but use a delimitered different from ``/``. This is handy when your rexexp has bunch of ``/`` that escaping becomes pain in the butt.
    /regexp/I |  ``I`` = case-insensitive modifier
    /regexp/M |  ``M`` = *multi-line* modifier. causes ``^`` and ``$`` to match respectively the empty string after the newline (and the empty line before a newline)

****************
Two address form
****************
An address range can be specified by specifying two addresses separated by a comma (,).

- An address range matches line starting from the **1st address** and ends at the **2nd address** (inclusive)
- if the 2nd address < 1st address, only the 1st address gets matched

.. csv-table:: 
    :header: address,description
    :widths: 20,70
    :delim: |

    0,/regexp/ | ...the description didn't make sense to me...
    ``addr1,+N`` | matches **addr1** and the N lines following it
    ``addr1,~N`` | matches **addr1** and the lines following it UNTIL the next line whose input line number is a multiple of N

************************
Match negation via ``!``
************************
Appending the ``!`` character to the end of an address specification negates the sense of the match. 

- ie, ``!`` follows an address range, then only lines which **do not match** the address range will be selected.


##########################################################
Regular Expressions: Overview of regular expression syntax
##########################################################
Here is a brief description of regular expression syntax as used in sed ( i already know below, but to get an idea what char needs to be escaped)

.. http://docutils.sourceforge.net/docs/ref/rst/directives.html#id4        
.. csv-table:: 
    :header: pattern, description
    :widths: 20,70
    :delim: |

    ``*`` | 0 or more of the preceding
    ``\+`` | one or more of the preceding
    ``\?`` | 0 or 1
    ``\{i\}`` | exactly i
    ``\{i,j\}`` | between i and j (inclusive)
    ``\{i,\}`` | more than i
    ``\{(regexp)\}`` | group matches via bracket. Eg, ``\\((abcd)\\\)\*`` will search for zero or more of the entire sequence of ``abcd``. In contrast, ``abcd*`` will match ``abc`` followed by 0 or more ``d``. Can also be used for **back-references** (see below)
    ``.`` | match any char
    ``^`` | Matches the null string at beginning of the pattern space (``^#include`` to match lines where ``#include`` is the first thing on the line
    ``$`` | end of pattern space
    ``[list]`` | Match any **single char** in the list. [aeiou] for all voewls. [char1-char2] for any char between (inclusive).
    ``[^list]`` | Match any **single char** NOT in the list. NOTE: chars ``$,*,.,[,\`` are normally not special in a list, meaning ``[\*]`` will match either ``\`` or ``*``
    ``\digit`` | **Back reference**. Matches the digit-th ``\( ..\)``  paranthesized subexpression in the regexp.  Subexpressions are implicity numbered by counting occurrences of ``\(`` left-to-right. 
    ``\n`` | matches the newline char
    ``\char`` | matches ``char``, where ``char`` is one of ``$,*,.,[,\,^``

Note that the regular expression matcher is greedy, i.e., matches are attempted from left to right and, if two or more matches are possible starting at the same character, it selects the longest. 

********
Examples
********
.. http://docutils.sourceforge.net/docs/ref/rst/directives.html#id4        
.. csv-table:: 
    :header: 
    :widths: 20,70
    :delim: |


    ``‘abcdef’`` |        Matches ‘abcdef’.
    ``‘a*b’`` |        Matches zero or more ‘a’s followed by a single ‘b’. For example, ‘b’ or ‘aaaaab’.
    ``‘a\?b’``|        Matches ‘b’ or ‘ab’.
    ``‘a\+b\+’``|        Matches one or more ‘a’s followed by one or more ‘b’s: ‘ab’ is the shortest possible match, but other examples are ‘aaaab’ or ‘abbbbb’ or ‘aaaaaabbbbbbb’.
    ``‘.*’``, ``'.\+'`` |        These two both match all the characters in a string; however, the first matches every string (including the empty string), while the second matches only strings containing at least one character.
    ``‘^main.*(.*)’`` |        This matches a string starting with ‘main’, followed by an opening and closing parenthesis. The ‘n’, ‘(’ and ‘)’ need not be adjacent.
    ``‘^#’`` |        This matches a string beginning with ‘#’.
    ``‘\\\\$’`` |        This matches a string ending with a single backslash. The regexp contains two backslashes for escaping.
    ``‘\\$’`` |        Instead, this matches a string consisting of a single dollar sign, because it is escaped.
    ``‘[a-zA-Z0-9]’``| In the C locale, this matches any ASCII letters or digits.
    ``‘[^ tab]\+’``| (Here tab stands for a single tab character.) This matches a string of one or more characters, none of which is a space or a tab. Usually this means a word.
    ``‘^\(\(.*\)\)\n\1$’``|        This matches a string consisting of two equal substrings separated by a newline.
    ``‘.\{9\}A$’`` |        This matches nine characters followed by an ‘A’.
    ``‘^.\{15\}A’`` |        This matches the start of a string that contains 16 characters, the last of which is an ‘A’. 

####################################
Common Commands: Often used commands
####################################
.. http://docutils.sourceforge.net/docs/ref/rst/directives.html#id4        
.. csv-table:: 
    :header: a,description
    :widths: 20,70
    :delim: |

    q [exit-code] |   Exit sed without processing any more commands or input. Note that the current pattern space is printed if auto-print is not disabled with the ``-n`` options.  (This command only accepts a single address)
    d [delete] | Delete the pattern space; immediately start next cycle.
    p [print] | Print out the pattern space (to the standard output). This command is usually only used in conjunction with the -n command-line option.
    n | If auto-print is not disabled (so ``-n`` is NOT used), **print the pattern space**, then, regardless, replace the pattern space with the next line of input. If there is no more input then sed exits without processing any more commands.
    { commands } |        A group of commands may be enclosed between { and } characters. This is particularly useful when you want a group of commands to be triggered by a single address (or address-range) match. 


#######################################
The "s" Command: sed's Swiss Army Knife
#######################################
The syntax of the ``s`` (as in substitute) command is ``‘s/regexp/replacement/flags’``.

- The ``s`` command is probably the most important in sed and has a lot of different options

***********
replacement
***********
- ``replacement`` can contain ``\n`` references (n is number from 1 to 9), which refer to the portion of the match
- ``replacement`` can contain unescaped & chars which reference the whole-matched portion of the pattern space.

- You can include a special sequence made of a backslash and one of the letters ``L, l, U, u, or E``. 
- To include a literal ``\, &``, or ``newline`` in the final replacement, be sure to precede the desired ``\, &``, or ``newline`` in the replacement with a ``\``. 

.. http://docutils.sourceforge.net/docs/ref/rst/directives.html#id4        
.. csv-table:: 
    :header: 
    :widths: 20,70
    :delim: |
    
    ``\L`` |  Turn the replacement to lowercase until a ``\U`` or ``\E`` is found,
    ``\l`` |  Turn the next character to lowercase,
    ``\U`` |  Turn the replacement to uppercase until a ``\L`` or ``\E`` is found,
    ``\u`` |  Turn the next character to uppercase,
    ``\E`` |  Stop case conversion started by ``\L`` or ``\U``. 

To include a literal ``\, &``, or ``newline`` in the final replacement, be sure to precede the desired ``\, &``, or ``newline`` in the replacement with a ``\``. 

*****
flags
*****
The ``s`` command can be followed by **zero or more** of the following flags: 

.. http://docutils.sourceforge.net/docs/ref/rst/directives.html#id4        
.. csv-table:: 
    :header: 
    :widths: 20,70
    :delim: |


    ``g``  (global) | Apply the replacement to all matches to the regexp, not just the first.
    *number* | Only replace the *number*-th match of the regexp.
    ``p`` (print) | If the substitution was made, then print the new pattern space. Note: when both the ``p and e`` options are specified, the **ordering** of the two produces very different results. In general, ``ep`` (**evaluate then print**) is what you want, but operating the other way round can be useful for debugging.
    ``w file-name`` (write to file) | If the substitution was made, then write out the result to the named file. Two special values of file-name are supported: ``/dev/stderr``, which writes the result to the standard error, and ``/dev/stdout``, which writes to the standard output.1
    ``e`` (pipe) | This command allows one to pipe input from a shell command into pattern space. If a substitution was made, the command that is found in pattern space is executed and pattern space is replaced with its output. A trailing newline is suppressed; results are undefined if the command to be executed contains a nul character. 
    ``I``, ``i`` (case sensitive) | The I modifier to regular-expression matching makes sed match regexp in a case-insensitive manner.
    ``M``, ``m`` (multiline) | The M modifier to regular-expression matching is a GNU sed extension which causes ^ and $ to match respectively (in addition to the normal behavior) the empty string after a newline, and the empty string before a newline. 

#############################################
Other Commands: Less frequently used commands
#############################################
Though perhaps less frequently used than those in the previous section, some very small yet useful sed scripts can be built with these commands.

.. http://docutils.sourceforge.net/docs/ref/rst/directives.html#id4        
.. csv-table:: 
    :header: 
    :widths: 20,70
    :delim: |

    ``y/source-chars/dest-chars/`` |(The ``/`` characters may be uniformly replaced by any other single character within any given y command.) Transliterate any characters in the pattern space which match any of the source-chars with the corresponding character in dest-chars. Instances of the / (or whatever other character is used in its stead), ``\``, or newlines can appear in the source-chars or dest-chars lists, provide that each instance is escaped by a ``\``. The source-chars and dest-chars lists must contain the same number of characters (after de-escaping).
    ``a\``, ``text`` | Queue the lines of text which follow this command (each but the last ending with a ``\``, which are removed from the output) to be output at the end of the current cycle, or when the next input line is read. (this command accepts **two addresses**) Escape sequences in text are processed, so you should use ``\\`` in text to print a single backslash. As a GNU extension, if between the a and the newline there is other than a whitespace-\ sequence, then the text of this line, starting at the first non-whitespace character after the a, is taken as the first line of the text block. (This enables a simplification in scripting a one-line add.) This extension also works with the i and c commands. 
    ``i\`` ``text`` | Immediately output the lines of text which follow this command (each but the last ending with a ``\``, which are removed from the output). (this command accepts **two addresses**)
    ``c\`` ``text`` | Delete the lines matching the address or address-range, and output the lines of text which follow this command (each but the last ending with a ``\``, which are removed from the output) in place of the last line (or in place of each line, if no addresses were specified). A new cycle is started after this command is done, since the pattern space will have been deleted.
    ``=`` | Print out the current input line number (with a trailing newline) (this command accepts **two addresses**)
    ``l n`` | Print the pattern space in an unambiguous form: non-printable characters (and the \ character) are printed in C-style escaped form; long lines are split, with a trailing ``\`` character to indicate the split; the end of each line is marked with a $. n specifies the desired line-wrap length; a length of 0 (zero) means to never wrap long lines. If omitted, the default as specified on the command line is used. The n parameter is a GNU sed extension.
    ``r filename`` | Queue the contents of filename to be read and inserted into the output stream at the end of the current cycle, or when the next input line is read. Note that if filename cannot be read, it is treated as if it were an empty file, without any error indication. (this command accepts **two addresses**) As a GNU sed extension, the special value /dev/stdin is supported for the file name, which reads the contents of the standard input.
    ``w filename`` | Write the pattern space to filename. As a GNU sed extension, two special values of file-name are supported: /dev/stderr, which writes the result to the standard error, and /dev/stdout, which writes to the standard output.1 The file will be created (or truncated) before the first input line is read; all w commands (including instances of the w flag on successful s commands) which refer to the same filename are output without closing and reopening the file.
    ``D`` (delete) | If pattern space contains no newline, start a normal new cycle as if the d command was issued. Otherwise, delete text in the pattern space up to the first newline, and restart cycle with the resultant pattern space, without reading a new line of input.
    ``N`` (newline) | Add a newline to the pattern space, then append the next line of input to the pattern space. If there is no more input then sed exits without processing any more commands.
    ``P`` (print) | Print out the portion of the pattern space up to the first newline.
    ``h`` (replace) | Replace the contents of the hold space with the contents of the pattern space.
    ``H`` (append) | Append a newline to the contents of the hold space, and then append the contents of the pattern space to that of the hold space.
    ``g``  | Replace the contents of the pattern space with the contents of the hold space.
    ``G`` | Append a newline to the contents of the pattern space, and then append the contents of the hold space to that of the pattern space.
    ``x`` (exchange) | Exchange the contents of the hold and pattern spaces. 

############################################
Programming Commands: Commands for sed gurus
############################################
.. warning::
    
    In most cases, **use of these commands indicates that you are probably better off programming in something like awk or Perl**. But occasionally one is committed to sticking with sed, and these commands can enable one to write quite convoluted scripts. 

.. http://docutils.sourceforge.net/docs/ref/rst/directives.html#id4        
.. csv-table:: 
    :header: 
    :widths: 20,70
    :delim: |

    
    ``: label`` | [No addresses allowed.] Specify the location of label for branch commands. In all other respects, a no-op.
    ``b label`` | Unconditionally branch to label. The label may be omitted, in which case the next cycle is started.
    ``t label`` | Branch to label only if there has been a successful substitution since the last input line was read or conditional branch was taken. The label may be omitted, in which case the next cycle is started. 

























