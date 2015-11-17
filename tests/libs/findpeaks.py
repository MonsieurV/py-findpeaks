""" Searches for peaks in data
    History:
         -nov 2015: Janko Slavic, update
         -mar 2013: janko.slavic@fs.uni-lj.si
"""

import numpy as np


def findpeaks(data, spacing=1, limit=None):
    """Finds peaks in `data` which are of `spacing` width and >=`limit`.
    :param data: values
    :param spacing: minimum spacing to the next peak (should be 1 or more)
    :param limit: peaks should have value greater or equal
    :return:
    """
    len = data.size
    x = np.zeros(len+2*spacing)
    x[:spacing] = data[0]-1.e-6
    x[-spacing:] = data[-1]-1.e-6
    x[spacing:spacing+len] = data
    peak_candidate = np.zeros(len)
    peak_candidate[:] = True
    for s in range(spacing):
        start = spacing - s - 1
        h_b = x[start : start + len]  # before
        start = spacing
        h_c = x[start : start + len]  # central
        start = spacing + s + 1
        h_a = x[start : start + len]  # after
        peak_candidate = np.logical_and(peak_candidate, np.logical_and(h_c > h_b, h_c > h_a))

    ind = np.argwhere(peak_candidate)
    ind = ind.reshape(ind.size)
    if limit is not None:
        ind = ind[data[ind] > limit]
    return ind


if __name__ == '__main__':
    import matplotlib.pyplot as plt

    n = 80
    m = 20
    limit = 0
    spacing = 3
    t = np.linspace(0., 1, n)
    x = np.zeros(n)
    np.random.seed(0)
    phase = 2 * np.pi * np.random.random(m)
    for i in range(m):
        x += np.sin(phase[i] + 2 * np.pi * t * i)

    peaks = findpeaks(x, spacing=spacing, limit=limit)
    plt.plot(t, x)
    plt.axhline(limit, color='r')
    plt.plot(t[peaks], x[peaks], 'ro')
    plt.title('Peaks: minimum value {limit}, minimum spacing {spacing} points'.format(**{'limit': limit, 'spacing': spacing}))
    plt.show()
