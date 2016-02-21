# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

VERSION = '1.0.0'

setup(
    name='visionary',
    description='Client library for Google Cloud Vision',
    url='https://github.com/shafaua/visionary',
    version=VERSION,
    author=u'Igor Gumenyuk',
    packages=find_packages(),
    install_requires=[
        'requests<3.0.0',
    ],
    include_package_data=True,
    zip_safe=False,
)
