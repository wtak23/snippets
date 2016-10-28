flask notes and snippets (``cs-flask``)
"""""""""""""""""""""""""""""""""""""""

.. contents:: `Contents`
   :depth: 1
   :local:


.. admonition:: Best lookups/references
   
    - Configuration Handling https://tedboy.github.io/flask/flask_doc.config.html
    - Useful functions and classes https://tedboy.github.io/flask/interface_api.useful_funcs.html

############################
Useful functions and classes
############################
https://tedboy.github.io/flask/interface_api.useful_funcs.html

- ``flask.current_app`` (`link <https://tedboy.github.io/flask/interface_api.useful_funcs.html#flask.current_app>`__)
- ``flask.has_request_context()`` (`link <https://tedboy.github.io/flask/interface_api.useful_funcs.html#flask.has_request_context>`__)::

    class User(db.Model):

        def __init__(self, username, remote_addr=None):
            self.username = username
            if remote_addr is None and has_request_context():
                remote_addr = request.remote_addr
            self.remote_addr = remote_addr
- ``flask.copy_current_request_context(f)`` (`link <https://tedboy.github.io/flask/interface_api.useful_funcs.html#flask.copy_current_request_context>`__)::

    import gevent
    from flask import copy_current_request_context

    @app.route('/')
    def index():
        @copy_current_request_context
        def do_some_work():
            # do some work here, it can access flask.request like you
            # would otherwise in the view function.
            ...
        gevent.spawn(do_some_work)
        return 'Regular response'
- ``flask.has_app_context()`` (`link <https://tedboy.github.io/flask/interface_api.useful_funcs.html#flask.has_app_context>`__)
- ``flask.url_for(endpoint, **values)`` (`link <https://tedboy.github.io/flask/interface_api.useful_funcs.html#flask.url_for>`__)
- ``flask.abort(code)`` --- ``abort(404)`` (`link <https://tedboy.github.io/flask/interface_api.useful_funcs.html#flask.abort>`__)
- ``flask.redirect(location, code=302, Response=None)`` --- (`link <https://tedboy.github.io/flask/interface_api.useful_funcs.html#flask.redirect>`__)
- ``flask.g`` (**application globals**) (`link <https://tedboy.github.io/flask/interface_api.app_globals.html>`__)
- ``flask.make_response(*args)`` (`link <https://tedboy.github.io/flask/interface_api.useful_funcs.html#flask.make_response>`__)::

    def index():
        response = make_response(render_template('index.html', foo=42))
        response.headers['X-Parachutes'] = 'parachutes are cool'
        return response
- ``flask.after_this_request(f)`` (`link <https://tedboy.github.io/flask/interface_api.useful_funcs.html#flask.after_this_request>`__)::

    @app.route('/')
    def index():
        @after_this_request
        def add_header(response):
            response.headers['X-Foo'] = 'Parachute'
            return response
        return 'Hello World!'
- ``flask.send_file(...)`` (`link <https://tedboy.github.io/flask/interface_api.useful_funcs.html#flask.send_file>`__)
- ``flask.send_from_directory(directory, filename, **options)`` (`link <https://tedboy.github.io/flask/interface_api.useful_funcs.html#flask.send_from_directory>`__)::

    @app.route('/uploads/<path:filename>')
    def download_file(filename):
        return send_from_directory(app.config['UPLOAD_FOLDER'],
                                   filename, as_attachment=True)
- ``flask.safe_join(directory, filename)`` safely join directory and filename (`link <https://tedboy.github.io/flask/interface_api.useful_funcs.html#flask.safe_join>`__)::

    @app.route('/wiki/<path:filename>')
    def wiki_page(filename):
        filename = safe_join(app.config['WIKI_FOLDER'], filename)
        with open(filename, 'rb') as fd:
            content = fd.read()  # Read and process the file content...
- flask.escape(s) (`link <https://tedboy.github.io/flask/interface_api.useful_funcs.html#flask.escape>`__)
- class flask.Markup (`link <https://tedboy.github.io/flask/interface_api.useful_funcs.html#flask.Markup>`__)::

    >>> Markup("Hello <em>World</em>!")
    Markup(u'Hello <em>World</em>!')
    >>> class Foo(object):
    ...  def __html__(self):
    ...   return '<a href="#">foo</a>'
    ...
    >>> Markup(Foo())
    Markup(u'<a href="#">foo</a>')

    >>> Markup.escape("Hello <em>World</em>!")
    Markup(u'Hello &lt;em&gt;World&lt;/em&gt;!')

    >>> em = Markup("<em>%s</em>")
    >>> em % "foo & bar"
    Markup(u'<em>foo &amp; bar</em>')
    >>> strong = Markup("<strong>%(text)s</strong>")
    >>> strong % {'text': '<blink>hacker here</blink>'}
    Markup(u'<strong>&lt;blink&gt;hacker here&lt;/blink&gt;</strong>')
    >>> Markup("<em>Hello</em> ") + "<foo>"
    Markup(u'<em>Hello</em> &lt;foo&gt;')

    >>> Markup("Main &raquo;  <em>About</em>").striptags()
    u'Main \xbb About'

######################################
app (Flask object) summary (whirlwind)
######################################

***********
app.context
***********
.. code-block:: python

    # ===
    with app.app_context():
        # within this block, current_app points to app.
        print current_app.name

***********************
app.teardown_appcontext
***********************
.. code-block:: python

    @app.teardown_appcontext
    def teardown_db(exception):
        db = getattr(g, '_database', None)
        if db is not None:
            db.close()

**********
app.config
**********
https://tedboy.github.io/flask/flask_doc.config.html

To update multiple keys at once you can use the ``dict.update()`` method:

.. code-block:: python

    # === touch app.config stuff ===
    if request.form['username'] != app.config['USERNAME']:
        error = 'Invalid username'

    # === config update with dict style method
    app.config.update(
        DEBUG=True,
        SECRET_KEY='...'
    )


From External file https://tedboy.github.io/flask/interface_api.configuration.html

.. code-block:: python

    app.config.from_pyfile('yourconfig.cfg')

Or using ``from_object`` (in bash, do ``export YOURAPPLICATION_SETTINGS='/path/to/config/file'``)

.. code-block:: python

    DEBUG = True
    SECRET_KEY = 'development key'
    app.config.from_object(__name__)

************************
app.route with variables
************************
.. code-block:: python

    # === routing with variables ===
    @app.route('/user/<username>')
    def show_user_profile(username):
        # show the user profile for that user
        return 'User %s' % username

    @app.route('/post/<int:post_id>')
    def show_post(post_id):
        # show the post with the given id, the id is an integer
        return 'Post %d' % post_id

*****************************
app.route with request object
*****************************
.. code-block:: python

    # === routing with request object ===
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            do_the_login()
        else:
            show_the_login_form()

    # == another example ===
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
    
    # === file upload example ===
    @app.route('/upload', methods=['GET', 'POST'])
    def upload_file():
        if request.method == 'POST':
            f = request.files['the_file']
            f.save('/var/www/uploads/uploaded_file.txt')
        ...

************************
app.test_request_context
************************
.. code-block:: python

    # === url_for and test_requeset_context
    from flask import Flask, url_for
    app = Flask(__name__)
    @app.route('/')
    def index(): pass
    
    @app.route('/login')
    def login(): pass
    
    @app.route('/user/<username>')
    def profile(username): pass
    
    with app.test_request_context():
       print url_for('index')
       print url_for('login')
       print url_for('login', next='/')
       print url_for('profile', username='John Doe')
       #/
       #/login
       #/login?next=/
       #/user/John%20Doe

****************
app.errorhandler
****************
.. code-block:: python

    # ===== error handling =====
    # image we have a view like this
    @app.errorhandler(404)
    def not_found(error):
        return render_template('error.html'), 404

    # You just need to wrap the return expression with flask.make_response
    # and get the object to modify it, then return it
    @app.errorhandler(404)
    def not_found(error):
        resp = make_response(render_template('error.html'), 404)
        resp.headers['X-Something'] = 'A value'
        return resp

    # === redirect and errors === 
    from flask import abort, redirect, url_for

    @app.route('/')
    def index():
        return redirect(url_for('login'))

    @app.route('/login')
    def login():
        abort(401) # 401 means access denied
        this_is_never_executed()

    # === custom error page ===
    from flask import render_template

    @app.errorhandler(404) # 404 means not found
    def page_not_found(error):
        #  the 404 after the render_template() tells Flask that the status code of that page should be 404
        return render_template('page_not_found.html'), 404

***********************************
app.template_filter (custom filter)
***********************************
.. code-block:: python

    # ==== register filter =====
    @app.template_filter('reverse')
    def reverse_filter(s):
        return s[::-1]

    def reverse_filter(s):
        return s[::-1]
    app.jinja_env.filters['reverse'] = reverse_filter

Now you can do this in jinja template file

.. sourcecode:: html+jinja

    {% for x in mylist | reverse %}
    {% endfor %}

****************************************************************
app.context_processor (make var/func accessible in any template)
****************************************************************

.. code-block:: python

    # ===== context processor (to have var/func accessible in template) =====
    @app.context_processor
    def utility_processor():
        def format_price(amount, currency=u'€'):
            return u'{0:.2f}{1}'.format(amount, currency)
        return dict(format_price=format_price)

Now you can do this in jinja template file

.. sourcecode:: html+jinja

    {{ format_price(0.33) }}

********************************
app.logger (haven't used it yet)
********************************
**12. Logging** https://tedboy.github.io/flask/quickstart/quickstart12.html

.. code-block:: python

    app.logger.debug('A value for debugging')
    app.logger.warning('A warning occurred (%d apples)', 42)
    app.logger.error('An error occurred')



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

##################################################################
Application context (to cache resource, like database connections)
##################################################################
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
- https://tedboy.github.io/flask/flask_doc.config.html
- https://tedboy.github.io/flask/interface_api.configuration.html

**Works like a dict** 



*************************
Config from external file
*************************
- https://tedboy.github.io/flask/flask_doc.config.html#configuring-from-files
- https://tedboy.github.io/flask/interface_api.configuration.html

.. code-block:: python

    app.config.from_pyfile('yourconfig.cfg')

Or using ``from_object``

.. code-block:: python

    DEBUG = True
    SECRET_KEY = 'development key'
    app.config.from_object(__name__)

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

******************************
Quick start 9. About Responses
******************************
https://tedboy.github.io/flask/quickstart/quickstart9.html

https://tedboy.github.io/flask/interface_api.useful_funcs.html#flask.make_response

- The return value from a **view function** is automatically converted into a **response object** for you.
- If the return value is a string it's converted into a response object with the string as response body, a ``200 OK`` status code and a **text/html mimetype**.

The logic that Flask applies to converting return values into response objects is as follows:

1.  If a **response object of the correct type is returned** it's directly
    returned from the view.
2.  **If it's a string**, a response object is created with that data and the
    default parameters.
3.  **If a tuple is returned** the items in the tuple can provide extra
    information.  Such tuples have to be in the form ``(response, status,
    headers)`` or ``(response, headers)`` where at least one item has
    to be in the tuple.  The ``status`` value will override the status code
    and ``headers`` can be a list or dictionary of additional header values.
4.  **If none of that works**, Flask will assume the return value is a
    valid WSGI application and convert that into a response object.

If you want to get hold of the resulting response object inside the view
you can use the :func:`~flask.make_response` function.

.. admonition:: Example

    Imagine you have a view like this::

        @app.errorhandler(404)
        def not_found(error):
            return render_template('error.html'), 404

    You just need to wrap the return expression with
    :func:`~flask.make_response` and get the response object to modify it, then
    return it::

        @app.errorhandler(404)
        def not_found(error):
            resp = make_response(render_template('error.html'), 404)
            resp.headers['X-Something'] = 'A value'
            return resp

##############
Session object
##############
To access the current session you can use the session object:

``class flask.session``
    The session object works pretty much like an ordinary dict, with the difference that it keeps track on modifications.

*********
flask api
*********
http://flask.pocoo.org/docs/0.11/api/#sessions

If you have the ``Flask.secret_key`` set you can use **sessions** in Flask applications. A **session** basically makes it possible to remember information from one request to another. 

The way Flask does this is by using a signed cookie. So the user can look at the session contents, but not modify it unless they know the secret key, so make sure to set that to something complex and unguessable.

***********************
Quickstart 10. Sessions
***********************
https://tedboy.github.io/flask/quickstart/quickstart10.html

``session`` allows you to store information specific to a user from one request to the next. This is implemented on top of cookies for you and signs the cookies cryptographically.

.. important:: In order to use sessions you have to set a **secret key**

Here is how sessions work:

.. code-block:: python

    from flask import Flask, session, redirect, url_for, escape, request

    app = Flask(__name__)

    @app.route('/')
    def index():
        if 'username' in session:
            return 'Logged in as %s' % escape(session['username'])
        return 'You are not logged in'

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        return '''
            <form method="post">
                <p><input type=text name=username>
                <p><input type=submit value=Login>
            </form>
        '''

    @app.route('/logout')
    def logout():
        # remove the username from the session if it's there
        session.pop('username', None)
        return redirect(url_for('index'))

    # set the secret key.  keep this really secret:
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

********************************
How to generate good secret keys
********************************
.. note:: **How to generate good secret keys**

   The problem with random is that it's hard to judge what is truly random.  And
   a secret key should be as random as possible.  Your operating system
   has ways to generate pretty random stuff based on a cryptographic
   random generator which can be used to get such a key::

       >>> import os
       >>> os.urandom(24)
       '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'

       Just take that thing and copy/paste it into your code and you're done.

A note on cookie-based sessions: Flask will take the values you put into the
session object and serialize them into a cookie.  If you are finding some
values do not persist across requests, cookies are indeed enabled, and you are
not getting a clear error message, check the size of the cookie in your page
responses compared to the size supported by web browsers.

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

https://tedboy.github.io/flask/interface_api.url_route_regis.html

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

*****************
Custom error page
*****************
https://tedboy.github.io/flask/patterns/errorpages.html

Common Error Codes
------------------

The following error codes are some that are often displayed to the user,
even if the application behaves correctly:

*404 Not Found*
    The good old "chap, you made a mistake typing that URL" message.  So
    common that even novices to the internet know that 404 means: damn,
    the thing I was looking for is not there.  It's a very good idea to
    make sure there is actually something useful on a 404 page, at least a
    link back to the index.

*403 Forbidden*
    If you have some kind of access control on your website, you will have
    to send a 403 code for disallowed resources.  So make sure the user
    is not lost when they try to access a forbidden resource.

*410 Gone*
    Did you know that there the "404 Not Found" has a brother named "410
    Gone"?  Few people actually implement that, but the idea is that
    resources that previously existed and got deleted answer with 410
    instead of 404.  If you are not deleting documents permanently from
    the database but just mark them as deleted, do the user a favour and
    use the 410 code instead and display a message that what they were
    looking for was deleted for all eternity.

*500 Internal Server Error*
    Usually happens on programming errors or if the server is overloaded.
    A terribly good idea is to have a nice page there, because your
    application *will* fail sooner or later (see also:
    :ref:`application-errors`).

Error Handlers
--------------

An error handler is a function, just like a view function, but it is
called when an error happens and is passed that error.  The error is most
likely a :exc:`~werkzeug.exceptions.HTTPException`, but in one case it
can be a different error: a handler for internal server errors will be
passed other exception instances as well if they are uncaught.

An error handler is registered with the :meth:`~flask.Flask.errorhandler`
decorator and the error code of the exception.  Keep in mind that Flask
will *not* set the error code for you, so make sure to also provide the
HTTP status code when returning a response.

Please note that if you add an error handler for "500 Internal Server
Error", Flask will not trigger it if it's running in Debug mode.

Here an example implementation for a "404 Page Not Found" exception::

    from flask import render_template

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

An example template might be this:

.. sourcecode:: html+jinja

   {% extends "layout.html" %}
   {% block title %}Page Not Found{% endblock %}
   {% block body %}
     <h1>Page Not Found</h1>
     <p>What you were looking for is just not there.
     <p><a href="{{ url_for('index') }}">go somewhere nice</a>
   {% endblock %}


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

