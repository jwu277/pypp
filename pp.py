import numpy as np
import matplotlib.pyplot as plt


EPSILON = 0.00001


def phase_portrait(xv, yv, dxf, dyf):

    x, y = np.meshgrid(xv, yv)

    dx = list(map(dxf, x))
    dy = list(map(dyf, y))

    return phase_portrait_raw(x, y, dx, dy)


def phase_portrait_raw(x, y, dx, dy, normalize=False):
    
    fig, ax = plt.subplots()

    if normalize:
        r = np.sqrt(np.square(dx) + np.square(dy)) + EPSILON
        dx = dx / r
        dy = dy / r

    ax.quiver(x, y, dx, dy)

    return fig, ax

