Plotly snippets (``cs-plotly``)
===============================

.. contents:: `Contents`
   :depth: 2
   :local:

.. code-block:: python

    import plotly
    import plotly.plotly as py
    import plotly.graph_objs as go
    import plotly.tools as tls
    import plotly.tools.FigureFactory as FF

#####################
Update layout posthoc
#####################

.. code-block:: python

    import plotly.plotly as py
    from plotly.tools import FigureFactory as FF
    import plotly.graph_objs as go

    import numpy as np

    X = np.random.rand(15, 15)
    dendro = FF.create_dendrogram(X)
    dendro['layout'].update({'width':800, 'height':500})
    py.iplot(dendro)

***************
Another example
***************
.. code-block:: python

    figure['layout'].update({'width':800, 'height':800,
                             'showlegend':False, 'hovermode': 'closest',
                             })
    # Edit xaxis
    figure['layout']['xaxis'].update({'domain': [.15, 1],
                                      'mirror': False,
                                      'showgrid': False,
                                      'showline': False,
                                      'zeroline': False,
                                      'ticks':""})
    # Edit xaxis2
    figure['layout'].update({'xaxis2': {'domain': [0, .15],
                                       'mirror': False,
                                       'showgrid': False,
                                       'showline': False,
                                       'zeroline': False,
                                       'showticklabels': False,
                                       'ticks':""}})

    # Edit yaxis
    figure['layout']['yaxis'].update({'domain': [0, .85],
                                      'mirror': False,
                                      'showgrid': False,
                                      'showline': False,
                                      'zeroline': False,
                                      'showticklabels': False,
                                      'ticks': ""})
    # Edit yaxis2
    figure['layout'].update({'yaxis2':{'domain':[.825, .975],
                                       'mirror': False,
                                       'showgrid': False,
                                       'showline': False,
                                       'zeroline': False,
                                       'showticklabels': False,
                                       'ticks':""}})

###########
3d subplots
###########
https://plot.ly/python/3d-subplots/

.. code-block:: python

    from plotly import tools
    fig = tools.make_subplots(rows=2, cols=2,
                              specs=[[{'is_3d': True}, {'is_3d': True}],
                                     [{'is_3d': True}, {'is_3d': True}]])

##############
Embed in ipynb
##############
.. code-block:: python

    import plotly.tools as tls
    tls.embed('https://plot.ly/~otto.stegmaier/609/previous-min-and-max-prices/')

###############
static image IO
###############
https://plot.ly/python/static-image-export/

.. code-block:: python

    fig = go.Figure(data=data, layout=layout)

    py.image.save_as(fig, filename='a-simple-plot.png')
    py.image.ishow(fig)

    # show in ipynb
    from IPython.display import Image
    Image('a-simple-plot.png')

    fig = py.get_figure('chris', '1638')
    py.image.save_as(fig,'chris-plot.png
    Image('chris-plot.png') # Display a static image

#########
Getfigure
#########
.. code-block:: python

    # get_figure downloads a figure from plot.ly or Plotly Enterprise. 
    # You need to provide credentials to download figures: https://plot.ly/python/getting-started/
    fig = py.get_figure('https://plot.ly/~jackp/8715', raw=True)
    iplot(fig)

####################
Demo - MPL to plotly
####################
From https://plot.ly/python/ipython-notebook-tutorial/

.. code-block:: python

    fig1 = plt.figure()
    # Make a legend for specific lines.
    import matplotlib.pyplot as plt
    import numpy as np


    t1 = np.arange(0.0, 2.0, 0.1)
    t2 = np.arange(0.0, 2.0, 0.01)

    # note that plot returns a list of lines.  The "l1, = plot" usage
    # extracts the first element of the list into l1 using tuple
    # unpacking.  So l1 is a Line2D instance, not a sequence of lines
    l1, = plt.plot(t2, np.exp(-t2))
    l2, l3 = plt.plot(t2, np.sin(2 * np.pi * t2), '--go', t1, np.log(1 + t1), '.')
    l4, = plt.plot(t2, np.exp(-t2) * np.sin(2 * np.pi * t2), 'rs-.')

    plt.xlabel('time')
    plt.ylabel('volts')
    plt.title('Damped oscillation')

    plt.show()

    #===== convert to plotly =====#
    py.iplot_mpl(fig1, strip_style = True)


############
Seaborn demo
############
from https://plot.ly/python/ipython-notebook-tutorial/

.. code-block:: python

    import matplotlib.pyplot as plt
    import plotly.plotly as py
    from numpy.random import randn
    from scipy import stats
    import matplotlib as mpl
    import seaborn as sns

    fig16 = plt.figure()

    sns.set_palette("hls")
    mpl.rc("figure", figsize=(8, 4))
    data = randn(200)
    sns.distplot(data);

    py.iplot_mpl(fig16, strip_style = True)

#############
webgl heatmap
#############
https://plot.ly/python/heatmap-webgl/

.. code-block:: python

    trace = dict(type='heatmapgl', z=z_data)
    py.iplot([trace], validate=False)

#########
log plots
#########
.. code-block:: python
    
    layout = go.Layout(
        xaxis=dict(
            type='log',
            autorange=True
        ),
        yaxis=dict(
            type='log',
            autorange=True
        )
    )
################
Layout to change
################
****************
Background color
****************
.. code-block:: python

    paper_bgcolor='rgb(248, 248, 255)',
    plot_bgcolor='rgb(248, 248, 255)',





