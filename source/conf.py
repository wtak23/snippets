# -*- coding: utf-8 -*-
#
# Snippets documentation build configuration file, created by
# sphinx-quickstart on Fri Aug  5 13:45:35 2016.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('./sphinxext/numpydoc')) # <- somehow needed when executing ``mymake.sh`` from sublime
# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
autosummary_generate=True
import IPython.sphinxext
import numpydoc
numpydoc_class_members_toctree = False
numpydoc_show_class_members = False
extensions = [
    'sphinx.ext.autosummary',
    'sphinx.ext.viewcode',
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.todo',
    'IPython.sphinxext.ipython_console_highlighting',
    'IPython.sphinxext.ipython_directive',
    'numpydoc', # used to parse numpy-style docstrings for autodoc    
]
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The encoding of source files.
#
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Snippets'
copyright = u'2016, Takanori Watanabe'
author = u'Takanori Watanabe'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u''
# The full version, including alpha/beta/rc tags.
release = u''

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#
# today = ''
#
# Else, today_fmt is used as the format for a strftime call.
#
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = [
'cs-rst-ignore.rst', # decided to just include links to good references
'cs-sphinx.rst',
'bct.rst', #<- exclude when prototyping
]




# The reST default role (used for this markup: `text`) to use for all
# documents.
#
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


_theme = 'rtd'
# _theme = 'bootstrap'
# -- Options for HTML output ----------------------------------------------
#=============================================================================#
# for rtd_theme
#=============================================================================#
if _theme == 'rtd':
    html_theme = 'sphinx_rtd_theme'
    html_theme_options = {
        'collapse_navigation': False, #<- set to false when publishing
        # 'sticky_navigation': True,  # Set to False to disable the sticky nav while scrolling.
        # 'navigation_depth': 4,
    }
#=============================================================================#
# Trying out the bootstrap theme
#=============================================================================#
elif _theme == 'bootstrap':
    import sphinx_bootstrap_theme
    html_theme = 'bootstrap'
    html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

    # Custom sidebar templates, maps document names to template names.
    #http://stackoverflow.com/questions/20939598/enabling-sidebar-on-python-sphinx-documentation-based-on-a-sphinx-bootstrap-them
    #http://www.sphinx-doc.org/en/stable/config.html#confval-html_sidebars
    # html_sidebars = {'**': ['localtoc.html', 'sourcelink.html', 'searchbox.html']}
    # html_sidebars = {'**': [
    #     # 'globaltoc.html',
    #     'localtoc.html',
    #     # 'relations.html',
    #     # 'sourcelink.html', # source link
    #     'searchbox.html'
    # ]}

    # Theme options are theme-specific and customize the look and feel of a theme
    # further.  For a list of options available for each theme, see the
    # documentation.
    #
    html_theme_options = {
        # Navigation bar title. (Default: ``project`` value)
        #'navbar_title': "Demo",

        # Tab name for entire site. (Default: "Site")
        'navbar_site_name': "Table of Contents",

        # A list of tuples containing pages or urls to link to.
        # Valid tuples should be in the following forms:
        #    (name, page)                 # a link to a page
        #    (name, "/aa/bb", 1)          # a link to an arbitrary relative url
        #    (name, "http://example.com", True) # arbitrary absolute url
        # Note the "1" or "True" value above as the third argument to indicate
        # an arbitrary url.
        'navbar_links': [
            ("Github", "https://github.com/wtak23", True),
            # ("Link", "http://example.com", True),
        ],

        # Render the next and previous page links in navbar. (Default: true)
        'navbar_sidebarrel': False,

        #-------------------------------------------------------------------------#
        # Render the current pages TOC in the navbar. (Default: true)
        'navbar_pagenav': True,

        # Tab name for the current pages TOC. (Default: "Page")
        'navbar_pagenav_name': "Contents (current page)",
        #-------------------------------------------------------------------------#

        # Global TOC depth for "site" navbar tab. (Default: 1)
        # Switching to -1 shows all levels.
        'globaltoc_depth': -1,

        # Include hidden TOCs in Site navbar?
        #
        # Note: If this is "false", you cannot have mixed ``:hidden:`` and
        # non-hidden ``toctree`` directives in the same page, or else the build
        # will break.
        #
        # Values: "true" (default) or "false"
        'globaltoc_includehidden': "true",

        # HTML navbar class (Default: "navbar") to attach to <div> element.
        # For black navbar, do "navbar navbar-inverse"
        # 'navbar_class': "navbar navbar-inverse",

        # Fix navigation bar to top of page?
        # Values: "true" (default) or "false"
        'navbar_fixed_top': "true",

        # Location of link to source.
        # Options are "nav" (default), "footer" or anything else to exclude.
        'source_link_position': "footer",

        #-------------------------------------------------------------------------#
        # bootstram theme (in conjunction with navbar class....combo matters for me here)
        #-------------------------------------------------------------------------#
        # Bootswatch (http://bootswatch.com/) theme.
        #
        # Options are nothing (default) or the name of a valid theme
        # such as "amelia" or "cosmo".
        # 'bootswatch_theme': "amelia",'navbar_class': "navbar", # <- ugh...not my taste!
        # 'bootswatch_theme': "cyborg",'navbar_class': "navbar navbar-inverse", # <- ugh...not my taste!

        # 'bootswatch_theme': "flatly",'navbar_class': "navbar navbar-inverse", # <- nice!
        # 'bootswatch_theme': "flatly", # <- nice!

        # 'bootswatch_theme': "journal",'navbar_class': "navbar navbar-inverse", # <- bit clunky... (huge navbar font, tiny body font...)

        # 'bootswatch_theme': "readable",'navbar_class': "navbar navbar-inverse", # <- pretty good...

        # 'bootswatch_theme': "simplex",'navbar_class': "navbar navbar-inverse", # <- red navbar ugly...
        'bootswatch_theme': "simplex",'navbar_class': "navbar", # <- Great! I might go with this...

        # 'bootswatch_theme': "slate",'navbar_class': "navbar navbar-inverse", # <- dark background...not a fan

        # 'bootswatch_theme': "spacelab",'navbar_class': "navbar navbar-inverse", # <- admonition background color and hyperlink color overlaps...everything else looks nice....(might have to tinker with custom css for this to fix the hyperlink color issue)
        
        # 'bootswatch_theme': "spruce",'navbar_class': "navbar navbar-inverse", # <- nope, not a fan
        # 'bootswatch_theme': "superhero",'navbar_class': "navbar navbar-inverse",# <- nope, not a fan

        # 'bootswatch_theme': "united",'navbar_class': "navbar navbar-inverse", # pretty cool
        # 'bootswatch_theme': "united",'navbar_class': "navbar", # pretty cool


        # 'bootswatch_theme': "cerulean",'navbar_class': "navbar navbar-inverse", # <- pretty neat
        
        # 'bootswatch_theme': "cosmo",'navbar_class': "navbar", # <- admonition too much glare...hurts my eye


        # Choose Bootstrap version.
        # Values: "3" (default) or "2" (in quotes)
        'bootstrap_version': "2", # 3 doesn't allow recursing over section depth at navbar TOC...use 2
    }
#=============================================================================#



# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.
# "<project> v<release> documentation" by default.
#
# html_title = u'Snippets v1'
html_title = ''

# A shorter title for the navigation bar.  Default is the same as html_title.
#
html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#
# html_logo = '_static/img/blockm.gif'

# The name of an image file (relative to this directory) to use as a favicon of
# the docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#
# html_favicon = './img/blockm.gif'
html_favicon = '_static/img/favicon-penn.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#
# html_extra_path = []

# If not None, a 'Last updated on:' timestamp is inserted at every page
# bottom, using the given strftime format.
# The empty string is equivalent to '%b %d, %Y'.
#
html_last_updated_fmt = ''

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#
# html_additional_pages = {}

# If false, no module index is generated.
#
# html_domain_indices = True

# If false, no index is generated.
#
# html_use_index = True

# If true, the index is split into individual pages for each letter.
#
# html_split_index = False

# If true, links to the reST sources are added to the pages.
#
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#
html_show_copyright = False

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr', 'zh'
#
# html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# 'ja' uses this config value.
# 'zh' user can custom change `jieba` dictionary path.
#
# html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
#
# html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'Snippetsdoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
     # The paper size ('letterpaper' or 'a4paper').
     #
     # 'papersize': 'letterpaper',

     # The font size ('10pt', '11pt' or '12pt').
     #
     # 'pointsize': '10pt',

     # Additional stuff for the LaTeX preamble.
     #
     # 'preamble': '',

     # Latex figure (float) alignment
     #
     # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'Snippets.tex', u'Snippets Documentation',
     u'tw', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#
# latex_use_parts = False

# If true, show page references after internal links.
#
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
#
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
#
# latex_appendices = []

# It false, will not define \strong, \code, 	itleref, \crossref ... but only
# \sphinxstrong, ..., \sphinxtitleref, ... To help avoid clash with user added
# packages.
#
# latex_keep_old_macro_names = True

# If false, no module index is generated.
#
# latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'snippets', u'Snippets Documentation',
     [author], 1)
]

# If true, show URL addresses after external links.
#
# man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Snippets', u'Snippets Documentation',
     author, 'Snippets', 'One line description of project.',
     'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#
# texinfo_appendices = []

# If false, no module index is generated.
#
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#
# texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#
# texinfo_no_detailmenu = False

#=============================================================================#
# My (tak) customization
#=============================================================================#
# http://www.sphinx-doc.org/en/stable/config.html#options-for-html-output
html_secnumber_suffix = ' '
html_add_permalinks = None # http://www.sphinx-doc.org/en/stable/config.html#confval-html_add_permalinks
def setup(app):
    # to hide/show the prompt in code examples:
    app.add_javascript('copybutton.js')

html_style='css/my_theme.css' # <- to get my css recognized http://stackoverflow.com/questions/23211695/modifying-sphinx-theme-read-the-docs    
# html_style='css/rtd_theme_unminified.css' # <- to identify style-names I'd like to tweak