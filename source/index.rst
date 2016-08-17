.. Snippets documentation master file, created by
   sphinx-quickstart on Fri Aug  5 13:45:35 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Tak's personal coding snippet repos
===================================
One of my biggest regret in life -- trying to maintain my code snippets in Evernote. Those were some dark dark days with no tangible signs of hope.

.. toctree::
    :maxdepth: 1
    :numbered:
    :caption: Table of Contents

    cs-bash-commands.rst
    cs-bash-scripts.rst
    cs-qsubber.rst
    cs-python.rst
    cs-pyspark.rst
    bct.rst
    cs-git.rst
    configs/configs.rst
    cs-R.rst
    cs-awk-oneliners.rst
    cs-perl-oneliners.rst
    cs-py-jupyter-notebook.rst
    cs-regexp.rst
    cs-rst-old.rst
    cs-sed.rst
    cs-sql.rst
    cs-scala.rst
    awk-tutorial/index.rst
    sed-tutorial/index.rst

All modules for which code is available (`link <./_modules/index.html>`_)

.. code-block:: bash

    echo * | sed 's/ /\n/g' | grep \.rst --color=never | xclip -selection clipboard