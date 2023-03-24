import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np


# plot decision boundary
def plot_decision_regions(X: np.ndarray,
                          y: np.ndarray,
                          classifier: object,
                          resolution=0.02,
                          test_idx: range = None) -> None:
    # setup marker generator and color map
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])

    # plot the decision surface
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))

    z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    z = z.reshape(xx1.shape)

    plt.contourf(xx1, xx2, z, alpha=0.3, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    # plot class samples
    for idx, clazz in enumerate(np.unique(y)):
        plt.scatter(x=X[y == clazz, 0],
                    y=X[y == clazz, 1],
                    alpha=0.8,
                    c=colors[idx],
                    marker=markers[idx],
                    label=clazz,
                    edgecolor='black')

    # highlight test samples
    if test_idx:
        # plot all samples

        X_test, y_test = X[test_idx, :], y[test_idx]

        plt.scatter(X_test[:, 0], X_test[:, 1],
                    c=None, edgecolor='black', alpha=0.5,
                    linewidth=1, marker='o',
                    s=100, label='test set')