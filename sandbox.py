import numpy as np
from pp import phase_portrait_raw
import matplotlib.pyplot as plt


def main():

    alpha = -1.0
    omega = 1.0
    l1 = 3.0
    m1 = 1.0
    l2 = -1.0
    m2 = 1.0

    xv = np.arange(-2, 2, 0.2)
    yv = np.arange(-2, 2, 0.2)

    x, y = np.meshgrid(xv, yv)

    r2 = np.square(x) + np.square(y)
    r4 = np.square(r2)

    dx = (alpha * x - omega * y) + (l1 * x - m1 * y) * r2 +  + (l2 * x - m2 * y) * r4
    dy = (omega * x + alpha * y) + (m1 * x + l1 * y) * r2 +  + (m2 * x + l2 * y) * r4

    phase_portrait_raw(x, y, dx, dy, normalize=True)
    plt.show()


if __name__ == "__main__":
    main()

