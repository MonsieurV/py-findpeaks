#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from vector import vector, plot_peaks
from oct2py import octave

# Load the Octage-Forge signal package.
octave.eval("pkg load signal")

print('Detect peaks without any filters.')
(_, indexes) = octave.findpeaks(
    np.array(vector),
    'DoubleSided', 'MinPeakHeight', 0, 'MinPeakDistance', 0, 'MinPeakWidth', 0
)
# The results are in a 2D array and in floats: get back to 1D array and convert
# peak indexes to integer. Also this is MatLab-style indexation (one-based),
# so we must substract one to get back to Python indexation (zero-based).
indexes = indexes[0].astype(int) - 1
print('Peaks are: %s' % (indexes))
plot_peaks(
    np.array(vector),
    indexes,
    algorithm='Octave-Forge findpeaks'
)

print('Detect peaks with minimum height and distance filters.')
(pks, indexes) = octave.findpeaks(
    np.array(vector),
    'DoubleSided', 'MinPeakHeight', 6, 'MinPeakDistance', 2, 'MinPeakWidth', 0
)
# The results are in a 2D array and in floats: get back to 1D array and convert
# peak indexes to integer. Also this is MatLab-style indexation (one-based),
# so we must substract one to get back to Python indexation (zero-based).
indexes = indexes[0].astype(int) - 1
print('Peaks are: %s' % (indexes))
plot_peaks(
    np.array(vector),
    indexes,
    mph=6, mpd=2, algorithm='Octave-Forge findpeaks'
)
