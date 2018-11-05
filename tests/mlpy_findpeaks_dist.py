#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
To install the mlpy, you may read (and run) /tests/install_mlpy.sh
"""
import numpy as np
from vector import vector, plot_peaks
import mlpy

print('Detect peaks without any filters.')
indexes = mlpy.findpeaks_dist(vector)
print('Peaks are: {}'.format(indexes))
plot_peaks(
    np.array(vector),
    indexes,
    algorithm='mlpy.findpeaks_dist'
)

print('Detect peaks with minimum distance filter.')
mdp = 2.1
indexes = mlpy.findpeaks_dist(vector, mindist=mdp)
print('Peaks are: {}'.format(indexes))
plot_peaks(
    np.array(vector),
    indexes,
    mpd=mdp, algorithm='mlpy.findpeaks_dist'
)
