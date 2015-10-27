#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from vector import vector, plot_peaks
from libs import detect_peaks

# loc = detect_peaks(vector, mph=22)
# loc = detect_peaks(vector, mph=22, mpd=None)
# loc = detect_peaks(vector, mph=0.05, mpd=10)

indices = detect_peaks.detect_peaks(vector)
print('Peaks are: %s' % (indices))
plot_peaks(np.array(vector), np.array(indices))
