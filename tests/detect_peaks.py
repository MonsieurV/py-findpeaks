#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from vector import vector, plot_peaks
from libs import detect_peaks

print('Detect peaks without any filters.')
indices = detect_peaks.detect_peaks(vector)
print('Peaks are: %s' % (indices))
plot_peaks(np.array(vector), indices,
    algorithm='detect_peaks from Marcos Duarte')

print('Detect peaks with minimum height and distance filters.')
indices = detect_peaks.detect_peaks(vector, mph=7, mpd=2)
print('Peaks are: %s' % (indices))
plot_peaks(np.array(vector), indices, mph=7, mpd=2,
    algorithm='detect_peaks from Marcos Duarte')
