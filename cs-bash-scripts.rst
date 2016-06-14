Here snippets and explanations for writing bash scripts


`[Parent Directory] <./>`_

.. contents:: **Table of Contents**
    :depth: 2

.. sectnum::    
    :start: 1    

###############################################################################
``command`` vs $(command)
###############################################################################
- $(commands) does the same thing as backticks, but you can nest them.
- `source <http://stackoverflow.com/questions/2657012/how-to-properly-nest-bash-backticks>`_

.. code:: bash

    echo $(date +"%Y-%m-%d_%H:%M:%S")

###############################################################################
variable name convention
###############################################################################
- UPPERCASE for env-vars and constant values
- lowercase for local vars

http://unix.stackexchange.com/questions/42847/are-there-naming-conventions-for-variables-in-shell-scripts

###############################################################################
How to expand ~ (tilde)
###############################################################################
http://stackoverflow.com/questions/3963716/how-to-manually-expand-a-special-variable-ex-tilde-in-bash
``echo ${HOME}``

.. code:: bash

    out_dir="${HOME}/data/tob/dti_volumes"
    echo ${out_dir}
    echo ${out_dir}/subdirec


###############################################################################
Create directory if it doesn't exist 06-14-2016 (00:17)
###############################################################################
- ``-p`` option does it, but for pedagogical purpose...
- http://stackoverflow.com/questions/4906579/how-to-use-bash-to-create-a-folder-if-it-doesnt-already-exist

.. code:: bash

    if [ ! -d /home/mlzboy/b2c2/shared/db ] 
    then
        mkdir -p /home/mlzboy/b2c2/shared/db
    fi