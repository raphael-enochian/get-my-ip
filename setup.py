#!/usr/bin/env python

from distutils.core import setup

setup(name='Get My Ip',
      version='1.0',
      description='Queries DDG API for your IP address and geoip.',
      author='Raphael Enochian',
      author_email='renochian@tutanota.com',
      url='https://github.com/renochian/get-my-ip',
      packages=['distutils', 'distutils.command'],
     )
