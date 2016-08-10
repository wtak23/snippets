rst
"""

.. contents:: **Table of Contents**
    :depth: 2

 




#######
Lookups
#######
- **directives** http://docutils.sourceforge.net/docs/ref/rst/directives.html
- **roles** (eg, ``:math:`` syntax
  
  - http://docutils.sourceforge.net/docs/ref/rst/roles.html

********************
Tutorials
********************
- https://pythonhosted.org/an_example_pypi_project/sphinx.html
- http://www.sphinx-doc.org/en/stable/rest.html
- http://docutils.sourceforge.net/docs/user/rst/quickref.html <= best one

********************
header convention (me)
********************
However, it is better to stick to the same convention throughout a project. For instance (`ref <http://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html#headings>`_):

- # with overline, for parts
- \* with overline, for chapters
- =, for sections
- -, for subsections
- ^, for subsubsections
- “, for paragraphs


############
Sphinx-based
############
- Tutorial: https://pythonhosted.org/an_example_pypi_project/sphinx.html
- RST tutorial for sphinx http://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html
- http://www.sphinx-doc.org/en/stable/ext/autodoc.html
  
  - to include documentation from docstrings

*******
autodoc
*******
- http://thomas-cokelaer.info/tutorials/sphinx/docstring_python.html
- http://www.sphinx-doc.org/en/stable/ext/autodoc.html?highlight=automodule#directive-automodule

::

  .. automodule::
  .. autoclass::
  .. autoexception::

This will by default, above will only insert the docstring of the object itself:


.. code-block:: rst

  .. autoclass:: Noodle
  .. This will produce something like:


::

  .. class:: Noodle

     Noodle's docstring.


recursive docstringing objects
==============================
.. code-block:: rst

    .. recursive autodoc all module members
    .. automodule:: noodle
       :members:

    .. recursively document all non-private member functions and properties
    .. autoclass:: Noodle
       :members:

      .. You can also give an explicit list of members; only these will then be documented
    .. autoclass:: Noodle
       :members: eat, slurp

    .. 
      By default, non-documented member functions will be ignored. 
      To avoid that, use :undoc-members: option
    .. autoclass:: Noodle
       :members:
       :undoc-members:

********************
Links (url)
********************
.. code-block:: rst

    This is a paragraph that contains `a link`_.

    This is an inline `link <http://example.com/>`_

    .. _a link: http://example.com/

This is a paragraph that contains `a link`_.

This is an inline `link <http://example.com/>`_

.. _a link: http://example.com/


**************
markup, showing code, inlines
**************
http://www.sphinx-doc.org/en/stable/markup/code.html

.. code-block:: rst
    
    .. code-block:: ruby
       :linenos:

       Some more Ruby code.

.. code-block:: rst

    .. literalinclude:: example.py

    .. literalinclude:: example.py
       :diff: example.py.orig

**************************
inline (bunch of roles)
**************************
http://www.sphinx-doc.org/en/stable/markup/inline.html

- ``:any:``
- ``:doc:``
- ``:download:``
- ``:numref:``

``:ref:``

::

    .. _my-reference-label:

    Section to cross-reference
    --------------------------

    This is the text of the section.

    It refers to the section itself, see :ref:`my-reference-label`.

    .. _my-figure:

    .. figure:: whatever

       Figure caption


******
domain
******
http://www.sphinx-doc.org/en/stable/domains.html


*************
python domain
*************
http://www.sphinx-doc.org/en/stable/domains.html#the-python-domain



*************
misc examples
*************
http://www.sphinx-doc.org/en/stable/markup/misc.html

.. code-block:: rst

    .. sectionauthor:: Guido van Rossum <guido@python.org>
    .. codeauthor:: name <email>
    .. index:: <entries>
    .. only:: html and draft
    .. tabularcolumns:: column spec


***************
Link documents
***************
- Suppose we have ``rst_tutorial.rst``
  
  - top of the file contains a **label** *rst_tutorial*, specified by typing
    ``.. _rst_tutorial``
- Two ways to call it (`link <http://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html#internal-and-external-links>`_)

  #. ``.. _rst_tutorial:`` 
  #. ``:ref: `rst_tutorial`` <= required if link is to be found in an **external rst file**
- so always use the second method

*************
conf.py setup
*************
http://www.sphinx-doc.org/en/stable/config.html#general-configuration

conf.py - html output options
=============================
http://www.sphinx-doc.org/en/stable/config.html#options-for-html-output


**********
Extensions
**********
this is the thing included in the list ``extensions=[...]`` in **conf.py**

- http://www.sphinx-doc.org/en/stable/extensions.html

  - http://www.sphinx-doc.org/en/stable/ext/autodoc.html
  - http://www.sphinx-doc.org/en/stable/ext/math.html

********************
Examples conf.py and github
********************
For bunch of **themes**: http://www.sphinx-doc.org/en/stable/theming.html

Options for ``extensions``: http://www.sphinx-doc.org/en/stable/extensions.html

Great cheatsheet (standard)
====================
- http://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html#headings  
- https://github.com/cokelaer/sphinx_tutorial
- https://github.com/cokelaer/sphinx_tutorial/blob/master/source/conf.py

.. code-block:: python

    import easydev
    from easydev import get_path_sphinx_themes
    html_theme = "standard"
    html_theme_options = {'homepage': url}
    html_theme_path = [get_path_sphinx_themes()]
    extensions = [
        'sphinx.ext.autodoc',
        'sphinx.ext.autosummary',
        'sphinx.ext.coverage',
        'sphinx.ext.graphviz',
        'sphinx.ext.doctest',
        'sphinx.ext.intersphinx',
        'sphinx.ext.todo',
        'sphinx.ext.coverage',
        'sphinx.ext.ifconfig',
        'sphinx.ext.viewcode',
        'easydev.copybutton',
        'matplotlib.sphinxext.plot_directive',
        'matplotlib.sphinxext.only_directives',
        'sphinx.ext.pngmath',
        ]


Sphinx doc (sphinx13)
====================
- http://www.sphinx-doc.org/en/stable/contents.html
- https://github.com/sphinx-doc/sphinx/blob/master/doc/conf.py

.. code-block:: python

    import sphinx
    extensions = ['sphinx.ext.autodoc', 'sphinx.ext.doctest', 'sphinx.ext.todo',
                  'sphinx.ext.autosummary', 'sphinx.ext.extlinks',
                  'sphinx.ext.viewcode']
    
    html_theme = 'sphinx13'
    html_theme_path = ['_themes']
    modindex_common_prefix = ['sphinx.']
    html_static_path = ['_static']
    html_sidebars = {'index': ['indexsidebar.html', 'searchbox.html']}
    html_additional_pages = {'index': 'index.html'}
    html_use_opensearch = 'http://sphinx-doc.org'


nimfa (alabaster)
====================
- http://nimfa.biolab.si/
- https://github.com/marinkaz/nimfa/blob/master/docs/source/conf.py

.. code-block:: python

    extensions = ['sphinx.ext.autodoc', 'sphinx.ext.doctest',
                  'sphinx.ext.intersphinx', 'sphinx.ext.ifconfig',
                  'alabaster']
    
    import alabaster

    html_theme_path = [alabaster.get_path()]
    html_theme = 'alabaster'
    html_sidebars = {
        '**': [
            'about.html',
            'navigation.html',
            'relations.html',
            'searchbox.html',
            'donate.html',
        ]
    }

    html_theme_options = {
        'github_user': 'marinkaz',
        'github_repo': 'nimfa',
        'github_button': True,
        'github_banner': True,
        'sidebar_width': '250px',
    }


pandas
====================
https://github.com/pydata/pandas/blob/master/doc/source/conf.py

.. code-block:: python

    html_theme = 'nature_with_gtoc'
    html_theme_path = ['themes']
    
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

scipy lecture notes
====================
http://www.scipy-lectures.org/

https://github.com/scipy-lectures/scipy-lecture-notes

.. code-block:: python

    import gen_rst # <= from scikit learn

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
    html_theme = 'scipy_lectures'
    html_theme_path = ['themes']
    html_theme_options = {
                    #'nosidebar': 'true',
                    'footerbgcolor': '#000000',
                    'relbarbgcolor': '#000000',
                    }
    html_title = "Scipy lecture notes"


scikit-learn
============
http://scikit-learn.org/stable/

https://github.com/scikit-learn/scikit-learn

https://github.com/scikit-learn/scikit-learn/blob/master/doc/conf.py

inside ``theme.conf``

::

  [theme]
  inherit = basic
  stylesheet = nature.css
  pygments_style = tango

  [options]
  oldversion = False
  collapsiblesidebar = True
  google_analytics = True
  surveybanner = False
  sprintbanner = True

inside ``conf.py``

.. code-block:: python

    from sklearn.externals.six import u
    import gen_rst # <= from scikit    
    extensions = ['gen_rst',
                  'sphinx.ext.autodoc', 'sphinx.ext.autosummary',
                  'sphinx.ext.pngmath', 'numpy_ext.numpydoc',
                  'sphinx.ext.linkcode', 'sphinx.ext.doctest',
                  ]
    autosummary_generate = True
    autodoc_default_flags = ['members', 'inherited-members']
    # generate autosummary even if no references
    autosummary_generate = True


    html_theme = 'scikit-learn'
    html_theme_options = {'oldversion': False, 'collapsiblesidebar': True,
                          'google_analytics': True, 'surveybanner': False,
                          'sprintbanner': True}

    # Add any paths that contain custom themes here, relative to this directory.
    html_theme_path = ['themes']

********************
themes
********************
http://www.sphinx-doc.org/en/stable/theming.html

.. code-block:: python

    html_theme = 'alabaster'
    html_theme = 'nature'
    html_theme = "sphinxdoc"   # currently no options beyond nosidebar and sidebarwidth
    html_theme = "traditional" # currently no options beyond nosidebar and sidebarwidth
    html_theme = "sphinx_rtd_theme"

    html_theme = "classic"
    html_theme_options = {
        "rightsidebar": "true",
        "relbarbgcolor": "black",
        "collapsiblesidebar": "false",
        "stickysidebar": "true",
    }


Bootstrap

.. code-block:: python

    import sphinx_bootstrap_theme
    html_theme = 'bootstrap'
    html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
    html_theme_options = {
        # Navigation bar title. (Default: ``project`` value)
        'navbar_title': "Demo",

        # Tab name for entire site. (Default: "Site")
        'navbar_site_name': "Site",

        # A list of tuples containing pages or urls to link to.
        # Valid tuples should be in the following forms:
        #    (name, page)                 # a link to a page
        #    (name, "/aa/bb", 1)          # a link to an arbitrary relative url
        #    (name, "http://example.com", True) # arbitrary absolute url
        # Note the "1" or "True" value above as the third argument to indicate
        # an arbitrary url.
        'navbar_links': [
            ("Examples", "examples"),
            ("Link", "http://example.com", True),
        ],

        # Render the next and previous page links in navbar. (Default: true)
        'navbar_sidebarrel': True,

        # Render the current pages TOC in the navbar. (Default: true)
        'navbar_pagenav': True,

        # Tab name for the current pages TOC. (Default: "Page")
        'navbar_pagenav_name': "Page",

        # Global TOC depth for "site" navbar tab. (Default: 1)
        # Switching to -1 shows all levels.
        'globaltoc_depth': 1,

        # Include hidden TOCs in Site navbar?
        #
        # Note: If this is "false", you cannot have mixed ``:hidden:`` and
        # non-hidden ``toctree`` directives in the same page, or else the build
        # will break.
        #
        # Values: "true" (default) or "false"
        'globaltoc_includehidden': "true",

        # HTML navbar class (Default: "navbar") to attach to <div> element.
        # For black navbar, do "navbar navbar-inverse"
        'navbar_class': "navbar navbar-inverse",

        # Fix navigation bar to top of page?
        # Values: "true" (default) or "false"
        'navbar_fixed_top': "true",

        # Location of link to source.
        # Options are "nav" (default), "footer" or anything else to exclude.
        'source_link_position': "nav",

        # Bootswatch (http://bootswatch.com/) theme.
        #
        # Options are nothing (default) or the name of a valid theme
        # such as "amelia" or "cosmo".
        #'bootswatch_theme': "united",

        # Choose Bootstrap version.
        # Values: "3" (default) or "2" (in quotes)
        #'bootstrap_version': "3",
    }

********************
toctree options
********************
- `link <http://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html#include-other-rst-files-with-the-toctree-directive>`_
- http://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html#include-other-rst-files-with-the-toctree-directive


.. code-block:: rst

  .. toctree::
      :maxdepth: 2
      :numbered:
  
      rst_file1.rst
      rst_file2.rst



*************************
References and citations
*************************
.. code-block:: rst

    http://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html#citations

    * Feature score computation representing its specificity to basis vectors [Park2007]_
    * Computation of most basis specific features for basis vectors [Park2007]_
    * Purity [Park2007]_
    * Residual sum of squares (rank estimation) [Hutchins2008]_, [Frigyesi2008]_
    * Sparseness [Hoyer2004]_


    .. [Park2007] Hyuonsoo Kim and Haesun Park. Sparse non-negative matrix factorizations via alternating non-negativity-constrained least squares for microarray data analysis. Bioinformatics, 23(12): 1495-1502, 2007. 

    .. [Hoyer2004] Patrik O. Hoyer. Non-negative matrix factorization with sparseness constraints. Journal of Machine Learning Research, 5: 1457-1469, 2004. 

    .. [Frigyesi2008] Attila Frigyesi and Mattias Hoglund. Non-negative matrix factorization for the analysis of complex gene expression data: identification of clinically relevant tumor subtypes. Cancer Informatics, 6: 275-292, 2008.

    .. [Hutchins2008] Lucie N. Hutchins, Sean P. Murphy, Priyam Singh and Joel H. Graber. Position-dependent motif characterization using non-negative matrix factorization. Bioinformatics, 24(23): 2684-2690, 2008.

http://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html#citations

* Feature score computation representing its specificity to basis vectors [Park2007]_
* Computation of most basis specific features for basis vectors [Park2007]_
* Purity [Park2007]_
* Residual sum of squares (rank estimation) [Hutchins2008]_, [Frigyesi2008]_
* Sparseness [Hoyer2004]_


.. [Park2007] Hyuonsoo Kim and Haesun Park. Sparse non-negative matrix factorizations via alternating non-negativity-constrained least squares for microarray data analysis. Bioinformatics, 23(12): 1495-1502, 2007. 

.. [Hoyer2004] Patrik O. Hoyer. Non-negative matrix factorization with sparseness constraints. Journal of Machine Learning Research, 5: 1457-1469, 2004. 

.. [Frigyesi2008] Attila Frigyesi and Mattias Hoglund. Non-negative matrix factorization for the analysis of complex gene expression data: identification of clinically relevant tumor subtypes. Cancer Informatics, 6: 275-292, 2008.

.. [Hutchins2008] Lucie N. Hutchins, Sean P. Murphy, Priyam Singh and Joel H. Graber. Position-dependent motif characterization using non-negative matrix factorization. Bioinformatics, 24(23): 2684-2690, 2008.

****************************
matplotlib, ipython directive options
****************************
In bookmark bar, type ``lookup sphinx pyplot/ipyhthon``

- http://matplotlib.org/sampledoc/extensions.html
- http://matplotlib.org/devel/documenting_mpl.html
- https://ipython.org/ipython-doc/3/api/generated/IPython.sphinxext.ipython_directive.html

.. code-block:: python

    extensions = ['matplotlib.sphinxext.only_directives',
                  'matplotlib.sphinxext.plot_directive',
                  'IPython.sphinxext.ipython_directive',
                  'IPython.sphinxext.ipython_console_highlighting',
                  'sphinx.ext.mathjax',
                  'sphinx.ext.autodoc',
                  'sphinx.ext.doctest',
                  'sphinx.ext.inheritance_diagram',
                  'numpydoc']

#################
Useful directives
#################

*******
replace
*******
http://docutils.sourceforge.net/docs/ref/rst/directives.html#replacement-text

.. code-block:: rst

    .. |reST| replace:: reStructuredText

    Yes, |reST| is a long word, so I can't blame anyone for wanting to
    abbreviate it.



.. |reST| replace:: reStructuredText

Yes, |reST| is a long word, so I can't blame anyone for wanting to
abbreviate it.

****
date
****
.. code-block:: rst

    .. |date| date::
    .. |time| date:: %H:%M

    Today's date is |date|.

    This document was generated on |date| at |time|.

.. |date| date::
.. |time| date:: %H:%M

Today's date is |date|.

This document was generated on |date| at |time|.

*************
raw directive
*************
http://docutils.sourceforge.net/docs/ref/rst/directives.html#raw-data-pass-through

For example, the following input would be passed untouched by an HTML Writer:

.. code-block:: rst

  .. raw:: html

     <hr width=50 size=10>

   .. raw:: latex

   \setlength{\parindent}{0pt}  

  .. raw:: html
     :file: inclusion.html


***************
class directive
***************
http://docutils.sourceforge.net/docs/ref/rst/directives.html#class


**************
role directive
**************
http://docutils.sourceforge.net/docs/ref/rst/directives.html#custom-interpreted-text-roles

default interpreted text role
=============================
http://docutils.sourceforge.net/docs/ref/rst/directives.html#setting-the-default-interpreted-text-role


********
Unicodes
********
http://docutils.sourceforge.net/docs/ref/rst/directives.html#unicode-character-codes

Motivated from http://www.scipy-lectures.org/

See here for interesting unicodes: http://unicode.scarfboy.com/?s=U%2bf08c

.. code-block:: rst

    .. |github| unicode:: U+f09b  .. github logo
    .. |pdf| unicode:: U+f1c1 .. PDF file
    .. |archive| unicode:: U+f187 .. archive file
    .. |linkedin| unicode:: U+f08c .. linkedin logo (this is a comment)

    |github|, |pdf|, |archive|, |linkedin|

.. |github| unicode:: U+f09b  .. github logo
.. |pdf| unicode:: U+f1c1 .. PDF file
.. |archive| unicode:: U+f187 .. archive file
.. |linkedin| unicode:: U+f08c .. linkedin logo (this is a comment)

|github|, |pdf|, |archive|, |linkedin|

**********
image
**********
::

    .. image:: http://mgoblog.com/sites/mgoblog.com/files/tapestry_logo.png
       :height: 100px
       :width: 200 px
       :scale: 50 %
       :alt: alternate text
       :align: right

.. image:: http://mgoblog.com/sites/mgoblog.com/files/tapestry_logo.png
   :height: 100px
   :width: 500 px
   :scale: 150 %
   :alt: alternate text
   :align: right


********************
csv-table
********************
.. csv-table:: OPTIONAL-TITLE
    :header: OPTIONAL-COL-HEADER
    :widths: 20,70
    :delim: |


::

    .. csv-table:: Frozen Delights!
       :header: "Treat", "Quantity", "Description"
       :widths: 15, 10, 30
       :delim: ,

       "Albatross", 2.99, "On a stick!"
       "Crunchy Frog", 1.49, "If we took the bones out, it wouldn't be
       crunchy, now would it?"
       "Gannet Ripple", 1.99, "On a stick!"


.. csv-table:: Frozen Delights!
   :header: "Treat", "Quantity", "Description"
   :widths: 15, 10, 30
   :delim: ,

   "Albatross", 2.99, "On a stick!"
   "Crunchy Frog", 1.49, "If we took the bones out, it wouldn't be
   crunchy, now would it?"
   "Gannet Ripple", 1.99, "On a stick!"


********************
header and footer
********************
::

    .. header:: This is a header (see top of page).
    .. footer:: This is a footer (see bottom of page).

.. comment header out here; annoying
.. .. header:: This is a header (see top of page).
.. footer:: This is a footer (see bottom of page).

********************
math (won't render on github (works on bitbucket)
********************
::

    Inline math using rst-"roles": :math:`\frac{x}{2} = \gamma \times\frac{\beta}{\alpha}`

    .. math::

        n_{\mathrm{offset}} = \sum_{k=0}^{N-1} s_k n_k

Above will produce this (renders on bitbucket):

Inline math using rst-"roles": :math:`\frac{x}{2} = \gamma \times\frac{\beta}{\alpha}`

.. math::

    n_{\mathrm{offset}} = \sum_{k=0}^{N-1} s_k n_k



********************
replace
********************
::
    
    .. |reST| replace:: reStructuredText

    Yes, |reST| is a long word, so I can't blame anyone for wanting to
    abbreviate it.

    I recommend you try |Python|_.

    .. |Python| replace:: Python, *the* best language around
    .. _Python: http://www.python.org/

.. |reST| replace:: reStructuredText

Yes, |reST| is a long word, so I can't blame anyone for wanting to
abbreviate it.

I recommend you try |Python|_.

.. |Python| replace:: Python, *the* best language around
.. _Python: http://www.python.org/

****
date
****
::

    .. |date| date::
    .. |time| date:: %H:%M

    Today's date is |date|.

    This document was generated on |date| at |time|.

.. |date| date::
.. |time| date:: %H:%M

Today's date is |date|.

This document was generated on |date| at |time|.

*****
Lists
*****
::

  - Hello world
  - Hello world

    - Hello world

      - Hello
  - Hello world

- Hello world
- Hello world

  - Hello world

    - Hello
- Hello world


::

  #. hi
    
     #. yo
     #. yo
  #. bye
  #. ke

#. hi
  
   #. yo
   #. yo
#. bye
#. ke

********************
Comments
********************
.. code-block:: rst

  .. this is a comment

  Hello

  .. 
    Multi line comments
    that wraps across
    multiple lines

.. this is a comment

Hello

.. 
  Multi line comments
  that wraps across
  multiple lines


####################
roles in RST
####################
Ref: http://docutils.sourceforge.net/docs/ref/rst/roles.html

- Basic syntax: ``ROLENAME:`INTERPRETED-TEXT``` (note the use of the backtick ````` in the second-half)
- Warning: must include a space before and after the above syntax...so if you want to suppress unwanted white space, use backslah ``\``

  - example: ``H\ :sub:`2`\ O`` renders H\ :sub:`2`\ O

As an example, the following are equivalent:: 

    - This is `interpreted text` using the default role.
    - This is :title:`interpreted text` using an explicit role.

- This is `interpreted text` using the default role.
- This is :title:`interpreted text` using an explicit role.

********************
List of equivalent ``roles`` (ultra-incomplete)
********************
.. code-block::

    *text*
    :emphasis:`text`    
    
    **text**
    :strong:`text`   
    
    ``text``
    :literal:`text`
    
 
********************
Some interesting looking ``roles``
********************
From main doc http://docutils.sourceforge.net/docs/ref/rst/roles.html

.. code-block::

    # latex code?
    .. role:: latex(code)
       :language: latex

    # math role
    :math:
        The input format is LaTeX math syntax without the “math delimiters“ ($ $), for example:
            The area of a circle is :math:`A_\text{c} = (\pi/4) d^2`.
            
    :subscript:       
        (alias -> :sup:)
    :superscript:
        (alias -> :sub:)


Example run (note the ``\`` with empty-space to handle the white-space)::

    - The area of a circle is :math:`A_\text{c} = (\pi/4) d^2`.
    - H\ :sub:`2`\ O
    - :sup:`18`\ **F-FDG**

- The area of a circle is :math:`A_\text{c} = (\pi/4) d^2`.
- H\ :sub:`2`\ O
- :sup:`18`\ **F-FDG**
