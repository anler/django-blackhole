"""Django application that let's you work in your templates apart from having or not the
corresponding views created.
"""
import os
import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand

import blackhole

py_version = sys.version_info[:2]

here = os.path.abspath(os.path.dirname(__file__))

try:
    README = open(os.path.join(here, "README.rst")).read()
    README += open(os.path.join(here, "HISTORY.rst")).read()
except IOError:
    README = "https://github.com/ikame/django-blackhole"


setup(name="django-blackhole",
      version=blackhole.__version__,
      description=__doc__,
      long_description=README,
      author="ikame",
      author_email="anler86@gmail.com",
      url="https://github.com/ikame/django-blackhole",
      license="MIT",
      keywords="django debug views templates",
      classifiers=[
          "Framework :: Django",
          "Environment :: Web Environment",
          "Intended Audience :: Developers",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 2.7",
          "Topic :: Software Development :: Libraries",
          "Topic :: Utilities"])
