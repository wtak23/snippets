`[Parent Directory] <./>`_

.. contents:: **Table of Contents**
    :depth: 2

.. sectnum::    
    :start: 1    

####################
Moving and copying
####################
http://ss64.com/bash/cp.html

**Remark**: when handling directories or *contents* of directories, becareful with the ending backslash ``/``.

.. code:: bash

    # rename a directory (note '/' after directory name has NO impact here,  there are cases I should be careful of the backslash)
    mv /home/user/oldname /home/user/newname

    # copy entire directory (copy folder test, and paste as test2)..-R for recursive directories
    cp -R test test2    

    # copy files *inside* the folder "test/" inside folder "target" (doesn't copy the folder itself)
    mkdir source target; cd source; touch a b c; cd ..
    cp -r source/* target # <= files "a,b,c" copied to folder target



    #=========================================================================#
    # copy 3 folders "test/" "test2/" "test3/" and file myfirst.exe inside a new directory called "cp_practice"
    #=========================================================================#
    mkdir cp_practice
    cp -R test test2 test3 myfirst.exe cp_practice/
    rm -r test test2 test3 myfirst.exe # clean up abobve results if desired