This is an overview of all the ready-to-use algorithms I've found to perform peak detection in Python. I've also written [a blog post](https://blog.ytotech.com/2015/11/01/findpeaks-in-python/) on the subject.

## Overview

| Algorithm | Integration | Filters | MatLab `findpeaks`-like? |
|-----------| ----------- | ------- | :----------------------: |
| [scipy.signal.find_peaks_cwt](#scipysignalfind_peaks_cwt) | Included in Scipy | ? | ✘ |
| [scipy.signal.argrelextrema](#scipysignalargrelextrema) | Included in Scipy 0.11+ | Minimum distance | ✘ |
| [scipy.signal.find_peaks](#scipysignalfind_peaks) | Included in Scipy 1.1+ | Amplitude<br>Threshold<br>Distance<br>Prominence<br>Width | ✔ |
| [detect_peaks](#detect_peaks-from-marcos-duarte) | Single file source<br>Depends on Numpy | Minimum distance<br>Minimum height<br>Relative threshold | ✔ |
| [peakutils.peak.indexes](#peakutilspeakindexes) | PyPI package PeakUtils<br> Depends on Scipy | Amplitude threshold<br>Minimum distance | ✔ |
| [peakdetect](#peakdetect-from-sixtenbe) | Single file source<br>Depends on Scipy | Minimum distance | ✘ |
| [Octave-Forge findpeaks](#octave-forge-findpeaks) | Requires an Octave-Forge distribution<br>+ PyPI package oct2py<br>Depends on Scipy | Minimum distance<br>Minimum height<br>Minimum peak width | ✘ |
| [Janko Slavic findpeaks](#janko-slavic-findpeaks) | Single function<br>Depends on Numpy | Minimum distance<br>Minimum height | ✘ |
| [Tony Beltramelli detect_peaks](#tony-beltramelli-detect_peaks) | Single function<br>Depends on Numpy | Amplitude threshold | ✘ |

## How to make your choice?

When you're selecting an algorithm, you might consider:

* **The function interface.** You may want the function to work natively with Numpy arrays or may search something similar to other platform algorithms, like the MatLab [`findpeaks`](http://fr.mathworks.com/help/signal/ref/findpeaks.html).
* **The dependencies.** Does it require extra dependency? Does is it easy to make it run on a fresh box?
* **The filtering support**. Does the algorithm allows to define multiple filters? Which ones do you need?

--------------------------------

## scipy.signal.find_peaks_cwt

![](/images/scipy_find_peaks_cwt.png?raw=true "scipy.signal.find_peaks_cwt")

```python
import numpy as np
vector = [
    0, 6, 25, 20, 15, 8, 15, 6, 0, 6, 0, -5, -15, -3, 4, 10, 8, 13, 8, 10, 3,
    1, 20, 7, 3, 0 ]
import scipy.signal
print('Detect peaks without any filters.')
indexes = scipy.signal.find_peaks_cwt(vector, np.arange(1, 4),
    max_distances=np.arange(1, 4)*2)
indexes = np.array(indexes) - 1
print('Peaks are: %s' % (indexes))
```

[Documentation](http://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.find_peaks_cwt.html).
[Sample code](/tests/scipy_find_peaks_cwt.py).

The first historical peak detection algorithm from the Scipy signal processing package.
Its name appears to make it an obvious choice (when you already work with Scipy), but it may actually not be, as it uses a wavelet convolution approach.

This function requires to understand wavelets to be properly used. This is less trivial and direct than other algorithms. However the wavelet approach can make it a good choice on noisy data.

## scipy.signal.argrelextrema

![](/images/scipy_argrelextrema.png?raw=true "scipy.signal.argrelextrema")

```python
import numpy as np
vector = [
    0, 6, 25, 20, 15, 8, 15, 6, 0, 6, 0, -5, -15, -3, 4, 10, 8, 13, 8, 10, 3,
    1, 20, 7, 3, 0 ]
import scipy.signal
print('Detect peaks with order (distance) filter.')
indexes = scipy.signal.argrelextrema(
    np.array(vector),
    comparator=np.greater,order=2
)
print('Peaks are: %s' % (indexes[0]))
```

[Documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.argrelextrema.html).
[Sample code](/tests/scipy_argrelextrema.py).

New peak detection algorithm from Scipy since version 0.11.0. Its usage is really trivial,
but it misses out of the box filtering capacities.

It includes an `order` parameter that can serve as a kind of minimum distance filter.
The filtering behavior is customizable through the `comparator` parameter, which
can make it a good choice for building your own filtering algorithm over it.

See also related functions [argrelmin](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.argrelmin.html) and [argrelmax](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.argrelmax.html).


## scipy.signal.find_peaks

![](/images/scipy_find_peaks.png?raw=true "scipy.signal.find_peaks")

```python
import numpy as np
import scipy.signal
vector = np.array([0, 6, 25, 20, 15, 8, 15, 6, 0, 6, 0, -5, -15, -3, 4, 10, 8,
                   13, 8, 10, 3, 1, 20, 7, 3, 0])
print('Detect peaks with minimum height and distance filters.')
indexes, _ = scipy.signal.find_peaks(vector, height=7, distance=2.1)
print('Peaks are: %s' % (indexes))
```

[Documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.find_peaks.html).
[Sample code](/tests/scipy_signal_find_peaks.py).

This function was added to SciPy in version 1.1.0 and is comparable to `findpeaks` provided in Matlab's Signal Processing Toolbox.

`scipy.signal.find_peaks` searches for peaks (local maxima) based on simple value comparison of neighbouring samples and returns those peaks whose properties match optionally specified conditions (minimum and / or maximum) for their height, prominence, width, threshold and distance to each other.


## detect_peaks from Marcos Duarte

![](/images/detect_peaks.png?raw=true "detect_peaks from Marcos Duarte")

```python
import numpy as np
vector = [
    0, 6, 25, 20, 15, 8, 15, 6, 0, 6, 0, -5, -15, -3, 4, 10, 8, 13, 8, 10, 3,
    1, 20, 7, 3, 0 ]
from libs import detect_peaks
print('Detect peaks with minimum height and distance filters.')
indexes = detect_peaks.detect_peaks(vector, mph=7, mpd=2)
print('Peaks are: %s' % (indexes))
```

[Documentation](http://nbviewer.ipython.org/github/demotu/BMC/blob/master/notebooks/DetectPeaks.ipynb).
[Source](/tests/libs/detect_peaks.py).
[Sample code](/tests/detect_peaks.py).

This algorithm comes from a notebook written by Marcos Duarte and is pretty trivial to use.

The function has an interface very similar and consistent results with the MatLab Signal Processing Toolbox `findpeaks`, yet with less complete filtering and tuning support.

## peakutils.peak.indexes

![](/images/peakutils_indexes.png?raw=true "peakutils.peak.indexes")

```python
import numpy as np
vector = [
    0, 6, 25, 20, 15, 8, 15, 6, 0, 6, 0, -5, -15, -3, 4, 10, 8, 13, 8, 10, 3,
    1, 20, 7, 3, 0 ]
import peakutils.peak
print('Detect peaks with minimum height and distance filters.')
indexes = peakutils.peak.indexes(np.array(vector),
    thres=7.0/max(vector), min_dist=2)
print('Peaks are: %s' % (indexes))
```

[Documentation](http://pythonhosted.org/PeakUtils/reference.html#peakutils.peak.indexes).
[Package](https://bitbucket.org/lucashnegri/peakutils).
[Sample code](/tests/peakutils_indexes.py).

This algorithm can be used as an equivalent of the MatLab `findpeaks` and will give easily give consistent results if you only need minimal distance and height filtering.

## peakdetect from sixtenbe

![](/images/sixtenbe_peakdetect.png?raw=true "peakdetect from sixtenbe")

```python
import numpy as np
vector = [
    0, 6, 25, 20, 15, 8, 15, 6, 0, 6, 0, -5, -15, -3, 4, 10, 8, 13, 8, 10, 3,
    1, 20, 7, 3, 0 ]
from libs import peakdetect
print('Detect peaks with distance filters.')
peaks = peakdetect.peakdetect(np.array(vector), lookahead=2, delta=2)
# peakdetect returns two lists, respectively positive and negative peaks,
# with for each peak a tuple of (indexes, values).
indexes = []
for posOrNegPeaks in peaks:
    for peak in posOrNegPeaks:
        indexes.append(peak[0])
print('Peaks are: %s' % (indexes))
```

[Source and documentation](https://gist.github.com/sixtenbe/1178136).
[Sample code](/tests/peakdetect.py).

The algorithm was written by sixtenbe based on the previous work of [endolith](https://gist.github.com/endolith/250860) and [Eli Billauer](http://billauer.co.il/peakdet.html).

Easy to setup as it comes in a single source file, but the lookahead parameter make it hard to use on low-sampled signals or short samples. May miss filtering capacities (only minimum peak distance with the delta parameter).

## Octave-Forge findpeaks

![](/images/octave_findpeaks.png?raw=true "Octave-Forge findpeaks")

```python
import numpy as np
vector = [
    0, 6, 25, 20, 15, 8, 15, 6, 0, 6, 0, -5, -15, -3, 4, 10, 8, 13, 8, 10, 3,
    1, 20, 7, 3, 0 ]
from oct2py import octave
# Load the Octage-Forge signal package.
octave.eval("pkg load signal")
print('Detect peaks with minimum height and distance filters.')
(pks, indexes) = octave.findpeaks(np.array(vector), 'DoubleSided',
    'MinPeakHeight', 6, 'MinPeakDistance', 2, 'MinPeakWidth', 0)
# The results are in a 2D array and in floats: get back to 1D array and convert
# peak indexes to integer. Also this is MatLab-style indexation (one-based),
# so we must substract one to get back to Python indexation (zero-based).
indexes = indexes[0].astype(int) - 1
print('Peaks are: %s' % (indexes))
```

[Documentation](http://octave.sourceforge.net/signal/function/findpeaks.html).
[oct2py package](https://github.com/blink1073/oct2py).
[Sample code](/tests/octave_findpeaks.py).

Use `findpeaks` from the Octave-Forge signal package through the oct2py bridge. This algorithm allows to make a double sided detection, which means it will detect both local maxima and minima in a single run.

Requires a rather complicated and not very efficient setup to be called from Python code. Of course, you will need an up-to-date distribution of Octave, with the signal package installed from Octave-Forge.

Although the function have an interface close to the MatLab `findpeaks`, it is harder to have the exact same results that with [detect_peaks](#detect_peaks-from-marcos-duarte) or [peakutils.peak.indexes](#peakutilspeakindexes).

## Janko Slavic findpeaks

![](/images/janko_slavic_findpeaks.png?raw=true "Janko Slavic findpeaks")

```python
import numpy as np
vector = [
    0, 6, 25, 20, 15, 8, 15, 6, 0, 6, 0, -5, -15, -3, 4, 10, 8, 13, 8, 10, 3,
    1, 20, 7, 3, 0 ]
from libs.findpeaks import findpeaks
indexes = findpeaks(np.array(vector), spacing=, limit=7)
print('Peaks are: %s' % (indexes))
```

[Documentation](https://github.com/jankoslavic/py-tools/blob/master/findpeaks/Findpeaks%20example.ipynb).
[Source](https://github.com/jankoslavic/py-tools/blob/master/findpeaks/findpeaks.py).
[Sample code](/tests/janko_slavic_findpeaks.py).

Small and fast peak detection algorithm, with minimum distance and height filtering support. Comes as an handy single function, depending only on Numpy.

Contrary to the MatLab `findpeaks`-like distance filters, the Janko Slavic `findpeaks` `spacing` param requires that all points within the specified width to be lower than the peak. If you work on very low sampled signal, the minimum distance filter may miss fine granularity tuning.

## Tony Beltramelli detect_peaks

![](/images/tony_beltramelli_detect_peaks.png?raw=true "Lightweight standalone peaks")

```python
import numpy as np
vector = [
    0, 6, 25, 20, 15, 8, 15, 6, 0, 6, 0, -5, -15, -3, 4, 10, 8, 13, 8, 10, 3,
    1, 20, 7, 3, 0 ]
from libs.tony_beltramelli_detect_peaks import detect_peaks
print('Detect peaks with height threshold.')
indexes = detect_peaks(vector, 1.5)
print('Peaks are: %s' % (indexes))
```

[Source and documentation](/tests/libs/tony_beltramelli_detect_peaks.py).
[Sample code](/tests/tony_beltramelli_detect_peaks.py).

Straightforward, simple and lightweight peak detection algorithm, with minimum distance filtering support.

No minimum peak height filtering support.

----------------------------------

# How to find both lows and highs?

Most algorithms detect only local _maximas_. You may want to detect both _minimas_ and _maximas_.

One solution is to invert the signal before feeding it to the algorithm for detecting lows, as suggested by [@raoofhujairi](https://github.com/MonsieurV/py-findpeaks/issues/3).

With two runs, you can then get both lows and highs:

![](/images/highs_and_lows_peakutils_indexes.png?raw=true "High and low peaks with PeakUtils Indexes")

See the related [sample code](/tests/lows_and_highs.py) using PeakUtils.

----------------------------------

# How to run the examples?

## Install Numpy, Scipy and Matplotlib

You need to have Numpy, Scipy and Matplotlib installed - possibly the latest versions.

To install - and update - them for Python 3:

```sh
pip3 install -U numpy scipy matplotlib
```

(you may need to run the command using `sudo` for a system-wide install)

## Install test sample dependencies

Some examples rely on other packages - like [PeakUtils](https://pypi.python.org/pypi/PeakUtils).
Install them using Pipenv to run all sample codes:

```sh
# Go in tests directory.
cd tests/
# Install dependencies in a virtualenv using Pipenv.
# We install also Matplotlib so we can access it in the virtualenv.
# If you do not want that, you can do a system-wide install using:
# pip install -r requirements.txt
pipenv install
```

## Run an example

You can them run any example to see the results.

For e.g. for testing PeakUtils:

```sh
pipenv run python3 peakutils_indexes.py
```

# Contribute

Feel free to [open a new ticket](https://github.com/MonsieurV/py-findpeaks/issues/new) or submit a PR to improve this overview.

Happy processing!
