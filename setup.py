import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

required = ['pyramid',
            'pyramid_jinja2',
            'Werkzeug',
            'SQLAlchemy',
            'repoze.tm2',
            'zope.sqlalchemy']

setup(name='RapidGiza',
      version='0.1.4',
      description='Set of paster templates for rapid Pyramid development',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Rocky Burt',
      author_email='rocky@serverzen.com',
      url='http://dist.serverzen.com/pypi/d/rapidgiza/',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=required,
      entry_points = """\
        [paste.paster_create_template]
        rapidgiza=rapidgiza.paster:RapidGizaProjectTemplate
      """
      )
