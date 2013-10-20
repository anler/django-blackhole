"""Django application that let's you work in your templates apart from having or not the
corresponding views created.
"""
import os
import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand

py_version = sys.version_info[:2]

here = os.path.abspath(os.path.dirname(__file__))

try:
    README = open(os.path.join(here, "README.rst")).read()
    README += open(os.path.join(here, "HISTORY.rst")).read()
except IOError:
    README = "https://github.com/ikame/django-blackhole"


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(name="django-blackhole",
      version='0.1.7',
      description=__doc__,
      long_description=README,
      author="ikame",
      author_email="anler86@gmail.com",
      url="https://github.com/ikame/django-blackhole",
      packages = ["blackhole"],
      tests_require=["pytest", "django"],
      cmdclass={"test": PyTest},
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
