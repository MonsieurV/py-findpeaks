#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from vector import cb, plot_peaks
import peakutils.peak

def plot_peaks_lows_highs(x, highs, lows, algorithm=None, mph=None, mpd=None):
    """Plot results of the peak dectection."""
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print('matplotlib is not available.')
        return
    _, ax = plt.subplots(1, 1, figsize=(8, 4))
    ax.plot(x, 'b', lw=1)
    if highs.size:
        label = 'high peak'
        label = label + 's' if highs.size > 1 else label
        ax.plot(highs, x[highs], '+', mfc=None, mec='r', mew=2, ms=8,
                label='%d %s' % (highs.size, label))
        ax.legend(loc='best', framealpha=.5, numpoints=1)
    if lows.size:
        label = 'low peak'
        label = label + 's' if lows.size > 1 else label
        ax.plot(lows, x[lows], '+', mfc=None, mec='g', mew=2, ms=8,
                label='%d %s' % (lows.size, label))
        ax.legend(loc='best', framealpha=.5, numpoints=1)
    ax.set_xlim(-.02*x.size, x.size*1.02-1)
    ymin, ymax = x[np.isfinite(x)].min(), x[np.isfinite(x)].max()
    yrange = ymax - ymin if ymax > ymin else 1
    ax.set_ylim(ymin - 0.1*yrange, ymax + 0.1*yrange)
    ax.set_xlabel('Data #', fontsize=14)
    ax.set_ylabel('Amplitude', fontsize=14)
    ax.set_title('%s (mph=%s, mpd=%s)' % (algorithm, mph, mpd))
    plt.show()

threshold = 0.02
min_dist = 150

print('Detect high peaks with minimum height and distance filters.')
highs = peakutils.peak.indexes(
    np.array(cb),
    thres=threshold/max(cb), min_dist=min_dist
)
print('High peaks are: %s' % (highs))

print('Detect low peaks with minimum height and distance filters.')
# Invert the signal.
cbInverted = cb * -1
lows = peakutils.peak.indexes(
    np.array(cbInverted),
    thres=threshold/max(cbInverted), min_dist=min_dist
)
print('Low peaks are: %s' % (lows))

plot_peaks_lows_highs(
    np.array(cb),
    highs,
    lows,
    mph=threshold, mpd=min_dist, algorithm='peakutils.peak.indexes'
)
