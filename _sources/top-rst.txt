##################################
Sphinx/RST-notes (``top-rst.rst``)
##################################

.. important::

    08-25-2016 (14:02)

    Rolled back Sphinx from v1.4.5 to v1.3.5. Bunch of problems resolved, including:

    - ``copybutton.js`` finally working!
    - ``autosummary`` auto-docing functions/class coming from external imports (I no longer need to replace the ``ext/autosummary/generate.py`` with my hacky fix)

    .. code-block:: python
    
        pip install sphinx==1.3.5 --user

.. toctree::
    :maxdepth: 1
    :caption: Table of Contents
    :numbered:
    :name: top-sphinx

    cs-rst.rst
    cs-rst.directive-test.rst
    cs-rst.math_part1.rst
    cs_rst.math_part2.rst
    cs-rst.ipython.rst
    cs-rst-old.rst
