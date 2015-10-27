# Peak detection algorithms in Python

This is an overview of all the ready-to-use algorithms I've found to perform peak detection using Python.

## Overview

| Algorithm | Depends on | Filters | Local minima? | MatLab `findpeaks`-like? |
|-----------| ----------------- | ------------- | ------------------------ |
| [scipy.signal.find_peaks_cwt](#scipy.signal.find_peaks_cwt) | Scipy | Max distance | ✘ | ✘ |
| [detect_peaks]() | Numpy | Minimum distance<br>Minimum heigth | ✘ | ✔ |
| [peakutils.indexes]() | PeakUtils and Scipy | ? | ? | ✘ |
| [peakdetect]() | Scipy | ? | ? | ✘ |
| [Octave-Forge findpeaks]() | Octave-Forge, oct2py and Scipy | ? | ? | ✘ |

Note:
* From theses options, the ones from Marcos Duarte and the PeakUtils are the easier and simpler to use if you come from the MatLab world and/or search a direct equivalent of [the MatLab findpeaks function](http://fr.mathworks.com/help/signal/ref/findpeaks.html).

## How to make your choice?

When you're selecting searching local maxima in signals, you might consider:
* the function interface ;
* the ease of integration in your program.

### Function interface

Does you have any prerequisite for the function interface?

You may want the function to work natively with Numpy arrays or may search something similar to other platform algorithms, like the MatLab [`findpeaks`](http://fr.mathworks.com/help/signal/ref/findpeaks.html).

### Ease of integration

Does it require extra dependency? Does is it easy to make it run on a fresh box?

## scipy.signal.find_peaks_cwt

[Documentation](http://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.find_peaks_cwt.html).

The peak detection algorithm from the Scipy signal processing package. It appears like the obvious choice when you already work with Scipy.

However this algorithm requires to understand wavelets to be well used, as its interface is constructed after the wavelet convolution approach. Its use may be thus judged as less trivial and direct than other algorithms.

## detect_peaks from Marcos Duarte

[Documentation](http://nbviewer.ipython.org/github/demotu/BMC/blob/master/notebooks/DetectPeaks.ipynb).

This algorithm comes from a notebook written by Marcos Duarte.

The function has an interface very similar and consistent results to the MatLab Signal Processing Toolbox `findpeaks`, yet with less complete filtering and tuning support. It can been considered trivial to use.

## peakutils.indexes

[Documentation](http://pythonhosted.org/PeakUtils/reference.html#peakutils.peak.indexes).
[Package](https://bitbucket.org/lucashnegri/peakutils).

This algorithm can be used as an equivalent of the MatLab `findpeaks` if you don't need filtering other than minimal distance.

## peakdetect from sixtenbe

[Source and documentation](https://gist.github.com/sixtenbe/1178136).

The algorithm was written by sixtenbe based on the previous work of [endolith](https://gist.github.com/endolith/250860) and [Eli Billauer](http://billauer.co.il/peakdet.html).

Easy to make it work, but may miss filtering capacities.

## Octave-Forge findpeaks

[Documentation](http://octave.sourceforge.net/signal/function/findpeaks.html).
[oct2py package](https://github.com/blink1073/oct2py).

Use the Octave-Forge `findpeaks` through the oct2py bridge.

Requires a complicated and not very efficient setup to be called from Python code. Of course, you will need an up-to-date distribution of Octave.

----------------------------------

## Contribute

If you've have found something else or want to improve this overview, feel free to [open a new ticket](https://github.com/MonsieurV/py-findpeaks/issues/new) or submit a PR.

Hoping this helps someone, happy digital processing!
