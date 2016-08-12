.. _qsubber:

qsubber
"""""""
.. contents:: **Table of Contents**
    :depth: 2

Test ref link to :ref:`regexp`

###########
qsub helper
###########
.. code-block:: bash

    qsub-run python tobpnc_save_bct_csv0721.py 0.1 True

    # create my own qsub-run script that suppresses email
    myqsub-run.sh python tobpnc_save_bct_csv0721.py 0.1 True

####################
qsub helper (old, pre April 2016  
####################

********************
A 3 step receipe for matlab
********************


.. code-block:: bash

  tw_mcc myprog.m
  qsub-run -c ./myprog > myprog.sh  # <- don't forget to include "./"
  qsub myprog.sh

********************
``memrec`` (to evaluate appropriate ``h_vmem`` value
********************
.. code-block:: bash

  memrec -d 5 ./myprog & # "-d 5" makes recording every 5 sec

- Run above to make recordings every 5 sec, and output memory usage to ``memprofile.txt``
- ``memprofile.txt`` has 3 columns:

  (\1) **SecondsRunning** (2) **ProcessMemory** (3) **ChildMemory**
- Set ``h_vmem`` at 10~\15% above (2)+(3) above  


********************
``qstat``
********************
.. code-block:: bash

  qstat -r
  qstat -r | egrep -i "full jobname"
  qstat -j job-ID | grep usage
  qstat -u '*' # <- see all users

  # delete jobs
  qdel JOBID

********************
``/usr/bin/time`` to see multithreaded or not
********************
.. code-block:: bash

  /usr/bin/time -pv myprog

Or just simply run the program, and use ``top`` to evaluate cpu usage  
    