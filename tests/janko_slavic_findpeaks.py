#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from vector import vector, plot_peaks
from libs.findpeaks import findpeaks

print('Detect peaks without any filters.')
indexes = findpeaks(np.array(vector), spacing=1)
print('Peaks are: %s' % (indexes))
plot_peaks(
    np.array(vector),
    np.array(indexes),
    algorithm='findpeaks from Janko Slavic'
)

print('Detect peaks with distance and height filters.')
indexes = findpeaks(np.array(vector), spacing=2, limit=7)
print('Peaks are: %s' % (indexes))
plot_peaks(
    np.array(vector),
    np.array(indexes), mph=7, mpd=2,
    algorithm='findpeaks from Janko Slavic'
)
