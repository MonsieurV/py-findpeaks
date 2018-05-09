#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from vector import vector, plot_peaks
import scipy.signal

print('Detect peaks without any filters.')
indexes, _ = scipy.signal.find_peaks(np.array(vector))
print('Peaks are: {}'.format(indexes))
plot_peaks(
    np.array(vector),
    indexes,
    algorithm='scipy.signal.find_peaks'
)

print('Detect peaks with minimum height and distance filters.')
indexes, _ = scipy.signal.find_peaks(
    np.array(vector),
    height=7, distance=2
)
print('Peaks are: {}'.format(indexes))
plot_peaks(
    np.array(vector),
    indexes,
    mph=7, mpd=2, algorithm='scipy.signal.find_peaks'
)
