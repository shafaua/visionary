# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

VERSION = '1.0.0'

with open('README.rst') as f:
    readme = f.read()

setup(
    name='visionary',
    description='Client library for Google Cloud Vision API',
    url='https://github.com/shafaua/visionary',
    version=VERSION,
    license="Apache 2.0",
    author=u'Igor Gumenyuk',
    long_description=readme,
    packages=find_packages(),
    install_requires=[
        'requests<3.0.0',
    ],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
