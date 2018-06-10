import matplotlib.pyplot as plt
import numpy as np
import math
import argparse
from colour import Color

def compute_regular_polygon(n, size):
    "Compute a regular polygon of the given shape"
    poly = []
    for k in range(n):
        x = math.sqrt(size) * math.cos(2 * k * math.pi / n)
        y = math.sqrt(size) * math.sin(2 * k * math.pi / n)
        P = [x, y]
        poly += [P]
    return np.array(poly)

def draw_shapes(shapes, colors):
    "Draw the given shape"
    for i in range(len(shapes)):
        shape = shapes[i]
        x = [c[0] for c in shape] + [shape[0][0]]
        y = [c[1] for c in shape] + [shape[0][1]]
        plt.plot(x, y, c=colors[i].rgb)
        plt.axes().set_aspect('equal', 'datalim')
    plt.show()

def compute_inside_polygon(poly, r):
    "Compute the polygon inside a given polygon with a rotation ratio of r"
    n = len(poly)
    inside_poly = []
    for i in range(n):
        P = r * poly[i] + (1 - r) * poly[(i+1)%n]
        inside_poly += [P]
    return np.array(inside_poly)


def iterate_polygons(start_polygon, iterations, ratio):
    "Compute the polygons inside a given polygon with a rotation ratio of r"
    shapes =  [start_polygon]
    inside = init_poly
    for i in range(args.iterations):
        inside = compute_inside_polygon(inside, ratio)
        shapes += [inside]
    return shapes


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--poly_size", help="size of the polygon", type=int, default=5)
    parser.add_argument("-n", "--iterations", help="number of iterations", type=int, default=10)
    parser.add_argument("-r", "--ratio", help="rotation ratio", type=float, default=0.2)
    args = parser.parse_args()
    init_poly = compute_regular_polygon(args.poly_size, 10)
    c1 = Color("#000000")
    c2 = Color("#33cccc")
    colors = list(c1.range_to(c2, args.iterations + 1))
    shapes = iterate_polygons(init_poly, args.iterations, args.ratio)
    draw_shapes(shapes, colors)
