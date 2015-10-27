import numpy as np

vector = [
    0, 6, 25, 20, 15, 8, 15, 6, 0, -5, -15, -3, 4, 10, 8, 13, 8, 10, 3, 1, 20,
    7, 3, 0 ]

def plot_peaks(x, indices, mph=None, mpd=None):
    """Plot results of the peak dectection."""
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print('matplotlib is not available.')
        return
    _, ax = plt.subplots(1, 1, figsize=(8, 4))
    ax.plot(x, 'b', lw=1)
    if indices.size:
        label = 'peak'
        label = label + 's' if indices.size > 1 else label
        ax.plot(indices, x[indices], '+', mfc=None, mec='r', mew=2, ms=8,
                label='%d %s' % (indices.size, label))
        ax.legend(loc='best', framealpha=.5, numpoints=1)
    ax.set_xlim(-.02*x.size, x.size*1.02-1)
    ymin, ymax = x[np.isfinite(x)].min(), x[np.isfinite(x)].max()
    yrange = ymax - ymin if ymax > ymin else 1
    ax.set_ylim(ymin - 0.1*yrange, ymax + 0.1*yrange)
    ax.set_xlabel('Data #', fontsize=14)
    ax.set_ylabel('Amplitude', fontsize=14)
    ax.set_title('Peak detection (mph=%s, mpd=%s)'
                 % (mph, mpd))
    # plt.grid()
    plt.show()
