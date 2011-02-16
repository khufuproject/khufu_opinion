.. -*-rst-*-

Introduction
============

RapidGiza_ is a set of paster templates for rapid Pyramid development.  It
makes several framework choices for the developer which are:

  * Pyramid_ for the underlying web framework

    - traversal based url routing

  * Jinja2_ for the page template language (similar to Django templates)

  * SQLAlchemy_ for ORM-based relational database persistence


Important URL's
---------------

  * Source Control - https://github.com/serverzen/RapidGiza

  * PyPi Entry - http://pypi.python.org/pypi/RapidGiza

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

  Commands:
      runserver             Run a reloadable development web server.

Paster
------

A ``development.ini`` file will be created inside the *Something*
directory.  This can be used with the standard ``paster`` commands::

  # use builtin paster http server
  paster serve development.ini

  # use the pyramid pshell command
  paster --plugin=pyramid pshell development.ini pyramid-Something

Deployment with Apache+mod_wsgi
-------------------------------

There is a preconfigured ``Something.wsgi`` file generated which
is necessary for plugging your app into a mod_wsgi environment.

A simple apache virtualhost entry will look like this::

  <VirtualHost *:80>
      ServerName www.something.com
  
      WSGIScriptAlias / /path/to/Something.wsgi
  </VirtualHost>


Developing With the New Project
===============================

Base Framework
--------------

RapidGiza is based on the Pyramid_ web application
framework.  As such, the Pyramid_ api will always be
the go-to api for working with the web application.  Please
see the `Pyramid docs`_ for further details.

Templating
----------

Any file ending with the ``.jinja2`` extension located inside
the ``Something/something/templates`` directory will be rendered using
the Jinja2_ templating system.  This template language is
based on the Django templating language.

RapidGiza produces two template files by default, one containing
the overall layout called, ``layout.jinja2`` and one for the default main
page called, ``main.jinja2``.

Data Access
-----------

All data access is handled by the SQLAlchemy_ ORM_ framework which wraps
relational databases.  Out of the box, any new project created by RapidGiza
will have a SQLAlchemy_ database session factory setup.

RapidGiza puts the orm model classes inside the ``models.py`` Python
file.  The active database session can always be retrieved as the ``db``
attribute on the ``request`` object.

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

Traversal
---------

The Pyramid_ web application framework provides a convenient mechanism
to traverse an object graph and map that graph to url's.  RapidGiza stores
it's traversal mechanism inside of the ``traversal.py`` file.

Credits
=======

  * Created and maintained by Rocky Burt (rocky AT serverzen DOT com)

.. _Jinja2: http://jinja.pocoo.org/
.. _Pyramid: http://docs.pylonshq.com/
.. _`Pyramid Docs`: http://docs.pylonshq.com/pyramid/dev/
.. _SQLAlchemy: http://www.sqlalchemy.org/
.. _orm: http://en.wikipedia.org/wiki/Object-relational_mapping
.. _virtualenv: http://pypi.python.org/pypi/virtualenv
.. _transaction: http://pypi.python.org/pypi/transaction
.. _`repoze.tm2`: http://pypi.python.org/pypi/repoze.tm2
.. _`Khufu-Script`: http://pypi.python.org/pypi/Khufu-Script
.. _RapidGiza: http://pypi.python.org/pypi/RapidGiza
