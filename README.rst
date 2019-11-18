**********
py_contour
**********

Computing contour polygons from data on a rectangular grid.

Cython wrappers around a C library contouring code found here:

http://paulbourke.net/papers/conrec/

Generates contour lines and polygons from recatagular grid of data.

Note that the C lib generates only line segments, which is great for drawing contour lines, but if you need to fill polygons, the code also sorts the line segments into polygons and polylines (for non-closed contours)

Installation
============

Dependencies
------------

Run Time:

* numpy

Built Time:

* setuptools'
* numpy
* cython>0.23

Test Time:

* pytest
* py_gd (optionally)

Building
--------

I don't currently have binary wheels available, so you need to have a properly configured C complier, etc.

Download the source code from gitHub, either as a clone or source tarball::

  pip install ./

should do it. or::

  pip install -e ./

For "editable mode"

Or::

  python setup.py develop

(which is the same thing as pip editable mode)

Testing
-------

Once both ``py_contour`` and ``pytest`` are installed, you should be able to run the tests directly in the source with::

  $ pytest

or::

  $ pytest test_contour.py


Or run the installed tests with::

  py.test --pyargs py_contour


There is also a small example file: ``image_example.py`` that shows how to visualize the results. The image examples require the ``py_gd`` package:

https://github.com/NOAA-ORR-ERD/py_gd

Binaries are available for conda here:

https://anaconda.org/conda-forge/py_gd






