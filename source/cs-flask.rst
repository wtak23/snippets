flask and jinja notes and snippets (``cs-flask``)
"""""""""""""""""""""""""""""""""""""""""""""""""

.. contents:: `Contents`
   :depth: 2
   :local:


.. admonition:: Best lookups/references
   
    - Configuration Handling (`link <https://tedboy.github.io/flask/flask_doc.config.html>`__)

################
Standard Context
################
The following global variables are available within Jinja2 templates
by default:

.. data:: config
   :noindex:

   The current configuration object (:data:`flask.config`)

   .. versionadded:: 0.6

   .. versionchanged:: 0.10
      This is now always available, even in imported templates.

.. data:: request
   :noindex:

   The current request object (:class:`flask.request`).  This variable is
   unavailable if the template was rendered without an active request
   context.

.. data:: session
   :noindex:

   The current session object (:class:`flask.session`).  This variable
   is unavailable if the template was rendered without an active request
   context.

.. data:: g
   :noindex:

   The request-bound object for global variables (:data:`flask.g`).  This
   variable is unavailable if the template was rendered without an active
   request context.

.. function:: url_for
   :noindex:

   The :func:`flask.url_for` function.

.. function:: get_flashed_messages
   :noindex:

   The :func:`flask.get_flashed_messages` function.

.. admonition:: The Jinja Context Behavior

   These variables are added to the context of variables, they are not
   global variables.  The difference is that by default these will not
   show up in the context of imported templates.  This is partially caused
   by performance considerations, partially to keep things explicit.

   What does this mean for you?  If you have a macro you want to import,
   that needs to access the request object you have two possibilities:

   1.   you explicitly pass the request to the macro as parameter, or
        the attribute of the request object you are interested in.
   2.   you import the macro "with context".

   Importing with context looks like this:

   .. sourcecode:: jinja

      {% from '_helpers.html' import my_macro with context %}

###################
Application context
###################
https://tedboy.github.io/flask/flask_doc.appcontext.html

.. note:: 

    Using ``g`` raises an error saying
    "working outside of application context"

    http://stackoverflow.com/questions/31444036/runtimeerror-working-outside-of-application-context

.. admonition:: Purpose of **application context**
   
   https://tedboy.github.io/flask/flask_doc.appcontext.html#purpose-of-the-application-context

.. admonition:: Creating app-context
   
   .. code-block:: python

       from flask import Flask, current_app

       app = Flask(__name__)
       with app.app_context():
           # within this block, current_app points to app.
           print current_app.name


****************************************
Context Usage (**Database connections**)
****************************************
https://tedboy.github.io/flask/flask_doc.appcontext.html#context-usage

The context is typically used to cache resources that need to be created
on a per-request or usage case.  For instance, database connections are
destined to go there.  When storing things on the application context
unique names should be chosen as this is a place that is shared between
Flask applications and extensions.

The most common usage is to split resource management into two parts:

1.  an implicit resource caching on the context.
2.  a context teardown based resource deallocation.

Generally there would be a ``get_X()`` function that creates resource
``X`` if it does not exist yet and otherwise returns the same resource,
and a ``teardown_X()`` function that is registered as teardown handler.

This is an example that connects to a database::

    import sqlite3
    from flask import g

    def get_db():
        db = getattr(g, '_database', None)
        if db is None:
            db = g._database = connect_to_database()
        return db

    @app.teardown_appcontext
    def teardown_db(exception):
        db = getattr(g, '_database', None)
        if db is not None:
            db.close()

The first time ``get_db()`` is called the connection will be established.
To make this implicit a :class:`~werkzeug.local.LocalProxy` can be used::

    from werkzeug.local import LocalProxy
    db = LocalProxy(get_db)

That way a user can directly access ``db`` which internally calls
``get_db()``.

######################
Configuration Handling
######################
https://tedboy.github.io/flask/flask_doc.config.html

To update multiple keys at once you can use the ``dict.update()`` method:

.. code-block:: python

    app.config.update(
        DEBUG=True,
        SECRET_KEY='...'
    )

*************************
Config from external file
*************************
see https://tedboy.github.io/flask/flask_doc.config.html#configuring-from-files

****************************
Builtin Configuration Values
****************************

The following configuration values are used internally by Flask:

.. tabularcolumns:: |p{6.5cm}|p{8.5cm}|

================================= =========================================
``DEBUG``                         enable/disable debug mode
``TESTING``                       enable/disable testing mode
``PROPAGATE_EXCEPTIONS``          explicitly enable or disable the
                                  propagation of exceptions.  If not set or
                                  explicitly set to ``None`` this is
                                  implicitly true if either ``TESTING`` or
                                  ``DEBUG`` is true.
``PRESERVE_CONTEXT_ON_EXCEPTION`` By default if the application is in
                                  debug mode the request context is not
                                  popped on exceptions to enable debuggers
                                  to introspect the data.  This can be
                                  disabled by this key.  You can also use
                                  this setting to force-enable it for non
                                  debug execution which might be useful to
                                  debug production applications (but also
                                  very risky).
``SECRET_KEY``                    the secret key
``SESSION_COOKIE_NAME``           the name of the session cookie
``SESSION_COOKIE_DOMAIN``         the domain for the session cookie.  If
                                  this is not set, the cookie will be
                                  valid for all subdomains of
                                  ``SERVER_NAME``.
``SESSION_COOKIE_PATH``           the path for the session cookie.  If
                                  this is not set the cookie will be valid
                                  for all of ``APPLICATION_ROOT`` or if
                                  that is not set for ``'/'``.
``SESSION_COOKIE_HTTPONLY``       controls if the cookie should be set
                                  with the httponly flag.  Defaults to
                                  ``True``.
``SESSION_COOKIE_SECURE``         controls if the cookie should be set
                                  with the secure flag.  Defaults to
                                  ``False``.
``PERMANENT_SESSION_LIFETIME``    the lifetime of a permanent session as
                                  :class:`datetime.timedelta` object.
                                  Starting with Flask 0.8 this can also be
                                  an integer representing seconds.
``SESSION_REFRESH_EACH_REQUEST``  this flag controls how permanent
                                  sessions are refreshed.  If set to ``True``
                                  (which is the default) then the cookie
                                  is refreshed each request which
                                  automatically bumps the lifetime.  If
                                  set to ``False`` a `set-cookie` header is
                                  only sent if the session is modified.
                                  Non permanent sessions are not affected
                                  by this.
``USE_X_SENDFILE``                enable/disable x-sendfile
``LOGGER_NAME``                   the name of the logger
``LOGGER_HANDLER_POLICY``         the policy of the default logging
                                  handler.  The default is ``'always'``
                                  which means that the default logging
                                  handler is always active.  ``'debug'``
                                  will only activate logging in debug
                                  mode, ``'production'`` will only log in
                                  production and ``'never'`` disables it
                                  entirely.
``SERVER_NAME``                   the name and port number of the server.
                                  Required for subdomain support (e.g.:
                                  ``'myapp.dev:5000'``)  Note that
                                  localhost does not support subdomains so
                                  setting this to “localhost” does not
                                  help.  Setting a ``SERVER_NAME`` also
                                  by default enables URL generation
                                  without a request context but with an
                                  application context.
``APPLICATION_ROOT``              If the application does not occupy
                                  a whole domain or subdomain this can
                                  be set to the path where the application
                                  is configured to live.  This is for
                                  session cookie as path value.  If
                                  domains are used, this should be
                                  ``None``.
``MAX_CONTENT_LENGTH``            If set to a value in bytes, Flask will
                                  reject incoming requests with a
                                  content length greater than this by
                                  returning a 413 status code.
``SEND_FILE_MAX_AGE_DEFAULT``     Default cache control max age to use with
                                  :meth:`~flask.Flask.send_static_file` (the
                                  default static file handler) and
                                  :func:`~flask.send_file`, as
                                  :class:`datetime.timedelta` or as seconds.
                                  Override this value on a per-file
                                  basis using the
                                  :meth:`~flask.Flask.get_send_file_max_age`
                                  hook on :class:`~flask.Flask` or
                                  :class:`~flask.Blueprint`,
                                  respectively. Defaults to 43200 (12 hours).
``TRAP_HTTP_EXCEPTIONS``          If this is set to ``True`` Flask will
                                  not execute the error handlers of HTTP
                                  exceptions but instead treat the
                                  exception like any other and bubble it
                                  through the exception stack.  This is
                                  helpful for hairy debugging situations
                                  where you have to find out where an HTTP
                                  exception is coming from.
``TRAP_BAD_REQUEST_ERRORS``       Werkzeug's internal data structures that
                                  deal with request specific data will
                                  raise special key errors that are also
                                  bad request exceptions.  Likewise many
                                  operations can implicitly fail with a
                                  BadRequest exception for consistency.
                                  Since it's nice for debugging to know
                                  why exactly it failed this flag can be
                                  used to debug those situations.  If this
                                  config is set to ``True`` you will get
                                  a regular traceback instead.
``PREFERRED_URL_SCHEME``          The URL scheme that should be used for
                                  URL generation if no URL scheme is
                                  available.  This defaults to ``http``.
``JSON_AS_ASCII``                 By default Flask serialize object to
                                  ascii-encoded JSON.  If this is set to
                                  ``False`` Flask will not encode to ASCII
                                  and output strings as-is and return
                                  unicode strings.  ``jsonify`` will
                                  automatically encode it in ``utf-8``
                                  then for transport for instance.
``JSON_SORT_KEYS``                By default Flask will serialize JSON
                                  objects in a way that the keys are
                                  ordered.  This is done in order to
                                  ensure that independent of the hash seed
                                  of the dictionary the return value will
                                  be consistent to not trash external HTTP
                                  caches.  You can override the default
                                  behavior by changing this variable.
                                  This is not recommended but might give
                                  you a performance improvement on the
                                  cost of cachability.
``JSONIFY_PRETTYPRINT_REGULAR``   If this is set to ``True`` (the default)
                                  jsonify responses will be pretty printed
                                  if they are not requested by an
                                  XMLHttpRequest object (controlled by
                                  the ``X-Requested-With`` header)
``JSONIFY_MIMETYPE``              MIME type used for jsonify responses.
``TEMPLATES_AUTO_RELOAD``         Whether to check for modifications of
                                  the template source and reload it
                                  automatically. By default the value is
                                  ``None`` which means that Flask checks
                                  original file only in debug mode.
``EXPLAIN_TEMPLATE_LOADING``      If this is enabled then every attempt to
                                  load a template will write an info
                                  message to the logger explaining the
                                  attempts to locate the template.  This
                                  can be useful to figure out why
                                  templates cannot be found or wrong
                                  templates appear to be loaded.
================================= =========================================


#########################
Refresher on HTTP Methods
#########################
(**From Flask Doc-page**)

The HTTP method (also often called "the verb") tells the server what the
client wants to *do* with the requested page.  The following methods are
very common:

``GET``
    The browser tells the server to just *get* the information stored on
    that page and send it.  This is probably the most common method.

``HEAD``
    The browser tells the server to get the information, but it is only
    interested in the *headers*, not the content of the page.  An
    application is supposed to handle that as if a ``GET`` request was
    received but to not deliver the actual content.  In Flask you don't
    have to deal with that at all, the underlying Werkzeug library handles
    that for you.

``POST``
    The browser tells the server that it wants to *post* some new
    information to that URL and that the server must ensure the data is
    stored and only stored once.  This is how HTML forms usually
    transmit data to the server.

``PUT``
    Similar to ``POST`` but the server might trigger the store procedure
    multiple times by overwriting the old values more than once.  Now you
    might be asking why this is useful, but there are some good reasons
    to do it this way.  Consider that the connection is lost during
    transmission: in this situation a system between the browser and the
    server might receive the request safely a second time without breaking
    things.  With ``POST`` that would not be possible because it must only
    be triggered once.

``DELETE``
    Remove the information at the given location.

``OPTIONS``
    Provides a quick way for a client to figure out which methods are
    supported by this URL.  Starting with Flask 0.6, this is implemented
    for you automatically.

Now the interesting part is that in HTML4 and XHTML1, the only methods a
form can submit to the server are ``GET`` and ``POST``.  But with JavaScript
and future HTML standards you can use the other methods as well.  Furthermore
HTTP has become quite popular lately and browsers are no longer the only
clients that are using HTTP. For instance, many revision control systems
use it.

.. _HTTP RFC: http://www.ietf.org/rfc/rfc2068.txt



#############
Using url_for
#############
- https://tedboy.github.io/flask/quickstart/quickstart4.html#url-building
- http://stackoverflow.com/questions/7478366/create-dynamic-urls-in-flask-with-url-for

``url_for('add', variable=foo)``, where we have the definition below:

.. code-block:: python

    def add(variable): ...

And in the **template** file, you can do:

.. code:: html

    <script src="{{ url_for('static', filename='jquery.min.js') }}"></script>``

.. code-block:: python

    url_for('name of the function of the route','parameters (if required)')

.. note:: 

    ``test_request_context()`` tells Flask to behave as though it is handling a request, even though we are interacting with it through a Python shell

.. code-block:: python

    >>> from flask import Flask, url_for
    >>> app = Flask(__name__)
    >>> @app.route('/')
    ... def index(): pass
    ...
    >>> @app.route('/login')
    ... def login(): pass
    ...
    >>> @app.route('/user/<username>')
    ... def profile(username): pass
    ...
    >>> with app.test_request_context():
    ...  print url_for('index')
    ...  print url_for('login')
    ...  print url_for('login', next='/')
    ...  print url_for('profile', username='John Doe')
    ...
    /
    /login
    /login?next=/
    /user/John%20Doe

#####################################
Variable rules in routing (app.route)
#####################################
**4. Routing** https://tedboy.github.io/flask/quickstart/quickstart4.html

The following converters exist:

.. csv-table:: 
    :delim: |

    string  | accepts any text without a slash (the default)
    int     | accepts integers
    float  | like int but for floating point values
    path   | like the default but also accepts slashes
    any | matches one of the items provided
    uuid  |  accepts UUID strings

.. code-block:: python

    @app.route('/user/<username>')
    def show_user_profile(username):
        # show the user profile for that user
        return 'User %s' % username

    @app.route('/post/<int:post_id>')
    def show_post(post_id):
        # show the post with the given id, the id is an integer
        return 'Post %d' % post_id

##############
Request object
##############

- https://tedboy.github.io/flask/interface_api.incoming_request_data.html
- https://tedboy.github.io/flask/generated/generated/flask.Request.html

.. admonition:: ``flask.request``

    https://tedboy.github.io/flask/interface_api.incoming_request_data.html#flask.request

    To access incoming request data, you can use the global ``request`` object. Flask parses incoming request data for you and gives you access to it through that global object. Internally Flask makes sure that you always get the correct data for the active thread if you are in a multithreaded environment.

    The ``request`` object is an instance of a ``Request`` subclass and provides all of the attributes Werkzeug defines. This just shows a quick overview of the most important ones.

*****************************
Quickstart - 4.3 HTTP Methods
*****************************
https://tedboy.github.io/flask/quickstart/quickstart4.html#http-methods

By default, a route only answers to ``GET`` requests, but that can be changed by providing the methods argument to the ``route()`` decorator. 

.. code-block:: python

    from flask import request

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            do_the_login()
        else:
            show_the_login_form()

**************************************
Quickstart - 7. Accessing Request Data
**************************************

Request object
==============
https://tedboy.github.io/flask/quickstart/quickstart7.html#the-request-object

.. note:: For web applications it's crucial to react to the data a client sends to the server. In Flask this information is provided by the global request object.

https://github.com/pallets/flask/blob/master/examples/flaskr/flaskr/flaskr.py

.. code-block:: python

    from flask import request

    if request.form['username'] != app.config['USERNAME']:
        error = 'Invalid username'


``method`` and ``form`` attribute

- ``method`` = current request method
- ``form`` = form data (data transmitted in a ``POST`` or ``PUT`` request)

.. code-block:: python

    @app.route('/login', methods=['POST', 'GET'])
    def login():
        error = None
        if request.method == 'POST':
            if valid_login(request.form['username'],
                           request.form['password']):
                return log_the_user_in(request.form['username'])
            else:
                error = 'Invalid username/password'
        # the code below is executed if the request method
        # was GET or the credentials were invalid
        return render_template('login.html', error=error)

File uploads
============
https://tedboy.github.io/flask/quickstart/quickstart7.html#file-uploads

.. code-block:: python

    from flask import request

    @app.route('/upload', methods=['GET', 'POST'])
    def upload_file():
        if request.method == 'POST':
            f = request.files['the_file']
            f.save('/var/www/uploads/uploaded_file.txt')
        ...

Cookies
=======
https://tedboy.github.io/flask/quickstart/quickstart7.html#cookies

.. code-block:: python

    # === reading cookies ===
    # The cookies attribute of request objects is a dictionary with all 
    # the cookies the client transmits
    @app.route('/')
    def index():
        username = request.cookies.get('username')
        # use cookies.get(key) instead of cookies[key] to not get a
        # KeyError if the cookie is missing.

    # === storing cookies ===
    # use the ``set_cookie`` method of response objects
    from flask import make_response

    @app.route('/')
    def index():
        resp = make_response(render_template(...))
        resp.set_cookie('username', 'the username')
        return resp



###############
Response object
###############
.. admonition:: flask.Response
   
   ``flask.Response(response=None, status=None, headers=None, mimetype=None, content_type=None, direct_passthrough=False)``

   http://flask.pocoo.org/docs/0.11/api/#response-objects

   The response object that is used by default in Flask. Works like the response object from Werkzeug but is set to have an HTML mimetype by default. Quite often you don’t have to create this object yourself because make_response() will take care of that for you.



##############
Session object
##############

.. admonition:: Description
   
   http://flask.pocoo.org/docs/0.11/api/#sessions

   If you have the ``Flask.secret_key`` set you can use **sessions** in Flask applications. A **session** basically makes it possible to remember information from one request to another. 

   The way Flask does this is by using a signed cookie. So the user can look at the session contents, but not modify it unless they know the secret key, so make sure to set that to something complex and unguessable.

   To access the current session you can use the session object:

   ``class flask.session``
        The session object works pretty much like an ordinary dict, with the difference that it keeps track on modifications.

######################
Redirecting and errors
######################
**Redirects and Errors** https://tedboy.github.io/flask/quickstart/quickstart8.html

.. code-block:: python

    from flask import abort, redirect, url_for

    @app.route('/')
    def index():
        return redirect(url_for('login'))

    @app.route('/login')
    def login():
        abort(401) # 401 means access denied
        this_is_never_executed()

Custom error page

.. code-block:: python

    from flask import render_template

    @app.errorhandler(404) # 404 means not found
    def page_not_found(error):
        #  the 404 after the render_template() tells Flask that the status code of that page should be 404
        return render_template('page_not_found.html'), 404

*****************************
Error handling (not read yet)
*****************************
https://tedboy.github.io/flask/flask_doc.errorhandling.html

###########
json stuffs
###########
- https://tedboy.github.io/flask/interface_api.json_support.html

.. function:: tojson
   :noindex:

   This function converts the given object into JSON representation.  This
   is for example very helpful if you try to generate JavaScript on the
   fly.

   Note that inside ``script`` tags no escaping must take place, so make
   sure to disable escaping with ``|safe`` before Flask 0.10 if you intend
   to use it inside ``script`` tags:

   .. sourcecode:: html+jinja

       <script type=text/javascript>
           doSomethingWith({{ user.username|tojson|safe }});
       </script>

*************
flask.jsonify
*************
- https://tedboy.github.io/flask/generated/flask.jsonify.html
- https://tedboy.github.io/flask/interface_api.json_support.html#flask.json.jsonify

Example usage

.. code-block:: python

    from flask import jsonify

    @app.route('/_get_current_user')
    def get_current_user():
        return jsonify(username=g.user.username,
                       email=g.user.email,
                       id=g.user.id)

This will send a JSON response like this to the browser:

.. code-block:: json
    
    {
        "username": "admin",
        "email": "admin@localhost",
        "id": 42
    }

#############################################
Registering filters (``app.template_filter``)
#############################################
The two following examples work the same and both reverse an object::

    @app.template_filter('reverse')
    def reverse_filter(s):
        return s[::-1]

    def reverse_filter(s):
        return s[::-1]
    app.jinja_env.filters['reverse'] = reverse_filter

In case of the decorator the argument is optional if you want to use the
function name as name of the filter.  Once registered, you can use the filter
in your templates in the same way as Jinja2's builtin filters, for example if
you have a Python list in context called `mylist`:

.. sourcecode:: html+jinja

    {% for x in mylist | reverse %}
    {% endfor %}


##############################################
Context Processors (``app.context_processor``)
##############################################
Let's you define variable/function accessible in the template.

Below is an example of a function

.. code-block:: python

    @app.context_processor
    def utility_processor():
        def format_price(amount, currency=u'€'):
            return u'{0:.2f}{1}'.format(amount, currency)
        return dict(format_price=format_price)

Then in the template:

.. sourcecode:: html+jinja

    {{ format_price(0.33) }}

