#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
To install the mlpy, you may read (and run) /tests/install_mlpy.sh
"""
import numpy as np
from vector import vector, plot_peaks
import mlpy

span = 3
print('Detect peaks with a sliding window of {} (minimum possible).'.format(span))
indexes = mlpy.findpeaks_win(vector, span=span)
print('Peaks are: {}'.format(indexes))
plot_peaks(
    np.array(vector),
    indexes,
    mpd=span, algorithm='mlpy.findpeaks_win'
)

span = 5
print('Detect peaks with a sliding window of {}.'.format(span))
indexes = mlpy.findpeaks_win(vector, span=span)
print('Peaks are: {}'.format(indexes))
plot_peaks(
    np.array(vector),
    indexes,
    mpd=span, algorithm='mlpy.findpeaks_win'
)
