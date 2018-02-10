#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from vector import vector, plot_peaks
import scipy.signal

print('Detect peaks without any filters (maxima).')
indexes = scipy.signal.argrelextrema(
    np.array(vector),
    comparator=np.greater
)
print('Peaks are: %s' % (indexes[0]))
plot_peaks(
    np.array(vector),
    indexes[0],
    algorithm='scipy.signal.argrelmax'
)

print('Detect peaks without any filters (minima).')
indexes = scipy.signal.argrelextrema(
    np.array(vector),
    comparator=np.less
)
print('Peaks are: %s' % (indexes[0]))
plot_peaks(
    np.array(vector),
    indexes[0],
    algorithm='scipy.signal.argrelmax'
)

print('Detect peaks with order (distance) filter.')
indexes = scipy.signal.argrelextrema(
    np.array(vector),
    comparator=np.greater,
    order=2
)
print('Peaks are: %s' % (indexes[0]))
plot_peaks(
    np.array(vector),
    indexes[0],
    mpd=2, algorithm='scipy.signal.argrelmax'
)
