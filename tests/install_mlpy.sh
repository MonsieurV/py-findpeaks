#!/bin/bash
set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
MLPY_DIR="$DIR/mlpy-code"

# Pulling code.
if [ -d "$MLPY_DIR" ]; then
    cd $MLPY_DIR && hg pull
else
    hg clone http://hg.code.sf.net/p/mlpy/code $MLPY_DIR
fi

# We try to install mlpy on Python 2, as the install is not compatible with Python 3.7+.
# (CPython must be updated to support Python 3.7+. See https://github.com/cython/cython/issues/1978)

# Installating dependencies.
# We also install matplotlib for our tests.
pip2 install -U --user numpy scipy matplotlib

# Also requires http://www.gnu.org/software/gsl/ to be installed.

# Installing.
# http://mlpy.sourceforge.net/docs/3.5/install.html
cd $MLPY_DIR
python2 setup.py build_ext --include-dirs=/usr/include/ --rpath=/usr/lib/
python2 setup.py install --user
