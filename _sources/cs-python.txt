
Python
""""""

.. note:: self-note when updating this rst note
    
    ``ctrl+f`` these key-words:

    - "Top-mpl" to get header for matplotlib related notes
    - "Top-pandas" to get header for pandas related notes


.. contents:: `Contents`
   :depth: 2
   :local:

Every once in a while, I'll try to organize below by **category**

(maybe categorized via modules? eg, pandas, np, ....think about it)

``$ python -m SimpleHTTPServer 8000``


###############################
Random Stack-overflow questions
###############################

***********************
A bit on python unicode
***********************
- https://docs.python.org/2.7/howto/unicode.html
- http://stackoverflow.com/questions/9942594/unicodeencodeerror-ascii-codec-cant-encode-character-u-xa0-in-position-20
- google search query used: https://www.google.com/#q=Encoding+error%3A+%27ascii%27+codec+can%27t+encode+character+u%27\xe4%27+in+position+5
- https://github.com/sphinx-doc/sphinx/issues/1739

>>> # This is a classic python unicode pain point! Consider the following:
>>> a = u'bats\u00E0'
>>> # All good so far, but if we call str(a), let's see what happens:
>>> print a
batsà
>>> str(a)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeEncodeError: 'ascii' codec can't encode character u'\xe0' in position 4: ordinal not in range(128)
>>> # To fix the error, encode the bytes explicitly with .encode and tell python what codec to use:
>>> a.encode('utf-8')
'bats\xc3\xa0'
>>> print a.encode('utf-8')
batsà

  The issue is that when you call str(), python uses the default character encoding to try and encode the bytes you gave it, which in your case are sometimes representations of unicode characters. To fix the problem, you have to tell python how to deal with the string you give it by using .encode('whatever_unicode'). Most of the time, you should be fine using utf-8.

************************************************************************
Locale thing (since i'm getting errors in sphinx regarding unicode error
************************************************************************
- https://github.com/sphinx-doc/sphinx/issues/1739
- https://www.google.com/#q=sphinx+encoding+error
- http://masasuzu.hatenablog.jp/entry/20110313/1299997912

.. code-block:: bash

    $ locale
    LANG=en_US.UTF-8
    LANGUAGE=
    LC_CTYPE="en_US.UTF-8"
    LC_NUMERIC="en_US.UTF-8"
    LC_TIME="en_US.UTF-8"
    LC_COLLATE="en_US.UTF-8"
    LC_MONETARY="en_US.UTF-8"
    LC_MESSAGES="en_US.UTF-8"
    LC_PAPER="en_US.UTF-8"
    LC_NAME="en_US.UTF-8"
    LC_ADDRESS="en_US.UTF-8"
    LC_TELEPHONE="en_US.UTF-8"
    LC_MEASUREMENT="en_US.UTF-8"
    LC_IDENTIFICATION="en_US.UTF-8"
    LC_ALL=

In python:

- http://stackoverflow.com/questions/2276200/changing-default-encoding-of-python

.. code-block:: python
    
    # sys.setdefaultencoding() does not exist, here!
    import sys
    reload(sys)  # Reload does the trick!
    sys.setdefaultencoding('UTF8')

::

    In [1]: import sys 

    In [2]: sys.getdefaultencoding()
    Out[2]: 'ascii'     

    In [3]: sys.getfilesystemencoding()
    Out[3]: 'UTF-8'

    In [4]: sys.setdefaultencoding('UTF8')
    ---------------------------------------------------------------------------
    AttributeError                            Traceback (most recent call last)
    <ipython-input-4-daa3932f9332> in <module>()
    ----> 1 sys.setdefaultencoding('UTF8')

    AttributeError: 'module' object has no attribute 'setdefaultencoding'

    In [5]: #  reload does the trick apparently

    In [6]: reload(sys);

    In [7]: sys.setdefaultencoding('UTF8')

    In [8]: sys.getdefaultencoding()
    'UTF8'

******************************
what does sitecustomize.py do?
******************************
- http://stackoverflow.com/questions/10693706/creating-a-secondary-site-packages-directory-and-loading-packages-from-pth-fil
- http://masasuzu.hatenablog.jp/entry/20110313/1299997912
- http://nedbatchelder.com/blog/201001/running_code_at_python_startup.html

****************************************
Things you can do with a **file** object
****************************************
I always forget the exact syntax for these...

- https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files
- https://tedboy.github.io/python_stl/generated/generated/__builtin__.file.html



**********
simplejson
**********
hmmm, look into this module?

- http://stackoverflow.com/questions/899103/writing-a-list-to-a-file-with-python


>>> import simplejson
>>> f = open('output.txt', 'w')
>>> simplejson.dump([1,2,3,4], f)
>>> f.close()

******************************
Find first occurence in a list
******************************
- http://stackoverflow.com/questions/2361426/what-is-the-best-way-to-get-the-first-item-from-an-iterable-matching-a-condition
- http://stackoverflow.com/questions/9868653/find-first-list-item-that-matches-criteria

.. code-block:: python

    next(x for x in the_iterable if x > 3)
    next(obj for obj in objs if obj.val==5)

    # next also provides a default value in case object does not exist
    next((i for i in range(500) if i > 600), 600)



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

##########
Exceptions
##########
- http://stackoverflow.com/questions/3702675/how-to-print-the-full-traceback-without-halting-the-program
- http://stackoverflow.com/questions/1483429/how-to-print-an-error-in-python
- http://stackoverflow.com/questions/4560288/python-try-except-showing-the-cause-of-the-error-after-displaying-my-variables


.. code-block:: python

    try:
        do_stuff()
    except Exception, err:
        print Exception, err

    #=========================================================================#
    # Use traceback and sys.exc_info to get more info
    #=========================================================================#
    import traceback
    import sys

    try:
        do_stuff()
    except Exception:
        # this appears to yiled the most info
        print(traceback.format_exc())
        # or
        print(sys.exc_info()[0])


*******************************
My most frequent *lazy* usecase
*******************************

>>> try:
>>>     fig_set_geom(pos)
>>> except Exception, err:
>>>     print err
name 'fig_set_geom' is not defined


>>> # more info using traceback.format_exc
>>> import traceback
>>> try:
>>>     fig_set_geom(pos)
>>> except:
>>>     print traceback.format_exc()
Traceback (most recent call last):
  File "<ipython-input-43-33c80ffe55e1>", line 3, in <module>
    fig_set_geom(pos)
NameError: name 'fig_set_geom' is not defined

##########
Top-pandas
##########
Keep adding pandas related notes/snippets here

******************************************************
Pandas - check if all columns are equal in a DataFrame
******************************************************
- http://stackoverflow.com/questions/22701799/pandas-dataframe-find-rows-where-all-columns-equal

.. code-block:: python

    # approach: check all columns against the first column using eq
    df.eq(df.iloc[:, 0], axis=0)
          a     b      c      d
    0  True  True   True   True
    1  True  True   True   True
    2  True  True   True   True

    df.eq(df.iloc[:, 0], axis=0).all(1)
    0     True
    1     True
    2     True
    dtype: bool

    # so to check if ALL columns match, apply np.all to above
    np.all(df.eq(df.iloc[:, 0], axis=0).all(1))
    True

#######
top-mpl
#######
Keep adding mpl related notes/snippets here

**********************************************
When plt.tight_layout doesn't work as expected
**********************************************
.. code-block:: python

    #http://stackoverflow.com/questions/8248467/matplotlib-tight-layout-doesnt-take-into-account-figure-suptitle
    plt.subplots_adjust(top=1.25)
    #plt.tight_layout()
    
*****************************
Append to existing axes title
*****************************
.. code-block:: python

    ax = plt.gca()
    ax.set_title(ax.get_title() + ' WHATEVER STRING') # <- append to title

***************************************
Change figure size of *existing* figure
***************************************
I have ``plt.figure(figsize=(10,8))`` option when creating figure, but how to 
change size of figure that already exists?  see below :)

- http://stackoverflow.com/questions/332289/how-do-you-change-the-size-of-figures-drawn-with-matplotlib

.. code-block:: python

    # ah, did not know the ``forward`` option below!    
    plt.gcf().set_size_inches(18.5, 10.5, forward=True)

####################################################################
Plotting and saving figure on remotely on server (on sge submission)
####################################################################
**References**

- http://stackoverflow.com/questions/4706451/how-to-save-a-figure-remotely-with-pylab
- http://stackoverflow.com/questions/21321292/using-matplotlib-when-display-is-undefined
- http://stackoverflow.com/questions/4930524/how-can-i-set-the-backend-in-matplotlib-in-python
- http://stackoverflow.com/questions/15455029/python-matplotlib-agg-vs-interactive-plotting-and-tight-layout
- http://stackoverflow.com/questions/3285193/how-to-switch-backends-in-matplotlib-python

.. code-block:: python

    # use **Agg** backend for non-interactive plotting w/o using X-server
    # (default on my workstation and interactive server is Qt4Agg)
    import matplotlib as mpl
    mpl.use('Agg') #<- needs to be called before modules from mpl is loaded

    # i like this better since i can set it anywhere in my code
    # (although it is am **experimental** feature) 
    # http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.switch_backend
    plt.switch_backend('Agg')    

One issue with the ``Agg`` backend: doesn't have the ``.window`` attribute
in the fig-manager (``plt.get_current_fig_manager().window`` doesn't exist, 
so can't set window position)

***********************************
Change i made to my figure function
***********************************
Just use ``try/exception`` in my ``fig_set_geom`` function.

- this way, i don't have to modify the calling script in any way when 
  running my script on sge-server 
- (this way, my script can be used in interactive-mode
  or server-mode without any changes)


.. code-block:: python

    # added below to my ``fig_set_geom`` function in my tak module
    try:
        mngr = plt.get_current_fig_manager()
        mngr.window.setGeometry(*pos)
    except Exception, err:
        str_warning = '\n'+str(err)+"\nAssign figure-size using pyplot"
        warnings.warn(str_warning)
        fig = plt.gcf()
        x_len = pos[2]/fig.dpi # <- convert from pixel to inches
        y_len = pos[3]/fig.dpi
        plt.gcf().set_size_inches(x_len,y_len,forward=True)


Going from pixel counts to inch size:

- http://stackoverflow.com/questions/13714454/specifying-and-saving-a-figure-with-exact-size-in-pixels


****************************************
Check if X11 is enabled in python script
****************************************
- http://stackoverflow.com/questions/8257385/automatic-detection-of-display-availability-with-matplotlib

.. code-block:: python

    # i do this
    if 'DISPLAY' not in os.environ.keys():
        plt.switch_backend('Agg')  # <- X11 display not available, so use non-interactive backend

    # in interactive mode, this key exists
    os.environ['DISPLAY']
    > Out[118]: ':0'

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