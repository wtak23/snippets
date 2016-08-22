rst cheatsheet (old)
""""""""""""""""""""
**OLD VERSION 06-15-2016 (17:32)**

I won't be updating this abomination....i wrote this when i first found out 
about rst files.

.. contents:: `Table of contents`
   :depth: 2
   :local:

- A **trial-and-error** result of which rst-*directives* from `docutil <http://docutils.sourceforge.net/docs/ref/rst/directives.html>`_ worked on github (or bitbucket)
- **Warning** - I wrote this as a note for myself as I am new to using restructuredtext, so I generally do not guarantee the correctness of the content presented.  However, you can verify with your own eyes what renders by skimming through this page.


###########################################
DIRECTIVES I FOUND USEFUL OR RUNS ON GITHUB
###########################################
Reminder: syntax for directives in RST (watchout for the space after the colon)::

    .. <name>:: <arguments>
        :<option>: <option values>

        content

**********
.. image::
**********
::

    .. image:: /_static/img/sparse-brain.png
       :height: 100px
       :width: 200 px
       :scale: 50 %
       :alt: alternate text
       :align: right

.. image:: /_static/img/sparse-brain.png
   :height: 100px
   :width: 200 px
   :scale: 50 %
   :alt: alternate text
   :align: right

**********************************************
.. code:: (use with ``:number-lines:`` option)
**********************************************
::

    .. code:: python
        :number-lines:

        import numpy as np
        import scipy as sp

        x=np.linspace(-2,2,51)

.. code:: python
    :number-lines:

    import numpy as np
    import scipy as sp

    x=np.linspace(-2,2,51)

**********
.. table::
**********
::

    .. table:: Truth table for "not"

       =====  =====
         A    not A
       =====  =====
       False  True
       True   False
       =====  =====

.. table:: Truth table for "not"

   =====  =====
     A    not A
   =====  =====
   False  True
   True   False
   =====  =====

**************
.. csv-table::
**************
::

    .. csv-table:: Frozen Delights!
       :header: "Treat", "Quantity", "Description"
       :widths: 15, 10, 30

       "Albatross", 2.99, "On a stick!"
       "Crunchy Frog", 1.49, "If we took the bones out, it wouldn't be
       crunchy, now would it?"
       "Gannet Ripple", 1.99, "On a stick!"

.. csv-table:: Frozen Delights!
   :header: "Treat", "Quantity", "Description"
   :widths: 15, 10, 30

   "Albatross", 2.99, "On a stick!"
   "Crunchy Frog", 1.49, "If we took the bones out, it wouldn't be
   crunchy, now would it?"
   "Gannet Ripple", 1.99, "On a stick!"

*************
.. contents::
*************
**Remarks**

- adding the ``:depth: int`` syntax is fine
- adding the ``:backlinks: {entry,top,none}`` screw the links up

::

      .. contents:: **Table of Contents**
          :depth: 3

*************************************************************************
.. sectnum:: ...works....but **WARNING!** - seem to screw up the TOC link
*************************************************************************
::

    .. sectnum::    
        :start: 1  

*****************************
.. header:: (and .. footer::)
*****************************
::

    .. header:: This is a header (see top of page).
    .. footer:: This is a footer (see bottom of page).

.. header:: This is a header (see top of page).
.. footer:: This is a footer (see bottom of page).

*****************************************************************
Sadly ``.. math::`` doesn't render on github (works on bitbucket)
*****************************************************************
::

    Inline math using rst-"roles": :math:`\frac{x}{2} = \gamma \times\frac{\beta}{\alpha}`
    .. math::

        n_{\mathrm{offset}} = \sum_{k=0}^{N-1} s_k n_k

Above will produce this (renders on bitbucket):

Inline math using rst-"roles": :math:`\frac{x}{2} = \gamma \times\frac{\beta}{\alpha}`

.. math::

    n_{\mathrm{offset}} = \sum_{k=0}^{N-1} s_k n_k



************
.. replace::
************
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

************
.. unicode::
************
::

    Copyright |copy| 2003, |BogusMegaCorp (TM)| |---|
    all rights reserved.

    .. |copy| unicode:: 0xA9 .. copyright sign
    .. |BogusMegaCorp (TM)| unicode:: BogusMegaCorp U+2122
       .. with trademark sign
    .. |---| unicode:: U+02014 .. em dash
       :trim:

Copyright |copy| 2003, |BogusMegaCorp (TM)| |---|
all rights reserved.

.. |copy| unicode:: 0xA9 .. copyright sign
.. |BogusMegaCorp (TM)| unicode:: BogusMegaCorp U+2122
   .. with trademark sign
.. |---| unicode:: U+02014 .. em dash
   :trim:

********
..date::
********
::

    .. |date| date::
    .. |time| date:: %H:%M

    Today's date is |date|.

    This document was generated on |date| at |time|.

.. |date| date::
.. |time| date:: %H:%M

Today's date is |date|.

This document was generated on |date| at |time|.

############################################################################
List of **GOTCHA's** to watch out for (at least the ones I suffered from...)
############################################################################


*******************************
Gotcha's with nested list items
*******************************
- **WARNINGS: BE CAREFUL TO ADD ADDITIONAL EMPTY LINE BEFORE THE NESTED LIST-ITEM BEGINS**
- **ALSO, DO NOT TAB-ALIGN, BUT RATHER Make sure the nested list is indented to the same level as the text of the parent list**
- REF: http://stackoverflow.com/questions/5550089/how-to-create-a-nested-list-in-restructuredtext

This (correct) code::

    - Parent nest conent

      - children nest content1
      - children nest content1

renders this result

- Parent nest conent

  - children nest content1
  - children nest content1

*****************************************************************
Sadly ``.. math::`` doesn't render on github (works on bitbucket)
*****************************************************************
::

    .. math::

        n_{\mathrm{offset}} = \sum_{k=0}^{N-1} s_k n_k

Above will produce this (renders on bitbucket):

.. math::

    n_{\mathrm{offset}} = \sum_{k=0}^{N-1} s_k n_k

*******************************
GOTCHA's with ``.. contents::``
*******************************
- adding the ``:depth: int`` syntax is fine
- adding the ``:backlinks: {entry,top,none}`` screws up the links in the TOC
- using auto-section numbering with ``.. sectnum::`` screws up the linking of TOC

**************************
``h1`` ``h2`` ... problems
**************************
- In github, you need to add some text between headers ``h1``, ``h2``, etc
  - blank lines will mess up the TOC structure.
  - I generally insert ``...`` just for the sake of having some text in between... 
- You cannot jump from ``h1`` to ``h3`` without ``h2`` in between
  - Github won't even try to render

********************************************************************************
Including styles on HEADER-NAMES will break the TOC link on github (unconfirmed)
********************************************************************************
Have no idea why, and have no idea what the rule for breaking the link actually is (seems random)

**********************************************************
Directives that just doesnt work on github or Sublime Text
**********************************************************
- `Admonitions <http://docutils.sourceforge.net/docs/ref/rst/directives.html#admonitions>`_
- `Topic <http://docutils.sourceforge.net/docs/ref/rst/directives.html#topic>`_
- `Line Block <http://docutils.sourceforge.net/docs/ref/rst/directives.html#line-block>`_ (works on ST, but not on Github...also deprecated anyways)
- ``.. parsed-literal::``
- ``raw`` role (not quite sure yet, but seems like Github seems to not support this)

********************************************************
Some special characters that may be a head-ache to print
********************************************************
::
    
    To get single-back-tick: `````

To get single interpreted back-tick: `````

################
``roles`` in RST
################
Ref: http://docutils.sourceforge.net/docs/ref/rst/roles.html

- Basic syntax: ``ROLENAME:`INTERPRETED-TEXT``` (note the use of the backtick ````` in the second-half)
- Warning: must include a space before and after the above syntax...so if you want to suppress unwanted white space, use backslah ``\``

  - example: ``H\ :sub:`2`\ O`` renders H\ :sub:`2`\ O

As an example, the following are equivalent:: 

    - This is `interpreted text` using the default role.
    - This is :title:`interpreted text` using an explicit role.

- This is `interpreted text` using the default role.
- This is :title:`interpreted text` using an explicit role.

***********************************************
List of equivalent ``roles`` (ultra-incomplete)
***********************************************
.. code::

    *text*
    :emphasis:`text`    
    
    **text**
    :strong:`text`   
    
    ``text``
    :literal:`text`
    
 
**********************************
Some interesting looking ``roles``
**********************************
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
