.. Snippets documentation master file, created by
   sphinx-quickstart on Fri Aug  5 13:45:35 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Tak's repos for coding snippets
===============================
One of my biggest regret in life -- trying to maintain my code snippets in Evernote. 

Those were dark days with no tangible signs of hope.

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
    top-misc.rst
    configs/top-configs.rst
    
    


All modules for which code is available (`link <./_modules/index.html>`_)

.. code-block:: bash

    echo * | sed 's/ /\n/g' | grep \.rst --color=never | xclip -selection clipboard