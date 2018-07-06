import math
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import math

def compute_regular_polygon(n, size):
    "Compute a regular polygon of the given shape"
    poly = []
    for k in range(n):
        x = math.sqrt(size) * math.cos(2 * k * math.pi / n)
        y = math.sqrt(size) * math.sin(2 * k * math.pi / n)
        P = [x, y]
        poly += [P]
    return np.array(poly)

def draw_shapes(shapes):
    "Draw the given shape"
    for shape in shapes:
        x = [c[0] for c in shape] + [shape[0][0]]
        y = [c[1] for c in shape] + [shape[0][1]]
        plt.plot(x, y)
        plt.axes().set_aspect('equal', 'datalim')
    plt.show()
