#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import find_packages, setup

about = {}
with open(os.path.join(os.path.dirname(__file__), "devcore",
                       "__about__.py")) as f:
    exec(f.read(), about)

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__summary__'],
    url=about['__uri__'],
    author=about['__author__'],
    author_email=about['__email__'],
    license=about['__license__'],
    platforms="Any",
    packages=find_packages(),
    provides=['devcore'],
    install_requires=[
        'log-colorizer-hook', 'flask-wdb-hook',
        'wdb', 'isort', 'importmagic3', 'cutter', 'better-exceptions',
        'semver', 'black==18.9b0'
    ],
    entry_points={
        'console_scripts': ['devcore=devcore.__main__:main', ],
    },
)
