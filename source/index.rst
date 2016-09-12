Tak's repos for coding snippets
===============================
One of my biggest regret in life -- trying to maintain my code snippets in Evernote. 

Those were dark days with no tangible signs of hope.

**HTML last built:**  |today|

.. important::

    08-25-2016 --- Decided to move all my `config` notes to a separate repository

    https://wtak23.github.io/configs

.. note::
  
    - The categorization in the top-level of the TOC tree below is very loose.
    - It is based on an arbitrary mnemonic that I developed out of nowhere.

.. toctree::
    :maxdepth: 2
    :caption: Table of Contents

    top-python.rst
    top-bash.rst
    top-datascience.rst
    top-unix.rst
    top-rst.rst

.. code-block:: bash

    echo * | sed 's/ /\n/g' | grep \.rst --color=never | xclip -selection clipboard

All modules for which code is available (`link <./_modules/index.html>`_)