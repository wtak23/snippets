rst
"""

.. contents:: `Contents`
   :depth: 2
   :local:

############
Best lookups
############
.. note:: 

  - Great summary of useful directives: http://www.sphinx-doc.org/en/stable/rest.html#directives
  - Predefined **substitutions** in Sphinx (`link <http://www.sphinx-doc.org/en/stable/markup/inline.html#substitutions>`__) ``|release|, |version|,|today|``



- http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html
  
  - a bit difficult to navigate, but the most comprehensive
- http://docutils.sourceforge.net/docs/ref/rst/directives.html  
- http://docutils.sourceforge.net/docs/ref/rst/roles.html
- http://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html
- http://rest-sphinx-memo.readthedocs.io/en/latest/index.html
- From Sphinx

  - http://www.sphinx-doc.org/en/stable/contents.html
  - `reStructuredText Primer <http://www.sphinx-doc.org/en/stable/rest.html>`__

#############################
Important external directives
#############################
- http://matplotlib.org/sampledoc/ipython_directive.html
- ..

################
Random overflows
################

**********
Get colors
**********
- http://stackoverflow.com/questions/4669689/how-to-use-color-in-text-with-restructured-text-rst2html-py-or-how-to-insert-h

Add this in the rst file (this definition must come before usage. cross-file support doesn't seem to exit)::

  .. raw:: html

      <style> .red {color:red} </style>

  .. role:: red

  Now you can use :red:`the role like` anywhere :red:`else`

.. raw:: html

    <style> .red {color:red} </style>

.. role:: red

Now you can use :red:`the role like` anywhere :red:`else`



************************
Add links without labels
************************
- http://stackoverflow.com/questions/5464627/how-to-have-same-text-in-two-links-with-restructured-text
- https://www.google.com/search?q=Named+hyperlink+references#q=rst+Named+hyperlink+references
- http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#hyperlink-references
- http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#anonymous-hyperlinks

Use double underscores

.. code-block:: rst

    .. To circumvent it, use anonymous hyperlink references with double underscores:

    `Foo <http://example.org>`__
    `Foo <http://example.com>`__


##########################
Link is kinda confusing...
##########################
- http://rest-sphinx-memo.readthedocs.io/en/latest/ReST.html#cross-references
- http://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html#internal-and-external-links

.. code-block:: rst

    - A link to `Sphinx Home`_ in **citation style**.
    - **In-line versions** are `Sphinx Home <http://sphinx.pocoo.org>`_

    .. _Sphinx Home: http://sphinx.pocoo.org

- A link to `Sphinx Home`_ in citation style.
- In-line versions are `Sphinx Home <http://sphinx.pocoo.org>`_

.. _Sphinx Home: http://sphinx.pocoo.org

****
hmmm
****
.. code-block:: rst

    - SQLite - `core functions <https://www.sqlite.org/>`_
    - SQLite - `date/time functions <https://www.sqlite.org/lang_datefunc.html>`_

    `core functions`_

- SQLite - `core functions <https://www.sqlite.org/>`_
- SQLite - `date/time functions <https://www.sqlite.org/lang_datefunc.html>`_

-  `core functions`_

Hmm...sadly this is restrictive in the sense that I cannot change the
text that appears...(ah, see below to get what i wanted :)

*************************
Ah, finally what i wanted
*************************
From http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#hyperlink-references

- Turned out i need to add another underscore inside ``<>`` bracket (see line 3,7 below)
- so you'll get ``_>_`` syntax at the end

.. code-block:: rst
    :linenos:
    :emphasize-lines: 3,7

    See the `Python home page <http://www.python.org>`_ for info.

    This `link <Python home page_>`_ is an alias to the link above.

    `Another test <http://www.sphinx-doc.org/en/stable/markup/inline.html>`_

    `This text appears differently but same link :) <Another test_>`_

See the `Python home page <http://www.python.org>`_ for info.

This `link <Python home page_>`_ is an alias to the link above.

`Another test <http://www.sphinx-doc.org/en/stable/markup/inline.html>`_

`This text appears differently but same link :) <Another test_>`_

########
csv-demo
########
From the url

.. http://docutils.sourceforge.net/docs/ref/rst/directives.html#id4        
.. csv-table::
    :header-rows: 1
    :url: https://raw.githubusercontent.com/mwaskom/seaborn-data/master/car_crashes.csv


######################################
Lookups (old, may remove this section)
######################################
http://thomas-cokelaer.info/tutorials/sphinx/docstring_python.html

http://www.sphinx-doc.org/en/stable/contents.html - Main TOC in the Sphinx-DOC

Ones I lookup frequently

http://www.sphinx-doc.org/en/stable/ext/autodoc.html

- http://www.sphinx-doc.org/en/stable/tutorial.html (global refresher)
- http://www.sphinx-doc.org/en/stable/glossary.html (to sort out jargons used in the doc)
- http://www.sphinx-doc.org/en/stable/extensions.html
- http://www.sphinx-doc.org/en/stable/markup/index.html (rst-syntax only defined/unique in Sphinx)
- http://www.sphinx-doc.org/en/stable/config.html (``conf.py`` file info)
- http://www.sphinx-doc.org/en/stable/theming.html (examples of themes)
- **reStructuredText Primer** http://www.sphinx-doc.org/en/stable/rest.html (helpful refresher on rst syntax)

******************************************
References for rst in general (non-sphinx)
******************************************
- http://docutils.sourceforge.net/docs/user/rst/quickref.html
- Roles: http://docutils.sourceforge.net/docs/ref/rst/roles.html
- Directives: http://docutils.sourceforge.net/docs/ref/rst/directives.html

  - (a good summary of useful ones) http://www.sphinx-doc.org/en/stable/rest.html#directives
- http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html

***************
Autodoc related
***************
- http://www.sphinx-doc.org/en/stable/ext/autodoc.html
- http://thomas-cokelaer.info/tutorials/sphinx/docstring_python.html