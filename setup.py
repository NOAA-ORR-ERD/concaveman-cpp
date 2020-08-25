#!/usr/bin/env python

from setuptools import setup, Extension

from Cython.Build import cythonize

import os
import sys
import numpy as np  # For the include directory.

rootpath = os.path.abspath(os.path.dirname(__file__))
long_description = open(os.path.join(rootpath, 'README.md')).read()

include_dirs = [np.get_include(),
                os.path.join(rootpath, 'src', 'cpp')]

# # Need the stdint header for Windows (VS2008).
# if sys.platform.startswith('win') and sys.version_info.major <= 2:
#     include_dirs.append(os.path.join('rootpath', 'src', 'win_headers'))


ext_modules = [Extension("concaveman.concaveman",
                         ["src/concaveman/build_hull.pyx",
                          "src/cpp/concaveman.cpp"],
                         include_dirs=include_dirs,
                         language="c++",
                         language_level='3',
                         )]


def extract_version():
    fname = os.path.join(rootpath, 'src', 'concaveman', '__init__.py')
    with open(fname) as f:
        for line in f:
            if (line.startswith('__version__')):
                version = line.split('=')[1].strip().strip('"')
                break
        else:
            raise ValueError("Couldn't find __version__ in %s" % fname)
    return version

setup(
    name="concaveman",
    version=extract_version(),
    description="Python wrappers around a C++ concave hull Implementation",
    long_description=long_description,
    author="s.adaszewski, Christopher H. Barker",
    author_email="Chris.Barker@noaa.gov",
    url="https://github.com/NOAA-ORR-ERD",
    license="BSD",
    # keywords = "",
    ext_modules=cythonize(ext_modules),
    packages=["src/concaveman", "src/concaveman/tests"],
    install_requires=['numpy', 'scipy'],
    setup_requires=['cython>0.29', 'setuptools'],
    tests_require=['pytest'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: Public Domain",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: C++",
        "Programming Language :: Cython",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Utilities",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Visualization",
    ],
)
