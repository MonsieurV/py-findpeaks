#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from vector import vector, plot_peaks
import peakutils.peak

print('Detect peaks without any filters.')
indexes = peakutils.peak.indexes(np.array(vector), thres=0, min_dist=0)
print('Peaks are: %s' % (indexes))
plot_peaks(
    np.array(vector),
    indexes,
    algorithm='peakutils.peak.indexes'
)

print('Detect peaks with minimum height and distance filters.')
indexes = peakutils.peak.indexes(
    np.array(vector),
    thres=7.0/max(vector), min_dist=2
)
print('Peaks are: %s' % (indexes))
plot_peaks(
    np.array(vector),
    indexes,
    mph=7, mpd=2, algorithm='peakutils.peak.indexes'
)
