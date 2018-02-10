#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from vector import vector, plot_peaks
from libs.tony_beltramelli_detect_peaks import detect_peaks

print('Detect peaks without any filters.')
indexes = detect_peaks(vector)
print('Peaks are: %s' % (indexes))
plot_peaks(
    np.array(vector),
    np.array(indexes),
    algorithm='detect_peaks from Tony Beltramelli'
)

print('Detect peaks with height threshold.')
indexes = detect_peaks(vector, 1.5)
print('Peaks are: %s' % (indexes))
plot_peaks(
    np.array(vector),
    np.array(indexes), mph=1.5,
    algorithm='detect_peaks from Tony Beltramelli'
)
