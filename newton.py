import matplotlib.pyplot as plt
import math
import cmath
import numpy as np
import numpy.polynomial.polynomial as poly


def find_convergence(c, dc, z, roots):
    "Compute the index of the root toward which the Newton method is converging starting at z"
    z_n = z
    for i in range(100):
        z_n = z_n - poly.polyval(z_n, c) / poly.polyval(z_n, dc)
    distances = [abs(r - z_n) for r in roots]
    return np.argmin(distances)


def compute_convergence_matrix(c, boundaries, shape):
    x_min, x_max = boundaries[0]
    y_min, y_max = boundaries[1]
    height, width = shape
    conv_mat = np.zeros(shape=(height, width))
    roots = poly.polyroots(c)
    dc = poly.polyder(c)
    for row in range(height):
        y = row * (y_max -  y_min) / height + y_min
        for col in range(width):
            x = col * (x_max -  x_min) / width + x_min
            z_n = complex(x, y)
            conv_val = find_convergence(c, dc, z_n, roots)
            conv_mat[row, col] = conv_val
    return conv_mat


c = [-1, 0 ,0 ,0, 0, 0, 1]
shape = (301, 301)
boundaries = [(-5, 5), (-5, 5)]

conv_mat = compute_convergence_matrix(c, boundaries, shape)

plt.imshow(conv_mat)
plt.show()

