#!/usr/bin/env python
# -*- coding: utf-8 -*-
import scipy.signal
import numpy as np
from vector import vector

print(scipy.signal.find_peaks_cwt(vector, np.arange(1, 10)))
