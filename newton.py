import matplotlib.pyplot as plt
import math
import numpy as np

def p(z):
    "Complex polynom"
    return z**3 - 1

def pp(z):
    "Derivative  of p"
    return 3 * z**2


def find_convergence(z):
    z_n = z
    roots = [1, complex(-1/2, math.sqrt(3)/2), complex(-1/2, -math.sqrt(3)/2)]
    for i in range(100):
        z_n = z_n - p(z_n) / pp(z_n)
    distances = [abs(r - z_n) for r in roots]
    return np.argmin(distances)


x_min, x_max = -5, 5
y_min, y_max = -5, 5
height, width = 1001, 1001
fractal = np.zeros(shape=(height, width))

for row in range(height):
    y = row * (y_max -  y_min) / height + y_min
    for col in range(width):
        x = col * (x_max -  x_min) / width + x_min
        z_n = complex(x, y)
        conv_val = find_convergence(z_n)
        fractal[row, col] = conv_val

plt.imshow(fractal)
plt.show()



