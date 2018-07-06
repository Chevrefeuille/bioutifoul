import matplotlib.pyplot as plt
from math import *
from tools import utils as ut

def draw_shape(shape):
    "Draw the given shape"
    x = [c[0] for c in shape]
    y = [c[1] for c in shape]
    plt.plot(x, y)
    plt.axes().set_aspect('equal', 'datalim')
    plt.show()


def create_fractal(shape, iterations):
    "Compute the fractal starting with the given shape"
    fractal = []
    n = len(shape)
    for i in range(n):
        segment = [shape[i], shape[(i+1)%n]]
        fractalized_segment = compute_recursively(segment, iterations, 0)
        fractal += fractalized_segment
    return fractal


def compute_recursively(segment, stop, step):
    "Apply fractal process"
    if step == stop:
        return segment
    xA = (segment[1][0] - segment[0][0]) / 3 + segment[0][0]
    xB = 2 * (segment[1][0] - segment[0][0]) / 3 + segment[0][0]
    yA = (segment[1][1] - segment[0][1]) / 3 + segment[0][1]
    yB = 2 * (segment[1][1] - segment[0][1]) / 3 + segment[0][1]
    xC = cos(-pi / 3) * (xB - xA) - sin(-pi / 3) * (yB - yA) + xA
    yC = sin(-pi / 3) * (xB - xA) + cos(-pi / 3) * (yB - yA) + yA
    part1 = [segment[0], (xA, yA)]
    part2 = [(xA, yA), (xC, yC)]
    part3 = [(xC, yC), (xB, yB)]
    part4 = [(xB, yB), segment[1]]
    return compute_recursively(part1, stop, step + 1) + compute_recursively(part2, stop, step + 1) + \
        compute_recursively(part3, stop, step + 1) + compute_recursively(part4, stop, step + 1)



shape = ut.compute_regular_polygon(3, 10)

fractal = create_fractal(shape, 7)

draw_shape(fractal)