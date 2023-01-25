import numpy as np
import matplotlib.pyplot as plt


def line_plot(x: np.ndarray, y: np.ndarray, x_label: str = "", y_label: str = "", title: str = ""):
    _, ax = plt.subplots()

    ax.plot(x, y, lw=2, color='#539caf', alpha=1)

    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)


def histogram(x, n_bins, cumulative=False, x_label="", title=""):
    _, ax = plt.subplots()
    ax.hist(x, n_bins, cumulative=cumulative, color='#539caf')
    ax.set_xlabel(x_label)
    ax.set_title(title)