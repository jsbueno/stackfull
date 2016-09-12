# -*- coding: utf-8 -*-
# Author: João S. O. bueno

from setuptools import setup

import os

version = '0.10'
description = "Tools for stack-usage in Python expressions",

def filedata(name):
    try:
        return open(name).read()
    except Exception as error:
        return ""

long_description = "\n".join((filedata("README.txt"),
    filedata("docs/INSTALL.txt"),
    filedata("docs/CREDITS.txt"),
    filedata("docs/HISTORY.txt"),
    ))

setup(
    name='stackfull',
    version=version,
    description=description,
    long_description=long_description,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        'License :: OSI Approved :: Python Software Foundation License',
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='python expressions stack acelerator utils push pop',
    author='João S. O. Bueno',
    author_email='gwidion@gmail.com',
    url='https://github.com/jsbueno/stackfull',
    license='License :: OSI Approved :: Python Software Foundation License',
    py_modules=['stackfull'],
    zip_safe=False,
    install_requires=[],
    extras_require={},
    entry_points="",
)
