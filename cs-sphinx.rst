`[Parent Directory] <./>`_


.. contents:: **Table of Contents**
    :depth: 3

.. sectnum::    
    :start: 1    


#######
Lookups
#######
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

*******************************************************************************
References for rst in general (non-sphinx)
*******************************************************************************
- http://docutils.sourceforge.net/docs/user/rst/quickref.html
- Roles: http://docutils.sourceforge.net/docs/ref/rst/roles.html
- Directives: http://docutils.sourceforge.net/docs/ref/rst/directives.html

  - (a good summary of useful ones) http://www.sphinx-doc.org/en/stable/rest.html#directives
- http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html

###############
Autodoc related
###############
- http://www.sphinx-doc.org/en/stable/ext/autodoc.html
- http://thomas-cokelaer.info/tutorials/sphinx/docstring_python.html


*********************
Main directives
*********************
List

.. code-block:: rst

    .. automodule::
    .. autoclass::
    .. autoexception::


    .. These work exactly like autoclass etc., but do not offer the options used for automatic member documentation.
    .. autofunction::
    .. autodata::
    .. automethod::
    .. autoattribute::

        

Usage 

.. code:: rst

    .. recursive autodoc all module members
    .. automodule:: noodle
       :members:

    .. only include the docstring of the object itself
    .. autoclass:: Noodle

    .. recursively document all non-private member functions and properties
    .. autoclass:: Noodle
       :members:

    .. You can also give an explicit list of members; only these will then be documented
    .. autoclass:: Noodle
       :members: eat, slurp


*********************
directive options
*********************
Summary

.. code-block:: bash

    :members:            # recursively include all member functions (or explicitly send member function names)
    :undoc-members:      # include member functions without docstring (default ignores them)
    :private-members:    # include member function that begin with underscore (like _func)
    :special-members:    # include member function of the form __special__
    :inherited-members:  # include inherited member functions

Usage

.. code-block:: rst

    .. include non-documented member functions (default ignores it)
    .. autoclass:: Noodle
       :members:
       :undoc-members


    .. include those with special method-names like __method__
    .. autoclass:: my.Class
       :members:
       :private-members:
       :special-members:


    .. include mix of autodoc and manualdoc
    .. autoclass:: Noodle
       :members: eat, slurp

       .. method:: boil(time=10)

          Boil the noodle *time* minutes.

My usage example
================
- https://tedboy.github.io/pyspark_doc/pyspark.ml.html
- https://tedboy.github.io/pyspark_doc/sources/pyspark.ml.txt


.. code-block:: rst

    .. automodule:: pyspark.ml
        :members:
        :undoc-members:
        :inherited-members:




****************************************************************************
autosummary (my notes highly incomplete...better to look at the doc page)
****************************************************************************
http://www.sphinx-doc.org/en/stable/ext/autosummary.html

- Pandas uses this in their api page (see below)
- This is especially useful when your docstrings are long and detailed, and 
  **putting each one of them on a separate page** makes them easier to read.
- The ``sphinx.ext.autosummary`` extension does this in two parts:

  #. There is an autosummary directive for generating summary listings that 
     contain **links to the documented items**, and short summary blurbs extracted 
     from their docstrings.
  #. **Optionally**, the convenience script sphinx-autogen or the new 
     ``autosummary_generate config`` value can be used to 
     **generate short “stub” files** for the entries listed in the 
     autosummary directives. These files by default contain only the 
     corresponding sphinx.ext.autodoc directive, but can be customized 
     with templates.

- Don't forget to include it in ``extensions`` list in ``conf.py``

.. code-block:: python

    extensions = ['sphinx.ext.autodoc',
                  'sphinx.ext.autosummary',]


autosummary directive
=====================
``.. autosummary::`` inserts a table that contains links to documented items, 
and a short summary blurb (the first sentence of the docstring) for each of them.

The autosummary directive can also optionally serve as a toctree entry for the included items. Optionally, stub .rst files 
for these items can also be automatically generated.

options
========
By default, no toctree is generated:

.. code-block:: rst

    .. currentmodule:: sphinx

    .. autosummary::

       environment.BuildEnvironment
       util.relative_uri


**autosummary table** also serves as a toctree entry:

.. code-block:: rst

    .. autosummary::
       :toctree: DIRNAME

       sphinx.environment.BuildEnvironment
       sphinx.util.relative_uri

Hide function signatures

.. code-block:: rst

    .. autosummary::
       :nosignatures:

       sphinx.environment.BuildEnvironment
       sphinx.util.relative_uri


pandas example
==============
**pandas** 

- http://pandas.pydata.org/pandas-docs/stable/api.html
- https://raw.githubusercontent.com/pydata/pandas/master/doc/source/api.rst
- https://github.com/pydata/pandas/tree/master/doc/source


Below auto-generates html files in directory ``generated`` via the option ``:toctree: generated/``

- http://pandas.pydata.org/pandas-docs/stable/api.html
- http://pandas.pydata.org/pandas-docs/stable/**generated**/pandas.read_excel.html

.. code-block:: rst

    JSON
    ~~~~

    .. autosummary::
       :toctree: generated/

       read_json

    .. currentmodule:: pandas.io.json

    .. autosummary::
       :toctree: generated/

       json_normalize

    .. currentmodule:: pandas

    HTML
    ~~~~

    .. autosummary::
       :toctree: generated/

       read_html


###############
conf.py related
###############
- http://www.sphinx-doc.org/en/stable/config.html
- http://www.sphinx-doc.org/en/stable/theming.html (examples of html themes)

.. code-block:: python

    html_theme = "classic"
    html_theme_options = {
        'stickysidebar': True,
    }

***************
Example conf.py
***************
See https://github.com/takwatanabe2004/snippets/blob/master/cs-rst.rst#examples-conf-py-and-github

- Pandas: https://github.com/pydata/pandas/blob/master/doc/source/conf.py
- https://github.com/cokelaer/sphinx_tutorial/blob/master/source/conf.py
- https://github.com/sphinx-doc/sphinx/blob/master/doc/conf.py
- https://github.com/marinkaz/nimfa/blob/master/docs/source/conf.py
- https://github.com/matplotlib/matplotlib/blob/master/doc/conf.py

Mine

.. code-block:: bash

    subl /home/takanori/Dropbox/git/tedboy/pyspark_docs/conf.py
    subl /home/takanori/Dropbox/git/tedboy/bs4doc_source/source/conf.py

**********
extensions
**********
- **extension** = a Python module that provides additional features for Sphinx projects
- http://www.sphinx-doc.org/en/stable/extensions.html

In ``conf.py``: 

.. code-block:: python

    extensions = [
        'sphinx.ext.autodoc',
        'sphinx.ext.viewcode',
        'epytext',
        'sphinx.ext.mathjax',
    ]

Ones i care about (including 3rd party...keep adding to the list as i find new ones)
=======================================
.. code-block:: python

    import sphinx

    # include fullpath to 3rd party ones (see packages like pandas,sklearn,mpl for example conf.py that does this)
    sys.path.append(os.path.abspath('sphinxext'))

    # include full list
    extensions = [# built-ins
                  'sphinx.ext.autodoc',
                  'sphinx.ext.autosummary',
                  'sphinx.ext.doctest',
                  'sphinx.ext.extlinks',
                  'sphinx.ext.todo',
                  'sphinx.ext.coverage',
                  'sphinx.ext.pngmath',
                  'sphinx.ext.ifconfig',
                  # 3rd parties
                  'numpydoc', # used to parse numpy-style docstrings for autodoc
                  'ipython_sphinxext.ipython_directive',
                  'ipython_sphinxext.ipython_console_highlighting',
                  'sphinx.ext.intersphinx',
                  ]



Examples
========
matplotlib: https://github.com/matplotlib/matplotlib/tree/master/doc

.. code-block:: python

    extensions = ['matplotlib.sphinxext.mathmpl', 'sphinxext.math_symbol_table',
                  'sphinx.ext.autodoc', 'matplotlib.sphinxext.only_directives',
                  'sphinx.ext.doctest', 'sphinx.ext.autosummary',
                  'matplotlib.sphinxext.plot_directive',
                  'sphinx.ext.inheritance_diagram',
                  'sphinxext.gen_gallery', 'sphinxext.gen_rst',
                  'sphinxext.github',
                  'numpydoc']


scipy-lecture-note: https://github.com/scipy-lectures/scipy-lecture-notes

Ensure `sphinxext <https://github.com/scipy-lectures/scipy-lecture-notes/tree/master/sphinxext>`_ dir is added to local path

.. code-block:: python

    sys.path.append(os.path.abspath('sphinxext'))
    extensions = [
            'gen_rst',
            'sphinx.ext.autodoc',
            'sphinx.ext.doctest',
            #'matplotlib.sphinxext.plot_directive',
            'plot_directive',
            'only_directives',
            'ipython_console_highlighting',
            #'matplotlib.sphinxext.only_directives',
            'sphinx.ext.pngmath',
            'sphinx.ext.intersphinx',
            'sphinx.ext.extlinks',
    ]

Scikit: https://github.com/scikit-learn/scikit-learn/tree/master/doc

.. code-block:: python

    sys.path.insert(0, os.path.abspath('sphinxext'))
    extensions = ['gen_rst',
                  'sphinx.ext.autodoc', 'sphinx.ext.autosummary',
                  'sphinx.ext.pngmath', 'numpy_ext.numpydoc',
                  'sphinx.ext.linkcode', 'sphinx.ext.doctest',
                  ]

Pandas: https://github.com/pydata/pandas/blob/master/doc/source/conf.py

.. code-block:: python

    sys.path.insert(0, os.path.abspath('../sphinxext'))

    sys.path.extend([

        # numpy standard doc extensions
        os.path.join(os.path.dirname(__file__),
                     '..', '../..',
                     'sphinxext')

    ])

    # -- General configuration -----------------------------------------------

    # Add any Sphinx extension module names here, as strings. They can be extensions
    # coming with Sphinx (named 'sphinx.ext.*') or your custom ones.  sphinxext.

    extensions = ['sphinx.ext.autodoc',
                  'sphinx.ext.autosummary',
                  'sphinx.ext.doctest',
                  'sphinx.ext.extlinks',
                  'sphinx.ext.todo',
                  'numpydoc', # used to parse numpy-style docstrings for autodoc
                  'ipython_sphinxext.ipython_directive',
                  'ipython_sphinxext.ipython_console_highlighting',
                  'sphinx.ext.intersphinx',
                  'sphinx.ext.coverage',
                  'sphinx.ext.pngmath',
                  'sphinx.ext.ifconfig',
                  ]

Sphinx built-in
================
.. code-block:: bash

    sphinx.ext.autodoc # Include documentation from docstrings
    sphinx.ext.autosectionlabel # Allow reference sections using its title
    sphinx.ext.autosummary # Generate autodoc summaries
    sphinx.ext.mathjax # Render math via JavaScript
    sphinx.ext.doctest – Test snippets in the documentation


3rd party extensions
=====================
ensure you add it to ``sys.path`` in the ``conf.py`` file

.. code-block:: python

    import sys, os
    sys.path.append(os.path.abspath('exts'))
    extensions = ['foo']


*****************************************
rtd theme (one of my favorite html-theme)
*****************************************

To see theme options available in rtd, open:

.. code-block:: bash

    $ cat /home/takanori/.local/lib/python2.7/site-packages/sphinx_rtd_theme-0.1.10a0-py2.7.egg/sphinx_rtd_theme/theme.conf

    [theme]
    inherit = basic
    stylesheet = css/theme.css

    [options]
    typekit_id = hiw1hhg
    analytics_id = 
    sticky_navigation = False
    logo_only =
    collapse_navigation = False
    display_version = True
    navigation_depth = 4

So in ``conf.py``, we can do something like this:

.. code-block:: python

    html_theme = "sphinx_rtd_theme"

    # Theme options are theme-specific and customize the look and feel of a theme
    # further.  For a list of options available for each theme, see the
    # documentation.

    #https://github.com/snide/sphinx_rtd_theme
    html_theme_options = {
        'collapse_navigation': False,
        'display_version': False,
        'navigation_depth': 4,
    }


####################################################
Functions I use frequently (non-autodoc ones)
####################################################
By **function**, I mean roles/directives.

Stuffs in this section mostly from http://www.sphinx-doc.org/en/stable/markup/index.html

*******
toctree
*******
http://www.sphinx-doc.org/en/stable/markup/toctree.html

`Usage <https://tedboy.github.io/pyspark_doc/sources/pyspark.ml.txt>`_

.. code-block:: bash

    .. toctree::
       :maxdepth: 1
       :numbered:

       # these are .rst file names (w/o the extensions)
       pyspark.ml.param
       pyspark.ml.feature
       pyspark.ml.classification
       pyspark.ml.clustering

****
Code
****
http://www.sphinx-doc.org/en/stable/markup/code.html

.. code-block:: rst

    # This will produce line numbers for all code blocks longer than five lines.
    .. highlight:: python
       :linenothreshold: 5

    .. code-block:: ruby
       :linenos:

    # emphasize particular lines
    .. code-block:: python
       :emphasize-lines: 3,5

Literal includes (include code from external file)
==================================================
.. code-block:: rst

    .. literalinclude:: example.py

    .. literalinclude:: example.rb
       :language: ruby
       :emphasize-lines: 12,15-18
       :linenos:

    # specify parts of file (for a Python module, you can selection class/function/method via the :pyobject: option
    .. literalinclude:: example.py
       :pyobject: Timer.start

    # specify line-numbers to include (i think scikit's tutorial use this often)
    .. literalinclude:: example.py
       :lines: 1,3,5-10,20-

    # show diffs between files
    .. literalinclude:: example.py
       :diff: example.py.orig

    # can specify encoding
    .. literalinclude:: example.py
       :encoding: latin-1

******************************
Python directives and roles
******************************
**Domain** = a collection of markup (reStructuredText directives and roles) to describe and link to objects belonging together, e.g. elements of a programming language. 

http://www.sphinx-doc.org/en/stable/domains.html

Directives
==========
http://www.sphinx-doc.org/en/stable/domains.html#cross-referencing-python-objects

.. code-block:: rst

    .. default-domain:: python
    .. module:: name
    .. currentmodule:: name
    .. function:: name
    .. class:: name
    .. attribute:: name
    .. method:: name

Example

.. code-block:: rst

    .. function:: foo(x)
                  foo(y, z)
       :module: some.module.name

       Return a line of text input from the user.

roles       
==========
- http://www.sphinx-doc.org/en/stable/domains.html#cross-referencing-python-objects
- Handy for cross-referencing Python objects (also gives hyperlinks if a matching identifier is found)

.. code-block:: bash

    :mod:
    :func:`function_name`
    :class:`class_name`
    :meth:  # reference a method of an object 
    :attr:  # reference a attribute of an object 
    :exc:  # reference an exception

Info field
==========
- I'll probably never use this, but know it exists
- See how below will render at: http://www.sphinx-doc.org/en/stable/domains.html#info-field-lists

.. code-block:: rst

    .. function:: send_message(sender, recipient, message_body, [priority=1])

       Send a message to a recipient

       :param str sender: The person sending the message
       :param str recipient: The recipient of the message
       :param str message_body: The body of the message
       :param priority: The priority of the message, can be a number 1-5
       :type priority: integer or None
       :return: the message id
       :rtype: int
       :raises ValueError: if the message_body exceeds 160 characters
       :raises TypeError: if the message_body is not a basestring


********************************************************
inline markups (mostly for cross-referencing via :ref:)
********************************************************
http://www.sphinx-doc.org/en/stable/markup/inline.html

There are bunch of them on the above link, but I rarely used them... ``:ref:`` 
is pretty much all i use here...

.. code-block:: rst

    :doc: # cross reference documents...I never used or tried
    :download:

    See :download:`this example script <../example.py>`.

    :numref: # link to the specified figures...never used....


ref
==============
Beauty of ``:ref:`` is that it works across files!

Idea: 

- add ``.. _ref.labelname:`` before a section title (notice the underscore)
- reference them via ``:ref:`ref.labelname``` (notice **no** underscore)


.. code-block:: rst

    .. _my-reference-label:

    Section to cross-reference
    --------------------------
    This is the text of the section.I see :ref:`my-reference-label`.

Works with figures too!

.. code-block:: rst

    .. _my-figure:

    .. figure:: whatever

       Figure caption

Labels that aren’t placed before a section title can still be referenced to, 
but you must give the link an explicit title, using this syntax: 
``:ref:`Link title <label-name>`.`` (however, this never worked for me so far...)

Example usage
==============
- See how ``.. _ml:`` is used right before the section name?
- Now I can reference them and hyperlink them via :ref:`ml`

  - https://tedboy.github.io/pyspark_doc/pyspark.ml.html
  - https://tedboy.github.io/pyspark_doc/pyspark.ml.param.html
  - https://tedboy.github.io/pyspark_doc/sources/pyspark.ml.txt
  - https://tedboy.github.io/pyspark_doc/sources/pyspark.ml.param.txt



dd

**************************
Paragraph-level directives
**************************
See this link for details of below: http://www.sphinx-doc.org/en/stable/markup/para.html

.. code-block:: rst

    .. note::

        This function is not suitable for sending spam e-mails.

    .. warning::
    .. versionadded:: 2.5
       The *spam* parameter.

    .. versionchanged::

    .. deprecated:: 3.1
       Use :func:`spam` instead.

    .. seealso:: modules :py:mod:`zipfile`, :py:mod:`tarfile`
    .. seealso::

       Module :py:mod:`zipfile`
          Documentation of the :py:mod:`zipfile` standard module.

       `GNU tar manual, Basic Tar Format <http://link>`_
          Documentation for tar archive files, including GNU tar extensions.

    .. rubric:: title
    .. centered:: LICENSE AGREEMENT
    .. hlist::
       :columns: 3

       * A list of
       * short items
       * that should be
       * displayed
       * horizontally

########################
restructured text primer
########################
http://docutils.sourceforge.net/docs/user/rst/quickref.html

- http://www.sphinx-doc.org/en/stable/rest.html
- Roles: http://docutils.sourceforge.net/docs/ref/rst/roles.html
- Directives
  
  - http://docutils.sourceforge.net/docs/ref/rst/directives.html
  - (a good summary of usefule ones) http://www.sphinx-doc.org/en/stable/rest.html#directives
- http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html

************************
Heading-level convention
************************
- ``#`` with overline, for **parts**
- ``*`` with overline, for **chapters**
- ``=``, for **sections**
- ``-``, for **subsections**
- ``^``, for **subsubsections**
- ``"``, for **paragraphs**


***********
Line blocks
***********
.. code-block:: rst

    | These lines are
    | broken exactly like in
    | the source file.

| These lines are
| broken exactly like in
| the source file.

*********
Citations
*********
.. code-block:: rst

    Lorem ipsum [Ref]_ dolor sit amet.

    .. [Ref] Book or article reference, URL or whatever.

*****
links
*****
.. code-block:: rst

    This is a paragraph that contains `a link`_ and an `inline link <http://www.espn.com>`_

    .. _a link: http://example.com/

This is a paragraph that contains `a link`_ and an `inline link <http://www.espn.com>`_

.. _a link: http://example.com/

*********
citations
*********
In Sphinx, all citations can be referenced from all files. 

.. code-block:: rst

    Lorem ipsum [Ref]_ dolor sit amet.

    .. [Ref] Book or article reference, URL or whatever.

Lorem ipsum [Ref]_ dolor sit amet.

.. [Ref] Book or article reference, URL or whatever.

**********************
substitutions |stuffs|
**********************
http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#substitution-definitions

.. code-block:: rst

    .. |name| replace:: replacement *text*
    .. |caution| image:: warning.png
                 :alt: Warning!

Sphinx-built-in substitutions

.. code-block:: rst

    |release|
    |version|
    |today|




********
comments
********
..
   This whole indented block
   is a comment.

   Still in the comment.

.. code-block:: rst

    ..
       This whole indented block
       is a comment.

       Still in the comment.

###########################
master document (index.rst)
###########################
``index.rst`` 

- contains the root of the **toctree** (connect multiple files to a single hierarchy of documents) (`link <http://www.sphinx-doc.org/en/stable/tutorial.html#defining-document-structure>`_)
- The document that contains the root toctree directive. (`link <http://www.sphinx-doc.org/en/stable/glossary.html#term-master-document>`_)


####################
Publishing on github
####################
need to rename the following folders to *without* underscores

::
    
    _modules -> modules
    _sources -> sources
    _static -> static

Also need to correct folder name on corresponding html file above (I simply use sed)

#################
sphinx quickstart
#################
http://stackoverflow.com/questions/34483545/how-to-use-sphinx-quickstart-in-non-interactive-mode

.. code-block:: bash

    sphinx-quickstart --quiet --project=TEST --author=TW -v 1 --ext-autodoc --ext-mathjax --no-batchfile

*******
queries
*******
.. code-block:: bash

    Welcome to the Sphinx 1.4.5 quickstart utility.

    Please enter values for the following settings (just press Enter to
    accept a default value, if one is given in brackets).

    Enter the root path for documentation.
    > Root path for the documentation [.]: 

    You have two options for placing the build directory for Sphinx output.
    Either, you use a directory "_build" within the root path, or you separate
    "source" and "build" directories within the root path.
    > Separate source and build directories (y/n) [n]: y

    Inside the root directory, two more directories will be created; "_templates"
    for custom HTML templates and "_static" for custom stylesheets and other static
    files. You can enter another prefix (such as ".") to replace the underscore.
    > Name prefix for templates and static dir [_]: AAA_

    The project name will occur in several places in the built documentation.
    > Project name: test
    > Author name(s): test

    Sphinx has the notion of a "version" and a "release" for the
    software. Each version can have multiple releases. For example, for
    Python the version is something like 2.5 or 3.0, while the release is
    something like 2.5.1 or 3.0a1.  If you don't need this dual structure,
    just set both to the same value.
    > Project version: 
    * Please enter some text.
    > Project version: 1
    > Project release [1]: 

    If the documents are to be written in a language other than English,
    you can select a language here by its language code. Sphinx will then
    translate text that it generates into that language.

    For a list of supported codes, see
    http://sphinx-doc.org/config.html#confval-language.
    > Project language [en]: 

    The file name suffix for source files. Commonly, this is either ".txt"
    or ".rst".  Only files with this suffix are considered documents.
    > Source file suffix [.rst]: 

    One document is special in that it is considered the top node of the
    "contents tree", that is, it is the root of the hierarchical structure
    of the documents. Normally, this is "index", but if your "index"
    document is a custom template, you can also set this to another filename.
    > Name of your master document (without suffix) [index]: 

    Sphinx can also add configuration for epub output:
    > Do you want to use the epub builder (y/n) [n]: 

    Please indicate if you want to use one of the following Sphinx extensions:
    > autodoc: automatically insert docstrings from modules (y/n) [n]: y
    > doctest: automatically test code snippets in doctest blocks (y/n) [n]: n
    > intersphinx: link between Sphinx documentation of different projects (y/n) [n]: 
    > todo: write "todo" entries that can be shown or hidden on build (y/n) [n]: 
    > coverage: checks for documentation coverage (y/n) [n]: 
    > imgmath: include math, rendered as PNG or SVG images (y/n) [n]: 
    > mathjax: include math, rendered in the browser by MathJax (y/n) [n]: y
    > ifconfig: conditional inclusion of content based on config values (y/n) [n]: 
    > viewcode: include links to the source code of documented Python objects (y/n) [n]: 
    > githubpages: create .nojekyll file to publish the document on GitHub pages (y/n) [n]: 

    A Makefile and a Windows command file can be generated for you so that you
    only have to run e.g. `make html' instead of invoking sphinx-build
    directly.
    > Create Makefile? (y/n) [y]: y
    > Create Windows command file? (y/n) [y]: n

    Creating file ./source/conf.py.
    Creating file ./source/index.rst.
    Creating file ./Makefile.

    Finished: An initial directory structure has been created.

    You should now populate your master file ./source/index.rst and create other documentation
    source files. Use the Makefile to build the docs, like so:
       make builder
    where "builder" is one of the supported builders, e.g. html, latex or linkcheck.


***
doc
***

Here's the doc:

.. code-block:: bash

    Sphinx v1.4.5
    Usage: sphinx-quickstart [options] [projectdir]

    Options:
      --version             show program's version number and exit
      -h, --help            show this help message and exit
      -q, --quiet           quiet mode

      Structure options:
        --sep               if specified, separate source and build dirs
        --dot=DOT           replacement for dot in _templates etc.

      Project basic options:
        -p PROJECT, --project=PROJECT
                            project name
        -a AUTHOR, --author=AUTHOR
                            author names
        -v VERSION          version of project
        -r RELEASE, --release=RELEASE
                            release of project
        -l LANGUAGE, --language=LANGUAGE
                            document language
        --suffix=SUFFIX     source file suffix
        --master=MASTER     master document name
        --epub              use epub

      Extension options:
        --ext-autodoc       enable autodoc extension
        --ext-doctest       enable doctest extension
        --ext-intersphinx   enable intersphinx extension
        --ext-todo          enable todo extension
        --ext-coverage      enable coverage extension
        --ext-imgmath       enable imgmath extension
        --ext-mathjax       enable mathjax extension
        --ext-ifconfig      enable ifconfig extension
        --ext-viewcode      enable viewcode extension
        --ext-githubpages   enable githubpages extension

      Makefile and Batchfile creation:
        --makefile          create makefile
        --no-makefile       not create makefile
        --batchfile         create batchfile
        --no-batchfile      not create batchfile
        -M, --no-use-make-mode
                            not use make-mode for Makefile/make.bat
        -m, --use-make-mode
                            use make-mode for Makefile/make.bat

    For more information, visit <http://sphinx-doc.org/>.

#####################################
Google-style vs numpy-style docstring
#####################################
ref - https://pypi.python.org/pypi/sphinxcontrib-napoleon

**************************
Google style (like theano)
**************************
.. code-block:: python

    def func(arg1, arg2):
        """Summary line.

        Extended description of function.

        Args:
            arg1 (int): Description of arg1
            arg2 (str): Description of arg2

        Returns:
            bool: Description of return value

        """
        return True

**************************
NumPy style (my preference)
**************************
.. code-block:: python

    def func(arg1, arg2):
        """Summary line.

        Extended description of function.

        Parameters
        ----------
        arg1 : int
            Description of arg1
        arg2 : str
            Description of arg2

        Returns
        -------
        bool
            Description of return value

        """
        return True

In ``conf.py``: https://raw.githubusercontent.com/pydata/pandas/master/doc/source/conf.py

.. code-block:: python

    extensions = [...
                  'numpydoc', # used to parse numpy-style docstrings for autodoc
                  'ipython_sphinxext.ipython_directive',
                  ...
                  ]