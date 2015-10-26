# Peak detection algorithms in Python

This is an overview of all the ready-to-use algorithms I've found to perform peak detection using Python.

## Overview

| Algorithm | Depends on | Local minima? | MatLab `findpeaks`-like? |
|-----------| ----------------- | ------------- | ------------------------ |
| [scipy.signal.find_peaks_cwt](http://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.find_peaks_cwt.html) | Scipy | ? | ✘ |
| [detect_peaks from Marcos Duarte](http://nbviewer.ipython.org/github/demotu/BMC/blob/master/notebooks/DetectPeaks.ipynb) | Numpy | ✘ | ✔ |
| [peakutils.indexes](http://pythonhosted.org/PeakUtils/reference.html#peakutils.peak.indexes) | [PeakUtils package](https://bitbucket.org/lucashnegri/peakutils) | ? | ✘ |
| [peakdetect](https://gist.github.com/sixtenbe/1178136) | Numpy | ? | ✘ |
| [Octave-Forge findpeaks](http://octave.sourceforge.net/signal/function/findpeaks.html) | Octave-Forge and [the oct2py package](https://github.com/blink1073/oct2py) | ? | ✘ |

Note:
* the [peakdetect function](https://gist.github.com/sixtenbe/1178136) that sixtenbe writted is based on [the endolith translation](https://gist.github.com/endolith/250860) of [a MatLab script from Eli Billauer](http://billauer.co.il/peakdet.html)
* The Octave-Forge `findpeaks` needs a complicated and not efficient setup to be runned through Python.
* From theses options, the ones from Marcos Duarte and the PeakUtils are the easier and simpler to use if you come from the MatLab world and/or search a direct equivalent of [the MatLab findpeaks function](http://fr.mathworks.com/help/signal/ref/findpeaks.html).

## How to make your choice?

When you're selecting searching local maxima in signals, you might consider:
* the function interface ;
* the ease of integration in your program.

### Function interface

Does you have any prerequisite for the function interface ?

You may want the function to work natively with Numpy arrays or may search something similar to other platform algorithms, like the MatLab `findpeaks`.

### Ease of integration

Does it require extra dependency? Does is it easy to make it run on a fresh box?

## Usage

For the usage of theses functions, please checkout [the tests](https://github.com/MonsieurV/py-findpeaks/tree/master/tests).

## Make this comparative better

If you've have found something else or want to improve this overview, [let me know](mailto:yoan@ytotech.com) or [open a new ticket](https://github.com/MonsieurV/py-findpeaks/issues/new).

Hoping this helps someone, happy digital processing!
