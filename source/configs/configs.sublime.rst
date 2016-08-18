configs.sublime
"""""""""""""""
**Date**: |today|



##################################
Sublime settings: sbia workstation
##################################

- `Snippets <https://github.com/wtak23/configs_master/tree/master/sbia-pc125-cinn/sublime-text/sublime-snippets-sbia>`_
- `Synced settings <https://github.com/wtak23/configs_master/tree/master/sbia-pc125-cinn/sublime-text/synced_settings>`_
- `Others <https://github.com/wtak23/configs_master/tree/master/sbia-pc125-cinn/sublime-text/macros>`_ (note: these cannot be sync'ed at **folder-level**, so I need to include symlinks individually for each files)

.. code-block:: bash

    # so for the stuffs in **others**, create symlinks file-wise
    ln -s ~/Dropbox/git/configs_master/sbia-pc125-cinn/sublime-text/add_date.py ~/.config/sublime-text-3/Packages/User/
    ln -s ~/Dropbox/git/configs_master/sbia-pc125-cinn/sublime-text/my_shift_newLine.sublime-macro/ ~/.config/sublime-text-3/Packages/User/

Things that cannot be synced in subdirs:

- ``*.sublime-macro``
. ``*.sublime-settings``

****************************
Preferences.sublime-settings
****************************


******************************
Default (Linux).sublime-keymap
******************************


#######################
Sublime-Text References
#######################
http://docs.sublimetext.info/en/latest/index.html

******************************************
Scope info (for snippets and build system)
******************************************
- https://gist.github.com/iambibhas/4705378

*****************
Build system info
*****************
- http://docs.sublimetext.info/en/latest/file_processing/build_systems.html
- http://sublimetext.info/docs/en/reference/build_systems.html