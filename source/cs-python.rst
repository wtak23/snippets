

Python
""""""
.. contents:: **Table of Contents**
    :depth: 2





###############################
Random Stack-overflow questions
###############################

**********************************************
When plt.tight_layout doesn't work as expected
**********************************************
.. code-block:: python

    #http://stackoverflow.com/questions/8248467/matplotlib-tight-layout-doesnt-take-into-account-figure-suptitle
    plt.subplots_adjust(top=1.25)
    #plt.tight_layout()

**********************
Swap 2 items in a list
**********************
- http://stackoverflow.com/questions/2493920/how-to-switch-position-of-two-items-in-a-python-list

  - ``foo[i], foo[j] = foo[j], foo[i]``

****************************************
Check all items in list or dict is equal
****************************************

- http://stackoverflow.com/questions/3844801/check-if-all-elements-in-a-list-are-identical
- http://stackoverflow.com/questions/3787908/python-determine-if-all-items-of-a-list-are-the-same-item

.. code-block:: python

    # My favorite
    len(set(items)) == 1

    # incase of dict
    len(set(dict_var.values()))==1


#######
Disk IO
#######

************************
Write list items to text
************************
- http://stackoverflow.com/questions/899103/writing-a-list-to-a-file-with-python

.. code-block:: python

    # My favorite
    out_txt_path = os.path.join(output_dir,'bblid_matched_seed{}.txt'.format(seed_matching))
    with open(out_txt_path,'w') as f:
        f.write('\n'.join(df_pnc2['bblid'].tolist()))

    #=========================================================================#
    # others
    #=========================================================================#
    outfile.write("\n".join(itemlist))

    for item in thelist:
      thefile.write("%s\n" % item)

########################
Seaborn and Pandas plots
########################

- http://stackoverflow.com/questions/26413185/how-to-recover-matplotlib-defaults-after-setting-stylesheet

************
mpl and sns?
************
- http://stackoverflow.com/questions/28430385/seaborn-cycle-through-colours-with-matplotlib-scatter

*************
Color palette
*************
- Great demo of **built-in** palettes: http://chrisalbon.com/python/seaborn_color_palettes.html

Do this in sns 

.. code-block:: python

    sns.set_palette('muted') # <- looks less glaring to the eye
    #https://stanford.edu/~mwaskom/software/seaborn/generated/seaborn.color_palette.html



  Matplotlib paletes can be specified as reversed palettes by appending “_r” to 
  the name or as dark palettes by appending “_d” to the name. 

- https://stanford.edu/~mwaskom/software/seaborn/tutorial/color_palettes.html
- https://stanford.edu/~mwaskom/software/seaborn/generated/seaborn.color_palette.html
- http://matplotlib.org/examples/color/named_colors.html
- http://matplotlib.org/examples/color/colormaps_reference.html

.. code-block:: python
    :linenos:

    # "Paired" is pretty nice 
    tw.figure()
    sns.countplot(x='age_bins',hue='hue',data=df_joined,order=labels_,
                  hue_order=sorted(df_joined['hue'].unique().tolist()),
                  palette=sns.color_palette('Paired'))

##########################
Python commands from shell
##########################
- http://stackoverflow.com/questions/2043453/executing-python-multi-line-statements-in-the-one-line-command-line

.. code-block:: bash
    :linenos:

    # for multiline commands
    echo -e "import sys\nfor r in range(10): print 'rob'" | python

    user@host:~$ python -c "import sys
    > for r in range(10): print 'rob'"

    # meh, better yet use ipython for multiline commands
    ipython -c "import matplotlib as mpl; print mpl.matplotlib_fname()"
    ipython -c "import matplotlib as mpl; print mpl.matplotlib_fname()" | xargs subl

##################
Matplotlib styling
##################
http://matplotlib.org/users/style_sheets.html

.. code-block:: bash
    :linenos:

    # to edit matplotlibbrc file
    ipython -c "import matplotlib as mpl; print mpl.matplotlib_fname()" | xargs 
    subl $(ipython -c "import matplotlib as mpl; print mpl.matplotlib_fname()")

*******************
Default color cycle
*******************
- http://stackoverflow.com/questions/9397944/default-color-cycle-with-matplotlib
- http://matplotlib.org/examples/color/color_cycle_demo.html
- http://matplotlib.org/devel/color_changes.html

Changed these in ``matplotlibrc``

.. code-block:: python

    axes.color_cycle    : b, g, r, c, m, y, k # <- original

    # edited
    axes.color_cycle    : b, r, g, c, m, y, k  # color cycle for plot lines
                                                # as list of string colorspecs:
                                                # single letter, long name, or
                                                # web-style hex


***************
Colormap helper
***************
- http://matplotlib.org/examples/color/colormaps_reference.html
- http://chrisalbon.com/python/seaborn_color_palettes.html

Add "_r" at the end to reverse colormap

.. code-block:: python

    tw.imconnmat(np.random.randn(50,50),newfig='f',cmap='gray')
    tw.imconnmat(np.random.randn(50,50),newfig='f',cmap='gray_r')

##################
installing modules
##################
http://scicomp.stackexchange.com/questions/2987/what-is-the-simplest-way-to-do-a-user-local-install-of-a-python-package

.. code-block:: bash
    :linenos:

    #http://scicomp.stackexchange.com/questions/2987/what-is-the-simplest-way-to-do-a-user-local-install-of-a-python-package
    python setup.py install --user
    pip install py4j --user
    pip install --upgrade sphinx_rtd_theme --user




#######
gochtas
#######

***************************************************
careful with array slicing! may change array values
***************************************************
http://stackoverflow.com/questions/18155972/unexpected-result-in-numpy-array-slicing-view-vs-copy


.. code-block:: python
    :linenos:
    :emphasize-lines: 2-6

    X = tw.data.tob_pnc.load_connectome()[0]

    # this won't change X
    tmp = X[np.arange(10)]
    tmp *= 0
    print X
        Out[215]: 
        array([[  1.96500000e+00,   8.85000000e-01,   1.51500000e+00, ...,
                  6.57650000e+01,   8.36055000e+02,   1.43835000e+02],
               [  1.70000000e-01,   3.59500000e+00,   1.50000000e-01, ...,
                  1.13330000e+02,   5.37860000e+02,   3.42055000e+02],
               [  1.75000000e-01,   5.49500000e+00,   7.93500000e+00, ...,
                  4.44100000e+01,   7.48985000e+02,   1.38840000e+02],
               ..., 
               [  2.94000000e+00,   1.14000000e+01,   1.00000000e+00, ...,
                  6.96750000e+01,   1.85573500e+03,   1.25484000e+03],
               [  4.80000000e-01,   2.80450000e+01,   3.57000000e+00, ...,
                  3.25420000e+02,   2.39266500e+03,   1.66609500e+03],
               [  3.00000000e-01,   4.87000000e+00,   2.16500000e+00, ...,
                  1.51200000e+02,   1.49544000e+03,   9.05030000e+02]])

    # this will! array slicing only creates a view!
    tmp = X[:10]
    tmp *= 0

    print X
        Out[204]: 
        array([[  0.00000000e+00,   0.00000000e+00,   0.00000000e+00, ...,
                  0.00000000e+00,   0.00000000e+00,   0.00000000e+00],
               [  0.00000000e+00,   0.00000000e+00,   0.00000000e+00, ...,
                  0.00000000e+00,   0.00000000e+00,   0.00000000e+00],
               [  0.00000000e+00,   0.00000000e+00,   0.00000000e+00, ...,
                  0.00000000e+00,   0.00000000e+00,   0.00000000e+00],
               ..., 
               [  2.94000000e+00,   1.14000000e+01,   1.00000000e+00, ...,
                  6.96750000e+01,   1.85573500e+03,   1.25484000e+03],
               [  4.80000000e-01,   2.80450000e+01,   3.57000000e+00, ...,
                  3.25420000e+02,   2.39266500e+03,   1.66609500e+03],
               [  3.00000000e-01,   4.87000000e+00,   2.16500000e+00, ...,
                  1.51200000e+02,   1.49544000e+03,   9.05030000e+02]])

#########
decorator
#########
- http://stackoverflow.com/questions/739654/how-can-i-make-a-chain-of-function-decorators-in-python?rq=1
- http://stackoverflow.com/questions/489720/what-are-some-common-uses-for-python-decorators
- http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/

.. code-block:: python
    :linenos:

    def print_warning(fn):
        def wrapper():
            warn('module-name changed from "pnc_tob" to "tob_pnc" on 06/22/2016',ImportWarning)
            print('module-name changed from "pnc_tob" to "tob_pnc" on 06/22/2016')
        return wrapper
    
    @print_warning
    def get_matched_subjects_0614():
        """ Get list of *matched* pnc/tob subjects
        pass

Using with arguments (``*args, **kwargs``)

.. code-block:: python
    :linenos:

    def logger(func):
        def inner(*args, **kwargs): #1
            print "Arguments were: %s, %s" % (args, kwargs)
            return func(*args, **kwargs) #2
        return inner

    >>> @logger
    ... def foo1(x, y=1):
    ...     return x * y
    >>> @logger
    ... def foo2():
    ...     return 2
    >>> foo1(5, 4)
    Arguments were: (5, 4), {}
    20
    >>> foo1(1)
    Arguments were: (1,), {}
    1
    >>> foo2()
    Arguments were: (), {}
    2

#########################
Plotting - short snippets
#########################

***********
Cool tricks
***********
.. code-block:: python
    :linenos:

    import matplotlib as mpl
    mpl.get_backend()
    mpl.is_interactive()
    mpl.get_home()

    #========================================================================#
    # Window manager 
    # http://doc.qt.io/qt-4.8/qwidget.html
    #========================================================================#
    mngr = plt.get_current_fig_manager()
    mngr.resize(1000,100)        # (width,height) in pixels
    mngr.window.showFullScreen() # maximize figure
    mngr.window.showNormal()     # go back to normal
    mngr.window.setGeometry(1800,100,640, 545)
    geom = mngr.window.geometry()
    x,y,dx,dy = geom.getRect()
    # "mngr" has the following stuffs"
    #  'canvas',
    #  'destroy',
    #  'full_screen_toggle',
    #  'get_window_title',
    #  'key_press',
    #  'key_press_handler_id',
    #  'num',
    #  'resize',
    #  'set_window_title',
    #  'show',
    #  'show_popup',
    #  'toolbar',
    #  'window'

    from pylab import subplot_tool
    subplot_tool()


    #%% xticklabel rotate
    # <your code here>
    locs, labels = plt.xticks()
    plt.setp(labels, rotation=45)
    plt.getp(plt.gcf())
    plt.getp(plt.gca())

    #========================================================================#
    # Rotate xlabel
    #========================================================================#
    #http://matplotlib.org/users/artists.html
    import numpy as np
    import matplotlib.pyplot as plt

    # plt.figure creates a matplotlib.figure.Figure instance
    fig = plt.figure()
    rect = fig.patch # a rectangle instance
    rect.set_facecolor('lightgoldenrodyellow')

    ax1 = fig.add_axes([0.1, 0.3, 0.4, 0.4])
    rect = ax1.patch
    rect.set_facecolor('lightslategray')

    for label in ax1.xaxis.get_ticklabels():
        # label is a Text instance
        label.set_color('red')
        label.set_rotation(45)
        label.set_fontsize(16)

    for line in ax1.yaxis.get_ticklines():
        # line is a Line2D instance
        line.set_color('green')
        line.set_markersize(25)
        line.set_markeredgewidth(3)

    #========================================================================#
    # Cool way to cycle through colormaps: use zip
    # from http://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_vs_lda.html
    #========================================================================#
    plt.figure()
    for c, i, target_name in zip("rgb", [0, 1, 2], target_names):
        plt.scatter(X_r2[y == i, 0], X_r2[y == i, 1], c=c, label=target_name)
    plt.legend()
    plt.title('LDA of IRIS dataset')

*****************
Plotting Snippets
*****************
.. code-block:: python
    :linenos:

    # getting step function (just a wrapper) 
    # http://stackoverflow.com/questions/15188005/linestyle-in-matplotlib-step-function
    # [‘default’ | ‘steps’ | ‘steps-pre’ | ‘steps-mid’ |‘steps-post’]
    df.plot(kind='line', drawstyle='steps') # <- pd data frame

    # remove rotation (including seaborn)
    # http://stackoverflow.com/questions/27037241/changing-the-rotation-of-tick-labels-in-seaborn-heatmap
    plt.yticks(rotation=0) 
    plt.xticks(rotation=0) 

    # for pandas dataframe, just include "rot" 
    nan_group.plot(kind='bar', stacked=True, grid=False,rot=88,fontsize=12)

##########
Exceptions
##########
.. code-block:: python
    :linenos:

    # https://docs.python.org/2/tutorial/errors.html <- list of builtin exceptions
    # http://www.pythonforbeginners.com/error-handling/python-try-and-except
    #%% exceptions can be written in many ways 
    #http://anandology.com/python-practice-book/object_oriented_programming.html#errors-and-exceptions
    #==========================================================================
    # catch all exceptions
    try:
        ...
    except:
    
    # catch just one exception
    try:
        ...
    except IOError:
        ...
    
    # catch one exception, but provide the exception object
    try:
        ...
    except IOError, e:
        ...
    
    # catch more than one exception
    try:
        ...
    except (IOError, ValueError), e:
        ...

    #========================================================================#
    # It is possible to have more than one except statements with one try.
    #========================================================================#
    try:
        ...
    except IOError, e:
        print >> sys.stderr, "Unable to open the file (%s): %s" % (str(e), filename)
        sys.exit(1)
    except FormatError, e:
        print >> sys.stderr, "File is badly formatted (%s): %s" % (str(e), filename)
    
    #=========================================================================
    # The try statement can have an optional else clause, which is executed 
    # only if no exception is raised in the try-block.
    #=========================================================================
    try:
        ...
    except IOError, e:
        print >> sys.stderr, "Unable to open the file (%s): %s" % (str(e), filename)
        sys.exit(1)
    else:
        print "successfully opened the file", filename
    #=========================================================================
    # There can be an optional else clause with a try statement, which is executed 
    # irrespective of whether or not exception has occured.
    #=========================================================================
    try:
        ...
    except IOError, e:
        print >> sys.stderr, "Unable to open the file (%s): %s" % (str(e), filename)
        sys.exit(1)
    finally:
        delete_temp_files()

    #=========================================================================
    # Exception is raised using the raised keyword.
    #=========================================================================
    raise Exception("error message")


    #=========================================================================
    #%%All the exceptions are extended from the built-in Exception class.
    #=========================================================================
    class ParseError(Exception):
    pass
    #%% exceptions (note: exceptions are classes!  See tutorial 9.8)

#############
Clever tricks
#############
.. code-block:: python
    :linenos:

    countries = np.array(['US', 'UK', 'GR', 'JP'])
    key = countries[np.random.randint(0, 4, 1000)]
    key

    Out[53]:
    array(['JP', 'GR', 'GR', 'GR', 'GR', 'JP', 'GR', 'GR', 'US', 'UK', 'US',
           'GR', 'US', 'GR', 'GR', 'JP', 'UK', 'UK', 'GR', 'US', 'GR', 'JP',
           'JP', 'GR', 'GR', 'JP', 'JP', 'US', 'JP', 'US', 'JP', 'JP', 'UK',
           'GR', 'GR', 'US', 'JP', 'GR', 'JP', 'GR', 'GR', 'UK', 'JP', 'JP',
           'JP', 'JP', 'JP', 'GR', 'US', 'GR', 'UK', 'US', 'JP', 'US', 'JP',
           'GR', 'US', 'JP', 'US', 'UK', 'JP', 'JP', 'JP', 'US', 'UK', 'UK',
           'UK', 'UK', 'US', 'US', 'US', 'US', 'UK', 'GR', 'GR', 'UK', 'JP',
           'UK', 'GR', 'UK', 'UK', 'US', 'GR', 'US', 'JP', 'US', 'US', 'UK',
           'UK', 'UK', 'US', 'US', 'US', 'JP', 'GR', 'GR', 'US', 'GR', 'UK',
           'JP', 'GR', 'JP', 'JP', 'GR', 'US', 'JP', 'GR', 'US', 'JP', 'UK',