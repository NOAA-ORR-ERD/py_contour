#!/usr/bin/env python


from setuptools import setup, Extension
from setuptools.command.test import test as TestCommand

from Cython.Build import cythonize

import os, sys
import numpy

rootpath = os.path.abspath(os.path.dirname(__file__))
long_description = open(os.path.join(rootpath, 'README.rst')).read()

def extract_version(package='py_contour'):
    fname = os.path.join(rootpath, package, '__init__.py')
    with open(fname) as f:
        for line in f:
            if (line.startswith('__version__')):
                version = line.split('=')[1].strip().strip('"')
                break
        else:
            raise ValueError("Couldn't find __version__ in %s"%fname)
    return version


include_dirs = [numpy.get_include(),]
ext_modules=[ Extension("py_contour.contour",
                        ["py_contour/contour.pyx", "py_contour/conrec.cxx"],
                        include_dirs = [numpy.get_include(),]
                         )]

setup(
    name = 'py_contour',
    ext_modules = cythonize(ext_modules),
    packages = ['py_contour'],
    version=extract_version(),
    description="Python wrappers around A C-based contouring code",
    long_description=long_description,
    author="Chris Barker",
    author_email="chris.barker@noaa.gov",
    url="https://github.com/NOAA-ORR-ERD",
    license="Public Domain",
    # keywords = "",
    install_requires=['numpy'],
    setup_requires=['cython>0.23', 'setuptools'],
    tests_require=['pytest'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: Public Domain",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: C",
        "Programming Language :: Cython",
        "Programming Language :: Python :: 2 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Utilities",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Visualization",
    ],
)

