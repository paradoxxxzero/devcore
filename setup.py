#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is part of unrest
#
# A troubling rest api library for sqlalchemy models
# Copyright © 2017 Kozea Florian Mounier
#
# This library is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with pygal. If not, see <http://www.gnu.org/licenses/>.

import os


from setuptools import find_packages, setup

about = {}
with open(os.path.join(
        os.path.dirname(__file__), "devcore", "__about__.py")) as f:
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
        'log-colorizer-hook',
        'flask-wdb-hook',
        'wdb',
        'isort',
        'flake8',
        'importmagic',
        'jedi',
        'cutter',
        'better-exceptions-hook',
        'semver'
    ],
    entry_points={
        'console_scripts': [
            'devcore=devcore.__main__:main',
        ],
    },
)
