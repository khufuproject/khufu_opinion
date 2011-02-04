.. -*-rst-*-

Introduction
============

RapidGiza is a set of Paster templates that provide out of the box:

  * An application based on the Pyramid_ web application framework

  * Default SQLAlchemy_ engine/session-factory setup

  * All ``.html`` files matched as Jinja2_ templates

  * Werkzeug_ setup for running the app in development mode

  * RESTful_ setup using Pyramid traversal

Important URL's
---------------

  * Project Location - http://dist.serverzen.com/pypi/d/rapidgiza/

  * PyPi Entry - http://pypi.python.org/pypi/RapidGiza

  * Source Control (svn) - https://dev.serverzen.com/svn/public-sandbox/RapidGiza/

Setting up a New Project
========================

Install RapidGiza into a Python environment (ie virtualenv_) with a working
Paster.  Once this has been done, you can create a new RapidGiza project
by simply running (where *Something* is the name of your new egg)::

  paster create -t rapidgiza Something

Once the template egg has been created you should set it up in develop
mode to start working on your project.
::

  cd Something
  python setup.py develop

Using the New Project
=====================

Command Runner
--------------

By default a new script named *something* will be created in the ``bin``
directory of your python envionment.  This script is a command
runner that provides the following::

  usage: something <action> [<options>]
         something --help
  
  actions:
    runserver:
      Run the development server.
      
      :param debug: run in debug mode
      :param verbosity: increase level of logging for more verbose logging
  
      -h, --hostname                string    0.0.0.0
      -p, --port                    integer   8080
      -d, --debug
      -v, --verbosity               integer   0
  
    syncdb:
      Ensure tables exist in the configured database.

Paster
------

A ``development.ini`` file will be created inside the *Something*
directory.  This can be used with the standard ``paster`` commands::

  # use builtin paster http server
  paster serve development.ini

  # use the pyramid pshell command
  paster --plugin=pyramid pshell development.ini pyramid-Something

Apache mod_wsgi
---------------

There is a preconfigured ``Something.wsgi`` file generated which
is necessary for plugging your app into a mod_wsgi environment.

Developing With the New Project
===============================

Base Framework
--------------

RapidGiza is based on the amazing Pyramid_ web application
framework.  As such, the Pyramid_ api will always be
the go-to api for building up the web application.  Please
see the `Pyramid docs`_ for further details.

Templating
----------

Any file ending with the ``.html`` extension located inside
the ``Something/something/templates`` directory will be rendered using
the Jinja2_ templating system.  This template language is
based on the Django templating language.

RapidGiza produces two template files by default, one containing
the overall layout called, ``layout.html`` and one for the default main
page called, ``main.html``.  These pages include HTML5 markup by default.

Data Access
-----------

All data access is handled by the SQLAlchemy_ ORM_ framework which wraps
relational databases.  Out of the box, any new project created by RapidGiza
will have a SQLAlchemy_ database session factory setup.

RapidGiza puts the data model classes inside the ``models.py`` Python
file.  Retrieving a db session inside of a view is done with::

  db_session = request.registry.settings['something.db_session_factory']()

Transaction Support
-------------------

Transactions are used to ensure all or nothing is performed.  With the
very useful `repoze.tm2`_ and transaction_ packages this can
be accomplished easily in Pyramid_ applications.

RapidGiza ensures all requests join a new transaction so that if
any error/exception occurs, the transaction is automatically
rolled back.  Any db sessions created via the provided session
factory automatically join this transaction and will be rolled back
in the event an error occurs.

RESTFul Interface
-----------------

The Pyramid_ web application framework provides a convenient mechanism
to traverse an object graph and map that graph to url's.  This lends
itself to RESTful_ interfaces quite well.

RapidGiza stores it's RESTful traversal mechanism inside of the
``traversal.py`` file.


Developing/Debugging
--------------------

The Werkzeug_ library is used to provide two things:

  1. A very useful debugging middleware

  2. A command runner

Credits
=======

RapidGiza is written and maintained by Rocky Burt
(rocky AT serverzen DOT com).

.. _Jinja2: http://jinja.pocoo.org/
.. _Pyramid: http://docs.pylonshq.com/
.. _`Pyramid Docs`: http://docs.pylonshq.com/pyramid/dev/
.. _Werkzeug: http://werkzeug.pocoo.org/
.. _SQLAlchemy: http://www.sqlalchemy.org/
.. _orm: http://en.wikipedia.org/wiki/Object-relational_mapping
.. _virtualenv: http://pypi.python.org/pypi/virtualenv
.. _RESTful: http://en.wikipedia.org/wiki/Representational_State_Transfer
.. _transaction: http://pypi.python.org/pypi/transaction
.. _`repoze.tm2`: http://pypi.python.org/pypi/repoze.tm2
