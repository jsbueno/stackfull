# -*- coding: utf-8 -*-
# Author: João S. O. bueno

from setuptools import setup

import os

version = '0.9'
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
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='python expressions stack acelerator utils',
    author='João S. O. Bueno',
    author_email='jsbueno@simplesconsultoria.com.br',
    url='https://github.com/jsbueno/stackfull',
    license='License :: OSI Approved :: Python Software Foundation License',
    py_modules=['stackfull'],
    zip_safe=False,
    install_requires=[],
    extras_require={},
    entry_points="",
)
