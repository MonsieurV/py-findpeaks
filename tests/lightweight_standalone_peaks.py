__author__ = 'Tony Beltramelli - 07/11/2015'

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# only dependencies required
import numpy as np
from math import sqrt

# threshold used to discard peaks too small
def detect_peaks(signal, threshold=0.5):
	# compute root mean square
	root_mean_square = sqrt(np.sum(np.square(signal) / len(signal)))

	# compute peak to average ratios
	ratios = np.array([pow(x / root_mean_square, 2) for x in signal])

	# apply first order logic
	peaks = (ratios > np.roll(ratios, 1)) & (ratios > np.roll(ratios, -1)) & (ratios > threshold)

	# optional: return peak indices
	peak_indexes = []
	
	for i in range(0, len(peaks)):
		if peaks[i]:
			peak_indexes.append(i)

	return peak_indexes

# example
from vector import vector, plot_peaks

indexes = detect_peaks(vector, 1.5)
print indexes
plot_peaks(np.array(vector), np.array(indexes), mph=1.5, algorithm='lightweight standalone peaks')