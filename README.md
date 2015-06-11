# MatLab/Octave findpeaks in Python/Scipy

Python implementation of the Octave-Forge [findpeaks](http://octave.sourceforge.net/signal/function/findpeaks.html) ([source](http://sourceforge.net/p/octave/signal/ci/eacfdb0962e8321ac29b677afc06683b616e83da/tree/inst/findpeaks.m)), so we have a findpeaks similar to the MatLab one to use with Numpy/Scipy (it is not easy to have the same result than the MatLab/Octave findpeaks with the Scipy [find_peaks_cwt()](http://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.find_peaks_cwt.html)).

This implementation is in alpha version and have *not* been extensively been test against the original Octave-Forge version.

If you are interested to use it and encounter any issue, please let me know and [report it](https://github.com/MonsieurV/py-findpeaks/issues/new).

Happy digital signal processing to you!