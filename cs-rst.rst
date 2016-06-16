`[Parent Directory] <./>`_

.. contents:: **Table of Contents**
    :depth: 2

.. sectnum::    
    :start: 1    

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

############
Sphinx-based
############
- Tutorial: https://pythonhosted.org/an_example_pypi_project/sphinx.html
- RST tutorial for sphinx http://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html
- http://www.sphinx-doc.org/en/stable/ext/autodoc.html
  
  - to include documentation from docstrings

*****
Links
*****
- Suppose we have ``rst_tutorial.rst``
  
  - top of the file contains a **label** *rst_tutorial*, specified by typing
    ``.. _rst_tutorial``
- Two ways to call it (`link <http://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html#internal-and-external-links>`_)

  #. ``.. _rst_tutorial:`` 
  #. ``:ref: `rst_tutorial`` <= required if link is to be found in an **external rst file**
- so always use the second method






********
Examples
********
- ``conf.py`` important (`link <https://pythonhosted.org/an_example_pypi_project/sphinx.html#conf-py>`_)

  - nimfa example [`link <https://github.com/marinkaz/nimfa/blob/master/docs/source/conf.py>`_]
  - http://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html#useful-extensions


############
Handy tricks
############
*************************
References and citations
*************************
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

#################
Useful directives
#################


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
Sadly ``.. math::`` doesn't render on github (works on bitbucket)
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
.. code:: rst

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
.. code::

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

.. code::

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
