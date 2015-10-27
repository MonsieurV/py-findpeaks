#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from vector import vector, plot_peaks
import scipy.signal

indices = scipy.signal.find_peaks_cwt(vector, np.arange(1, 2))
print('Peaks are: %s' % (indices))
plot_peaks(np.array(vector), np.array(indices),
    algorithm='scipy.signal.find_peaks_cwt')
