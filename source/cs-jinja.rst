jinja notes and snippets (``cs-jinja``)
"""""""""""""""""""""""""""""""""""""""


.. contents:: `Contents`
   :depth: 1
   :local:

Main resource: https://tedboy.github.io/jinja2/off_doc.templates.html

######################
Quick review of basics
######################
************************
Default Jinja delimiters
************************
https://tedboy.github.io/jinja2/templ1.html#synopsis

.. note:: These can be modified to something like ``<% foo %>``, but i don't see myself needing to do that

* ``{% ... %}`` for `Statements <https://tedboy.github.io/jinja2/templ11.html#list-of-control-structures>`__
* ``{{ ... }}`` for `Expressions <https://tedboy.github.io/jinja2/templ13.html#expressions>`__ to print to the template output
* ``{# ... #}`` for `Comments <https://tedboy.github.io/jinja2/templ5.html>`__
* ``#  ... ##`` for `Line Statements <https://tedboy.github.io/jinja2/templ8.html#line-statements>`__

******************
Template Variables
******************
https://tedboy.github.io/jinja2/templ2.html#variables

**Template variables** are defined by the :ref:`context dictionary <template_context_def>` passed to the template 

You can use a dot (``.``) to access attributes of a variable in addition
to the standard Python ``__getitem__`` "subscript" syntax (``[]``).

.. sourcecode:: html+jinja

    {{ foo.bar }}
    {{ foo['bar'] }}

*******
Filters
*******
https://tedboy.github.io/jinja2/templ3.html#filters

Variables can be modified by **filters**.  Filters are separated from the
variable by a pipe symbol (``|``) and may have optional arguments in
parentheses.  Multiple filters can be chained.  The output of one filter is
applied to the next.

For example, ``{{ name|striptags|title }}`` will remove all HTML Tags from
variable `name` and title-case the output (``title(striptags(name))``).

Filters that accept arguments have parentheses around the arguments, just like
a function call.  For example: ``{{ listx|join(', ') }}`` will join a list with
commas (``str.join(', ', listx)``).

See :ref:`list of built-in filters <jina_builtin_filters>`

*****
Tests
*****
https://tedboy.github.io/jinja2/templ4.html#tests

- Tests can accept arguments, too.

  - If the test only takes one argument, you can leave out the parentheses. 
  - For example, the following two expressions do the same thing:

.. sourcecode:: html+jinja

    {% if loop.index is divisibleby 3 %}
    {% if loop.index is divisibleby(3) %}


See :ref:`list of built-in tests <jina_builtin_tests>`

******************
Whitespace control
******************
https://tedboy.github.io/jinja2/templ6.html#whitespace-control

In the default configuration:

- a single trailing newline is stripped if present
- other whitespace (spaces, tabs, newlines etc.) is returned unchanged

.. sourcecode:: html+jinja

    <div>
        {% if True %}
            yay
        {% endif %}
    </div>

    {# above renders like this #}
    <div>

            yay

    </div>

You can manually disable the lstrip_blocks behavior by putting a plus sign (``+``) at the start of a block:

.. sourcecode:: html+jinja

    <div>
            {%+ if something %}yay{% endif %}
    </div>

    {# above renders like this #}
    <div>
            yay
    </div>

If you add a minus sign (``-``) to the start or end of a block (e.g. a For tag), a comment, or a variable expression, the whitespaces before or after that block will be removed:

.. sourcecode:: html+jinja

    {# If seq was a list of numbers from 1 to 9, the output would be 123456789 #}
    {% for item in seq -%}
        {{ item }}
    {%- endfor %}

********
Escaping
********
https://tedboy.github.io/jinja2/templ7.html#escaping

(when you want to include ``{{`` as raw string)

The easiest way to output a literal variable delimiter ({{) is by using a variable expression:

.. sourcecode:: html+jinja

    {{ '{{' }}

For bigger sections, it makes sense to mark a block raw. For example, to include example Jinja syntax in a template, you can use this snippet:

.. sourcecode:: html+jinja

    {% raw %}
        <ul>
        {% for item in seq %}
            <li>{{ item }}</li>
        {% endfor %}
        </ul>
    {% endraw %}

*************
HTML escaping
*************
https://tedboy.github.io/jinja2/templ10.html#html-escaping

- When generating HTML from templates, there's always a risk that a variable will include characters that affect the resulting HTML.
- Jinja gives you 2 options: 
    1. manually escaping each variable; or
    2. automatically escaping everything by default.       
- The **default** configuration is no automatic escaping

Manual escaping with ``|e`` filter
==================================
- What to escape? 
- If you have a variable that may include any of the following chars (``>, <, &, or "``) you SHOULD escape it unless the variable contains well-formed and trusted HTML. 
- Escaping works by piping the variable through the ``|e`` filter (:ref:`escape filter <_jinja_filter_escape>`):

.. sourcecode:: html+jinja

    {{ user.username|e }}

Automatic escaping (I don't use this)
=====================================
The main problem with this approach is that Python itself doesn't have the concept of tainted values; so whether a value is safe or unsafe can get lost

***********************
Import Context Behavior
***********************
https://tedboy.github.io/jinja2/templ12.html#import-context-behavior

####################
Template inheritance
####################
https://tedboy.github.io/jinja2/templ9.html#template-inheritance

- By default, included templates are passed the current context and imported templates are not. 
- The reason for this is that imports, unlike includes, are **cached**; as imports are often used just as a module that holds macros.

.. raw:: </br>

- This behavior can be changed explicitly by adding ``with context`` or ``without context ``to the ``import/include`` **directive**, the current context can be passed to the template and caching is disabled automatically.

Here are two examples:

.. sourcecode:: html+jinja

    {% from 'forms.html' import input with context %}
    {% include 'header.html' without context %}

.. admonition:: Note

    From Jinja 2.1, ``render_box.html`` below can access the ``box`` variable
    (the context that was passed to the **included template**
    includes variables defined in the template)

    .. sourcecode:: html+jinja
    
        {% for box in boxes %}
            {% include "render_box.html" %}
        {% endfor %}

**********************
Base (parent) template
**********************
Use ``{% block BLOCKNAME %} ... {% endblock %}`` syntax

Suppose we have a file called ``base.html`` like this

.. sourcecode:: html+jinja

    <!DOCTYPE html>
    <html lang="en">
    <head>
        {% block head %}
        <link rel="stylesheet" href="style.css" />
        <title>{% block title %}{% endblock %} - My Webpage</title>
        {% endblock %}
    </head>
    <body>
        <div id="content">{% block content %}{% endblock %}</div>
        <div id="footer">
            {% block footer %}
            &copy; Copyright 2008 by <a href="http://domain.invalid/">you</a>.
            {% endblock footer %}
            {# adding block-name at "endblock" is optional, but I like to include it for readability #}
        </div>
    </body>
    </html>

**************
Child template
**************
Use ``{% extends "base.html" %}`` syntax

.. sourcecode:: html+jinja

    {% extends "base.html" %}
    {% block title %}Index{% endblock %}
    {% block head %}
        {#- super will render the content of the parent block as well -#}
        {{ super() }}
        <style type="text/css">
            .important { color: #336699; }
        </style>
    {% endblock %}
    {% block content %}
        <h1>Index</h1>
        <p class="important">
          Welcome to my awesome homepage.
        </p>
    {% endblock %}

***********************
Nested blocks and scope
***********************
.. important:: per default blocks may not access variables from outer scopes:

    .. sourcecode:: html+jinja
    
        {# This outputs empty <li> items since "item" is unavailable inside the block #}
        {% for item in seq %}
            <li>{% block loop_item %}{{ item }}{% endblock %}</li>
        {% endfor %}

.. admonition:: solution (scoped modified)

   Add the ``scoped`` modifier to the block

   .. sourcecode:: html+jinja

       {% for item in seq %}
           <li>{% block loop_item scoped %}{{ item }}{% endblock %}</li>
       {% endfor %}

************
Super Blocks
************
It's possible to render the contents of the parent block by calling super. This gives back the results of the parent block:

.. sourcecode:: html+jinja

    {% block sidebar %}
        <h3>Table Of Contents</h3>
        ...
        {{ super() }}
    {% endblock %}

********************
Named block-end tags
********************
.. sourcecode:: html+jinja

    {% block sidebar %}
        {% block inner_sidebar %}
            ...
        {% endblock inner_sidebar %}
    {% endblock sidebar %}

#################################################
List of control structures (``{% ... %}``)
#################################################
https://tedboy.github.io/jinja2/templ11.html#list-of-control-structures

******************************************
filter ``{% filter .. %} {% endfilter %}``
******************************************
Apply a filter to entire block

.. sourcecode:: html+jinja

    {% filter upper %}
        This text becomes uppercase
    {% endfilter %}

*******************************************
Variable assignments using ``{% set .. %}``
*******************************************
- you can also assign values to variables. 
- Assignments at top level (outside of blocks, macros or loops) are exported from the template like top level macros 
- Assignments **can be imported** by other templates.
- Assignments use the set tag and **can have multiple targets**

.. sourcecode:: html+jinja

    {% set navigation = [('index.html', 'Index'), ('about.html', 'About')] %}
    {% set key, value = call_something() %}

**********************************
Block assignments (from jinja 2.8)
**********************************
- use block assignments to capture the contents of a block into a variable name. 
- This can be useful in some situations as an **alternative for macros**. 
- In that case, instead of using an equals sign and a value, you just write the variable name and then everything until ``{% endset %}`` is captured.

.. sourcecode:: html+jinja

    {# The "navigation" variable then contains the navigation HTML source. #}
    {% set navigation %}
        <li><a href="/">Index</a>
        <li><a href="/downloads">Downloads</a>
    {% endset %}

************************************
For loops ``{% for %} {% endfor %}``
************************************
.. sourcecode:: html+jinja

    <ul>
    {% for user in users %}
      <li>{{ user.username|e }}</li>
    {% endfor %}
    </ul>

    {# it is possible to iterate over containers like dict #}
    <dl>
    {% for key, value in my_dict.iteritems() %}
        <dt>{{ key|e }}</dt>
        <dd>{{ value|e }}</dd>
    {% endfor %}
    </dl>

.. admonition:: Special variable accessible inside a loop

    Inside of a for-loop block, you can access some special variables:

    +-----------------------+---------------------------------------------------+
    | Variable              | Description                                       |
    +=======================+===================================================+
    | `loop.index`          | The current iteration of the loop. (1 indexed)    |
    +-----------------------+---------------------------------------------------+
    | `loop.index0`         | The current iteration of the loop. (0 indexed)    |
    +-----------------------+---------------------------------------------------+
    | `loop.revindex`       | The number of iterations from the end of the loop |
    |                       | (1 indexed)                                       |
    +-----------------------+---------------------------------------------------+
    | `loop.revindex0`      | The number of iterations from the end of the loop |
    |                       | (0 indexed)                                       |
    +-----------------------+---------------------------------------------------+
    | `loop.first`          | True if first iteration.                          |
    +-----------------------+---------------------------------------------------+
    | `loop.last`           | True if last iteration.                           |
    +-----------------------+---------------------------------------------------+
    | `loop.length`         | The number of items in the sequence.              |
    +-----------------------+---------------------------------------------------+
    | `loop.cycle`          | A helper function to cycle between a list of      |
    |                       | sequences.  See the explanation below.            |
    +-----------------------+---------------------------------------------------+
    | `loop.depth`          | Indicates how deep in a recursive loop            |
    |                       | the rendering currently is.  Starts at level 1    |
    +-----------------------+---------------------------------------------------+
    | `loop.depth0`         | Indicates how deep in a recursive loop            |
    |                       | the rendering currently is.  Starts at level 0    |
    +-----------------------+---------------------------------------------------+

.. sourcecode:: html+jinja

    {# use "loop.cycle" helper to cycle among a list of strings/variables each time through the loop #}
    {% for row in rows %}
        <li class="{{ loop.cycle('odd', 'even') }}">{{ row }}</li>
    {% endfor %}

.. warning:: 

    Python dicts are not ordered; so you might want to pass a ``collections.OrderedDict`` – to the template, or use the ``dictsort`` filter

.. admonition:: No break or continue in Jinja!!!

    - Unlike in Python, it's not possible to break or continue in a loop. 
    - You can, however, filter the sequence during iteration, which allows you to skip items
    - The example below skips all the users which are hidden

      - The **advantage** is that the special loop variable will count correctly; thus not counting the users not iterated over. 

.. sourcecode:: html+jinja

    {# loop variable counts correctly, not counting the users not iterated over #}
    {% for user in users if not user.hidden %}
        <li>{{ user.username|e }}</li>
    {% endfor %}

    {# use "else" in case loop gave empty result (perhaps from filtering) #}
    <ul>
    {% for user in users %}
        <li>{{ user.username|e }}</li>
    {% else %}
        <li><em>no users found</em></li>
    {% endfor %}
    </ul>

.. admonition:: Recursive loop with the ``recursive`` modifier
   
   To use loops recursively, you have to add the ``recursive`` modifier to the loop definition and call the **loop variable** with the new iterable where you want to recurse. 

   - The loop variable always refers to the **closest (innermost) loop**. 
   - If we have more than one level of loops, we can rebind the variable loop by writing ``{% set outer_loop = loop %}`` after the loop that we want to use recursively. 
   - Then, we can call it using ``{{ outer_loop(...) }}``

.. sourcecode:: html+jinja

    <ul class="sitemap">
    {# note the "recursive" modifier #}
    {%- for item in sitemap recursive %}
        <li><a href="{{ item.href|e }}">{{ item.title }}</a>
        {%- if item.children -%}
            <ul class="submenu">{{ loop(item.children) }}</ul>
        {%- endif %}</li>
    {%- endfor %}
    </ul>

*********************************************
if (``{% if .. %} {% elif .. %} {% else %}``)
*********************************************
https://tedboy.github.io/jinja2/templ11.html#if

.. sourcecode:: html+jinja

    {# test if a variable is defined, not empty or not false #}
    {% if users %}
    <ul>
    {% for user in users %}
        <li>{{ user.username|e }}</li>
    {% endfor %}
    </ul>
    {% endif %}

    {# if elif else constructs #}
    {% if kenny.sick %}
        Kenny is sick.
    {% elif kenny.dead %}
        You killed Kenny!  You bastard!!!
    {% else %}
        Kenny looks okay --- so far
    {% endif %}

****************************************************
Macros (``{% macro funcname(..) %} {% endmacro %}``)
****************************************************
https://tedboy.github.io/jinja2/templ11.html#macros

note:: If a macro name starts with an underscore, it’s not exported and can't be imported.

.. sourcecode:: html+jinja

    {# define macro (like function) #}
    {% macro input(name, value='', type='text', size=20) -%}
        <input type="{{ type }}" name="{{ name }}" value="{{
            value|e }}" size="{{ size }}">
    {%- endmacro %}

    {# use above macro like a function in the namespace #}
    <p>{{ input('username') }}</p>
    <p>{{ input('password', type='password') }}</p>

.. admonition:: special variables and attributes accessible in macros
   
   .. csv-table:: 
       :delim: |
       
       ``varargs`` |    If more positional arguments are passed to the macro than accepted by the macro, they end up in the special varargs variable as a list of values.
       ``kwargs``  |    Like varargs but for keyword arguments. All unconsumed keyword arguments are stored in this special variable.
       ``caller``  |   If the macro was called from a call tag, the caller is stored in this variable as a callable macro.
       ``name``     |       The name of the macro. {{ input.name }} will print input.
       ``arguments`` |       A tuple of the names of arguments the macro accepts.
       ``defaults`` |       A tuple of default values.
       ``catch_kwargs`` |       This is true if the macro accepts extra keyword arguments (i.e.: accesses the special kwargs variable).
       ``catch_varargs`` |       This is true if the macro accepts extra positional arguments (i.e.: accesses the special varargs variable).
       ``caller`` |       This is true if the macro accesses the special caller variable and may be called from a call tag.

***************************************************************
Call (pass macro to another macro) ``{% call %} {% endcall %}``
***************************************************************
https://tedboy.github.io/jinja2/templ11.html#call

Generally speaking, a call block works exactly like a macro without a name.

.. sourcecode:: html+jinja

    {% macro render_dialog(title, class='dialog') -%}
        <div class="{{ class }}">
            <h2>{{ title }}</h2>
            <div class="contents">
                {{ caller() }}
            </div>
        </div>
    {%- endmacro %}

    {# now use call #}
    {% call render_dialog('Hello World') %}
        This is a simple dialog rendered by using a macro and
        a call block.
    {% endcall %}

Here's an example of how a call block can be used with arguments:

.. sourcecode:: html+jinja

    {% macro dump_users(users) -%}
        <ul>
        {%- for user in users %}
            <li><p>{{ user.username|e }}</p>{{ caller(user) }}</li>
        {%- endfor %}
        </ul>
    {%- endmacro %}

    {% call(user) dump_users(list_of_user) %}
        <dl>
            <dl>Realname</dl>
            <dd>{{ user.realname|e }}</dd>
            <dl>Description</dl>
            <dd>{{ user.description }}</dd>
        </dl>
    {% endcall %}

*************************************
Include ``{% include 'file.html' %}``
*************************************
https://tedboy.github.io/jinja2/templ11.html#include

The include statement is useful to include a template and return the rendered contents of that file into the current namespace

.. important:: 
    
    Included templates have access to the variables of the active context by default**. 

    For more details about context behavior of imports and includes, see **Import Context Behavior**.

.. sourcecode:: html+jinja

    {% include 'header.html' %}
        Body
    {% include 'footer.html' %}

    {# ``ignore missing`` modified used to ignore the statement of template to be included does not exist (else exception raised) #}
    {% include "sidebar.html" ignore missing %}
    {% include "sidebar.html" ignore missing with context %}
    {% include "sidebar.html" ignore missing without context %}

    {# you can also provide a list of template to check for existence #}
    {# (the first template that exists will be included #}
    {% include ['page_detailed.html', 'page.html'] %}
    {% include ['special_sidebar.html', 'sidebar.html'] ignore missing %}

******
Import
******
https://tedboy.github.io/jinja2/templ11.html#import

- Jinja2 supports putting often used code into macros. 
- These macros can go into different templates and get imported from there. 
- This works similarly to the import statements in Python. 
- It's important to know that:

  - **imports are cached** 
  - imported templates don't have access to the **current template variables**, just the globals by default. 
- For more details about context behavior of imports and includes, see **Import Context Behavior**.
- There are two ways to import templates. 

  1. You can **import a complete template into a variable** or 
  2. **request specific macros / exported variables** from it.
- Macros and variables starting with one or more **underscores** are private and cannot be imported.
- Changed in version 2.4: If a template object was passed to the template context, you can import from that object.

.. rubric:: Example

Imagine we have a helper module that renders forms (called ``forms.html``):

.. sourcecode:: html+jinja

    {% macro input(name, value='', type='text') -%}
        <input type="{{ type }}" value="{{ value|e }}" name="{{ name }}">
    {%- endmacro %}

    {%- macro textarea(name, value='', rows=10, cols=40) -%}
        <textarea name="{{ name }}" rows="{{ rows }}" cols="{{ cols
            }}">{{ value|e }}</textarea>
    {%- endmacro %}

The easiest and most flexible way to access a template's variables and macros is to **import the whole template module into a variable**. That way, you can access the attributes:

.. sourcecode:: html+jinja

    {% import 'forms.html' as forms %}
    <dl>
        <dt>Username</dt>
        <dd>{{ forms.input('username') }}</dd>
        <dt>Password</dt>
        <dd>{{ forms.input('password', type='password') }}</dd>
    </dl>
    <p>{{ forms.textarea('comment') }}</p>

Alternatively, you can **import specific names from a template** into the **current namespace**:

.. sourcecode:: html+jinja

    {% from 'forms.html' import input as input_field, textarea %}
    <dl>
        <dt>Username</dt>
        <dd>{{ input_field('username') }}</dd>
        <dt>Password</dt>
        <dd>{{ input_field('password', type='password') }}</dd>
    </dl>
    <p>{{ textarea('comment') }}</p>

###################
List of Expressions
###################
https://tedboy.github.io/jinja2/templ13.html#expressions

*********************************************
Literals (string, numbers, list, dict, bools)
*********************************************
.. csv-table:: 
    :delim: |

    **String** | ``"Hello World"`` | Everything between two double or single quotes is a string.
    **Numbers** | ``42 / 42.23`` | Integers and floating point numbers are created by just writing the number down. If a dot is present, the number is a float, otherwise an integer.
    **Bool** | ``true / false`` | (``True`` and ``None`` also works, but lowercase as convention)
    **List** | ``['list', 'of', 'objects']`` | Everything between two brackets is a list
    **Tuple** | ``('tuple', 'of', 'values')`` | Tuples are like lists that cannot be modified ("immutable"). If a tuple only has one item, it must be followed by a comma ``(('1-tuple',))``. Tuples are usually used to represent items of two or more elements.
    **Dict** | ``{'dict': 'of', 'key': 'and', 'value': 'pairs'}`` | **Dicts are rarely used in templates;** they are useful in some rare cases such as the xmlattr() filter.

.. sourcecode:: html+jinja

    {# use of list of tuples to iterate over #}
    <ul>
    {% for href, caption in [('index.html', 'Index'), ('about.html', 'About'),
                             ('downloads.html', 'Downloads')] %}
        <li><a href="{{ href }}">{{ caption }}</a></li>
    {% endfor %}
    </ul>

*******************************
Math (rarely used in templates)
*******************************
.. csv-table:: 
    :delim: |

    ``+`` |    Adds two objects together. Usually the objects are numbers, but if both are strings or lists, you can concatenate them this way. This, however, is not the preferred way to concatenate strings! For string concatenation, have a look-see at the ``~`` operator. ``{{ 1 + 1 }}`` is 2.
    ``-`` |    Subtract the second number from the first one. ``{{ 3 - 2 }}`` is 1.
    ``/`` |    Divide two numbers. **The return value will be a floating point number**. ``{{ 1 / 2 }}`` is ``{{ 0.5 }}``. (Just like ``from __future__ import division``.)
    ``//`` |    Divide two numbers and return the truncated integer result. ``{{ 20 // 7 }}`` is 2.
    ``%`` |    Calculate the remainder of an integer division. ``{{ 11 % 7 }}`` is 4.
    ``*`` |    Multiply the left operand with the right one. ``{{ 2 * 2 }}`` would return 4. 
    ``*`` |    Repeat a string multiple times. ``{{ '=' * 80 }}`` would print a bar of 80 equal signs.
    ``**`` |    Raise the left operand to the power of the right operand. ``{{ 2**3 }}`` would return 8.
    
***************
Comparison test
***************
.. csv-table:: 
    :delim: |

    ``==`` |     Compares two objects for equality.
    ``!=`` |     Compares two objects for inequality.
    ``>``  |    true if the left hand side is greater than the right hand side.
    ``>=`` |    true if the left hand side is greater or equal to the right hand side.
    ``<``  |    true if the left hand side is lower than the right hand side.
    ``<=`` |    true if the left hand side is lower or equal to the right hand side.

*****************************************
Logical expression (to be used in ``if``)
*****************************************
.. csv-table:: 
    :delim: |

    ``and`` |    Return true if the left and the right operand are true.
    ``or``  |    Return true if the left or the right operand are true.
    ``not`` |    negate a statement (see below).
    ``(expr)`` |    group an expression.   

.. admonitino:: ``is in`` **infix** notation


    - The ``is`` and ``in`` operators support negation using an **infix notation**, too: 
    - ``foo is not bar`` and ``foo not in bar`` instead of ``not foo is bar`` and ``not foo in bar``. 
    - All other expressions require a prefix notation: ``not (foo and bar)``.

*********************************************************
Other operators (ones that don't fit in above categories)
*********************************************************
in
    Perform a sequence / mapping containment test.  Returns true if the left
    operand is contained in the right.  ``{{ 1 in [1, 2, 3] }}`` would, for
    example, return true.

is
    Performs a :ref:`test <tests>`.

\|
    Applies a :ref:`filter <filters>`.

~
    Converts all operands into strings and concatenates them.

    ``{{ "Hello " ~ name ~ "!" }}`` would return (assuming `name` is set
    to ``'John'``) ``Hello John!``.

()
    Call a callable: ``{{ post.render() }}``.  Inside of the parentheses you
    can use positional arguments and keyword arguments like in Python:

    ``{{ post.render(user, full=true) }}``.

. / []
    Get an attribute of an object.  (See :ref:`variables`)

*************************
inline ``if`` expressions
*************************
- **inline if statement** are useful in some situations.  
- For example, you can use this to **extend from one template if a variable is defined**, otherwise from the default layout template:

.. sourcecode:: html+jinja

    {% extends layout_template if layout_template is defined else 'master.html' %}

- The general syntax is: ``<do something> if <something is true> else <do something else>``.
- The ``else`` part is **optional**.  If not provided, the else block implicitly evaluates into an undefined object:

.. sourcecode:: html+jinja

    {{ '[%s]' % page.title if page.title }}

########################
List of global functions
########################
https://tedboy.github.io/jinja2/templ16.html#list-of-global-functions

****************************
range([start=0, ]stop[, step])
****************************
- ``range(i, j)`` returns [i, i+1, i+2, ..., j-1]; 
- ``range(4)`` and ``range(0, 4, 1)`` return [0, 1, 2, 3] (**end point is omitted!**)

**Useful to repeat a template block multiple times (eg, fill a list)**

.. sourcecode:: html+jinja

    {# Imagine you have 7 users in the list but you want to render #}
    {# three empty items to enforce a height with CSS              #}
    <ul>
    {% for user in users %}
        <li>{{ user.username }}</li>
    {% endfor %}
    {% for number in range(10 - users|count) %}
        <li class="empty"><span>...</span></li>
    {% endfor %}
    </ul>

***************************************
lipsum(n=5, html=True, min=20, max=100)
***************************************
- Generates some lorem ipsum for the template.
- By **default** (``n=5``), **five paragraphs of HTML** are generated with each paragraph between 20 and 100 words. 
- If ``html`` is False, regular text is returned. 


*************
dict(**items)
*************
- A convenient alternative to dict literals. 
- ``{'foo': 'bar'}`` is the same as ``dict(foo='bar')``.

********************
class cycler(*items)
********************
- The cycler allows you to cycle among values similar to how ``loop.cycle``
works.  
- Unlike ``loop.cycle``, you can use this cycler outside of
loops or over multiple loops.
- This can be very **useful if you want to show a list of folders and
files** with the folders on top but both in the same list with **alternating
row colors**.

.. sourcecode:: html+jinja

    {% set row_class = cycler('odd', 'even') %}
    <ul class="browser">
    {% for folder in folders %}
      <li class="folder {{ row_class.next() }}">{{ folder|e }}</li>
    {% endfor %}
    {% for filename in files %}
      <li class="file {{ row_class.next() }}">{{ filename|e }}</li>
    {% endfor %}
    </ul>

A cycler has the following attributes and methods:

.. method:: reset()

    Resets the cycle to the first item.

.. method:: next()

    Goes one item ahead and returns the then-current item.

.. attribute:: current

    Returns the current item.

**********************
class joiner(sep=', ')
**********************
- A tiny helper that can be used to "join" multiple sections. 
- A **joiner** is passed a string and will return that string every time it's called, except the first time (in which case it returns an empty string). 
- You can use this to join things:

.. sourcecode:: html+jinja

    {% set pipe = joiner("|") %}
    {% if categories %} {{ pipe() }}
        Categories: {{ categories|join(", ") }}
    {% endif %}
    {% if author %} {{ pipe() }}
        Author: {{ author() }}
    {% endif %}
    {% if can_edit %} {{ pipe() }}
        <a href="?action=edit">Edit</a>
    {% endif %}


.. _jina_builtin_filters:

##########################
Built-in filters (general)
##########################

***************
attr(obj, name)
***************
Get an attribute of an object. 

``foo|attr("bar")`` works like ``foo.bar`` just that always an attribute is returned and items are not looked up.

***************************************
batch(value, linecount, fill_with=None)
***************************************
- A filter that batches items. 
- It works pretty much like slice just the other way round. It returns a list of lists with the given number of items. 
- If you provide a second parameter this is used to fill up missing items. 

.. sourcecode:: html+jinja

    <table>
    {%- for row in items|batch(3, '&nbsp;') %}
      <tr>
      {%- for column in row %}
        <td>{{ column }}</td>
      {%- endfor %}
      </tr>
    {%- endfor %}
    </table>

*******
default
*******
``default(value, default_value=u'', boolean=False)``

Aliases:    ``d``

If the value is ``undefined`` it will return the passed default value, otherwise the value of the variable. For instance, below will output the value of my_variable if the variable was defined, otherwise 'my_variable is not defined'. 

.. sourcecode:: html+jinja

    {{ my_variable|default('my_variable is not defined') }}

If you want to use default with variables that evaluate to false you have to set the second parameter to ``true``:

.. sourcecode:: html+jinja

    {{ ''|default('the string was empty', true) }}


***********************************************
dictsort(value, case_sensitive=False, by='key')
***********************************************
- Sort a dict and yield (key, value) pairs. 
- Because **python dicts are unsorted** you may want to use this function to order them by either key or value:

.. sourcecode:: html+jinja

    {% for item in mydict|dictsort %}
        sort the dict by key, case insensitive

    {% for item in mydict|dictsort(true) %}
        sort the dict by key, case sensitive

    {% for item in mydict|dictsort(false, 'value') %}
        sort the dict by value, case insensitive


**********
first(seq)
**********
Return the first item of a sequence.

*************************
groupby(value, attribute)
*************************
Group a sequence of objects by a common attribute.

If you for example have a **list of dicts** or **objects** that represent persons with ``gender``, ``first_name`` and ``last_name`` **attributes** and you want to **group all users by genders** you can do something like the following snippet:

.. sourcecode:: html+jinja

    <ul>
    {% for group in persons|groupby('gender') %}
        <li>{{ group.grouper }}<ul>
        {% for person in group.list %}
            <li>{{ person.first_name }} {{ person.last_name }}</li>
        {% endfor %}</ul></li>
    {% endfor %}
    </ul>

Additionally it’s possible to use tuple unpacking for the grouper and list:

.. sourcecode:: html+jinja

    <ul>
    {% for grouper, list in persons|groupby('gender') %}
        ...
    {% endfor %}
    </ul>

*********
last(seq)
*********
Return the last item of a sequence.

**************
length(object)
**************
Return the number of items of a sequence or collection.

**Aliases**:    ``count``

***********
list(value)
***********
- Convert the value into a list. 

.. note:: For **string** the returned list will be a **list of characters**.


*****
map()
*****
- Applies a filter on a sequence of objects or looks up an attribute. 
- **This is useful when dealing with lists of objects but you are really only interested in a certain value of it**.

.. admonition:: Basic Usage -- mapping an attribute
   
    Imagine you have a list of users but you are only interested in a list of usernames:

    .. sourcecode:: html+jinja
    
        Users on this page: {{ users|map(attribute='username')|join(', ') }}

    - Alternatively you can let it invoke a filter by passing the name of the filter and the arguments afterwards. 
    - A good example would be applying a text conversion filter on a sequence:

    .. sourcecode:: html+jinja
    
        Users on this page: {{ titles|map('lower')|join(', ') }}

****************************
pprint(value, verbose=False)
****************************
- Pretty print a variable. Useful for debugging.

***********
random(seq)
***********
Return a random item from the sequence.

********
reject()
********
Filters a sequence of objects by applying a test to the object and rejecting the ones with the test succeeding.

Example usage:

.. sourcecode:: html+jinja

    {{ numbers|reject("odd") }}

************
rejectattr()
************
Filters a sequence of objects by applying a test to an attribute of an object or the attribute and rejecting the ones with the test succeeding.

.. sourcecode:: html+jinja

    {{ users|rejectattr("is_active") }}
    {{ users|rejectattr("email", "none") }}

**************
reverse(value)
**************
Reverse the object or return an iterator that iterates over it the other way round.

***********
safe(value)
***********
Mark the value as safe which means that in an environment with automatic escaping enabled this variable will not be escaped.

********
select()
********
Filters a sequence of objects by applying a test to the object and only selecting the ones with the test succeeding. (see built-in tests)

Example usage:

.. sourcecode:: html+jinja

    {# "odd" and "even" are built-in tests in jina #}
    {{ numbers|select("odd") }}
    {{ numbers|select("even") }}


************
selectattr()
************
Filters a sequence of objects by applying a test to an attribute of an object and only selecting the ones with the test succeeding.

Example usage:

.. sourcecode:: html+jinja

    {{ users|selectattr("is_active") }}
    {{ users|selectattr("email", "none") }}

************************************
slice(value, slices, fill_with=None)
************************************
- Slice an iterator and return a list of lists containing those items. 
- **Useful if you want to create a div containing three ul tags that represent columns**:

.. sourcecode:: html+jinja

    <div class="columwrapper">
      {%- for column in items|slice(3) %}
        <ul class="column-{{ loop.index }}">
        {%- for item in column %}
          <li>{{ item }}</li>
        {%- endfor %}
        </ul>
      {%- endfor %}
    </div>

If you pass it a second argument it's used to fill missing values on the last iteration.

****************************************************************
sort(value, reverse=False, case_sensitive=False, attribute=None)
****************************************************************
- Sort an iterable. 
- **default = sorts ascending**, if you pass it true as first argument it will reverse the sorting.
- **If the iterable is made of strings** the **third parameter** can be used to control the case sensitiveness of the comparison which is disabled by default.

.. sourcecode:: html+jinja

    {% for item in iterable|sort %}
        ...
    {% endfor %}

It is also possible to sort by an attribute (for example to sort by the date of an object) by specifying the attribute parameter:

.. sourcecode:: html+jinja

    {% for item in iterable|sort(attribute='date') %}
        ...
    {% endfor %}


**************************
xmlattr(d, autospace=True)
**************************
Create an SGML/XML attribute string based on the items in a dict. All values that are neither none nor undefined are automatically escaped:

.. sourcecode:: html+jinja

    <ul{{ {'class': 'my_list', 'missing': none,
            'id': 'list-%d'|format(variable)}|xmlattr }}>
    ...
    </ul>

Results in something like this:

.. sourcecode:: html+jinja

    <ul class="my_list" id="list-42">
    ...
    </ul>

As you can see it automatically prepends a space in front of the item if the filter returned something unless the second parameter is false.

#########################
Built-in filters (string)
#########################

*************
capitalize(s)
*************
Capitalize a value. The first character will be uppercase, all others lowercase.

***********************
center(value, width=80)
***********************
Centers the value in a field of a given width.

.. _jinja_filter_escape:

*********
escape(s)
*********
- Convert the characters ``&, <, >, ', "`` in string s to HTML-safe sequences. - Use this if you need to display text that might contain such characters in HTML. 
- Marks return value as markup string.

**Aliases**:    ``e``

******************
forceescape(value)
******************
Enforce HTML escaping. This will probably double escape variables.

******************************
format(value, *args, **kwargs)
******************************
Apply python string formatting on an object:

.. sourcecode:: html+jinja

    {{ "%s - %s"|format("Hello?", "Foo!") }}
        -> Hello? - Foo!

*************************************
indent(s, width=4, indentfirst=False)
*************************************
- Return a copy of the passed string, each line indented by 4 spaces. 
- The first line is not indented. If you want to change the number of spaces or indent the first line too you can pass additional parameters to the filter:

.. sourcecode:: html+jinja

    {{ mytext|indent(2, true) }}
        indent by two spaces and indent the first line too.

**********************************
join(value, d=u'', attribute=None)
**********************************
- Return a string which is the concatenation of the strings in the sequence. 
- The separator between elements is an empty string per default, you can define it with the optional parameter:

.. sourcecode:: html+jinja

    {{ [1, 2, 3]|join('|') }}
        -> 1|2|3

    {{ [1, 2, 3]|join }}
        -> 123

It is also possible to join certain attributes of an object:

.. sourcecode:: html+jinja

    {{ users|join(', ', attribute='username') }}

********
lower(s)
********
Convert a value to lowercase.

********************************
replace(s, old, new, count=None)
********************************
- Return a copy of the value with all occurrences of a substring replaced with a new one. 
- The first argument is the substring that should be replaced, the second is the replacement string. 
- If the optional third argument count is given, only the first count occurrences are replaced:

.. sourcecode:: html+jinja

    {{ "Hello World"|replace("Hello", "Goodbye") }}
        -> Goodbye World

    {{ "aaaaargh"|replace("a", "d'oh, ", 2) }}
        -> d'oh, d'oh, aaargh

**************
string(object)
**************
Make a string unicode if it isn't already. That way a markup string is not converted back to unicode.

****************
striptags(value)
****************
Strip SGML/XML tags and replace adjacent whitespace by one space.

********
title(s)
********
Return a titlecased version of the value. I.e. words will start with uppercase letters, all remaining characters are lowercase.

***********
trim(value)
***********
Strip leading and trailing whitespace.

***************************************************
truncate(s, length=255, killwords=False, end='...')
***************************************************
- Return a truncated copy of the string. 
- The length is specified with the first parameter which defaults to 255. 
- If the second parameter is true the filter will cut the text at length. 
Otherwise it will discard the last word. 
- If the text was in fact truncated it will append an ellipsis sign (``"..."``). 
- If you want a different ellipsis sign than "..." you can specify it using the third parameter.


.. sourcecode:: html+jinja

    {{ "foo bar baz"|truncate(9) }}
        -> "foo ..."
    {{ "foo bar baz"|truncate(9, True) }}
        -> "foo ba..."

********
upper(s)
********
Convert a value to uppercase.

****************
urlencode(value)
****************
Escape strings for use in URLs (uses UTF-8 encoding). It accepts both dictionaries and regular strings as well as pairwise iterables.

***************************************************************
urlize(value, trim_url_limit=None, nofollow=False, target=None)
***************************************************************
Converts URLs in plain text into clickable links.

If you pass the filter an additional integer it will shorten the urls to that number. Also a third argument exists that makes the urls ``"nofollow"``:

.. sourcecode:: html+jinja

    {{ mytext|urlize(40, true) }}
        links are shortened to 40 chars and defined with rel="nofollow"

If target is specified, the target attribute will be added to the ``<a>`` tag:

.. sourcecode:: html+jinja

    {{ mytext|urlize(40, target='_blank') }}

************
wordcount(s)
************
Count the words in that string.

*************************************************************
wordwrap(s, width=79, break_long_words=True, wrapstring=None)
*************************************************************
Return a copy of the string passed to the filter wrapped after 79 characters. You can override this default using the first parameter. If you set the second parameter to false Jinja will not split words apart if they are longer than width. By default, the newlines will be the default newlines for the environment, but this can be changed using the wrapstring keyword argument.


##########################
Built-in filters (numeric)
##########################

***********
abs(number)
***********
Return the absolute value of the argument.

***********************************
filesizeformat(value, binary=False)
***********************************
- Format the value like a 'human-readable' file size (i.e. 13 kB, 4.1 MB, 102 Bytes, etc). 
- Per default decimal prefixes are used (Mega, Giga, etc.), if the second parameter is set to True the binary prefixes are used (Mebi, Gibi).

*************************
float(value, default=0.0)
*************************
- Convert the value into a floating point number. 
- If the conversion doesn't work it will return 0.0. You can override this default using the first parameter.

******************************
int(value, default=0, base=10)
******************************
- Convert the value into an integer. 
- If the conversion doesn’t work it will return 0.
- You can override this default using the first parameter. 
- You can also override the default base (10) in the second parameter, which handles input with prefixes such as 0b, 0o and 0x for bases 2, 8 and 16 respectively.

******************************************
round(value, precision=0, method='common')
******************************************
Round the number to a given precision. The first parameter specifies the precision (default is 0), the second the rounding method:

- ``'common'`` rounds either up or down
- ``'ceil'`` always rounds up
- ``'floor'`` always rounds down

.. sourcecode:: html+jinja

    {{ 42.55|round }}
        -> 43.0
    {{ 42.55|round(1, 'floor') }}
        -> 42.5

Note that even if rounded to 0 precision, a float is returned. If you need a real integer, pipe it through int:

.. sourcecode:: html+jinja

    {{ 42.55|round|int }}
        -> 43

**************************************
sum(iterable, attribute=None, start=0)
**************************************
Returns the sum of a sequence of numbers plus the value of parameter ``'start'``. When the sequence is empty it returns start.

It is also possible to sum up only certain attributes:

.. sourcecode:: html+jinja

    Total: {{ items|sum(attribute='price') }}

.. _jina_builtin_tests:

#############
Built-in test
#############
****************
callable(object)
****************
Return whether the object is callable (i.e., some kind of function). Note that classes are callable, as are instances with a ``__call__()`` method.

**************
defined(value)
**************
Return true if the variable is defined:

.. sourcecode:: html+jinja
    
    {% if variable is defined %}
        value of variable: {{ variable }}
    {% else %}
        variable is not defined
    {% endif %}

See the ``default()`` filter (`link <https://tedboy.github.io/jinja2/templ14.html#default>`__) for a simple way to set undefined variables.

***********************
divisibleby(value, num)
***********************
Check if a variable is divisible by a number.

*********************
equalto(value, other)
*********************
Check if an object has the same value as another object:

.. sourcecode:: html+jinja

    {% if foo.expression is equalto 42 %}
        the foo attribute evaluates to the constant 42
    {% endif %}

This appears to be a useless test as it does exactly the same as the ``==`` operator, but it **can be useful when used together with the** ``selectattr`` filter (`link <https://tedboy.github.io/jinja2/templ14.html?highlight=selectattr#selectattr>`__):

.. sourcecode:: html+jinja

    {{ users|selectattr("email", "equalto", "foo@bar.invalid") }}

**************
escaped(value)
**************
Check if the value is escaped.

***********
even(value)
***********
Return true if the variable is even.

***************
iterable(value)
***************
Check if it's possible to iterate over an object.

************
lower(value)
************
Return true if the variable is lowercased.

**************
mapping(value)
**************
Return true if the object is a mapping (dict etc.).


***********
none(value)
***********
Return true if the variable is none.

*************
number(value)
*************
Return true if the variable is a number.

**********
odd(value)
**********
Return true if the variable is odd.

********************
sameas(value, other)
********************
Check if an object points to the same memory address than another object:

.. sourcecode:: html+jinja

    {% if foo.attribute is sameas false %}
        the foo attribute really is the `False` singleton
    {% endif %}

***************
sequence(value)
***************
Return true if the variable is a sequence. Sequences are variables that are iterable.

*************
string(value)
*************
Return true if the object is a string.

****************
undefined(value)
****************
Like defined() but the other way round.

************
upper(value)
************
Return true if the variable is uppercased.

#####################
Cusom filter and test
#####################
.. note:: 

    Not sure I need these when using Flask (I never touch ``jinja2.Environment`` when writing Flask app)

    https://tedboy.github.io/jinja2/generated/generated/jinja2.Environment.html

*************
Custom filter
*************
https://tedboy.github.io/jinja2/off_doc.api.html#custom-filters

.. code-block:: python

    def datetimeformat(value, format='%H:%M / %d-%m-%Y'):
        return value.strftime(format)

    # register above function on the template environment
    environment.filters['datetimeformat'] = datetimeformat

In the template:

.. sourcecode:: html+jinja

    written on: {{ article.pub_date|datetimeformat }}
    publication date: {{ article.pub_date|datetimeformat('%d-%m-%Y') }}

***********
Custom test
***********
https://tedboy.github.io/jinja2/off_doc.api.html#custom-tests

.. code-block:: python

    import math

    def is_prime(n):
        if n == 2:
            return True
        for i in xrange(2, int(math.ceil(math.sqrt(n))) + 1):
            if n % i == 0:
                return False
        return True

    # # register above test on the template environment
    environment.tests['prime'] = is_prime

In the template:

.. sourcecode:: html+jinja

    {% if 42 is prime %}
        42 is a prime number
    {% else %}
        42 is not a prime number
    {% endif %}



.. _template_context_def:

############################
Definition: Template Context
############################
https://tedboy.github.io/jinja2/off_doc.api.html#the-context

- The **template context** holds the variables of a template. 
- It stores the **values** passed to the template and also the **names** the template exports. 
- Creating instances is neither supported nor useful as it's created automatically at various stages of the template evaluation and should not be created by hand. 

.. raw:: </br>

- The context is **immutable**. Modifications on :attr:`parent` **must not** happen and modifications on :attr:`vars` are allowed from generated template code only. 
- Template filters and global functions marked as :func:`contextfunction`\s get the active context passed as first argument and are allowed to access the context read-only. 

.. raw:: </br>

- The **template context** supports **read only dict operations** (``get``, ``keys``, ``values``, ``items``, ``iterkeys``, ``itervalues``, ``iteritems``, ``__getitem__``, ``__contains__``). 
- Additionally there is a :meth:`resolve` method that doesn't fail with a `KeyError` but returns an :class:`Undefined` object for missing variables. """

##########
Extensions
##########
- https://tedboy.github.io/jinja2/templ17.html#extensions
- https://tedboy.github.io/jinja2/off_doc.extensions.html

***************************************************
i18n (to mark template parts that are translatable)
***************************************************
https://tedboy.github.io/jinja2/ext2.html#i18n-extension

**Import name**: ``jinja2.ext.i18n``

.. sourcecode:: html+jinja

    <p>{% trans %}Hello {{ user }}!{% endtrans %}</p>
    <p>{% trans user=user.username %}Hello {{ user }}!{% endtrans %}</p>

    {% trans book_title=book.title, author=author.name %}
    This is {{ book_title }} by {{ author }}
    {% endtrans %}

    {# pluraize #}
    {% trans count=list|length %}
    There is {{ count }} {{ name }} object.
    {% pluralize %}
    There are {{ count }} {{ name }} objects.
    {% endtrans %}

**************************************
Expression statement (to modify lists)
**************************************
https://tedboy.github.io/jinja2/ext3.html#expression-statement

**Import name**: ``jinja2.ext.do``

If the **expression-statement extension** is loaded, a tag called ``do`` is available that works exactly like the regular variable expression (``{{ ... }}``); **except it doesn't print anything**. 

This can be **used to modify lists**:

.. sourcecode:: html+jinja

    {% do navigation.append('a string') %}

**********************************************************
Loop controls (enable ``break`` and ``continue`` in loops)
**********************************************************
https://tedboy.github.io/jinja2/ext4.html#loop-controls

**Import name**: ``jinja2.ext.loopcontrols``

.. important:: Note that ``loop.index`` starts with 1, and ``loop.index0`` starts with 0

.. sourcecode:: html+jinja

    {# skips every 2nd item #}
    {% for user in users %}
        {%- if loop.index is even %}{% continue %}{% endif %}
        ...
    {% endfor %}

    {# stop loop after the 10th iteration #}
    {% for user in users %}
        {%- if loop.index >= 10 %}{% break %}{% endif %}
    {%- endfor %}

*******************************************************************
With statement (``with`` keyword for fine-grained variable scoping)
*******************************************************************
https://tedboy.github.io/jinja2/ext5.html#with-extension

**Import name**: ``jinja2.ext.with_``

- This makes it possible to create a new inner scope. 
- **Variables set within this scope are not visible outside of the scope**.

.. sourcecode:: html+jinja

    {% with %}
        {% set foo = 42 %}
        {{ foo }}           foo is 42 here
    {% endwith %}
    foo is not visible here any longer

**TFAE** (I like the first one better)

.. sourcecode:: html+jinja

    {% with foo = 42 %}
        {{ foo }}
    {% endwith %}

    {% with %}
        {% set foo = 42 %}
        {{ foo }}
    {% endwith %}

********************
Autoescape Extension
********************
- https://tedboy.github.io/jinja2/templ18.html#autoescape-extension
- https://tedboy.github.io/jinja2/ext6.html#autoescape-extension

**Import name**: ``jinja2.ext.autoescape``

If the application enables the `Autoescape Extension <https://tedboy.github.io/jinja2/ext6.html#autoescape-extension>`__, one can activate and deactivate the autoescaping from within the templates.

.. sourcecode:: html+jinja

    {% autoescape true %}
        Autoescaping is active within this block
    {% endautoescape %}

    {% autoescape false %}
        Autoescaping is inactive within this block
    {% endautoescape %}

###################################
Tips and Tricks (from official doc)
###################################
https://tedboy.github.io/jinja2/off_doc.tricks.html

****************
Alternating rows
****************
.. sourcecode:: html+jinja

    <ul>
    {% for row in rows %}
      <li class="{{ loop.cycle('odd', 'even') }}">{{ row }}</li>
    {% endfor %}
    </ul>

******************************
Highlighting Active Menu Items
******************************
.. note:: I used to achieve this using jquery...This is better :)

**Child template**

.. sourcecode:: html+jinja

    {% extends "layout.html" %}
    {% set active_page = "index" %}


**Layout template**

.. sourcecode:: html+jinja

    {% set navigation_bar = [
        ('/', 'index', 'Index'),
        ('/downloads/', 'downloads', 'Downloads'),
        ('/about/', 'about', 'About')
    ] -%}
    {% set active_page = active_page|default('index') -%}
    {#- default value assigned to the variable via filter -#}
    ...
    <ul id="navigation">
    {% for href, id, caption in navigation_bar %}
      <li{% if id == active_page %} class="active"{% endif
      %}><a href="{{ href|e }}">{{ caption|e }}</a></li>
    {% endfor %}
    </ul>
    ...


*************************
Accessing the parent Loop
*************************
The special `loop` variable always points to the innermost loop.  If it's
desired to have access to an outer loop it's possible to alias it:

.. sourcecode:: html+jinja

    <table>
    {% for row in table %}
      <tr>
      {% set rowloop = loop %}
      {% for cell in row %}
        <td id="cell-{{ rowloop.index }}-{{ loop.index }}">{{ cell }}</td>
      {% endfor %}
      </tr>
    {% endfor %}
    </table>

