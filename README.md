This is an overview of all the ready-to-use algorithms I've found to perform peak detection in Python.

## Overview

| Algorithm | Depends on | Filters | Double sided? | MatLab `findpeaks`-like? |
|-----------| ---------- | ------- | ------------- | ------------------------ |
| [scipy.signal.find_peaks_cwt](#scipysignalfind_peaks_cwt) | Scipy | Max distance | ✘ | ✘ |
| [detect_peaks](#detect_peaks-from-marcos-duarte) | Numpy | Minimum distance<br>Minimum height | ✘ | ✔ |
| [peakutils.indexes](#peakutilsindexes) | PeakUtils and Scipy | ? | ? | ✘ |
| [peakdetect](#peakdetect-from-sixtenbe) | Scipy | ? | ? | ✘ |
| [Octave-Forge findpeaks](#octave-forge-findpeaks) | Octave-Forge, oct2py and Scipy | ? | ? | ✘ |

## How to make your choice?

When you're selecting an algorithm, you might consider:

* **The function interface.** You may want the function to work natively with Numpy arrays or may search something similar to other platform algorithms, like the MatLab [`findpeaks`](http://fr.mathworks.com/help/signal/ref/findpeaks.html).
* **The dependencies.** Does it require extra dependency? Does is it easy to make it run on a fresh box?
* **The filtering support**. Does the algorithm allows to define multiple filters? Which ones do you need?

--------------------------------

## scipy.signal.find_peaks_cwt

[Documentation](http://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.find_peaks_cwt.html).

The peak detection algorithm from the Scipy signal processing package. It appears like the obvious choice when you already work with Scipy.

However this algorithm requires to understand wavelets to be well used, as its interface is constructed after the wavelet convolution approach. Its use may be thus judged as less trivial and direct than other algorithms.

## detect_peaks from Marcos Duarte

![](/images/detect_peaks.png?raw=true "detect_peaks from Marcos Duarte")

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

![](/images/octave_findpeaks.png?raw=true "Octave-Forge findpeaks")

```python
import numpy as np
from vector import vector, plot_peaks
from oct2py import octave
# Load the Octage-Forge signal package.
octave.eval("pkg load signal")
print('Detect peaks without any filters.')
(_, indices) = octave.findpeaks(np.array(vector), 'DoubleSided',
    'MinPeakHeight', 0, 'MinPeakDistance', 0, 'MinPeakWidth', 0)
# The results are in a 2D array and in floats: get back to 1D array and convert
# peak indices to integer. Also this is MatLab-style indexation (one-based),
# so we must substract one to get back to Python indexation (zero-based).
indices = indices[0].astype(int) - 1
print('Peaks are: %s' % (indices))
```

[Documentation](http://octave.sourceforge.net/signal/function/findpeaks.html).
[oct2py package](https://github.com/blink1073/oct2py).

Use `findpeaks` from the Octave-Forge signal package through the oct2py bridge. This algorithm allows to make a double sided detection, which means it will detect both local maximam and minima in a single run.

Requires a rather complicated and not very efficient setup to be called from Python code. Of course, you will need an up-to-date distribution of Octave, with the signal package installed from Octave-Forge.

----------------------------------

# Contribute

If you've have found something else or want to improve this overview, feel free to [open a new ticket](https://github.com/MonsieurV/py-findpeaks/issues/new) or submit a PR.

This has helped you? [Let me know!](mailto:yoan@ytotech.com)

Happy digital processing!
