#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from vector import vector, plot_peaks
from libs import peakdetect

print('Detect peaks without any filters.')
peaks = peakdetect.peakdetect(np.array(vector), lookahead=2)
# peakdetect returns two lists, respectively positive and negative peaks,
# with for each peak a tuple of (indexes, values).
indexes = []
for posOrNegPeaks in peaks:
    for peak in posOrNegPeaks:
        indexes.append(peak[0])
print('Peaks are: %s' % (indexes))
plot_peaks(
    np.array(vector),
    np.array(indexes),
    algorithm='peakdetect from sixtenbe'
)

print('Detect peaks with distance filters.')
peaks = peakdetect.peakdetect(np.array(vector), lookahead=2, delta=2)
# peakdetect returns two lists, respectively positive and negative peaks,
# with for each peak a tuple of (indexes, values).
indexes = []
for posOrNegPeaks in peaks:
    for peak in posOrNegPeaks:
        indexes.append(peak[0])
print('Peaks are: %s' % (indexes))
plot_peaks(
    np.array(vector),
    np.array(indexes),
    mph=None, mpd=2, algorithm='peakdetect from sixtenbe'
)
