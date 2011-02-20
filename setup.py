import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

required = [
    'pyramid >= 1.0',
    'pyramid_jinja2',
    'Khufu-SQLAHelper',
    'Khufu-Script',
    'WebError',
]

setup(name='khufu_opinion',
      version='0.2.1',
      description='Set of paster templates for rapid Pyramid development',
      long_description=README + '\n\n' + CHANGES,
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
      url='https://github.com/serverzen/khufu_opinion',
      keywords='web wsgi bfg pylons pyramid sqlalchemy khufu jinja2',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=required,
      entry_points="""
        [paste.paster_create_template]
        khufu_opinion=khufu_opinion.paster:KhufuOpinionProjectTemplate
      """
      )
