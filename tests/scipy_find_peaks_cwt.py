#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from vector import vector, plot_peaks
import scipy.signal

print('Detect peaks without any filters.')
indexes = scipy.signal.find_peaks_cwt(
    vector,
    np.arange(1, 4),
    max_distances=np.arange(1, 4)*2
)
indexes = np.array(indexes) - 1
print('Peaks are: %s' % (indexes))
plot_peaks(
    np.array(vector),
    np.array(indexes),
    algorithm='scipy.signal.find_peaks_cwt'
)
