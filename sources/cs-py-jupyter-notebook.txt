python-jupyter-notebook
"""""""""""""""""""""""

.. contents:: **Table of Contents**
    :depth: 2



#########################
Ipython notebook defaults
#########################
.. code-block:: python

    import seaborn as sns
    sns.set_style("whitegrid")
    sns.set_context("notebook", rc={'figure.figsize':(14,10)})

    import pandas as pd
    pd.set_option('display.max_rows', 20)
    pd.set_option('precision',4)


********************
Frequently used config
********************
.. code:: python

    import ipywidgets as widgets
    from IPython.widgets import interact, interactive
    from IPython.display import display

    import seaborn as sns
    sns.set_style("whitegrid")
    sns.set_context("notebook", rc={'figure.figsize':(14,10)})

    import pandas as pd
    pd.set_option('display.max_rows', 20)
    pd.set_option('precision',4)

********************
widgets
********************
.... code:: python

    # the below two are equivalent
    from IPython.html.widgets import interact, interactive
    from ipywidgets.widgets import interact, interactive
        <function ipywidgets.widgets.interaction.interact>
        <function ipywidgets.widgets.interaction.interactive>

All widget types
====================
.. code:: python


    widgets.Widget.widget_types.values()
    Out[92]:

        [ipywidgets.widgets.widget_string.Text,
         ipywidgets.widgets.widget_box.Box,
         ipywidgets.widgets.widget_controller.Axis,
         ipywidgets.widgets.widget_bool.Checkbox,
         ipywidgets.widgets.widget_int.IntRangeSlider,
         ipywidgets.widgets.widget_selection.RadioButtons,
         ipywidgets.widgets.widget_string.HTML,
         ipywidgets.widgets.widget_float.FloatRangeSlider,
         ipywidgets.widgets.widget_box.PlaceProxy,
         ipywidgets.widgets.widget_selection.ToggleButtons,
         ipywidgets.widgets.widget_int.IntText,
         ipywidgets.widgets.widget_selection.Dropdown,
         ipywidgets.widgets.widget_bool.Valid,
         ipywidgets.widgets.widget_bool.ToggleButton,
         ipywidgets.widgets.widget_float.FloatSlider,
         ipywidgets.widgets.widget_int.IntProgress,
         ipywidgets.widgets.widget_selection.SelectMultiple,
         ipywidgets.widgets.widget_float.FloatProgress,
         ipywidgets.widgets.widget_string.Latex,
         ipywidgets.widgets.widget_box.FlexBox,
         ipywidgets.widgets.widget_string.Textarea,
         ipywidgets.widgets.widget_float.BoundedFloatText,
         ipywidgets.widgets.widget_controller.Button,
         ipywidgets.widgets.widget_selection.Select,
         ipywidgets.widgets.widget_selectioncontainer.Accordion,
         ipywidgets.widgets.widget_float.FloatText,
         ipywidgets.widgets.widget_image.Image,
         ipywidgets.widgets.widget_button.Button,
         ipywidgets.widgets.widget_int.BoundedIntText,
         ipywidgets.widgets.widget_box.Proxy,
         ipywidgets.widgets.widget_selectioncontainer.Tab,
         ipywidgets.widgets.widget_int.IntSlider,
         ipywidgets.widgets.widget_controller.Controller]

********************
Now config
********************

.. code:: python

    import matplotlib as mpl
    import matplotlib.pyplot as plt
    import pandas as pd
    import seaborn as sns

    %matplotlib inline
    #========================================================================#
    # matplotlib
    #========================================================================#
    import matplotlib as mpl

    %matplotlib inline
    rcParam = {
        'figure.figsize': (12,10),
        'font.weight': 'bold',
        'axes.labelsize': 24.0,
        'axes.titlesize': 24.0,
        'axes.titleweight': 'bold',
        'legend.fontsize': 18,
        'xtick.labelsize': 18,
        'ytick.labelsize': 18,
    }
    for key,value in rcParam.iteritems():
        mpl.rcParams[key] = value

    # brute froce way
    mpl.rcParams['figure.figsize'] = (14,10)
    mpl.rcParams['font.weight'] = 'bold'
    mpl.rcParams['font.size'] = 44.0

    mpl.rcParams['figure.edgecolor'] = 'black' # <- noeffect
    mpl.rcParams['axes.labelsize']=24.0
    mpl.rcParams['axes.titlesize']=24.0
    mpl.rcParams['axes.titleweight'] = 'bold'
    mpl.rcParams['legend.fontsize'] = 18
    mpl.rcParams['xtick.labelsize'] = 14
    mpl.rcParams['ytick.labelsize'] = 14

    # to restore default
    mpl.rcdefaults()

    #========================================================================#
    # pandas
    #========================================================================#
    # pd.set_option('display.height', 55)
    pd.set_option('display.max_rows', 20)
    # pd.set_option('display.max_columns', 50)
    # pd.set_option('display.width', 5)
    # pd.reset_option('all')
    # pd.set_option('expand_frame_repr', False)
    pd.set_option('precision',4)
    # pd.reset_option('precision')


    # see bottom of api http://pandas.pydata.org/pandas-docs/stable/api.html
    # pd.describe_option()
    # pd.reset_option()
    # pd.get_option()
    # pd.set_option()
    # pd.option_context(*args)   Context manager to temporarily set options in the with statement context.

    #========================================================================#
    # seaborn
    #========================================================================#
    sns.set_style("whitegrid")
    sns.set_context("notebook", rc={'figure.figsize':(14,10)})

    # to see all rc options, type this
    mpl.rc_params()
    sns.axes_style()