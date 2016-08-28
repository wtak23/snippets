Tak's repos for coding snippets
===============================
One of my biggest regret in life -- trying to maintain my code snippets in Evernote. 

Those were dark days with no tangible signs of hope.

.. note::
  
    ``|today|`` = |today|
    
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
    
    


All modules for which code is available (`link <./_modules/index.html>`_)

.. code-block:: bash

    echo * | sed 's/ /\n/g' | grep \.rst --color=never | xclip -selection clipboard