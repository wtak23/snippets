Plotly snippets (``cs-plotly``)
"""""""""""""""""""""""""""""""

.. contents:: `Contents`
   :depth: 2
   :local:

#######
Imports
#######

.. code-block:: python

    import plotly.plotly as py
    import plotly.graph_objs as go
    import plotly.tools as tls
    from plotly.tools import FigureFactory as FF

    import cufflinks as cf

************
offline mode
************
.. code-block:: python

    import plotly.offline as py
    py.init_notebook_mode(connected=True)
    import plotly.graph_objs as go
    import plotly.tools as tls
    from plotly.tools import FigureFactory as FF

    import cufflinks as cf
    cf.set_config_file(theme='ggplot',sharing='secret',offline=True,offline_show_link=False)

##################
My privacy setting
##################
``~/.plotly/.config``

.. code-block:: json

    {
        "sharing": "secret", 
        "world_readable": false, 
        "plotly_streaming_domain": "stream.plot.ly", 
        "plotly_ssl_verification": true, 
        "plotly_proxy_authorization": false, 
        "plotly_api_domain": "https://api.plot.ly", 
        "auto_open": true, 
        "plotly_domain": "https://plot.ly"
    }

*****************
cufflinks setting
*****************
``~/.cufflinks/.config``

.. code-block:: json

    {
        "sharing": "secret", 
        "dimensions": null, 
        "colorscale": "dflt", 
        "offline_link_text": "test", 
        "theme": "ggplot", 
        "offline_show_link": false, 
        "offline_url": true, 
        "offline": true, 
        "datagen_mode": "stocks"
    }

*********
demo plot
*********
Secret plot

.. raw:: html

    <iframe width="600" height="600" frameborder="0" scrolling="no" src="https://plot.ly/~takanori/820.embed?share_key=rKsms5CTwwagSZtGPbMMGQ"></iframe>

##########################
Get figure object from url
##########################
https://plot.ly/python/get-requests/

.. code-block:: python

    fig = py.get_figure("https://plot.ly/~PlotBot/5")
    plot_url = py.plot(fig, filename="python-replot1")

    # get_figure.get_data
    data = py.get_figure("https://plot.ly/~AlexHP/68").get_data()
    distance = [d['y'][0] for d in data]  # check out the data for yourself!

    fig = go.Figure()
    fig['data'] += [go.Histogram(y=distance, name="flyby distance", histnorm='probability')]
    xaxis = dict(title="Probability for Flyby at this Distance")
    yaxis = dict(title="Distance from Earth (Earth Radii)")
    fig['layout'].update(title="data source: https://plot.ly/~AlexHP/68", xaxis=xaxis, yaxis=yaxis)

    plot_url = py.plot(fig, filename="python-get-data")

################
figure.to_string
################
.. code-block:: python

    figure = df.iplot(kind='scatter', asFigure=True)
    print figure.to_string()

##########
CF offline
##########
.. code-block:: python

    cf.go_offline()
    cf.go_online() # switch back to online mode, where graphs are saved on your online plotly account

##################################################################
Use ``requests`` package to communicate with my plotly web account
##################################################################
https://plot.ly/python/privacy/

****************************************
Use requests package to get static image
****************************************
https://plot.ly/matplotlib/static-image-export/

.. code-block:: python
  
    # Save static image
    py.image.save_as(plotly_fig, 'your_image_filename.png') 

    # you can use requests to download lates image
    import requests
    image_bytes = requests.get('https://plot.ly/~chris/1638.png').content

******************************************
trash, restore, delete from plotly account
******************************************
https://plot.ly/python/delete-plots/

https://plot.ly/settings/api

Configure authorization
=======================

.. code-block:: python

    import requests
    from requests.auth import HTTPBasicAuth

    username = 'takanori'
    key_path = os.path.expanduser('~/private/plotly_apikey')
    with open(keypath,'r') as f:
        api_key = f.read()

    auth = HTTPBasicAuth(username, api_key)
    headers = {'Plotly-Client-Platform': 'python'}


Trash and Restore Example
=========================
.. code-block:: python
    
    >>> plotly.tools.set_credentials_file(username=username, api_key=api_key)
    >>> url = py.plot({"data": [{"x": [1, 2, 3],
    >>>                          "y": [4, 2, 4]}],
    >>>                "layout": {"title": "Let's Trash This Plot<br>(then restore it)"}},
    >>>               filename='trash example')
    >>> print url
    u'https://plot.ly/~private_plotly/18'

    >>> # include fileid  in your request (file-id = username:plotid#)
    >>> fid = username+':18'
    >>> print fid
    'private_plotly:18'

    >>> # === Trash your plotly item via http POST === #
    >>> requests.post('https://api.plot.ly/v2/files/'+fid+'/trash', auth=auth, headers=headers)
    <Response [200]>

    >>> # === restore example === #
    >>> requests.post('https://api.plot.ly/v2/files/'+fid+'/restore', auth=auth, headers=headers)
    <Response [200]>

    >>> # === permanent delete via http DELETE === #
    >>> requests.post('https://api.plot.ly/v2/files/'+fid+'/trash', auth=auth, headers=headers)
    <Response [200]>
    >>> requests.delete('https://api.plot.ly/v2/files/'+fid+'/permanent_delete', auth=auth, headers=headers)
    <Response [204]>

##################
Colorscale setting
##################

**************************************
Converting colorscale from colorlovers
**************************************
https://plot.ly/pandas/2D-Histogram/

.. code-block:: python

    import colorlover as cl
    scl = cl.scales['9']['seq']['Blues']
    colorscale = [ [ float(i)/float(len(scl)-1), scl[i] ] for i in range(len(scl)) ]

***********
from mpl cm
***********
- I'll choose seismic colormap from mpl (see http://matplotlib.org/examples/color/colormaps_reference.html for a full list)
- below, I borrowed the idea from http://thomas-cokelaer.info/blog/2014/09/about-matplotlib-colormap-and-how-to-get-rgb-values-of-the-map/

.. code-block:: python

    # convert to plotly readable form, which requires list containing paired values:
    # (1) value interpolating from decimal value 0 to 1
    # (2) corresponding rgb hex value
    from matplotlib import cm
    cscale = cm.seismic
    colorscale = []
    for i in xrange(256):
        r,g,b = cscale(i)[:3]
        colorscale.append([i/255., '#%02x%02x%02x' %  (int(r*255+0.5), int(g*255+0.5), int(b*255+0.5))])

#############################
Subplots with addtrace method
#############################
akin to ``subplots`` from mpl

https://plot.ly/pandas/subplots/

.. code-block:: python

    import plotly.tools as tls
    import plotly.plotly as py
    
    fig = tls.make_subplots(rows=2, cols=1, shared_xaxes=True)

    for col in ['a', 'b']:
        fig.append_trace({'x': df.index, 'y': df[col], 'type': 'scatter', 'name': col}, 1, 1)
    
    for col in ['c', 'd']:
        fig.append_trace({'x': df.index, 'y': df[col], 'type': 'bar', 'name': col}, 2, 1)

    py.iplot(fig)

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





