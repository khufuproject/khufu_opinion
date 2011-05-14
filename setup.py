import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()

required = [
    'pyramid >= 1.0',
    'Chameleon < 2.0dev',
    'pyramid_jinja2',
    'khufu_sqlalchemy',
    'khufu_script',
]

setup(name='khufu_opinion',
      version='0.5',
      description='Set of paster templates for rapid Pyramid development',
      long_description=README + '\n\n' + CHANGES,
      license='BSD',
      classifiers=[
        "License :: OSI Approved :: BSD License",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        ],
      author='Rocky Burt',
      author_email='rocky@serverzen.com',
      url='https://github.com/khufuproject/khufu_opinion',
      keywords='wsgi pylons pyramid sqlalchemy khufu jinja2',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=required,
      entry_points="""
        [paste.paster_create_template]
        khufu_starter=khufu_opinion.paster:KhufuOpinionProjectTemplate
      """
      )
