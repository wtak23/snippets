git-snippet
"""""""""""

.. contents:: `Table of contents`
   :depth: 2
   :local: 

##############
Stackoverflows
##############



http://stackoverflow.com/questions/61212/how-to-remove-local-untracked-files-from-the-current-git-branch

.. code-block:: bash

    # do a dry run
    git clean -n 

    # do interactive (to be on the save side)
    git clean -i

    # include directory 
    git clean -n -d

    # if happy with dry run, actually do clean
    git clean -f -d

