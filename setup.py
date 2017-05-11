#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

VERSION = __import__('balancer').__version__

try:
    long_description = open('README.rst', 'rt').read()
except IOError:
    long_description = ''

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

description = 'A set of tools for using Django\'s multi-db feature to balance '\
              'database requests'

setup(
    name='django-balancer',
    version=VERSION,
    description=description,
    long_description=long_description,
    author='Brandon Konkle, Mike Helmick',
    author_email='mike@drund.com',
    license='BSD License',
    url='https://github.com/michaelhelmick/django-balancer',
    packages=['balancer'],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'Development Status :: 3 - Alpha',
        'Topic :: Database',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English'
    ]
)
