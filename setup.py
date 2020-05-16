#!/usr/bin/env python

from os.path import join, dirname

from setuptools import setup, find_packages

import Scene

setup(
    name='Scene_tz',

    version=Scene.__version__,
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.txt')).read()
)
