""" Searches for peaks in data
    History:
         -nov 2015: Janko Slavic, update
         -mar 2013: janko.slavic@fs.uni-lj.si
"""

import numpy as np

def findpeaks(data, spacing=10, limit=None):
    """Finds peaks in `data` which are of `spacing` width and >=`limit`.
    :param data: values
    :param spacing: minimum width for single peak
    :param limit: peaks should have value greater or equal
    :return:
    """
    x = np.zeros(len(data)+2*spacing)
    x[:spacing] = data[0]
    x[-spacing:] = data[-1]
    x[spacing:-spacing] = data
    peak_candidate = np.zeros(x.size - 2*spacing - 2)
    peak_candidate[:] = True
    for s in range(spacing):
        h_b = x[s:-2 * spacing + s - 2]  # before
        h_c = x[spacing: -spacing - 2]  # central
        h_a = x[spacing + s + 1: -spacing + s - 1]  # after
        peak_candidate = np.logical_and(peak_candidate, np.logical_and(h_c > h_b, h_c > h_a))

    ind = np.argwhere(peak_candidate)
    ind = ind.reshape(ind.size)
    if limit is not None:
        ind = ind[data[ind] > limit]
    return ind


if __name__ == '__main__':
    import matplotlib.pyplot as plt

    n = 1000
    m = 20
    t = np.linspace(0., 1, n)
    x = np.zeros(n)
    np.random.seed(0)
    phase = 2 * np.pi * np.random.random(m)
    for i in range(m):
        x += np.sin(phase[i] + 2 * np.pi * t * i)

    peaks = findpeaks(x, spacing=100, limit=4.)
    plt.plot(t, x)
    plt.axhline(4, color='r')
    plt.plot(t[peaks], x[peaks], 'ro')
    plt.title('Peaks: minimum value 4., minimum width 100 points')
    plt.show()
