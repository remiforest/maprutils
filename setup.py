#!/usr/bin/env python

from setuptools import setup, find_packages

import maprutils

setup(name='maprutils',
      version=maprutils.__version__,
      include_package_data=True,
      packages=find_packages(),
      description='MapR utilities',
      url='https://github.com/remiforest/maprutils',
      author='Remi Forest',
      author_email='remi.forest@akilio.com',
      license='LICENSE.txt',
    )