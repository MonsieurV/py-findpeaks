# findpeaks alternatives in the Python world

Overview of all the alternatives I've found to do peak detection (local maxima) in Python.

The main alternatives are:
* Use [find_peaks_cwt](http://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.find_peaks_cwt.html) from the Scipy signal processing module
* Use the [detect_peaks function](http://nbviewer.ipython.org/github/demotu/BMC/blob/master/notebooks/DetectPeaks.ipynb) from Marcos Duarte.
* Use the [indexes function](http://pythonhosted.org/PeakUtils/reference.html#peakutils.peak.indexes) from [the PeakUtils package](https://bitbucket.org/lucashnegri/peakutils)
* Use the [peakdetect function](https://gist.github.com/sixtenbe/1178136) that sixtenbe writted on the base of [the endolith translation](https://gist.github.com/endolith/250860) of [a MatLab script from Eli Billauer](http://billauer.co.il/peakdet.html)
* Use the Octave [findpeaks](http://octave.sourceforge.net/signal/function/findpeaks.html) (from the Octave-Forge signal package) through [the oct2py module](https://github.com/blink1073/oct2py)

From theses options, the ones from Marcos Duarte and the PeakUtils are the easier and simpler to use if you come from the MatLab world and/or search a direct equivalent of [the MatLab findpeaks function](http://fr.mathworks.com/help/signal/ref/findpeaks.html).

For the usage of theses functions, please checkout [the tests](https://github.com/MonsieurV/py-findpeaks/tree/master/tests).

If you've have found something else or want to improve this overview, [let me know](mailto:yoan@ytotech.com) or [open a new ticket](https://github.com/MonsieurV/py-findpeaks/issues/new). I will happily receive any contribution.

Hoping this help someone, happy processing!