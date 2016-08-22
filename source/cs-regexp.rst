.. _regexp:

regular expressions
"""""""""""""""""""

.. contents:: `Table of contents`
   :depth: 2
   :local:

**Regular expression references**

Two best tutorials

- http://www.regular-expressions.info/tutorial.html
- http://www.rexegg.com/regex-quickstart.html

Best python tutorial

- http://www.tutorialspoint.com/python/python_reg_expressions.htm

- quantifiers cheat sheet (a good review of **greedy vs lazy**)
  
  - http://www.rexegg.com/regex-quantifiers.html#cheat_sheet

| Sublime Text uses the Perl Compatible Regular Expressions (PCRE) engine from the Boost library to power regular expressions in search panels.

#########
Overflows
#########
***********************
Use Perl engine in bash
***********************
- http://unix.stackexchange.com/questions/84477/forcing-bash-to-use-perl-regex-engine


*********************
Negate specific word?
*********************
- http://stackoverflow.com/questions/1240275/how-to-negate-specific-word-in-regex
- http://stackoverflow.com/questions/899422/regular-expression-for-a-string-that-does-not-start-with-a-sequence

.. code-block:: bash

    # i want to negate word bar, but ``[^bar]`` won't work (works char-wise)

    # S.O.'s answer: use negative lookahead (hmmm...doesn't wrok in my regex engine in bash...flag issue?
    grep -P '^(?!.*bar).*$'

    # avoid line containing 'age'
    find . | grep  '^(?!.*age).*$' | sort

    # note: i can't add comment at linebreaks like below; below just for my own help
    find . -maxdepth 1 \
        | sed 's/\.\///g' \# clean up "./" 
        | sort
        | grep -P '(?<!^age).+age' # get line with "age", but doesn't start with "age"
    find . -maxdepth 1 | sed 's/\.\///g' | sort | grep -P '(?<!^age).+age'




###########
Sublimetext
###########
https://github.com/dmikalova/sublime-cheat-sheets/blob/master/cheat-sheets/Regular%20Expressions.cheatsheet

- http://docs.sublimetext.info/en/latest/search_and_replace/search_and_replace_overview.html

    Sublime Text uses the **Perl Compatible Regular Expressions (PCRE) engine** from  the **Boost library** to power regular expressions in search panels.

- http://www.boost.org/doc/libs/1_61_0/libs/regex/doc/html/boost_regex/syntax/perl_syntax.html
- http://www.boost.org/doc/libs/1_61_0/libs/regex/doc/html/boost_regex/format/perl_format.html

######################################
Regular expression (regexp) for python
######################################
**References**

- https://docs.python.org/2/howto/regex.html
- http://www.tutorialspoint.com/python/python_reg_expressions.htm
  
  - great to use as cheatsheets

***********************
Basic functions/modules
***********************
https://docs.python.org/2/howto/regex.html#performing-matches

.. csv-table:: 
    :header: methods, purpose
    :widths: 20,70
    :delim: |

    |Performing matches/searches
    search() |    Scan through a string, looking for any location where this RE matches.
    findall() |   Find all substrings where the RE matches, and returns them as a list.
    finditer() |  Find all substrings where the RE matches, and returns them as an iterator.
    |Grouping
    group() |     Return the string matched by the RE
    start() |     Return the starting position of the match
    end()   | Return the ending position of the match
    span()  | Return a tuple containing the (start, end) positions of the match
    |Modifying strings
    split()  |   Split the string into a list, splitting it wherever the RE matches
    sub() |  Find all substrings where the RE matches, and replace them with a different string
    subn() | Does the same thing as sub(), but returns the new string and the number of replacements

.. code-block:: python
    :linenos:

    p = re.compile('[a-z]+')
    m = p.match('tempo')    

    >>> m.group()
    'tempo'
    >>> m.start(), m.end()
    (0, 5)
    >>> m.span()
    (0, 5)

    >>> m = p.search('::: message')
    >>> m.group()
    'message'
    >>> m.span()
    (4, 11)

    >>> p = re.compile('\d+')
    >>> p.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping')
    ['12', '11', '10']

    >>> iterator = p.finditer('12 drummers drumming, 11 ... 10 ...')
    >>> for match in iterator:
    ...     print match.span()
    ...
    (0, 2)
    (22, 24)
    (29, 31)

    # if match is not found, ``None`` is returned, so can use ``if-else`` clause
    p = re.compile( ... )
    m = p.match( 'string goes here' )
    if m:
        print 'Match found: ', m.group()
    else:
        print 'No match'

*****************
Splitting strings
*****************
- use of **capturing paranthesis** to obtain the splitted portion that normally gets dropped

.. code-block:: python
    :linenos:

    >>> p = re.compile(r'\W+')
    >>> p.split('This is a test, short and sweet, of split().')
    ['This', 'is', 'a', 'test', 'short', 'and', 'sweet', 'of', 'split', '']
    >>> p.split('This is a test, short and sweet, of split().', 3)
    ['This', 'is', 'a', 'test, short and sweet, of split().']

    >>> p = re.compile(r'\W+')
    >>> p2 = re.compile(r'(\W+)')
    >>> p.split('This... is a test.')
    ['This', 'is', 'a', 'test', '']


    #If capturing parentheses are used in the RE, then their values are also returned as part of the list
    >>> p2.split('This... is a test.')
    ['This', '... ', 'is', ' ', 'a', ' ', 'test', '.', '']


    >>> re.split('[\W]+', 'Words, words, words.')
    ['Words', 'words', 'words', '']
    >>> re.split('([\W]+)', 'Words, words, words.')
    ['Words', ', ', 'words', ', ', 'words', '.', '']
    >>> re.split('[\W]+', 'Words, words, words.', 1)
    ['Words', 'words, words.']

***************************
Search and replace with sub
***************************
.. code-block:: python
    :linenos:

    >>> p = re.compile('(blue|white|red)')
    >>> p.sub('colour', 'blue socks and red shoes')
    'colour socks and colour shoes'
    >>> p.sub('colour', 'blue socks and red shoes', count=1)
    'colour socks and red shoes'

    # subn() method does the same work, but returns a 2-tuple
    >>> p = re.compile('(blue|white|red)')
    >>> p.subn('colour', 'blue socks and red shoes')
    ('colour socks and colour shoes', 2)
    >>> p.subn('colour', 'no colours at all')
    ('no colours at all', 0)


    >>> p = re.compile('section{ (?P<name> [^}]* ) }', re.VERBOSE)
    >>> p.sub(r'subsection{\1}','section{First}')
    'subsection{First}'
    >>> p.sub(r'subsection{\g<1>}','section{First}')
    'subsection{First}'
    >>> p.sub(r'subsection{\g<name>}','section{First}')
    'subsection{First}'

**Advanced**

- ``\g<number>`` is better than ``\number`` since it makes it unambiguous with multiple digits

  - eg: ``\g<2>0`` vs ``\20``, which is reference to group 20


.. code-block:: python
    :linenos:

    # This example matches the word section followed by a string enclosed in {, }, and changes section to subsection:
    >>> p = re.compile('section{ ( [^}]* ) }', re.VERBOSE)
    >>> p.sub(r'subsection{\1}','section{First} section{second}')
    'subsection{First} subsection{second}'

    >>> p = re.compile('section{ (?P<name> [^}]* ) }', re.VERBOSE)
    >>> p.sub(r'subsection{\1}','section{First}')
    'subsection{First}'
    >>> p.sub(r'subsection{\g<1>}','section{First}')
    'subsection{First}'
    >>> p.sub(r'subsection{\g<name>}','section{First}')
    'subsection{First}'

    # replace decimal with hex
    >>> def hexrepl(match):
    ...     "Return the hex string for a decimal number"
    ...     value = int(match.group())
    ...     return hex(value)
    ...
    >>> p = re.compile(r'\d+')
    >>> p.sub(hexrepl, 'Call 65490 for printing, 49152 for user code.')
    'Call 0xffd2 for printing, 0xc000 for user code.'


*****************
Compilation flags
*****************
https://docs.python.org/2/howto/regex.html#compilation-flags

.. csv-table:: 
    :header: Flag, Meaning
    :widths: 20,70
    :delim: |

    DOTALL, S   | Make . match any character, including newlines
    IGNORECASE, I |  Do case-insensitive matches
    LOCALE, L |  Do a locale-aware match
    MULTILINE, M  |  Multi-line matching, affecting ^ and $
    VERBOSE, X | Enable verbose REs, which can be organized more cleanly and understandably.
    UNICODE, U | Makes several escapes like \w, \b, \s and \d dependent on the Unicode character database.

*******************
Greedy vs nongreedy
*******************
- nongreedy qualifiers: ``*?, +?, ??, or {m,n}?,``

.. code-block:: python
    :linenos:

    >>> s = '<html><head><title>Title</title>'

    >>> # greedy
    >>> print re.match('<.*>', s).group()
    <html><head><title>Title</title>

    >>> # non-greedy with the ? qualifier
    >>> print re.match('<.*?>', s).group()
        <html>

****************************************
Improve readibility with re.Verbose flag
****************************************
https://docs.python.org/2/howto/regex.html#using-re-verbose

  The re.VERBOSE flag has several effects. Whitespace in the regular expression that isn’t inside a character class is ignored. This means that an expression such as dog | cat is equivalent to the less readable dog|cat, but [a b] will still match the characters 'a', 'b', or a space. In addition, you can also put comments inside a RE; comments extend from a # character to the next newline. When used with triple-quoted strings, this enables REs to be formatted more neatly:

.. code-block:: python
    :linenos:

    pat = re.compile(r"""
     \s*                 # Skip leading whitespace
     (?P<header>[^:]+)   # Header name
     \s* :               # Whitespace, and a colon
     (?P<value>.*?)      # The header's value -- *? used to
                         # lose the following trailing whitespace
     \s*$                # Trailing whitespace to end-of-line
    """, re.VERBOSE)

    # above is far more readable than:
    pat = re.compile(r"\s*(?P<header>[^:]+)\s*:(?P<value>.*?)\s*$")


Another example

.. code-block:: python
    :linenos:

    charref = re.compile(r"""
     &[#]                # Start of a numeric entity reference
     (
         0[0-7]+         # Octal form
       | [0-9]+          # Decimal form
       | x[0-9a-fA-F]+   # Hexadecimal form
     )
     ;                   # Trailing semicolon
    """, re.VERBOSE)


    # w/o Verbose, you get:
    charref = re.compile("&#(0[0-7]+"
                         "|[0-9]+"
                         "|x[0-9a-fA-F]+);")


************
Named groups
************
- ``(?P<name>...)`` defines a **named group**, 
- ``(?P=name)`` is a **backreference** to a named group
- ``(?:...)`` is particularly useful when modifying an existing pattern, since you can add new groups without changing how all the other groups are numbered

.. code-block:: python
    :linenos:

    >>> m = re.match("([abc])+", "abc")
    >>> m.groups()
    ('c',)
    >>> m = re.match("(?:[abc])+", "abc")
    >>> m.groups()
    ()


    #=== named group demo ===#
    >>> p = re.compile(r'(?P<word>\b\w+\b)')
    >>> m = p.search( '(((( Lots of punctuation )))' ))
    >>> m.group('word') # named group
    'Lots'
    >>> m.group(1)      # group by index position
    'Lots'

    InternalDate = re.compile(r'INTERNALDATE "'
            r'(?P<day>[ 123][0-9])-(?P<mon>[A-Z][a-z][a-z])-'
            r'(?P<year>[0-9][0-9][0-9][0-9])'
            r' (?P<hour>[0-9][0-9]):(?P<min>[0-9][0-9]):(?P<sec>[0-9][0-9])'
            r' (?P<zonen>[-+])(?P<zoneh>[0-9][0-9])(?P<zonem>[0-9][0-9])'
            r'"')

    # use of back-reference
    >>> p = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')
    >>> p.search('Paris in the the spring').group()
    'the the'

*******************
Lookahed assertions
*******************
- ``(?=...)`` Positive lookahead assertion.

  - successfully matches at the current location
- ``(?!...)`` Negative lookahead assertion
  
  - succeeds if the contained expression **doesn’t** match

*****************
Bunch of examples
*****************
.. code-block:: python
    :linenos:

    # (ab)* will match zero or more repetitions of ab.
    p = re.compile('(ab)*')
    print p.match('ababababab').span()
    >>> (0, 10)

    phone = "2004-959-559 # This is Phone Number"
    
    # Delete Python-style comments (empty replace string for deletion)
    num = re.sub(r'#.*$', "", phone)
    print "Phone Num : ", num
    >>> Phone Num :  2004-959-559

    # Remove anything other than digits
    num = re.sub(r'\D', "", phone)    
    print "Phone Num : ", num
    >>> Phone Num :  2004959559