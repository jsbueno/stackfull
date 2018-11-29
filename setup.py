# -*- coding: utf-8 -*-
# Author: João S. O. bueno

from pathlib import Path
from setuptools import setup

import os

version = "1.0.0"
description = "Tools for stack-usage in Python expressions"

def filedata(name):
    try:
        return open(name).read()
    except Exception as error:
        return ""

here = Path(os.path.abspath(os.path.dirname(__file__)))
docs = here / "docs"

long_description = "\n".join((filedata("README.txt"),
    filedata(docs / "INSTALL.txt"),
    filedata(docs / "CREDITS.txt"),
    filedata(docs / "STACKFULL.txt"),
    ))

setup(
    name='stackfull',
    py_modules=['stackfull'],
    package_dir={'':'src'},
    version=version,
    description=description,
    long_description=long_description,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        'License :: OSI Approved :: Python Software Foundation License',
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='python expressions stack acelerator utils push pop',
    author='João S. O. Bueno',
    author_email='gwidion@gmail.com',
    url='https://github.com/jsbueno/stackfull',
    license='License :: OSI Approved :: Python Software Foundation License',
    zip_safe=False,
    install_requires=[],
    extras_require={},
    entry_points="",
)
