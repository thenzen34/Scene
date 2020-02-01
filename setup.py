#!/usr/bin/env python

from os.path import join, dirname

from setuptools import setup, find_packages

setup(
    name='Scene',

    version='1.1',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.txt')).read(), install_requires=['svgwrite', 'numpy',
                                                                                           'pygame', 'Pillow',
                                                                                           'shapely', 'matplotlib',
                                                                                           'peewee', 'scipy',
                                                                                           'svgpathtools']
)
