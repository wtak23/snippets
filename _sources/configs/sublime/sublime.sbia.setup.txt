################
SBIA Workstation
################

The two most important files:

1. ``Preferences.sublime-settings`` --- global setup
2. ``Default (Linux).sublime-keymap`` --- keyboard shortcuts

  - (saved as ``keyboard_shortcut_sbia.sublime-keymap`` locally)

*********
File-tree
*********
`Github link <./>`_

08-18-2016 (12:48)

.. code-block:: bash

    $ tree -L 1 --dirsfirst
    .
    ├── snippets
    ├── synced_by_files
    ├── synced_by_folder
    ├── keyboard_shortcut_sbia.sublime-keymap
    ├── Preferences_sbia.sublime-settings
    ├── sublime.references.rst
    └── sublime.sbia.setup.rst

    3 directories, 4 files


- ``./synced_by_folder`` 

  - contains files that must directly reside under ``~/.config/sublime-text-3/Packages/User`` (subfolders not allowed)
  - examples: ``*.sublime-settings``, ``*.sublime-macros``
- ``./snippets`` 

  - contains my sublime **snippets** (gawd I love this functionality)
- ``./synced_by_files`` 

  - contains files that can be synced as subfolders in ``User`` directory in Sublime

/home/takanori/Dropbox/git/snippet/source/configs/sublime/keyboard_shortcut_sbia.sublime-keymap

************
global setup
************
.. code-block:: bash

    # global setups (settings & keyboard)
    ln -s "$HOME/Dropbox/git/snippet/source/configs/sublime/keyboard_shortcut_sbia.sublime-keymap" \
        "$HOME/.config/sublime-text-3/Packages/User/Default (Linux).sublime-keymap"    
    ln -s "$HOME/Dropbox/git/snippet/source/configs/sublime/Preferences_sbia.sublime-settings" \
        "$HOME/.config/sublime-text-3/Packages/User/Preferences.sublime-settings"

    # folders
    ln -s ~/Dropbox/git/snippet/source/configs/sublime/snippets \
        ~/.config/sublime-text-3/Packages/User/snippets
    ln -s ~/Dropbox/git/snippet/source/configs/sublime/synced_by_folder \
        ~/.config/sublime-text-3/Packages/User/synced_by_folder

***************
file-wise setup
***************
- macros and sublime-setting files must be copied directly under the ``User`` 
  directory

Last update: 08-18-2016 (02:28)

.. code-block:: bash
  
    ln -s ~/Dropbox/git/snippet/source/configs/sublime/synced_by_files/add_date.py \
        ~/.config/sublime-text-3/Packages/User/add_date.py    
    ln -s ~/Dropbox/git/snippet/source/configs/sublime/synced_by_files/Diff.sublime-settings \
        ~/.config/sublime-text-3/Packages/User/Diff.sublime-settings
    ln -s ~/Dropbox/git/snippet/source/configs/sublime/synced_by_files/my_shift_newLine.sublime-macro \
        ~/.config/sublime-text-3/Packages/User/my_shift_newLine.sublime-macro
    ln -s ~/Dropbox/git/snippet/source/configs/sublime/synced_by_files/Anaconda.sublime-settings \
        ~/.config/sublime-text-3/Packages/User/Anaconda.sublime-settings
    ln -s ~/Dropbox/git/snippet/source/configs/sublime/synced_by_files/FoldPython.sublime-settings \
        ~/.config/sublime-text-3/Packages/User/FoldPython.sublime-settings
    ln -s ~/Dropbox/git/snippet/source/configs/sublime/synced_by_files/OmniMarkupPreviewer.sublime-settings \
        ~/.config/sublime-text-3/Packages/User/OmniMarkupPreviewer.sublime-settings
    ln -s ~/Dropbox/git/snippet/source/configs/sublime/synced_by_files/Python.sublime-settings \
        ~/.config/sublime-text-3/Packages/User/Python.sublime-settings



