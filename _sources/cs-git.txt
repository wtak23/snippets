git-snippet (``cs-git.rst``)
""""""""""""""""""""""""""""

.. contents:: `Table of contents`
   :depth: 2
   :local: 

#############################################
Remove folder and/or filetypes from git repos
#############################################
http://dalibornasevic.com/posts/2-permanently-remove-files-and-folders-from-git-repo

.. code-block:: bash

    git filter-branch --tree-filter 'rm -rf vendor/gems' HEAD
    git filter-branch --tree-filter 'rm -rf webpage-new/build' HEAD


    # BY FILE TYPE (mayneed -f flag)
    git filter-branch --tree-filter 'git rm -r -f --ignore-unmatch *.pyc' HEAD
    git filter-branch -f --tree-filter 'git rm -r -f --ignore-unmatch *.pdf' HEAD

################
Random Overflows
################
******************
Clone specific tag
******************
http://stackoverflow.com/questions/791959/download-a-specific-tag-with-git

Git the whole repos, and then checkout the branch.

.. code-block:: bash

    git clone REPOS

    # list the tags
    git tag -l

    # checkout a specific tag
    get checkout tags/<tag_name>

    # checkout and create a branch
    get checkout tags/<tag_name> -b <branch_name>

**********************
Delete untracked files
**********************
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

******************
change author name
******************
For a single commit

http://stackoverflow.com/questions/750172/change-the-author-of-a-commit-in-git


.. code-block:: bash
    :linenos:

    git commit --amend --author "Author Name <email@address.com>"     


For entire git repos:

https://help.github.com/articles/changing-author-info/

`git-author-rewrite.sh <https://gist.githubusercontent.com/octocat/0831f3fbd83ac4d46451/raw/c197afe3e9ea2e4218f9fccbc0f36d2b8fd3c1e3/git-author-rewrite.sh>`_

.. code-block:: bash
    :linenos:

    #!/bin/sh

    git filter-branch -f --env-filter '

    CORRECT_NAME="your name"
    CORRECT_EMAIL="your_email@example.com"

    export GIT_COMMITTER_NAME="$CORRECT_NAME"
    export GIT_COMMITTER_EMAIL="$CORRECT_EMAIL"

    export GIT_AUTHOR_NAME="$CORRECT_NAME"
    export GIT_AUTHOR_EMAIL="$CORRECT_EMAIL"
    ' --tag-name-filter cat -- --branches --tags