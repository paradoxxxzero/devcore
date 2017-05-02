from setuptools import setup

setup(name='devcore',
      version='0.0.2',
      description='Meta package for a development environment',
      install_requires=[
          'log-colorizer-hook',
          'flask-wdb-hook',
          'wdb',
          'isort',
          'flake8',
          'importmagic',
          'jedi',
          'cutter',
          'better-exceptions-hook'
      ])
