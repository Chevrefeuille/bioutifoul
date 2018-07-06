import numpy as np
import math
import argparse
from tools import utils as ut


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
    init_poly = ut.compute_regular_polygon(args.poly_size, 10)
    shapes = iterate_polygons(init_poly, args.iterations, args.ratio)
    ut.draw_shapes(shapes)
