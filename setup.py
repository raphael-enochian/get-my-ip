#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='Get My IP',
      version='1.0',
      description='Queries DDG API for your IP address and geoip.',
      author='Raphael Enochian',
      author_email='renochian@tutanota.com',
      url='https://github.com/renochian/get-my-ip',
      scripts=[
          "get-my-ip.py",
      ],
      install_requires=[
          "requests==2.7.0",
      ]
     )
